#!/usr/bin/env python3
"""Analyze app reviews for sentiment, themes, and keyword opportunities.

Basic sentiment analysis using keyword matching (no ML dependencies).
Extracts frequent terms, clusters by theme, and reports rating distribution.

Usage:
    python review_analyzer.py --file reviews.json --json
    echo '[{"text": "Great app!", "rating": 5}]' | python review_analyzer.py --stdin --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

POSITIVE_WORDS = {
    "love", "great", "amazing", "awesome", "excellent", "perfect", "best",
    "fantastic", "wonderful", "helpful", "useful", "easy", "beautiful",
    "smooth", "fast", "brilliant", "superb", "intuitive", "recommend",
    "reliable", "simple", "clean", "powerful", "impressed", "solid",
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "horrible", "worst", "hate", "annoying",
    "broken", "crash", "bug", "slow", "laggy", "useless", "frustrating",
    "confusing", "expensive", "scam", "disappointing", "poor", "ugly",
    "complicated", "freeze", "glitch", "error", "fail", "garbage",
    "waste", "unresponsive", "unreliable", "missing",
}

THEME_KEYWORDS = {
    "performance": {"slow", "fast", "laggy", "smooth", "crash", "freeze", "glitch", "responsive", "speed", "loading"},
    "ui_design": {"beautiful", "ugly", "clean", "design", "interface", "layout", "color", "theme", "dark mode", "intuitive"},
    "features": {"feature", "add", "missing", "need", "want", "wish", "option", "setting", "update", "new"},
    "pricing": {"expensive", "cheap", "free", "price", "subscription", "pay", "cost", "worth", "premium", "trial"},
    "bugs": {"bug", "crash", "error", "fix", "broken", "glitch", "issue", "problem", "fail", "not working"},
    "support": {"support", "help", "response", "contact", "customer", "service", "team", "reply"},
}


def classify_sentiment(text: str, rating: int | None = None) -> str:
    """Classify review sentiment as positive, negative, or neutral."""
    words = set(re.findall(r"\b\w+\b", text.lower()))
    pos_count = len(words & POSITIVE_WORDS)
    neg_count = len(words & NEGATIVE_WORDS)

    if rating is not None:
        if rating >= 4:
            pos_count += 2
        elif rating <= 2:
            neg_count += 2

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    return "neutral"


def extract_themes(text: str) -> list[str]:
    """Extract theme labels from review text."""
    words = set(re.findall(r"\b\w+\b", text.lower()))
    themes = []
    for theme, keywords in THEME_KEYWORDS.items():
        if words & keywords:
            themes.append(theme)
    return themes


def extract_frequent_terms(reviews: list[dict], top_n: int = 20) -> list[dict]:
    """Extract most frequent meaningful terms from all reviews."""
    stop_words = {
        "the", "a", "an", "is", "it", "i", "to", "and", "of", "for", "in",
        "on", "my", "this", "that", "with", "but", "not", "so", "very",
        "just", "was", "are", "be", "have", "has", "had", "do", "does",
        "app", "use", "get", "would", "could", "can", "been", "will",
        "its", "you", "me", "we", "they", "their", "there", "from",
        "all", "one", "also", "more", "when", "what", "how", "really",
        "much", "like", "even", "still", "than", "other", "some", "only",
        "about", "out", "up", "if", "or", "no", "as", "at", "by",
    }

    word_counter = Counter()
    for review in reviews:
        text = review.get("text", "")
        words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
        meaningful = [w for w in words if w not in stop_words]
        word_counter.update(meaningful)

    return [{"term": term, "count": count} for term, count in word_counter.most_common(top_n)]


def analyze_reviews(reviews: list[dict]) -> dict:
    """Full review analysis: sentiment, themes, terms, rating distribution."""
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}
    theme_counts = Counter()
    rating_dist = Counter()
    analyzed = []

    for review in reviews:
        text = review.get("text", "")
        rating = review.get("rating")

        sentiment = classify_sentiment(text, rating)
        sentiments[sentiment] += 1

        themes = extract_themes(text)
        theme_counts.update(themes)

        if rating is not None:
            rating_dist[int(rating)] += 1

        analyzed.append({
            "text": text[:200],
            "rating": rating,
            "sentiment": sentiment,
            "themes": themes,
        })

    total = len(reviews)
    return {
        "total_reviews": total,
        "sentiment_distribution": {
            "positive": sentiments["positive"],
            "negative": sentiments["negative"],
            "neutral": sentiments["neutral"],
            "positive_pct": round(sentiments["positive"] / total * 100, 1) if total else 0,
            "negative_pct": round(sentiments["negative"] / total * 100, 1) if total else 0,
        },
        "rating_distribution": {str(k): v for k, v in sorted(rating_dist.items())},
        "average_rating": round(sum(r.get("rating", 0) for r in reviews if r.get("rating")) / max(1, sum(1 for r in reviews if r.get("rating"))), 2),
        "theme_counts": dict(theme_counts.most_common()),
        "frequent_terms": extract_frequent_terms(reviews),
        "sample_reviews": analyzed[:10],
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze app reviews")
    parser.add_argument("--file", help="JSON file with reviews array")
    parser.add_argument("--stdin", action="store_true", help="Read reviews from stdin")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.stdin:
        reviews = json.loads(sys.stdin.read())
    elif args.file:
        with open(args.file) as f:
            reviews = json.load(f)
    else:
        parser.print_help()
        sys.exit(1)

    if not isinstance(reviews, list):
        reviews = [reviews]

    report = analyze_reviews(reviews)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Total reviews: {report['total_reviews']}")
        print(f"Average rating: {report['average_rating']}")
        print(f"Sentiment: {report['sentiment_distribution']['positive_pct']}% positive, {report['sentiment_distribution']['negative_pct']}% negative")
        print()
        print("Themes:")
        for theme, count in report["theme_counts"].items():
            print(f"  {theme}: {count}")
        print()
        print("Top terms:")
        for term_data in report["frequent_terms"][:10]:
            print(f"  {term_data['term']}: {term_data['count']}")


if __name__ == "__main__":
    main()

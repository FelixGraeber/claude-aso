#!/usr/bin/env python3
"""Analyze keyword density and placement across app store metadata fields.

Counts keyword occurrences across all metadata fields, calculates density
for Android descriptions, and reports a placement matrix.

Usage:
    python keyword_density.py --keywords "habit,tracker,daily" --title "Habit Tracker" --description "..." --json
    python keyword_density.py --file metadata.json --keywords "habit,tracker" --json
"""

import argparse
import json
import re
import sys


def count_keyword(text: str, keyword: str) -> int:
    """Count case-insensitive whole-word occurrences of keyword in text."""
    if not text or not keyword:
        return 0
    pattern = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
    return len(pattern.findall(text))


def calculate_density(text: str, keyword: str) -> float:
    """Calculate keyword density as percentage of total words."""
    if not text:
        return 0.0
    words = text.split()
    if not words:
        return 0.0
    occurrences = count_keyword(text, keyword)
    keyword_word_count = len(keyword.split()) * occurrences
    return round(keyword_word_count / len(words) * 100, 2)


def assess_density(density: float) -> str:
    """Assess keyword density for Android descriptions."""
    if density == 0:
        return "missing"
    elif density < 1.0:
        return "under-optimized"
    elif density <= 3.0:
        return "optimal"
    elif density <= 5.0:
        return "over-optimized"
    else:
        return "keyword-stuffing"


def analyze_keywords(keywords: list[str], metadata: dict, platform: str = "android") -> dict:
    """Analyze keyword density and placement across all fields."""
    fields_to_check = {}

    if platform == "ios":
        fields_to_check = {
            "title": metadata.get("title", ""),
            "subtitle": metadata.get("subtitle", ""),
            "keywords_field": metadata.get("keywords", ""),
            "description": metadata.get("description", ""),
        }
    else:
        fields_to_check = {
            "title": metadata.get("title", ""),
            "short_description": metadata.get("short_description", ""),
            "full_description": metadata.get("full_description", "") or metadata.get("description", ""),
        }

    results = []
    for keyword in keywords:
        keyword = keyword.strip()
        if not keyword:
            continue

        placement = {}
        for field_name, field_text in fields_to_check.items():
            count = count_keyword(field_text, keyword)
            density = calculate_density(field_text, keyword) if field_name in ("full_description", "description") else None
            placement[field_name] = {
                "count": count,
                "present": count > 0,
            }
            if density is not None:
                placement[field_name]["density"] = density
                placement[field_name]["assessment"] = assess_density(density)

        in_first_sentence = False
        desc_text = fields_to_check.get("full_description", "") or fields_to_check.get("description", "")
        if desc_text:
            first_sentence = re.split(r"[.!?\n]", desc_text)[0]
            in_first_sentence = count_keyword(first_sentence, keyword) > 0

        total_count = sum(p["count"] for p in placement.values())

        results.append({
            "keyword": keyword,
            "total_mentions": total_count,
            "in_first_sentence": in_first_sentence,
            "placement": placement,
        })

    return {
        "platform": platform,
        "keyword_count": len(results),
        "keywords": results,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze keyword density and placement")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords to analyze")
    parser.add_argument("--platform", choices=["ios", "android"], default="android")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--keywords-field", default="", help="iOS keywords field content")
    parser.add_argument("--short-desc", default="")
    parser.add_argument("--full-desc", default="")
    parser.add_argument("--description", default="")
    parser.add_argument("--file", help="JSON file with metadata")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    keyword_list = [k.strip() for k in args.keywords.split(",") if k.strip()]

    if args.file:
        with open(args.file) as f:
            metadata = json.load(f)
        platform = metadata.get("platform", args.platform)
    else:
        platform = args.platform
        metadata = {
            "title": args.title,
            "subtitle": args.subtitle,
            "keywords": args.keywords_field,
            "short_description": args.short_desc,
            "full_description": args.full_desc,
            "description": args.description,
        }

    report = analyze_keywords(keyword_list, metadata, platform)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Platform: {report['platform']}")
        print(f"Keywords analyzed: {report['keyword_count']}")
        print()
        for kw_data in report["keywords"]:
            print(f"  '{kw_data['keyword']}' — {kw_data['total_mentions']} total mentions")
            print(f"    In first sentence: {'Yes' if kw_data['in_first_sentence'] else 'No'}")
            for field, info in kw_data["placement"].items():
                extra = ""
                if "density" in info:
                    extra = f" | density: {info['density']}% [{info['assessment']}]"
                print(f"    {field}: {info['count']} occurrences{extra}")
            print()


if __name__ == "__main__":
    main()

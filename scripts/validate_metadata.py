#!/usr/bin/env python3
"""Validate app store metadata against character limits.

Checks all metadata fields for both iOS and Android against platform-specific
character limits. Reports per-field pass/fail with character counts.

Usage:
    python validate_metadata.py --platform ios --title "My App" --subtitle "Best App" --keywords "word1,word2" --json
    python validate_metadata.py --platform android --title "My App" --short-desc "Best app ever" --full-desc "..."  --json
    python validate_metadata.py --file metadata.json --json
"""

import argparse
import json
import re
import sys

LIMITS = {
    "ios": {
        "title": 30,
        "subtitle": 30,
        "keywords": 100,
        "description": 4000,
        "promotional_text": 170,
        "whats_new": 4000,
    },
    "android": {
        "title": 50,
        "short_description": 80,
        "full_description": 4000,
        "whats_new": 500,
    },
}


def validate_field(value: str, limit: int) -> dict:
    """Validate a single field against its character limit."""
    length = len(value)
    return {
        "length": length,
        "limit": limit,
        "remaining": limit - length,
        "utilization": round(length / limit * 100, 1) if limit > 0 else 0,
        "pass": length <= limit,
        "over_by": max(0, length - limit),
    }


def validate_ios_keywords(keywords: str) -> list[dict]:
    """iOS-specific keyword field validation."""
    issues = []

    if ", " in keywords:
        issues.append({
            "severity": "critical",
            "message": "Spaces after commas in keywords field. Use 'word1,word2' not 'word1, word2'",
        })

    if keywords and not keywords.endswith(","):
        parts = keywords.split(",")
        for part in parts:
            if part != part.strip():
                issues.append({
                    "severity": "high",
                    "message": f"Leading/trailing spaces in keyword: '{part}'",
                })

    return issues


def check_keyword_duplication(title: str, subtitle: str, keywords: str) -> list[dict]:
    """Check if iOS keywords field duplicates words from title/subtitle."""
    issues = []
    title_words = set(title.lower().split())
    subtitle_words = set(subtitle.lower().split())
    indexed_words = title_words | subtitle_words

    if keywords:
        keyword_list = [k.strip().lower() for k in keywords.split(",") if k.strip()]
        for kw in keyword_list:
            kw_words = set(kw.split())
            overlap = kw_words & indexed_words
            if overlap:
                issues.append({
                    "severity": "high",
                    "message": f"Keyword '{kw}' duplicates word(s) already in title/subtitle: {overlap}. Remove to save space.",
                })

    return issues


def validate_metadata(platform: str, metadata: dict) -> dict:
    """Validate all metadata fields for a platform."""
    limits = LIMITS.get(platform)
    if not limits:
        return {"error": f"Unknown platform: {platform}"}

    report = {
        "platform": platform,
        "fields": {},
        "issues": [],
        "overall_pass": True,
    }

    for field, limit in limits.items():
        value = metadata.get(field, "")
        if value:
            result = validate_field(value, limit)
            report["fields"][field] = result
            if not result["pass"]:
                report["overall_pass"] = False
                report["issues"].append({
                    "severity": "critical",
                    "field": field,
                    "message": f"{field} exceeds limit: {result['length']}/{limit} (over by {result['over_by']})",
                })
            elif result["utilization"] < 80 and value:
                report["issues"].append({
                    "severity": "medium",
                    "field": field,
                    "message": f"{field} underutilized: {result['utilization']}% ({result['length']}/{limit})",
                })

    if platform == "ios":
        kw_issues = validate_ios_keywords(metadata.get("keywords", ""))
        report["issues"].extend(kw_issues)
        if any(i["severity"] == "critical" for i in kw_issues):
            report["overall_pass"] = False

        dup_issues = check_keyword_duplication(
            metadata.get("title", ""),
            metadata.get("subtitle", ""),
            metadata.get("keywords", ""),
        )
        report["issues"].extend(dup_issues)

    return report


def main():
    parser = argparse.ArgumentParser(description="Validate app store metadata")
    parser.add_argument("--platform", choices=["ios", "android"], help="Target platform")
    parser.add_argument("--title", default="", help="App title")
    parser.add_argument("--subtitle", default="", help="iOS subtitle")
    parser.add_argument("--keywords", default="", help="iOS keywords field")
    parser.add_argument("--description", default="", help="iOS description")
    parser.add_argument("--promotional-text", default="", help="iOS promotional text")
    parser.add_argument("--short-desc", default="", help="Android short description")
    parser.add_argument("--full-desc", default="", help="Android full description")
    parser.add_argument("--whats-new", default="", help="What's new text")
    parser.add_argument("--file", help="JSON file with metadata")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            data = json.load(f)
        platform = data.get("platform", args.platform)
        metadata = data
    else:
        platform = args.platform
        if not platform:
            parser.error("--platform required when not using --file")
        metadata = {
            "title": args.title,
            "subtitle": args.subtitle,
            "keywords": args.keywords,
            "description": args.description,
            "promotional_text": args.promotional_text,
            "short_description": args.short_desc,
            "full_description": args.full_desc,
            "whats_new": args.whats_new,
        }

    report = validate_metadata(platform, metadata)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Platform: {report['platform']}")
        print(f"Overall: {'PASS' if report['overall_pass'] else 'FAIL'}")
        print()
        for field, result in report.get("fields", {}).items():
            status = "PASS" if result["pass"] else "FAIL"
            print(f"  {field}: {result['length']}/{result['limit']} ({result['utilization']}%) [{status}]")
        if report.get("issues"):
            print()
            print("Issues:")
            for issue in report["issues"]:
                severity = issue.get("severity", "info").upper()
                print(f"  [{severity}] {issue['message']}")


if __name__ == "__main__":
    main()

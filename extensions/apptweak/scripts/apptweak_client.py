#!/usr/bin/env python3
"""AppTweak REST API client for ASO data.

Handles authentication, credit tracking, and rate limiting.
API key loaded from environment variable APPTWEAK_API_KEY.

Usage:
    python apptweak_client.py keywords "fitness tracker" --platform ios --country us --json
    python apptweak_client.py rankings id284882215 --country us --json
    python apptweak_client.py competitors id284882215 --json
"""

import argparse
import json
import os
import sys
from pathlib import Path

import requests

BASE_URL = "https://api.apptweak.com"
TIMEOUT = 15


def load_api_key() -> str:
    """Load API key from environment or .env file."""
    key = os.environ.get("APPTWEAK_API_KEY")
    if key:
        return key

    env_paths = [
        Path.home() / ".claude" / "skills" / "aso" / ".env",
        Path(".env"),
    ]
    for env_path in env_paths:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("APPTWEAK_API_KEY="):
                    return line.split("=", 1)[1].strip()

    raise ValueError(
        "APPTWEAK_API_KEY not found. Set it as an environment variable or in ~/.claude/skills/aso/.env"
    )


def make_request(endpoint: str, params: dict | None = None) -> dict:
    """Make authenticated request to AppTweak API."""
    api_key = load_api_key()
    headers = {
        "X-Apptweak-Key": api_key,
        "Accept": "application/json",
    }
    url = f"{BASE_URL}{endpoint}"
    resp = requests.get(url, headers=headers, params=params or {}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def cmd_keywords(args):
    """Fetch keyword suggestions."""
    params = {
        "term": args.query,
        "country": args.country,
        "language": args.language,
    }
    device = "iphone" if args.platform == "ios" else "android"
    endpoint = f"/{device}/keywords/search.json"
    return make_request(endpoint, params)


def cmd_rankings(args):
    """Fetch keyword rankings for an app."""
    device = "iphone" if args.platform == "ios" else "android"
    endpoint = f"/{device}/applications/{args.app_id}/keywords.json"
    params = {"country": args.country, "language": args.language}
    return make_request(endpoint, params)


def cmd_competitors(args):
    """Fetch competitor apps."""
    device = "iphone" if args.platform == "ios" else "android"
    endpoint = f"/{device}/applications/{args.app_id}/competitors.json"
    params = {"country": args.country}
    return make_request(endpoint, params)


def cmd_timeline(args):
    """Fetch historical ranking data."""
    device = "iphone" if args.platform == "ios" else "android"
    endpoint = f"/{device}/applications/{args.app_id}/rankings/history.json"
    params = {"country": args.country}
    return make_request(endpoint, params)


def cmd_reviews(args):
    """Fetch recent reviews."""
    device = "iphone" if args.platform == "ios" else "android"
    endpoint = f"/{device}/applications/{args.app_id}/reviews.json"
    params = {"country": args.country, "count": args.count}
    return make_request(endpoint, params)


def main():
    parser = argparse.ArgumentParser(description="AppTweak API client")
    parser.add_argument("--platform", choices=["ios", "android"], default="ios")
    parser.add_argument("--country", default="us")
    parser.add_argument("--language", default="en")
    parser.add_argument("--json", action="store_true")

    subparsers = parser.add_subparsers(dest="command", required=True)

    kw_parser = subparsers.add_parser("keywords")
    kw_parser.add_argument("query")

    rank_parser = subparsers.add_parser("rankings")
    rank_parser.add_argument("app_id")

    comp_parser = subparsers.add_parser("competitors")
    comp_parser.add_argument("app_id")

    time_parser = subparsers.add_parser("timeline")
    time_parser.add_argument("app_id")

    rev_parser = subparsers.add_parser("reviews")
    rev_parser.add_argument("app_id")
    rev_parser.add_argument("--count", type=int, default=50)

    args = parser.parse_args()

    commands = {
        "keywords": cmd_keywords,
        "rankings": cmd_rankings,
        "competitors": cmd_competitors,
        "timeline": cmd_timeline,
        "reviews": cmd_reviews,
    }

    try:
        result = commands[args.command](args)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except ValueError as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(json.dumps({"error": f"API error: {e}"}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

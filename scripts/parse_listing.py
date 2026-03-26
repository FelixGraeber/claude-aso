#!/usr/bin/env python3
"""Parse app store listing HTML into structured ASO data.

Parses Google Play HTML pages into structured JSON. iOS data from iTunes API
is already structured, so this primarily handles Android parsing.

Usage:
    python parse_listing.py <html-file> --json
    cat listing.html | python parse_listing.py --stdin --json
"""

import argparse
import json
import re
import sys

from bs4 import BeautifulSoup


def parse_google_play_html(html: str) -> dict:
    """Extract structured data from Google Play listing HTML."""
    soup = BeautifulSoup(html, "lxml")

    result = {
        "platform": "android",
        "title": "",
        "short_description": "",
        "full_description": "",
        "developer": "",
        "category": "",
        "rating": None,
        "rating_count": None,
        "screenshots": [],
        "icon_url": "",
        "version": "",
        "last_updated": "",
        "size": "",
        "installs": "",
        "content_rating": "",
        "whats_new": "",
        "price": "",
        "in_app_purchases": False,
    }

    title_el = soup.find("h1")
    if title_el:
        result["title"] = title_el.get_text(strip=True)

    dev_el = soup.find("a", href=re.compile(r"/store/apps/dev"))
    if dev_el:
        result["developer"] = dev_el.get_text(strip=True)

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            ld = json.loads(script.string or "")
            if isinstance(ld, dict):
                if ld.get("@type") == "SoftwareApplication":
                    result["title"] = result["title"] or ld.get("name", "")
                    result["full_description"] = ld.get("description", "")
                    result["rating"] = ld.get("aggregateRating", {}).get("ratingValue")
                    result["rating_count"] = ld.get("aggregateRating", {}).get("ratingCount")
                    result["category"] = ld.get("applicationCategory", "")
                    if "offers" in ld:
                        result["price"] = ld["offers"].get("price", "")
                    result["icon_url"] = ld.get("image", "")
        except (json.JSONDecodeError, TypeError):
            continue

    screenshot_imgs = soup.find_all("img", src=re.compile(r"play-lh\.googleusercontent\.com"))
    for img in screenshot_imgs:
        src = img.get("src", "") or img.get("data-src", "")
        if src and "screenshot" in (img.get("alt", "").lower() + src.lower()):
            result["screenshots"].append(src)

    if not result["screenshots"]:
        for img in screenshot_imgs:
            src = img.get("src", "") or img.get("data-src", "")
            srcset = img.get("srcset", "")
            if src and ("=w" in src or "=w" in srcset):
                result["screenshots"].append(src)

    meta_sections = soup.find_all("div", class_=re.compile(r"content"))
    for section in meta_sections:
        text = section.get_text(strip=True)
        if "What's new" in text or "what's new" in text.lower():
            next_div = section.find_next_sibling("div")
            if next_div:
                result["whats_new"] = next_div.get_text(strip=True)

    for div in soup.find_all("div"):
        text = div.get_text(strip=True)
        if re.match(r"^\d+[KMB]?\+? downloads?$", text, re.IGNORECASE):
            result["installs"] = text
            break
        if "Contains ads" in text:
            pass
        if "In-app purchases" in text:
            result["in_app_purchases"] = True

    return result


def main():
    parser = argparse.ArgumentParser(description="Parse app store listing HTML")
    parser.add_argument("file", nargs="?", help="HTML file to parse")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.stdin:
        html = sys.stdin.read()
    elif args.file:
        with open(args.file) as f:
            html = f.read()
    else:
        parser.print_help()
        sys.exit(1)

    result = parse_google_play_html(html)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for key, value in result.items():
            if isinstance(value, list):
                print(f"{key}: {len(value)} items")
            elif isinstance(value, str) and len(value) > 200:
                print(f"{key}: {value[:200]}...")
            else:
                print(f"{key}: {value}")


if __name__ == "__main__":
    main()

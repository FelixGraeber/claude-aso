#!/usr/bin/env python3
"""Fetch app store listing data by app ID or URL.

Supports iOS App Store and Google Play. Auto-detects platform from input format.

Usage:
    python fetch_listing.py <app-id-or-url> [--country CODE] [--json]

Examples:
    python fetch_listing.py id284882215 --country us --json
    python fetch_listing.py com.whatsapp --json
    python fetch_listing.py "https://apps.apple.com/app/id284882215"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from urllib.parse import urlparse

import requests

try:
    from scripts.network_security import validate_remote_url
except ModuleNotFoundError:
    from network_security import validate_remote_url


TIMEOUT = 15
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


ALLOWED_STORE_HOSTS = {
    "apps.apple.com",
    "itunes.apple.com",
    "play.google.com",
}


def detect_platform(identifier: str) -> tuple[str, str]:
    """Return (platform, app_id) from an identifier string."""
    identifier = identifier.strip()
    parsed = urlparse(identifier)

    if parsed.scheme and parsed.netloc:
        validate_remote_url(identifier, allowed_hosts=ALLOWED_STORE_HOSTS)

    if parsed.hostname == "apps.apple.com":
        match = re.search(r"id(\d+)", identifier)
        if match:
            return "ios", f"id{match.group(1)}"
        raise ValueError(f"Cannot extract iOS app ID from URL: {identifier}")

    if parsed.hostname == "play.google.com":
        match = re.search(r"id=([a-zA-Z0-9_.]+)", identifier)
        if match:
            return "android", match.group(1)
        raise ValueError(f"Cannot extract Android package name from URL: {identifier}")

    if re.match(r"^id\d+$", identifier):
        return "ios", identifier

    if re.match(r"^\d+$", identifier):
        return "ios", f"id{identifier}"

    if re.match(r"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)+$", identifier):
        return "android", identifier

    raise ValueError(
        f"Cannot detect platform from '{identifier}'. "
        "Use iOS format (id123456789) or Android format (com.example.app)"
    )
def fetch_ios_listing(app_id: str, country: str = "us") -> dict:
    """Fetch iOS app listing via iTunes Lookup API + web scraping."""
    numeric_id = app_id.replace("id", "")
    lookup_url = f"https://itunes.apple.com/lookup?id={numeric_id}&country={country}"

    resp = requests.get(lookup_url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
    resp.raise_for_status()
    data = resp.json()

    if data.get("resultCount", 0) == 0:
        return {"error": f"iOS app not found: {app_id}", "platform": "ios", "app_id": app_id}

    result = data["results"][0]

    return {
        "platform": "ios",
        "app_id": app_id,
        "numeric_id": numeric_id,
        "title": result.get("trackName", ""),
        "subtitle": "",
        "description": result.get("description", ""),
        "keywords": "",
        "rating": result.get("averageUserRating"),
        "rating_count": result.get("userRatingCount"),
        "review_count": result.get("userRatingCountForCurrentVersion"),
        "screenshots": result.get("screenshotUrls", []),
        "ipad_screenshots": result.get("ipadScreenshotUrls", []),
        "icon_url": result.get("artworkUrl512", result.get("artworkUrl100", "")),
        "category": result.get("primaryGenreName", ""),
        "category_id": result.get("primaryGenreId"),
        "developer": result.get("artistName", ""),
        "developer_url": result.get("artistViewUrl", ""),
        "price": result.get("price", 0),
        "currency": result.get("currency", "USD"),
        "version": result.get("version", ""),
        "release_date": result.get("releaseDate", ""),
        "current_release_date": result.get("currentVersionReleaseDate", ""),
        "minimum_os": result.get("minimumOsVersion", ""),
        "size_bytes": result.get("fileSizeBytes"),
        "content_rating": result.get("contentAdvisoryRating", ""),
        "languages": result.get("languageCodesISO2A", []),
        "url": result.get("trackViewUrl", ""),
        "bundle_id": result.get("bundleId", ""),
        "seller": result.get("sellerName", ""),
        "in_app_purchases": [
            iap.get("label", "") for iap in result.get("inAppPurchases", [])
        ] if "inAppPurchases" in result else [],
        "genres": result.get("genres", []),
        "release_notes": result.get("releaseNotes", ""),
        "error": None,
    }


def fetch_android_listing(package_name: str, country: str = "us") -> dict:
    """Fetch Android app listing by scraping Google Play web page."""
    url = f"https://play.google.com/store/apps/details?id={package_name}&hl=en&gl={country}"
    validate_remote_url(url, allowed_hosts={"play.google.com"})

    resp = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
    if resp.status_code == 404:
        return {"error": f"Android app not found: {package_name}", "platform": "android", "app_id": package_name}
    resp.raise_for_status()

    return {
        "platform": "android",
        "app_id": package_name,
        "url": url,
        "html": resp.text,
        "status_code": resp.status_code,
        "error": None,
    }


def fetch_listing(identifier: str, country: str = "us") -> dict:
    """Fetch listing data for any app identifier."""
    platform, app_id = detect_platform(identifier)

    if platform == "ios":
        return fetch_ios_listing(app_id, country)
    else:
        return fetch_android_listing(app_id, country)


def main():
    parser = argparse.ArgumentParser(description="Fetch app store listing data")
    parser.add_argument("identifier", help="App ID, package name, or store URL")
    parser.add_argument("--country", default="us", help="Country code (default: us)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    try:
        result = fetch_listing(args.identifier, args.country)
    except ValueError as e:
        result = {"error": str(e)}
    except requests.RequestException as e:
        result = {"error": f"HTTP error: {e}"}

    if args.json:
        output = {k: v for k, v in result.items() if k != "html"}
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        if result.get("error"):
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)
        for key, value in result.items():
            if key == "html":
                print(f"{key}: [{len(value)} chars]")
            elif isinstance(value, list):
                print(f"{key}: {', '.join(str(v) for v in value[:5])}{'...' if len(value) > 5 else ''}")
            else:
                print(f"{key}: {value}")


if __name__ == "__main__":
    main()

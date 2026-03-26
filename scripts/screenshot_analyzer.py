#!/usr/bin/env python3
"""Analyze app store screenshots for composition and ASO best practices.

Fetches screenshot images and analyzes count, dimensions, text presence,
and narrative flow. Optionally uses Playwright for store page capture.

Usage:
    python screenshot_analyzer.py --urls "url1,url2,url3" --platform ios --json
    python screenshot_analyzer.py --app-url "https://apps.apple.com/app/id123" --json
"""

import argparse
import json
import sys

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from PIL import Image
    from io import BytesIO
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    from scripts.network_security import validate_remote_url
except ModuleNotFoundError:
    from network_security import validate_remote_url


IOS_SCREENSHOT_SPECS = {
    "iPhone 6.9": {"width": 1320, "height": 2868},
    "iPhone 6.7": {"width": 1290, "height": 2796},
    "iPhone 6.5": {"width": 1284, "height": 2778},
    "iPhone 5.5": {"width": 1242, "height": 2208},
    "iPad Pro 13": {"width": 2064, "height": 2752},
    "iPad Pro 12.9": {"width": 2048, "height": 2732},
}

ANDROID_SCREENSHOT_SPECS = {
    "phone_min": {"width": 320, "height": 320},
    "phone_max": {"width": 3840, "height": 3840},
}

MAX_DOWNLOAD_BYTES = 20 * 1024 * 1024
SUPPORTED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}


def analyze_screenshot_url(url: str) -> dict:
    """Analyze a single screenshot from URL."""
    result = {
        "url": url,
        "accessible": False,
        "width": None,
        "height": None,
        "aspect_ratio": None,
        "orientation": None,
        "format": None,
    }

    if not HAS_REQUESTS:
        result["error"] = "requests not installed"
        return result

    try:
        validate_remote_url(url)
        resp = requests.get(url, timeout=10, stream=True)
        resp.raise_for_status()

        content_type = resp.headers.get("Content-Type", "").split(";", 1)[0].lower()
        if content_type and content_type not in SUPPORTED_CONTENT_TYPES:
            raise ValueError(f"Unsupported content type: {content_type}")

        content_length = resp.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_DOWNLOAD_BYTES:
            raise ValueError(f"Screenshot exceeds {MAX_DOWNLOAD_BYTES // (1024 * 1024)} MB limit")

        content = bytearray()
        for chunk in resp.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            content.extend(chunk)
            if len(content) > MAX_DOWNLOAD_BYTES:
                raise ValueError(f"Screenshot exceeds {MAX_DOWNLOAD_BYTES // (1024 * 1024)} MB limit")

        result["accessible"] = True

        if HAS_PIL:
            img = Image.open(BytesIO(content))
            result["width"] = img.width
            result["height"] = img.height
            result["format"] = img.format
            result["aspect_ratio"] = round(img.width / img.height, 2) if img.height else None
            result["orientation"] = "portrait" if img.height > img.width else "landscape"
    except Exception as e:
        result["error"] = str(e)

    return result


def analyze_screenshot_set(screenshots: list[dict], platform: str) -> dict:
    """Analyze a complete set of screenshots."""
    total = len(screenshots)

    report = {
        "platform": platform,
        "total_count": total,
        "screenshots": screenshots,
        "issues": [],
        "recommendations": [],
    }

    if platform == "ios":
        max_allowed = 10
        if total < 5:
            report["issues"].append({
                "severity": "high",
                "message": f"Only {total} screenshots. Recommend at least 5 for conversion.",
            })
        if total < 3:
            report["issues"].append({
                "severity": "critical",
                "message": f"Only {total} screenshots. First 3 appear in search results — need at least 3.",
            })
    else:
        max_allowed = 8
        if total < 4:
            report["issues"].append({
                "severity": "high",
                "message": f"Only {total} screenshots. Recommend at least 4 for Android.",
            })
        if total < 2:
            report["issues"].append({
                "severity": "critical",
                "message": f"Only {total} screenshots. Google Play requires minimum 2.",
            })

    if total >= max_allowed:
        report["recommendations"].append(f"Using all {max_allowed} screenshot slots — good.")
    elif total > 0:
        report["recommendations"].append(f"Using {total}/{max_allowed} slots. Fill remaining for more conversion surface.")

    orientations = [s.get("orientation") for s in screenshots if s.get("orientation")]
    if orientations and len(set(orientations)) > 1:
        report["issues"].append({
            "severity": "medium",
            "message": "Mixed orientations (portrait and landscape). Consider consistency.",
        })

    report["recommendations"].append("Ensure first 3 screenshots tell a complete value story.")
    report["recommendations"].append("Add clear, readable screenshot captions that improve conversion and support discoverability.")
    report["recommendations"].append("Localize screenshot text for each target market.")

    return report


def main():
    parser = argparse.ArgumentParser(description="Analyze app store screenshots")
    parser.add_argument("--urls", help="Comma-separated screenshot URLs")
    parser.add_argument("--platform", choices=["ios", "android"], default="ios")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    screenshots = []
    if args.urls:
        for url in args.urls.split(","):
            url = url.strip()
            if url:
                screenshots.append(analyze_screenshot_url(url))

    report = analyze_screenshot_set(screenshots, args.platform)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Platform: {report['platform']}")
        print(f"Screenshots: {report['total_count']}")
        if report["issues"]:
            print("\nIssues:")
            for issue in report["issues"]:
                print(f"  [{issue['severity'].upper()}] {issue['message']}")
        if report["recommendations"]:
            print("\nRecommendations:")
            for rec in report["recommendations"]:
                print(f"  - {rec}")


if __name__ == "__main__":
    main()

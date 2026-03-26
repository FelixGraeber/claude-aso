#!/usr/bin/env python3
"""Auto-detect local app project and extract metadata.

Scans the current directory for iOS/Android project markers and Fastlane
metadata. Returns structured JSON with detected platform, metadata, and paths.

Usage:
    python detect_project.py [--path DIR] --json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def find_files(root: Path, patterns: list[str]) -> dict[str, Path]:
    """Find first match for each glob pattern."""
    found = {}
    for pattern in patterns:
        matches = sorted(root.glob(pattern))
        if matches:
            found[pattern] = matches[0]
    return found


def read_text_file(path: Path) -> str:
    """Read a text file, return empty string if missing."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except (FileNotFoundError, UnicodeDecodeError):
        return ""


def detect_fastlane_ios(root: Path) -> dict | None:
    """Detect and parse Fastlane iOS metadata."""
    meta_dir = root / "fastlane" / "metadata"
    if not meta_dir.is_dir():
        return None

    android_dir = meta_dir / "android"
    locales = []
    for item in sorted(meta_dir.iterdir()):
        if item.is_dir() and item != android_dir and re.match(r"^[a-z]{2}(-[A-Z]{2})?$", item.name):
            locales.append(item.name)

    if not locales:
        return None

    metadata_by_locale = {}
    for locale in locales:
        locale_dir = meta_dir / locale
        metadata_by_locale[locale] = {
            "name": read_text_file(locale_dir / "name.txt"),
            "subtitle": read_text_file(locale_dir / "subtitle.txt"),
            "keywords": read_text_file(locale_dir / "keywords.txt"),
            "description": read_text_file(locale_dir / "description.txt"),
            "promotional_text": read_text_file(locale_dir / "promotional_text.txt"),
            "release_notes": read_text_file(locale_dir / "release_notes.txt"),
        }

    primary = metadata_by_locale.get(locales[0], {})
    return {
        "source": "fastlane",
        "platform": "ios",
        "metadata_path": str(meta_dir),
        "locales": locales,
        "primary_locale": locales[0],
        "title": primary.get("name", ""),
        "subtitle": primary.get("subtitle", ""),
        "keywords": primary.get("keywords", ""),
        "description": primary.get("description", ""),
        "promotional_text": primary.get("promotional_text", ""),
        "release_notes": primary.get("release_notes", ""),
        "metadata_by_locale": metadata_by_locale,
    }


def detect_fastlane_android(root: Path) -> dict | None:
    """Detect and parse Fastlane Android metadata."""
    meta_dir = root / "fastlane" / "metadata" / "android"
    if not meta_dir.is_dir():
        return None

    locales = []
    for item in sorted(meta_dir.iterdir()):
        if item.is_dir() and re.match(r"^[a-z]{2}(-[A-Z]{2})?$", item.name):
            locales.append(item.name)

    if not locales:
        return None

    metadata_by_locale = {}
    for locale in locales:
        locale_dir = meta_dir / locale
        metadata_by_locale[locale] = {
            "title": read_text_file(locale_dir / "title.txt"),
            "short_description": read_text_file(locale_dir / "short_description.txt"),
            "full_description": read_text_file(locale_dir / "full_description.txt"),
        }

    primary = metadata_by_locale.get(locales[0], {})
    return {
        "source": "fastlane",
        "platform": "android",
        "metadata_path": str(meta_dir),
        "locales": locales,
        "primary_locale": locales[0],
        "title": primary.get("title", ""),
        "short_description": primary.get("short_description", ""),
        "full_description": primary.get("full_description", ""),
        "metadata_by_locale": metadata_by_locale,
    }


def detect_xcode_project(root: Path) -> dict | None:
    """Detect Xcode project and extract bundle ID."""
    xcodeproj = find_files(root, ["*.xcodeproj", "**/*.xcodeproj"])
    if not xcodeproj:
        return None

    proj_path = list(xcodeproj.values())[0]
    pbxproj = proj_path / "project.pbxproj"

    bundle_id = ""
    if pbxproj.exists():
        content = pbxproj.read_text(errors="replace")
        match = re.search(r'PRODUCT_BUNDLE_IDENTIFIER\s*=\s*"?([^";]+)', content)
        if match:
            bundle_id = match.group(1).strip()

    info_plist = find_files(root, ["Info.plist", "*/Info.plist", "*/*/Info.plist"])
    app_name = ""
    if info_plist:
        plist_path = list(info_plist.values())[0]
        content = plist_path.read_text(errors="replace")
        match = re.search(r"<key>CFBundleDisplayName</key>\s*<string>([^<]+)", content)
        if not match:
            match = re.search(r"<key>CFBundleName</key>\s*<string>([^<]+)", content)
        if match:
            app_name = match.group(1).strip()

    return {
        "source": "xcode",
        "platform": "ios",
        "project_path": str(proj_path),
        "bundle_id": bundle_id,
        "app_name": app_name,
    }


def detect_android_project(root: Path) -> dict | None:
    """Detect Android/Gradle project and extract package name."""
    gradle_files = find_files(root, [
        "app/build.gradle",
        "app/build.gradle.kts",
        "build.gradle",
        "build.gradle.kts",
    ])
    if not gradle_files:
        return None

    gradle_path = list(gradle_files.values())[0]
    content = gradle_path.read_text(errors="replace")

    app_id = ""
    match = re.search(r'applicationId\s*[=\s]*"([^"]+)"', content)
    if not match:
        match = re.search(r"applicationId\s*[=\s]*'([^']+)'", content)
    if match:
        app_id = match.group(1)

    manifest = find_files(root, [
        "app/src/main/AndroidManifest.xml",
        "src/main/AndroidManifest.xml",
    ])
    if not app_id and manifest:
        manifest_path = list(manifest.values())[0]
        manifest_content = manifest_path.read_text(errors="replace")
        match = re.search(r'package="([^"]+)"', manifest_content)
        if match:
            app_id = match.group(1)

    app_name = ""
    strings_xml = find_files(root, [
        "app/src/main/res/values/strings.xml",
        "res/values/strings.xml",
    ])
    if strings_xml:
        strings_path = list(strings_xml.values())[0]
        strings_content = strings_path.read_text(errors="replace")
        match = re.search(r'<string name="app_name">([^<]+)', strings_content)
        if match:
            app_name = match.group(1)

    return {
        "source": "gradle",
        "platform": "android",
        "gradle_path": str(gradle_path),
        "app_id": app_id,
        "app_name": app_name,
    }


def detect_project(root: Path) -> dict:
    """Auto-detect app project type and extract available metadata."""
    root = root.resolve()
    result = {
        "project_root": str(root),
        "detected": False,
        "platforms": [],
        "sources": [],
        "fastlane_ios": None,
        "fastlane_android": None,
        "xcode": None,
        "android": None,
    }

    fl_ios = detect_fastlane_ios(root)
    if fl_ios:
        result["fastlane_ios"] = fl_ios
        result["sources"].append("fastlane-ios")
        if "ios" not in result["platforms"]:
            result["platforms"].append("ios")

    fl_android = detect_fastlane_android(root)
    if fl_android:
        result["fastlane_android"] = fl_android
        result["sources"].append("fastlane-android")
        if "android" not in result["platforms"]:
            result["platforms"].append("android")

    xcode = detect_xcode_project(root)
    if xcode:
        result["xcode"] = xcode
        result["sources"].append("xcode")
        if "ios" not in result["platforms"]:
            result["platforms"].append("ios")

    android = detect_android_project(root)
    if android:
        result["android"] = android
        result["sources"].append("gradle")
        if "android" not in result["platforms"]:
            result["platforms"].append("android")

    result["detected"] = len(result["sources"]) > 0

    if result["fastlane_ios"]:
        result["primary_source"] = "fastlane-ios"
    elif result["fastlane_android"]:
        result["primary_source"] = "fastlane-android"
    elif result["xcode"]:
        result["primary_source"] = "xcode"
    elif result["android"]:
        result["primary_source"] = "gradle"
    else:
        result["primary_source"] = None

    return result


def main():
    parser = argparse.ArgumentParser(description="Auto-detect local app project")
    parser.add_argument("--path", default=".", help="Project root directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = detect_project(Path(args.path))

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        if not result["detected"]:
            print("No app project detected in current directory.")
            print("Looked for: Fastlane metadata, .xcodeproj, build.gradle, AndroidManifest.xml")
            sys.exit(1)

        print(f"Project root: {result['project_root']}")
        print(f"Platforms: {', '.join(result['platforms'])}")
        print(f"Sources: {', '.join(result['sources'])}")
        print(f"Primary source: {result['primary_source']}")

        if result["fastlane_ios"]:
            fl = result["fastlane_ios"]
            print(f"\nFastlane iOS metadata ({len(fl['locales'])} locales):")
            print(f"  Name: {fl['title']}")
            print(f"  Subtitle: {fl['subtitle']}")
            print(f"  Keywords: {fl['keywords'][:80]}...")
            print(f"  Locales: {', '.join(fl['locales'])}")

        if result["fastlane_android"]:
            fl = result["fastlane_android"]
            print(f"\nFastlane Android metadata ({len(fl['locales'])} locales):")
            print(f"  Title: {fl['title']}")
            print(f"  Short description: {fl['short_description']}")
            print(f"  Locales: {', '.join(fl['locales'])}")

        if result["xcode"]:
            xc = result["xcode"]
            print(f"\nXcode project: {xc['project_path']}")
            print(f"  Bundle ID: {xc['bundle_id']}")
            print(f"  App name: {xc['app_name']}")

        if result["android"]:
            an = result["android"]
            print(f"\nAndroid project: {an['gradle_path']}")
            print(f"  Application ID: {an['app_id']}")
            print(f"  App name: {an['app_name']}")


if __name__ == "__main__":
    main()

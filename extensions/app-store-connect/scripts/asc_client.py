#!/usr/bin/env python3
"""App Store Connect API client.

JWT-based authentication for Apple's App Store Connect API.
Fetches metadata, reviews, ratings, and version info.

Usage:
    python asc_client.py metadata <app-id> --json
    python asc_client.py reviews <app-id> --json
    python asc_client.py ratings <app-id> --json
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

try:
    import jwt
    HAS_JWT = True
except ImportError:
    HAS_JWT = False

BASE_URL = "https://api.appstoreconnect.apple.com/v1"
TIMEOUT = 15


def load_credentials() -> dict:
    """Load ASC credentials from environment or .env file."""
    creds = {
        "key_id": os.environ.get("ASC_KEY_ID"),
        "issuer_id": os.environ.get("ASC_ISSUER_ID"),
        "key_path": os.environ.get("ASC_KEY_PATH"),
    }

    if not all(creds.values()):
        env_paths = [
            Path.home() / ".claude" / "skills" / "aso" / ".env",
            Path(".env"),
        ]
        for env_path in env_paths:
            if env_path.exists():
                for line in env_path.read_text().splitlines():
                    if "=" in line:
                        key, val = line.split("=", 1)
                        key = key.strip()
                        val = val.strip()
                        if key == "ASC_KEY_ID" and not creds["key_id"]:
                            creds["key_id"] = val
                        elif key == "ASC_ISSUER_ID" and not creds["issuer_id"]:
                            creds["issuer_id"] = val
                        elif key == "ASC_KEY_PATH" and not creds["key_path"]:
                            creds["key_path"] = val

    missing = [k for k, v in creds.items() if not v]
    if missing:
        raise ValueError(f"Missing ASC credentials: {', '.join(missing)}")

    return creds


def generate_token(creds: dict) -> str:
    """Generate JWT token for App Store Connect API."""
    if not HAS_JWT:
        raise ImportError("PyJWT required. Install with: pip install PyJWT")

    key_path = Path(creds["key_path"]).expanduser()
    private_key = key_path.read_text()

    now = int(time.time())
    payload = {
        "iss": creds["issuer_id"],
        "iat": now,
        "exp": now + 1200,
        "aud": "appstoreconnect-v1",
    }
    headers = {
        "alg": "ES256",
        "kid": creds["key_id"],
        "typ": "JWT",
    }
    return jwt.encode(payload, private_key, algorithm="ES256", headers=headers)


def make_request(endpoint: str, params: dict | None = None) -> dict:
    """Make authenticated request to App Store Connect API."""
    creds = load_credentials()
    token = generate_token(creds)
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    url = f"{BASE_URL}{endpoint}"
    resp = requests.get(url, headers=headers, params=params or {}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def cmd_metadata(args):
    """Fetch app metadata (localizations)."""
    endpoint = f"/apps/{args.app_id}/appInfos"
    data = make_request(endpoint, {"include": "appInfoLocalizations"})
    return data


def cmd_reviews(args):
    """Fetch customer reviews."""
    endpoint = f"/apps/{args.app_id}/customerReviews"
    params = {"sort": "-createdDate", "limit": args.count}
    return make_request(endpoint, params)


def cmd_ratings(args):
    """Fetch rating data."""
    endpoint = f"/apps/{args.app_id}"
    params = {"fields[apps]": "name,bundleId"}
    return make_request(endpoint, params)


def cmd_versions(args):
    """Fetch app versions."""
    endpoint = f"/apps/{args.app_id}/appStoreVersions"
    params = {"limit": 10}
    return make_request(endpoint, params)


def main():
    parser = argparse.ArgumentParser(description="App Store Connect API client")
    parser.add_argument("--json", action="store_true")

    subparsers = parser.add_subparsers(dest="command", required=True)

    meta_parser = subparsers.add_parser("metadata")
    meta_parser.add_argument("app_id")

    rev_parser = subparsers.add_parser("reviews")
    rev_parser.add_argument("app_id")
    rev_parser.add_argument("--count", type=int, default=50)

    rate_parser = subparsers.add_parser("ratings")
    rate_parser.add_argument("app_id")

    ver_parser = subparsers.add_parser("versions")
    ver_parser.add_argument("app_id")

    args = parser.parse_args()

    commands = {
        "metadata": cmd_metadata,
        "reviews": cmd_reviews,
        "ratings": cmd_ratings,
        "versions": cmd_versions,
    }

    try:
        result = commands[args.command](args)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (ValueError, ImportError) as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(json.dumps({"error": f"API error: {e}"}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

"""Shared metadata limits and policy-facing constants."""

IOS_METADATA_LIMITS = {
    "title": 30,
    "subtitle": 30,
    "keywords": 100,
    "description": 4000,
    "promotional_text": 170,
    "whats_new": 4000,
}

ANDROID_METADATA_LIMITS = {
    "title": 30,
    "short_description": 80,
    "full_description": 4000,
    "whats_new": 500,
}

LIMITS = {
    "ios": IOS_METADATA_LIMITS,
    "android": ANDROID_METADATA_LIMITS,
}

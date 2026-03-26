---
name: aso-asc
description: >
  Apple App Store Connect API integration. Fetch and manage iOS app metadata,
  reviews, ratings, and version info directly from App Store Connect.
  Requires API key. Triggers on: "app store connect", "asc".
user-invokable: true
argument-hint: "<command> <app-id> [--locale LOCALE]"
---

# ASO App Store Connect — Apple API Integration

Direct access to App Store Connect for iOS metadata management.

## Commands

| Command | What it does |
|---------|-------------|
| `/aso asc metadata <app-id>` | Fetch current metadata (name, subtitle, keywords, description) |
| `/aso asc keywords <app-id>` | Fetch keywords field per locale |
| `/aso asc reviews <app-id>` | Fetch customer reviews |
| `/aso asc ratings <app-id>` | Fetch rating data and distribution |
| `/aso asc versions <app-id>` | List app versions and submission states |

## Usage

```bash
uv run python scripts/asc_client.py <command> <app-id> --json
```

## Authentication
JWT-based auth using credentials from `~/.claude/skills/aso/.env`:
- ASC_KEY_ID
- ASC_ISSUER_ID
- ASC_KEY_PATH (path to .p8 file)

## Available Tools
Read, Bash, Write, Glob, Grep

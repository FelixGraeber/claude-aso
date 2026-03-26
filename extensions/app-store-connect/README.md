# App Store Connect Extension for Skill ASO

Integrates Apple's App Store Connect API for direct metadata management, review fetching, and analytics access.

## Prerequisites
- Apple Developer Program membership
- App Store Connect API key (from Users and Access > Integrations > Keys)
- Key ID, Issuer ID, and private key (.p8 file)

## Installation

```bash
bash extensions/app-store-connect/install.sh
```

This will:
1. Prompt for Key ID, Issuer ID, and .p8 key file path
2. Store credentials in `~/.claude/skills/aso/.env`
3. Install the ASC skill and agent
4. Install Python dependencies (PyJWT)

## Commands

| Command | Description |
|---------|-------------|
| `/aso asc metadata <app-id>` | Fetch current metadata from App Store Connect |
| `/aso asc keywords <app-id>` | Fetch current keywords field |
| `/aso asc reviews <app-id>` | Fetch customer reviews |
| `/aso asc ratings <app-id>` | Fetch rating data and distribution |
| `/aso asc versions <app-id>` | List app versions and their states |

## Authentication

Uses JWT-based authentication per Apple's requirements:
- Key ID and Issuer ID stored in `.env`
- Private key (.p8) file path stored in `.env`
- Tokens are generated per request (20-minute expiry)

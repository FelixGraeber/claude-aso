# AppTweak Extension for Skill ASO

Integrates AppTweak's REST API for live keyword data, rankings, and competitor intelligence.

## Prerequisites
- AppTweak account with API access (Pro plan or higher)
- API key from https://www.apptweak.io/documentation

## Installation

```bash
bash extensions/apptweak/install.sh
```

This will:
1. Prompt for your AppTweak API key
2. Store it in the ASO env file (`$ASO_ENV_FILE` or the default install location)
3. Install the AppTweak skill and agent
4. Install Python dependencies

## Commands

| Command | Description | Credits |
|---------|-------------|---------|
| `/aso apptweak keywords <seed>` | Live keyword suggestions with volume + difficulty | ~5 per query |
| `/aso apptweak rankings <app-id>` | Current keyword rankings for an app | ~10 per app |
| `/aso apptweak competitors <app-id>` | Competitor apps with overlap scores | ~10 per app |
| `/aso apptweak timeline <app-id>` | Ranking history over time | ~15 per app |
| `/aso apptweak reviews <app-id>` | Review analysis with sentiment | ~10 per app |

## API Key Management

Prefer the `APPTWEAK_API_KEY` environment variable. The installer can also write it to the ASO env file with `0600` permissions.
Monthly credit budget: 25,000 credits on Pro plan.

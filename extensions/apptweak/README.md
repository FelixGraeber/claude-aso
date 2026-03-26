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
2. Store it in `~/.claude/skills/aso/.env`
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

The API key is stored in `~/.claude/skills/aso/.env` as `APPTWEAK_API_KEY`.
Monthly credit budget: 25,000 credits on Pro plan.

## Credit Usage

Monitor your credit usage. Each API call consumes credits. The client tracks
cumulative usage per session and warns when approaching limits.

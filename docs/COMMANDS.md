# Commands Reference

## Core Commands

| Command | Description |
|---------|-------------|
| `/aso` | Show command table and help |
| `/aso audit <app-id>` | Full listing audit (7-9 parallel agents, health score) |
| `/aso keywords <seeds>` | Keyword research and placement strategy |
| `/aso metadata <app-id>` | Metadata field analysis and rewrite suggestions |
| `/aso visuals <app-id>` | Screenshot, icon, and video analysis |
| `/aso reviews <app-id>` | Review sentiment, themes, response strategy |
| `/aso competitors <app-id>` | Competitor comparison and gap analysis |
| `/aso localization <app-id>` | Multi-locale optimization strategy |
| `/aso ab-testing <app-id>` | A/B test design (iOS PPO / Android experiments) |
| `/aso technical <app-id>` | Technical health (size, crashes, updates) |
| `/aso conversion <app-id>` | Conversion rate optimization |
| `/aso plan <category>` | Strategic ASO roadmap |
| `/aso launch <app-id>` | Pre-launch and launch day strategy |
| `/aso seasonal <app-id>` | Seasonal keyword opportunities |

## Extension Commands

### AppTweak (requires API key)
| Command | Description |
|---------|-------------|
| `/aso apptweak keywords <seed>` | Live keyword suggestions with volume |
| `/aso apptweak rankings <app-id>` | Current keyword rankings |
| `/aso apptweak competitors <app-id>` | Similar apps with overlap scores |
| `/aso apptweak timeline <app-id>` | Historical ranking data |
| `/aso apptweak reviews <app-id>` | Reviews with sentiment |

### App Store Connect (requires API key)
| Command | Description |
|---------|-------------|
| `/aso asc metadata <app-id>` | Fetch metadata from ASC |
| `/aso asc reviews <app-id>` | Fetch customer reviews |
| `/aso asc ratings <app-id>` | Fetch rating distribution |
| `/aso asc versions <app-id>` | List app versions |

## App ID Formats

| Platform | Format | Example |
|----------|--------|---------|
| iOS | Numeric ID | `id284882215` |
| iOS | Store URL | `https://apps.apple.com/app/id284882215` |
| Android | Package name | `com.whatsapp` |
| Android | Store URL | `https://play.google.com/store/apps/details?id=com.whatsapp` |

# Claude ASO — App Store Optimization for Claude Code

Comprehensive App Store Optimization skill for Claude Code. Analyzes iOS App Store and Google Play listings using parallel subagents across 7 categories, producing an ASO Health Score (0-100) and prioritized action plan.

Inspired by [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) — adapted from SEO website analysis to ASO mobile app optimization with the same parallel subagent architecture.

## Features

- **13 specialized sub-skills**: keywords, metadata, visuals, reviews, competitors, localization, A/B testing, technical, conversion, planning, launch, seasonal
- **9 parallel subagents**: full audit spawns agents simultaneously for fast analysis
- **Platform-aware**: auto-detects iOS vs Android, applies correct rules (character limits, indexing behavior, A/B testing capabilities)
- **Quality gates**: prevents bad recommendations (no keyword stuffing, respects char limits, iOS description not indexed)
- **Extension system**: optional AppTweak and App Store Connect API integrations

## Quick Start

```bash
git clone https://github.com/felixgraeber/claude-aso.git
cd claude-aso
bash install.sh
```

Then in Claude Code:

```
/aso audit id284882215          # Full iOS audit
/aso audit com.whatsapp         # Full Android audit
/aso keywords "habit tracker"   # Keyword research
/aso metadata id284882215       # Metadata optimization
```

## Commands

| Command | Description |
|---------|-------------|
| `/aso audit <app-id>` | Full listing audit with health score |
| `/aso keywords <seeds>` | Keyword research and placement strategy |
| `/aso metadata <app-id>` | Metadata field analysis and rewrites |
| `/aso visuals <app-id>` | Screenshot, icon, video analysis |
| `/aso reviews <app-id>` | Review sentiment and response strategy |
| `/aso competitors <app-id>` | Competitor gap analysis |
| `/aso localization <app-id>` | Multi-locale optimization |
| `/aso ab-testing <app-id>` | A/B test design |
| `/aso technical <app-id>` | Technical health check |
| `/aso conversion <app-id>` | Conversion rate optimization |
| `/aso plan <category>` | Strategic ASO roadmap |
| `/aso launch <app-id>` | Launch strategy |
| `/aso seasonal <app-id>` | Seasonal keyword calendar |

## Architecture

```
aso/SKILL.md              Main orchestrator (entry point)
skills/aso-*/SKILL.md     13 specialized sub-skills
agents/aso-*.md           9 parallel subagents
references/*.md           Platform specs, quality gates
scripts/*.py              Python utilities (fetch, parse, validate)
extensions/               Optional API integrations
```

## Scoring

The audit produces a weighted ASO Health Score:

| Category | Weight |
|----------|--------|
| Keywords | 20% |
| Metadata | 20% |
| Visuals | 15% |
| Reviews | 15% |
| Competitive | 10% |
| Technical | 10% |
| Conversion | 10% |

## Extensions

| Extension | Purpose | Requires |
|-----------|---------|----------|
| AppTweak | Live keyword data, rankings, competitors | API key ($69+/mo) |
| App Store Connect | Direct Apple API for metadata and reviews | Developer account |

## Requirements

- Python 3.12+
- Claude Code CLI
- Optional: Playwright for visual analysis

## License

MIT

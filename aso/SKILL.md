---
name: aso
description: >
  Comprehensive App Store Optimization for iOS and Android apps. Full listing
  audits with parallel subagents, keyword research, metadata optimization,
  visual asset analysis, review management, competitor intelligence,
  localization, A/B testing, technical ASO, and conversion rate optimization.
user-invokable: true
argument-hint: "[command] [app-id-or-url]"
---

# ASO — App Store Optimization Skill

Comprehensive ASO analysis for iOS App Store and Google Play apps. Platform-aware: automatically detects iOS vs Android from the app ID format and applies platform-specific rules.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/aso audit <app-id>` | Full listing audit — 7-9 parallel agents, health score 0-100 |
| `/aso keywords <seeds>` | Keyword research — difficulty, volume, placement strategy |
| `/aso metadata <app-id>` | Metadata optimization — per-field scoring, rewrite suggestions |
| `/aso visuals <app-id>` | Visual assets — screenshots, icon, preview video analysis |
| `/aso reviews <app-id>` | Reviews — sentiment analysis, response templates, keyword extraction |
| `/aso competitors <app-id>` | Competitor analysis — keyword gaps, metadata comparison |
| `/aso localization <app-id>` | Localization — per-locale keyword research, cultural adaptation |
| `/aso ab-testing <app-id>` | A/B testing — iOS PPO / Android experiment design |
| `/aso technical <app-id>` | Technical ASO — Android Vitals, app size, crashes, update cadence |
| `/aso conversion <app-id>` | Conversion — install rate benchmarking, first-impression audit |
| `/aso plan <category>` | Strategic plan — 4-phase roadmap with category templates |
| `/aso launch <app-id>` | Launch — pre-launch checklist, soft launch, day-1 strategy |
| `/aso seasonal <app-id>` | Seasonal — trending keyword opportunities, holiday calendar |

## Platform Detection

Automatically detect platform from input:
- **iOS**: Numeric ID (`id284882215`), Apple App Store URL (`apps.apple.com/...`)
- **Android**: Package name (`com.whatsapp`), Google Play URL (`play.google.com/store/apps/details?id=...`)
- **Both**: When user provides both IDs or asks for cross-platform analysis
- **Ambiguous**: Ask user to specify platform

## App ID Formats

```
iOS:     id284882215  OR  https://apps.apple.com/app/id284882215
Android: com.whatsapp  OR  https://play.google.com/store/apps/details?id=com.whatsapp
```

## Category Detection

After fetching listing data, classify the app:
- **Gaming**: game category, IAP patterns, leaderboards
- **SaaS/Productivity**: subscription model, enterprise features, workspace tools
- **Health/Fitness**: HealthKit/Google Fit, workout terms, wellness
- **E-commerce**: shopping category, payment, cart, product catalog
- **Social**: messaging, feed, connections, sharing
- **Fintech**: banking, payments, investment, crypto
- **Other**: education, travel, utilities, news, entertainment

Category informs which plan templates and benchmarks to apply.

## Audit Orchestration Flow

When running `/aso audit <app-id>`:

### Step 1 — Data Fetch (sequential)
```bash
uv run python scripts/fetch_listing.py <app-id> --country us --json
```
Parse the result to get structured listing data.

### Step 2 — Category Detection (sequential)
Classify app from listing metadata. Load category-specific benchmarks.

### Step 3 — Parallel Subagent Dispatch
Spawn these agents in parallel using the Agent tool:

| Agent | Focus |
|-------|-------|
| `aso-keywords` | Keyword coverage in current metadata |
| `aso-metadata` | Field quality, char limits, keyword placement |
| `aso-visuals` | Screenshot count, narrative, icon, video |
| `aso-reviews` | Sentiment distribution, themes, response rate |
| `aso-competitors` | Top 5 competitor comparison |
| `aso-technical` | App size, update recency, stability signals |
| `aso-conversion` | First-impression elements, CRO signals |
| `aso-localization` | *(conditional: if multi-locale detected)* |

Each agent receives the parsed listing JSON and returns a structured report with scores and findings.

### Step 4 — Score Aggregation (sequential)

Calculate weighted **ASO Health Score (0-100)**:

| Category | Weight |
|----------|--------|
| Keyword Optimization | 20% |
| Metadata Quality | 20% |
| Visual Assets | 15% |
| Reviews & Ratings | 15% |
| Competitive Position | 10% |
| Technical Health | 10% |
| Conversion Signals | 10% |

### Step 5 — Report Generation (sequential)

Generate two files:

**ASO-AUDIT-REPORT.md**:
- Executive summary (score, platform, category, top 3 issues, quick wins)
- Per-category detailed findings
- Platform-specific notes

**ASO-ACTION-PLAN.md**:
- **Critical**: Character limit violations, missing keywords in title, <3.5 star rating
- **High**: Poor screenshot narrative, no preview video, low review velocity
- **Medium**: Localization gaps, A/B test opportunities, secondary keyword misses
- **Low**: Seasonal optimization, minor copy improvements, icon A/B test

## Quality Gates

These rules are ALWAYS enforced — never recommend violations:

1. **Character limits are absolute** — violations are always Critical priority
2. **iOS description is NOT indexed** — never optimize it for keywords, only conversion
3. **iOS keyword field**: comma-separated, no spaces after commas, no duplication with title/subtitle
4. **Android description**: primary keyword in first sentence, 2-3% density for primary keyword
5. **No keyword stuffing**: >3 repetitions of same keyword in any field = stuffing
6. **Review health**: <3.5 stars = Critical, <4.0 = High priority
7. **Update recency**: >90 days since last update = warning signal

## Platform Metadata Quick Reference

### iOS App Store

| Field | Limit | Indexed? | Notes |
|-------|-------|----------|-------|
| App Name | 30 chars | YES (high weight) | Primary keyword here |
| Subtitle | 30 chars | YES | Secondary keywords |
| Keywords | 100 chars | YES | Hidden, comma-separated |
| Description | 4,000 chars | NO | Conversion copy only |
| Promotional Text | 170 chars | NO | No review needed to update |
| What's New | 4,000 chars | NO | Update messaging |

### Google Play

| Field | Limit | Indexed? | Notes |
|-------|-------|----------|-------|
| Title | 50 chars | YES (high weight) | More space than iOS |
| Short Description | 80 chars | YES | Visible in some views |
| Full Description | 4,000 chars | YES | Keyword density matters |
| Developer Name | variable | YES (low) | Branding |
| What's New | 500 chars | NO | Shorter than iOS |

## Available Tools

All skills can use: Read, Bash, Write, Glob, Grep, WebFetch, Agent

## Reference Files

Load on demand from `references/`:
- `ios-metadata-specs.md` — Full iOS field specs and indexing rules
- `android-metadata-specs.md` — Full Android field specs and indexing rules
- `keyword-placement-rules.md` — Keyword weight by field position per platform
- `visual-asset-specs.md` — Screenshot/icon/video dimensions per device
- `quality-gates.md` — Thresholds, hard stops, density limits
- `category-taxonomy.md` — iOS/Android category IDs and mapping

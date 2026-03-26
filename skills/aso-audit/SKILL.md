---
name: aso-audit
description: >
  Full app listing audit with parallel subagent delegation. Scores listing
  across 7 categories (0-100), flags problems, generates prioritized action plan.
  Works in local mode (auto-detect Fastlane/Xcode/Gradle metadata) or remote
  mode (fetch live listing by app ID). Triggers on: "audit", "full ASO check",
  "analyze my app", "listing health check".
user-invokable: true
argument-hint: "[app-id-or-url] [--country CODE]"
---

# ASO Audit — Full Listing Analysis

Comprehensive app listing audit that spawns 7-9 specialized subagents in parallel.

## Modes

| Mode | Trigger | Data Source |
|------|---------|-------------|
| **Local** | `/aso audit` (no args) | Fastlane metadata, Xcode project, Gradle project |
| **Remote** | `/aso audit <app-id>` | Live App Store / Google Play listing |
| **Compare** | `/aso audit --compare <app-id>` | Both local + remote, shows diff |

## Process

### Step 1: Get Metadata (sequential)

**If no app ID provided (local mode):**
```bash
uv run python scripts/detect_project.py --json
```
This scans the working directory for Fastlane metadata (`fastlane/metadata/`), Xcode project (`.xcodeproj`), or Gradle project (`app/build.gradle`). If Fastlane metadata is found, all store fields are available. If only Xcode/Gradle is found, extract the app/bundle ID and offer to fetch the live listing.

**If app ID provided (remote mode):**
```bash
uv run python scripts/fetch_listing.py <app-id> --country us --json
```
For Android, also pipe through `parse_listing.py`.

**If --compare flag (compare mode):**
Run both detect_project.py AND fetch_listing.py, then diff the results.

### Step 2: Platform & Category Detection (sequential)
- Detect iOS vs Android from project type or app ID format
- Classify category from listing metadata (Gaming, SaaS, Health, E-commerce, Social, Fintech, Other)
- Load category-specific benchmarks

### Step 3: Parallel Subagent Dispatch
Spawn ALL of these agents simultaneously using the Agent tool:

| Agent | Input | Focus |
|-------|-------|-------|
| aso-keywords | listing JSON | Keyword coverage in title, subtitle/short desc, keywords field, description |
| aso-metadata | listing JSON | Field quality, character limits, utilization, keyword placement |
| aso-visuals | listing JSON | Screenshot count, narrative flow, icon, preview video |
| aso-reviews | listing JSON | Rating, sentiment distribution, themes, response rate |
| aso-competitors | listing JSON + category | Top 5 competitors, keyword gaps, metadata comparison |
| aso-technical | listing JSON | App size, update recency, stability, category fit |
| aso-conversion | listing JSON | First-impression elements, screenshot narrative, CRO |

Conditional agents (spawn if relevant):
| aso-localization | listing JSON | If app supports >1 locale |

Each agent returns: `{ score: 0-100, findings: [...], recommendations: [...] }`

### Step 4: Score Aggregation (sequential)

| Category | Weight | Source Agent |
|----------|--------|-------------|
| Keyword Optimization | 20% | aso-keywords |
| Metadata Quality | 20% | aso-metadata |
| Visual Assets | 15% | aso-visuals |
| Reviews & Ratings | 15% | aso-reviews |
| Competitive Position | 10% | aso-competitors |
| Technical Health | 10% | aso-technical |
| Conversion Signals | 10% | aso-conversion |

**ASO Health Score** = weighted average, rounded to integer.

### Step 5: Report Generation (sequential)

Generate two files in the current directory:

**ASO-AUDIT-REPORT.md:**
```markdown
# ASO Audit Report: [App Name]
## Executive Summary
- ASO Health Score: XX/100
- Platform: iOS / Android
- Category: [detected]
- Top 3 Issues: [...]
- Quick Wins: [...]

## Keyword Optimization (XX/100)
[agent findings]

## Metadata Quality (XX/100)
[agent findings]

## Visual Assets (XX/100)
[agent findings]

## Reviews & Ratings (XX/100)
[agent findings]

## Competitive Position (XX/100)
[agent findings]

## Technical Health (XX/100)
[agent findings]

## Conversion Signals (XX/100)
[agent findings]
```

**ASO-ACTION-PLAN.md:**
```markdown
# ASO Action Plan: [App Name]

## Critical (Fix Immediately)
- [ ] [issue + specific recommendation]

## High Priority (This Week)
- [ ] [issue + specific recommendation]

## Medium Priority (This Month)
- [ ] [issue + specific recommendation]

## Low Priority (Backlog)
- [ ] [issue + specific recommendation]
```

## Available Tools
Read, Bash, Write, Glob, Grep, WebFetch, Agent

## Error Handling
- App not found → report error, suggest checking ID format
- Partial data → run available agents, note missing data in report
- Agent timeout → report partial results, mark category as "incomplete"

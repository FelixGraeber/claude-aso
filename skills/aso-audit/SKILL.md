---
name: aso-audit
description: >
  Full app listing audit with parallel subagent delegation. Scores listing
  across 7 categories (0-100), flags problems, generates prioritized action plan.
  Triggers on: "audit", "full ASO check", "analyze my app", "listing health check".
user-invokable: true
argument-hint: "<app-id-or-url> [--country CODE]"
---

# ASO Audit — Full Listing Analysis

Comprehensive app listing audit that spawns 7-9 specialized subagents in parallel.

## Process

### Step 1: Fetch & Parse (sequential)
```bash
uv run python scripts/fetch_listing.py <app-id> --country us --json
```
Parse result into structured listing data. If Android, also run:
```bash
uv run python scripts/parse_listing.py --stdin --json
```

### Step 2: Platform & Category Detection (sequential)
- Detect iOS vs Android from app ID format
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

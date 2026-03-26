# Architecture

## 3-Layer Model

```
Layer 1: Main Skill (aso/SKILL.md)
  → Entry point, routing, platform detection, scoring methodology

Layer 2: Sub-Skills (skills/aso-*/SKILL.md)
  → 14 specialized skills, independently invocable

Layer 3: Agents (agents/aso-*.md)
  → 10 specialist agents
```

## Data Flow

```
User: /aso audit <app-id>
  │
  ├── fetch_listing.py → Structured JSON
  ├── parse_listing.py → Enriched JSON (Android)
  │
  ├── [Parallel] Agent: aso-keywords
  ├── [Parallel] Agent: aso-metadata
  ├── [Parallel] Agent: aso-visuals
  ├── [Parallel] Agent: aso-reviews
  ├── [Parallel] Agent: aso-competitors
  ├── [Parallel] Agent: aso-technical
  ├── [Parallel] Agent: aso-conversion
  ├── [Conditional] Agent: aso-localization
  │
  ├── [Sequential] Agent: aso-compliance
  │
  └── Aggregate → ASO Health Score → Reports
```

## Platform Detection

Auto-detect from input format:
- `id\d+` or `apps.apple.com` → iOS
- `com.example.app` or `play.google.com` → Android

## Scoring

Weighted average of 7 category scores (0-100 each):
- Keywords: 20%, Metadata: 20%, Visuals: 15%, Reviews: 15%
- Competitive: 10%, Technical: 10%, Conversion: 10%

## Extension System

Optional API integrations in `extensions/`:
- `apptweak/` — Live keyword data, rankings, competitors
- `app-store-connect/` — Direct Apple API access (metadata, reviews)

Each extension has: install script, skill, agent, Python client.

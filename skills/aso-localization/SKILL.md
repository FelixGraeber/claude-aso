---
name: aso-localization
description: >
  Multi-locale ASO optimization. Per-locale keyword research, cultural adaptation,
  cross-localization strategy, CJK-specific considerations.
  Triggers on: "localization", "localize", "translation", "multi-locale", "international".
user-invokable: true
argument-hint: "<app-id> [--locales en,de,ja,es]"
---

# ASO Localization — International Optimization

## Capabilities
1. Current locale coverage assessment
2. Market prioritization by size and competition
3. Per-locale keyword research (keywords don't translate 1:1)
4. Cross-localization strategy (iOS locale inheritance)
5. Cultural adaptation recommendations
6. CJK character width considerations

## Key Principle

**Localization ≠ Translation.** Each locale needs independent keyword research. A direct translation of English keywords often misses how users actually search in that language.

Impact: Adding a local language → up to 128% more downloads, 26% revenue increase per country.

## Process

1. Fetch listing and identify current locales
2. Assess market opportunity per locale:
   - Market size (app downloads in region)
   - Competition density
   - Revenue potential
3. Per-locale keyword research (adapted, not translated)
4. Generate localized metadata recommendations
5. Identify cross-localization opportunities

## Platform Locale Support

### iOS
- 35+ localizations available
- Each locale: independent App Name, Subtitle, Keywords, Description, Screenshots
- Cross-localization: Apple indexes related locales (e.g., en-US → en-GB)
- Keyword field per locale: independent 100-char allocation

### Android
- 75+ localizations
- Custom store listings: up to 50 per app
- Target by country OR language
- Full description indexed per locale independently

## CJK Considerations (Chinese, Japanese, Korean)
- Characters convey more meaning → fewer chars needed for same concept
- Keyword density calculations differ (word segmentation)
- Character width: CJK chars take ~2x visual space
- Search behavior: shorter queries, different word boundaries

## Output Format

```markdown
# Localization Report: [App Name]

## Current Coverage
[X locales supported, list]

## Market Priority Matrix
| Locale | Market Size | Competition | Revenue Potential | Priority |
|--------|------------|-------------|-------------------|----------|

## Per-Locale Keyword Maps
### [Locale]
- Title: "[localized title]"
- Keywords: [locale-specific keywords]
- Notes: [cultural adaptation notes]

## Cross-Localization Opportunities
[iOS locale inheritance strategies]

## Recommended Localization Roadmap
Phase 1: [top 3-5 locales]
Phase 2: [next 5-10 locales]
Phase 3: [remaining high-value locales]
```

## Available Tools
Read, Bash, Write, Glob, Grep, WebFetch

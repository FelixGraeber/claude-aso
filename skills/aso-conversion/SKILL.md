---
name: aso-conversion
description: >
  Conversion rate optimization for app store listings. Analyzes first-impression
  elements, screenshot narrative, social proof signals, and psychology-based
  messaging to maximize install rate.
  Triggers on: "conversion", "install rate", "CRO", "conversion rate".
user-invokable: true
argument-hint: "<app-id>"
---

# ASO Conversion — Conversion Rate Optimization

## Capabilities
1. First-impression audit (what users see before tapping "Read More")
2. Screenshot narrative arc analysis
3. Social proof signal assessment
4. Psychology-based messaging evaluation
5. Category conversion benchmarking
6. Conversion funnel analysis (impression → page view → install)

## Conversion Benchmarks (2024-2025)

| Platform | Average Conversion |
|----------|--------------------|
| iOS App Store | ~25% |
| Google Play | ~27% |

Category variance is significant (10-115%+ range).

## First-Impression Elements

What users see WITHOUT scrolling or tapping "Read More":

### iOS Search Results
- App icon
- App name
- Subtitle
- Rating (stars + count)
- First 3 screenshots (CRITICAL)
- Price / "Get" button

### Google Play Search Results
- App icon
- App title
- Developer name
- Rating (stars)
- Price / "Install" button

### Full Listing (Above Fold)
- Icon + name + developer
- Rating + review count
- Screenshots (scrollable)
- Short description (Android) / first 3 lines of description (iOS)

## Scoring (0-100)

| Factor | Weight | What to assess |
|--------|--------|---------------|
| First 3 screenshots | 25% | Clear value prop, hook, visual quality |
| Title clarity | 20% | Does it explain what the app does? |
| Rating strength | 20% | ≥4.5 = strong, ≥4.0 = acceptable, <4.0 = hurting |
| Social proof | 15% | Review count, awards, editor's choice, download count |
| Subtitle/short desc | 10% | Benefit-oriented, compelling |
| Icon appeal | 10% | Distinctive, professional, recognizable |

## Psychology Triggers to Evaluate

1. **Social proof**: High rating, large review count, "X million users"
2. **Authority**: Awards, press mentions, editor's choice badges
3. **Loss aversion**: "Don't miss out", limited features in free tier
4. **Specificity**: Concrete numbers ("Track 50+ habits") vs vague claims
5. **Benefit framing**: Focus on outcomes, not features

## Output Format

```markdown
# Conversion Analysis: [App Name]

## Score: XX/100

## First-Impression Audit
| Element | Current | Assessment | Recommendation |
|---------|---------|-----------|----------------|
| Icon | [description] | [score] | [improvement] |
| Title | "[current]" | [score] | [improvement] |
| Subtitle/Short Desc | "[current]" | [score] | [improvement] |
| Rating | X.X (Y reviews) | [score] | [improvement] |
| Screenshot 1 | [description] | [score] | [improvement] |
| Screenshot 2 | [description] | [score] | [improvement] |
| Screenshot 3 | [description] | [score] | [improvement] |

## Screenshot Narrative Analysis
[Flow assessment: hook → features → proof]

## Social Proof Signals
[What's present, what's missing]

## Psychology Triggers
[Which are used, which could be added]

## Quick Wins
[Highest-impact, lowest-effort changes]
```

## Available Tools
Read, Bash, Write, Glob, Grep

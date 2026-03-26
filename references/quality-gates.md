# ASO Quality Gates

Hard rules enforced across all analyses. Never recommend violations.

## Critical (Must Fix)

| Rule | Threshold | Applies To |
|------|-----------|------------|
| Character limit exceeded | Any field over limit | Both platforms |
| No primary keyword in title | Title missing target keyword | Both platforms |
| Rating below 3.5 stars | <3.5 average | Both platforms |
| iOS keywords with spaces after commas | `word1, word2` instead of `word1,word2` | iOS only |
| iOS keyword field duplicates title/subtitle words | Wasted keyword space | iOS only |
| Keyword stuffing | >3% density for any single keyword | Android |
| iOS description optimized for keywords | Description is NOT indexed | iOS only |
| Competitor brand names in keywords | Policy violation → rejection risk | Both platforms |

## High Priority

| Rule | Threshold | Applies To |
|------|-----------|------------|
| Rating below 4.0 stars | 3.5-4.0 average | Both platforms |
| <5 screenshots | Missing conversion opportunity | Both platforms |
| No app preview video | Missing engagement driver | Both platforms |
| >90 days since last update | Stale app signal | Both platforms |
| <80% character utilization | Unused keyword space | Both platforms |
| No keywords in first sentence of description | Weak opening | Android only |
| Primary keyword density <1% | Under-optimized | Android only |
| <100 total reviews | Low credibility signal | Both platforms |

## Medium Priority

| Rule | Threshold | Applies To |
|------|-----------|------------|
| <3 locales supported | Missing international traffic | Both platforms |
| No A/B tests running | Missing optimization opportunity | Both platforms |
| Screenshot text not localized | Generic screenshots across locales | Both platforms |
| No promotional text set | Missing quick-update opportunity | iOS only |
| No feature graphic | Missing branding opportunity | Android only |
| App size >100MB | Download friction | Both platforms |

## Low Priority

| Rule | Threshold | Applies To |
|------|-----------|------------|
| No seasonal keyword rotation | Missing trending opportunities | Both platforms |
| Icon not A/B tested | Unknown if optimal | Both platforms |
| App size >200MB | High download friction | Both platforms |
| No in-app events | Missing engagement surface | iOS only |

## Scoring Thresholds

| Score Range | Label | Color |
|-------------|-------|-------|
| 90-100 | Excellent | Green |
| 75-89 | Good | Light Green |
| 60-74 | Needs Work | Yellow |
| 40-59 | Poor | Orange |
| 0-39 | Critical | Red |

## Keyword Density Bands (Android Full Description)

| Density | Assessment |
|---------|-----------|
| 0% | Missing — keyword not present |
| 0.1-0.9% | Under-optimized |
| 1-3% | Optimal range |
| 3.1-5% | Over-optimized — risk of penalty |
| >5% | Keyword stuffing — likely penalty |

---
name: aso-technical
description: >
  Technical ASO factors analysis. Android Vitals, app size, crash rates,
  update frequency, category selection, content rating impact.
  Triggers on: "technical ASO", "Android Vitals", "app size", "crash rate", "update frequency".
user-invokable: true
argument-hint: "<app-id>"
---

# ASO Technical — Technical Health Analysis

## Capabilities
1. App size analysis (download and install)
2. Android Vitals assessment (crash rate, ANR rate)
3. Update frequency and recency evaluation
4. Category selection validation
5. Content rating impact assessment
6. Device compatibility review

## Technical Ranking Factors (2025-2026)

| Factor | Platform | Impact |
|--------|----------|--------|
| Download volume & velocity | Both | Highest |
| User retention & engagement | Both | Very High |
| Ratings & reviews | Both | High |
| Android Vitals (crashes, ANR) | Android | High |
| Metadata quality | Both | High |
| Update frequency | Both | Medium |
| App size | Both | Medium |
| Revenue performance | Both | Low-Medium |

## Scoring (0-100)

### App Size
| Size (Download) | Score | Assessment |
|-----------------|-------|-----------|
| <50MB | 100 | Excellent |
| 50-100MB | 80 | Good |
| 100-200MB | 50 | Warning |
| >200MB | 20 | Critical — high download friction |

### Android Vitals
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Crash rate | <1.09% | 1.09-2% | >2% |
| ANR rate | <0.47% | 0.47-1% | >1% |

### Update Recency
| Days Since Update | Score | Assessment |
|-------------------|-------|-----------|
| <14 | 100 | Very fresh |
| 14-30 | 90 | Fresh |
| 30-60 | 70 | Acceptable |
| 60-90 | 40 | Getting stale |
| >90 | 10 | Stale — hurting rankings |

### Category Fit
- Category matches app functionality: +30
- Secondary category set (iOS): +10
- Tags properly configured (Android): +10

## Output Format

```markdown
# Technical ASO Report: [App Name]

## Score: XX/100

## App Size
- Download size: [X MB]
- Assessment: [Good/Warning/Critical]
- Recommendation: [if needed]

## Stability (Android Vitals)
- Crash rate: [X%] — [assessment]
- ANR rate: [X%] — [assessment]

## Update Cadence
- Last update: [date]
- Days ago: [X]
- Update frequency: [weekly/biweekly/monthly/sporadic]
- Assessment: [Fresh/Acceptable/Stale]

## Category Selection
- Primary: [category] — [fit assessment]
- Secondary: [category or "not set"]

## Recommendations
[Prioritized technical improvements]
```

## Available Tools
Read, Bash, Write, Glob, Grep

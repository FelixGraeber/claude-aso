---
name: aso-competitors
description: >
  Competitor analysis and gap finding. Compares keyword targeting, metadata
  strategy, visual approaches, ratings, and identifies differentiation opportunities.
  Triggers on: "competitors", "competitor analysis", "gap analysis", "benchmark".
user-invokable: true
argument-hint: "<app-id> [--competitors id1,id2,id3]"
---

# ASO Competitors — Competitive Intelligence

## Capabilities
1. Identify top competitors (same category, similar keywords)
2. Metadata comparison matrix (titles, subtitles, descriptions)
3. Keyword gap analysis (keywords they rank for, you don't)
4. Visual strategy comparison (screenshot styles, icon patterns)
5. Rating and review count benchmarking
6. Differentiation opportunity identification

## Process

1. Fetch target app listing
2. Identify 5-10 competitors:
   - Same category apps
   - Apps ranking for target keywords
   - User-specified competitor IDs
3. Fetch competitor listings
4. Build comparison matrices
5. Identify gaps and opportunities

## Analysis Dimensions

### Metadata Comparison
| Field | Your App | Competitor 1 | Competitor 2 | ... |
|-------|----------|-------------|-------------|-----|
| Title | | | | |
| Subtitle/Short Desc | | | | |
| Keyword themes | | | | |
| Description approach | | | | |

### Keyword Gap Analysis
- **Your unique keywords**: Keywords you target that competitors don't
- **Competitor unique keywords**: Keywords they target that you miss → OPPORTUNITIES
- **Shared keywords**: Keywords everyone targets → HIGH competition
- **Untapped keywords**: Keywords none of you target → EXPLORE

### Rating Benchmarking
| Metric | Your App | Category Avg | Top Competitor |
|--------|----------|-------------|----------------|
| Rating | | | |
| Review count | | | |
| Recent trend | | | |

### Visual Strategy
- Screenshot narrative style comparison
- Icon design patterns in category
- Video presence/absence

## Output Format

```markdown
# Competitor Analysis: [App Name]

## Competitor Set
[List of identified competitors with brief description]

## Metadata Comparison Matrix
[Side-by-side comparison table]

## Keyword Gap Report
### Keywords You're Missing (Opportunities)
| Keyword | Competitors Using | Est. Competition |
|---------|------------------|-----------------|

### Your Unique Keywords (Differentiators)
| Keyword | Notes |

## Rating Comparison
[Benchmarking table]

## Differentiation Opportunities
[Prioritized list of ways to stand out]
```

## Available Tools
Read, Bash, Write, Glob, Grep, WebFetch

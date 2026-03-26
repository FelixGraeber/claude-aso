---
name: aso-keywords
description: >
  Keyword research and strategy for iOS and Android apps. Analyzes keyword
  difficulty, search volume, relevance, and optimal placement across metadata
  fields. Platform-aware indexing rules.
  Triggers on: "keywords", "keyword research", "keyword strategy", "search terms".
user-invokable: true
argument-hint: "<seed-keywords> [--platform ios|android] [--app-id ID]"
---

# ASO Keywords — Keyword Research & Strategy

## Capabilities
1. Seed keyword expansion (synonyms, long-tail, related terms)
2. Platform-specific placement strategy (iOS fields vs Android fields)
3. Keyword density analysis for Android descriptions
4. Keyword deduplication check for iOS (title/subtitle vs keywords field)
5. Competitor keyword gap analysis (when competitor IDs provided)

## Process

### If seed keywords provided:
1. Expand seed keywords into primary, secondary, and long-tail categories
2. For each keyword, assess:
   - **Relevance**: How closely it matches app functionality (1-10)
   - **Competition**: Estimated difficulty based on top results (low/medium/high)
   - **Intent**: Navigational, informational, or transactional
3. Generate placement map per platform

### If app ID provided:
1. Fetch current listing metadata
2. Extract existing keywords from all indexed fields
3. Identify gaps and opportunities
4. Run `scripts/keyword_density.py` for Android density analysis
5. Run `scripts/validate_metadata.py` to check iOS keyword field format

## Platform-Specific Rules

### iOS Placement Strategy
| Priority | Field | Action |
|----------|-------|--------|
| 1 | App Name (30 chars) | Primary keyword, must be here |
| 2 | Subtitle (30 chars) | Secondary keyword phrase |
| 3 | Keywords field (100 chars) | All remaining keywords, NO duplicates from name/subtitle |

- Keywords field: comma-separated, NO spaces after commas
- Singular forms only (Apple matches plurals automatically)
- Do NOT include: articles, prepositions, your app name, competitor names
- Description is NOT indexed — never optimize it for keywords

### Android Placement Strategy
| Priority | Field | Action |
|----------|-------|--------|
| 1 | Title (50 chars) | Primary keyword, natural language |
| 2 | Short Description (80 chars) | Secondary keyword + benefit |
| 3 | Full Description (4000 chars) | All keywords, 2-3% density for primary |

- Primary keyword in first sentence of description
- 2-3% density for primary, 1-2% for secondary
- >3% density = keyword stuffing risk

## Output Format

```markdown
# Keyword Strategy: [App Name / Seeds]

## Primary Keywords (high volume, high relevance)
| Keyword | Relevance | Competition | Intent | Placement |
|---------|-----------|-------------|--------|-----------|

## Secondary Keywords (medium volume)
| Keyword | Relevance | Competition | Intent | Placement |

## Long-Tail Keywords (specific, lower competition)
| Keyword | Relevance | Competition | Intent | Placement |

## iOS Metadata Map
- Title: "[suggested title with primary keyword]"
- Subtitle: "[suggested subtitle]"
- Keywords: "[comma,separated,keywords,field]"

## Android Metadata Map
- Title: "[suggested title]"
- Short Description: "[suggested short description]"
- Description keywords: [list with target density per keyword]
```

## Available Tools
Read, Bash, Write, Glob, Grep, WebFetch

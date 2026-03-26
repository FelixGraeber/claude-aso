---
name: aso-metadata
description: >
  Metadata optimization for iOS and Android app listings. Per-field scoring,
  character limit validation, keyword placement analysis, and rewrite suggestions.
  Triggers on: "metadata", "title", "subtitle", "description", "optimize listing".
user-invokable: true
argument-hint: "<app-id> [--platform ios|android]"
---

# ASO Metadata — Metadata Optimization

## Capabilities
1. Per-field character limit validation
2. Keyword presence and placement scoring
3. Conversion copy quality assessment
4. Optimized metadata rewrite suggestions (3 variants)
5. Cross-field consistency check

## Process

1. Fetch current metadata: `uv run python scripts/fetch_listing.py <app-id> --json`
2. Validate limits: `uv run python scripts/validate_metadata.py --file listing.json --json`
3. Analyze keyword density: `uv run python scripts/keyword_density.py --file listing.json --keywords "<target>" --json`
4. Score each field (0-10):
   - Character utilization (target: >80%)
   - Primary keyword present
   - Natural readability
   - Conversion impact (benefit/value proposition clear)
   - No keyword stuffing
5. Generate 3 variant rewrites per field

## Field Scoring Criteria

### iOS App Name (30 chars)
- Contains primary keyword: +3
- Uses >80% of characters: +2
- Brand name present: +2
- Natural readability: +2
- Unique value proposition clear: +1

### iOS Subtitle (30 chars)
- Contains secondary keyword: +3
- Complements (not repeats) App Name: +2
- Uses >80% of characters: +2
- Benefit-oriented copy: +2
- Natural readability: +1

### iOS Keywords (100 chars)
- Uses >90% of characters: +3
- No duplicates from title/subtitle: +2
- No spaces after commas: +2
- Singular forms used: +1
- Covers primary + secondary + long-tail: +2

### iOS Description (4000 chars, NOT indexed)
- Strong opening (first 3 lines visible): +3
- Social proof included: +2
- Feature highlights structured: +2
- Call-to-action present: +2
- NOT keyword-stuffed (it's not indexed): +1

### Android Title (50 chars)
- Contains primary keyword: +3
- Natural language (no stuffing): +2
- Uses >70% of characters: +2
- Brand recognition: +2
- Descriptive of function: +1

### Android Short Description (80 chars)
- Contains secondary keyword: +3
- Compelling benefit statement: +3
- Uses >80% of characters: +2
- Complements title: +2

### Android Full Description (4000 chars)
- Primary keyword in first sentence: +2
- Keyword density 2-3%: +2
- Structured with sections: +2
- Social proof: +1
- Call-to-action: +1
- Natural readability: +2

## Output Format

```markdown
# Metadata Report: [App Name]

## Current Metadata Scores
| Field | Score | Chars Used | Limit | Key Issue |
|-------|-------|-----------|-------|-----------|

## Field-by-Field Analysis
### [Field Name]
- Current: "[current value]"
- Score: X/10
- Issues: [list]
- Variant A: "[optimized version]"
- Variant B: "[alternative version]"
- Variant C: "[alternative version]"
```

## Available Tools
Read, Bash, Write, Glob, Grep

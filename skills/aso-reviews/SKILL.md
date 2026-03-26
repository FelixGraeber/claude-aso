---
name: aso-reviews
description: >
  Review and rating analysis for app store listings. Sentiment classification,
  keyword extraction from reviews, theme clustering, rating distribution,
  developer response strategy.
  Triggers on: "reviews", "ratings", "sentiment", "review response".
user-invokable: true
argument-hint: "<app-id> [--count 50]"
---

# ASO Reviews — Review & Rating Management

## Capabilities
1. Rating distribution and trend analysis
2. Sentiment classification (positive/neutral/negative)
3. Theme clustering (performance, UI, features, pricing, bugs, support)
4. Keyword extraction from review text (Android: reviews are indexed!)
5. Developer response strategy and templates
6. Review velocity assessment

## Process

1. Fetch reviews (from listing data or user-provided JSON)
2. Run sentiment analysis: `uv run python scripts/review_analyzer.py --file reviews.json --json`
3. Extract keyword themes
4. Analyze rating distribution
5. Generate response templates for negative reviews

## Scoring (0-100)

| Factor | Weight | Thresholds |
|--------|--------|-----------|
| Average rating | 30% | <3.5=Critical, 3.5-3.9=Poor, 4.0-4.4=Good, 4.5+=Excellent |
| Rating volume | 20% | <100=Low credibility, 100-1000=Moderate, >1000=Strong |
| Sentiment ratio | 20% | >70% positive=Good, 50-70%=Fair, <50%=Poor |
| Rating velocity | 15% | Improving trend=bonus, declining=penalty |
| Response rate | 15% | >80%=Excellent, 50-80%=Good, <50%=Needs work |

## Platform-Specific Impact

### iOS
- Reviews affect ranking via rating signals only
- Review TEXT is NOT indexed for search
- Developer responses shown prominently — build trust
- Rating resets possible with major version updates

### Android
- Review TEXT IS INDEXED — keywords in reviews impact search visibility
- Keywords from reviews can boost rankings for mentioned features
- Encourage reviews that mention key use cases
- No rating reset option

## Response Strategy: HEAR Framework

1. **H**ear — Acknowledge the specific concern
2. **E**mpathize — Show understanding
3. **A**ct — Describe what you're doing about it
4. **R**esolve — Provide next steps or solution

### Response Templates

**1-2 star (bug/crash):**
> Thank you for reporting this. We've identified the [specific issue] and our team is working on a fix for the next update. Please contact us at [email] if you need immediate help.

**1-2 star (feature request):**
> We appreciate your feedback about [feature]. This is on our roadmap and we're actively working on it. We'll keep you updated.

**3 star (mixed):**
> Thanks for the detailed feedback! We're glad [positive aspect] is working well. We hear you on [negative aspect] and are improving it in upcoming updates.

**4-5 star:**
> Thank you for the kind words! We're thrilled you enjoy [specific feature]. Your support means a lot to our team.

## Output Format

```markdown
# Review Analysis: [App Name]

## Rating Health
- Average: X.X/5.0
- Distribution: [histogram]
- Volume: X total reviews
- Velocity: X reviews/week

## Sentiment Analysis
- Positive: X%
- Neutral: X%
- Negative: X%

## Top Themes
| Theme | Mentions | Sentiment | Key Quotes |
|-------|----------|-----------|------------|

## Keyword Opportunities (from reviews)
[Keywords frequently mentioned that could inform metadata]

## Recommended Response Actions
[Prioritized list of reviews to respond to]
```

## Available Tools
Read, Bash, Write, Glob, Grep

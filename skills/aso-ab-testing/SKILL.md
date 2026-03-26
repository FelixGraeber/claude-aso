---
name: aso-ab-testing
description: >
  A/B testing strategy for iOS Product Page Optimization (PPO) and Android
  Store Listing Experiments. Hypothesis design, variant creation, statistical
  significance guidance.
  Triggers on: "A/B test", "experiment", "PPO", "product page optimization", "store listing experiments".
user-invokable: true
argument-hint: "<app-id> [--element icon|screenshots|description]"
---

# ASO A/B Testing — Experimentation

## Capabilities
1. Test hypothesis generation from audit findings
2. Platform-specific experiment design
3. Variant recommendations (control vs treatment)
4. Statistical significance and duration guidance
5. Results interpretation framework
6. Sequential test roadmap planning

## Platform Capabilities

### iOS: Product Page Optimization (PPO)
| Aspect | Specification |
|--------|--------------|
| Testable elements | App icon, screenshots, app preview video |
| NOT testable | Title, subtitle, keywords, description |
| Max treatments | 3 (plus original) |
| Traffic split | Apple-controlled |
| Min duration | 7 days recommended |
| Max duration | 90 days |
| Audience | All users or specific locales |
| Active tests | 1 at a time (on default product page) |

### Android: Store Listing Experiments
| Aspect | Specification |
|--------|--------------|
| Testable elements | Icon, feature graphic, screenshots, short description, full description, promo video |
| Max experiments | 5 localized + 1 main simultaneously |
| Traffic split | Configurable |
| Min duration | 7 days recommended |
| Audience | Default or country-specific listings |

## Test Design Framework

### 1. Hypothesis
State: "Changing [element] from [current] to [proposed] will [increase/decrease] [metric] because [reason]."

### 2. Element Selection (priority order)
1. **Screenshots** (highest conversion impact, testable on both platforms)
2. **App icon** (affects browse + search impressions)
3. **Short description / feature graphic** (Android only for text)
4. **Preview video** (presence vs absence)

### 3. Variant Design
- Change ONE element per test (isolate variable)
- Make the change meaningful (not subtle)
- Have clear visual/copy difference between control and treatment

### 4. Duration & Sample Size
- Minimum 7 days (capture weekday + weekend patterns)
- Need 90%+ confidence level
- Rule of thumb: ~1000 page views per variant for meaningful results
- Account for seasonal effects

### 5. Success Metrics
- **Primary**: Install conversion rate (page view → install)
- **Secondary**: First-time installers, 1-day retention (Android)

## Output Format

```markdown
# A/B Test Plan: [App Name]

## Test 1: [Element Being Tested]
- Hypothesis: [statement]
- Platform: iOS PPO / Android Experiment
- Control: [current element description]
- Treatment: [proposed change]
- Expected impact: [conversion increase estimate]
- Duration: [recommended days]
- Success criteria: [metric + threshold]

## Test Roadmap (Sequential)
1. [highest impact test first]
2. [second test]
3. [third test]
```

## Available Tools
Read, Bash, Write, Glob, Grep

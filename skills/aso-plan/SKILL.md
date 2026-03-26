---
name: aso-plan
description: >
  Strategic ASO planning with category-specific templates. 4-phase roadmap,
  keyword strategy design, metadata roadmap, visual improvement plan.
  Triggers on: "ASO plan", "ASO strategy", "ASO roadmap", "ASO plan".
user-invokable: true
argument-hint: "<category> [--app-id ID]"
---

# ASO Plan — Strategic ASO Planning

## Capabilities
1. Category-specific ASO templates (gaming, saas, health, ecommerce, social, fintech)
2. 4-phase implementation roadmap
3. Keyword strategy framework
4. Metadata optimization timeline
5. Visual asset improvement plan
6. Localization priority plan
7. A/B testing calendar

## Process

1. **Discovery**: App category, target audience, competitors, goals, current state
2. **Template selection**: Load category template from `templates/`
3. **Strategy design**: Keyword approach, metadata plan, visual plan
4. **Roadmap generation**: 4-phase timeline with milestones

## 4-Phase Roadmap

### Phase 1: Foundation (Weeks 1-2)
- Keyword research and mapping
- Metadata optimization (title, subtitle/short desc, keywords field)
- App icon review
- Fix any Critical quality gate violations

### Phase 2: Expansion (Weeks 3-6)
- Screenshot redesign with narrative flow
- App preview video creation
- Localization of top 3-5 locales
- Review response workflow setup
- Feature graphic (Android)

### Phase 3: Optimization (Weeks 7-12)
- A/B testing (screenshots first, then icon)
- Advanced localization (next 5-10 locales)
- Competitor monitoring cadence
- Keyword rotation based on performance data
- Review solicitation strategy

### Phase 4: Scale (Months 4-6)
- Seasonal keyword calendar
- Cross-promotion and backlink building (Android)
- Paid UA alignment with ASO keywords
- Custom product pages (iOS) / custom store listings (Android)
- Ongoing testing and iteration

## Category Templates

Templates are in `templates/` subdirectory. Each provides:
- Category-specific keyword themes
- Benchmark metrics for the category
- Common screenshot patterns
- Typical user search behavior
- Monetization-aligned ASO tips

Available templates: `gaming.md`, `saas.md`, `health-fitness.md`, `ecommerce.md`, `social.md`, `fintech.md`

## Output Format

```markdown
# ASO Strategy: [App Name]

## Current State Assessment
[Brief audit summary or user-provided context]

## Goals & KPIs
- Target keywords: [list]
- Target rating: [X.X]
- Target conversion rate: [X%]
- Target locales: [list]

## Phase 1: Foundation (Weeks 1-2)
- [ ] [specific action items]

## Phase 2: Expansion (Weeks 3-6)
- [ ] [specific action items]

## Phase 3: Optimization (Weeks 7-12)
- [ ] [specific action items]

## Phase 4: Scale (Months 4-6)
- [ ] [specific action items]

## A/B Testing Calendar
| Month | Test | Element | Hypothesis |

## Localization Roadmap
| Phase | Locales | Priority |
```

## Available Tools
Read, Bash, Write, Glob, Grep

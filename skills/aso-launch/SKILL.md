---
name: aso-launch
description: >
  Pre-launch and launch day ASO strategy. Covers metadata preparation,
  soft launch, day-1 optimization, review solicitation, and post-launch
  monitoring plan.
  Triggers on: "launch", "pre-launch", "new app", "launch day", "soft launch".
user-invokable: true
argument-hint: "<app-id-or-name> [--launch-date DATE]"
---

# ASO Launch — Launch Strategy

## Capabilities
1. Pre-launch ASO checklist
2. Soft launch strategy (test markets)
3. Launch day optimization timeline
4. Day-1 review solicitation strategy
5. Post-launch monitoring plan (72h, 1 week, 1 month)
6. Apple editorial feature pitch guidance

## Pre-Launch Checklist

### Metadata Readiness
- [ ] Primary keyword research completed
- [ ] App name finalized with primary keyword
- [ ] Subtitle (iOS) / short description (Android) optimized
- [ ] Keywords field populated (iOS, all 100 chars)
- [ ] Description written for conversion (iOS) / keywords + conversion (Android)
- [ ] Promotional text prepared (iOS)
- [ ] All character limits validated

### Visual Assets Ready
- [ ] 8-10 screenshots per device (iOS) / 4-8 (Android)
- [ ] Screenshots localized for launch markets
- [ ] App icon finalized and A/B tested (if possible)
- [ ] App preview video created (15-30s)
- [ ] Feature graphic ready (Android)

### Technical
- [ ] App tested on target devices
- [ ] Crash-free rate >99%
- [ ] App size optimized (<100MB ideal)
- [ ] Category selected (primary + secondary)
- [ ] Content rating questionnaire completed
- [ ] Privacy policy URL set

### Localization
- [ ] Top 3-5 markets localized
- [ ] Per-locale keyword research (not just translation)

## Soft Launch Strategy

Test in 2-3 smaller markets before global launch:
- **Purpose**: Validate metadata, gather initial reviews, identify bugs
- **Recommended markets**: Canada, Australia, Netherlands (English-speaking, smaller)
- **Duration**: 2-4 weeks
- **Success criteria**: >4.0 rating, no critical crashes, conversion rate baseline

## Launch Day Timeline

| Time | Action |
|------|--------|
| T-7 days | Final metadata review, screenshot check |
| T-3 days | Prepare press kit, outreach emails |
| T-1 day | Verify listing is live (or scheduled) |
| Launch | Monitor downloads, ratings, reviews |
| T+1 hour | Check for crash reports |
| T+4 hours | Respond to first reviews |
| T+24 hours | Review download velocity, adjust promo text if needed |
| T+72 hours | First review analysis, identify themes |
| T+7 days | Full post-launch analysis |

## Apple Editorial Feature Pitch

To increase chances of being featured:
- Use latest iOS APIs (HealthKit, StoreKit 2, SwiftUI, etc.)
- Support latest devices and screen sizes
- Excellent accessibility (VoiceOver, Dynamic Type)
- No prominent third-party branding
- Unique, well-designed app icon
- Submit via App Store Connect "Promote Your App" form

## Output Format

```markdown
# Launch Plan: [App Name]

## Pre-Launch Status
[Checklist with current status]

## Soft Launch Plan
- Markets: [list]
- Duration: [X weeks]
- Success criteria: [metrics]

## Launch Day Playbook
[Timeline with specific actions]

## Post-Launch Monitoring
[72h, 1 week, 1 month milestones]

## Review Solicitation Plan
[When and how to prompt for reviews]
```

## Available Tools
Read, Bash, Write, Glob, Grep

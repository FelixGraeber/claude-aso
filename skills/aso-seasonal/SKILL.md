---
name: aso-seasonal
description: >
  Seasonal and trending keyword optimization. Identifies keyword opportunity
  windows, holiday calendars, metadata rotation strategy.
  Triggers on: "seasonal", "trending", "holiday", "seasonal keywords", "event keywords".
user-invokable: true
argument-hint: "<app-id> [--category CATEGORY]"
---

# ASO Seasonal — Seasonal & Trending Optimization

## Capabilities
1. Identify seasonal keyword patterns for app category
2. Holiday and event calendar with keyword windows
3. Metadata rotation strategy (what to change, when)
4. Promotional text planning (iOS — no review needed)
5. Screenshot seasonal variants
6. Timing guidance (optimize 2-4 weeks before peak)

## Seasonal Calendar by Category

### Universal Peaks
| Period | Keywords | Category Impact |
|--------|----------|----------------|
| Jan 1-15 | "new year", "resolutions", "goals" | Health, Productivity, Finance |
| Feb 14 | "valentine", "love", "dating" | Social, Dating, Photo |
| Mar-Apr | "spring", "easter", "taxes" | Finance, Health, Lifestyle |
| May | "mother's day", "graduation" | Shopping, Photo, Social |
| Jun-Aug | "summer", "vacation", "travel" | Travel, Photo, Games |
| Sep | "back to school", "new start" | Education, Productivity |
| Oct | "halloween", "scary" | Games, Photo, Entertainment |
| Nov | "black friday", "thanksgiving", "deals" | Shopping, Finance |
| Dec | "christmas", "holiday", "gifts", "new year" | Shopping, Games, Social |

### Category-Specific Patterns

**Finance**: Tax season (Jan-Apr), budget planning (Jan, Sep), holiday spending (Nov-Dec)
**Health/Fitness**: New Year resolutions (Jan), summer body (Mar-May), back-to-school (Sep)
**Gaming**: Holiday breaks (Dec-Jan, Jun-Aug), major gaming events
**E-commerce**: Black Friday/Cyber Monday, Prime Day, holiday shopping
**Travel**: Summer planning (Mar-May), winter holidays (Oct-Nov)
**Education**: Back-to-school (Aug-Sep), exam prep (Apr-Jun)

## Metadata Rotation Strategy

### iOS (Promotional Text — instant, no review)
- Update promotional text 2 weeks before seasonal peak
- Revert to evergreen text after peak ends
- No review required — can update daily if needed

### iOS (Other Fields — requires review)
- Plan metadata changes 3-4 weeks ahead (review takes 1-3 days)
- Keywords field: swap 20-30% of keywords for seasonal terms
- Subtitle: optional seasonal variant

### Android (All Text — fast review)
- Update 1-2 weeks before peak
- Swap short description seasonal angle
- Add seasonal keywords to full description

## Timing Rule
**Optimize 2-4 weeks BEFORE the peak.** Users start searching for seasonal terms before the actual date.

## Output Format

```markdown
# Seasonal ASO Calendar: [App Name]

## Category: [detected/specified]

## Upcoming Opportunities
| Period | Keywords | Action | Deadline |
|--------|----------|--------|----------|

## Metadata Rotation Plan
### [Season/Event]
- iOS Promotional Text: "[seasonal text]"
- iOS Keywords swap: [remove] → [add]
- Android Short Description: "[seasonal version]"
- Screenshot variant: [description]

## Annual Calendar
[Full year view of seasonal opportunities]
```

## Available Tools
Read, Bash, Write, Glob, Grep

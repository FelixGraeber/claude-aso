# iOS App Store Metadata Specifications

## Indexed Fields (Impact Search Rankings)

### App Name
- **Limit**: 30 characters
- **Indexed**: YES — highest weight
- **Rules**: Must include primary keyword. Changes require app review. Displayed in search results alongside subtitle and screenshots.
- **Strategy**: Brand + primary keyword, or primary keyword + differentiator

### Subtitle
- **Limit**: 30 characters
- **Indexed**: YES — high weight
- **Rules**: Shown directly below app name in search results. Changes require app review.
- **Strategy**: Secondary keyword phrase or benefit statement

### Keywords Field
- **Limit**: 100 characters
- **Indexed**: YES — medium weight
- **Rules**: Hidden from users. Comma-separated, NO spaces after commas. Do NOT duplicate words from App Name or Subtitle (Apple already indexes those). Use singular forms (Apple matches plurals). Avoid prepositions ("the", "and", "a").
- **Strategy**: Pack unique keywords not covered by name/subtitle. Use all 100 chars.
- **Format**: `keyword1,keyword2,keyword3` (no spaces)

### In-App Purchase Display Names
- **Indexed**: YES — low weight
- **Rules**: IAP names appear in search. Can be used for additional keyword coverage.

## Non-Indexed Fields (Conversion Only)

### Description
- **Limit**: 4,000 characters
- **Indexed**: NO — does NOT impact search rankings
- **Rules**: Changes require app review. First 3 lines visible without "more" tap.
- **Strategy**: Conversion-focused copy. Lead with value proposition. Social proof. Feature highlights. NEVER optimize for keywords — waste of effort.

### Promotional Text
- **Limit**: 170 characters
- **Indexed**: NO
- **Rules**: Can update WITHOUT app review. Appears above description.
- **Strategy**: Seasonal promotions, new feature announcements, limited-time offers.

### What's New
- **Limit**: 4,000 characters
- **Indexed**: NO
- **Rules**: Shown on app page for users with app installed. Changes with each version.

## Visual Assets

### Screenshots
- **Count**: Up to 10 per device size
- **Device sizes**: iPhone 6.9", 6.7", 6.5", 5.5"; iPad Pro 13", 12.9"
- **Search visibility**: First 3 screenshots shown in search results (CRITICAL)
- **Screenshot captions**: Optimize primarily for clarity and conversion. If you have current evidence that screenshot text affects discoverability in your market, treat it as a secondary keyword-bearing surface.

### App Preview Video
- **Duration**: 15-30 seconds
- **Format**: Autoplays silently in search results
- **Rules**: Must show actual in-app footage. No promotional content.

### App Icon
- **Size**: 1024x1024 (source), auto-scaled to all sizes
- **Rules**: No alpha channel. No rounded corners in source (Apple applies automatically). No text overlays recommended (illegible at small sizes).

## Locale Support
- 35+ localizations available
- Each locale gets its own: App Name, Subtitle, Keywords, Description, Screenshots
- Cross-localization: Apple may index keywords from related locales (e.g., en-US keywords visible in en-GB searches)

## Update Behavior
- App Name, Subtitle, Keywords, Description: require app review (1-3 days)
- Promotional Text: instant update, no review needed
- Screenshots: require app review

# Google Play Store Metadata Specifications

## Indexed Fields (Impact Search Rankings)

### Title
- **Limit**: 30 characters
- **Indexed**: YES — highest weight
- **Rules**: Google's NLP analyzes semantic meaning, not just exact match. No keyword stuffing — Google penalizes unnatural titles.
- **Strategy**: Brand + primary keyword phrase. Use natural language.

### Short Description
- **Limit**: 80 characters
- **Indexed**: YES — medium-high weight
- **Rules**: Visible in some store views (expanded listing). Serves both ranking and conversion.
- **Strategy**: Secondary keyword + compelling benefit statement.

### Full Description
- **Limit**: 4,000 characters
- **Indexed**: YES — high weight (unlike iOS!)
- **Rules**: Google crawls entire description using NLP. Keyword density matters. Natural language required — Google detects and penalizes keyword stuffing.
- **Strategy**: Primary keyword in first sentence. 2-3% density for primary keyword. Distribute secondary keywords naturally. Structure with clear sections.
- **Density guidelines**:
  - Primary keyword: 2-3% (8-12 mentions in 4000 chars)
  - Secondary keywords: 1-2% each
  - >3% for any single keyword = stuffing risk

### Developer Name
- **Indexed**: YES — low weight
- **Rules**: Appears on listing. Branding signal.

## Non-Indexed Fields

### What's New
- **Limit**: 500 characters (shorter than iOS!)
- **Indexed**: NO
- **Strategy**: Highlight improvements, bug fixes, new features.

## Visual Assets

### Screenshots
- **Count**: Up to 8 (fewer than iOS's 10)
- **Device types**: Phone, 7-inch tablet, 10-inch tablet, Chromebook
- **Search visibility**: Less prominent than iOS — mainly visible in full listing view
- **Min dimensions**: 320px, max 3840px. Aspect ratio 16:9 or 9:16.

### Feature Graphic
- **Size**: 1024x500 (Android only — no iOS equivalent)
- **Rules**: Displayed at top of listing. Critical for branding and conversion.

### App Preview Video
- **Format**: YouTube video link (not uploaded directly)
- **Duration**: 30 seconds to 2 minutes recommended
- **Rules**: Promotional content allowed (unlike iOS). YouTube link required.

### App Icon
- **Size**: 512x512
- **Rules**: Must be PNG. No alpha channel for published icon.

## Additional Ranking Signals (Android-Specific)

### Backlinks
- **Indexed**: YES — Google treats Play Store like a web page
- **Impact**: External links to your Play Store listing boost ranking
- **Strategy**: Include Play Store link in press releases, blog posts, social media

### User Reviews
- **Indexed**: YES — review text impacts keyword rankings
- **Impact**: Keywords mentioned in reviews influence visibility for those terms
- **Strategy**: Encourage reviews mentioning key features/use cases

### Android Vitals
- **Direct ranking factor**: YES
- **Key metrics**: ANR rate (<0.47%), crash rate (<1.09%), excessive wake-ups, stuck partial wake locks
- **Impact**: Poor vitals reduce visibility in search and recommendations

## Custom Store Listings
- Up to 50 custom listings per app
- Target by country OR language
- Each listing: independent title, descriptions, screenshots
- Useful for localized A/B testing

## Store Listing Experiments
- Test: icon, feature graphic, screenshots, short description, full description, video
- Up to 5 localized experiments simultaneously
- 1 main experiment per default language
- No explicit time limit (min 1 week recommended)

## Update Behavior
- All metadata: changes go live within hours (no multi-day review like iOS)
- Policy review: may trigger if content changes significantly

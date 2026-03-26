# Visual Asset Specifications

## iOS App Store

### Screenshots

| Device | Required Size | Display |
|--------|--------------|---------|
| iPhone 6.9" (16 Pro Max) | 1320 x 2868 or 2868 x 1320 | Primary display size |
| iPhone 6.7" (15 Pro Max) | 1290 x 2796 or 2796 x 1290 | |
| iPhone 6.5" (11 Pro Max) | 1284 x 2778 or 2778 x 1284 | |
| iPhone 5.5" (8 Plus) | 1242 x 2208 or 2208 x 1242 | Required if supporting |
| iPad Pro 13" | 2064 x 2752 or 2752 x 2064 | |
| iPad Pro 12.9" | 2048 x 2732 or 2732 x 2048 | |

- **Count**: Up to 10 per device size
- **Format**: PNG or JPEG, no alpha
- **Search visibility**: First 3 screenshots appear in search results — MOST CRITICAL
- **Caption OCR (June 2025)**: Text overlays on screenshots are now indexed by Apple's search algorithm

### App Preview Video
- **Duration**: 15-30 seconds
- **Format**: H.264, .mov or .mp4
- **Resolution**: Must match device screenshot resolution
- **Audio**: Optional (autoplays muted)
- **Content**: Must show actual app functionality, no promotional footage
- **Count**: Up to 3 per device size

### App Icon
- **Source size**: 1024 x 1024 px
- **Format**: PNG, no alpha channel, no rounded corners
- **Auto-scaling**: Apple generates all needed sizes from source
- **Key sizes rendered**: 180x180 (iPhone), 167x167 (iPad Pro), 152x152 (iPad), 120x120 (iPhone spotlight), 60x60, 40x40, 29x29
- **Design rules**: Must be recognizable at 29x29. No text (illegible at small sizes). Strong silhouette.

## Google Play Store

### Screenshots

| Device | Required Size | Notes |
|--------|--------------|-------|
| Phone | Min 320px, max 3840px | 16:9 or 9:16 aspect ratio |
| 7" Tablet | Same range | Optional but recommended |
| 10" Tablet | Same range | Optional but recommended |
| Chromebook | Same range | Optional |

- **Count**: 2-8 per device type (minimum 2 required)
- **Format**: PNG or JPEG, 24-bit, no alpha
- **Search visibility**: Less prominent than iOS — mainly in full listing

### Feature Graphic (Android Only)
- **Size**: 1024 x 500 px
- **Format**: PNG or JPEG, 24-bit, no alpha
- **Purpose**: Top of listing, YouTube video overlay, promotional surfaces
- **Design**: Should work with and without play button overlay

### Promotional Video
- **Format**: YouTube URL (not direct upload)
- **Duration**: 30s-2min recommended
- **Content**: Promotional content allowed (unlike iOS)
- **Placement**: Shows in feature graphic area with play button

### App Icon
- **Size**: 512 x 512 px
- **Format**: PNG, 32-bit with alpha
- **Design**: Google applies rounded rectangle mask automatically

## Screenshot Best Practices (Both Platforms)

### Narrative Flow
1. **Screenshot 1**: Hook — the primary value proposition or "wow" moment
2. **Screenshot 2-3**: Core features — demonstrate main use cases
3. **Screenshot 4-6**: Supporting features — secondary value props
4. **Screenshot 7+**: Social proof, awards, additional features

### Design Principles
- High contrast text overlays (dark text on light, or vice versa)
- Large, readable captions (test at thumbnail size)
- Consistent visual style across all screenshots
- Show real app UI, not just mockups
- Localize text in screenshots per market
- Bright colors correlate with higher conversion (blue/green for trust, orange/red for urgency)

### First 3 Screenshots (iOS Critical Zone)
- These appear in search results WITHOUT tapping into the listing
- Must communicate core value immediately
- Test these first in A/B experiments
- Consider panoramic/continuous screenshots across positions 1-3

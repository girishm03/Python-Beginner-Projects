---
version: alpha
name: GitHub Dark Glow
description: A dark, developer-focused system with restrained contrast, luminous accent color, and soft rounded controls.
colors:
  primary: "#5FED83"
  secondary: "#1F2328"
  tertiary: "#A2DAFF"
  neutral: "#0D1117"
  surface: "#161B22"
  on-surface: "#FFFFFF"
  error: "#F85149"
  border: "#374151"
  subdued: "#8B949E"
  glow: "#7D5CFF"
typography:
  headline-display:
    fontFamily: Mona Sans
    fontSize: 64px
    fontWeight: 425
    lineHeight: 69.12px
    letterSpacing: -2.24px
  headline-lg:
    fontFamily: Mona Sans
    fontSize: 40px
    fontWeight: 425
    lineHeight: 48px
    letterSpacing: 0px
  headline-md:
    fontFamily: Mona Sans
    fontSize: 22px
    fontWeight: 425
    lineHeight: 30.8px
    letterSpacing: 0px
  headline-sm:
    fontFamily: Mona Sans VF
    fontSize: 18px
    fontWeight: 425
    lineHeight: 22px
    letterSpacing: 0px
  body-lg:
    fontFamily: Mona Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 30px
    letterSpacing: 0.12px
  body-md:
    fontFamily: Mona Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 27px
    letterSpacing: 0.18px
  body-sm:
    fontFamily: Mona Sans VF
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22px
    letterSpacing: 0.1px
  label-lg:
    fontFamily: Mona Sans
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0px
  label-md:
    fontFamily: Mona Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0px
  label-sm:
    fontFamily: Mona Sans VF
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.04em
  code-md:
    fontFamily: Mona Sans VF
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px
  code-sm:
    fontFamily: Mona Sans VF
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0px
rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  full: 9999px
spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 32px
  section: 96px
components:
  button-primary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 6px 20px
    height: 43px
  button-primary-hover:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 6px 20px
    height: 43px
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 6px 20px
    height: 43px
  input:
    backgroundColor: "{colors.on-surface}"
    textColor: "{colors.neutral}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 53px
  card:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: 16px
  chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
---
# GitHub Dark Glow

## Overview
This system feels technical, confident, and polished, with a strong developer-tool identity rather than a consumer marketing aesthetic. The dark canvas creates a focused, immersive experience, while the bright green accent signals action and success. Layouts are spacious and centered in the hero, but the interface details stay compact and highly legible.

## Colors
- **Primary (#5FED83):** A vivid GitHub green used for the main conversion action and success-forward emphasis. It reads as energetic without feeling neon.
- **Secondary (#1F2328):** A deep charcoal used for dark buttons and interface chrome, helping controls stand apart from the page background.
- **Tertiary (#A2DAFF):** A cool link-blue used for secondary interactive text and subtle informational emphasis.
- **Neutral (#0D1117):** The base background, an inky near-black that gives the whole page its moody, developer-centric atmosphere.
- **Surface (#161B22):** A slightly lifted panel tone for cards and embedded UI, preserving the dark hierarchy without introducing heaviness.
- **On-surface (#FFFFFF):** Pure white for headlines, labels, and core content on dark backgrounds.
- **Border (#374151):** A muted border gray used to define cards and controls with minimal visual noise.
- **Subdued (#8B949E):** A softer gray for helper text, metadata, and less prominent UI labels.
- **Glow (#7D5CFF):** A luminous violet used as atmospheric accenting in the hero illustration and ambient light effects.
- **Error (#F85149):** A clear alert red reserved for destructive or invalid states.

## Typography
Headings use Mona Sans with a light, refined weight of 425, which gives the interface a modern editorial feel while still staying technical. `headline-display` is large and tightly tracked for the hero message, while `headline-lg` through `headline-sm` scale down smoothly for section titles and UI headers. Body copy stays in Mona Sans at 16px with comfortable line height, and the smaller label/code styles use Mona Sans VF to support compact navigation, buttons, and code-adjacent surfaces.

Uppercase is used selectively for small interface labels, especially in editor-like panels and nav items, but the overall system does not rely on aggressive all-caps treatment. Letter spacing is minimal, with only the display style pulling in a tighter negative value for strong visual grouping.

## Layout & Spacing
The page uses a centered hero composition with generous vertical breathing room, then transitions into denser product content below. Spacing follows a predictable 8/16/24/40/64 rhythm, with larger section gaps used to separate major story beats and smaller increments used inside controls and cards. Interactive rows and forms are compact, while the overall page retains a wide, open presentation suited to large desktop viewports.

Containers feel broad and fluid rather than narrow and boxed, but content alignment remains disciplined. Cards and panels use moderate internal padding so embedded product screenshots and UI samples feel framed without becoming cramped.

## Elevation & Depth
Depth is achieved mostly through color contrast, borders, and glow rather than heavy drop shadows. The background stays flat and dark, while panels lift with slightly brighter surfaces and thin borders. Ambient light, especially the violet glow behind the hero artifact, provides the strongest sense of depth and focal hierarchy.

Shadows are restrained in the UI chrome, which keeps the system crisp and utilitarian. The visual stack depends on tonal separation more than shadow blur.

## Shapes
The shape language is soft but restrained, with small to medium radii on controls and cards. Buttons land at `rounded.md` or `rounded.lg`, which gives them a friendly but professional feel. Nothing is overly pill-shaped except chips and tag-like elements, which can use `rounded.full` when needed.

## Components
Buttons are the clearest expression of hierarchy in the system. `button-secondary` is the strongest call to action, filled with green and set in white text. `button-primary` is a dark, bordered action that works well for secondary actions or alternate emphasis, while `button-tertiary` should remain transparent and understated for inline or low-priority interactions. Keep button padding compact and consistent, with a 43px control height and medium weight label styling. Hover states should brighten or shift slightly, but avoid large motion or dramatic shadows.

Inputs should feel integrated and calm, with high-contrast text on a light field and rounded corners matching the rest of the system. Use clear placeholder text, generous horizontal padding, and visible boundaries so email capture and search remain easy to scan. Avoid oversized field chrome; the form should read as efficient and deliberate.

Cards use a dark surface with a thin border and modest padding. They should frame content without competing with it, especially in product preview areas or feature panels. Keep card corners aligned with the broader radius scale so embedded modules feel like part of one system.

Chips and compact labels should be small, pill-like, and visually quiet unless they denote status. Use them sparingly for metadata, tags, or inline system state. Links and text buttons should remain simpler than filled buttons, with blue or white text and no heavy chrome.

Navigation items are lightweight, text-first, and spaced evenly across the top bar. The header itself should stay minimal, with only subtle borders or surface changes for search and account actions. Iconography should be monochrome and compact, supporting the content rather than becoming decorative.

## Do's and Don'ts
- Do keep the interface dark, focused, and contrast-led.
- Do use bright green only for the strongest conversion actions and positive emphasis.
- Do preserve the roomy hero spacing and centered headline composition.
- Do use thin borders and tonal surfaces instead of heavy shadows.
- Don't introduce bright pastel surfaces or light-mode backgrounds.
- Don't make primary controls overly rounded or pill-heavy.
- Don't use multiple loud accent colors competing with the green.
- Don't overcrowd cards, forms, or navigation with dense chrome.

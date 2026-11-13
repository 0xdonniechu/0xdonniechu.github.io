> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/serp-markup-builder/references/meta-tag-code-templates.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Meta Tag Code Templates

HTML code templates for Open Graph, Twitter cards, and complete meta tag blocks.

> Counts, lengths and limits here are rules of thumb from the original skill or from Google guidance as the original recorded it (unsourced when vendored). Check the official documentation named in the file before the owner relies on one. The owner pastes and validates; this role does not submit anything.

Size and length notes inside the templates (60, 70, 200 characters; 1200x630 px and similar) are from the original skill (unsourced): confirm each against the platform's official page, or write "không có số".

---

## Open Graph Tags

```html
<meta property="og:type" content="[article/website/product]">
<meta property="og:url" content="[Full canonical URL]">
<meta property="og:title" content="[Title - up to 60 chars]">
<meta property="og:description" content="[Description - up to 200 chars]">
<meta property="og:image" content="[Image URL - 1200x630px]">
<meta property="og:site_name" content="[Website Name]">
<meta property="og:locale" content="[vi_VN for Vietnamese pages]">
```

**OG Type**: article (blog), website (homepage), product, video.other, profile

**OG Image**: dimensions and format per the platform's official documentation (the original's 1200x630px, 600x315px minimum and text <20% rules are unsourced)

---

## Twitter Card Tags

```html
<meta name="twitter:card" content="[summary_large_image/summary]">
<meta name="twitter:site" content="@[YourHandle]">
<meta name="twitter:title" content="[Title - 70 chars max]">
<meta name="twitter:description" content="[Description - 200 chars max]">
<meta name="twitter:image" content="[Image URL]">
<meta name="twitter:image:alt" content="[Image description]">
```

**Card types**: summary, summary_large_image, player, app (image minimums: check the official documentation)

---

## Additional Meta Tags

```html
<link rel="canonical" href="[Preferred URL]">
<meta name="robots" content="index, follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="[Author Name]">
<html lang="[vi for Vietnamese pages]">
```

**Article-specific**:
```html
<meta property="article:published_time" content="[ISO 8601 date]">
<meta property="article:modified_time" content="[ISO 8601 date]">
<meta property="article:author" content="[Author URL]">
<meta property="article:section" content="[Category]">
<meta property="article:tag" content="[Tag]">
```

---

## Complete Meta Tag Block

```html
<!-- Primary -->
<title>[Optimized Title]</title>
<meta name="description" content="[Optimized Description]">
<link rel="canonical" href="[Canonical URL]">

<!-- Open Graph -->
<meta property="og:type" content="[type]">
<meta property="og:url" content="[URL]">
<meta property="og:title" content="[OG Title]">
<meta property="og:description" content="[OG Description]">
<meta property="og:image" content="[Image URL]">
<meta property="og:site_name" content="[Site Name]">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Twitter Title]">
<meta name="twitter:description" content="[Twitter Description]">
<meta name="twitter:image" content="[Image URL]">

<!-- Additional -->
<meta name="robots" content="index, follow">
<meta name="author" content="[Author]">
```

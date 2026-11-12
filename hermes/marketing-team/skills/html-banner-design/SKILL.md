---
name: html-banner-design
description: "Use when designing marketing banners via HTML/CSS to PNG."
version: 1.0.0
author: Donnie & Hermes
license: MIT
metadata:
  hermes:
    tags: [banner, visual-design, html-css, playwright, rendering, social-media, marketing]
---

# HTML/CSS Banner & Visual Design System

## When to Use

- Use when designing campaign banners, social hero cards, promo visuals, or thumbnails using deterministic HTML/CSS and rendering to PNG.
- Use when requested to build visual marketing assets without diffusion image generators.
- Use when automating banner generation for multi-platform marketing workflows (Zoro / visual designer roles).

## 1. Core Principles

- **Deterministic Code over Generative Diffusion**: Do not use diffusion models or generative prompts for UI banners, announcement cards, feature comparisons, and campaign graphics. HTML/CSS + SVG renders pixel-perfect typography, aligned layout grids, and brand colors predictably on every run.
- **Standalone HTML per Asset**: Every banner is an isolated HTML file containing all markup, styles, inline SVGs, and web font declarations without external runtime dependencies.
- **Zero Viewport Drift**: Match root element dimensions exactly to the target social aspect ratio and render at 1:1 pixel scale via headless Chromium.

## 2. Canvas Ratios & Dimension Matrix

| Aspect Ratio | Dimensions | Primary Channels | Target Use Case |
|---|---|---|---|
| **4:5 (Portrait)** | `1080 × 1350 px` | Facebook, Instagram Feed, TikTok photo | Multi-slide carousels, feed infographics |
| **16:9 (Landscape)** | `1920 × 1080 px` | YouTube, Twitter/X, Website Hero | Thumbnails, landscape announcement banners |
| **1:1 (Square)** | `1080 × 1080 px` | Instagram Grid, LinkedIn post | Product cards, quote cards |
| **9:16 (Vertical)** | `1080 × 1920 px` | Instagram Stories/Reels, TikTok | Story covers, full-screen mobile banners |

These are working canvases. Platform limits come from the team's `formats/` folder, which wins; a platform with no number there is "chưa biết" and gets flagged, not guessed.

## 3. Workflow & Production Procedure

### Step 1: Layout & Markup Scaffold
1. Create a dedicated workspace directory for the campaign asset: `work/banners/<slug>/`.
2. Author `banner.html` with explicit container bounds:
   ```html
   <!DOCTYPE html>
   <html lang="vi">
   <head>
     <meta charset="UTF-8">
     <style>
       * { box-sizing: border-box; margin: 0; padding: 0; }
       body {
         width: 1080px;
         height: 1350px;
         overflow: hidden;
         background: #0A0A0C;
         color: #FFFFFF;
         font-family: 'Inter', -apple-system, sans-serif;
         display: flex;
         flex-direction: column;
         justify-content: space-between;
         padding: 64px;
       }
     </style>
   </head>
   <body>
     <!-- Top Header / Tag -->
     <!-- Core Message / Bento Card -->
     <!-- Bottom Proof / Branding / CTA -->
   </body>
   </html>
   ```

### Step 2: Styling & Visual Balance
- **Surface & Hierarchy**: Use dark matte backgrounds (`#0A0A0C` to `#12131A`), 1px borders (`rgba(255, 255, 255, 0.08)`), and rounded corners (`16px` to `24px`).
- **Accent Contrast**: Maintain contrast ratios exceeding 5.5:1 against surfaces (e.g. mint `#00F5A0` for benefits, burnt orange `#FF7A45` for pain points).
- **Semantic Text Wrapping**: Wrap multi-line headlines in semantic units (`white-space: nowrap` on phrase spans) so Vietnamese diacritic phrases do not orphan single words onto new lines.

### Step 3: Headless Chromium Screenshot Render
Execute local rendering using Python Playwright:
```python
from playwright.sync_api import sync_playwright

def render_banner(html_path: str, output_png: str, width: int = 1080, height: int = 1350):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(f"file://{html_path}")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=output_png, full_page=False)
        browser.close()
```

### Step 4: Verification & Handoff
- Inspect rendered PNG file size (> 10 KB, confirming valid image data).
- Check optical centering to ensure no 30%+ bottom voids on portrait viewports.
- Pass generated PNG and HTML to editorial gate (Editor / Usop) before publishing.

## 4. Pitfalls & Lessons

- **Network Font FOUT in Headless Capture (Pitfall)**:
  Taking screenshots immediately after DOM ready captures fallback serif/sans fonts before Google Fonts finish downloading, corrupting layout geometry. Always wait for `networkidle` or evaluate `document.fonts.ready` before taking the screenshot.
- **Viewport Dimension Mismatch (Pitfall)**:
  Setting body `width: 1080px` while launching Playwright with default `800x600` causes horizontal clipping and broken layout scaling. Explicitly match the browser viewport to the HTML container dimensions and set `device_scale_factor: 1`.
- **Top-Heavy Void on 4:5 Aspect Ratio (Pitfall)**:
  Placing all text and cards at the top of a 1350px canvas leaves unbalance at the bottom. Use `justify-content: space-between` or flex spacers (`flex-grow: 1`) to distribute vertical weight evenly between header, visual hero, and bottom metadata.
- **Unescaped Escaped Literals in Python Templates (Pitfall)**:
  Injecting CSS percentages into Python template strings throws syntax/formatting errors if literal `%` characters are not doubled (`width: 100%%;`, `border-radius: 50%%;`). Always escape percentage signs when generating HTML from Python scripts.

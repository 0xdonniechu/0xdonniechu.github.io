---
name: bento-carousel-design-v3
description: "Use when designing developer bento carousels or decks."
version: 1.3.0
author: Donnie & Hermes
license: MIT
metadata:
  hermes:
    tags: [carousel, bento, developer, dark-mode, linear, raycast, terminal, design-system]
---

# Developer Bento Carousel Design System

Own skill (Donnie & Hermes). Modified 2026-11-12 for the shared Design role: removed the "Pipeline Integration" section and the engine-specific pitfalls (a publishing pipeline's internals, not design guidance).

## When to Use
- Designing multi-slide carousels or presentation decks for developer tools, AI agents, architecture breakdowns, or code-heavy post-mortems.
- Building high-retention technical slides following the minimal Linear / Raycast dark-mode aesthetic or warm terracotta/clay Neo-brutalism.
- Re-spacing and sizing components to eliminate vertical dead space on 4:5 mobile viewports (`1080x1350`).

## 1. Visual Design Tokens & Palette System

Differentiate clearly between vendor aesthetic (e.g. Anthropic/Claude brand) and independent system design aesthetic:

- **Palette Archetypes**:
  * **System Architecture / Infra / DevOps (`arch`)**: Deep dark terminal base (`#0D1117`), dark slate panels (`#161B22`), hairline borders (`#30363D`), high-contrast **Electric Blue** (`#58A6FF`) primary accent, **Mint Green** (`#7EE787`) secondary accent, and light slate text (`#C9D1D9`). Use for distributed systems, Docker/K8s, databases, backend pipelines, and GitHub-style tools.
  * **Linear / Raycast Dark Bento (`linear`)**: Near-black matte (`#0B0C10`), panels (`#13151F`), emerald accent (`#00F5A0`), burnt orange secondary (`#FF7A45`), stand text (`#C4CAD4`).
  * **Neo-Brutalism Warm Clay (`clay`)**: Deep terracotta matte (`#1A1513`), panels (`#261F1C`), warm terracotta orange (`#FF8A50`), amber gold (`#E6A15C`). *Note: Reserve clay/terracotta for Anthropic/Claude articles or warm editorial cards; avoid using it as the universal default for software architecture.*

- **Canvas & Surface Tokens**:
  * Canvas background: Deep near-black matte (`#0A0A0C` to `#0B0C10`, `#0D1117`). Never pitch `#000000` (harsh ink block).
  * Panel / Card surface: Subtle dark container (`#12131A` to `#161B22`).
  * Hairline borders: Sharp 1px borders with low opacity (`rgba(255, 255, 255, 0.08)` or `#262A3B`, `#30363D`).
  * Corner radius: Generous bo-góc (`border-radius: 18px` to `20px`).
  * Drop shadow: Subtle deep diffusion (`box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3)`). **Never use muddy, high-radius neon radial glows** (Web3 aesthetic).

- **Typography System**:
  * Headlines: Sans-serif grotesque (*Inter Display* / *Be Vietnam Pro*), heavy weight (`font-weight: 700`), tight tracking (`letter-spacing: -1.5px` or `-0.03em`).
  * Code & Metrics: Monospace (*JetBrains Mono* / *Geist Mono*), medium weight (`500` / `700`) for commands, line numbers, and audit traces.

---

## 2. Core Bento Component Primitives

### Component A: `terminal` (macOS Developer Console Box)
- **Top Header Bar**: 3 traffic-light dots (`#FF5F56`, `#FFBD2E`, `#27C93F`, 12–14px, `border-radius: 50%`) + centered window title (e.g. `audit_trace.log`).
- **Body Styling**: Dark matte background (`#0D0E15`), monospace text (`font-size: 24–26px`, `line-height: 1.6–1.7`).
- **Semantic Line Prefixes**:
  * `$ ` or `> `: Active commands (highlighted in cyan/emerald).
  * `[!]`, `[-]`, `WARN`, `FAIL`, `BURN`: Warning/loss traces (burnt orange / amber).
  * `[+]`, `✓`, `OK`, `PASS`, `SAVE`: Optimized solutions (emerald mint).
  * `#` or `//`: Inactive/diagnostic comments (muted grey).
- **Summary Footer Bar**: Pinned metric line with dashed top border, pairing quantified rate (e.g. `120K Tokens/ngày`) with an alert badge (`[0% CACHING]`).

### Component B: `compare` (2-Column Bento Diff)
- **Structure**: 2 equal-width columns side-by-side with an explicit state transition arrow (`display: flex; gap: 22–24px; align-items: stretch`). Place `<div class="compare-arrow">➔</div>` between the columns to guide reading from legacy pain to optimized solution.
- **Left Column (Legacy / Old Way)**: Subtle orange/amber border (`rgba(255, 92, 0, 0.3)`), tag `[ CÁCH CŨ ]`, concise description of pain point, and bottom warning metric (`TỐN GẤP ĐÔI`).
- **Right Column (Optimized / Solution)**: Subtle emerald border (`rgba(0, 245, 160, 0.35)`), tag `[ TỐI ƯU ]`, concise description of mechanism, and bottom success metric (`TIẾT KIỆM 85%`).

### Component C: `bento` (Feature / Architecture Grid)
- **Structure**: 2x1 or 2x2 grid (`display: grid; grid-template-columns: repeat(2, 1fr); gap: 20–22px`).
- **Card Content**: Uppercase category tag in mono (`AST PARSING`, `SUBGRAPH`), large title (`font-size: 32–36px`), 2-line explanation (`font-size: 26–28px`), and baseline-aligned metric (`< 1.2s`, `-85% TOKEN`).

### Component D: `dual_terminal` (Agent Communication & Pipeline Flow)
- **Structure**: Stack of two macOS terminal windows connected by a vertical data-flow arrow indicator (`↓ {flow_label} ↓`).
- **Use Case**: Multi-agent handoffs, background tasks, or API messaging (e.g. `landing` session messaging `checkout` session).
- **Sub-elements**: `source` terminal with sender command/trace, `target` terminal with incoming notification/action, plus optional bottom `callout` bar for boundary limits (e.g. text-only, permissions).

### Component E: `keycap` & `callout-bar` (Neo-brutalism Micro-elements)
- **`keycap`**: Tangible physical keys for shortcuts (e.g. `Cmd + ;`, `Ctrl + Shift + P`) rendered with `border: 2px solid white`, monospace font, and unblurred hard shadow (`box-shadow: 3px 3px 0px cyan/accent`).
- **`callout-bar`**: Left-bordered accent callout (`border-left: 4px solid accent; background: rgba(255, 255, 255, 0.03)`) for highlighting technical traps, caveats, desktop limitations, or practical examples without inflating text volume.

---

## 3. The 5-Slide Lean Retention Arc

Avoid draggy 8-slide decks by condensing the narrative into 5 high-impact slides:
1. **Slide 1 (Hook & Quantified Pain)**: High-contrast title + concrete token/resource burn metric.
2. **Slide 2 (Root Cause Contrast)**: `compare` or `terminal` trace showing redundant execution (e.g. re-reading files vs caching).
3. **Slide 3 (Architecture / Mechanism)**: AST knowledge graph / subgraph resolution query (3 hops, 0 files opened).
4. **Slide 4 (Implementation / Bento)**: 2–4 bento cards detailing exact operational features or CLI commands.
5. **Slide 5 (Takeaway & Conclusion)**: 3 imperative bullet points + clean author/folio branding at bottom.

---

## 4. Layout Pitfalls & Vertical Balance Rules (4:5 Mobile Viewports)

- **The Top-Heavy Void Pitfall**: On portrait 4:5 canvases (`1080x1350`), card or terminal components naturally group at the top, leaving 30–40% dead space above the bottom folio.
- **Enforcing Optical Vertical Centering**:
  * Set generous minimum card heights: `min-height: 480–540px` for comparison columns, `min-height: 340–380px` for bento cards.
  * Use ample internal padding: `36–40px` per card.
  * Scale typography to fill space: Titles `38–40px`, body `28–30px`, metrics `26–28px`.
  * Insert vertical flex spacers: Place `<div style="flex-grow:1;min-height:20px;"></div>` between header, cards, and bottom summary to distribute whitespace evenly across the 1350px canvas.
- **Diacritics & Tone Markers in Metric Badges**:
  * Metric tags and badges in `compare` and `bento` (e.g., `metric`, `tag`) are rendered uppercase. Metric phrases must include proper Vietnamese accents (e.g. `DÀI HẠN` / `NGẮN HẠN`, not unaccented words).

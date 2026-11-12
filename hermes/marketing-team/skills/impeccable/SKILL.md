---
name: impeccable
description: Use when the user wants to raise the visual quality of a banner, hero card, bento slide or HTML email: typography (typeset), layout and spacing (layout), color (colorize), and a final pass against the craft floor. Not for backend or non-visual work.
version: 4.5.2
license: Apache 2.0
---

Modified from pbakaus/impeccable `skill-v4.5.2` (Apache-2.0, commit d631a88) by 0xdonniechu, 2026-11-12, cut down for the Design role. Removed: the `scripts/` launcher (it downloads and runs a binary), live mode, hooks, doctor, pin, and every command and reference file except `typeset`, `layout`, `colorize` and `craft-floor`. The rules marked (ours) are the owner's own additions to this skill, not upstream.

This skill gives you the tools and permission to create design that earns to be called out-of-distribution craft: production-grade output, a clear point of view, deep understanding of the brief and its audience, and exceptional craft.

Core principles:
- Go all out. No hedging, no shortcuts. The deliverable must be complete (except assets the user must provide).
- Verify in bounded passes, not a loop: build fully, inspect once with a batched round (desktop and mobile together for email), fix everything it shows in one batch, confirm with at most one more round, and stop polishing.

## Setup

1. Read the brief, `voice.md` and any brand colors, logo or DESIGN.md the project has, without inventing missing context. There is no context launcher in this copy.
2. Load the reference for the request: [reference/typeset.md](reference/typeset.md), [reference/layout.md](reference/layout.md) or [reference/colorize.md](reference/colorize.md).
3. Read [reference/craft-floor.md](reference/craft-floor.md) immediately before any visual edit, including small refinements. It carries the quality floor and the things to refuse.

## How to design

- **The brief wins.** Honor pinned aesthetics, eras, materials, fonts and palettes even when they conflict with a saturated-pattern warning. Redirecting a clear brief toward your taste is failure.
- **Refinement preserves; redesign replaces.** Refinement keeps the incumbent identity, behavior, copy and everything outside scope. Ask before replacing factual copy or adding claims. A redesign needs the owner's approval first.
- **Loaded symbols stay out of the decoration.** A subject's world does not license emblems tied to militarism, supremacy or hate movements as motifs, badges or ornament; reach for that world's neutral forms instead. Content that documents such a symbol as fact stays as it is.
- **Boxy metrics anti-pattern (ours):** Never wrap hero metrics in large white or dark rectangular cards (the out-of-meta SaaS template). Use integrated status ticker strips or inline ledges instead.
- **Mobile phrase wrapping (ours):** Multi-line display headings in segmented or tonal languages (such as Vietnamese) must wrap by complete semantic clauses (`white-space: nowrap` on phrase blocks). Never allow single words to drop alone.
- **Zero overkill platform previews (ours):** When demonstrating content repurposing across social media, avoid nested button tabs or click-to-view overlays; use a smooth horizontal touch-scroll rail showing authentic mobile phone frames side by side.
- **Kicker redundancies (ours):** Never place an eyebrow badge above a hero heading if it duplicates claims, hours or promises in the main headline. Let the heading carry its own weight.

## Modes

The mode names what the visitor's success looks like on this surface.

- **Persuade:** the visitor decides and acts; design is the product. Landing pages, marketing, campaigns, pricing.
- **Operate:** the visitor completes a task. App UI, dashboards, tools. Scanability and consistency outrank expression.
- **Read:** the visitor understands something. Docs, articles, guides.
- **Experience:** the visitor is inside the work itself. Portfolios, galleries, showcases.

Banners and campaign emails are almost always Persuade.

## Commands

| Command | Description | Reference |
|---|---|---|
| `typeset [target]` | Improve typography hierarchy and fonts | [reference/typeset.md](reference/typeset.md) |
| `layout [target]` | Fix spacing, rhythm and visual hierarchy | [reference/layout.md](reference/layout.md) |
| `colorize [target]` | Add strategic color to monochromatic work | [reference/colorize.md](reference/colorize.md) |

- **Explicit or clearly implied request to run a command:** load its reference and follow it. Ask once if two commands fit.
- **Otherwise:** treat the request as general design work and apply the craft floor.

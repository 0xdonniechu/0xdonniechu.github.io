---
name: youtube-packaging
description: Use when the owner supplies a video (transcript, notes, script or a Shorts idea) and wants on-brand YouTube titles, thumbnail concepts, a video description, A/B packaging options, or precise revisions of a thumbnail brief. Default output is brief-only, as text. Titles and descriptions are written from the team's formats/youtube.md (title 100 characters, description 5,000 characters). Image generation is optional and only on the owner's explicit request. Never publishes or changes anything on YouTube.
metadata:
  version: 1.0.0
  updated: 2026-09-02
---

Adapted from ericosiu/ai-marketing-skills `packaging-youtube-thumbnails` (MIT, commit d2237ec) by 0xdonniechu, 2026-11-08: removed the usage-reporting and version-check preamble, all bundled scripts and the image-generation requirement; default is brief-only.

# YouTube Packaging

## Overview

Turn new video content into differentiated packages: exact title, thumbnail concept, thumbnail copy and a description. Use a saved channel profile and any numbers the owner shares. Keep three things separate: channel identity, episode packaging, and performance learning.

**Team rules.** Draft only. This skill never uploads, edits or publishes anything on YouTube, fetches nothing, calls no API and uses no keys. The owner approves and posts. Brand voice: `voice.md` at the team root.

**Limits come from the team's file.** Write titles and descriptions from `formats/youtube.md` in the team's formats/ folder: title 100 characters, description 5,000 characters. Thumbnail spec (aspect ratio, minimum width, file types and sizes) and Shorts limits are in the same file. Where the file says a value was not found (for example tags, safe zone for Shorts), say so and do not invent one. Check the character counts of every title and description you write.

## Modes

**Brief-only mode (default).** Return titles, thumbnail concepts, thumbnail copy, composition and component inventory, descriptions, scores and risks as text. No images are generated.

**Render mode (optional).** Only when the owner explicitly asks for rendered thumbnails AND an image tool is already available in the session, use it for raster generation or editing, one call per variant, and save to a new versioned file under the team's `work/` folder each time (never overwrite a shown version). Use only a local image tool; never send drafts to an outside service. The owner supplies any account or key outside this skill; this skill never asks for one. If no image tool is available, stay in brief-only mode and say why. Use [references/thumbnail-brief-contract.md](references/thumbnail-brief-contract.md) for the prompt shape.

## Channel profile

Resolve the profile in order: a path the owner gives, then `work/youtube-channel-profile.md` in the team folder. If neither exists, run an identity bootstrap.

- **Bootstrap or refresh only** when no usable profile exists, the owner asks, or the owner supplies new brand examples. The owner supplies roughly 20 recent long-form thumbnails (files or screenshots); this skill does not browse the channel. Save a profile using [references/channel-profile-template.md](references/channel-profile-template.md). Do not refresh merely because time has passed.
- **When a profile exists:** load it before developing hooks. Do not re-audit the channel or rewrite the profile. Use its identity rules, approved references and avoid list. Treat the new transcript, notes, brief and owner additions as one source pack. The latest explicit owner instruction wins.

## Workflow

### 0. Apply co-design calibration

When the owner names a prior package as successful or preferred, inspect it before developing new hooks. Extract five things: the promise pattern, title pattern, visual grammar, rejected tendencies, and which elements must repeat versus vary. If the reference is a platform screenshot, separate the creative from platform chrome (progress bars, duration badges, player controls, surrounding titles, metrics) and exclude the chrome from any prompt.

Keep the evidence classes apart: a direct correction or stated preference is workflow evidence and applies immediately; public views or one result are directional context, not causal proof; repeated comparable results belong in the performance readback. Persist a preference in the profile only when the owner asks, with the evidence class and an incremented profile version and date. Preserve distinct promise lanes; do not copy a podium, trophy or comparison device when the new episode has no matching relationship.

### 1. Read the source pack

Read all supplied content. Extract the viewer, thesis, verdict, proof, tension, stakes, consequence and caveats. Exclude incomplete tests from claims. Verify product and model spelling. For roundups and tool lists, count every named item, then count only items with enough explanation or proof to support the promise, and use the substantive count in numeric titles and thumbnail copy. Find the two or three strongest content spikes (achieved numbers, concrete outputs, strong opinions, mistakes, sharp lines) and let them decide whether to lead with a list, personal proof, outcome, verdict or framework.

For show-and-tell episodes, name the exact artifact, result screen, prop or before/after that proves the promise and prefer it as the dominant object. For future-of-work, framework and trend episodes, state what the viewer can build, change, decide or do differently, and keep that as the title's main promise when the source supports it. Treat a product or moment as a trend only after the owner confirms recent sustained attention; put a product in the title only when a substantial share of the episode delivers a product-centered promise.

### 2. Use performance evidence (optional)

If the owner pastes numbers from YouTube Studio for earlier videos, read [references/performance-readback.md](references/performance-readback.md). Surface a 72-hour subject collision (a recent upload on the same subject) before proposing packages. Never infer causality from raw public views or fewer than three comparable results.

### 3. Create the packages

Read [references/packaging-rubric.md](references/packaging-rubric.md). Use distinct lanes: (1) verdict or contrarian tension, (2) specific proof, outcome or transformation, (3) decision utility, framework or real-work test. Make the requested number of packages (default three). Keep set IDs and headline-thumbnail pairings stable through revision rounds. For each: exact title, thumbnail copy (zero to four words preferred), composition, component inventory, hook logic, risk. The options must be different promise hypotheses, not cosmetic treatments. Apply the rubric's simplicity and semantic-clarity gates before scoring. Score every package, recommend one.

When the source has real creator usage, favor personal proof (a concrete count, a named product, a real job or outcome, a workflow to copy) over abstract category language. Keep a practical promise and a career-identity promise as distinct lanes when both are supported.

### 4. Write the video description

Write the description from `formats/youtube.md` (5,000 characters maximum; check the count). The first lines carry the promise and the main entities. Add chapters only from timestamps the owner supplies. Do not state claims the source does not support. Mark product or offer claims `[needs source]` when the owner has not approved wording.

### 5. Verify visible brands

If the thumbnail shows an app, product or model mark, name which mark is meant (app icon, parent-company logo, product family mark, campaign art, mascot, wordmark) and ask the owner to supply the official file. Record the classification in the brief. If the owner corrects a mark, treat the correction as a hard constraint across every variant.

### 6. Encode the promise as visual hierarchy

Translate relational language into geometry: `wins`/`king`/`best` makes the winner the largest object; `easier` centers and enlarges the easy option; `versus` compares equivalent entities; `use cases` makes the product the hero with cases grouped beneath; `chases`/`replaces` shows unambiguous direction. Run a copy-off test: hide the headline and describe the visual relationship in one sentence. Reject the concept if it implies the opposite winner or needs arrows and question marks to explain. As a starting ratio (unsourced), make the hero about 2 to 3 times the area of each subordinate mark. For episodes about humans managing AI agents, show the creator's role and the agent's role; do not imply autonomous replacement when the content covers delegation or review.

### 7. Revise from a feedback matrix

Convert feedback into a matrix: set and headline, target variant, locked control variant, required changes, invariants, exact copy, rejected implications. Preserve variants the owner approved or did not target. Version changed variants and keep prior ones. For each revised set, check at feed size: the requested hero is the first read, the visual cannot be read the opposite way, and any count in the copy is supported by the content. If the video covers more items than a small displayed subset, prefer non-numeric copy over an unsupported total.

### 8. Hand back for review

Group output by headline. Under each headline show A and B with their thumbnail copy, and one feedback line: `A / B / neither / combine` plus `Changes needed`. After revisions, show the full current comparison set including unchanged controls.

## Deliverable

Return: profile and review date, evidence gaps, the requested package count, one recommendation, titles with character counts, thumbnail briefs, the description with character count, risks, and the feedback structure. Never publish or change a live YouTube asset.

# Thumbnail Brief Contract

Adapted from ericosiu/ai-marketing-skills `packaging-youtube-thumbnails/references/image-contracts.md` (MIT, commit d2237ec): scripts, guard commands and archive handoff removed. Use it to write a thumbnail brief as text, or as the prompt when the owner asks for a render and an image tool is available.

Thumbnail file specs (ratio, minimum width, formats, size limits): the team's `formats/youtube.md`. The pixel margins below are the original author's heuristics (unsourced); check them by eye on the brief or the render.

## Output layout (render mode only)

```text
<output-root>/<video-slug>/
  manifest.md
  variant-01/variant-01-v001.png
  variant-02/variant-02-v001.png
```

Use `v002`, `v003` and descriptive suffixes such as `-logo-only` for revisions. Never overwrite accepted or previously shown versions.

## Brief shape

One brief per distinct asset. Label every input image by role.

```text
Asset type: finished YouTube thumbnail, 16:9 landscape (size per formats/youtube.md)
Primary request: <package promise>
Input images: label the subject, channel style, and each verified brand asset by role
Scene/backdrop: <channel-supported setting>
Subject: <one focal subject and one dominant relationship>
Component budget: no more than three major visual groups plus one short text block; a comparison pair may be one grouped unit
Component inventory: <group 1>; <group 2>; <group 3>; <text block>
Style/medium: high-end YouTube thumbnail; readable at phone size
Composition/framing: <placement, scale, negative space, timestamp-safe corner>
Color palette: <channel palette>
Text (verbatim): "<exact copy>"
Edge safety (unsourced heuristic): keep complete critical marks clear of the edges, and keep the lower-right corner (where the duration badge sits) free of critical marks and copy
Constraints: exact text once; complete official marks; no extra text; no watermark; remove or group instead of shrinking
Avoid: tiny UI, redundant props, unrelated logos, unsupported claims
```

If the design is text-free, state: `No text, letters, numbers, punctuation, labels, or UI copy anywhere.`

## Simplicity check

At 320x180, the focal relationship must be identifiable in one second. Fail the variant if it exceeds three major visual groups, lacks a clear hierarchy, or depends on tiny UI or several secondary props. Prefer removal or grouping over shrinking. A complex official mark counts as one group when it reads as one silhouette. Record the component inventory. If it cannot be expressed as three groups plus one text block, do not score or render the candidate.

## Brand check

Before a mark appears: the owner supplies the official asset; record the product or model spelling; decide whether the mark identifies the company, app, product family or exact model; distinguish a primary logo from campaign art; prefer the exact-model mark; accept version binding only from the official asset or an official page that labels it for that version. In the brief, name each supplied file's role and forbid known substitutions, generic robots and added wordmarks. Do not store third-party brand assets in the team's skills folder.

## Relationship check

Write the intended relationship as one literal sentence before rendering, then encode it through scale and placement. The hero must be the first read at 320x180. A winner, easier option or recommended product usually takes 2 to 3 times the area of each subordinate mark (unsourced). Cross-outs sit directly over the rejected objects and never touch the hero. A chase or replacement shows direction through pose or motion. Remove arrows, question marks and connector clutter when size and position already communicate the relationship. Hide the copy during review: fail the image if what remains can reasonably communicate the opposite claim.

## Precise edit (render mode only)

```text
Primary request: replace only <target> with <replacement> in the same approximate bounds
Allowed edit area: <describe the region>
Invariants: preserve face, pose, crop, background, lighting, typography, exact text, and every unrelated object
Constraints: change only the requested region; no reframing; no extra text; no watermark
```

Treat every edit as provisional. Compare the result with the accepted version by eye at original size; if anything outside the region changed, reject it and retry once from the last accepted version with a tighter prompt. After a second failure, label the result a controlled re-render and keep the last accepted version current.

## Review delivery

Show each current variant separately. Group A/B comparisons under their shared headline, keep unchanged controls visible after revisions, and give one copyable feedback line per set.

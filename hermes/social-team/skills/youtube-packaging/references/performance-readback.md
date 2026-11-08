# Performance Readback (manual)

Adapted from ericosiu/ai-marketing-skills `packaging-youtube-thumbnails/references/performance-learning.md` (MIT, commit d2237ec). The original ran a local ledger with bundled scripts; here the owner pastes numbers and the comparison is done by hand in the conversation. Nothing is fetched and nothing is stored outside the team's `work/` folder.

## Inputs

Numbers the owner copies from YouTube Studio (Reach and Engagement reports) at 24, 72 and 168 hours after upload, for each video: impressions, click-through rate, retention (or average view duration and video length), views, and Browse / Suggested impressions and CTR when available. Public view counts are context only. Do not ask for screenshots with viewer-level data, cookies or credentials.

Describe each video with its package: hook lane, thumbnail copy, composition, and a `comparison_group` that names a genuinely comparable format (for example `business-use-cases`, `operator-framework`).

## Diagnosis

Compare only videos in the same comparison group and the same measurement window. Require at least three comparables, otherwise record the result and learn no rule.

| Evidence pattern | Classification | Packaging response |
| --- | --- | --- |
| Normal impressions, materially weaker CTR | packaging weakness | Rework promise and thumbnail clarity |
| Weak impressions, healthy CTR and retention | topic or distribution weakness | Reconsider topic breadth, timing, audience fit |
| Healthy CTR, materially weaker retention | promise-content mismatch | Align the package with the opening and the delivered proof |
| Weak CTR, materially stronger retention | undersold content | Make the value and stakes more concrete |
| Fewer than three comparables | insufficient evidence | Record the result; do not learn a rule |

"Materially" is a judgment call: state the numbers you compared. These are triage, not causality. Check traffic sources, native A/B test results and audience context first. YouTube's native title-and-thumbnail test result takes precedence over sequential swaps.

## Lessons

One result is a hypothesis. A durable lesson needs three distinct videos in the same comparison group with 72-hour-or-later numbers, and the owner's explicit review. A lesson applies only to that comparison group. Re-review lessons after 90 days or 20 newer comparable uploads, and retire one when three newer comparable results contradict it. Never promote a lesson just because a package looks successful in hindsight.

## Cadence

Manual readback after each packaged upload. No scheduled or automatic collection.

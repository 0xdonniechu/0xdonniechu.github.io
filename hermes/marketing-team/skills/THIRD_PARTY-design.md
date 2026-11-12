# Third-party skills (Design)

Copied 2026-11-12 by 0xdonniechu from Zoro's live Hermes profile (`~/.hermes/profiles/zoro/skills`) into `skills/`. Licences are in `skills/LICENSES/<owner>_<repo>.LICENSE`.

| Skill folder | Source | Licence | What was changed |
|---|---|---|---|
| `html-banner-design` | Own skill (author "Donnie & Hermes", v1.0.0) | MIT | One note added under the canvas table: platform limits come from `../social/formats/`, which wins. |
| `email-newsletter-design` | Own skill (author "Donnie & Hermes", v1.0.0) | MIT | Copied as is. |
| `bento-carousel-design-v3` | Own skill (author "Donnie & Hermes", v1.3.0) | MIT | Removed section 4 "Pipeline Integration" and two engine-specific pitfalls (a publishing pipeline's internals, not design guidance), plus the line about retrofitting scheduled articles; a provenance line added. |
| `impeccable` | pbakaus/impeccable tag `skill-v4.5.2`, commit d631a88 (`LICENSES/pbakaus_impeccable.LICENSE`) | Apache-2.0 | Cut down to `SKILL.md` plus four references (`craft-floor`, `typeset`, `layout`, `colorize`), all read in full. Removed: `scripts/` (a launcher that downloads and runs a binary), live mode, hooks, doctor, pin, every other command and its reference file (they depend on those scripts or on web-app work). In the kept files the script scan steps, live-mode sections and links to removed files were cut. `SKILL.md` was rewritten for the Design role; the owner's own rules (Vietnamese phrase wrapping, no boxy metric cards, no kicker above a heading, platform-preview rail) are kept and marked "(ours)". |

## Not vendored

`pretext` (NousResearch/hermes-agent `optional-skills/creative/pretext`, MIT, commit 2bd378ed1b) was on Zoro's live profile but is not in this repo. It builds interactive web demos that import `@chenglou/pretext` and fonts from esm.sh and CDNs at run time, which is against the shared rule on remote code, and it is not a banner or email tool (email cannot run scripts). A copy is kept outside the repo. To restore it, add the folder back and say so here.

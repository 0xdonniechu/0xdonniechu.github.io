# 0xdonniechu.github.io: static research and planning pages published with GitHub Pages

## What it does
69 static HTML pages (plus about 47 markdown files and 16 images: png, jpg, svg), no build step, no JavaScript (no `<script>` tags), Google Fonts via CSS links on 68 of 69 pages. Folders: `research`, `pm`, `marketing`, `hermes`, `intro-video`; top-level `index.html`, `thesis.html`, `synthesis.html`, `debrief-2026-10-31.html`. `.nojekyll` is present; `vercel.json` only sets `cleanUrls=false`.
GitHub Pages serves branch `main` from `/` (legacy build) at https://0xdonniechu.github.io/. A push or merge to `main` publishes every changed page publicly.
A bug costs: a wrong or private claim, a leaked token or private name goes live. No data is lost.

## Verify
There is no test suite, and none is invented here. Verify is currently manual:
- `git diff --stat` reviewed.
- Open the changed HTML files locally, or serve them with `python3 -m http.server` (owner-only visual check: write "not run" unless it was done).
- Secret scan: `grep -rEn "ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY" --include=*.html --include=*.md .` (GitHub token, API key, AWS key id or private key patterns) must print nothing.
- All three are manual; none is a builder `--check`.

## HARD: the main session does it directly, then hard-reviewer
- Content is rated by its own kind (a typo is EASY, new pages MEDIUM, and so on); a merge or push to `main` always needs the owner's approval because it publishes.
- Changing Pages settings, `vercel.json`, `CNAME` or `.nojekyll`.
- Anything with secrets, private names or unreleased business data.

## MEDIUM: builder builds, reviewer reviews
- New or restructured pages.
- Shared CSS, or the site's shared layout or navigation across pages.
- Research claims presented as facts.

## EASY: transcriber or builder, no review
- Typos, wording, adding a source link.

## Rules
- The repo's default git identity is `0xdonniechu`. Before any GitHub write, check `gh api user --jq .login` is `0xdonniechu`. Never `gh auth switch`.
- No Ambysto workflow, accounts or memory apply in this repo.
- Branches are named by slug. A push or merge to `main` publishes, so the main session does it only with the owner's approval.
- This file is published at /CLAUDE.md because Pages serves every tracked file; keep private names and paths out of it.
- Web rules: follow `webdev-playbook` (sibling repo of the same owner).
  - Browser baseline is Baseline Widely available (a stated assumption; the owner may change it).
  - Pages stay no-JS unless the owner approves.
  - Keep `<meta name="viewport">` and `<html lang=...>` on every page.
  - New pages need an accessible heading order, alt text on images and readable contrast.
  - Never silently change the baseline or add a dependency, CDN script or tracker.

## Session state
- Work in progress lives in `HANDOFF.md` (must stay untracked and gitignored). If it exists at session start, read it before anything else. Update it with `/handoff` before `/clear`; delete it once the goal is finished and recorded.
- Durable facts go in this file; tasks in the tracker. `HANDOFF.md` holds only where the current goal stands.

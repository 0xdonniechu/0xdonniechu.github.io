# 0xdonniechu.github.io: static research and planning pages published with GitHub Pages

## What it does
69 static HTML pages (plus 46 markdown files and a few images), no build step, no JavaScript (no `<script>` tags), Google Fonts via CSS links. Folders: `research`, `pm`, `marketing`, `hermes`, `intro-video`; top-level `index.html`, `thesis.html`, `synthesis.html`, `debrief-2026-10-31.html`. `.nojekyll` is present; `vercel.json` only sets `cleanUrls=false`.
GitHub Pages serves branch `main` from `/` (legacy build) at https://0xdonniechu.github.io/. A push or merge to `main` publishes every changed page publicly.
A bug costs: a wrong or private claim, a leaked token or private name goes live. No data is lost.

## Verify
There is no test suite, and none is invented here. Verify is currently manual:
- `git diff --stat` reviewed.
- Open the changed HTML files locally, or serve them with `python3 -m http.server` (owner-only visual check: write "not run" unless it was done).
- Secret scan: `grep -rEn "ghp_|sk-|api[_-]?key|token" --include=*.html --include=*.md .` must show no real secret.
- All three are manual; none is a builder `--check`.

## HARD: the main session does it directly, then hard-reviewer
- Anything that publishes: a merge or push to `main`, changing Pages settings, `vercel.json`, `CNAME` or `.nojekyll`.
- Anything with secrets, private names or unreleased business data.

## MEDIUM: builder builds, reviewer reviews
- New or restructured pages.
- Shared CSS, or the site's shared layout or navigation across pages.
- Research claims presented as facts.

## EASY: transcriber or builder, no review
- Typos, wording, adding a source link, README-like text.

## Rules
- Git author is `0xdonniechu <donniechu.eth@gmail.com>`. Before any GitHub write, check `gh api user --jq .login` is `0xdonniechu`. Never `gh auth switch`.
- No Ambysto workflow, accounts or memory apply in this repo.
- Branches are named by slug. Never push to `main` directly. The main session merges only after the owner approves, because a merge publishes.
- Web rules: follow `webdev-playbook` (`~/work/0xdonniechu/webdev-playbook`).
  - Browser baseline is Baseline Widely available (a stated assumption; the owner may change it).
  - Pages stay no-JS unless the owner approves.
  - Keep `<meta name="viewport">` and `<html lang=...>` on every page.
  - New pages need an accessible heading order, alt text on images and readable contrast.
  - Never silently change the baseline or add a dependency, CDN script or tracker.

## Session state
- Work in progress lives in `HANDOFF.md` (must stay untracked and gitignored). If it exists at session start, read it before anything else. Update it with `/handoff` before `/clear`; delete it once the goal is finished and recorded.
- Durable facts go in this file; tasks in the tracker. `HANDOFF.md` holds only where the current goal stands.

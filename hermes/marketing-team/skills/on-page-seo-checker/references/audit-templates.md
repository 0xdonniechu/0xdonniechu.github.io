> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/tune/on-page-seo-checker/references/audit-templates.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# On-Page SEO Auditor - Compact Output Templates

Use one shape: evidence -> checks -> issues -> fix -> score. Keep only sections that match page type.

> Weights, benchmarks and thresholds in this file (content length by query type, keyword density, internal link counts, image sizes, grade boundaries) are conventions from the original skill, not verified facts (unsourced). Section scores are your judgement from the evidence (Estimated). Core Web Vitals values are per the original skill; verify at web.dev/vitals. Missing data is "không có số".


## Shared Conventions

| Item | Rule |
|------|------|
| Status | `✅` pass, `⚠️` partial risk, `❌` fail |
| Severity | `P0` blocks ranking/indexing, `P1` suppresses performance, `P2` hygiene |
| Evidence | Page state, date read, competitor set (public pages), inferred keyword |
| Scores | `/10` sections; final roll-up `/100` |

## Step Map

| Step | Focus | Must Capture |
|------|-------|--------------|
| 1 | Setup | URL, keyword, page type, goal |
| 2 | Title | length, keyword position, clickability |
| 3 | Meta description | length, CTA, intent match |
| 4 | Headers | single H1, hierarchy, keyword coverage |
| 5 | Content quality | depth, proof, freshness, readability |
| 6 | Keyword usage | placement, related terms, overuse |
| 7 | Internal links | count, anchor quality, gaps |
| 8 | Images | alt text, file names, size, format, lazy load |
| 9 | Technical on-page | URL, canonical, speed, mobile, schema |
| 10 | Quick content scan | 17 page-level checks |
| 11 | Summary | priorities, quick wins, checklist |

## Setup

Page URL, target keyword, secondary keywords, page type, business goal, competitor set.

## Title Tag

Current title, character count, length 50-60 chars (unsourced), primary keyword, front-loaded wording, intent/clickability, recommended title, score.

## Meta Description

Current description, character count, length 150-160 chars (unsourced), natural keyword, CTA, promise match, recommended description, score.

## Headers

Current H1/H2/H3 hierarchy, single H1, H1 keyword coverage, logical nesting, subtopic coverage, score.

## Content Quality

Word count, read time, depth vs competitors, unique proof, freshness, readability, E-E-A-T signals, intro answer, chunking, examples/stats, FAQ/conclusion/CTA, score.

## Keyword Usage

Primary keyword, density, title/meta/H1/first 100 words/H2-H3/URL/image alt status, related terms, missing terms, overuse risk, score.

## Internal Links

Total internal links, descriptive anchors, topical depth, broken/misdirected links, recommended additions, score.

## Images

| Image | Alt Text | File Name | Size/Format | Lazy Load | Status | Fix |
|-------|----------|-----------|-------------|-----------|--------|-----|
| [image] | [alt or missing] | [filename] | [KB/WebP/JPG] | [yes/no] | ✅/⚠️/❌ | [fix] |

| Image check | Status | Notes | Fix |
|-------------|--------|-------|-----|
| File names are descriptive | ✅/⚠️/❌ | [notes] | [fix] |
| Lazy loading enabled where appropriate | ✅/⚠️/❌ | [notes] | [fix] |

Score: [X]/10.

## Technical On-Page

URL/slug, canonical, mobile, page speed, HTTPS, schema markup, score.

## Quick Content Scan

A flag for deeper editorial review, not a publish verdict.

| Check | Status | Notes |
|-------|--------|-------|
| Intent alignment | ✅/⚠️/❌ | [notes] |
| Direct answer early | ✅/⚠️/❌ | [notes] |
| FAQ coverage | ✅/⚠️/❌ | [notes] |
| Closing resolves the question | ✅/⚠️/❌ | [notes] |
| Heading hierarchy | ✅/⚠️/❌ | [notes] |
| Summary/takeaways | ✅/⚠️/❌ | [notes] |
| Tables where needed | ✅/⚠️/❌ | [notes] |
| Schema markup | ✅/⚠️/❌ | [notes] |
| Section chunking | ✅/⚠️/❌ | [notes] |
| Data precision (sourced numbers only) | ✅/⚠️/❌ | [notes] |
| Citations for claims | ✅/⚠️/❌ | [notes] |
| Visible date / freshness | ✅/⚠️/❌ | [notes] |
| Internal link graph | ✅/⚠️/❌ | [notes] |
| Content consistency | ✅/⚠️/❌ | [notes] |
| First-person experience | ✅/⚠️/❌ | [notes] |
| Author identity | ✅/⚠️/❌ | [notes] |
| Disclosure statements | ✅/⚠️/❌ | [notes] |

**Quick Score**: [X]/17 passing

## Step 11: Generate Audit Summary

| Area | Score | Top Issue | First Fix |
|------|:-----:|-----------|-----------|
| Title | [X]/10 | [issue] | [fix] |
| Meta | [X]/10 | [issue] | [fix] |
| Headers | [X]/10 | [issue] | [fix] |
| Content | [X]/10 | [issue] | [fix] |
| Keywords | [X]/10 | [issue] | [fix] |
| Links | [X]/10 | [issue] | [fix] |
| Images | [X]/10 | [issue] | [fix] |
| Technical | [X]/10 | [issue] | [fix] |
| Quick content scan (scaled) | [scaled score]/20 | [issue] | [fix] |

Scaling rule: `scaled score = round(passed_checks / 17 * 20)`. Finish with P0/P1/P2 issues, quick wins, competitor gap snapshot, and action checklist.

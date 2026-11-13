# Rank Tracking Routine (manual, from owner exports)

Adapted from aaron-he-zhu/aaron-marketing-skills `seo-geo/evaluate/rank-tracker/references/tracking-setup-guide.md` @ 61075e8 (Apache-2.0), rewritten for a team with no rank-tool connectors, alerts or dashboards. Numbers in this file (counts, frequencies, thresholds) are rules of thumb from the original skill (unsourced).

## The monthly routine

| Step | Who | Action |
|------|-----|--------|
| 1 | Owner | Export the Search Console performance report (queries and pages) for the last full month and for the month before; note the country and device filters. |
| 2 | Owner | For a few priority queries, hand-check the live result page and any AI answer; write the date, surface and whether our URL appears. |
| 3 | Lelouch | Join the two exports by query and page; compute the delta; label each cell with its file and date range. |
| 4 | Lelouch | Write `work/seo/readout-<YYYY-MM>.md` from the templates; list what the owner still has to export. |

No alerts, schedules or messages are sent from this role. A "drop alert" is a line in the readout.

## Keyword selection

| Include | Rule |
|---------|------|
| Revenue and brand terms | Always |
| Page 1-3 terms | Current opportunity set |
| Strategic terms | Product priorities even if volume is low or "không có số" |
| Content investments | Every page the team is actively improving |

Skip broad one-word terms, low-volume misspellings and terms with no target page. Keep Vietnamese spellings with and without diacritics as separate rows.

## Interpretation rules

| Pattern | Meaning | Action |
|---------|---------|--------|
| Day-to-day or week-to-week movement of one or two positions | Normal volatility | Track the trend, do not react |
| Sudden drop that recovers in a few days | Test or data variation | Monitor |
| Steady decline over two or more weeks | Probably real | Investigate content, links, SERP, technical |
| Many keywords drop together | Algorithm or technical issue | Check crawlability and indexation (technical-seo-checker) |
| One URL drops across terms | Page-level issue | Check noindex, 404, speed, content decay (on-page-seo-checker, seo-content-writer refresh) |
| Competitor surges | Market or content shift | Read their page; link counts only if the owner provides them |

Generic "click loss per position" tables were removed (unsourced). Use the page's own click history from the export instead.

## Data quality checks

| Check | Frequency |
|-------|-----------|
| Hand-check a handful of queries against the export | Monthly |
| Confirm date range, country and device filters match between the two exports | Every readout |
| Note when a page was changed, so a delta is not attributed to the wrong cause | Every readout |

## Changing the data source

If the owner switches export source, keep both for a few weeks, compare systematic differences and say in the readout which is the baseline. A small difference between sources is normal; document it before comparing history.

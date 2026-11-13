> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/evaluate/rank-tracker/references/ranking-analysis-templates.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Ranking Analysis Output Templates

Compact templates for rank tracking setup, movement analysis, SERP features, GEO visibility, competitors, and reporting.

> Fill every number from the owner's export (name the file and date range). Where none exists write "không có số"; never estimate. Search Console positions are averages over the date range.

## 1. Setup And Snapshot

```markdown
## Rank Tracking Setup
**Domain**: [domain] | **Location**: [country/city] | **Device**: [mobile/desktop/both] | **Language**: [language] | **Frequency**: [daily/weekly]

| Keyword | Impressions (export) | Avg position (export) | Type | Priority | Target URL |
|---------|----------------------|-----------------------|------|----------|------------|
| [keyword] | [number or không có số] | [number or không có số] | Primary/Secondary/Brand | H/M/L | [URL] |

**Competitors**: [domain 1], [domain 2], [domain 3]
**Categories**: Brand [X], Product [X], Informational [X], Commercial [X]

## Current Ranking Snapshot -- [date]
| Position Range | Count | Share |
|----------------|-------|-------|
| #1 | [X] | [Y]% |
| #2-3 | [X] | [Y]% |
| #4-10 | [X] | [Y]% |
| #11-20 | [X] | [Y]% |
| #21-50 | [X] | [Y]% |
| #51-100 | [X] | [Y]% |
| Not ranking | [X] | [Y]% |

| Keyword | Position | URL | SERP Features | Change |
|---------|----------|-----|---------------|--------|
| [kw] | [pos] | [URL] | [feature] | [+/-] |
```

## 2. Movement Analysis

```markdown
## Ranking Change Analysis
**Window**: [start] to [end]

| Metric | Start | End | Change |
|--------|-------|-----|--------|
| Avg position | [X] | [Y] | [+/-Z] |
| Keywords in Top 10 | [X] | [Y] | [+/-Z] |
| Keywords in Top 3 | [X] | [Y] | [+/-Z] |

| Segment | Keyword | Old -> New | Clicks change (export) | Hypothesis | Action |
|---------|---------|------------|---------------------|------------|--------|
| Improvement | [kw] | [old -> new] | [number or không có số] | [possible cause] | [protect/expand] |
| Decline | [kw] | [old -> new] | [number or không có số] | [likely factor] | [investigate/refresh] |
| New | [kw] | [none -> pos] | [number or không có số] | [new content/intent] | [monitor] |
| Lost | [kw] | [pos -> none] | [number or không có số] | [index/intent/competition] | [recover] |

Hypotheses are based on available signals, not confirmed causes.
```

## 3. SERP Feature And GEO Tracking

```markdown
## SERP Feature Tracking

| Feature | Your Count | Competitor (public page, dated) | Opportunity |
|---------|------------|----------------|-------------|
| Featured snippets | [X or không có số] | [Y or không có số] | [win/defend] |
| People Also Ask | [X or không có số] | [Y or không có số] | [answer gaps] |
| Image / video / local pack | [X or không có số] | [Y or không có số] | [asset need] |

| Keyword | Feature | You Own? | Current Owner | Winnable? |
|---------|---------|----------|---------------|-----------|
| [kw] | [feature] | Y/N | [domain] | H/M/L |

## AI/GEO Visibility (from the owner's hand-checked table)
| Keyword | AI answer present (date, surface) | You cited? | Citation position | Content Gap |
|---------|---------------------|------------|-------------------|-------------|
| [kw] | Y/N | Y/N | [pos] | [definition/stat/source gap] |

**Citation rate**: [your citations] / [checks made] = [Z]%, only with the number of checks stated; a single check is one observation, not a rate
```

## 4. Competitor Comparison (only with owner-provided numbers or dated public pages)

```markdown
## Competitor Ranking Comparison

| Domain | Keywords Ranked | Avg Position | Source |
|--------|-----------------|--------------|--------|
| [your site] | [X or không có số] | [Y or không có số] | [export, date range] |
| [competitor] | [X or không có số] | [Y or không có số] | [source or không có số] |

| Keyword | Your Rank | Competitor Rank | Winner | Threat / Opportunity |
|---------|-----------|-----------------|--------|----------------------|
| [kw] | [rank] | [rank] | [domain] | [note] |

| Competitor | Keyword | Movement | Threat Level |
|------------|---------|----------|--------------|
| [domain] | [kw] | [+/- positions] | H/M/L |
```

## 5. Ranking Performance Report

```markdown
# Ranking Performance Report
**Domain**: [domain] | **Period**: [start] to [end] | **Generated**: [date]

## Executive Summary
**Overall trend**: [Improving/Stable/Declining]

| Metric | Value | vs Last Period | Status |
|--------|-------|----------------|--------|
| Total tracked keywords | [X] | [+/-Y] | [status] |
| Keywords in Top 10 | [X] | [+/-Y] | [status] |
| Average position | [X] | [+/-Y] | [status] |
| AI citation rate | [X]% of [n] checks, or không có số | [+/-Y] | [status] |

**Wins**: [list]
**Concerns**: [list]
**Opportunities**: [list]

| Timing | Recommendation | Expected Impact (hypothesis) |
|--------|----------------|-----------------|
| Immediate | [action] | [impact] |
| This month | [action] | [impact] |
| Next quarter | [action] | [impact] |

**Next readout**: [date] | **Focus areas**: [areas] | **Owner must export**: [files]
```

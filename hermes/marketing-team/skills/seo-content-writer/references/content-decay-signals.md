> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/content-writer/references/content-decay-signals.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Content Decay Signals

> Numbers in this file (character counts, word counts, link counts, thresholds) are rules of thumb from the original skill, not verified platform facts (unsourced). Where a number matters, the owner confirms it. Data about the site comes from public pages or numbers the owner exports; missing means "không có số".

The severity bands, composite weights and refresh frequencies below are the original skill's rules of thumb (unsourced). Traffic, ranking and CTR inputs come only from the owner's Search Console or analytics export; without one, write "không có số" and score from on-page signals only.

## Primary Signals (High Reliability)

### 1. Organic Traffic Decline

| Severity | Threshold (MoM) | Action |
|----------|-----------------|--------|
| Watch | 10-20% decline | Add to monitoring list |
| Warning | 20-40% decline | Schedule refresh within 2 weeks |
| Critical | 40-60% decline | Refresh this week |
| Emergency | >60% decline | Investigate immediately (may be technical) |

**False positive check**: Rule out seasonality (compare YoY), algorithm updates, technical issues, tracking changes.

### 2. Ranking Position Drops

| Severity | Threshold (2-week avg) | Action |
|----------|------------------------|--------|
| Watch | 1-3 positions lost | Monitor |
| Warning | 3-5 positions lost | Investigate cause |
| Critical | 5-10 positions lost | Immediate refresh |
| Emergency | Off page 1 to page 3+ | Priority refresh or rewrite |

### 3. Click-Through Rate Decline

| Severity | Threshold | Action |
|----------|-----------|--------|
| Watch | CTR below expected for position | Review title + meta |
| Warning | CTR dropped 20%+ vs baseline | Rewrite title + meta |
| Critical | CTR dropped 40%+ vs baseline | Full refresh: title, description, structured data |

Compare CTR with the page's own history and with other pages at a similar average position in the owner's export. Generic CTR-by-position benchmarks were removed (unsourced).

## Secondary Signals

| Signal | Decay Indicator |
|--------|----------------|
| Bounce rate increase >15% | Content no longer satisfies intent |
| Time on page decrease >20% | Users leaving faster |
| Published >12mo, never updated | High decay risk |
| Year references 2+ years old | High decay risk |
| Broken external links >10% | Medium decay risk |
| References to discontinued products | High decay risk |
| New competitor ranking above you | Competitive displacement |
| Featured snippet lost | Competitive displacement |
| An AI answer covers the query without a click | Competitive displacement |

## Alert Priority Matrix

| Signal Combination | Priority | Response |
|--------------------|----------|----------|
| Traffic decline + Position drop | P1 Critical | Refresh within 48 hours |
| Traffic decline + CTR decline | P1 Critical | Rewrite title/desc immediately, schedule refresh |
| Position drop + Competitor displacement | P2 High | Refresh within 1 week |
| Traffic decline + Engagement decline | P2 High | Refresh within 1 week |
| CTR decline only | P3 Medium | Rewrite title + meta this week |
| Freshness indicators only | P3 Medium | Schedule refresh within 2 weeks |

## Composite Decay Score (0-100, unsourced weights)

| Signal | Weight |
|--------|--------|
| Traffic decline | 30% |
| Position drops | 25% |
| CTR decline | 15% |
| Content freshness | 15% |
| Competitive displacement | 15% |

| Score | Stage | Action |
|-------|-------|--------|
| 0-20 | Healthy | Continue monitoring |
| 21-40 | Early decay | Refresh queue (next month) |
| 41-60 | Active decay | Refresh this week |
| 61-80 | Significant decay | Immediate refresh or rewrite |
| 81-100 | Terminal decay | Rewrite, redirect, or retire |

## Refresh vs. Rewrite Decision

**REFRESH when**: URL has backlinks, was ranking well, <50% content changing, intent unchanged.
**REWRITE when**: Never ranked well, no backlinks, >50% needs rewriting, search intent evolved.

## Content Retirement Checklist

Retire when: zero search volume keyword | topic irrelevant to business | no backlinks | never ranked well | refresh cost > 12-month recovery value | cannibalizes better page.

| Option | When to Use |
|--------|------------|
| 301 redirect | Has backlinks or residual traffic |
| Consolidate | Multiple weak pages on same topic |
| Noindex | Internal utility only |
| Delete (410) | No value, no links, no traffic |

## Refresh Frequency by Content Type

| Content Type | Frequency | Shelf Life |
|-------------|-----------|-----------|
| Statistics roundups | Every 6 months | 6-12 months |
| Tool comparisons | Every 3-6 months | 3-6 months |
| How-to guides | Annually | 12-18 months |
| Evergreen guides | Every 12-18 months | 18-24 months |
| News/trend content | Don't refresh | 1-3 months |
| Case studies | Rarely | 2-3 years |

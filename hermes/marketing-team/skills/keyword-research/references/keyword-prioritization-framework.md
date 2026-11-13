> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/survey/keyword-research/references/keyword-prioritization-framework.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Keyword Prioritization Framework

Systematic scoring methodology for ranking keywords by strategic value.

> Thresholds, bands and counts in this file are conventions or rules of thumb from the original skill (unsourced). Volume, difficulty and trend numbers come only from the owner's export; missing is "không có số" and the row is not scored. Vietnam first: Vietnamese queries, with and without diacritics.


## Relationship to Opportunity Score

**Which score to use**: Use the Priority Score (below) for initial keyword triage and shortlisting. Use the Opportunity Score (Step 6 in the main workflow) for final content calendar prioritization.

## Priority Scoring Matrix

Score each keyword 1-5, then calculate the weighted total. If volume, difficulty or trend is "không có số", do not score that keyword; list it as `NOT_SCORED`. Weights are the original skill's convention (unsourced):

| Factor | Weight | Score 1 (Low) | Score 5 (High) |
|--------|--------|---------------|----------------|
| Search Volume | 20% | low in the owner's export | high in the owner's export |
| Keyword Difficulty | 25% | hard in the owner's tool | easy in the owner's tool |
| Business Relevance | 30% | Tangential to offering | Core to offering |
| Search Intent Match | 15% | Informational only | Transactional/commercial |
| Trend Direction | 10% | Declining | Growing (from the owner's export; else không có số) |

**Priority Score** = Sum(Factor Weight x Score) / 5

## Priority Categories

| Priority | Score Range | Action |
|----------|------------|--------|
| P0 — Must Target | 4.0-5.0 | Create content immediately |
| P1 — High Value | 3.0-3.9 | Queue for next content sprint |
| P2 — Opportunity | 2.0-2.9 | Plan for future content calendar |
| P3 — Monitor | 1.0-1.9 | Track but don't prioritize |

## Seasonal Keyword Patterns

| Season Trigger | Example Keywords | Planning Lead Time | Content Strategy |
|---------------|-----------------|-------------------|-----------------|
| Calendar events (Vietnam: Tết, 11.11, 12.12, Black Friday) | "[event] [topic]" | Lead times are unsourced guides | Publish before the peak the owner's data shows |
| Industry events | "[Conference] takeaways", "Google algorithm update" | 1-2 months / reactive | Pre-plan templates, react quickly |
| Budget cycles | "marketing budget template Q1", "SEO ROI report" | 2-3 months ahead | Target the planning season (check the owner's data) |
| Seasonal demand | "summer marketing ideas", "holiday email campaigns" | 2-3 months ahead | Refresh annually with new data |

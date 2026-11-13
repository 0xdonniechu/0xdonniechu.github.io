> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/survey/keyword-research/references/instructions-detail.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Keyword Research — Detailed Instructions

Compact workflow, scoring rules, and delivery templates for the Keyword Research skill.

> Thresholds, bands and counts in this file are conventions or rules of thumb from the original skill (unsourced). Volume, difficulty and trend numbers come only from the owner's export; missing is "không có số" and the row is not scored. Vietnam first: Vietnamese queries, with and without diacritics.


At the start of each phase, announce `**[Phase X/8: Name]**`.

## Phase 1/8: Scope

Confirm the topic, audience, business goal, domain strength, geography, and language.

## Phase 2/8: Discover

**Start from the owner's Search Console export when there is one (striking-distance first).** Your first opportunity set is queries already earning impressions at average positions of roughly 5-20 (unsourced range), which is demand a small push may convert. Filter the exported rows yourself, then carry that shortlist into Phase 5 scoring (label its metrics **Measured**, with file name and date). Only after working the striking-distance set, expand with the seeds below.

Then seed from:
- Core product and service terms
- Problem-focused keywords
- Solution-focused keywords
- Audience-specific language
- Industry terminology

## Phase 3/8: Variations

```markdown
## Keyword Expansion Patterns

### Modifiers
- Best [keyword]
- Top [keyword]
- [keyword] for [audience]
- [keyword] [year]
- How to [keyword]
- What is [keyword]
- [keyword] vs [alternative]
- [keyword] examples
- [keyword] tools

### Long-tail Variations
- [keyword] for beginners
- [keyword] for small business
- Free [keyword]
- [keyword] software/tool/service
- [keyword] template
- [keyword] checklist
- [keyword] guide
```

## Phase 4/8: Classify

| Intent | Signals | Example | Content Type |
|--------|---------|---------|--------------|
| Informational | what, how, why, guide, learn | "what is SEO" | Guides, explainers |
| Navigational | brand names, specific sites | "google analytics login" | Homepage, support |
| Commercial | best, review, vs, compare | "best SEO tools" | Comparisons, reviews |
| Transactional | buy, price, discount, order | "buy SEO software" | Product and pricing pages |

## Phase 5/8: Score

Difficulty comes from the owner's tool export (scales differ between tools; say which tool). Without it, write "không có số". Bands from the original skill (unsourced):
- **Low (1-39)**: weak competitors, thin content, or long-tail intent
- **Medium (40-69)**: mixed authority landscape and moderate link/content bar
- **High (70-100)**: major brands, heavy backlink requirements, ad-heavy SERPs

Opportunity formula:

`Opportunity = (Volume × Intent Value) / Difficulty`

Intent values:
- Informational = 1
- Navigational = 1
- Commercial = 2
- Transactional = 3

| Scenario | Volume | Difficulty | Intent | Priority |
|----------|--------|------------|--------|----------|
| Quick Win | Low-Med | Low | High | 5 stars |
| Growth | High | Medium | High | 4 stars |
| Long-term | High | High | High | 3 stars |
| Research | Low | Low | Low | 2 stars |

## Phase 6/8: GEO-Check

Flag keywords likely to overlap with AI answers (a judgement, not a measurement):
- Questions, definitions, comparisons, lists, and how-to queries
- Queries that can be answered concisely or with structured facts
- Well-documented topics with low to medium commercial friction

## Phase 7/8: Cluster

```markdown
## Topic Cluster: [Main Topic]

**Pillar Content**: [Primary keyword]
- Search volume: [X]
- Difficulty: [X]
- Content type: [Guide / landing / comparison]

**Cluster Content**:
- [Secondary keyword] — Volume [X], Difficulty [X], links to [pillar]
- [Secondary keyword] — Volume [X], Difficulty [X], links to [pillar + related cluster]
```

## Phase 8/8: Deliver

Report sections:
- Executive Summary
- Top Opportunities: Quick Wins / Growth / GEO
- Topic Clusters
- Content Calendar
- Next Steps

**Quality bar**: every recommendation names a concrete keyword and a reason, and carries a number only when the owner's data has one.

| Generic | Actionable |
|---|---|
| "Target long-tail keywords for better results" | "Target '[long-tail keyword]' (vol: [from export or không có số], KD: [from export or không có số]); top 10 on [date] shows [observed pattern]" |
| "This keyword has good potential" | "[keyword]: [intent], striking-distance in the export (avg position [x], [n] impressions); the top result was last updated [date]" |
| "Consider creating content around this topic" | "Write '[A] vs [B] for [audience]': comparison intent; the current #1 on [date] is from [year]" |


## Advanced Usage

- **Intent Mapping**: `Map all keywords for [topic] by search intent and funnel stage`
- **Seasonal Analysis**: `Identify seasonal keyword trends for [industry]`
- **Competitor Gap**: `What do [competitor 1], [competitor 2] cover on their public pages that we do not?` (page titles and headings only; their ranking numbers need an owner export)
- **Local Keywords**: `Research local keywords for [business type] in [city/region]`

## Tips for Success

Start from strong seeds, respect intent, cluster tightly, include GEO candidates, and refresh the research quarterly.

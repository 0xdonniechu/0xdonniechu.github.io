> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/geo-content-optimizer/references/instructions-detail.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# GEO Content Optimizer — Detailed Instructions

Compact workflow, GEO-first targets, rating templates, and example output for the GEO Content Optimizer skill.

> The item IDs (C02, O05, R01...) are local labels from the original skill's checklist; the standard text is what counts. Word counts and scores here are rules of thumb or judgements (unsourced), not measured facts. Brand voice: `voice.md` at the workspace root.

## Step 1: Load GEO-First Targets

Prioritize these items first:

| Rank | ID | Standard | Why It Matters |
|------|----|----------|----------------|
| 1 | C02 | Direct Answer in the opening (the 150-word guide is unsourced) | Easier to extract |
| 2 | C09 | Structured FAQ with Schema | Matches follow-up AI queries |
| 3 | O03 | Comparisons in tables | Easy for systems to quote |
| 4 | O05 | JSON-LD Schema Markup | Clarifies content type |
| 5 | E01 | Original first-party data | Supports citation trust |
| 6 | O02 | Summary Box / Key Takeaways | Good summary surface |

Per-engine priorities are not listed here: the original skill's engine-by-engine item ranking was unsourced and was removed. For what each engine documents, see [ai-citation-patterns.md](ai-citation-patterns.md).

## Step 2: Analyze Current Content

Scores are your judgement from reading the page (label them Estimated); they are not measurements.

```markdown
## GEO Analysis: [Content Title]

| GEO Factor | Current Score (1-10) | Notes |
|------------|----------------------|-------|
| Clear definitions | [X] | [notes] |
| Quotable statements | [X] | [notes] |
| Factual density | [X] | [notes] |
| Source citations | [X] | [notes] |
| Q&A format | [X] | [notes] |
| Authority signals | [X] | [notes] |
| Content freshness | [X] | [notes] |
| Structure clarity | [X] | [notes] |

**Primary Weaknesses**: [1], [2], [3]
**Quick Wins**: [1], [2]
```

## Step 3: Apply GEO Optimization Techniques

Use these six techniques:
- **Definition optimization**: short (25-50 words is an unsourced guide), standalone, starts with the term
- **Quotable statements**: specific facts or stats with sources
- **Authority signals**: expert quotes, credentials, citations
- **Structure optimization**: Q&A, tables, numbered lists
- **Factual density**: replace vague claims with verifiable specifics
- **FAQ schema**: JSON-LD that matches visible FAQ content

## Step 4: Generate GEO-Optimized Output

```markdown
## GEO Optimization Report

### Changes Made
- Definitions added or improved
- Quotable statements created
- Authority signals added
- Structural changes applied

### Before / After GEO Score
| GEO Factor | Before | After | Change |
|------------|--------|-------|--------|
| Clear definitions | [X] | [X] | +[X] |
| Quotable statements | [X] | [X] | +[X] |
| Factual density | [X] | [X] | +[X] |
| Source citations | [X] | [X] | +[X] |
| Q&A format | [X] | [X] | +[X] |
| Authority signals | [X] | [X] | +[X] |
| Overall GEO Score | [X]/10 | [X]/10 | +[X] |

### AI Query Coverage
- "What is [topic]?"
- "How does [topic] work?"
- "[topic] vs [alternative]"
```

## Step 5: GEO Self-Check

Verify these 14 items:

| ID | Standard | Status |
|----|----------|--------|
| C02 | Direct Answer in first 150 words | Pass/Warn/Fail |
| C04 | Key terms defined on first use | Pass/Warn/Fail |
| C09 | Structured FAQ with Schema | Pass/Warn/Fail |
| O02 | Summary Box / Key Takeaways | Pass/Warn/Fail |
| O03 | Comparisons in tables | Pass/Warn/Fail |
| O05 | JSON-LD Schema Markup | Pass/Warn/Fail |
| O06 | Section chunking | Pass/Warn/Fail |
| R01 | Precise data points (only sourced ones) | Pass/Warn/Fail |
| R02 | Citation density | Pass/Warn/Fail |
| R04 | Claims backed by evidence | Pass/Warn/Fail |
| R07 | Full entity names | Pass/Warn/Fail |
| E01 | Original first-party data | Pass/Warn/Fail |
| Exp10 | Limitations acknowledged | Pass/Warn/Fail |
| Ept08 | Reasoning transparency | Pass/Warn/Fail |

## Example

**User**: "Optimize this paragraph for GEO: 'Email marketing is a good way to reach customers...'"

**Output summary**:
- Adds a precise definition
- Replaces vague claims with sourced stats (or `[needs source]` placeholders)
- Introduces quotable bullet points
- Improves structure for AI extraction
- Shows a before/after rating (a judgement, labelled Estimated)

## Tips for Success

Answer first, be specific, cite sources, stay current, and optimize for the exact query shape users ask.

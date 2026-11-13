> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/serp-markup-builder/references/meta-tag-formulas.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Meta Tag Formulas Reference

Compact formulas for titles, descriptions, testing, freshness, and localization.

> Counts, lengths and limits here are rules of thumb from the original skill or from Google guidance as the original recorded it (unsourced when vendored). Check the official documentation named in the file before the owner relies on one. The owner pastes and validates; this role does not submit anything.


## 1. Title Formulas

| Intent / Type | Formula Patterns |
|---------------|------------------|
| Informational | `How to [Action] in [Year]`; `[Topic]: The Complete Guide ([Year])`; `What Is [Topic]? [Clarifier]`; `[Topic] for Beginners: [Promise]` |
| Listicle | `[N] [Topic] Tips That [Result]`; `[N] Best [Items] in [Year] ([Qualifier])`; `[N] [Topic] Mistakes [Consequence]` |
| Comparison | `[A] vs [B]: [Differentiator]`; `[A] vs [B] ([Year]): [Angle]`; `[N] Best [Product] Alternatives in [Year]` |
| Commercial | `[Product] - [Benefit] \| [Brand]`; `[Product] Pricing: [Value Statement]`; `[Product] Review ([Year]): [Verdict]`; `Free [Tool Type]: [What It Does]` |
| Local | `[Service] in [City] - [Brand] \| [Differentiator]`; `Best [Service] in [City] ([Year])` |
| Problem-aware | `Why [Problem] (And How to Fix It)`; `Stop [Bad Practice]: [Alternative]` |

## 2. Meta Description Templates

| Page Type | Template | Target Length (unsourced) |
|-----------|----------|---------------|
| Article | `Learn [topic] with our [qualifier] guide. Covers [point 1], [point 2], and [point 3]. [CTA].` | 140-155 |
| Question | `[Question]? This [year] guide explains [what], [why], and [how]. Get actionable tips now.` | 130-150 |
| Test/result | `[Bold claim]. We tested [N] [methods/tools] and found what works. See the results.` | 130-150 |
| Product/service | `[Product] helps you [benefit]. [Feature 1], [Feature 2], [Feature 3]. [CTA].` | 140-155 |
| Solution/social proof | `Looking for [solution]? [Product] [differentiator]. Trusted by [social proof]. [CTA].` | 130-150 |
| Comparison | `[A] vs [B]: which is better for [use case]? We compared [criteria]. See the winner.` | 145-160 |
| E-commerce | `Shop [category] from [Brand]. [N]+ items starting at [price]. [Shipping/returns value].` | 145-160 |
| Local | `[Service] in [City] by [Brand]. [experience/proof]. [rating/proof]. [CTA].` | 150-160 |

## 3. A/B Testing Method

```markdown
1. Record baseline CTR from the owner's Search Console export over a stated period (the original suggested 30 days and 1,000 impressions, unsourced).
2. State one hypothesis: "Changing [element] will improve CTR by [target] because [reason]."
3. Change only one element.
4. Allow time for recrawl (3-7 days, unsourced).
5. Monitor for a stated period (30+ days, unsourced), excluding the first week.
6. Compare at the same average position, then keep, revert, or iterate.
```

| Priority | Element to test |
|----------|-----------------|
| 1 | Add or remove a number |
| 2 | Add or remove the year |
| 3 | Add brackets or parentheses |
| 4 | Change a power word |
| 5 | Add a CTA in the description |

CTR uplift percentages from the original skill were removed (unsourced). Measure the result from the owner's Search Console export, not from a quoted figure.

| Result | Action |
|--------|--------|
| CTR up, position stable/up | Keep and document |
| CTR down, position stable | Revert immediately |
| CTR flat, position stable | Try a bolder variation |

## 4. Freshness

| Pattern | Rule |
|---------|------|
| Year modifiers | Use only when the page is materially current |
| "Best/top" queries | Refresh modifiers every 3-6 months |
| Monthly update labels | Use only when content was actually reviewed that month |
| Seasonal events | Match the user's planning window, not just the calendar |

A CTR-by-position benchmark table was removed (unsourced). Compare a page's CTR with its own history and with similar pages at a similar average position in the owner's export; if the export is missing write "không có số".

| CTR gap against the page's own history | Likely cause | Action |
|----------------------------------------|--------------|--------|
| Large | Title mismatches intent | Rewrite around query intent |
| Moderate | Weak title or strong SERP features | Add specificity, a number or brackets |
| Small | Competitors have sharper titles | Read the top three and differentiate |

## 5. Localization And Modifiers

Vietnamese (our first market): titles are displayed by pixel width, not character count, and Vietnamese diacritics can widen a title, so a title that fits in English may truncate. Preview the title in a SERP preview before the owner approves; the character guide is "không có số" until the owner confirms one.

Principles: do not translate literally; run Vietnam-specific keyword research (with and without diacritics); adjust the CTA to the Vietnamese reader.

| Purpose | Modifiers |
|---------|-----------|
| Freshness | [Year], Updated, Latest, This Month |
| Comprehensiveness | Complete, Ultimate, Definitive, In-Depth |
| Ease | Easy, Simple, Quick, Beginner, No-Code |
| Authority | Expert, Pro, Advanced, Data-Driven |
| Value | Free, Budget, Affordable, Open-Source |
| Format | Guide, Checklist, Template, Cheat Sheet, Playbook |
| Social proof | Trusted, [N]+ Users, Award-Winning, #1 Rated |

Avoid keyword stuffing, duplicate titles, all caps, generic titles, misleading clickbait, non-branded titles that lead with brand, and titles that exceed the visible limit.

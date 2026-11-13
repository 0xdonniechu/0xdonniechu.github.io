> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/geo-content-optimizer/references/geo-optimization-techniques.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# GEO Optimization Techniques

> Word counts and recency windows here (25-50 words, 40-60 words, within 2 years) are rules of thumb from the original skill (unsourced). Statistics in examples are placeholders: use only numbers with a source and date, otherwise `[needs source]`.

## Definition Optimization

**Template**: "[Term] is [category] that [primary function], [key characteristic]."

**Before**: "SEO is really important for businesses and involves various techniques..."
**After**: "**Search Engine Optimization (SEO)** is the practice of optimizing websites and content to rank higher in SERPs, increasing organic traffic and visibility."

**Checklist**:
- [ ] Starts with the term being defined
- [ ] Provides clear category
- [ ] Explains primary function
- [ ] Precise, unambiguous language
- [ ] Can stand alone as a complete answer
- [ ] Short enough to quote (25-50 words, unsourced)

## Quotable Statement Optimization

**Types of Quotable Statements**:
1. **Statistics** — specific numbers, cite source, add context (timeframe, comparison)
2. **Facts** — verifiable, unambiguous, authoritative source
3. **Definitions** — (see above)
4. **Comparisons** — "Unlike [A], [B] [specific difference], which means [implication]."
5. **How-to Steps** — numbered, action-oriented

## Authority Signal Enhancement

**Authority Elements**:
- [ ] Author byline with credentials
- [ ] Expert quotes with attribution
- [ ] Citations to peer-reviewed research
- [ ] References to recognized authorities
- [ ] Original data or research
- [ ] Case studies with named companies
- [ ] Industry statistics with sources

## Structure Optimization for GEO

**Q&A Format**:
```html
<h2>What is [Topic]?</h2>
<p>[Direct answer, short and standalone]</p>
<h2>How does [Topic] work?</h2>
<p>[Clear explanation with steps if applicable]</p>
```

**Comparison Tables**:
| Feature | Option A | Option B |
|---------|----------|----------|
| [Feature 1] | [Specific value] | [Specific value] |
| **Best for** | [Use case] | [Use case] |

**Numbered Lists** for process queries:
1. **Step 1: [Action]** - [Brief explanation]
2. **Step 2: [Action]** - [Brief explanation]

**Definition Boxes**: `> **Key Definition**: [Term] refers to [clear definition].`

## Factual Density Improvement

**Factual Enhancement Checklist**:
- [ ] Add specific statistics with sources
- [ ] Include exact dates and numbers, each with a source
- [ ] Replace vague claims with verified facts
- [ ] Prefer recent data (the 2-year window is unsourced)
- [ ] Include multiple data points per section
- [ ] Cross-reference with authoritative sources

## FAQ Optimization for GEO

**FAQ Structure**:
### [Question matching common query]?
[Direct answer, short and standalone]
[Supporting detail or example]

**FAQ Schema (JSON-LD)**:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "[Question text]",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "[Answer text]"
    }
  }]
}
```

## GEO Readiness Checklist

**Definitions & Clarity**
- [ ] Key terms clearly defined
- [ ] Definitions can stand alone as answers
- [ ] Language is precise and unambiguous

**Quotable Content**
- [ ] Specific statistics included
- [ ] Facts have source citations
- [ ] Memorable statements created

**Authority**
- [ ] Expert quotes or credentials present
- [ ] Authoritative sources cited
- [ ] Original data or research included

**Structure**
- [ ] Q&A format sections included
- [ ] Clear headings match common queries
- [ ] Comparison tables where relevant
- [ ] Numbered lists for processes

**Technical**
- [ ] FAQ schema markup added
- [ ] Content freshness indicated
- [ ] Sources are verifiable

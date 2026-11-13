> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/serp-markup-builder/references/schema-instructions-detail.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Schema Markup Generator — Detailed Instructions

Compact workflow, schema mapping, implementation guidance, validation checklist, and FAQ example for the Schema Markup Generator skill.

> Counts, lengths and limits here are rules of thumb from the original skill or from Google guidance as the original recorded it (unsourced when vendored). Check the official documentation named in the file before the owner relies on one. The owner pastes and validates; this role does not submit anything.


## Step 1: Identify Content Type and Rich Result Opportunity

Match content type to schema:

| Content Type | Required Schema | Conditional Schema |
|--------------|-----------------|--------------------|
| Blog guide | Article, Breadcrumb | FAQ, HowTo |
| Blog tools | Article, Breadcrumb | FAQ, Review |
| Best-of / alternatives | ItemList, Breadcrumb, FAQ | AggregateRating |
| Landing page | SoftwareApplication, Breadcrumb, FAQ | WebPage |
| FAQ page | FAQPage, Breadcrumb | — |
| Testimonial page | Review, Breadcrumb | FAQ, Person |

Then evaluate rich-result eligibility:

| Rich Result Type | Eligible now? (verify in Google's documentation) |
|------------------|---------------------------------------------------|
| FAQ | Yes/No (limited by Google; see SKILL.md) |
| How-To | Yes/No (desktop deprecated; see SKILL.md) |
| Product | Yes/No |
| Review | Yes/No |
| Article | Yes/No |
| Breadcrumb | Yes/No |
| Video | Yes/No |

## Step 2: Generate Schema Markup

For the chosen schema type:
- Include all required properties
- Add optional properties only when they are true and visible on page
- Include a short rich-result preview
- Split fields into required vs. optional notes
- Note which fields affect rich-result eligibility
- Combine multiple schema types inside one JSON array when needed

> **Reference**: See [references/schema-templates.md](schema-templates.md) for copy-start JSON-LD templates.

## Step 3: Provide Implementation and Validation

```markdown
## Implementation Guide

### Placement
- `<head>` is preferred
- Before `</body>` also works if the stack requires it

### Validation Checklist
- [ ] JSON is valid
- [ ] Required properties are present
- [ ] URLs are absolute
- [ ] Dates use ISO 8601
- [ ] Schema matches visible page content
- [ ] No policy violations
```

Validation flow:
1. The owner tests the page or staging URL with Google's Rich Results Test
2. The owner re-checks in the Schema.org Validator
3. The owner reads the Search Console enhancement and rich-result reports

## Example FAQ Schema for SEO Page

**User**: "Generate FAQ schema for a page about SEO with 3 questions"

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[direct answer]"
      }
    },
    {
      "@type": "Question",
      "name": "How long does SEO take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[direct answer]"
      }
    },
    {
      "@type": "Question",
      "name": "Is SEO better than paid ads?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[direct answer]"
      }
    }
  ]
}
```

Wrap the JSON-LD in `<script type="application/ld+json">...</script>`; the owner validates it before deployment.

## Schema Type Quick Reference

| Content Type | Schema Type | Key Properties |
|--------------|-------------|----------------|
| Blog Post | BlogPosting / Article | headline, datePublished, author |
| Product | Product | name, offers, availability |
| FAQ | FAQPage | Question, Answer |
| How-To | HowTo | step, totalTime |
| Local Business | LocalBusiness | address, geo, openingHours |
| Recipe | Recipe | ingredients, cookTime |
| Event | Event | startDate, location |
| Video | VideoObject | uploadDate, duration |
| Course | Course | provider, name |
| Review | Review | itemReviewed, ratingValue |

## Tips for Success

Match visible content, avoid unsupported claims, keep values fresh, validate thoroughly, and watch Search Console after launch.

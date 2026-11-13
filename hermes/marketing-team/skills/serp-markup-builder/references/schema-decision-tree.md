> Modified from aaron-he-zhu/aaron-marketing-skills `seo-geo/implement/serp-markup-builder/references/schema-decision-tree.md` @ 61075e8 (Apache-2.0) by 0xdonniechu, 2026-11-13. Changes are listed in `THIRD_PARTY.md` at the team root.

# Schema Type Decision Tree

Guidelines for selecting the right schema types based on content, industry, and implementation priority.

> Counts, lengths and limits here are rules of thumb from the original skill or from Google guidance as the original recorded it (unsourced when vendored). Check the official documentation named in the file before the owner relies on one. The owner pastes and validates; this role does not submit anything.

The "Rich Result Eligibility" column lists what the original skill expected; Google has since limited some (FAQ, HowTo; see SKILL.md), so verify before promising a SERP feature.

---

## When to Use Which Schema

| Your Content | Primary Schema | Add If Applicable | Rich Result Eligibility |
|-------------|---------------|-------------------|----------------------|
| Blog post / article | Article | FAQ, HowTo, Speakable | Article carousel (verify) |
| Product page | Product | Review, Offer, AggregateRating | Product snippet with price/rating |
| Service page | Service | FAQ, LocalBusiness | Service snippet |
| How-to guide | HowTo | Article, FAQ | How-to rich result (deprecated on desktop; verify) |
| FAQ page | FAQPage | Article | FAQ accordion (limited by Google; verify) |
| Recipe | Recipe | Video, AggregateRating | Recipe carousel |
| Event | Event | Offer, Organization | Event snippet with date/location |
| Video | VideoObject | Article | Video carousel, key moments |
| Local business | LocalBusiness | Review, OpeningHoursSpecification | Local pack, knowledge panel |
| Person/author | Person | Organization | Knowledge panel |
| Organization | Organization | ContactPoint, Logo | Knowledge panel |
| Course | Course | Organization | Course rich result |
| Job posting | JobPosting | Organization | Google for Jobs listing |
| Breadcrumb | BreadcrumbList | (Always add alongside other schema) | Breadcrumb trail in SERP |
| Software/App | SoftwareApplication | Review, Offer | App snippet |

---

## Industry-Specific Schema Recommendations

| Industry | Essential Schema | High-Value Additions |
|----------|-----------------|---------------------|
| E-commerce | Product, BreadcrumbList, Organization | AggregateRating, FAQ, Review |
| SaaS | SoftwareApplication, FAQPage, Organization | HowTo, VideoObject, Review |
| Local Services | LocalBusiness, Service | FAQ, Review, Event |
| Publishing/Media | Article, Person, Organization | FAQ, Speakable, VideoObject |
| Education | Course, Organization | FAQ, HowTo, Event |
| Healthcare | MedicalWebPage, Organization | FAQ, Physician, MedicalClinic |
| Real Estate | RealEstateListing, Organization | LocalBusiness, FAQ |
| Restaurants | Restaurant, Menu | Review, Event, FAQ |

---

## Schema Implementation Priority

| Priority | Schema Types | Why |
|----------|-------------|-----|
| P0 -- Always | Organization, BreadcrumbList, WebSite | Foundation for all sites |
| P1 -- Content | Article, FAQPage, HowTo | Describes the page; rich-result eligibility varies (verify) |
| P2 -- Commercial | Product, Review, AggregateRating, Offer | Revenue-impacting rich results |
| P3 -- Authority | Person, SameAs, Speakable | Entity and author signals |
| P4 -- Specialized | Industry-specific types | Niche rich results |

---

## Schema Validation Quick Reference

| Issue | Impact | Fix |
|-------|--------|-----|
| Missing required property | Schema ignored by Google | Add all required fields (check schema.org) |
| Invalid date format | Warning, may lose rich result | Use ISO 8601: "2026-02-11" |
| Incorrect @type | Schema misinterpreted | Match @type exactly to schema.org |
| Self-referencing sameAs | Warning | sameAs should link to EXTERNAL profiles |
| Missing image for Article | Loses article rich result | Add image property with valid URL |
| Review without itemReviewed | Review not connected | Nest review inside Product/Service/etc. |

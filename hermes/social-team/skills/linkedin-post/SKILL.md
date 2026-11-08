---
name: linkedin-post
description: When drafting LinkedIn post copy for a profile or Company Page, or tuning it for the feed. Use for "LinkedIn post," "LinkedIn copy," "professional post," "document post," "poll," "LinkedIn engagement." Produces draft text with a first line and character count; never posts. Limits come from the team's formats/linkedin.md. Not for LinkedIn ads.
metadata:
  version: 1.2.0
---

# LinkedIn Posts

Adapted from kostja94/marketing-skills `skills/platforms/linkedin` (MIT, commit ac823a1) by 0xdonniechu, 2026-11-08: removed links to skills this team does not ship; unsourced numbers marked; limits defer to the team's `formats/linkedin.md`.

**Team rules:** draft only, the owner approves and posts. Hard limits (3,000-character post, image and document specs, video specs) are in the team's `formats/` folder (formats/linkedin.md) and win over anything below. Numbers marked "(unsourced)" are rules of thumb from the original skill, not verified platform facts. Brand voice: read `voice.md` at the team root. Edit the draft with the **copy-editing** skill.

Guides LinkedIn post copy creation and optimization. Use for generating professional post drafts ready for the owner's review.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Output: Draft Copy

This skill generates LinkedIn post drafts optimized for engagement. Output includes character-counted text and structure for the "See more" threshold.

## Post Types and Entry Points (organic)

| Kind | What to know |
|------|----------------|
| **Start a post** | Short update; can include **link preview** if you paste a URL. Same feed format as other updates. |
| **Photo** | Single or multiple images (carousel in feed). |
| **Video** | Uploaded file (distinct from **LinkedIn Live**, which is live streaming and has separate gating). |
| **Write article** | **Article** = long-form editor, **separate** from the short post box; long URL, better for depth and some **off-site** discoverability. |
| **Document** | PDF / PPT / DOC (slides in feed). Size and page limits: formats/linkedin.md. |
| **Poll** | Engagement driver; keep question and options scannable. |
| **More** (menu) | Often includes **celebrations**, **hiring**-style share, **Find an expert**, etc. (varies by product/region). |
| **Reshare** | Reshare or **quote** another member’s post with your take—adds context; avoid empty reshares. |
| **Newsletter** | **Series** subscription; not the same as a one-off post but compound reach over time. |
| **Event** | Create/promote events via a dedicated flow, not the same as a plain text post. |

**Product detail**: [Get started with posting on LinkedIn](https://www.linkedin.com/help/linkedin/answer/a518996) · [Upload and share documents](https://www.linkedin.com/help/linkedin/answer/a518909)

**Why it matters for copy**: Match CTA and length to the **form** (e.g. a document deck vs a 5-line hot take). Do not treat a **short post** and an **Article** as interchangeable.

## Platform Positioning

LinkedIn is a professional network—its core value is career identity, B2B relationships, and professional content. Key differences from general social platforms:

| Dimension | LinkedIn | Meta / X / TikTok |
|-----------|----------|--------------------|
| **Primary intent** | Job seeking, B2B networking, industry learning | Entertainment, social, discovery |
| **Identity** | Real name + career history | Username or lifestyle persona |
| **Content tone** | Professional, constructive | Casual, entertaining, opinion |
| **B2B lead value** | High (job title + company targeting) | Low to medium |
| **Algorithm signal** | Professional interest + network + editorial | Engagement, watch time, virality |

**Prioritize LinkedIn when**: targeting B2B buyers, building professional authority, recruiting, or publishing industry thought leadership. For consumer brand awareness or entertainment, other platforms are often more effective.

## How the Feed Ranks (what to write for)

- The feed is **not** a pure reverse-chronological friend list. It blends **1st-degree connections, follows, company/topic interest, and recommended “out of network”** content from the **Economic Graph**, plus ads. [How the Feed ranks content](https://www.linkedin.com/help/linkedin/answer/a9554004)
- Relevance uses **context** of the post, **profile and network signals**, and **behavior** (read, react, comment, share, **dwell**). Demographics like age or gender are **not** used to rank feed visibility (per public help guidance).
- Platform direction in recent public communications: more **LLM/semantic** understanding, less **inauthentic engagement** and **engagement-bait** / low-quality repetition; favor **real expertise** and **meaningful** discussion. [Background on feed engineering (blog)](https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed)

**Writing implications**: Strong **first line** and **on-topic depth**; comments that add substance; avoid templates that look automated or “pod” coordinated, and avoid engagement bait ("Agree?", "Thoughts?").

## Off-Site Search Visibility (SEO & GEO)

LinkedIn content is visible to search engines on a **selective** basis (the visibility table below is the original author's claim, unverified)—understand what gets indexed for SEO and cited for GEO.

### What Google Indexes vs. What Is Login-Gated

| Surface | Search Visibility | GEO (AI citation) Value |
|---------|-----------------|-------------------------|
| **Public profile** (Headline, About, Experience) | Indexed for name/company/role queries | Strong entity signal; citable paragraphs |
| **Articles** (long-form editor) | Indexed when set to public | High; structured paragraphs with keywords |
| **Company Page** | Indexed for brand queries | Medium; brand entity signals |
| **Short feed posts** | **Login-gated**—not indexed | **Low**; cannot be cited if behind login |
| **Newsletter issues** | Indexed if public; behind login if subscriber-only | Depends on visibility setting |

### SEO Through LinkedIn

- **Headline** is the most SEO-visible field on your profile—treat it as a title tag. Include primary keyword + value proposition (e.g. “B2B SaaS Marketing | Helping startups scale through content”).
- **About section**: Write public-facing paragraphs with keywords and proof points. This is indexed and often appears in Google search snippets.
- **Featured section**: Use to showcase key links (site, case studies, press). These appear on your public profile and add backlink value.
- **Articles**: Long-form content on LinkedIn ranks independently on Google. Treat as secondary publication, not primary—repurpose site content with canonical or unique article.
- **Consistency**: Align name, headline, and entity names across LinkedIn, your site, and other public bios.

### GEO Through LinkedIn

- **Entity consistency**: Your LinkedIn profile is a high-authority entity source. AI search tools (ChatGPT, Perplexity, Google AI Overviews) can cite your LinkedIn profile when answering “who is [person]” or “what does [company] do” queries.
- **Citable paragraphs**: Write your About section in answer-first format (40–60 words per block, unsourced) so AI tools can extract and cite it directly.
- **Evidence links**: Add links to your site, case studies, talks, and publications in Featured and About. AI tools cite external links as supporting references.
- **Public articles**: Publish LinkedIn Articles on relevant topics; well-structured articles with data and citations increase the likelihood of AI citation.
- **Limitation**: Short feed posts behind login walls are invisible to AI crawlers and search engines. Do not rely on feed posts for GEO.

**Actionable checklist**:
- [ ] Headline includes primary keyword + value proposition (treat as meta title)
- [ ] About section written in answer-first format (quotable paragraphs)
- [ ] Featured section showcases site, case studies, key publications
- [ ] Entity names (name, company, role) consistent across LinkedIn and site
- [ ] At least one public Article published on a relevant industry topic
- [ ] LinkedIn profile URL uses custom alias (not default ID string)

## Profile Modules for Discovery

Key LinkedIn profile modules that affect search visibility and AI citation:

| Module | SEO/GEO Value | Optimization |
|--------|---------------|--------------|
| **Headline** | Highest—indexed, appears in search snippets | Customize beyond job title; include keyword + audience + value |
| **About** | High—indexed; citable for AI | Write in answer-first format; include proof points, external links |
| **Featured** | Medium—showcases key links on public profile | Add site URL, case studies, press, portfolio |
| **Experience (media)** | Low-medium—media attachments are indexed | Add relevant documents, links, images to each role |
| **Skills & Endorsements** | Low—indexed but thin signal | Include relevant skills; endorsements add social proof |
| **Articles** | High—indexed and rankable | Publish long-form content with keywords and data |
| **Custom URL** | Indirect—clean URL improves shareability | Set to firstnamelastname or similar |

For the full profile module inventory, see [LinkedIn help: Add sections to your profile](https://www.linkedin.com/help/linkedin/answer/a540837).

## Character Limits

| Type | Limit | Notes |
|------|-------|-------|
| **Post** | 3,000 characters | Official, see formats/linkedin.md |
| **"See more" cut-off** | No official number found (formats/linkedin.md) | The original skill claims 210–235 characters and that 60–80% of readers decide on the first line (both unsourced). Put the whole point in the first line anyway |
| **Short posts** | 100–200 chars (unsourced) | Polls, announcements, quotes |

## Length by Content Type (unsourced rules of thumb)

| Type | Characters | Use |
|------|------------|-----|
| **Short** | 100–200 | Polls, announcements, quotes |
| **Medium** | 300–1,200 | Case studies, tips, BTS |
| **Long** | 1,200–2,000 | Thought leadership, analysis |

The original skill also gave a "1,300–1,600 sweet spot" with a "~35% engagement drop" past 2,000 characters. Neither number has a source, so do not quote them to the owner as facts. Write as long as the story needs and stay under 3,000.

## First Line (Hook)

- **Place key message in the first ~140 chars** (unsourced)
- **Strong openings**: Specific results, pain points, bold claims, surprising stats
- **Avoid**: Vague teases, hashtag-first, generic greetings

## Image and Document Specs

Dimensions, ratios, file sizes, the 20-image limit and document limits are in the team's `formats/linkedin.md`. Use those. (The original skill listed 1200×627 and a 10 MB limit; the team's file lists a 5 MB limit for images, so the original numbers are dropped.) Vertical or 4:5 images are generally preferred on mobile (unsourced).

## Best Practices

- **Mobile-first**: most members read on mobile (the original skill said 88%, unsourced)
- **Polls and document (PDF) posts**: Often strong for reach; pair with a clear takeaway
- **Post frequency**: Weekly minimum is a common bar for company pages; individuals often **several times per week** if sustainable
- **Alt text**: Add for accessibility
- **B2B tone**: Professional and constructive; align with `voice.md`

## Output Format

When generating LinkedIn copy, provide:

1. **First line** (hook, ideally ≤140 characters (unsourced))
2. **Full post** with character count
3. **Hashtags** (a few, relevant; end of post; no official limit was found, see formats/linkedin.md)
4. **Media note** (image or document needed, sized per formats/linkedin.md)
5. **Form note** if not a plain post (e.g. “pair with a 5-slide document” or “use Article for 1,200+ words”)

## Related Skills

- **social-playbook**: Hooks, templates and carousels across platforms
- **copy-editing**: Edit the draft and remove AI tells
- **voice-dossier**: Builds `voice.md`

## Official references (index)

- [Get started with posting](https://www.linkedin.com/help/linkedin/answer/a518996) · [Feed ranking (help)](https://www.linkedin.com/help/linkedin/answer/a9554004) · [Share photos](https://www.linkedin.com/help/linkedin/answer/a527229) · [Share videos](https://www.linkedin.com/help/linkedin/answer/a7174587)

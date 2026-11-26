# Product Record

## Platform

Responsive static website for desktop and mobile, published through Cloudflare Pages.

## Stack

Python 3 standard-library build script, Markdown source files, semantic HTML, CSS, and a small existing vanilla JavaScript enhancement for article tables of contents. No front-end framework or runtime dependency.

## Users

Entry-level and no-experience job seekers in the United States and other English-speaking markets, especially fresh graduates targeting machine learning, software engineering, and data roles.

## Product Purpose

Help candidates turn projects, coursework, internships, and adjacent technical experience into credible resume evidence. Provide complete examples, copy-ready bullets, practical guides, and free Word templates without requiring sign-up.

## Positioning

A free, practical resume library for early-career technical candidates. The site focuses on evidence and truthful framing rather than generic career advice, invented experience, or interview guarantees.

## Operating Context

- English-language content; collaborators communicate in Chinese.
- Organic search is a primary acquisition channel.
- The site seeks Google AdSense approval and uses clearly disclosed affiliate links.
- Fifteen guides, three Word templates, legal pages, and an editorial policy are already present.
- Cloudflare Pages publishes the generated `site/` directory.

## Capabilities and Constraints

- Preserve canonical URLs, sitemap and robots generation, structured data, verification meta tags, and affiliate `rel="sponsored"` attributes.
- Preserve all guides, downloads, author attribution, legal content, and internal links.
- The Markdown parser supports only the syntax documented in `AGENTS.md`.
- The site must remain fully usable without JavaScript.
- No fabricated testimonials, customer counts, placement rates, or interview guarantees.

## Brand Commitments

- Free complete resources, with paid tools presented only as optional conveniences.
- Concrete examples over abstract advice.
- Honest framing of projects and coursework, never invented employment history.
- Readable, ATS-aware, and accessible presentation.
- A useful first screen on desktop and mobile.

## Evidence on Hand

- Repository brief and `AGENTS.md` define the audience, search strategy, publishing workflow, and protected SEO elements.
- Fifteen Markdown guides and three downloadable `.docx` templates exist locally.
- The live site and local generator were inspected on November 26, 2026.
- The live homepage and pillar article were captured at desktop and mobile sizes before redesign.
- Existing guide copy supplies the annotated machine-learning project example used in the new homepage visual.

## Product Principles

1. Show the transformation from project work to resume evidence; do not merely claim expertise.
2. Let visitors reach a relevant guide or template within one clear action.
3. Use editorial hierarchy and generous reading space instead of decorative dashboard patterns.
4. Keep every claim specific, truthful, and supported by repository content.
5. Treat mobile navigation, keyboard access, reduced motion, and readable line lengths as release requirements.

## Accessibility and Inclusion

- Semantic landmarks and heading order, keyboard-accessible navigation, visible focus states, and meaningful link text.
- Body text targets WCAG AA contrast and remains at least 16px on small screens.
- Touch targets are at least 44px where practical.
- Motion uses a single restrained entrance and is disabled under `prefers-reduced-motion`.
- Content remains visible without animation or JavaScript; long titles, CJK, RTL, and zoom must reflow without clipping.

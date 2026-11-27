# Scheduled Content Queue

This directory holds the 100-topic original-content plan and articles that are ready for future publication. Files here are not part of the live site until `publish_next.py` moves one into `pages/`.

## Status meanings

- `ready`: the Markdown file exists in this directory and passes all publication checks.
- `draft`: the topic is reserved, but the full article is not finished. Drafts never publish automatically.
- `published`: the article has been moved to `pages/` and included in a deployment.

`manifest.json` reserves each slug, title, category, keyword, and publication order. Check the currently published guides before changing a reserved topic; overlapping search intent should be merged rather than published as a second article.

## Article requirements

Every ready article must include:

- YAML frontmatter with `slug`, `category`, `title`, `keyword`, `description`, `summary`, `template`, and `related`
- `published: auto` and `updated: auto`, replaced with the actual publication date by the publisher
- 1500–1900 words of original English content
- A complete illustrative example, practical rewrites, copy-ready material, and 4–5 FAQ entries
- Existing slugs only in `related`
- No copied reference text, invented metrics, fake credentials, or guaranteed outcomes

Reference articles are used to understand search intent and useful structure, not as text to paraphrase. A ready article needs its own examples, explanation, and verification steps.

## Manual publication

Run from the repository root:

```bash
python publish_next.py --check   # validate the next ready article without changing files
python publish_next.py           # move exactly one ready article into pages/
python gen_missing_og.py
python build_site.py
python validate_build.py
```

Commit the moved article, updated manifest, generated site, and documentation. Pushing to `main` deploys through Cloudflare Pages.

## Automatic publication

`.github/workflows/publish-scheduled-guide.yml` runs at 01:17 UTC (09:17 Asia/Shanghai) on Monday, Wednesday, and Friday, and can also be started manually with **Run workflow**. It publishes at most one ready article, rebuilds and validates the site, then commits and pushes only when an article was actually published. If no article is ready, it exits without creating a commit.

Before publication, the publisher rejects duplicate titles or keywords, exact sentences of 12 or more words shared with another guide, and candidates whose 8-word-shingle Jaccard similarity with any published or queued guide is 0.20 or higher. These checks reduce repetition but do not guarantee AdSense approval; substantive review is still required.

# Deployment Note v1

## Current State
The project now has a static site shell with 5 generated HTML pages under `site/`.

## What Can Be Deployed Right Now
- `site/index.html`
- `site/status.html`
- `site/styles.css`
- `site/pages/*.html`

## Simplest Deployment Path
Use a static host such as Cloudflare Pages or Netlify.
Point the publish directory to `projects/english-template-site/site`.

## Minimum Pre-Deploy Checklist
- verify all 5 pages exist in `site/pages/`
- open `site/index.html` locally and check navigation
- confirm internal links point to `/pages/*.html`
- add custom domain only after first successful static deploy

## Not Done Yet
- analytics
- search console verification
- sitemap/robots
- beginner hand-holding deployment guide

## Next Best Step
After this round, write a true beginner deployment guide with step-by-step host setup, publish directory selection, and post-deploy checks.

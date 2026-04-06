from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path('/root/.openclaw/workspace/projects/english-template-site')
PAGES_DIR = ROOT / 'pages'
SITE_DIR = ROOT / 'site'
SITE_PAGES_DIR = SITE_DIR / 'pages'
BASE_URL = 'https://resumepathlab.com'

PAGES = [
    {
        'slug': 'entry-level-machine-learning-engineer-resume',
        'title': 'Entry Level Machine Learning Engineer Resume',
        'keyword': 'entry level machine learning engineer resume',
        'role': 'Pillar / Core Conversion',
        'summary': 'Turn adjacent software, CS, or data backgrounds into a credible entry-level machine-learning-resume path.',
        'source': PAGES_DIR / 'entry-level-machine-learning-engineer-resume.md',
    },
    {
        'slug': 'software-engineer-resume-no-experience',
        'title': 'Software Engineer Resume With No Experience',
        'keyword': 'software engineer resume no experience',
        'role': 'Traffic Entry',
        'summary': 'Capture broad no-experience software-resume demand and route the right readers toward the ML path.',
        'source': PAGES_DIR / 'software-engineer-resume-no-experience.md',
    },
    {
        'slug': 'entry-level-data-science-resume',
        'title': 'Entry Level Data Science Resume',
        'keyword': 'entry level data science resume',
        'role': 'Bridge Entry',
        'summary': 'Capture adjacent data-science demand and move users toward stronger machine-learning positioning when relevant.',
        'source': PAGES_DIR / 'entry-level-data-science-resume.md',
    },
    {
        'slug': 'machine-learning-projects-for-resume',
        'title': 'Machine Learning Projects for Resume Beginners',
        'keyword': 'machine learning projects for resume beginner',
        'role': 'Longtail Signal',
        'summary': 'Show beginners which ML projects are resume-worthy, how to write them, and how to map them to job descriptions.',
        'source': PAGES_DIR / 'machine-learning-projects-for-resume.md',
    },
]

PLANNED = []


def inline_format(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    chunks: list[str] = []
    in_ul = False
    in_ol = False
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            joined = ' '.join(part.strip() for part in paragraph if part.strip())
            if joined:
                chunks.append(f'<p>{inline_format(joined)}</p>')
            paragraph = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            chunks.append('</ul>')
            in_ul = False
        if in_ol:
            chunks.append('</ol>')
            in_ol = False

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            close_lists()
            continue
        if stripped.startswith('# '):
            flush_paragraph()
            close_lists()
            chunks.append(f'<h1>{inline_format(stripped[2:])}</h1>')
            continue
        if stripped.startswith('## '):
            flush_paragraph()
            close_lists()
            chunks.append(f'<h2>{inline_format(stripped[3:])}</h2>')
            continue
        if stripped.startswith('### '):
            flush_paragraph()
            close_lists()
            chunks.append(f'<h3>{inline_format(stripped[4:])}</h3>')
            continue
        if re.match(r'^-\s+', stripped):
            flush_paragraph()
            if in_ol:
                chunks.append('</ol>')
                in_ol = False
            if not in_ul:
                chunks.append('<ul>')
                in_ul = True
            chunks.append(f'<li>{inline_format(re.sub(r"^-\\s+", "", stripped))}</li>')
            continue
        if re.match(r'^\d+\.\s+', stripped):
            flush_paragraph()
            if in_ul:
                chunks.append('</ul>')
                in_ul = False
            if not in_ol:
                chunks.append('<ol>')
                in_ol = True
            chunks.append(f'<li>{inline_format(re.sub(r"^\\d+\\.\\s+", "", stripped))}</li>')
            continue
        if stripped.startswith('> '):
            flush_paragraph()
            close_lists()
            chunks.append(f'<blockquote>{inline_format(stripped[2:])}</blockquote>')
            continue
        paragraph.append(stripped)

    flush_paragraph()
    close_lists()
    return '\n'.join(chunks)


GOOGLE_SITE_VERIFICATION = "zNXWb6AU4dkWiFODD_S9UiH9y3zi7Hr3vD-eHLggWnA"


def shell(title: str, body: str, description: str, nav_html: str) -> str:
    verification_meta = ""
    if GOOGLE_SITE_VERIFICATION:
        verification_meta = f'  <meta name="google-site-verification" content="{html.escape(GOOGLE_SITE_VERIFICATION)}">\n'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
{verification_meta}  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="/index.html">Resume Path Lab</a>
      <nav class="top-nav">{nav_html}</nav>
    </header>
    <main>
      {body}
    </main>
    <footer class="site-footer">
      <p>Round 1 validation build for the English template site project.</p>
    </footer>
  </div>
</body>
</html>
'''


def build_nav() -> str:
    links = ['<a href="/index.html">Home</a>']
    for page in PAGES:
        links.append(f'<a href="/pages/{page["slug"]}.html">{html.escape(page["title"])}</a>')
    links.append('<a href="/status.html">Status</a>')
    return ''.join(links)


def build_home(nav_html: str) -> None:
    cards = []
    for page in PAGES:
        cards.append(
            f'''<article class="card">
<h2><a href="/pages/{page["slug"]}.html">{html.escape(page["title"])}</a></h2>
<p class="meta">{html.escape(page["role"])} · {html.escape(page["keyword"])}</p>
<p>{html.escape(page["summary"])}</p>
</article>'''
        )
    planned = []
    for page in PLANNED:
        planned.append(
            f'''<article class="card muted">
<h2>{html.escape(page["title"])}</h2>
<p class="meta">{html.escape(page["role"])}</p>
<p>Planned next. Not written yet.</p>
</article>'''
        )
    planned_section = ''
    if planned:
        planned_section = f'''
<section>
  <h2>Next Planned Pages</h2>
  <div class="grid">{''.join(planned)}</div>
</section>
'''
    body = f'''
<section class="hero">
  <p class="eyebrow">Round 1 Site Shell</p>
  <h1>English Resume Template Site</h1>
  <p class="lead">This build turns the current markdown drafts into a site-ready shell so the project can move from page samples to a real publishable structure.</p>
</section>
<section>
  <h2>Live Pages</h2>
  <div class="grid">{''.join(cards)}</div>
</section>
{planned_section}
'''
    (SITE_DIR / 'index.html').write_text(shell('Resume Path Lab', body, 'Validation build for the English resume template site.', nav_html), encoding='utf-8')


def build_status(nav_html: str) -> None:
    body = '''
<section class="hero compact">
  <p class="eyebrow">Execution Status</p>
  <h1>Current Build State</h1>
</section>
<section class="grid single">
  <article class="card">
    <h2>Built</h2>
    <ul>
      <li>Shared site shell and CSS</li>
      <li>Homepage with current live pages</li>
      <li>4 HTML content pages generated from markdown drafts</li>
      <li>Explicit status page to keep unfinished scope visible</li>
    </ul>
  </article>
  <article class="card">
    <h2>Not Built Yet</h2>
    <ul>
      <li>Deployment pipeline</li>
      <li>Search Console / analytics integration</li>
      <li>Framework-based component system</li>
    </ul>
  </article>
</section>
'''
    (SITE_DIR / 'status.html').write_text(shell('Build Status', body, 'Honest status page for the validation build.', nav_html), encoding='utf-8')


def build_page(page: dict[str, str], nav_html: str) -> None:
    markdown = page['source'].read_text(encoding='utf-8')
    article = markdown_to_html(markdown)
    body = f'''
<section class="page-head">
  <p class="eyebrow">{html.escape(page['role'])}</p>
  <h1>{html.escape(page['title'])}</h1>
  <p class="lead">{html.escape(page['summary'])}</p>
  <p class="meta">Target keyword: <code>{html.escape(page['keyword'])}</code></p>
</section>
<article class="prose">
{article}
</article>
'''
    out = SITE_PAGES_DIR / f"{page['slug']}.html"
    out.write_text(shell(page['title'], body, page['summary'], nav_html), encoding='utf-8')


def build_seo_files() -> None:
    urls = [f'{BASE_URL}/']
    for page in PAGES:
        urls.append(f"{BASE_URL}/pages/{page['slug']}.html")

    sitemap_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        sitemap_parts.append('  <url>')
        sitemap_parts.append(f'    <loc>{html.escape(url)}</loc>')
        sitemap_parts.append('  </url>')
    sitemap_parts.append('</urlset>')
    (SITE_DIR / 'sitemap.xml').write_text('\n'.join(sitemap_parts) + '\n', encoding='utf-8')

    robots = f'''User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
'''
    (SITE_DIR / 'robots.txt').write_text(robots, encoding='utf-8')


def build_css() -> None:
    css = '''
:root {
  --bg: #f6f2ea;
  --panel: #fffdf8;
  --ink: #1f1a17;
  --muted: #6f6259;
  --line: #ddd2c3;
  --accent: #0f766e;
  --accent-soft: #d8f3ee;
  --shadow: 0 20px 40px rgba(45, 33, 20, 0.08);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: radial-gradient(circle at top, #fff9ef 0%, var(--bg) 58%);
  line-height: 1.7;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.site-shell { max-width: 1040px; margin: 0 auto; padding: 24px; }
.site-header {
  display: flex; justify-content: space-between; gap: 16px; align-items: center;
  padding: 14px 0 24px; border-bottom: 1px solid var(--line);
}
.brand { font-size: 1.1rem; font-weight: 700; color: var(--ink); }
.top-nav { display: flex; flex-wrap: wrap; gap: 14px; }
.hero, .page-head {
  padding: 36px; margin: 28px 0; background: var(--panel); border: 1px solid var(--line);
  border-radius: 24px; box-shadow: var(--shadow);
}
.hero.compact { padding-bottom: 22px; }
.eyebrow { text-transform: uppercase; letter-spacing: .14em; font-size: .78rem; color: var(--muted); }
.lead { font-size: 1.12rem; color: #3b322d; max-width: 740px; }
.meta { color: var(--muted); font-size: .95rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; }
.grid.single { grid-template-columns: 1fr; }
.card {
  background: var(--panel); border: 1px solid var(--line); border-radius: 22px;
  padding: 22px; box-shadow: var(--shadow);
}
.card.muted { opacity: .88; }
.prose {
  background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
  padding: 34px; box-shadow: var(--shadow);
}
.prose h1:first-child { display: none; }
.prose h2 { margin-top: 2.2rem; font-size: 1.55rem; }
.prose h3 { margin-top: 1.4rem; font-size: 1.15rem; }
.prose p, .prose li, .prose blockquote { font-size: 1.02rem; }
.prose ul, .prose ol { padding-left: 1.4rem; }
.prose blockquote {
  margin: 1rem 0; padding: 1rem 1.2rem; background: var(--accent-soft);
  border-left: 4px solid var(--accent); border-radius: 12px;
}
code {
  background: #efe8dd; padding: .12rem .4rem; border-radius: 6px; font-size: .92em;
}
.site-footer { padding: 28px 0 40px; color: var(--muted); font-size: .92rem; }
@media (max-width: 720px) {
  .site-shell { padding: 18px; }
  .site-header { align-items: flex-start; flex-direction: column; }
  .hero, .page-head, .prose { padding: 22px; }
}
'''
    (SITE_DIR / 'styles.css').write_text(css.strip() + '\n', encoding='utf-8')


def main() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    SITE_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    nav_html = build_nav()
    build_css()
    build_home(nav_html)
    build_status(nav_html)
    for page in PAGES:
        build_page(page, nav_html)
    build_seo_files()


if __name__ == '__main__':
    main()

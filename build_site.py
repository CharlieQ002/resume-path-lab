from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / 'pages'
SITE_DIR = ROOT / 'site'
SITE_PAGES_DIR = SITE_DIR / 'pages'
BASE_URL = 'https://resumepathlab.com'

SITE_NAME = 'Resume Path Lab'
TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# MONETIZATION: replace these with your affiliate links once approved.
# Sign up: Kickresume (Impact), ResumeGenius, Zety (CJ / Impact).
# Until then the buttons point to the plain sites and earn you nothing.
# ---------------------------------------------------------------------------
AFFILIATE = {
    'kickresume': 'https://www.kickresume.com/',
    'resumegenius': 'https://resumegenius.com/',
    'zety': 'https://zety.com/',
}

GOOGLE_SITE_VERIFICATION = 'zNXWb6AU4dkWiFODD_S9UiH9y3zi7Hr3vD-eHLggWnA'
YEAHPROMOS_VERIFICATION = '5c5859c41495'

PAGES = [
    {
        'slug': 'entry-level-machine-learning-engineer-resume',
        'title': 'Entry-Level Machine Learning Engineer Resume: Example & Template',
        'nav': 'ML Engineer Resume',
        'pillar': True,
        'keyword': 'entry level machine learning engineer resume',
        'description': 'Entry-level machine learning engineer resume example with a copy-ready template. Turn software or data projects into ML resume bullets that get interviews.',
        'summary': 'Turn software, CS, or data project experience into a credible entry-level machine learning engineer resume, step by step.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'how-to-write-machine-learning-resume-without-experience',
            'machine-learning-resume-summary-examples',
            'machine-learning-projects-for-resume',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'how-to-write-machine-learning-resume-without-experience',
        'title': 'How to Write a Machine Learning Resume Without Experience',
        'nav': 'ML Resume, No Experience',
        'pillar': True,
        'keyword': 'how to write machine learning resume without experience',
        'description': 'How to write a machine learning resume without experience: the 7-step method to turn software, CS, or data projects into credible ML resume proof.',
        'summary': 'The 7-step method for writing a credible machine learning resume when you have no formal ML work experience.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'entry-level-machine-learning-engineer-resume',
            'machine-learning-resume-summary-examples',
            'machine-learning-projects-for-resume',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'software-engineer-resume-no-experience',
        'title': 'Software Engineer Resume With No Experience: Example & Guide',
        'nav': 'Software Engineer Resume',
        'pillar': True,
        'keyword': 'software engineer resume no experience',
        'description': 'Software engineer resume with no experience: real example, copy-ready template, and steps to turn projects and coursework into interview-worthy bullets.',
        'summary': 'A no-experience software engineer resume example, plus how to route your projects toward ML and data roles.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'entry-level-machine-learning-engineer-resume',
            'entry-level-data-science-resume',
            'how-to-write-machine-learning-resume-without-experience',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'entry-level-data-science-resume',
        'title': 'Entry-Level Data Science Resume: Example & Template',
        'nav': 'Data Science Resume',
        'pillar': True,
        'keyword': 'entry level data science resume',
        'description': 'Entry-level data science resume example with a copy-ready template. Learn how to frame projects, skills, and coursework for your first data job.',
        'summary': 'An entry-level data science resume example, with guidance on framing projects and skills for a first data role.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-analyst-resume',
            'entry-level-machine-learning-engineer-resume',
            'machine-learning-projects-for-resume',
            'software-engineer-resume-no-experience',
        ],
    },
    {
        'slug': 'machine-learning-projects-for-resume',
        'title': 'Machine Learning Projects for a Resume: Beginner Guide',
        'nav': 'ML Projects for Resume',
        'pillar': True,
        'keyword': 'machine learning projects for resume beginner',
        'description': 'The best machine learning projects for a resume as a beginner, with copy-ready bullet templates and tips for mapping projects to job descriptions.',
        'summary': 'Which ML projects are resume-worthy, how to write them up, and how to map them to real job descriptions.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'kaggle-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
            'how-to-write-machine-learning-resume-without-experience',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'machine-learning-resume-summary-examples',
        'title': 'Machine Learning Resume Summary Examples: 8 Entry-Level Versions',
        'nav': 'Summary Examples',
        'keyword': 'machine learning resume summary examples',
        'description': '8 copy-ready machine learning resume summary examples for entry-level candidates: CS grads, career changers, and Kaggle competitors.',
        'summary': '8 copy-ready ML resume summary examples by background, plus the 3-part formula and weak-to-fixed rewrites.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'entry-level-machine-learning-engineer-resume',
            'how-to-write-machine-learning-resume-without-experience',
            'machine-learning-projects-for-resume',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'kaggle-projects-for-resume',
        'title': 'Kaggle Projects for a Resume: What Actually Counts (2026 Guide)',
        'nav': 'Kaggle Projects',
        'keyword': 'kaggle projects for resume',
        'description': 'Learn which Kaggle projects count on a resume, how to write competition and notebook bullets, and when a personal project beats a Kaggle ranking.',
        'summary': 'Which Kaggle activities carry weight, copy-ready competition and notebook bullets, and when to skip Kaggle entirely.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'machine-learning-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
            'machine-learning-resume-summary-examples',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'entry-level-data-analyst-resume',
        'title': 'Entry-Level Data Analyst Resume: Example & Template',
        'nav': 'Data Analyst Resume',
        'keyword': 'entry level data analyst resume',
        'description': 'Entry-level data analyst resume example with SQL, Excel, and visualization project bullets. Copy-ready template for first data analyst jobs.',
        'summary': 'An entry-level data analyst resume example, with SQL, Excel, and visualization bullets that work without formal experience.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-science-resume',
            'machine-learning-projects-for-resume',
            'software-engineer-resume-no-experience',
            'kaggle-projects-for-resume',
        ],
    },
    {
        'slug': 'resume-with-no-work-experience',
        'title': 'How to Write a Resume With No Work Experience: First Resume Guide',
        'nav': 'First Resume Guide',
        'keyword': 'how to write a resume with no work experience',
        'description': 'How to write a resume with no work experience: a complete first-resume example, plus how to fill the page with coursework, projects, and volunteering.',
        'summary': 'A complete first-resume example and method for candidates with zero work history, built on coursework, projects, and volunteering.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'software-engineer-resume-no-experience',
            'machine-learning-resume-summary-examples',
            'ats-friendly-resume-guide',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'ats-friendly-resume-guide',
        'title': 'ATS-Friendly Resume for Tech Jobs: Format Rules & Example',
        'nav': 'ATS Resume Guide',
        'keyword': 'ats friendly resume for tech jobs',
        'description': 'What an ATS actually does, the formatting rules that keep a tech resume parseable, a keyword-matching method, and a full ATS-friendly example.',
        'summary': 'How applicant tracking systems really filter resumes, the format rules that survive parsing, and a complete ATS-friendly example.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'resume-with-no-work-experience',
            'machine-learning-resume-summary-examples',
            'entry-level-machine-learning-engineer-resume',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'machine-learning-engineer-cover-letter',
        'title': 'Machine Learning Engineer Cover Letter: Entry-Level Example & Templates',
        'nav': 'ML Cover Letter',
        'keyword': 'machine learning engineer cover letter entry level',
        'description': 'An entry-level machine learning engineer cover letter example with a section-by-section breakdown, copy-ready paragraph templates, and common mistakes.',
        'summary': 'A complete entry-level ML engineer cover letter example, broken down paragraph by paragraph, with copy-ready templates.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'entry-level-machine-learning-engineer-resume',
            'how-to-write-machine-learning-resume-without-experience',
            'machine-learning-resume-summary-examples',
            'ats-friendly-resume-guide',
        ],
    },
]

PAGE_BY_SLUG = {p['slug']: p for p in PAGES}

LEGAL_DIR = ROOT / 'legal'

LEGAL_PAGES = [
    {
        'slug': 'about',
        'title': f'About {SITE_NAME}',
        'nav': 'About',
        'description': 'What Resume Path Lab publishes, why it exists, and how we write our entry-level resume guides.',
    },
    {
        'slug': 'contact',
        'title': f'Contact {SITE_NAME}',
        'nav': 'Contact',
        'description': 'How to reach Resume Path Lab: corrections, suggestions, feedback, and privacy requests.',
    },
    {
        'slug': 'privacy-policy',
        'title': 'Privacy Policy',
        'nav': 'Privacy Policy',
        'description': 'What information Resume Path Lab collects, how cookies and advertising work, and your choices.',
    },
    {
        'slug': 'terms',
        'title': 'Terms of Use',
        'nav': 'Terms',
        'description': 'The terms for using Resume Path Lab, including acceptable use and liability limits.',
    },
    {
        'slug': 'disclaimer',
        'title': 'Disclaimer',
        'nav': 'Disclaimer',
        'description': 'Disclaimers for Resume Path Lab content, including our affiliate link disclosure.',
    },
]


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


def extract_faq(markdown: str) -> list[tuple[str, str]]:
    """Pull (question, answer) pairs out of the '## FAQ' section."""
    faqs: list[tuple[str, str]] = []
    in_faq = False
    current_q: str | None = None
    answer_lines: list[str] = []

    def flush() -> None:
        nonlocal current_q, answer_lines
        if current_q and answer_lines:
            answer = ' '.join(a.strip() for a in answer_lines if a.strip())
            if answer:
                faqs.append((current_q, answer))
        current_q = None
        answer_lines = []

    for raw in markdown.splitlines():
        stripped = raw.strip()
        if stripped.startswith('## '):
            if stripped == '## FAQ':
                in_faq = True
                continue
            if in_faq:
                break
        if not in_faq:
            continue
        if stripped.startswith('### '):
            flush()
            current_q = stripped[4:].strip()
        elif current_q and stripped:
            answer_lines.append(stripped)
    flush()
    return faqs


def build_nav() -> str:
    links = ['<a href="/">Home</a>']
    for page in PAGES:
        if not page.get('pillar'):
            continue
        links.append(f'<a href="/pages/{page["slug"]}">{html.escape(page["nav"])}</a>')
    return ''.join(links)


def affiliate_cta() -> str:
    return f'''
<aside class="cta-box">
  <h3>Want this done in 15 minutes?</h3>
  <p>Copy the examples above into <a href="{html.escape(AFFILIATE["kickresume"])}" rel="sponsored noopener" target="_blank">Kickresume</a> and get a polished, ATS-friendly PDF resume without fighting Word formatting. Templates, pre-written bullets, cover letter included.</p>
  <a class="cta-button" href="{html.escape(AFFILIATE["kickresume"])}" rel="sponsored noopener" target="_blank">Build my resume with Kickresume</a>
  <p class="cta-alt">Free alternatives: <a href="{html.escape(AFFILIATE["resumegenius"])}" rel="sponsored noopener" target="_blank">ResumeGenius</a> · <a href="{html.escape(AFFILIATE["zety"])}" rel="sponsored noopener" target="_blank">Zety</a></p>
</aside>'''


def related_box(slug: str) -> str:
    page = PAGE_BY_SLUG[slug]
    cards = []
    for rel_slug in page['related']:
        rel = PAGE_BY_SLUG[rel_slug]
        cards.append(
            f'''<article class="card">
<h3><a href="/pages/{rel['slug']}">{html.escape(rel['title'])}</a></h3>
<p>{html.escape(rel['summary'])}</p>
</article>'''
        )
    return f'''
<section class="related">
  <h2>Related guides</h2>
  <div class="grid">{''.join(cards)}</div>
</section>'''


def json_ld(payload: dict) -> str:
    return f'<script type="application/ld+json">{json.dumps(payload, ensure_ascii=False)}</script>'


def page_schema(page: dict, canonical: str, faqs: list[tuple[str, str]]) -> str:
    schemas = [
        {
            '@context': 'https://schema.org',
            '@type': 'Article',
            'headline': page['title'],
            'description': page['description'],
            'author': {'@type': 'Organization', 'name': SITE_NAME, 'url': BASE_URL},
            'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': BASE_URL},
            'datePublished': '2026-04-05',
            'dateModified': TODAY,
            'mainEntityOfPage': canonical,
        }
    ]
    if faqs:
        schemas.append({
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': [
                {
                    '@type': 'Question',
                    'name': q,
                    'acceptedAnswer': {'@type': 'Answer', 'text': a},
                }
                for q, a in faqs
            ],
        })
    return '\n'.join(json_ld(s) for s in schemas)


def build_footer_nav() -> str:
    return ' · '.join(
        f'<a href="/{page["slug"]}">{html.escape(page["nav"])}</a>' for page in LEGAL_PAGES
    )


def shell(title: str, description: str, canonical: str, nav_html: str, body: str, extra_head: str = '', og_image: str = '') -> str:
    footer_nav = build_footer_nav()
    verification = ''
    if GOOGLE_SITE_VERIFICATION:
        verification += f'  <meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">\n'
    if YEAHPROMOS_VERIFICATION:
        verification += f'  <meta name="verify-yeahpromos" content="{YEAHPROMOS_VERIFICATION}">\n'
    og_image = og_image or (BASE_URL + '/assets/og/home.png')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
{verification}  <link rel="canonical" href="{html.escape(canonical)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{html.escape(canonical)}">
  <meta property="og:image" content="{html.escape(og_image)}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{html.escape(og_image)}">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
{extra_head}  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="/">{SITE_NAME}</a>
      <nav class="top-nav">{nav_html}</nav>
    </header>
    <main>
{body}
    </main>
    <footer class="site-footer">
      <p>{SITE_NAME} publishes free, copy-ready resume examples and templates for entry-level machine learning, software, and data roles. Some links are affiliate links: we may earn a commission at no extra cost to you.</p>
      <nav class="footer-nav">{footer_nav}</nav>
      <p>&copy; 2026 {SITE_NAME}</p>
    </footer>
  </div>
</body>
</html>
'''


def build_home(nav_html: str) -> None:
    cards = []
    for page in PAGES:
        cards.append(
            f'''<article class="card">
<h2><a href="/pages/{page['slug']}">{html.escape(page['title'])}</a></h2>
<p>{html.escape(page['summary'])}</p>
</article>'''
        )
    body = f'''
<section class="hero">
  <p class="eyebrow">Free resume examples & templates</p>
  <h1>Entry-Level Resume Guides That Get Interviews</h1>
  <p class="lead">Copy-ready resume examples, project bullet templates, and step-by-step guides for breaking into machine learning, software engineering, and data science with little or no formal experience.</p>
</section>
<section>
  <h2>All guides</h2>
  <div class="grid">{''.join(cards)}</div>
</section>
<section class="value-prop">
  <h2>Why these guides work</h2>
  <ul>
    <li><strong>Real examples, not filler.</strong> Every guide includes a full resume example and bullets you can copy and adapt.</li>
    <li><strong>Built for no-experience candidates.</strong> Projects and coursework framed as proof, not decoration.</li>
    <li><strong>Mapped to real job descriptions.</strong> Learn to mirror employer language so ATS and recruiters both notice.</li>
  </ul>
</section>
'''
    description = 'Free, copy-ready resume examples and templates for entry-level machine learning engineers, software engineers, and data scientists with no experience.'
    (SITE_DIR / 'index.html').write_text(
        shell(f'{SITE_NAME} | Free Resume Examples for Entry-Level Tech Careers', description, f'{BASE_URL}/', nav_html, body),
        encoding='utf-8',
    )


def build_status(nav_html: str) -> None:
    body = '''
<section class="hero compact">
  <p class="eyebrow">Build log</p>
  <h1>Site Status</h1>
</section>
<section class="grid single">
  <article class="card">
    <h2>Live now</h2>
    <ul>
      <li>11 full resume guides (about 17,000 words of copy-ready content)</li>
      <li>About, Contact, Privacy Policy, Terms, and Disclaimer pages</li>
      <li>3 downloadable Word resume templates (ATS-safe single-column layouts)</li>
      <li>FAQ structured data, canonical URLs, Open Graph images on every page</li>
      <li>Clean internal linking between all guides</li>
      <li>Sitemap, robots.txt, Search Console verification</li>
    </ul>
  </article>
  <article class="card">
    <h2>In progress</h2>
    <ul>
      <li>Affiliate program approvals (Kickresume, ResumeGenius, Zety)</li>
      <li>Google Docs versions of the templates</li>
      <li>Backlink outreach (Reddit, Pinterest, relevant forums)</li>
    </ul>
  </article>
</section>
'''
    (SITE_DIR / 'status.html').write_text(
        shell(f'Status | {SITE_NAME}', 'Live pages and roadmap for Resume Path Lab.', f'{BASE_URL}/status', nav_html, body),
        encoding='utf-8',
    )


def build_legal(page: dict, nav_html: str) -> None:
    markdown = (LEGAL_DIR / f"{page['slug']}.md").read_text(encoding='utf-8')
    article = markdown_to_html(markdown)
    canonical = f"{BASE_URL}/{page['slug']}"
    body = f'''
<section class="page-head">
  <p class="eyebrow">{SITE_NAME}</p>
  <h1>{html.escape(page['title'])}</h1>
</section>
<article class="prose">
{article}
</article>
'''
    out = SITE_DIR / f"{page['slug']}.html"
    out.write_text(shell(page['title'], page['description'], canonical, nav_html, body), encoding='utf-8')


def insert_before_faq(article: str, cta: str) -> str:
    idx = article.find('<h2>FAQ</h2>')
    if idx == -1:
        return article + cta
    return article[:idx] + cta + '\n' + article[idx:]


def download_box(page: dict) -> str:
    template = page.get('template', '')
    if not template:
        return ''
    return (
        '<section class="download-box" aria-label="Free template download">'
        '<div class="download-box-text">'
        '<strong>Free matching template</strong>'
        '<span>Word document · ATS-safe single-column layout · matches every example on this page</span>'
        '</div>'
        f'<a class="download-box-btn" href="/downloads/{template}" download>Download .docx</a>'
        '</section>'
    )


def build_page(page: dict, nav_html: str) -> None:
    markdown = (PAGES_DIR / f"{page['slug']}.md").read_text(encoding='utf-8')
    article = markdown_to_html(markdown)
    cta = affiliate_cta()
    article = insert_before_faq(article, cta)
    canonical = f"{BASE_URL}/pages/{page['slug']}"
    faqs = extract_faq(markdown)
    body = f'''
<section class="page-head">
  <p class="eyebrow">Free guide + copy-ready template</p>
  <h1>{html.escape(page['title'])}</h1>
  <p class="lead">{html.escape(page['summary'])}</p>
</section>
{download_box(page)}
<article class="prose">
{article}
</article>
{related_box(page['slug'])}
'''
    schema = page_schema(page, canonical, faqs)
    out = SITE_PAGES_DIR / f"{page['slug']}.html"
    og_image = f"{BASE_URL}/assets/og/{page['slug']}.png"
    if not (SITE_DIR / 'assets' / 'og' / f"{page['slug']}.png").exists():
        og_image = f"{BASE_URL}/assets/og/home.png"
    out.write_text(
        shell(
            page['title'],
            page['description'],
            canonical,
            nav_html,
            body,
            extra_head=schema + '\n',
            og_image=og_image,
        ),
        encoding='utf-8',
    )


def build_seo_files() -> None:
    urls = [(f'{BASE_URL}/', TODAY), (f'{BASE_URL}/status', TODAY)]
    for page in PAGES:
        urls.append((f"{BASE_URL}/pages/{page['slug']}", TODAY))
    for page in LEGAL_PAGES:
        urls.append((f"{BASE_URL}/{page['slug']}", TODAY))

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, lastmod in urls:
        parts.append('  <url>')
        parts.append(f'    <loc>{html.escape(url)}</loc>')
        parts.append(f'    <lastmod>{lastmod}</lastmod>')
        parts.append('  </url>')
    parts.append('</urlset>')
    (SITE_DIR / 'sitemap.xml').write_text('\n'.join(parts) + '\n', encoding='utf-8')

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
.top-nav { display: flex; flex-wrap: wrap; gap: 14px; font-size: .95rem; }
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
.card h3 { margin-top: 0; font-size: 1.05rem; }
.prose {
  background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
  padding: 34px; box-shadow: var(--shadow);
}
.prose h1:first-child { display: none; }
.prose h2 { margin-top: 2.2rem; font-size: 1.55rem; }
.prose h2:first-of-type { margin-top: 0; }
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
.cta-box {
  margin: 2.4rem 0; padding: 26px 28px; background: var(--accent-soft);
  border: 1px solid var(--accent); border-radius: 18px;
}
.cta-box h3 { margin-top: 0; color: #0b4f4a; }
.cta-button {
  display: inline-block; margin: .6rem 0; padding: 12px 22px;
  background: var(--accent); color: #fff; border-radius: 12px; font-weight: 700;
}
.cta-button:hover { background: #0b5a54; text-decoration: none; }
.cta-alt { font-size: .9rem; color: var(--muted); margin-bottom: 0; }
.value-prop { margin: 28px 0; padding: 28px; background: var(--panel); border: 1px solid var(--line); border-radius: 24px; }
.related { margin: 28px 0 8px; }
.related h2 { font-size: 1.4rem; }
.site-footer { padding: 28px 0 40px; color: var(--muted); font-size: .9rem; border-top: 1px solid var(--line); margin-top: 32px; }
.footer-nav { margin: 10px 0; line-height: 2; }
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
    for page in LEGAL_PAGES:
        build_legal(page, nav_html)
    build_seo_files()


if __name__ == '__main__':
    main()

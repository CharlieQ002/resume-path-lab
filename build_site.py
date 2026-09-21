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
_today = date.today()
UPDATED_LABEL = f'{_today:%b} {_today.day}, {_today:%Y}'

# ---------------------------------------------------------------------------
# AUTHOR: placeholder pen name shown in every byline and the author box.
# Replace name/title/bio here and it updates site-wide on the next build.
# ---------------------------------------------------------------------------
AUTHOR = {
    'name': 'Jordan Blake',
    'title': 'Career Writer & Former Tech Recruiting Coordinator',
    'bio': (
        'Jordan Blake is a career writer and former tech recruiting coordinator who '
        'screened entry-level applications for software, data, and machine learning roles. '
        'Jordan writes from that screening experience: what survives the ATS parse, what '
        'survives the six-second recruiter scan, and what quietly gets resumes filtered out.'
    ),
    'url': f'{BASE_URL}/about#about-the-author',
}

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
        'category': 'Machine Learning',
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
        'category': 'Machine Learning',
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
        'category': 'Software',
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
            'python-projects-for-resume',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'entry-level-data-science-resume',
        'category': 'Data',
        'title': 'Entry-Level Data Science Resume: Example & Template',
        'nav': 'Data Science Resume',
        'pillar': True,
        'keyword': 'entry level data science resume',
        'description': 'Entry-level data science resume example with a copy-ready template. Learn how to frame projects, skills, and coursework for your first data job.',
        'summary': 'An entry-level data science resume example, with guidance on framing projects and skills for a first data role.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-analyst-resume',
            'data-science-internship-resume',
            'machine-learning-projects-for-resume',
            'software-engineer-resume-no-experience',
        ],
    },
    {
        'slug': 'machine-learning-projects-for-resume',
        'category': 'Machine Learning',
        'title': 'Machine Learning Projects for a Resume: Beginner Guide',
        'nav': 'ML Projects for Resume',
        'pillar': True,
        'keyword': 'machine learning projects for resume beginner',
        'description': 'The best machine learning projects for a resume as a beginner, with copy-ready bullet templates and tips for mapping projects to job descriptions.',
        'summary': 'Which ML projects are resume-worthy, how to write them up, and how to map them to real job descriptions.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'python-projects-for-resume',
            'kaggle-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'machine-learning-resume-summary-examples',
        'category': 'Machine Learning',
        'title': 'Machine Learning Resume Summary Examples: 8 Entry-Level Versions',
        'nav': 'Summary Examples',
        'keyword': 'machine learning resume summary examples',
        'description': '8 copy-ready machine learning resume summary examples for entry-level candidates: CS grads, career changers, and Kaggle competitors.',
        'summary': '8 copy-ready ML resume summary examples by background, plus the 3-part formula and weak-to-fixed rewrites.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'entry-level-machine-learning-engineer-resume',
            'resume-skills-section-tech',
            'machine-learning-projects-for-resume',
            'entry-level-data-science-resume',
        ],
    },
    {
        'slug': 'kaggle-projects-for-resume',
        'category': 'Machine Learning',
        'title': 'Kaggle Projects for a Resume: What Actually Counts (2026 Guide)',
        'nav': 'Kaggle Projects',
        'keyword': 'kaggle projects for resume',
        'description': 'Learn which Kaggle projects count on a resume, how to write competition and notebook bullets, and when a personal project beats a Kaggle ranking.',
        'summary': 'Which Kaggle activities carry weight, copy-ready competition and notebook bullets, and when to skip Kaggle entirely.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'machine-learning-projects-for-resume',
            'python-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
            'entry-level-data-analyst-resume',
        ],
    },
    {
        'slug': 'entry-level-data-analyst-resume',
        'category': 'Data',
        'title': 'Entry-Level Data Analyst Resume: Example & Template',
        'nav': 'Data Analyst Resume',
        'keyword': 'entry level data analyst resume',
        'description': 'Entry-level data analyst resume example with SQL, Excel, and visualization project bullets. Copy-ready template for first data analyst jobs.',
        'summary': 'An entry-level data analyst resume example, with SQL, Excel, and visualization bullets that work without formal experience.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-science-resume',
            'data-science-internship-resume',
            'python-projects-for-resume',
            'kaggle-projects-for-resume',
        ],
    },
    {
        'slug': 'resume-with-no-work-experience',
        'category': 'Resume Basics',
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
        'category': 'Resume Basics',
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
        'slug': 'resume-skills-section-tech',
        'category': 'Resume Basics',
        'title': 'Tech Resume Skills Section: What to List & How to Group It',
        'nav': 'Skills Section Guide',
        'keyword': 'tech resume skills section',
        'description': 'How to write a tech resume skills section with no experience: what to list, how to group skills, ATS keyword rules, and copy-ready templates.',
        'summary': 'How to build a believable tech resume skills section with no experience: grouping, exact ATS wording, and copy-ready templates.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'ats-friendly-resume-guide',
            'resume-with-no-work-experience',
            'entry-level-machine-learning-engineer-resume',
            'software-engineer-resume-no-experience',
        ],
    },
    {
        'slug': 'machine-learning-engineer-cover-letter',
        'category': 'Machine Learning',
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
    {
        'slug': 'data-science-internship-resume',
        'category': 'Data',
        'title': 'Data Science Internship Resume: What Actually Gets Interviews',
        'keyword': 'data science internship resume',
        'description': 'Data science internship resume guide: the structure that gets interviews, how to frame coursework as experience, and a project example that stands out.',
        'summary': 'The data science internship resume structure recruiters screen for, with coursework framing, project examples, and the mistakes that get applications rejected.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-science-resume',
            'entry-level-data-analyst-resume',
            'entry-level-machine-learning-engineer-resume',
            'machine-learning-resume-summary-examples',
        ],
    },
    {
        'slug': 'python-projects-for-resume',
        'category': 'Machine Learning',
        'title': 'Python Projects for a Resume: 10 That Beat Coursework',
        'keyword': 'python projects for resume',
        'description': 'The best Python projects for a resume have users, data, or a deploy. Ten ideas ranked by interview value, plus copy-ready bullet formulas for each.',
        'summary': 'Ten Python projects ranked by interview value, the three qualities that make a project resume-worthy, and bullet formulas to write them up.',
        'template': 'entry-level-ml-engineer-resume-template.docx',
        'related': [
            'machine-learning-projects-for-resume',
            'kaggle-projects-for-resume',
            'software-engineer-resume-no-experience',
            'entry-level-data-analyst-resume',
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
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+|/[^)\s]*)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def slugify(text: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return slug or 'section'


def extract_toc(markdown: str) -> list[tuple[str, str]]:
    toc = []
    for raw in markdown.splitlines():
        stripped = raw.strip()
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            toc.append((slugify(title), title))
    return toc


def strip_frontmatter(markdown: str) -> str:
    """Drop a leading YAML frontmatter block (--- ... ---) if present.

    Page metadata lives in PAGES; frontmatter in source files is ignored.
    """
    lines = markdown.splitlines()
    if lines and lines[0].strip() == '---':
        for idx in range(1, len(lines)):
            if lines[idx].strip() == '---':
                return '\n'.join(lines[idx + 1:])
    return markdown


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
            heading = stripped[3:]
            chunks.append(f'<h2 id="{slugify(heading)}">{inline_format(heading)}</h2>')
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
            chunks.append(f'<li>{inline_format(re.sub(r"^-\s+", "", stripped))}</li>')
            continue
        if re.match(r'^\d+\.\s+', stripped):
            flush_paragraph()
            if in_ul:
                chunks.append('</ul>')
                in_ul = False
            if not in_ol:
                chunks.append('<ol>')
                in_ol = True
            chunks.append(f'<li>{inline_format(re.sub(r"^\d+\.\s+", "", stripped))}</li>')
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
    links = []
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
            'author': {
                '@type': 'Person',
                'name': AUTHOR['name'],
                'jobTitle': AUTHOR['title'],
                'url': AUTHOR['url'],
            },
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


LOGO_SVG = (
    '<svg class="logo-mark" width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true">'
    '<rect width="30" height="30" rx="8" fill="#1d4ed8"/>'
    '<path d="M9 8h8.5a3.5 3.5 0 0 1 0 7H9V8zm0 7h9l3 7h-4l-3-7h-5v7H9v-7z" fill="#fff"/>'
    '</svg>'
)


def build_footer_nav() -> str:
    return ''.join(
        f'<a href="/{page["slug"]}">{html.escape(page["nav"])}</a>' for page in LEGAL_PAGES
    )


def build_footer_guides() -> str:
    links = []
    for page in PAGES:
        if page.get('pillar'):
            links.append(f'<a href="/pages/{page["slug"]}">{html.escape(page["nav"])}</a>')
    return ''.join(links)


def shell(title: str, description: str, canonical: str, nav_html: str, body: str, extra_head: str = '', og_image: str = '') -> str:
    footer_nav = build_footer_nav()
    footer_guides = build_footer_guides()
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
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
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
      <a class="brand" href="/">{LOGO_SVG}<span>{SITE_NAME}</span></a>
      <nav class="top-nav">{nav_html}<a class="nav-cta" href="/templates">Free Templates</a></nav>
    </header>
    <main>
{body}
    </main>
  </div>
  <footer class="site-footer">
    <div class="site-shell footer-grid">
      <div class="footer-col footer-brand">
        <a class="brand" href="/">{LOGO_SVG}<span>{SITE_NAME}</span></a>
        <p>Free, copy-ready resume examples and templates for entry-level machine learning, software, and data roles.</p>
        <p class="footer-fine">Some links are affiliate links: we may earn a commission at no extra cost to you.</p>
      </div>
      <nav class="footer-col" aria-label="Popular guides">
        <h2>Popular guides</h2>
        {footer_guides}
      </nav>
      <nav class="footer-col" aria-label="Site and legal">
        <h2>Site &amp; legal</h2>
        <a href="/status">Status</a>
        {footer_nav}
      </nav>
      <div class="footer-col">
        <h2>Contact</h2>
        <a href="mailto:Puxin9666@gmail.com">Puxin9666@gmail.com</a>
        <a href="/contact">Contact page</a>
        <p class="footer-fine">We read every message and usually reply within a few days.</p>
      </div>
    </div>
    <div class="site-shell footer-bottom">
      <p>&copy; {_today.year} {SITE_NAME}. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
'''


CATEGORY_ORDER = ['Resume Basics', 'Machine Learning', 'Software', 'Data']


def guide_card(page: dict) -> str:
    return f'''<article class="card">
<p class="card-tag">{html.escape(page.get('category', 'Guide'))}</p>
<h2><a href="/pages/{page['slug']}">{html.escape(page['title'])}</a></h2>
<p>{html.escape(page['summary'])}</p>
<p class="card-meta">{html.escape(AUTHOR['name'])} &middot; Updated {UPDATED_LABEL}</p>
</article>'''


def build_home(nav_html: str) -> None:
    sections = []
    for category in CATEGORY_ORDER:
        cards = ''.join(guide_card(p) for p in PAGES if p.get('category') == category)
        if not cards:
            continue
        sections.append(
            f'<section class="guide-category">\n'
            f'  <h2>{html.escape(category)}</h2>\n'
            f'  <div class="grid">{cards}</div>\n'
            f'</section>'
        )
    body = f'''
<section class="hero">
  <p class="eyebrow">Free resume examples & templates</p>
  <h1>Entry-Level Resume Guides That Get Interviews</h1>
  <p class="lead">Copy-ready resume examples and step-by-step guides that turn projects and coursework into interview-worthy proof for machine learning, software, and data roles.</p>
  <div class="hero-actions">
    <a class="btn-primary" href="#guides">Browse all guides</a>
    <div class="hero-chips">
      <span class="chip">{len(PAGES)} in-depth guides</span>
      <span class="chip">3 free Word templates</span>
      <span class="chip">No sign-up, ever</span>
    </div>
  </div>
</section>
<div id="guides">
{''.join(sections)}
</div>
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
      <li>14 full resume guides (about 22,100 words of copy-ready content)</li>
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


TEMPLATES = [
    {
        'file': 'entry-level-ml-engineer-resume-template.docx',
        'name': 'Entry-Level Machine Learning Engineer Resume Template',
        'desc': 'Single-column, ATS-safe Word template with a projects-first structure. Matches every example in our ML engineer resume guides.',
    },
    {
        'file': 'software-engineer-resume-no-experience-template.docx',
        'name': 'Software Engineer Resume Template (No Experience)',
        'desc': 'Built for candidates with projects and coursework instead of job history. Works for software, data analyst, and first-resume situations.',
    },
    {
        'file': 'entry-level-data-science-resume-template.docx',
        'name': 'Entry-Level Data Science Resume Template',
        'desc': 'Skills-grouped layout tuned for data roles, with room for SQL, visualization, and statistics projects.',
    },
]


def build_templates(nav_html: str) -> None:
    cards = []
    for t in TEMPLATES:
        cards.append(f'''<article class="card template-card">
<h2>{html.escape(t['name'])}</h2>
<p>{html.escape(t['desc'])}</p>
<a class="download-box-btn" href="/downloads/{t['file']}" download>Download .docx</a>
</article>''')
    body = f'''
<section class="page-head">
  <p class="eyebrow">Free downloads</p>
  <h1>Free Resume Templates for Entry-Level Tech Roles</h1>
  <p class="lead">Three ATS-safe Word templates that match the examples in our guides. Download, replace the placeholder text with your own projects, and keep the formatting exactly as it is.</p>
</section>
<section class="grid">{''.join(cards)}</section>
<section class="value-prop">
  <h2>How to use these templates</h2>
  <ul>
    <li><strong>Keep the layout.</strong> Single column, standard headings, no tables or text boxes &mdash; that is what keeps them ATS-safe.</li>
    <li><strong>Fill every placeholder with proof.</strong> Each guide on this site shows what to write, section by section.</li>
    <li><strong>Export as PDF before applying.</strong> Unless the job posting asks for a Word file, PDF keeps your formatting intact.</li>
  </ul>
</section>
'''
    (SITE_DIR / 'templates.html').write_text(
        shell(
            f'Free Resume Templates (Word) | {SITE_NAME}',
            'Download three free, ATS-safe Word resume templates for entry-level machine learning, software, and data roles. No sign-up required.',
            f'{BASE_URL}/templates',
            nav_html,
            body,
        ),
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
    idx = article.find('<h2 id="faq">FAQ</h2>')
    if idx == -1:
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


def extract_summary(markdown: str, max_words: int = 100) -> str:
    """Paragraph text of a guide's first section, capped at max_words."""
    in_first_section = False
    buf: list[str] = []
    words = 0
    for raw in markdown.splitlines():
        stripped = raw.strip()
        if stripped.startswith('# '):
            continue
        if stripped.startswith('## '):
            if in_first_section:
                break
            in_first_section = True
            continue
        if not stripped:
            continue
        if stripped.startswith('### ') or stripped.startswith('> ') or re.match(r'^(-|\d+\.)\s+', stripped):
            continue
        buf.append(stripped)
        words += len(stripped.split())
        if words >= max_words:
            break
    text_words = ' '.join(buf).split()
    if len(text_words) > max_words:
        return ' '.join(text_words[:max_words]).rstrip(',;:') + '…'
    return ' '.join(text_words)


def summary_box(markdown: str, page: dict) -> str:
    text = extract_summary(markdown)
    if len(text.split()) < 8:
        text = page['summary']
    return f'''
<aside class="summary-box">
  <strong>Quick summary</strong>
  <p>{inline_format(text)}</p>
</aside>'''


def extract_takeaways(markdown: str, limit: int = 6) -> list[str]:
    """First sentence of the opening paragraph of each H2 section (FAQ excluded)."""
    takeaways: list[str] = []
    lines = markdown.splitlines()
    i = 0
    while i < len(lines) and len(takeaways) < limit:
        stripped = lines[i].strip()
        i += 1
        if not stripped.startswith('## '):
            continue
        if stripped == '## FAQ':
            break
        buf: list[str] = []
        first_bullet = ''
        for s in (l.strip() for l in lines[i:]):
            if not s:
                if buf or first_bullet:
                    break
                continue
            if s.startswith('#') or s.startswith('> '):
                break
            m = re.match(r'^(?:-|\d+\.)\s+(.*)', s)
            if m:
                if not first_bullet:
                    first_bullet = m.group(1).strip()
                if buf:
                    break
                continue
            if first_bullet:
                break
            buf.append(s)
        sentence = ''
        if buf:
            candidate = re.split(r'(?<=[.!?])\s+', ' '.join(buf))[0].strip()
            if (
                candidate and not candidate.endswith(':')
                and '@' not in candidate and '|' not in candidate
                and len(candidate.split()) >= 5
            ):
                sentence = candidate
        if not sentence and first_bullet:
            if (
                not first_bullet.endswith(':') and '[' not in first_bullet
                and len(first_bullet.split()) >= 5
            ):
                sentence = first_bullet
        if not sentence:
            continue
        if len(sentence) > 160:
            sentence = sentence[:157].rsplit(' ', 1)[0].rstrip(',;:') + '…'
        takeaways.append(sentence)
    return takeaways


def takeaways_box(markdown: str) -> str:
    items = extract_takeaways(markdown)
    if len(items) < 3:
        return ''
    lis = ''.join(f'<li>{inline_format(t)}</li>' for t in items)
    return f'''
<aside class="takeaways-box">
  <h2>Key takeaways</h2>
  <ul>{lis}</ul>
</aside>'''


def author_box() -> str:
    initials = ''.join(part[0] for part in AUTHOR['name'].split())
    return f'''
<aside class="author-box">
  <div class="author-avatar" aria-hidden="true">{html.escape(initials)}</div>
  <div class="author-text">
    <strong>About the author</strong>
    <p>{html.escape(AUTHOR['bio'])} <a href="/about#about-the-author">More about {html.escape(AUTHOR['name'])}</a></p>
  </div>
</aside>'''


TOC_SCRIPT = '''<script>
(function () {
  var toc = document.querySelector('.toc-desktop');
  if (!toc || !('IntersectionObserver' in window)) { return; }
  var links = {};
  toc.querySelectorAll('a[href^="#"]').forEach(function (a) {
    links[a.getAttribute('href').slice(1)] = a;
  });
  var current = null;
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting && links[entry.target.id]) {
        if (current) { current.classList.remove('active'); }
        current = links[entry.target.id];
        current.classList.add('active');
      }
    });
  }, { rootMargin: '-90px 0px -70% 0px' });
  document.querySelectorAll('.prose h2[id]').forEach(function (h) { observer.observe(h); });
})();
</script>'''


def build_page(page: dict, nav_html: str) -> None:
    markdown = strip_frontmatter((PAGES_DIR / f"{page['slug']}.md").read_text(encoding='utf-8'))
    article = markdown_to_html(markdown)
    h2_positions = [m.start() for m in re.finditer(r'<h2 id="', article)]
    if len(h2_positions) >= 2:
        at = h2_positions[1]
        article = article[:at] + download_box(page) + '\n' + article[at:]
    article = insert_before_faq(article, takeaways_box(markdown) + '\n' + affiliate_cta())
    canonical = f"{BASE_URL}/pages/{page['slug']}"
    faqs = extract_faq(markdown)
    minutes = max(4, round(len(markdown.split()) / 200))
    toc = extract_toc(markdown)
    toc_items = ''.join(f'<li><a href="#{anchor}">{html.escape(text)}</a></li>' for anchor, text in toc)
    toc_desktop = ''
    toc_mobile = ''
    if len(toc) >= 4:
        toc_desktop = f'''
<aside class="toc-sidebar">
  <nav class="toc toc-desktop" aria-label="Table of contents">
    <h2>In this guide</h2>
    <ol>{toc_items}</ol>
  </nav>
</aside>'''
        toc_mobile = f'''
<details class="toc toc-mobile">
  <summary>In this guide</summary>
  <ol>{toc_items}</ol>
</details>'''
    body = f'''
<section class="page-head">
  <p class="eyebrow">{html.escape(page.get('category', 'Guide'))} &middot; Free guide + copy-ready template</p>
  <h1>{html.escape(page['title'])}</h1>
  <p class="lead">{html.escape(page['summary'])}</p>
  <p class="byline">By <a href="/about#about-the-author">{html.escape(AUTHOR['name'])}</a>, {html.escape(AUTHOR['title'])} &middot; Last updated {UPDATED_LABEL} &middot; {minutes} min read</p>
</section>
<div class="article-layout">
  {toc_desktop}
  <div class="article-main">
    {summary_box(markdown, page)}
    {toc_mobile}
    <article class="prose">
{article}
    </article>
    {author_box()}
    {download_box(page)}
  </div>
</div>
{related_box(page['slug'])}
{TOC_SCRIPT if toc_desktop else ''}
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


def build_favicon() -> None:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 30 30">'
        '<rect width="30" height="30" rx="8" fill="#1d4ed8"/>'
        '<path d="M9 8h8.5a3.5 3.5 0 0 1 0 7H9V8zm0 7h9l3 7h-4l-3-7h-5v7H9v-7z" fill="#fff"/>'
        '</svg>'
    )
    (SITE_DIR / 'favicon.svg').write_text(svg, encoding='utf-8')


def build_404(nav_html: str) -> None:
    body = f'''
<section class="hero compact not-found">
  <p class="eyebrow">404</p>
  <h1>This page does not exist</h1>
  <p class="lead">The link may be old or mistyped. Head back to the homepage to browse all free resume guides and templates.</p>
  <div class="hero-actions">
    <a class="btn-primary" href="/">Back to homepage</a>
  </div>
</section>
'''
    (SITE_DIR / '404.html').write_text(
        shell(f'Page Not Found | {SITE_NAME}', 'The page you are looking for does not exist.', f'{BASE_URL}/404', nav_html, body),
        encoding='utf-8',
    )


def build_seo_files() -> None:
    urls = [(f'{BASE_URL}/', TODAY), (f'{BASE_URL}/status', TODAY), (f'{BASE_URL}/templates', TODAY)]
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
  --bg: #ffffff;
  --panel: #ffffff;
  --ink: #1b2a3a;
  --muted: #5b6b7c;
  --line: #e2e8f0;
  --accent: #1d4ed8;
  --accent-strong: #173da6;
  --accent-soft: #eef3fd;
  --summary-bg: #f4f6f9;
  --footer-bg: #10233f;
  --footer-ink: #c3d2e8;
  --footer-muted: #8ba1bd;
  --shadow: 0 1px 2px rgba(27, 42, 58, 0.05), 0 8px 24px rgba(27, 42, 58, 0.06);
  --radius: 16px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.site-shell { max-width: 1120px; margin: 0 auto; padding: 0 24px; }

/* Header */
.site-header {
  position: sticky; top: 0; z-index: 20;
  display: flex; justify-content: space-between; gap: 20px; align-items: center;
  padding: 12px 24px; margin: 0 -24px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}
.brand {
  display: inline-flex; align-items: center; gap: 10px;
  font-size: 1.08rem; font-weight: 800; letter-spacing: -0.01em; color: var(--ink);
  white-space: nowrap;
}
.brand:hover { text-decoration: none; }
.logo-mark { display: block; border-radius: 8px; }
.top-nav { display: flex; flex-wrap: wrap; align-items: center; gap: 4px; font-size: .94rem; }
.top-nav a {
  color: var(--ink); padding: 7px 12px; border-radius: 10px; font-weight: 500;
}
.top-nav a:hover { background: var(--accent-soft); color: var(--accent-strong); text-decoration: none; }
.top-nav a.nav-cta {
  margin-left: 8px; padding: 10px 18px; background: var(--accent); color: #fff;
  font-weight: 700; border-radius: 10px; min-height: 40px;
  display: inline-flex; align-items: center;
}
.top-nav a.nav-cta:hover { background: var(--accent-strong); color: #fff; }

/* Hero & page heads */
.hero, .page-head {
  padding: 56px 44px; margin: 32px 0; background: var(--panel); border: 1px solid var(--line);
  border-radius: 24px; box-shadow: var(--shadow);
}
.hero { border-top: 4px solid var(--accent); }
.hero.compact { padding: 36px 44px; }
.hero h1, .page-head h1 {
  font-size: clamp(1.9rem, 4vw, 2.7rem); line-height: 1.15;
  letter-spacing: -0.02em; margin: 10px 0 16px;
}
.eyebrow {
  text-transform: uppercase; letter-spacing: .14em; font-size: .76rem;
  font-weight: 700; color: var(--accent); margin: 0;
}
.lead { font-size: 1.15rem; color: #3a4a5c; max-width: 720px; margin: 0; }
.byline { margin: 18px 0 0; font-size: .92rem; color: var(--muted); }
.byline a { color: var(--ink); font-weight: 600; }
.byline a:hover { color: var(--accent); }
.hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 18px; margin-top: 28px; }
.btn-primary {
  display: inline-flex; align-items: center; min-height: 48px; padding: 12px 26px;
  background: var(--accent); color: #fff; border-radius: 12px; font-weight: 700; font-size: 1rem;
  transition: background .15s ease, transform .15s ease;
}
.btn-primary:hover { background: var(--accent-strong); text-decoration: none; transform: translateY(-1px); }
.hero-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip {
  padding: 6px 14px; border: 1px solid var(--line); border-radius: 999px;
  background: var(--panel); font-size: .85rem; color: var(--muted); font-weight: 500;
}

/* Cards */
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 18px; }
.grid.single { grid-template-columns: 1fr; }
.card {
  background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius);
  padding: 24px; box-shadow: var(--shadow);
  transition: transform .15s ease, border-color .15s ease;
}
.card:hover { transform: translateY(-2px); border-color: var(--accent); }
.card h2, .card h3 { margin-top: 0; font-size: 1.12rem; line-height: 1.35; letter-spacing: -0.01em; }
.card h2 a, .card h3 a { color: var(--ink); }
.card h2 a:hover, .card h3 a:hover { color: var(--accent); text-decoration: none; }
.card p { margin-bottom: 0; color: var(--muted); font-size: .96rem; }
.card-tag {
  display: inline-block; margin: 0 0 12px; padding: 3px 12px; border-radius: 999px;
  background: var(--accent-soft); color: var(--accent-strong);
  font-size: .74rem; font-weight: 700; text-transform: uppercase; letter-spacing: .07em;
}
.card-meta { margin: 14px 0 0 !important; font-size: .84rem !important; color: var(--muted) !important; }
.template-card .download-box-btn { margin-top: 16px; }
.guide-category { margin: 40px 0; }
.guide-category > h2 {
  display: inline-block; margin: 0 0 16px; padding-bottom: 8px;
  font-size: 1.45rem; letter-spacing: -0.015em; border-bottom: 3px solid var(--accent);
}

/* Article layout: sticky TOC sidebar + narrow prose column */
.article-layout {
  display: grid; grid-template-columns: 240px minmax(0, 1fr);
  gap: 40px; align-items: start; margin: 0 0 8px;
}
.article-main { max-width: 740px; min-width: 0; }
.toc-sidebar { position: sticky; top: 92px; }
.toc-desktop {
  padding: 20px 22px; background: var(--panel);
  border: 1px solid var(--line); border-radius: var(--radius);
}
.toc-desktop h2 {
  margin: 0 0 10px; font-size: .8rem; text-transform: uppercase;
  letter-spacing: .08em; color: var(--muted);
}
.toc-desktop ol { margin: 0; padding-left: 1.2rem; }
.toc-desktop li { margin: 7px 0; font-size: .9rem; line-height: 1.45; }
.toc-desktop a { color: var(--muted); }
.toc-desktop a:hover { color: var(--accent); text-decoration: none; }
.toc-desktop a.active { color: var(--accent-strong); font-weight: 700; }
.toc-mobile { display: none; }

/* Summary & takeaways boxes */
.summary-box {
  margin: 0 0 28px; padding: 20px 24px; background: var(--summary-bg);
  border: 1px solid var(--line); border-radius: var(--radius);
}
.summary-box > strong {
  display: block; margin-bottom: 6px; font-size: .8rem; text-transform: uppercase;
  letter-spacing: .08em; color: var(--muted);
}
.summary-box p { margin: 0; font-size: 1rem; color: #33404e; }
.takeaways-box {
  margin: 2.4rem 0; padding: 24px 28px; background: var(--summary-bg);
  border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: var(--radius);
}
.takeaways-box h2 { margin: 0 0 10px !important; font-size: 1.2rem; }
.takeaways-box ul { margin: 0; padding-left: 1.3rem; }
.takeaways-box li { margin: 6px 0; font-size: 1rem; }

/* Author box */
.author-box {
  display: flex; gap: 18px; align-items: flex-start; margin: 28px 0;
  padding: 22px 26px; background: var(--panel); border: 1px solid var(--line);
  border-radius: var(--radius);
}
.author-avatar {
  flex: 0 0 auto; width: 52px; height: 52px; border-radius: 50%;
  background: var(--accent); color: #fff; display: flex; align-items: center;
  justify-content: center; font-weight: 800; font-size: 1.05rem;
}
.author-text > strong {
  font-size: .8rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted);
}
.author-text p { margin: 6px 0 0; font-size: .95rem; color: #33404e; }

/* Article prose */
.prose {
  background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
  padding: 40px 44px; box-shadow: var(--shadow);
}
.prose h1:first-child { display: none; }
.prose h2 { margin-top: 2.4rem; font-size: 1.5rem; letter-spacing: -0.015em; scroll-margin-top: 90px; }
.prose h2:first-of-type { margin-top: 0; }
.prose h3 { margin-top: 1.5rem; font-size: 1.14rem; scroll-margin-top: 90px; }
.prose p, .prose li, .prose blockquote { font-size: 1.125rem; color: #2a3644; }
.prose p { margin: 1.1em 0; }
.prose ul, .prose ol { padding-left: 1.4rem; }
.prose li { margin: 6px 0; }
.prose blockquote {
  margin: 1.2rem 0; padding: 1rem 1.3rem; background: var(--accent-soft);
  border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0;
}
code {
  background: #eef1f6; padding: .12rem .42rem; border-radius: 6px; font-size: .9em;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

/* CTA & download boxes */
.cta-box {
  margin: 2.4rem 0; padding: 26px 28px; background: var(--accent-soft);
  border: 1px solid var(--accent); border-radius: var(--radius);
}
.cta-box h3 { margin-top: 0; color: var(--accent-strong); }
.cta-button {
  display: inline-flex; align-items: center; min-height: 48px; margin: .6rem 0; padding: 12px 22px;
  background: var(--accent); color: #fff; border-radius: 12px; font-weight: 700;
  transition: background .15s ease;
}
.cta-button:hover { background: var(--accent-strong); text-decoration: none; }
.cta-alt { font-size: .9rem; color: var(--muted); margin-bottom: 0; }
.download-box {
  display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;
  margin: 2rem 0; padding: 18px 24px; background: var(--accent-soft);
  border: 1px solid #c8d8f8; border-radius: var(--radius);
}
.article-main > .download-box:last-child { margin-bottom: 0; }
.download-box-text { display: flex; flex-direction: column; gap: 2px; }
.download-box-text strong { font-size: 1.02rem; }
.download-box-text span { font-size: .88rem; color: var(--muted); }
.download-box-btn {
  display: inline-flex; align-items: center; justify-content: center; min-height: 48px;
  padding: 10px 20px; border: 1.5px solid var(--accent);
  color: var(--accent-strong); border-radius: 12px; font-weight: 700; white-space: nowrap;
  transition: background .15s ease;
}
.download-box-btn:hover { background: #fff; text-decoration: none; }

/* Misc sections */
.value-prop { margin: 28px 0; padding: 32px; background: var(--panel); border: 1px solid var(--line); border-radius: 24px; box-shadow: var(--shadow); }
.value-prop h2 { margin-top: 0; }
.value-prop li { margin: 6px 0; }
.related { margin: 28px 0 32px; }
.related h2 { font-size: 1.35rem; letter-spacing: -0.01em; }
.not-found { text-align: center; }

/* Footer */
.site-footer { background: var(--footer-bg); color: var(--footer-ink); margin-top: 48px; }
.footer-grid {
  display: grid; grid-template-columns: 1.7fr 1fr 1fr 1fr; gap: 36px;
  padding-top: 44px; padding-bottom: 32px;
}
.footer-brand .brand { color: #fff; }
.footer-brand p { font-size: .92rem; margin: 14px 0 0; max-width: 320px; }
.footer-fine { color: var(--footer-muted); font-size: .82rem !important; }
.footer-col h2 {
  font-size: .82rem; text-transform: uppercase; letter-spacing: .1em;
  color: var(--footer-muted); margin: 6px 0 14px;
}
.footer-col a { display: block; color: var(--footer-ink); padding: 4px 0; font-size: .95rem; word-break: break-word; }
.footer-col a:hover { color: #fff; text-decoration: none; }
.footer-col p.footer-fine { margin: 10px 0 0; }
.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding-top: 18px; padding-bottom: 22px; font-size: .85rem; color: var(--footer-muted);
}
.footer-bottom p { margin: 0; }

/* Responsive */
@media (max-width: 900px) {
  .article-layout { grid-template-columns: 1fr; }
  .article-main { width: 100%; margin: 0 auto; }
  .toc-desktop, .toc-sidebar { display: none; }
  .toc-mobile {
    display: block; margin: 0 0 28px; padding: 16px 20px; background: var(--panel);
    border: 1px solid var(--line); border-radius: var(--radius);
  }
  .toc-mobile summary { cursor: pointer; font-weight: 700; font-size: 1rem; }
  .toc-mobile ol { margin: 12px 0 2px; padding-left: 1.3rem; }
  .toc-mobile li { margin: 6px 0; font-size: .98rem; }
}
@media (max-width: 860px) {
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 26px; }
}
@media (max-width: 768px) {
  body { font-size: 16px; }
  .site-header { position: static; flex-direction: column; align-items: flex-start; gap: 10px; }
  .top-nav { width: 100%; flex-wrap: nowrap; overflow-x: auto; padding-bottom: 4px; -webkit-overflow-scrolling: touch; }
  .top-nav a { white-space: nowrap; }
  .top-nav a.nav-cta { margin-left: 0; min-height: 48px; }
  .hero, .page-head { padding: 28px 20px; margin: 20px 0; }
  .hero h1, .page-head h1 { font-size: 1.7rem; }
  .lead { font-size: 1.05rem; }
  .prose { padding: 24px 18px; }
  .prose p, .prose li, .prose blockquote { font-size: 1rem; }
  .grid { grid-template-columns: 1fr; }
  .download-box { flex-direction: column; align-items: stretch; }
  .download-box-btn { width: 100%; }
  .author-box { padding: 18px 20px; }
  .summary-box, .takeaways-box { padding: 18px 20px; }
  .footer-grid { grid-template-columns: 1fr; }
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
    build_templates(nav_html)
    for page in PAGES:
        build_page(page, nav_html)
    for page in LEGAL_PAGES:
        build_legal(page, nav_html)
    build_favicon()
    build_404(nav_html)
    build_seo_files()


if __name__ == '__main__':
    main()

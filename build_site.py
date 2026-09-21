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
            'python-projects-for-resume',
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
            'data-science-internship-resume',
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
            'python-projects-for-resume',
            'kaggle-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
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
            'resume-skills-section-tech',
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
            'python-projects-for-resume',
            'entry-level-machine-learning-engineer-resume',
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
            'data-science-internship-resume',
            'python-projects-for-resume',
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
        'slug': 'resume-skills-section-tech',
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
        'slug': 'data-science-cover-letter-entry-level',
        'title': 'Data Science Cover Letter Entry Level: Example & Templates',
        'keyword': 'data science cover letter entry level',
        'description': 'Entry-level data science cover letter example with the 4-paragraph structure, copy-ready paragraph templates, and the mistakes that get letters ignored.',
        'summary': 'A complete entry-level data science cover letter example, the 4-paragraph structure behind it, and copy-ready templates for every paragraph.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'machine-learning-engineer-cover-letter',
            'data-science-internship-resume',
            'entry-level-data-science-resume',
            'python-projects-for-resume',
        ],
    },
    {
        'slug': 'data-science-internship-resume',
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
    {
        'slug': 'editorial-policy',
        'title': 'Editorial Policy',
        'nav': 'Editorial Policy',
        'description': 'How Resume Path Lab creates, reviews, and updates its resume guides, and our independence commitments.',
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
        },
        {
            '@context': 'https://schema.org',
            '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{BASE_URL}/'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': f'{BASE_URL}/#guides'},
                {'@type': 'ListItem', 'position': 3, 'name': page['title'], 'item': canonical},
            ],
        },
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
    '<rect width="30" height="30" rx="8" fill="#0f766e"/>'
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
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
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
      <nav class="top-nav">{nav_html}</nav>
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
      <nav class="footer-col" aria-label="Site information">
        <h2>Site</h2>
        <a href="/status">Status</a>
        {footer_nav}
      </nav>
    </div>
    <div class="site-shell footer-bottom">
      <p>&copy; 2026 {SITE_NAME}. All rights reserved.</p>
    </div>
  </footer>
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
  <div class="hero-actions">
    <a class="btn-primary" href="#guides">Browse all guides</a>
    <div class="hero-chips">
      <span class="chip">{len(PAGES)} in-depth guides</span>
      <span class="chip">3 free Word templates</span>
      <span class="chip">No sign-up, ever</span>
    </div>
  </div>
</section>
<section id="guides">
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
      <li>15 full resume guides (about 23,700 words of copy-ready content)</li>
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


def build_page(page: dict, nav_html: str) -> None:
    markdown = (PAGES_DIR / f"{page['slug']}.md").read_text(encoding='utf-8')
    article = markdown_to_html(markdown)
    cta = affiliate_cta()
    article = insert_before_faq(article, cta)
    canonical = f"{BASE_URL}/pages/{page['slug']}"
    faqs = extract_faq(markdown)
    minutes = max(4, round(len(markdown.split()) / 200))
    toc = extract_toc(markdown)
    toc_html = ''
    if len(toc) >= 4:
        toc_items = ''.join(f'<li><a href="#{anchor}">{html.escape(text)}</a></li>' for anchor, text in toc)
        toc_html = f'''
<nav class="toc" aria-label="Table of contents">
  <h2>In this guide</h2>
  <ol>{toc_items}</ol>
</nav>'''
    body = f'''
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="crumb-sep">/</span><a href="/#guides">Guides</a><span class="crumb-sep">/</span><span class="crumb-current">{html.escape(page.get('nav', page['title']))}</span></nav>
<section class="page-head">
  <p class="eyebrow">Free guide + copy-ready template</p>
  <h1>{html.escape(page['title'])}</h1>
  <p class="lead">{html.escape(page['summary'])}</p>
  <p class="byline">By the {SITE_NAME} Editorial Team &middot; Updated {TODAY} &middot; {minutes} min read</p>
</section>
{download_box(page)}
{toc_html}
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


def build_favicon() -> None:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 30 30">'
        '<rect width="30" height="30" rx="8" fill="#0f766e"/>'
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
  --bg: #f7f7f4;
  --panel: #ffffff;
  --ink: #16191d;
  --muted: #5c666d;
  --line: #e5e3de;
  --accent: #0f766e;
  --accent-strong: #0b5a54;
  --accent-soft: #e8f4f2;
  --footer-bg: #12211f;
  --footer-ink: #c8d4d1;
  --shadow: 0 1px 2px rgba(22, 25, 29, 0.05), 0 8px 24px rgba(22, 25, 29, 0.06);
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
.site-shell { max-width: 1080px; margin: 0 auto; padding: 0 24px; }

/* Header */
.site-header {
  position: sticky; top: 0; z-index: 20;
  display: flex; justify-content: space-between; gap: 20px; align-items: center;
  padding: 14px 24px; margin: 0 -24px;
  background: rgba(247, 247, 244, 0.85);
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
.top-nav { display: flex; flex-wrap: wrap; gap: 4px; font-size: .94rem; }
.top-nav a {
  color: var(--ink); padding: 7px 12px; border-radius: 10px; font-weight: 500;
}
.top-nav a:hover { background: var(--accent-soft); color: var(--accent-strong); text-decoration: none; }

/* Hero & page heads */
.hero, .page-head {
  padding: 56px 44px; margin: 32px 0; background: var(--panel); border: 1px solid var(--line);
  border-radius: 24px; box-shadow: var(--shadow);
}
.hero { background: linear-gradient(135deg, #ffffff 0%, var(--accent-soft) 130%); }
.hero.compact { padding: 36px 44px; }
.hero h1, .page-head h1 {
  font-size: clamp(1.9rem, 4vw, 2.7rem); line-height: 1.15;
  letter-spacing: -0.02em; margin: 10px 0 16px;
}
.eyebrow {
  text-transform: uppercase; letter-spacing: .14em; font-size: .76rem;
  font-weight: 700; color: var(--accent); margin: 0;
}
.lead { font-size: 1.15rem; color: #39424a; max-width: 720px; margin: 0; }
.byline { margin: 18px 0 0; font-size: .9rem; color: var(--muted); }
.crumbs { margin: 26px 0 -14px; font-size: .88rem; color: var(--muted); }
.crumbs a { color: var(--muted); }
.crumbs a:hover { color: var(--accent); }
.crumb-sep { margin: 0 8px; color: var(--line); }
.crumb-current { color: var(--ink); font-weight: 500; }
.hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 18px; margin-top: 28px; }
.btn-primary {
  display: inline-block; padding: 13px 26px; background: var(--accent); color: #fff;
  border-radius: 12px; font-weight: 700; font-size: 1rem;
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

/* Table of contents */
.toc {
  margin: 0 0 28px; padding: 24px 30px; background: var(--panel);
  border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow);
}
.toc h2 { margin: 0 0 10px; font-size: 1rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
.toc ol { margin: 0; padding-left: 1.3rem; columns: 2; column-gap: 40px; }
.toc li { margin: 4px 0; font-size: .96rem; break-inside: avoid; }
.toc a { color: var(--ink); }
.toc a:hover { color: var(--accent); }

/* Article prose */
.prose {
  background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
  padding: 40px 44px; box-shadow: var(--shadow);
}
.prose h1:first-child { display: none; }
.prose h2 { margin-top: 2.4rem; font-size: 1.5rem; letter-spacing: -0.015em; scroll-margin-top: 90px; }
.prose h2:first-of-type { margin-top: 0; }
.prose h3 { margin-top: 1.5rem; font-size: 1.14rem; }
.prose p, .prose li, .prose blockquote { font-size: 1.03rem; color: #2a3138; }
.prose ul, .prose ol { padding-left: 1.4rem; }
.prose li { margin: 5px 0; }
.prose blockquote {
  margin: 1.1rem 0; padding: 1rem 1.3rem; background: var(--accent-soft);
  border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0;
}
code {
  background: #f0eeea; padding: .12rem .42rem; border-radius: 6px; font-size: .9em;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

/* CTA & download boxes */
.cta-box {
  margin: 2.4rem 0; padding: 26px 28px; background: var(--accent-soft);
  border: 1px solid var(--accent); border-radius: var(--radius);
}
.cta-box h3 { margin-top: 0; color: var(--accent-strong); }
.cta-button {
  display: inline-block; margin: .6rem 0; padding: 12px 22px;
  background: var(--accent); color: #fff; border-radius: 12px; font-weight: 700;
  transition: background .15s ease;
}
.cta-button:hover { background: var(--accent-strong); text-decoration: none; }
.cta-alt { font-size: .9rem; color: var(--muted); margin-bottom: 0; }
.download-box {
  display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;
  margin: 0 0 28px; padding: 18px 24px; background: var(--panel);
  border: 1px dashed var(--accent); border-radius: var(--radius);
}
.download-box-text { display: flex; flex-direction: column; gap: 2px; }
.download-box-text strong { font-size: 1.02rem; }
.download-box-text span { font-size: .88rem; color: var(--muted); }
.download-box-btn {
  display: inline-block; padding: 10px 20px; border: 1.5px solid var(--accent);
  color: var(--accent-strong); border-radius: 12px; font-weight: 700; white-space: nowrap;
  transition: background .15s ease;
}
.download-box-btn:hover { background: var(--accent-soft); text-decoration: none; }

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
  display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px;
  padding-top: 44px; padding-bottom: 32px;
}
.footer-brand .brand { color: #fff; }
.footer-brand p { font-size: .92rem; margin: 14px 0 0; max-width: 340px; }
.footer-fine { color: #8fa39e; font-size: .82rem !important; }
.footer-col h2 {
  font-size: .82rem; text-transform: uppercase; letter-spacing: .1em;
  color: #8fa39e; margin: 6px 0 14px;
}
.footer-col a { display: block; color: var(--footer-ink); padding: 4px 0; font-size: .95rem; }
.footer-col a:hover { color: #fff; text-decoration: none; }
.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding-top: 18px; padding-bottom: 22px; font-size: .85rem; color: #8fa39e;
}
.footer-bottom p { margin: 0; }

@media (max-width: 860px) {
  .footer-grid { grid-template-columns: 1fr; gap: 26px; }
  .toc ol { columns: 1; }
}
@media (max-width: 720px) {
  .site-header { position: static; flex-direction: column; align-items: flex-start; }
  .hero, .page-head { padding: 30px 24px; }
  .prose { padding: 26px 22px; }
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
    build_favicon()
    build_404(nav_html)
    build_seo_files()


if __name__ == '__main__':
    main()

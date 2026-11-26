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
CONTENT_REVIEW_DATE = '2026-11-27'

AUTHOR = {
    'name': 'Jordan Blake',
    'title': 'Editorial pen name, Resume Path Lab',
    'bio': (
        'Jordan Blake is the editorial pen name used for Resume Path Lab guides. '
        'Articles combine AI-assisted drafting with structured editorial review, practical '
        'examples, and copy-ready templates. Examples are illustrative, and guidance focuses '
        'on evidence candidates can verify in their own work.'
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
        'title': 'Entry-Level Machine Learning Engineer Resume Example',
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
        'title': 'Machine Learning Resume Summary: 8 Examples',
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
        'title': 'Kaggle Projects for a Resume: What Counts',
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
        'title': 'How to Write a Resume With No Work Experience: Guide',
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
        'title': 'Machine Learning Engineer Cover Letter: Entry-Level Example',
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
        'category': 'Data',
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
        'category': 'Data',
        'title': 'Data Science Internship Resume: Example & Guide',
        'keyword': 'data science internship resume',
        'description': 'Data science internship resume example and guide: frame coursework, projects, and analysis clearly, with copy-ready bullets and a final review checklist.',
        'summary': 'A data science internship resume example with coursework framing, project rewrites, and practical checks for different internship tracks.',
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
    {
        'slug': 'internship-resume-computer-science',
        'published': CONTENT_REVIEW_DATE,
        'category': 'Software',
        'title': 'Computer Science Internship Resume: Example & Project Guide',
        'keyword': 'computer science internship resume',
        'description': 'Computer science internship resume example and guide: present coursework, coding projects, tutoring, and skills without formal work experience.',
        'summary': 'A complete CS internship resume example with project rewrites, section ordering, and ways to show coursework and tutoring as evidence.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'software-engineer-resume-no-experience',
            'entry-level-software-developer-portfolio',
            'data-science-internship-resume',
            'how-to-list-projects-on-resume',
        ],
    },
    {
        'slug': 'entry-level-software-developer-portfolio',
        'published': CONTENT_REVIEW_DATE,
        'category': 'Software',
        'title': 'Entry-Level Developer Portfolio: Projects & Examples',
        'keyword': 'entry level software developer portfolio',
        'description': 'Entry-level software developer portfolio guide: choose projects, write useful READMEs, show validation, and connect your best work to resume bullets.',
        'summary': 'Build a small, credible developer portfolio with lead projects, useful READMEs, validation proof, and matching resume bullets.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'internship-resume-computer-science',
            'software-engineer-resume-no-experience',
            'how-to-list-projects-on-resume',
            'python-projects-for-resume',
        ],
    },
    {
        'slug': 'how-to-list-projects-on-resume',
        'published': CONTENT_REVIEW_DATE,
        'category': 'Resume Basics',
        'title': 'How to List Projects on a Resume: Bullets & Examples',
        'keyword': 'how to list projects on resume',
        'description': 'How to list projects on a resume: choose relevant work, order entries, write evidence-based bullets, handle team projects, and avoid invented metrics.',
        'summary': 'A practical projects section guide with complete examples, bullet templates, and honest ways to present team, tutorial, and personal work.',
        'template': 'software-engineer-resume-no-experience-template.docx',
        'related': [
            'entry-level-software-developer-portfolio',
            'machine-learning-projects-for-resume',
            'python-projects-for-resume',
            'resume-with-no-work-experience',
        ],
    },
    {
        'slug': 'entry-level-data-engineer-resume',
        'published': CONTENT_REVIEW_DATE,
        'category': 'Data',
        'title': 'Entry-Level Data Engineer Resume: Example & Projects',
        'keyword': 'entry level data engineer resume',
        'description': 'Entry-level data engineer resume example and project guide: show SQL, Python, pipelines, validation, and data quality without production-scale claims.',
        'summary': 'A complete data engineer resume example focused on pipelines, SQL modeling, validation, and reliable data workflows.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'sql-projects-for-resume',
            'entry-level-data-analyst-resume',
            'entry-level-data-science-resume',
            'ats-friendly-resume-guide',
        ],
    },
    {
        'slug': 'sql-projects-for-resume',
        'published': CONTENT_REVIEW_DATE,
        'category': 'Data',
        'title': 'SQL Projects for a Resume: 8 Ideas & Copy-Ready Bullets',
        'keyword': 'sql projects for resume',
        'description': 'SQL projects for a resume: eight practical ideas with schemas, validation checks, and copy-ready bullets for analyst and data engineering roles.',
        'summary': 'Eight SQL project ideas with clear schemas, data quality checks, and resume bullets for analysis and data engineering.',
        'template': 'entry-level-data-science-resume-template.docx',
        'related': [
            'entry-level-data-engineer-resume',
            'entry-level-data-analyst-resume',
            'python-projects-for-resume',
            'how-to-list-projects-on-resume',
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


def display_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f'{parsed:%b} {parsed.day}, {parsed:%Y}'


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
    links = [
        ('/#guides', 'All guides'),
        ('/pages/entry-level-machine-learning-engineer-resume', 'Machine learning'),
        ('/pages/software-engineer-resume-no-experience', 'Software'),
        ('/pages/entry-level-data-science-resume', 'Data'),
    ]
    return ''.join(f'<a href="{href}">{label}</a>' for href, label in links)


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
            'datePublished': page.get('published', '2026-04-05'),
            'dateModified': page.get('updated', CONTENT_REVIEW_DATE),
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
    '<svg class="logo-mark" width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">'
    '<path d="M5 4h17v26H5z" fill="#123f35"/>'
    '<path d="M22 4l7 7v19H12" fill="#dce9df"/>'
    '<path d="M10 11h7M10 16h12M10 21h8" stroke="#fff" stroke-width="2"/>'
    '<path d="M23 22l3 3 5-7" stroke="#c7472e" stroke-width="2.5" stroke-linecap="square"/>'
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
{extra_head}  <link rel="stylesheet" href="/styles.css?v=20261126-4">
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="/">{LOGO_SVG}<span>{SITE_NAME}</span></a>
      <nav class="top-nav" aria-label="Primary navigation">{nav_html}<a class="nav-cta" href="/templates">Free Templates</a></nav>
      <details class="nav-toggle">
        <summary>Menu</summary>
        <nav class="mobile-nav" aria-label="Mobile navigation">{nav_html}<a class="nav-cta" href="/templates">Free Templates</a></nav>
      </details>
    </header>
    <main id="main-content">
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
CATEGORY_DESCRIPTIONS = {
    'Resume Basics': 'Start with a clear structure, a parseable format, and skills you can defend.',
    'Machine Learning': 'Turn models, notebooks, and CS projects into evidence of practical ML work.',
    'Software': 'Show how you build, evaluate, and deliver software before your first full-time role.',
    'Data': 'Frame SQL, analysis, visualization, and statistics projects for your first data job.',
}


def guide_card(page: dict) -> str:
    markdown = (PAGES_DIR / f"{page['slug']}.md").read_text(encoding='utf-8')
    minutes = max(4, round(len(markdown.split()) / 200))
    return f'''<article class="guide-card">
<h3><a href="/pages/{page['slug']}">{html.escape(page['title'])}</a></h3>
<p>{html.escape(page['summary'])}</p>
<p class="card-meta">{minutes} min read &middot; Free template included</p>
</article>'''


def build_home(nav_html: str) -> None:
    sections = []
    for category in CATEGORY_ORDER:
        category_pages = [p for p in PAGES if p.get('category') == category]
        cards = ''.join(guide_card(p) for p in category_pages)
        if not cards:
            continue
        sections.append(
            f'<section class="guide-category">\n'
            f'  <div class="category-heading"><h2>{html.escape(category)}</h2>'
            f'<p>{html.escape(CATEGORY_DESCRIPTIONS[category])}</p>'
            f'<span class="guide-count">{len(category_pages)} {"guide" if len(category_pages) == 1 else "guides"}</span></div>\n'
            f'  <div class="guide-list">{cards}</div>\n'
            f'</section>'
        )
    body = f'''
<section class="hero home-hero">
  <div class="hero-copy">
    <h1>Your projects are the experience.</h1>
    <p class="lead">Free resume examples and step-by-step guides that turn projects and coursework into credible proof for machine learning, software, and data roles.</p>
    <div class="hero-actions">
      <a class="btn-primary" href="#guides">Explore the guides</a>
      <a class="text-link" href="/templates">Download free templates</a>
    </div>
    <ul class="hero-proof" aria-label="Library highlights">
      <li>{len(PAGES)} practical guides</li>
      <li>3 free Word templates</li>
      <li>No sign-up</li>
    </ul>
  </div>
  <div class="hero-workbench" aria-label="Annotated example from the machine learning resume guide">
    <div class="workbench-bar"><span>PROJECT REVIEW</span><span>ENTRY-LEVEL ML</span></div>
    <div class="resume-sheet">
      <p class="example-label">ANNOTATED EXAMPLE</p>
      <p class="resume-name">Alex Chen</p>
      <p class="resume-contact">Computer Science &middot; Python &middot; Machine Learning</p>
      <div class="resume-rule"></div>
      <p class="resume-section">PROJECTS</p>
      <p class="resume-project">Customer Churn Prediction Pipeline</p>
      <p class="resume-bullet">Built a machine learning pipeline to predict customer churn using Python, pandas, and scikit-learn.</p>
      <p class="resume-bullet">Cleaned and transformed tabular data, engineered high-signal features, and compared multiple classification models.</p>
      <div class="annotation">
        <span>WHY IT WORKS</span>
        <p>The bullet names the problem, tools, and workflow. It shows evidence without inventing job history.</p>
      </div>
    </div>
    <p class="workbench-caption">From coursework to credible proof.</p>
  </div>
</section>
<div id="guides" class="guide-index">
{''.join(sections)}
</div>
<section class="value-prop">
  <div class="value-intro">
    <h2>Advice you can put on the page.</h2>
    <p>Every guide moves from a real job-search question to something you can use in your own resume.</p>
  </div>
  <ol class="method-list">
    <li><strong>Study a complete example.</strong> See how the summary, skills, projects, and education work together.</li>
    <li><strong>Adapt copy-ready bullets.</strong> Replace the placeholders with your actual tools, decisions, and results.</li>
    <li><strong>Map it to the job.</strong> Mirror the employer's language truthfully, then download the matching Word template.</li>
  </ol>
</section>
'''
    description = 'Free, copy-ready resume examples and templates for entry-level machine learning engineers, software engineers, and data scientists with no experience.'
    (SITE_DIR / 'index.html').write_text(
        shell(f'{SITE_NAME} | Free Entry-Level Tech Resume Examples', description, f'{BASE_URL}/', nav_html, body),
        encoding='utf-8',
    )


def build_status(nav_html: str) -> None:
    body = '''
<section class="page-head compact">
  <h1>Site Status</h1>
  <p class="lead">What is live, what is in progress, and where the library is heading next.</p>
</section>
<section class="grid single">
  <article class="card">
    <h2>Live now</h2>
    <ul>
      <li>20 full resume guides (about 34,200 words of copy-ready content)</li>
      <li>About, Contact, Editorial Policy, Privacy Policy, Terms, and Disclaimer pages</li>
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
<section class="page-head compact">
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
        if stripped.endswith(':'):
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
    updated_label = display_date(page.get('updated', CONTENT_REVIEW_DATE))
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
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="crumb-sep">/</span><a href="/#guides">Guides</a><span class="crumb-sep">/</span><span class="crumb-current">{html.escape(page.get('nav', page['title']))}</span></nav>
<section class="page-head article-head">
  <h1>{html.escape(page['title'])}</h1>
  <p class="page-context">{html.escape(page.get('category', 'Guide'))} &middot; Free guide + copy-ready template</p>
  <p class="lead">{html.escape(page['summary'])}</p>
  <p class="byline">By <a href="/about#about-the-author">{html.escape(AUTHOR['name'])}</a>, {html.escape(AUTHOR['title'])} &middot; Last updated {updated_label} &middot; {minutes} min read</p>
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
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 34 34">'
        '<path d="M5 4h17v26H5z" fill="#123f35"/>'
        '<path d="M22 4l7 7v19H12" fill="#dce9df"/>'
        '<path d="M10 11h7M10 16h12M10 21h8" stroke="#fff" stroke-width="2"/>'
        '<path d="M23 22l3 3 5-7" stroke="#c7472e" stroke-width="2.5"/>'
        '</svg>'
    )
    (SITE_DIR / 'favicon.svg').write_text(svg, encoding='utf-8')


def build_404(nav_html: str) -> None:
    body = f'''
<section class="page-head compact not-found">
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
        urls.append((f"{BASE_URL}/pages/{page['slug']}", page.get('updated', CONTENT_REVIEW_DATE)))
    for page in LEGAL_PAGES:
        urls.append((f"{BASE_URL}/{page['slug']}", page.get('updated', CONTENT_REVIEW_DATE)))

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
  --bg: #f3f5f2;
  --panel: #ffffff;
  --ink: #16241f;
  --muted: #59675f;
  --line: #d5ded7;
  --accent: #0e5b49;
  --accent-strong: #083e33;
  --accent-soft: #e4eee8;
  --note: #b6412c;
  --note-soft: #f8e9e4;
  --summary-bg: #edf2ed;
  --footer-bg: #102d26;
  --footer-ink: #e0ebe5;
  --footer-muted: #a9bdb3;
  --shadow: 0 18px 44px rgba(22, 36, 31, 0.12);
  --radius: 14px;
  --font-body: Aptos, "Segoe UI", sans-serif;
  --font-display: "Aptos Display", Aptos, "Segoe UI", sans-serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 100px; }
body {
  margin: 0;
  font-family: var(--font-body);
  font-size: 16px;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}
::selection { color: var(--ink); background: #c9ddd0; }
a { color: var(--accent); text-decoration-thickness: .08em; text-underline-offset: .18em; }
a:hover { text-decoration: underline; }
button, a, summary { -webkit-tap-highlight-color: transparent; }
a:focus-visible, summary:focus-visible, button:focus-visible {
  outline: 3px solid var(--note); outline-offset: 4px;
}
svg { flex: 0 0 auto; }
.site-shell { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
.skip-link {
  position: fixed; top: 10px; left: 10px; z-index: 100; padding: 10px 16px;
  color: #fff; background: var(--ink); border-radius: 8px; transform: translateY(-160%);
}
.skip-link:focus { transform: translateY(0); }

.site-header {
  position: sticky; top: 0; z-index: 20;
  display: flex; justify-content: space-between; gap: 24px; align-items: center;
  min-height: 76px; padding: 12px 32px; margin: 0 -32px;
  background: var(--bg); border-bottom: 1px solid var(--line);
}
.brand {
  display: inline-flex; align-items: center; gap: 11px;
  font-family: var(--font-display); font-size: 1.08rem; font-weight: 800;
  letter-spacing: -0.01em; color: var(--ink); white-space: nowrap; text-decoration: none;
}
.logo-mark { display: block; }
.top-nav { display: flex; align-items: center; gap: 4px; font-size: .92rem; }
.top-nav a {
  display: inline-flex; align-items: center; min-height: 44px; padding: 8px 12px;
  color: var(--ink); border-radius: 10px; font-weight: 600; text-decoration: none;
}
.top-nav a:hover { background: var(--accent-soft); color: var(--accent-strong); }
.top-nav a.nav-cta, .mobile-nav a.nav-cta {
  margin-left: 8px; padding: 10px 18px; background: var(--accent); color: #fff; font-weight: 750;
}
.top-nav a.nav-cta:hover, .mobile-nav a.nav-cta:hover { background: var(--accent-strong); color: #fff; }
.nav-toggle { display: none; position: relative; }
.nav-toggle summary {
  display: flex; align-items: center; justify-content: center; min-width: 76px; min-height: 44px;
  padding: 8px 14px; border: 1px solid var(--line); border-radius: 10px;
  background: var(--panel); font-weight: 700; cursor: pointer; list-style: none;
}
.nav-toggle summary::-webkit-details-marker { display: none; }
.mobile-nav {
  width: 100%; margin-top: 10px; padding: 8px 0 0;
  background: var(--panel); border-top: 1px solid var(--line);
}
.mobile-nav a {
  display: flex; align-items: center; min-height: 48px; padding: 10px 12px;
  color: var(--ink); border-radius: 8px; font-weight: 650; text-decoration: none;
}
.mobile-nav a:hover { background: var(--accent-soft); }
.mobile-nav a.nav-cta { margin: 8px 0 0; justify-content: center; }

.home-hero {
  display: grid; grid-template-columns: minmax(0, 1.06fr) minmax(390px, .94fr);
  gap: 64px; align-items: center; padding: 68px 0 76px;
}
.hero-copy { min-width: 0; }
.hero h1, .page-head h1 {
  margin: 0 0 24px; font-family: var(--font-display); font-weight: 800;
  letter-spacing: -0.035em; text-wrap: balance;
}
.home-hero h1 { max-width: 680px; font-size: clamp(3.1rem, 5.5vw, 5rem); line-height: 1.3; }
.lead {
  max-width: 670px; margin: 0; color: #3e5047; font-size: 1.22rem; line-height: 1.65;
  text-wrap: pretty;
}
.hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 20px; margin-top: 32px; }
.btn-primary {
  display: inline-flex; align-items: center; justify-content: center; min-height: 52px; padding: 13px 24px;
  background: var(--accent); color: #fff; border-radius: 12px; font-weight: 750;
  text-decoration: none; transition: background .15s ease, transform .15s ease;
}
.btn-primary:hover { background: var(--accent-strong); transform: translateY(-2px); }
.text-link { font-weight: 700; }
.hero-proof {
  display: flex; flex-wrap: wrap; gap: 0; margin: 32px 0 0; padding: 0; list-style: none;
  color: var(--muted); font-size: .9rem;
}
.hero-proof li + li { margin-left: 16px; padding-left: 16px; border-left: 1px solid var(--line); }
.hero-workbench {
  min-width: 0; padding: 18px; background: #dfe8e0; border: 1px solid #c8d5ca;
  border-radius: 16px; box-shadow: var(--shadow); transform: rotate(-1deg);
  animation: workbench-enter .7s cubic-bezier(.16, 1, .3, 1) both;
}
.workbench-bar {
  display: flex; justify-content: space-between; gap: 16px; padding: 0 2px 14px;
  color: var(--accent-strong); font-size: .72rem; font-weight: 800; letter-spacing: .08em;
}
.resume-sheet { padding: 28px; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; }
.example-label, .resume-section, .annotation span {
  font-size: .72rem; font-weight: 800; letter-spacing: .08em;
}
.example-label { margin: 0 0 20px; color: var(--note); }
.resume-name { margin: 0; font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; line-height: 1.35; }
.resume-contact { margin: 3px 0 0; color: var(--muted); font-size: .8rem; }
.resume-rule { height: 1px; margin: 20px 0; background: var(--ink); }
.resume-section { margin: 0 0 12px; color: var(--accent); }
.resume-project { margin: 0 0 12px; font-size: 1rem; font-weight: 750; line-height: 1.4; }
.resume-bullet { position: relative; margin: 9px 0; padding-left: 17px; font-size: .88rem; line-height: 1.6; }
.resume-bullet::before {
  content: ""; position: absolute; left: 0; top: .65em; width: 5px; height: 5px; background: var(--accent);
}
.annotation { margin-top: 22px; padding: 15px 17px; background: var(--note-soft); border: 1px solid #e9c9bf; border-radius: 12px; }
.annotation span { color: var(--note); }
.annotation p { margin: 5px 0 0; font-size: .84rem; line-height: 1.55; }
.workbench-caption { margin: 14px 4px 0; color: var(--accent-strong); font-size: .88rem; font-weight: 700; }
@keyframes workbench-enter {
  from { transform: translateY(20px) rotate(1deg); }
  to { transform: translateY(0) rotate(-1deg); }
}

.guide-index { padding-top: 16px; }
.guide-category {
  display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 64px;
  padding: 56px 0; border-top: 1px solid var(--line);
}
.category-heading h2, .value-prop h2, .related > h2 {
  margin: 0; font-family: var(--font-display); font-size: 2rem; font-weight: 800;
  line-height: 1.35; letter-spacing: -0.02em; text-wrap: balance;
}
.category-heading p { margin: 14px 0 0; color: var(--muted); line-height: 1.65; }
.guide-count { display: block; margin-top: 20px; color: var(--accent); font-size: .86rem; font-weight: 750; }
.guide-list { border-top: 1px solid var(--ink); }
.guide-card { position: relative; padding: 27px 0; border-bottom: 1px solid var(--line); }
.guide-card h3 { margin: 0 0 10px; font-family: var(--font-display); font-size: 1.24rem; line-height: 1.4; letter-spacing: -0.01em; }
.guide-card h3 a { color: var(--ink); text-decoration: none; }
.guide-card h3 a:hover { color: var(--accent); text-decoration: underline; }
.guide-card > p { max-width: 72ch; margin: 0; color: var(--muted); font-size: .96rem; line-height: 1.65; }
.guide-card .card-meta { margin-top: 12px; color: var(--accent); font-size: .8rem; font-weight: 650; }

.value-prop {
  display: grid; grid-template-columns: .85fr 1.15fr; gap: 64px;
  margin: 64px 0; padding: 44px; color: var(--footer-ink); background: var(--footer-bg); border-radius: 16px;
}
.value-prop h2 { color: #fff; font-size: 2.35rem; }
.value-intro > p { margin: 16px 0 0; color: var(--footer-ink); line-height: 1.65; }
.method-list { margin: 0; padding-left: 1.5rem; }
.method-list li { padding-left: 8px; line-height: 1.65; }
.method-list li + li { margin-top: 20px; }
.method-list strong { display: block; color: #fff; }

.page-head { max-width: 1020px; margin: 0 0 40px; padding: 56px 0 42px; border-bottom: 1px solid var(--line); }
.page-head h1 { max-width: 980px; font-size: clamp(2.35rem, 4.7vw, 4rem); line-height: 1.3; }
.page-head.compact { max-width: 860px; }
.page-head.compact h1 { font-size: clamp(2.2rem, 4vw, 3.3rem); }
.page-context { margin: -4px 0 20px; color: var(--accent); font-size: .9rem; font-weight: 750; }
.byline { max-width: 760px; margin: 20px 0 0; color: var(--muted); font-size: .88rem; line-height: 1.65; }
.byline a { color: var(--ink); font-weight: 650; }
.crumbs { margin: 26px 0 0; color: var(--muted); font-size: .86rem; overflow-wrap: anywhere; }
.crumbs a { color: var(--muted); }
.crumb-sep { margin: 0 8px; color: #8b9990; }
.crumb-current { color: var(--ink); font-weight: 600; }

.article-layout {
  display: grid; grid-template-columns: 220px minmax(0, 760px); justify-content: center;
  gap: 56px; align-items: start;
}
.article-main { min-width: 0; }
.toc-sidebar { position: sticky; top: 104px; }
.toc-desktop { padding: 18px 0; border-top: 2px solid var(--ink); border-bottom: 1px solid var(--line); }
.toc-desktop h2 { margin: 0 0 12px; font-size: .88rem; line-height: 1.4; }
.toc-desktop ol { margin: 0; padding: 0; list-style: none; }
.toc-desktop li { margin: 0; font-size: .88rem; line-height: 1.45; }
.toc-desktop a { display: block; padding: 8px 0; color: var(--muted); text-decoration: none; }
.toc-desktop a:hover, .toc-desktop a.active { color: var(--accent-strong); font-weight: 700; }
.toc-mobile { display: none; }
.summary-box { margin: 0 0 34px; padding: 24px 0; border-top: 1px solid var(--ink); border-bottom: 1px solid var(--line); }
.summary-box > strong { display: block; margin-bottom: 8px; color: var(--accent); font-size: .82rem; text-transform: uppercase; letter-spacing: .06em; }
.summary-box p { margin: 0; color: #2d4036; font-size: 1.12rem; line-height: 1.7; }
.takeaways-box { margin: 40px 0; padding: 26px 28px; background: var(--accent-soft); border-radius: var(--radius); }
.takeaways-box h2 { margin: 0 0 12px !important; font-size: 1.3rem !important; }
.takeaways-box ul { margin: 0; padding-left: 1.3rem; }
.takeaways-box li { margin: 8px 0; font-size: 1rem; }

.prose { max-width: 72ch; min-width: 0; }
.prose h1:first-child { display: none; }
.prose h2 {
  margin: 3.2rem 0 1rem; font-family: var(--font-display); font-size: 1.85rem; font-weight: 800;
  line-height: 1.35; letter-spacing: -0.02em; scroll-margin-top: 100px; text-wrap: balance;
}
.prose h2:first-of-type { margin-top: 0; }
.prose h3 { margin: 2.2rem 0 .8rem; font-size: 1.28rem; line-height: 1.4; scroll-margin-top: 100px; text-wrap: balance; }
.prose p, .prose li, .prose blockquote { color: #27372f; font-size: 1.1rem; line-height: 1.75; overflow-wrap: anywhere; }
.prose p { margin: 1.1em 0; text-wrap: pretty; }
.prose ul, .prose ol { padding-left: 1.4rem; }
.prose li { margin: 8px 0; }
.prose blockquote { margin: 28px 0; padding: 20px 24px; background: var(--summary-bg); border: 1px solid var(--line); border-radius: var(--radius); }
.prose blockquote p { font-size: inherit; }
code { padding: .12rem .42rem; background: var(--accent-soft); border-radius: 6px; font-family: Consolas, monospace; font-size: .9em; overflow-wrap: anywhere; }

.author-box { display: flex; gap: 18px; align-items: flex-start; margin: 44px 0 28px; padding: 28px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.author-avatar {
  flex: 0 0 auto; display: flex; align-items: center; justify-content: center; width: 52px; height: 52px;
  color: #fff; background: var(--accent); border-radius: 50%; font-weight: 800;
}
.author-text > strong { color: var(--accent); font-size: .82rem; text-transform: uppercase; letter-spacing: .06em; }
.author-text p { margin: 7px 0 0; color: #34483d; font-size: .95rem; line-height: 1.65; }
.cta-box { margin: 40px 0; padding: 30px; color: var(--footer-ink); background: var(--footer-bg); border-radius: var(--radius); }
.cta-box h3 { margin: 0 0 12px; color: #fff; font-family: var(--font-display); font-size: 1.55rem; line-height: 1.4; }
.cta-box p { color: var(--footer-ink); }
.cta-box a { color: #fff; }
.cta-button {
  display: inline-flex; align-items: center; justify-content: center; min-height: 48px; margin: 8px 0; padding: 12px 22px;
  color: var(--ink) !important; background: #fff; border-radius: 10px; font-weight: 750; text-decoration: none;
}
.cta-button:hover { background: var(--accent-soft); }
.cta-box .cta-alt { margin-bottom: 0; color: var(--footer-muted); font-size: .9rem; }
.download-box {
  display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap;
  margin: 32px 0; padding: 22px 24px; background: var(--accent-soft); border: 1px solid #c3d6c8; border-radius: var(--radius);
}
.download-box-text { display: flex; flex-direction: column; gap: 4px; }
.download-box-text strong { font-size: 1.02rem; }
.download-box-text span { max-width: 480px; color: var(--muted); font-size: .88rem; line-height: 1.55; }
.download-box-btn {
  display: inline-flex; align-items: center; justify-content: center; min-height: 48px; padding: 10px 20px;
  color: #fff; background: var(--accent); border-radius: 10px; font-weight: 750; white-space: nowrap; text-decoration: none;
}
.download-box-btn:hover { background: var(--accent-strong); }

.grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }
.grid.single { grid-template-columns: 1fr; }
.card { min-width: 0; padding: 26px; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); }
.card h2, .card h3 { margin: 0 0 12px; font-family: var(--font-display); font-size: 1.24rem; line-height: 1.4; letter-spacing: -0.01em; }
.card h2 a, .card h3 a { color: var(--ink); }
.card p { color: var(--muted); font-size: .96rem; line-height: 1.65; }
.card li { margin: 8px 0; line-height: 1.65; }
.template-card { display: flex; flex-direction: column; }
.template-card p { flex: 1; }
.template-card .download-box-btn { align-self: flex-start; margin-top: 12px; }
.related { margin: 64px 0; }
.related > h2 { margin-bottom: 22px; }
.related .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.not-found { max-width: 760px; }

.site-footer { margin-top: 24px; color: var(--footer-ink); background: var(--footer-bg); }
.footer-grid { display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 36px; padding-top: 48px; padding-bottom: 36px; }
.footer-brand .brand { color: #fff; }
.footer-brand p { max-width: 320px; margin: 16px 0 0; font-size: .92rem; line-height: 1.65; }
.footer-fine { color: var(--footer-muted) !important; font-size: .82rem !important; }
.footer-col h2 { margin: 6px 0 14px; color: var(--footer-muted); font-size: .82rem; line-height: 1.4; text-transform: uppercase; letter-spacing: .06em; }
.footer-col a { display: block; padding: 5px 0; color: var(--footer-ink); font-size: .94rem; line-height: 1.5; overflow-wrap: anywhere; }
.footer-col a:hover { color: #fff; }
.footer-col p.footer-fine { margin: 12px 0 0; }
.footer-bottom { padding-top: 20px; padding-bottom: 24px; border-top: 1px solid #395149; color: var(--footer-muted); font-size: .84rem; }
.footer-bottom p { margin: 0; }

@media (max-width: 1060px) {
  .home-hero { grid-template-columns: minmax(0, 1fr) minmax(360px, .9fr); gap: 36px; }
  .article-layout { grid-template-columns: 200px minmax(0, 740px); gap: 36px; }
  .footer-grid { grid-template-columns: 1.4fr 1fr 1fr; }
  .footer-grid > :last-child { grid-column: 2; }
}
@media (max-width: 900px) {
  .article-layout { grid-template-columns: 1fr; }
  .article-main { width: 100%; max-width: 760px; margin: 0 auto; }
  .toc-desktop, .toc-sidebar { display: none; }
  .toc-mobile { display: block; margin: 0 0 30px; padding: 16px 20px; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); }
  .toc-mobile summary { min-height: 44px; cursor: pointer; font-weight: 700; }
  .toc-mobile ol { margin: 12px 0 2px; padding-left: 1.3rem; }
  .toc-mobile li { margin: 8px 0; font-size: .98rem; }
  .home-hero { grid-template-columns: 1fr; gap: 44px; padding: 52px 0 60px; }
  .hero-copy { max-width: 740px; }
  .hero-workbench { width: min(100%, 640px); }
  .guide-category { grid-template-columns: 1fr; gap: 26px; }
  .category-heading { max-width: 660px; }
  .value-prop { grid-template-columns: 1fr; gap: 30px; }
}
@media (max-width: 768px) {
  .site-shell { padding: 0 20px; }
  .site-header { display: grid; grid-template-columns: minmax(0, 1fr) auto; min-height: 68px; margin: 0 -20px; padding: 10px 20px; }
  .site-header > .brand { grid-column: 1; grid-row: 1; align-self: start; z-index: 1; margin-top: 5px; }
  .top-nav { display: none; }
  .nav-toggle { display: block; grid-column: 2; grid-row: 1; margin: 0; }
  .nav-toggle[open] { display: grid; grid-column: 1 / -1; grid-template-columns: minmax(0, 1fr) auto; }
  .nav-toggle summary { grid-column: 2; width: max-content; margin-left: auto; }
  .mobile-nav { grid-column: 1 / -1; }
  .home-hero { padding: 40px 0 50px; }
  .home-hero h1 { font-size: clamp(2.65rem, 12vw, 4rem); }
  .lead { font-size: 1.08rem; }
  .hero-workbench { padding: 12px; transform: none; animation-name: workbench-enter-mobile; }
  .resume-sheet { padding: 22px; }
  .guide-category { padding: 42px 0; }
  .category-heading h2, .value-prop h2, .related > h2 { font-size: 1.75rem; }
  .value-prop { margin: 48px 0; padding: 28px; }
  .page-head { margin-bottom: 30px; padding: 38px 0 30px; }
  .page-head h1, .page-head.compact h1 { font-size: clamp(2rem, 9vw, 3rem); }
  .crumbs { margin-top: 20px; }
  .grid, .related .grid { grid-template-columns: 1fr; }
  .prose h2 { font-size: 1.6rem; }
  .prose p, .prose li, .prose blockquote { font-size: 1rem; }
  .download-box { flex-direction: column; align-items: stretch; }
  .download-box-btn { width: 100%; white-space: normal; text-align: center; }
  .related { margin: 48px 0; }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 28px; }
  .footer-grid > :last-child { grid-column: auto; }
}
@media (max-width: 520px) {
  .brand { font-size: .98rem; }
  .logo-mark { width: 30px; height: 30px; }
  .home-hero { display: flex; flex-direction: column; gap: 0; padding: 28px 0 36px; }
  .hero-copy, .hero-actions { display: contents; }
  .home-hero h1 { order: 1; margin-bottom: 16px; font-size: clamp(2.25rem, 9vw, 2.6rem); }
  .home-hero .lead { order: 2; font-size: 1rem; line-height: 1.55; }
  .home-hero .btn-primary { order: 3; width: 100%; margin-top: 24px; }
  .home-hero .hero-workbench { order: 4; margin-top: 24px; }
  .home-hero .text-link { order: 5; margin-top: 20px; }
  .home-hero .hero-proof { order: 6; }
  .hero-workbench { padding: 12px; }
  .hero-proof { display: block; }
  .hero-proof li + li { margin: 6px 0 0; padding: 0; border: 0; }
  .workbench-bar { flex-wrap: wrap; gap: 4px 12px; padding-bottom: 10px; }
  .resume-sheet { padding: 16px; }
  .example-label, .resume-name, .resume-contact, .resume-rule, .workbench-caption,
  .resume-bullet + .resume-bullet { display: none; }
  .resume-project { font-size: .94rem; }
  .resume-bullet { font-size: .84rem; }
  .annotation { margin-top: 14px; padding: 12px 14px; }
  .annotation p { line-height: 1.5; }
  .value-prop { padding: 24px 20px; }
  .takeaways-box, .cta-box { padding: 22px 20px; }
  .author-box { gap: 14px; }
  .author-avatar { width: 44px; height: 44px; }
  .footer-grid { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .hero-workbench { transform: none; }
}
@keyframes workbench-enter-mobile {
  from { transform: translateY(16px); }
  to { transform: translateY(0); }
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

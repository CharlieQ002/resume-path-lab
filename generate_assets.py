"""Generate downloadable .docx resume templates and OG share images.

Outputs into site/downloads/ and site/assets/og/. Run from repo root:
    python3 generate_assets.py
"""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / 'site'
DOWNLOADS_DIR = SITE_DIR / 'downloads'
OG_DIR = SITE_DIR / 'assets' / 'og'

INK = (31, 26, 23)
MUTED = (111, 98, 89)
BG = (246, 242, 234)
PANEL = (255, 253, 248)
ACCENT = (15, 118, 110)
ACCENT_SOFT = (216, 243, 238)

LATO_BLACK = '/usr/share/fonts/truetype/lato/Lato-Black.ttf'
LATO_BOLD = '/usr/share/fonts/truetype/lato/Lato-Bold.ttf'
LATO_REG = '/usr/share/fonts/truetype/lato/Lato-Regular.ttf'


# --------------------------------------------------------------------------- docx

def set_cell_border_bottom(paragraph, color='999999', size='6'):
    p = paragraph._p
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), size)
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_section_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text.upper())
    run.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Calibri'
    run.font.color.rgb = RGBColor(0x1F, 0x1A, 0x17)
    r = run._element.rPr
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:val'), '20')
    r.append(spacing)
    set_cell_border_bottom(p)
    return p


def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    if bold_prefix:
        run = p.add_run(bold_prefix)
        run.bold = True
        run.font.size = Pt(10.5)
        run.font.name = 'Calibri'
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.name = 'Calibri'
    return p


def add_body(doc, text, bold=False, italic=False, size=10.5, space_after=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.name = 'Calibri'
    return p


def add_two_line(doc, left, right):
    """Left-bold title + right-aligned date-ish text on one line via tab stop."""
    from docx.enum.text import WD_TAB_ALIGNMENT
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.1), WD_TAB_ALIGNMENT.RIGHT)
    run = p.add_run(left)
    run.bold = True
    run.font.size = Pt(10.5)
    run.font.name = 'Calibri'
    run = p.add_run('\t' + right)
    run.font.size = Pt(10.5)
    run.font.name = 'Calibri'
    run.font.color.rgb = RGBColor(0x6F, 0x62, 0x59)
    return p


def build_docx(path: Path, name: str, contact: str, summary: str, skills: dict,
               projects: list[dict], education: list[tuple[str, str]]):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(10.5)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(name)
    run.bold = True
    run.font.size = Pt(20)
    run.font.name = 'Calibri'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(contact)
    run.font.size = Pt(9.5)
    run.font.name = 'Calibri'
    run.font.color.rgb = RGBColor(0x6F, 0x62, 0x59)

    add_section_heading(doc, 'Professional Summary')
    add_body(doc, summary)

    add_section_heading(doc, 'Skills')
    for category, items in skills.items():
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(f'{category}: ')
        run.bold = True
        run.font.size = Pt(10.5)
        run.font.name = 'Calibri'
        run = p.add_run(items)
        run.font.size = Pt(10.5)
        run.font.name = 'Calibri'

    add_section_heading(doc, 'Projects')
    for proj in projects:
        add_two_line(doc, proj['name'], proj.get('meta', ''))
        for bullet in proj['bullets']:
            add_bullet(doc, bullet)

    add_section_heading(doc, 'Education')
    for school, detail in education:
        add_two_line(doc, school, detail)

    doc.save(path)


def generate_templates() -> None:
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    build_docx(
        DOWNLOADS_DIR / 'entry-level-ml-engineer-resume-template.docx',
        name='[Your Name]',
        contact='[City, State] | [email@example.com] | [LinkedIn] | [GitHub] | [Portfolio]',
        summary=('Entry-level machine learning engineer with a background in computer science and hands-on '
                 'project experience in Python, data analysis, model training, and deployment workflows. '
                 'Built end-to-end ML projects involving data cleaning, feature engineering, model evaluation, '
                 'and API-based delivery. Seeking to apply software fundamentals and practical machine learning '
                 'project experience in a full-time ML engineering role.'),
        skills={
            'Languages': 'Python, SQL, JavaScript',
            'ML / Data': 'scikit-learn, pandas, NumPy, Matplotlib, basic PyTorch',
            'Engineering': 'Git, REST APIs, Jupyter, Linux, Docker basics',
            'Concepts': 'feature engineering, model evaluation, supervised learning, data preprocessing, deployment basics',
        },
        projects=[
            {
                'name': 'Customer Churn Prediction Pipeline',
                'meta': '[GitHub link]',
                'bullets': [
                    'Built a machine learning pipeline to predict customer churn using Python, pandas, and scikit-learn',
                    'Cleaned and transformed tabular data, engineered high-signal features, and compared multiple classification models',
                    'Improved validation F1 score by tuning hyperparameters and selecting features based on model contribution',
                    'Packaged final inference workflow into a simple API demo and documented assumptions, failure cases, and next steps',
                ],
            },
            {
                'name': 'Resume Job Match Classifier',
                'meta': '[GitHub link]',
                'bullets': [
                    'Created a classification workflow that maps resume features to target job categories using NLP preprocessing and feature extraction',
                    'Designed a rule-plus-model baseline to improve explainability for non-technical reviewers',
                    'Evaluated model outputs against manually labeled samples and wrote clear analysis of false positives and edge cases',
                ],
            },
        ],
        education=[('[Degree, e.g. B.S. in Computer Science], [University Name]', 'Graduation: [Year]')],
    )

    build_docx(
        DOWNLOADS_DIR / 'software-engineer-resume-no-experience-template.docx',
        name='[Your Name]',
        contact='[City, State] | [email@example.com] | [LinkedIn] | [GitHub]',
        summary=('Recent computer science graduate targeting entry-level software engineering roles. Built '
                 'practical projects in Python and JavaScript involving APIs, databases, and testing, with a '
                 'focus on clean code, documentation, and measurable outcomes.'),
        skills={
            'Languages': 'Python, JavaScript, SQL, Java',
            'Frameworks': 'Flask / FastAPI, React basics, Node.js basics',
            'Tools': 'Git, Docker basics, PostgreSQL, Linux, pytest',
            'Concepts': 'data structures, REST API design, unit testing, CI basics',
        },
        projects=[
            {
                'name': 'Task Management API',
                'meta': '[GitHub link]',
                'bullets': [
                    'Designed and built a REST API with Flask, PostgreSQL, and JWT authentication, covering full CRUD workflows',
                    'Wrote unit and integration tests with pytest, reaching over 80% coverage on core endpoints',
                    'Containerized the application with Docker and documented setup steps for local development',
                ],
            },
            {
                'name': 'Portfolio Website + Blog',
                'meta': '[Live link]',
                'bullets': [
                    'Built a responsive personal site with React and a static site generator, deployed on a CDN',
                    'Added a custom search and tagging system, improving content discoverability across 20+ posts',
                ],
            },
        ],
        education=[('[Degree], [University Name]', 'Graduation: [Year]')],
    )

    build_docx(
        DOWNLOADS_DIR / 'entry-level-data-science-resume-template.docx',
        name='[Your Name]',
        contact='[City, State] | [email@example.com] | [LinkedIn] | [GitHub] | [Kaggle]',
        summary=('Entry-level data scientist with a background in statistics and hands-on project experience in '
                 'Python, SQL, and end-to-end analysis workflows. Turned messy datasets into clear findings and '
                 'decision-ready reporting for class projects and self-directed work.'),
        skills={
            'Languages': 'Python, SQL, R',
            'Analysis': 'pandas, NumPy, scikit-learn, Matplotlib, Seaborn, Excel',
            'Workflow': 'Jupyter, Git, data cleaning, EDA, A/B test basics, dashboarding',
            'Concepts': 'regression, classification, clustering, statistical testing, data storytelling',
        },
        projects=[
            {
                'name': 'Retail Sales Analysis Dashboard',
                'meta': '[GitHub link]',
                'bullets': [
                    'Analyzed 100K+ rows of retail transaction data to identify revenue trends, seasonality, and underperforming categories',
                    'Built reusable cleaning and aggregation pipelines in pandas, cutting repeated analysis time across weekly updates',
                    'Presented findings as charts and a written brief that translated metrics into pricing and inventory recommendations',
                ],
            },
            {
                'name': 'Customer Segmentation Study',
                'meta': '[GitHub link]',
                'bullets': [
                    'Applied clustering techniques to transaction data to group customers by behavior and value',
                    'Validated segment stability across multiple runs and summarized segment profiles for non-technical readers',
                ],
            },
        ],
        education=[('[Degree, e.g. B.S. in Statistics], [University Name]', 'Graduation: [Year]')],
    )


# --------------------------------------------------------------------------- og images

def draw_tracked(draw, xy, text, font, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ''
    for w in words:
        trial = f'{current} {w}'.strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


def og_image(path: Path, eyebrow: str, title: str, brand: str = 'Resume Path Lab'):
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    # accent top-left bar
    draw.rectangle([0, 0, 14, H], fill=ACCENT)

    f_eye = ImageFont.truetype(LATO_BOLD, 30)
    f_brand = ImageFont.truetype(LATO_BOLD, 34)

    # card
    margin = 90
    card = [margin, 110, W - margin, H - 110]
    draw.rounded_rectangle(card, radius=36, fill=PANEL, outline=(221, 210, 195), width=2)

    x = card[0] + 50
    max_w = card[2] - card[0] - 100

    # accent chip behind eyebrow
    f_eye_size = 30
    ew = draw.textlength(eyebrow.upper(), font=f_eye) + 2 * len(eyebrow)
    chip_w = ew + 30
    chip_y = card[1] + 50
    draw.rounded_rectangle([x - 6, chip_y - 8, x + chip_w, chip_y + 44], radius=12, fill=ACCENT_SOFT)
    draw_tracked(draw, (x + 12, chip_y), eyebrow.upper(), f_eye, ACCENT, tracking=2)

    # title: auto-shrink until it fits on at most 2 lines
    f_title = None
    lines = []
    for size in (68, 62, 56, 50, 46):
        f_title = ImageFont.truetype(LATO_BLACK, size)
        lines = wrap_text(draw, title, f_title, max_w)
        if len(lines) <= 2:
            break
    line_h = f_title.size + 16
    y = chip_y + 92
    for line in lines[:2]:
        draw.text((x, y), line, font=f_title, fill=INK)
        y += line_h

    # accent bar, only if it clears the brand zone
    brand_y = card[3] - 66
    bar_y = y + 20
    if bar_y + 10 <= brand_y - 12:
        draw.rectangle([x, bar_y, x + 120, bar_y + 8], fill=ACCENT)

    # brand pinned to bottom of the card
    draw.text((x, brand_y), brand, font=f_brand, fill=INK)

    img.save(path, 'PNG')


def generate_og() -> None:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    pages = [
        ('home', 'Free resume examples', 'Entry-Level Resume Guides That Get Interviews'),
        ('entry-level-machine-learning-engineer-resume', 'Free guide + template', 'Entry-Level Machine Learning Engineer Resume'),
        ('how-to-write-machine-learning-resume-without-experience', 'Free 7-step guide', 'How to Write a Machine Learning Resume Without Experience'),
        ('software-engineer-resume-no-experience', 'Free guide + template', 'Software Engineer Resume With No Experience'),
        ('entry-level-data-science-resume', 'Free guide + template', 'Entry-Level Data Science Resume'),
        ('machine-learning-projects-for-resume', 'Free beginner guide', 'Machine Learning Projects for a Resume'),
        ('machine-learning-resume-summary-examples', '8 copy-ready examples', 'Machine Learning Resume Summary Examples'),
        ('kaggle-projects-for-resume', 'Free 2026 guide', 'Kaggle Projects for a Resume'),
        ('entry-level-data-analyst-resume', 'Free guide + template', 'Entry-Level Data Analyst Resume'),
        ('data-science-internship-resume', 'Internship screen secrets', 'Data Science Internship Resume'),
        ('python-projects-for-resume', '10 projects ranked', 'Python Projects for a Resume'),
    ]
    for slug, eyebrow, title in pages:
        og_image(OG_DIR / f'{slug}.png', eyebrow, title)
        print('og:', slug)


def main() -> None:
    generate_templates()
    generate_og()
    print('done. templates:', len(list(DOWNLOADS_DIR.glob('*.docx'))), 'og images:', len(list(OG_DIR.glob('*.png'))))


if __name__ == '__main__':
    main()

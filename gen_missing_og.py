"""Generate OG share images (1200x630) for pages that lack one, plus apple-touch-icon.

Windows-safe standalone script: uses system Arial/Segoe UI fonts instead of the
Linux Lato paths in generate_assets.py. Run from repo root:
    python gen_missing_og.py
"""
from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import build_site

ROOT = Path(__file__).resolve().parent
OG_DIR = ROOT / 'site' / 'assets' / 'og'

INK = (22, 36, 31)
MUTED = (89, 103, 95)
BG = (243, 245, 242)
PANEL = (255, 255, 255)
ACCENT = (14, 91, 73)
ACCENT_SOFT = (228, 238, 232)

FONT_BLACK = 'C:/Windows/Fonts/arialbd.ttf'
FONT_BOLD = 'C:/Windows/Fonts/arialbd.ttf'
FONT_REG = 'C:/Windows/Fonts/arial.ttf'

PAGES = {
    'home': ('FREE RESUME LIBRARY', 'Your Projects Are the Experience'),
    'ats-friendly-resume-guide': ('FREE 2026 GUIDE', 'ATS-Friendly Resume for Tech Jobs'),
    'resume-with-no-work-experience': ('FREE 2026 GUIDE', 'How to Write a Resume With No Work Experience'),
    'resume-skills-section-tech': ('FREE 2026 GUIDE', 'Tech Resume Skills Section'),
    'machine-learning-engineer-cover-letter': ('FREE 2026 GUIDE', 'Machine Learning Engineer Cover Letter'),
    'internship-resume-computer-science': ('EXAMPLE + PROJECT GUIDE', 'Computer Science Internship Resume'),
    'entry-level-software-developer-portfolio': ('PROJECTS + EXAMPLES', 'Entry-Level Software Developer Portfolio'),
    'how-to-list-projects-on-resume': ('BULLETS + EXAMPLES', 'How to List Projects on a Resume'),
    'entry-level-data-engineer-resume': ('EXAMPLE + PROJECTS', 'Entry-Level Data Engineer Resume'),
    'sql-projects-for-resume': ('8 IDEAS + BULLETS', 'SQL Projects for a Resume'),
}

FORCE = {'home'}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def draw_og(slug: str, badge: str, title: str) -> None:
    img = Image.new('RGB', (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, 630], fill=ACCENT)
    d.rounded_rectangle([90, 65, 1110, 565], radius=28, fill=PANEL, outline=(221, 210, 195))

    badge_font = font(FONT_BOLD, 26)
    bw = d.textbbox((0, 0), badge, font=badge_font)[2]
    d.rounded_rectangle([140, 155, 140 + bw + 40, 205], radius=22, fill=ACCENT_SOFT)
    d.text((160, 165), badge, font=badge_font, fill=ACCENT)

    title_font = font(FONT_BLACK, 64)
    lines = textwrap.wrap(title, width=26)
    y = 250
    for i, line in enumerate(lines[:3]):
        d.text((140, y), line, font=title_font, fill=INK)
        y += 84
    if y + 20 < 470:
        d.rectangle([140, y + 6, 240, y + 14], fill=ACCENT)

    d.text((140, 480), 'Resume Path Lab', font=font(FONT_REG, 30), fill=MUTED)

    out = OG_DIR / f'{slug}.png'
    img.save(out, optimize=True)
    print('wrote', out.name)


def draw_touch_icon() -> None:
    img = Image.new('RGB', (180, 180), ACCENT)
    d = ImageDraw.Draw(img)
    d.text((42, 32), 'R', font=font(FONT_BLACK, 110), fill=(255, 255, 255))
    out = ROOT / 'site' / 'apple-touch-icon.png'
    img.save(out, optimize=True)
    print('wrote', out.name)


def main() -> None:
    for slug, (badge, title) in PAGES.items():
        if slug not in FORCE and (OG_DIR / f'{slug}.png').exists():
            print('skip existing', slug)
            continue
        draw_og(slug, badge, title)
    for page in build_site.PAGES:
        slug = page['slug']
        if (OG_DIR / f'{slug}.png').exists():
            continue
        draw_og(slug, 'FREE GUIDE + TEMPLATE', page['title'])
    draw_touch_icon()


if __name__ == '__main__':
    main()

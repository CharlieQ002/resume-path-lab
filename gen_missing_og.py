"""Generate OG share images (1200x630) for pages that lack one, plus apple-touch-icon.

Windows-safe standalone script: uses system Arial/Segoe UI fonts instead of the
Linux Lato paths in generate_assets.py. Run from repo root:
    python gen_missing_og.py
"""
from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OG_DIR = ROOT / 'site' / 'assets' / 'og'

INK = (31, 26, 23)
MUTED = (111, 98, 89)
BG = (246, 242, 234)
PANEL = (255, 253, 248)
ACCENT = (15, 118, 110)
ACCENT_SOFT = (216, 243, 238)

FONT_BLACK = 'C:/Windows/Fonts/arialbd.ttf'
FONT_BOLD = 'C:/Windows/Fonts/arialbd.ttf'
FONT_REG = 'C:/Windows/Fonts/arial.ttf'

PAGES = {
    'ats-friendly-resume-guide': ('FREE 2026 GUIDE', 'ATS-Friendly Resume for Tech Jobs'),
    'resume-with-no-work-experience': ('FREE 2026 GUIDE', 'How to Write a Resume With No Work Experience'),
    'machine-learning-engineer-cover-letter': ('FREE 2026 GUIDE', 'Machine Learning Engineer Cover Letter'),
}


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
    for i, line in enumerate(lines[:2]):
        d.text((140, y), line, font=title_font, fill=INK)
        y += 84
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
        if (OG_DIR / f'{slug}.png').exists():
            print('skip existing', slug)
            continue
        draw_og(slug, badge, title)
    draw_touch_icon()


if __name__ == '__main__':
    main()

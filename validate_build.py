import json
import re
import sys
from pathlib import Path

site = Path('site/pages')
for f in sorted(site.glob('*.html')):
    h = f.read_text(encoding='utf-8')
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    types = []
    faq_n = 0
    for s in schemas:
        d = json.loads(s)
        types.append(d.get('@type'))
        if d.get('@type') == 'FAQPage':
            faq_n = len(d.get('mainEntity', []))
    cta = 'cta-box' in h
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    title = re.search(r'<title>(.*?)</title>', h).group(1)
    desc = re.search(r'<meta name="description" content="([^"]+)"', h).group(1)
    print(f'{f.name}')
    print(f'  schema: {types} faq_items={faq_n} cta={cta}')
    print(f'  canonical: {canonical.group(1)}')
    print(f'  title({len(title)}): {title}')
    print(f'  desc({len(desc)}): {desc[:90]}...')
    print()

h = Path('site/index.html').read_text(encoding='utf-8')
d = re.search(r'<meta name="description" content="([^"]+)"', h).group(1)
t = re.search(r'<title>(.*?)</title>', h).group(1)
print('index.html')
print(f'  title({len(t)}): {t}')
print(f'  desc({len(d)}): {d}')
print('  has shell jargon:', 'Round 1' in h or 'validation build' in h.lower())
print()
sm = Path('site/sitemap.xml').read_text(encoding='utf-8')
print('sitemap urls:', sm.count('<loc>'))
print('sitemap has .html:', '.html' in sm)

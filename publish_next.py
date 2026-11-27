from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

import build_site

ROOT = Path(__file__).resolve().parent
QUEUE_DIR = ROOT / 'content_queue'
MANIFEST_PATH = QUEUE_DIR / 'manifest.json'
SIMILARITY_LIMIT = 0.20


def load_manifest() -> list[dict]:
    entries = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
    assert len(entries) == 100, 'The queue must contain exactly 100 topics'
    for key in ('order', 'slug', 'keyword', 'title'):
        values = [entry[key] for entry in entries]
        assert len(values) == len(set(values)), f'Duplicate {key} in manifest'
    assert sorted(entry['order'] for entry in entries) == list(range(1, 101))
    return entries


def text_features(text: str) -> tuple[set[tuple[str, ...]], set[str]]:
    body = build_site.strip_frontmatter(text).lower()
    words = re.findall(r'[a-z0-9]+', body)
    shingles = {tuple(words[index:index + 8]) for index in range(max(0, len(words) - 7))}
    plain = re.sub(r'[#>*_\[\]()-]', ' ', body)
    sentences = set()
    for sentence in re.split(r'(?<=[.!?])\s+', plain):
        normalized = ' '.join(re.findall(r'[a-z0-9]+', sentence))
        if len(normalized.split()) >= 12:
            sentences.add(normalized)
    return shingles, sentences


def originality_report(slug: str, text: str) -> tuple[float, str]:
    candidate_shingles, candidate_sentences = text_features(text)
    sources = [
        (page['slug'], ROOT / 'pages' / f"{page['slug']}.md")
        for page in build_site.PAGES
    ]
    sources.extend(
        (entry['slug'], QUEUE_DIR / f"{entry['slug']}.md")
        for entry in load_manifest()
        if entry['status'] == 'ready' and entry['slug'] != slug
    )
    highest = (0.0, '')
    for other_slug, source in sources:
        other_shingles, other_sentences = text_features(source.read_text(encoding='utf-8'))
        repeated = candidate_sentences & other_sentences
        if repeated:
            example = sorted(repeated)[0]
            raise ValueError(f'{slug}: repeated long sentence with {other_slug}: {example[:120]}')
        union = candidate_shingles | other_shingles
        similarity = len(candidate_shingles & other_shingles) / len(union) if union else 0.0
        if similarity > highest[0]:
            highest = (similarity, other_slug)
    return highest


def validate_article(entry: dict) -> str:
    slug = entry['slug']
    source = QUEUE_DIR / f'{slug}.md'
    if not source.exists():
        raise ValueError(f'{slug}: ready article is missing')
    text = source.read_text(encoding='utf-8')
    metadata = build_site.parse_frontmatter(text)
    required = {'category', 'title', 'keyword', 'description', 'summary', 'template', 'related'}
    missing = required - metadata.keys()
    if missing:
        raise ValueError(f'{slug}: missing metadata {sorted(missing)}')
    if metadata.get('slug', slug) != slug:
        raise ValueError(f'{slug}: frontmatter slug does not match filename')
    for key in ('category', 'title', 'keyword'):
        if metadata[key] != entry[key]:
            raise ValueError(f'{slug}: {key} does not match manifest')
    if len(metadata['title']) > 60:
        raise ValueError(f'{slug}: title exceeds 60 characters')
    if len(metadata['description']) > 155:
        raise ValueError(f'{slug}: description exceeds 155 characters')
    if slug in build_site.PAGE_BY_SLUG:
        raise ValueError(f'{slug}: already exists in published pages')
    for page in build_site.PAGES:
        if metadata['keyword'].casefold() == page['keyword'].casefold():
            raise ValueError(f"{slug}: keyword already used by {page['slug']}")
        if metadata['title'].casefold() == page['title'].casefold():
            raise ValueError(f"{slug}: title already used by {page['slug']}")
    word_count = len(build_site.strip_frontmatter(text).split())
    if not 1500 <= word_count <= 1900:
        raise ValueError(f'{slug}: expected 1500-1900 words, found {word_count}')
    faq_count = len(build_site.extract_faq(text))
    if not 4 <= faq_count <= 5:
        raise ValueError(f'{slug}: expected 4-5 FAQ entries, found {faq_count}')
    missing_related = [slug for slug in metadata['related'] if slug not in build_site.PAGE_BY_SLUG]
    if missing_related:
        raise ValueError(f'{slug}: unknown related pages {missing_related}')
    if not (ROOT / 'site' / 'downloads' / metadata['template']).exists():
        raise ValueError(f'{slug}: template does not exist')
    similarity, similar_slug = originality_report(slug, text)
    if similarity >= SIMILARITY_LIMIT:
        raise ValueError(f'{slug}: similarity {similarity:.3f} with {similar_slug} exceeds {SIMILARITY_LIMIT:.2f}')
    return text


def stamp_publication_date(text: str, published: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if index and line.strip() == '---':
            break
        if line.startswith('published:'):
            lines[index] = f'published: {published}'
        elif line.startswith('updated:'):
            lines[index] = f'updated: {published}'
    return '\n'.join(lines) + '\n'


def update_agents(entry: dict, published_count: int) -> None:
    path = ROOT / 'AGENTS.md'
    text = path.read_text(encoding='utf-8')
    text = re.sub(
        r'pages/\*\.md      → 指南源稿（Markdown，\d+ 篇）',
        f'pages/*.md      → 指南源稿（Markdown，{published_count} 篇）',
        text,
    )
    row = f"| {entry['slug']} | {entry['keyword']} |"
    if row not in text:
        text = text.replace('\n合规页（在 `legal/`，不在 PAGES）：', f'\n{row}\n\n合规页（在 `legal/`，不在 PAGES）：')
    text = '\n'.join(
        line for line in text.splitlines()
        if not line.startswith('- `') or f"`{entry['slug']}`" not in line
    ) + '\n'
    path.write_text(text, encoding='utf-8')


def publish_next(check_only: bool = False) -> str:
    entries = load_manifest()
    ready = [entry for entry in entries if entry['status'] == 'ready']
    if not ready:
        return ''
    entry = ready[0]
    text = validate_article(entry)
    if check_only:
        return entry['slug']

    published = date.today().isoformat()
    stamped = stamp_publication_date(text, published)
    destination = ROOT / 'pages' / f"{entry['slug']}.md"
    destination.write_text(stamped, encoding='utf-8')
    (QUEUE_DIR / f"{entry['slug']}.md").unlink()

    entry['status'] = 'published'
    entry['published'] = published
    MANIFEST_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    update_agents(entry, len(build_site.PAGES) + 1)
    return entry['slug']


def main() -> None:
    parser = argparse.ArgumentParser(description='Validate or publish the next ready guide')
    parser.add_argument('--check', action='store_true', help='validate without changing files')
    args = parser.parse_args()
    slug = publish_next(check_only=args.check)
    if slug:
        print(slug)


if __name__ == '__main__':
    main()

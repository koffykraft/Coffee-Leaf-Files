#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path('.')
OUT = ROOT / 'rebuild-audit-output'
OUT.mkdir(exist_ok=True)

TAG_RE = re.compile(r'<[^>]+>', re.S)
SCRIPT_STYLE_RE = re.compile(r'<(script|style)\b[^>]*>.*?</\1>', re.I | re.S)
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)
TITLE_RE = re.compile(r'<title\b[^>]*>(.*?)</title>', re.I | re.S)
HEADING_RE = re.compile(r'<h([1-6])\b[^>]*>(.*?)</h\1>', re.I | re.S)
LINK_RE = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.I | re.S)
HREF_RE = re.compile(r'href\s*=\s*["\']([^"\']+)["\']', re.I)
CLASS_RE = re.compile(r'class\s*=\s*["\']([^"\']+)["\']', re.I)
ID_RE = re.compile(r'id\s*=\s*["\']([^"\']+)["\']', re.I)
NAV_RE = re.compile(r'<nav\b([^>]*)>(.*?)</nav>', re.I | re.S)
BREAD_RE = re.compile(r'class\s*=\s*["\'][^"\']*breadcrumb[^"\']*["\']', re.I)
REF_HEADING_RE = re.compile(r'\b(references?|sources?|bibliography|works cited)\b', re.I)
CITATION_PATTERNS = [
    re.compile(r'\[(\d{1,3})\]'),
    re.compile(r'<sup\b[^>]*>.*?</sup>', re.I | re.S),
    re.compile(r'\bdoi\s*[: ]\s*10\.\d{4,9}/[-._;()/:A-Z0-9]+', re.I),
]


def strip_tags(value: str) -> str:
    value = COMMENT_RE.sub(' ', value)
    value = SCRIPT_STYLE_RE.sub(' ', value)
    value = TAG_RE.sub(' ', value)
    value = html.unescape(value)
    return re.sub(r'\s+', ' ', value).strip()


def attrs_value(attrs: str, regex: re.Pattern[str]) -> str:
    m = regex.search(attrs)
    return m.group(1).strip() if m else ''


def classify_nav(attrs: str, body: str) -> str:
    cls = attrs_value(attrs, CLASS_RE).lower()
    text = strip_tags(body).lower()
    if 'breadcrumb' in cls:
        return 'breadcrumb-nav'
    if 'section' in cls or any(x in text for x in ['purpose', 'history', 'sources', 'evidence']):
        return 'section-nav'
    if 'top' in cls or 'main' in cls or 'site' in cls:
        return 'site/local-top-nav'
    return 'nav'


def page_record(path: Path) -> dict:
    raw = path.read_text(encoding='utf-8', errors='replace')
    visible = strip_tags(raw)
    words = re.findall(r"\b[\w’'-]+\b", visible, flags=re.UNICODE)

    title_m = TITLE_RE.search(raw)
    title = strip_tags(title_m.group(1)) if title_m else ''
    headings = [(int(level), strip_tags(body)) for level, body in HEADING_RE.findall(raw)]

    links = []
    link_texts = []
    for attrs, body in LINK_RE.findall(raw):
        href_m = HREF_RE.search(attrs)
        if not href_m:
            continue
        href = html.unescape(href_m.group(1).strip())
        text = strip_tags(body)
        links.append(href)
        link_texts.append((text, href))

    navs = []
    for attrs, body in NAV_RE.findall(raw):
        navs.append({
            'type': classify_nav(attrs, body),
            'class': attrs_value(attrs, CLASS_RE),
            'text': strip_tags(body)[:220]
        })

    breadcrumbs = len(BREAD_RE.findall(raw))
    back_library = sum(1 for text, href in link_texts
                       if ('back' in text.lower() and 'librar' in text.lower())
                       or text.lower().strip() in {'buna library', 'library'})
    internal_targets = [h for h in links if not h.startswith(('http://','https://','mailto:','tel:','javascript:','#'))]
    duplicate_targets = {k:v for k,v in Counter(internal_targets).items() if v > 1}

    ref_headings = [text for level, text in headings if REF_HEADING_RE.search(text)]
    citation_hits = sum(len(p.findall(raw)) for p in CITATION_PATTERNS)

    repeated_navigation_risk = (len(navs) + breadcrumbs + (1 if back_library else 0)) >= 3

    return {
        'page': path.as_posix(),
        'title': title,
        'word_count': len(words),
        'heading_count': len(headings),
        'h1_count': sum(1 for level, _ in headings if level == 1),
        'headings': headings,
        'nav_count': len(navs),
        'navs': navs,
        'breadcrumb_blocks': breadcrumbs,
        'library_back_or_home_links': back_library,
        'repeated_navigation_risk': repeated_navigation_risk,
        'link_count': len(links),
        'duplicate_internal_targets': duplicate_targets,
        'reference_headings': ref_headings,
        'citation_signal_count': citation_hits,
        'has_reference_section': bool(ref_headings),
        'has_api_call': '/api/' in raw,
        'meta_refresh': bool(re.search(r'http-equiv\s*=\s*["\']refresh["\']', raw, re.I)),
    }


def main() -> None:
    pages = sorted(p for p in ROOT.rglob('*.html') if '.git' not in p.parts and 'rebuild-audit-output' not in p.parts)
    records = [page_record(p) for p in pages]

    (OUT / 'page-inventory.json').write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding='utf-8')

    fields = [
        'page','title','word_count','heading_count','h1_count','nav_count','breadcrumb_blocks',
        'library_back_or_home_links','repeated_navigation_risk','link_count',
        'citation_signal_count','has_reference_section','has_api_call','meta_refresh'
    ]
    with (OUT / 'page-matrix.csv').open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in records:
            writer.writerow({k:r[k] for k in fields})

    risky = [r for r in records if r['repeated_navigation_risk']]
    refs_missing = [r for r in records if r['citation_signal_count'] and not r['has_reference_section']]

    md = [
        '# Buna Rebuild Audit — Machine Inventory', '',
        f'- HTML pages inventoried: **{len(records)}**',
        f'- Pages with repeated-navigation risk: **{len(risky)}**',
        f'- Pages with citation signals but no explicit reference heading: **{len(refs_missing)}**', '',
        '## Repeated-navigation risk', '',
        'This is a screening signal only. Each page must be visually inspected; multiple navigation layers may be legitimate if they perform different functions.', ''
    ]
    for r in risky:
        md.append(f"- `{r['page']}` — nav={r['nav_count']}, breadcrumb blocks={r['breadcrumb_blocks']}, Library/back links={r['library_back_or_home_links']}")
    md += ['', '## Dossier rule', '',
           'Machine findings do not determine truth, value or disposition. Every page still requires the human reconstruction dossier defined in `governance/BUNA_REBUILD_AUDIT_FRAMEWORK.md`.', '']
    (OUT / 'summary.md').write_text('\n'.join(md), encoding='utf-8')

    print('\n'.join(md))

if __name__ == '__main__':
    main()

from pathlib import Path

# 1. Stop using visitor-lounge as an ordinary navigation destination.
changed = []
for p in Path('.').rglob('*.html'):
    if p.name == 'visitor-lounge.html':
        continue
    s = p.read_text(encoding='utf-8')
    old = s
    s = s.replace('href="visitor-lounge.html"', 'href="index.html"')
    s = s.replace("href='visitor-lounge.html'", "href='index.html'")
    if s != old:
        p.write_text(s, encoding='utf-8')
        changed.append(str(p))

# 2. Preserve alternate Foundation pages but remove canonical ambiguity.
def legacy_foundation(path, old_title, new_title):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    if '<link rel="canonical" href="the-foliage-of-buna.html">' not in s:
        marker = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        if marker not in s:
            raise SystemExit(f'{path}: viewport marker not found')
        s = s.replace(marker, marker + '\n    <meta name="robots" content="noindex,follow">\n    <link rel="canonical" href="the-foliage-of-buna.html">', 1)
    if old_title not in s:
        raise SystemExit(f'{path}: expected title not found')
    s = s.replace(old_title, new_title, 1)
    p.write_text(s, encoding='utf-8')

legacy_foundation(
    'foliage-of-buna.html',
    '<title>The Foliage of Buna — Foundation</title>',
    '<title>The Foliage of Buna — Legacy Foundation Archive</title>'
)
legacy_foundation(
    'the-foliage-of-buna-minimal.html',
    '<title>THE FOLIAGE OF BUNA</title>',
    '<title>The Foliage of Buna — Legacy Minimal Archive</title>'
)

print(f'Updated visitor-lounge links in {len(changed)} HTML files:')
for p in changed:
    print(' -', p)
print('Canonicalized two preserved Foundation variants.')

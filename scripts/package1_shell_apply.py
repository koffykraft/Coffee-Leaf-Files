from pathlib import Path


def replace(path, old, new, count=1):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    n = s.count(old)
    if n < count:
        raise SystemExit(f'{path}: expected at least {count} occurrence(s) of {old!r}, found {n}')
    s = s.replace(old, new, count)
    p.write_text(s, encoding='utf-8')

# Catalogue title
replace('catalogue.html',
        '<title>The Foliage of Buna — Coffee Leaf Knowledge & Practices</title>',
        '<title>Buna Coffee Leaf Library — Catalogue</title>')

# Homepage semantic H1 and canonical contact address
replace('index.html',
        '<p class="lounge-hook">A library about brewing coffee leaves.</p>',
        '<h1 class="lounge-hook">A library about brewing coffee leaves.</h1>')
replace('index.html', 'mailto:hello@koffykraft.com', 'mailto:info@koffykraft.com')

# Terrain Map semantic H1, visually hidden so the existing full-screen UI is unchanged
replace('citane-terrain-map.html', '<body>\n\n<nav>',
        '<body>\n<h1 style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;">Citane Terrain Map</h1>\n\n<nav>')

# Sensory Companion stale door count
replace('sensory-companion.html',
        "label: 'The Library — all six doors'",
        "label: 'The Library — all nine doors'")

# visitor-lounge is a legacy redirect, but retain a meaningful fallback document
p = Path('visitor-lounge.html')
p.write_text('''<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="robots" content="noindex,follow">\n<meta http-equiv="refresh" content="0; url=index.html">\n<link rel="canonical" href="index.html">\n<title>Buna Library — Legacy Redirect</title>\n</head>\n<body>\n<h1>This Buna Library address has moved</h1>\n<p><a href="index.html">Continue to the Buna Coffee Leaf Library</a></p>\n<script>window.location.replace('index.html');</script>\n</body>\n</html>\n''', encoding='utf-8')

print('Package 1 shell corrections applied.')

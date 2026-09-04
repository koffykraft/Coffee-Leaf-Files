from pathlib import Path
import re


def read(path): return Path(path).read_text(encoding='utf-8')
def write(path, s): Path(path).write_text(s, encoding='utf-8')


def add_tab(path, href, label):
    s = read(path)
    if f'href="{href}"' in s:
        return
    start = s.find('<div class="tabs">')
    if start < 0:
        raise SystemExit(f'{path}: tabs block not found')
    end = s.find('</div>', start)
    if end < 0:
        raise SystemExit(f'{path}: tabs close not found')
    s = s[:end] + f'  <a class="tab" href="{href}">{label}</a>\n' + s[end:]
    write(path, s)

# Tradition learning resources: surface from each family intro.
for href, label in [
    ('chemo-schoolbook-guide.html','Schoolbook Guide'),
    ('chemo-visual-pictogram-guide.html','Visual Guide'),
]: add_tab('chemo-intro.html', href, label)

for href, label in [
    ('engere-schoolbook-guide-part-1.html','Schoolbook I'),
    ('engere-schoolbook-guide-part-2.html','Schoolbook II'),
    ('engere-visual-pictogram-guide.html','Visual Guide'),
]: add_tab('engere-intro.html', href, label)

for href, label in [
    ('kuti-schoolbook-guide.html','Schoolbook Guide'),
    ('kuti-visual-pictogram-guide.html','Visual Guide'),
]: add_tab('kuti-intro.html', href, label)

for href, label in [
    ('kawa-daun-schoolbook-guide.html','Schoolbook Guide'),
    ('kawa-daun-visual-pictogram-guide.html','Visual Guide'),
]: add_tab('kawa-daun-intro.html', href, label)

# Specialist deep pages.
add_tab('chemo-deep.html', 'chemo-plants.html', 'Plants & Spices')
add_tab('engere-deep.html', 'engere-people-work-context.html', 'People & Work')

# Vocabulary visual boards: surface from the matching topic and give each board a parent return.
def add_vocab_board(topic, board, label):
    s = read(topic)
    if board not in s:
        marker = '<div class="container">'
        if marker not in s:
            raise SystemExit(f'{topic}: container marker missing')
        link = f'<p class="image-caption" style="margin-top:18px;"><a href="{board}">Open the {label} visual board →</a></p>\n\n'
        s = s.replace(marker, marker + '\n\n' + link, 1)
        write(topic, s)
    b = read('vocab/' + board)
    parent = Path(topic).name
    if f'href="{parent}"' not in b:
        backlink = f'\n<p style="max-width:900px;margin:32px auto;padding:0 24px;"><a href="{parent}">← Back to {label}</a></p>\n'
        b = b.replace('</body>', backlink + '</body>', 1)
        write('vocab/' + board, b)

add_vocab_board('vocab/process-shaping.html', 'board-process-shaping.html', 'Process Shaping')
add_vocab_board('vocab/sensory-flavour.html', 'board-sensory-flavour.html', 'Sensory Flavour')
add_vocab_board('vocab/thermal-transformation.html', 'board-thermal-transformation.html', 'Thermal Transformation')

# Door Three: surface the cinnamon smoke trial; surface the cross-project hub outside Doors.
s = read('index.html')
needle = '                    <li><a href="citane-hack-gas-flame-roasted-leaf.html">Field Note: Gas-Flame Roasted Leaf</a></li>'
if 'href="cinnamon-smoke-trial.html"' not in s:
    if needle not in s: raise SystemExit('index.html: Door Three insertion point missing')
    s = s.replace(needle, needle + '\n                    <li><a href="cinnamon-smoke-trial.html">Field Trial: Cinnamon Smoke</a></li>', 1)
if 'href="projects.html"' not in s:
    marker = '            <p style="margin-top:12px;"><a href="vocab/index.html" style="color:#5a7a5a;">Buna Vocabulary — shared language for producers and café staff →</a></p>'
    if marker not in s: raise SystemExit('index.html: footer insertion point missing')
    s = s.replace(marker, marker + '\n            <p style="margin-top:12px;"><a href="projects.html" style="color:var(--accent);">KoffyKraft project landscape →</a></p>', 1)
write('index.html', s)

# Projects hub: add the actual Buna field trial so the hub has a meaningful internal Buna route.
s = read('projects.html')
if 'cinnamon-smoke-trial.html' not in s:
    marker = '</div>\n\n<div class="footer">'
    if marker not in s: raise SystemExit('projects.html: project grid close marker missing')
    card = '''\n<a class="project-card" href="cinnamon-smoke-trial.html">\n<div class="project-type">Leaf · Field Trial</div>\n<h2>Cinnamon Smoke Trial</h2>\n<p>A Buna field experiment exploring smoke as a controlled processing variable.</p>\n</a>\n'''
    s = s.replace(marker, card + '\n' + marker, 1)
write('projects.html', s)

# Archive pages: preserve content, but keep them out of canonical/current indexing.
def add_archive_meta(path, canonical):
    p = Path(path); s = p.read_text(encoding='utf-8')
    if 'name="robots" content="noindex,follow"' not in s:
        m = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        if m not in s: raise SystemExit(f'{path}: viewport meta missing')
        s = s.replace(m, m + f'\n<meta name="robots" content="noindex,follow">\n<link rel="canonical" href="{canonical}">', 1)
    p.write_text(s, encoding='utf-8')

add_archive_meta('buna-visual-guide.html', 'index.html')
add_archive_meta('assets/vocab/icon-board.html', '/vocab/index.html')

# Legacy health/function URLs: retire independent content structurally and redirect to governed Door Nine.
def redirect(path, target, title):
    Path(path).write_text(f'''<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="robots" content="noindex,follow">\n<meta http-equiv="refresh" content="0; url={target}">\n<link rel="canonical" href="{target}">\n<title>{title}</title>\n</head>\n<body>\n<h1>This legacy Buna page has moved</h1>\n<p><a href="{target}">Continue to Coffee Leaf and Human Biology</a></p>\n<script>window.location.replace('{target}');</script>\n</body>\n</html>\n''', encoding='utf-8')

redirect('coffee-leaf-health-benefits.html', 'coffee-leaf-human-biology.html', 'Coffee Leaf Health — Legacy Redirect')
redirect('functional-compendium.html', 'coffee-leaf-human-biology.html', 'Functional Compendium — Legacy Redirect')
redirect('the-buna-lifestyle-manual.html', 'coffee-leaf-human-biology.html', 'Buna Lifestyle Manual — Legacy Redirect')

print('Package 3 discoverability/classification repairs applied.')

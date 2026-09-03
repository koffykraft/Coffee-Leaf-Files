#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

changed = []

def update(path, transform):
    p = ROOT / path
    old = p.read_text(encoding='utf-8')
    new = transform(old)
    if new != old:
        p.write_text(new, encoding='utf-8')
        changed.append(path)
    return old, new

# 1. Door Eight: evidence/status placeholders are not destinations.
# Preserve the visible wording exactly; only remove false hyperlink behaviour.
vocab_files = [
    'vocab/environment-impact.html',
    'vocab/leaf-origin.html',
    'vocab/plant-care.html',
    'vocab/plant-source.html',
    'vocab/plant-variety.html',
    'vocab/process.html',
    'vocab/quality-at-source.html',
    'vocab/seasons-phenology.html',
    'vocab/sensory-flavour.html',
    'vocab/sensory-mouthfeel.html',
    'vocab/thermal-transformation.html',
]
placeholder_re = re.compile(r'<a class="term-link" href="(doc|obs|trad|hyp)">(.*?)</a>', re.S)
placeholder_count = 0
for path in vocab_files:
    def transform(text):
        global placeholder_count
        def repl(m):
            global placeholder_count
            placeholder_count += 1
            return f'<span class="term-link term-link--status" data-evidence-code="{m.group(1)}">{m.group(2)}</span>'
        return placeholder_re.sub(repl, text)
    update(path, transform)

if placeholder_count != 132:
    raise SystemExit(f'Expected 132 vocabulary placeholder links, changed {placeholder_count}. Refusing partial repair.')

# 2. Wrong relative Chemo destination inside /vocab/.
def fix_process(text):
    old = 'href="chemo-deep.html"'
    if text.count(old) != 1:
        raise SystemExit(f'Expected exactly one wrong Chemo link, found {text.count(old)}')
    return text.replace(old, 'href="../chemo-deep.html"')
update('vocab/process.html', fix_process)

# 3. Misplaced assets/vocab/icon-board.html remains available for now,
# but all of its navigation must resolve from its actual directory.
def fix_icon_board(text):
    replacements = {
        'href="vocab-style.css"': 'href="../../vocab/vocab-style.css"',
        'href="../index.html"': 'href="../../index.html"',
        'href="index.html"': 'href="../../vocab/index.html"',
        'href="plant-source.html"': 'href="../../vocab/plant-source.html"',
        'href="process.html"': 'href="../../vocab/process.html"',
        'href="sensory-flavour.html"': 'href="../../vocab/sensory-flavour.html"',
        'href="process-shaping.html"': 'href="../../vocab/process-shaping.html"',
        'href="environment-impact.html"': 'href="../../vocab/environment-impact.html"',
        'src="../buna-nav.js"': 'src="../../buna-nav.js"',
    }
    for a,b in replacements.items():
        text = text.replace(a,b)
    # Same structural treatment for the one evidence placeholder on this page.
    text, n = re.subn(r'<a class="term-link" href="obs">(.*?)</a>', r'<span class="term-link term-link--status" data-evidence-code="obs">\1</span>', text, flags=re.S)
    if n != 1:
        raise SystemExit(f'Expected one icon-board evidence placeholder, changed {n}')
    return text
update('assets/vocab/icon-board.html', fix_icon_board)

# 4. Homepage professional shortcut: use the existing, verified Catalogue research/Citane section.
def fix_home(text):
    old='catalogue.html#for-professionals'
    if text.count(old) != 1:
        raise SystemExit(f'Expected one broken professional shortcut, found {text.count(old)}')
    return text.replace(old, 'catalogue.html#citane')
update('index.html', fix_home)

# 5. Missing buna-in-kerala.html must not be invented during structural repair.
# Remove the broken navigation promise while preserving the surrounding material.
def fix_ritual(text):
    replacements = {
        '<a class="term-link" href="../buna-in-kerala.html">See Buna in Kerala — Morning Register →</a>': '<span class="term-link term-link--status">Buna in Kerala — Morning Register</span>',
        '<a class="term-link" href="../buna-in-kerala.html">See Buna in Kerala — The Kadi →</a>': '<span class="term-link term-link--status">Buna in Kerala — The Kadi</span>',
        '<a class="term-link" href="../buna-in-kerala.html">See Buna in Kerala — Workers and Athletes →</a>': '<span class="term-link term-link--status">Buna in Kerala — Workers and Athletes</span>',
        '<a class="conn-link" href="../buna-in-kerala.html">Buna in Kerala →</a>': '<span class="conn-link" aria-disabled="true">Buna in Kerala</span>',
    }
    for a,b in replacements.items():
        if text.count(a) != 1:
            raise SystemExit(f'Expected one ritual-context Kerala link: {a}')
        text=text.replace(a,b)
    return text
update('vocab/ritual-context.html', fix_ritual)

def fix_culinary_concepts(text):
    old='<a href="buna-in-kerala.html">Buna in Kerala →</a>'
    if text.count(old) != 1:
        raise SystemExit(f'Expected one culinary Kerala link, found {text.count(old)}')
    return text.replace(old, '<a href="buna-culinary.html">↑ Buna Culinary</a>')
update('buna-culinary-concepts.html', fix_culinary_concepts)

# Verification inside the executor before any commit.
all_html='\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in ROOT.rglob('*.html'))
for bad in ['href="doc"','href="obs"','href="trad"','href="hyp"','buna-in-kerala.html','catalogue.html#for-professionals']:
    if bad in all_html:
        raise SystemExit(f'Phase I residual remains after transformation: {bad}')

print('Phase I transformed files:')
for p in changed:
    print(' -', p)
print(f'Placeholder hyperlinks neutralised: {placeholder_count + 1}')

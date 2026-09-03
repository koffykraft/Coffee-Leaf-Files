from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(path, old, new, expected=None):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if expected is not None and count != expected:
        raise SystemExit(f'{path}: expected {expected} occurrences of {old!r}, found {count}')
    if count == 0:
        raise SystemExit(f'{path}: required text not found: {old!r}')
    p.write_text(text.replace(old, new), encoding='utf-8')
    print(f'{path}: replaced {count} x {old!r}')

# A. High-level cultural entry must enter each tradition through its intro.
for name in ('engere', 'kuti', 'chemo', 'kawa-daun'):
    replace_exact('begin-with-a-cup.html', f'href="{name}.html"', f'href="{name}-intro.html"', expected=1)

# B. Homepage Door Eight should have one canonical entry. Branches remain available
# inside the Vocabulary Index and Library Map, rather than acting as peer entry routes.
index = ROOT / 'index.html'
text = index.read_text(encoding='utf-8')
for line in (
    '                    <li><a href="vocab/leaf-origin.html">Leaf Origin — Ten Growth Factors</a></li>\n',
    '                    <li><a href="vocab/process.html">Process — Icon Board</a></li>\n',
    '                    <li><a href="vocab/sensory-flavour.html">Flavour &amp; Sensory</a></li>\n',
    '                    <li><a href="vocab/ritual-context.html">Ritual Context</a></li>\n',
):
    if text.count(line) != 1:
        raise SystemExit(f'index.html: expected exactly one Door Eight branch line: {line.strip()}')
    text = text.replace(line, '')
index.write_text(text, encoding='utf-8')
print('index.html: removed four deep Door Eight homepage entry routes')

# C. Logic Board contextual tradition links are external entries into those families;
# route them through canonical intro pages. Family-internal sequencing is untouched.
logic = ROOT / 'citane-logic-board.html'
text = logic.read_text(encoding='utf-8')
counts = {}
for name in ('engere', 'kuti', 'chemo', 'kawa-daun'):
    old = f'url: "{name}.html"'
    new = f'url: "{name}-intro.html"'
    count = text.count(old)
    counts[name] = count
    if count:
        text = text.replace(old, new)
if not any(counts.values()):
    raise SystemExit('citane-logic-board.html: no tradition middle-page contextual links found')
logic.write_text(text, encoding='utf-8')
print('citane-logic-board.html:', counts)

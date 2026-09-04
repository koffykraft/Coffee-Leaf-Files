from pathlib import Path

FILES = [
    'buna-culinary-school.html',
    'citane-logic-board.html',
    'citane-epsilon-board.html',
]

for path in FILES:
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    old = s
    s = s.replace('/.netlify/functions/epsilon', '/api/epsilon')
    # Remove obsolete platform wording without changing prompts or interaction copy.
    s = s.replace('Netlify function', 'Buna API')
    s = s.replace('Netlify Function', 'Buna API')
    s = s.replace('Netlify', 'Buna hosting')
    if s == old:
        raise SystemExit(f'{path}: expected legacy route/platform reference not found')
    p.write_text(s, encoding='utf-8')
    print('Updated', path)

#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
content=(ROOT/'data/buna-content.js').read_text()
claims=(ROOT/'data/buna-claims.js').read_text()
sources=(ROOT/'data/buna-sources.js').read_text()
shell=(ROOT/'index.html').read_text()
middleware=(ROOT/'functions/_middleware.js').read_text()
redirects=(ROOT/'_redirects').read_text().splitlines()

errors=[]
routes=set(re.findall(r'^"(/[^"]*)":\{', content, re.M))
expected={
'/', '/foundation/','/catalogue/','/sources/',
'/cup/','/cup/understand/','/cup/examine/',
'/traditions/','/traditions/understand/','/traditions/examine/',
'/processing/','/processing/understand/','/processing/examine/',
'/chemistry/','/chemistry/understand/','/chemistry/examine/',
'/tools/','/tools/understand/','/tools/examine/',
'/sensory/','/sensory/understand/','/sensory/examine/',
'/culinary/','/culinary/understand/','/culinary/examine/',
'/vocabulary/','/vocabulary/understand/','/vocabulary/examine/',
'/biology/','/biology/understand/','/biology/examine/','/biology/safety/'
}
if routes != expected:
    errors.append(f'Route set mismatch. missing={sorted(expected-routes)} extra={sorted(routes-expected)}')

for route in sorted(expected):
    p=ROOT/'index.html' if route=='/' else ROOT/route.strip('/')/'index.html'
    if not p.exists(): errors.append(f'Missing route file: {p.relative_to(ROOT)}')

for asset in ['assets/buna-v2.css','assets/buna-v2.js','data/buna-content.js','data/buna-claims.js','data/buna-sources.js','data/buna-terms.js']:
    if not (ROOT/asset).exists(): errors.append(f'Missing runtime asset: {asset}')

if 'buna-nav.js' in shell: errors.append('v2 shell still loads legacy buna-nav.js')
if 'HTMLRewriter' in middleware or '.append(' in middleware: errors.append('middleware still mutates HTML')

source_ids=set(re.findall(r'^\s*"([^"]+)":\{title:', sources, re.M))
claim_source_lists=re.findall(r'sources:\[([^\]]*)\]', claims)
for group in claim_source_lists:
    for sid in re.findall(r'"([^"]+)"', group):
        if sid not in source_ids: errors.append(f'Claim references missing source: {sid}')

for line in redirects:
    line=line.strip()
    if not line or line.startswith('#'): continue
    parts=line.split()
    if len(parts)<2: errors.append(f'Invalid redirect line: {line}'); continue
    target=parts[1]
    if target.startswith('/') and target.endswith('/') and target not in expected:
        errors.append(f'Redirect target is not canonical route: {target}')

# Navigation must expose all nine Doors once in the renderer source.
app=(ROOT/'assets/buna-v2.js').read_text()
for door in ['/cup/','/traditions/','/processing/','/chemistry/','/tools/','/sensory/','/culinary/','/vocabulary/','/biology/']:
    if app.count("'"+door+"'") < 1: errors.append(f'Global nav missing {door}')

print(f'canonical_routes={len(routes)} expected={len(expected)} redirects={len([x for x in redirects if x.strip()])}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PASS')

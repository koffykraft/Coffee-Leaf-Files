from pathlib import Path
p=Path('sensory-companion.html')
s=p.read_text(encoding='utf-8')
old='<a class="el-link" href="index.html"><span>The Library — all six doors</span><span class="el-arrow">→</span></a>'
new='<a class="el-link" href="index.html"><span>The Library — all nine doors</span><span class="el-arrow">→</span></a>'
if old not in s:
    raise SystemExit('Expected remaining six-door runtime link not found')
p.write_text(s.replace(old,new,1),encoding='utf-8')
print('Corrected final stale six-door runtime link.')

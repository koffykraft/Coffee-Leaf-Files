from pathlib import Path
p=Path('citane-epsilon-board.html')
s=p.read_text(encoding='utf-8')
old='https://magnificent-starlight-38c2ae.netlify.app/citane-epsilon-board.html'
new='https://buna.koffykraft.coffee/citane-epsilon-board.html'
if old not in s:
    raise SystemExit('Expected legacy hosting URL not found')
p.write_text(s.replace(old,new,1),encoding='utf-8')
print('Replaced final legacy hosting URL with canonical Buna production URL.')

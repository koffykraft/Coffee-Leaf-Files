from pathlib import Path
p=Path('data/buna-content.js')
s=p.read_text(encoding='utf-8')
needle='</tbody></table></div></section>`}\n\n"/processing/":'
if needle not in s:
    raise SystemExit('Door Two boundary not found')
s=s.replace(needle,'</tbody></table></div></section>`},\n\n"/processing/":',1)
p.write_text(s,encoding='utf-8')
print('corrected Door Two/Three object separator')

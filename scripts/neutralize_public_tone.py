from pathlib import Path

p=Path('data/buna-content.js')
s=p.read_text(encoding='utf-8')
repls={
'Three depths, one truth':'Three levels of detail',
'The deeper pages add resolution. They are not allowed to reverse or quietly strengthen what the simple page said.':'The deeper pages add context, evidence and technical detail while describing the same subject.',
'<strong>Reading rule</strong>A documented tradition remains a tradition. A laboratory result remains a laboratory result. A field observation remains an observation. A hypothesis remains a hypothesis until stronger evidence changes its status.':'<strong>How evidence is described</strong>Documented traditions, laboratory results, field observations and hypotheses are identified according to the type of evidence behind them.',
'<h2>What survives a rebuild</h2><p>We keep material that helps a reader understand the plant, the cup, the traditions, the process, the sensory experience, the kitchen or the biology. We remove duplicated explanations, competing definitions, invisible AI truth sets and pages that look more certain than their evidence.</p>':'<h2>What the Library covers</h2><p>The Library brings together the plant, the cup, traditions, processing, sensory experience, culinary use and human-biology research. Related subjects are connected so that the same idea does not need several competing explanations.</p>',
'The canonical public routes in the rebuilt Buna Library.':'The current public routes in the Buna Coffee Leaf Library.',
'<strong>Catalogue rule</strong>Only current canonical routes appear here. Legacy URLs and archived prototypes are not treated as separate knowledge pages.':'<strong>About this catalogue</strong>The catalogue lists current public pages. Older archived or prototype pages are not listed as separate knowledge pages.',
'<strong>Important</strong>A source at the bottom of a page does not automatically support every sentence above it. Claims must stay close to the source and evidence level that actually supports them.':'<strong>About source links</strong>Each source is connected to the particular findings or context for which it is relevant.',
'<strong>One useful caution</strong>There is no single universal “coffee-leaf flavour.” Plant, leaf age, processing and preparation all change the cup.':'<strong>Variation</strong>Coffee-leaf flavour varies with the plant, leaf age, processing and preparation.',
'<strong>Tradition is not treatment</strong>When people describe a drink as strengthening, warming, refreshing or restorative, the Library records those words as lived experience unless a different kind of study has measured a clinical effect.':'<strong>What the sources describe</strong>Words such as strengthening, warming, refreshing or restorative may appear in community accounts of use. Clinical effects are a separate research question and require different evidence.',
'<strong>Simple rule</strong>A process name tells you what was done. It does not by itself prove what happened chemically or what the result will do in a person.':'<strong>Process and evidence</strong>A process name describes what was done to the leaf. Chemical changes and human responses are separate questions that require their own measurements.',
'Keeping these levels separate prevents technical vocabulary from turning an experiment into a false law.':'This separation shows which parts of an experiment were measured, observed or inferred.',
'<strong>Rebuild rule</strong>Claims such as “GABA increased,” “oxidation completed,” or “safe temperature” require the corresponding measurement or a source. Visual appearance alone cannot prove them.':'<strong>Evidence and measurement</strong>Statements about GABA, oxidation or temperature effects depend on the measurements or sources available for those particular questions. Visual appearance records appearance, not the full underlying chemistry.',
'<strong>Do not skip a step</strong>“The leaf contains X” is not the same as “the cup contains X,” and neither statement means “X produces a human benefit.”':'<strong>Leaf, cup and human response</strong>A compound measured in the leaf may or may not appear in the same amount in the brewed cup. Neither measurement by itself establishes a human effect.',
'In Buna, the safest explanation distinguishes reactions measured in coffee-leaf research from mechanisms inferred from broader food science.':'Some reactions have been measured directly in coffee-leaf research, while other explanations are inferred from broader food science. The two have different evidence bases.',
'Where a connection is an inference or proposed mechanism, that status must be visible at the connection itself.':'Connections can be identified according to whether they are measured relationships, inferences or proposed mechanisms.',
'Interactive tools help you ask questions; they do not become evidence simply because they draw a map or generate an answer.':'Interactive tools provide ways to explore relationships, maps and possible interpretations. Their outputs draw on the evidence and assumptions described with each tool.',
'A tool helps explore an idea. It does not by itself prove that the idea is true.':'Tool outputs are exploratory representations; supporting evidence is shown separately where available.'
}
missing=[]
for old,new in repls.items():
    if old not in s:
        missing.append(old[:80])
    s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print(f'replacements={len(repls)-len(missing)} missing={len(missing)}')
if missing:
    print('Missing patterns:')
    for x in missing: print('-',x)

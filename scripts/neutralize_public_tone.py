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
'A tool helps explore an idea. It does not by itself prove that the idea is true.':'Tool outputs are exploratory representations; supporting evidence is shown separately where available.',
'What should we preserve when we explain a tradition?':'What forms part of a documented tradition?',
'Reported roles must stay reported roles; they are not automatically medicinal effects.':'The study records reported roles. Medicinal effects were not established by that study.',
'How should a processing pathway be described?':'What information describes a processing pathway?',
'What makes a field or kitchen trial credible?':'What information is available from a field or kitchen trial?',
'How should we talk about reactions without overclaiming?':'Which reactions are measured directly, and which are inferred?',
'Every line, number and recommendation in a tool rests on an assumption or evidence object.':'Lines, numbers and generated relationships in a tool depend on underlying evidence, assumptions or calculations.',
'<strong>AI rule</strong>The prompt controls behaviour. Knowledge comes from the same audited claim/source registry used by pages. AI is not allowed to carry a second hard-coded set of facts.':'<strong>AI knowledge source</strong>The prompt controls behaviour. Factual material is drawn from the same claim and source registry used by the Library pages.',
'What must be inspectable?':'What information sits behind a tool output?',
'The legacy interactive pages remain implementation references until each data relationship is migrated to this model.':'The interactive tools can show the source, scope, calculation and evidence status behind their relationships where those records are available.',
'<strong>Ordinary-reader rule</strong>Your perception is an observation. It does not need a chemical explanation before it is useful.':'<strong>Sensory observation</strong>Aroma, taste, texture and finish can be described directly from the cup. Chemical explanations are a separate layer of information.',
'Descriptors should be grounded either in published sensory work or clearly labelled direct tasting observations.':'Descriptors may come from published sensory work or from identified tasting observations.',
'A plausible compound association should not be displayed as if one molecule “causes” the entire sensory impression.':'A compound association describes one possible contribution within a mixture; sensory impressions also depend on concentration, matrix and perception.',
'<strong>Correction carried into rebuild</strong>Old statements such as taste being mapped to fixed tongue zones or an unnamed compound being “the same cooling mechanism as mint” are not admitted without appropriate evidence.':'<strong>Sensory evidence</strong>Taste is not confined to fixed tongue zones. Specific cooling mechanisms require identification and supporting evidence before they can be attributed to a coffee-leaf cup.',
'Coffee leaf can be explored in the kitchen, but a modern experiment should not be disguised as inherited tradition.':'Coffee leaf appears in documented traditions and in modern culinary experiments. These are different sources of knowledge.',
'<strong>Status matters</strong>A documented traditional preparation, a KoffyKraft trial, a reconstruction and an untested idea are four different things.':'<strong>Preparation context</strong>A documented traditional preparation, a recorded KoffyKraft trial, a reconstruction and an untested concept describe different kinds of material.',
'Methods are easier to learn when the page says what was actually tried and what remains an idea.':'Methods can be described by separating what was documented or tried from what remains a proposed idea.',
'Advanced culinary pages should be reproducible records, and the Kitchen Companion must use the same audited knowledge as the public text.':'Advanced culinary records can include reproducible details, while the Kitchen Companion draws factual material from the same shared knowledge records as the public text.',
'<strong>Prompt audit</strong>The old Kitchen Companion contained stronger claims than the visible culinary essays. Those hidden claims are not admitted into the rebuilt knowledge layer.':'<strong>Kitchen Companion knowledge</strong>The Kitchen Companion uses the shared Library knowledge records rather than a separate set of factual claims.',
'How should definitions work across the Library?':'How are definitions shared across the Library?',
'Each term has one canonical plain definition. Other pages may explain it briefly in context, but they should not maintain their own competing definition.':'Each term has one shared plain definition. Other pages may explain the term briefly in context and link back to that definition.',
'<strong>Category correction</strong>Farm-management doctrine, processing frameworks and proposed ritual-use categories are not vocabulary merely because they were once presented as term cards.':'<strong>Scope of the vocabulary</strong>The vocabulary contains definitions. Farm-management frameworks, processing models and proposed use categories belong with the subjects they describe.',
'Those stages should not be collapsed.':'Each stage answers a different question and may use a different kind of measurement.',
'<strong>Door Nine rule</strong>No result is promoted above the level where it was observed. A mouse result stays a mouse result. A traditional report stays a traditional report.':'<strong>Evidence levels</strong>Animal studies, human studies, laboratory measurements and traditional reports represent different kinds of evidence.',
'What should a producer or reader ask?':'What information affects safety and exposure?',
'<strong>Define the material</strong>':'<strong>Material</strong>',
'<strong>Define the process</strong>':'<strong>Process</strong>',
'<strong>Define the serving</strong>':'<strong>Serving</strong>',
'<strong>Measure what matters</strong>':'<strong>Measurements</strong>',
'<strong>Do not borrow safety</strong>A low caffeine value or safety result from one product should not be silently transferred to another cultivar, extract or brew strength.':'<strong>Product-specific safety</strong>Caffeine and other safety measurements can vary between cultivars, extracts, processing methods and brew strengths.',
'The strongest current story is not a list of benefits. It is a chain of increasingly specific research questions.':'Current research spans composition, laboratory models, animal studies and a smaller amount of human work.',
'What does current research suggest, without turning it into a treatment claim?':'What has current research measured?',
'What does a measured compound in a leaf tell us about a cup?':'How does a leaf measurement relate to the brewed cup?'
}
changed=0
for old,new in repls.items():
    if old in s:
        s=s.replace(old,new)
        changed+=1
p.write_text(s,encoding='utf-8')
print(f'replacements_applied={changed}')

from pathlib import Path

files=[Path('data/buna-content.js'),Path('data/buna-claims.js')]
repls={
'Understand compounds and reactions without pretending a model is a law.':'Explore compounds, reactions and research models inside the leaf.',
'You do not need to learn chemistry before tasting it. Start by noticing aroma, bitterness, sweetness, body and finish.':'Aroma, bitterness, sweetness, body and finish are simple ways to describe a cup.',
'The Library treats coffee leaf as its own subject. It does not assume that rules from coffee beans, tea leaves, herbal medicine or supplements automatically transfer.':'The Library treats coffee leaf as its own subject. Findings from coffee beans, Camellia tea, herbal products or supplements are related evidence only when their relevance to coffee leaf is established.',
'The current public routes in the Buna Coffee Leaf Library.':'A complete map of the pages available in the Buna Coffee Leaf Library.',
'<strong>About this catalogue</strong>The catalogue lists current public pages. Older archived or prototype pages are not listed as separate knowledge pages.':'<strong>About this catalogue</strong>The catalogue lists the pages available for reading in the Library.',
'eye:"Evidence registry",lead:"Research and regulatory sources are stored once and reused by pages, tools and explanations."':'eye:"Research and references",lead:"Research and regulatory sources used across the Library are listed here."',
'Kuti is associated in the Library source corpus with Harari coffee-leaf practice in eastern Ethiopia.':'Kuti is associated with Harari coffee-leaf practice in eastern Ethiopia.',
'The present evidence base used here is less complete than the recent Engere, Chemo and Kawa Daun studies. Detailed caffeine values, child-safety statements and fixed recipe rules are therefore not included as general facts.':'Published documentation available for detailed Kuti preparation and composition is more limited than for the recent Engere, Chemo and Kawa Daun studies. Exact caffeine values, child-safety conclusions and fixed preparation rules are not established by the sources represented here.',
'Legacy Buna material connects Kuti with Harar, household coffee practice and the use of mature or fallen leaves. It also contains stronger historical, caffeine and health statements whose source basis is not sufficiently resolved for public factual use.':'Accounts connect Kuti with Harar, household coffee practice and the use of mature or fallen leaves. Precise historical chronology, caffeine values and physiological claims require stronger source support than these accounts provide.',
'This page therefore keeps the cultural identity and preparation category visible while leaving precise chronology, physiological explanations and safety claims to source-level research.':'The cultural identity and preparation category are described separately from unresolved chronology, physiological explanations and safety questions.',
'The advanced Kuti view makes the evidence gaps visible rather than filling them with inherited certainty.':'The available Kuti evidence is uneven across cultural context, preparation, composition and safety questions.',
'Which details still depend on stronger source resolution?':'What evidence is available for the main Kuti questions?',
'<th>Current position</th>':'<th>Evidence available</th>',
'Retained as the core cultural identification in the source corpus.':'Accounts consistently associate Kuti with Harari coffee-leaf practice.',
'No general value admitted.':'No general value is established by the sources represented here.',
'No Kuti-specific mechanism admitted.':'No Kuti-specific mechanism is established by the sources represented here.',
'Kuti is associated in the Library source corpus with Harari coffee-leaf practice, while several detailed legacy claims lack a resolved primary-source basis.':'Kuti is associated with Harari coffee-leaf practice, while detailed evidence for several preparation, composition and safety claims remains limited.',
'Exact caffeine values, child-safety statements, fixed preparation rules and long historical chronologies are not used as admitted facts here.':'Exact caffeine values, child-safety conclusions, fixed preparation rules and long historical chronologies require stronger source support.'
}
for p in files:
    s=p.read_text(encoding='utf-8')
    changed=0
    for old,new in repls.items():
        if old in s:
            s=s.replace(old,new)
            changed+=1
    p.write_text(s,encoding='utf-8')
    print(p,changed)

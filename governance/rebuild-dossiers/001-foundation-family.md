# Rebuild Dossier 001 — Foundation Family

Pages reviewed:
- `index.html`
- `the-foliage-of-buna.html`
- `foliage-of-buna.html`
- `the-foliage-of-buna-minimal.html`
- `catalogue.html`

Audit state: FOUNDATION FAMILY REVIEWED — VALIDITY ITEMS STILL OPEN

## 1. What this family is supposed to do

The rebuilt site needs three distinct entry functions, not five competing entry experiences:

1. **Home / Library entrance** — explains what Buna is and offers clear reader routes.
2. **Foundation** — explains why coffee leaf matters, the scope of the library, the evidence discipline, and the minimum historical/cultural context required before deeper reading.
3. **Catalogue / index** — complete, low-rhetoric inventory for readers who already know what they want.

The current family blurs these functions.

## 2. `index.html` — intended role and disposition

### Intended role

Primary public entrance to the library.

### What it currently does

- headline introduction;
- nine Door cards;
- professional/research shortcut;
- selected deep links inside Door cards;
- a second route to the Catalogue;
- selected direct links to Vocabulary and Projects;
- broad claims about source handling and overclaiming.

### Strengths to preserve

- simple plain-language headline;
- visual Door grouping gives a useful mental model;
- multiple reader types are acknowledged;
- mobile card layout is relatively understandable.

### Problems

- It behaves simultaneously as homepage, Door map, mini-Catalogue and professional shortcut page.
- Door cards contain uneven levels of depth: some Doors expose only their landing page, others expose deep pages directly.
- Door Two includes the Foundation page even though the Foundation is not logically a tradition.
- Door Four claims to be the research foundation but also points back to Foundation evidence rules.
- Door Five describes tools as "AI-generated speculative routes" — this is a message-engine claim requiring exact tool-by-tool classification.
- The footer statement "Nothing is overclaimed" is not a defensible site-level promise until the validity/honesty audit is complete.
- Direct links to Projects and Vocabulary compete with the Door hierarchy.

### Rebuild disposition

**REWRITE AS HOME / LIBRARY ENTRANCE.**

Target job:
- explain Buna in one sentence;
- offer 3–5 reader journeys;
- show the top-level knowledge architecture;
- offer one clear route to Foundation and one to Catalogue;
- do not duplicate full Catalogue detail.

## 3. `the-foliage-of-buna.html` — intended role and disposition

### Intended role

Canonical Foundation essay.

### Strengths to preserve

- current language is materially more cautious than the archived variants;
- useful distinction between evidence, interpretation, observation and hypothesis;
- disputed Kaffa etymology is presented as disputed rather than asserted;
- "overshadowed, not erased" is more honest than the older historical-erasure framing;
- cultural practice is separated from proof of effect;
- the page attempts to orient readers before they enter traditions, research and experiments.

### Problems

#### Purpose repetition

Purpose is explained three times:
- opening purpose paragraphs;
- Reading Rule box;
- What This Page Is For box.

Disposition: **MERGE** into one concise Foundation purpose section plus one evidence-rule block.

#### Navigation duplication

The page currently contains:
- Back to Buna Library;
- sticky local nav with another Library link;
- injected global Buna navigation;
- a later embedded Library Map.

Disposition: **REBUILD** with:
- one global navigation;
- optional lightweight local section index;
- no second full Library Map inside the essay;
- a short Where Next block at the end.

#### Content architecture

History, culture, ethnobotany, evidence discipline and site navigation are bundled together. The Foundation should keep only the amount of each necessary to orient the reader. Detailed tradition material should live in tradition pages; site-map detail belongs in Catalogue/navigation.

#### Validity/message-engine items still requiring source verification

- "overshadowed, not erased" — likely useful editorial synthesis but must be identified as synthesis unless sources directly support it;
- explanation that leaves remained local because they were perishable / less suited to export — plausible interpretation requiring evidence calibration;
- naming/etymology history;
- statements about native range and whole-plant use;
- all numbered support lists must be mapped proposition-by-proposition to bibliography entries.

### Rebuild disposition

**KEEP CORE + REWRITE ARCHITECTURE + SOURCE-VERIFY CLAIMS.**

## 4. `foliage-of-buna.html` — archive role

### Current state

Already marked `noindex,follow` and canonicalized to `the-foliage-of-buna.html`.

### Meaning

This is not merely a duplicate file. It is a prior Foundation architecture with:
- larger table of contents;
- multi-part structure;
- more extensive explanatory apparatus;
- older visual system.

### Rebuild disposition

**ARCHIVE / SOURCE MINING ONLY.**

Before retirement, extract any unique factual material, useful diagrams, source references or explanations not present in the canonical Foundation. Do not restore its navigation or page architecture.

## 5. `the-foliage-of-buna-minimal.html` — archive with high message risk

### Current state

Marked `noindex,follow` and canonicalized to the current Foundation.

### Important finding

This version contains substantially stronger historical and medical claims than the current Foundation, including assertions that:

- coffee leaf knowledge was "deliberately erased from global knowledge";
- "The word coffee is geographically wrong";
- merchants confused Kaffa with the plant name;
- Ethiopian populations used Buna as the plant's "true designation";
- Al-Razi classified Buna as a pharmaceutical and used it clinically;
- traditional practice "always knew" things later verified scientifically.

These claims are not safe to inherit into the rebuild merely because they are eloquent or older.

### Rebuild disposition

**ARCHIVE — CLAIM QUARANTINE.**

Every unique proposition from this file must be independently source-verified before reuse. Default disposition for its rhetoric is **DO NOT CARRY FORWARD** unless verified and rewritten with appropriate certainty.

## 6. `catalogue.html` — intended role and disposition

### Intended role

Complete inventory / professional index of the current library.

### What it currently does

- full hero introduction;
- source taxonomy;
- Foundation section;
- reference section;
- traditions;
- guides;
- Citane research;
- tools;
- culinary material;
- its own sticky site navigation;
- runtime-injected global navigation.

### Strengths to preserve

- cards can work well for an index;
- professional readers benefit from a comprehensive inventory;
- source taxonomy is useful if made precise;
- a Catalogue is a legitimate separate page from the public homepage.

### Problems

- It partially duplicates the homepage's job.
- It contains its own global header/nav while shared nav is injected, creating the same class of duplication seen on the Foundation page.
- "For a gentler starting point, visit index.html — Begin With a Cup" confuses the homepage with the `begin-with-a-cup.html` page.
- Its taxonomy reflects earlier generations of the library rather than a derived final architecture.
- Source labels such as "Citane Research & Trials" need precise distinction between internal framework, experiment, hypothesis and externally validated research.

### Rebuild disposition

**KEEP FUNCTION / REBUILD CONTENT MODEL.**

The future Catalogue should be generated from or governed by the canonical content inventory, not manually become a second architecture.

## 7. Foundation-family reconstruction model

The rebuild should separate these roles:

### A. Home

Purpose: orientation by reader intent.

Contains:
- what Buna is;
- why the library exists;
- reader routes;
- top-level domains;
- Foundation link;
- Catalogue link.

Does not contain:
- detailed source taxonomy;
- full page inventory;
- embedded bibliography;
- deep links across every branch.

### B. Foundation

Purpose: establish context and reading discipline.

Contains:
1. what coffee leaf is;
2. why it deserves study;
3. short historical/cultural orientation;
4. evidence/claim discipline;
5. how the library distinguishes tradition, research, observation, interpretation and hypothesis;
6. where to go next.

### C. Catalogue

Purpose: complete index.

Contains:
- current canonical pages only;
- grouped by final knowledge architecture;
- concise descriptions;
- evidence/source type metadata where helpful;
- no competing global navigation architecture.

### D. Archives

Old Foundation variants remain preserved outside normal navigation until all unique material has been mined and classified.

## 8. Message-engine rules derived from this family

1. Stronger rhetoric never outranks better-supported wording.
2. Historical interpretation must be visibly distinguished from documented fact.
3. "Traditional knowledge" must not be converted into proof of physiological effect.
4. Site-level promises such as "Nothing is overclaimed" are prohibited until the audit can actually establish them.
5. Source taxonomy must distinguish external peer-reviewed research from internal Citane observation/hypothesis.
6. Navigation copy must not make knowledge claims that exceed the pages it points to.

## 9. What survives a rebuild

### Survives conceptually

- Buna Library identity;
- Foundation concept;
- Door/domain mental map if later whole-library synthesis still supports it;
- evidence-discipline concept;
- professional Catalogue;
- cautious current Foundation wording where source verification succeeds;
- useful unique archival source material after verification.

### Does not survive automatically

- present nine-Door arrangement;
- duplicated nav bars;
- embedded Foundation Library Map;
- old Foundation rhetoric;
- manual Catalogue taxonomy;
- claims of deliberate erasure, true naming, medieval pharmaceutical use or scientific validation of traditional knowledge without direct evidence review;
- site-wide promise that nothing is overclaimed.

## 10. Next audit dependency

Before the Foundation is content-approved, complete a source-to-claim verification of every numbered Foundation reference. That belongs to the validity/honesty vertical and will be carried into the final whole-library synthesis.

Next family to audit: **Door Two — Living Traditions**, beginning with the canonical entry sequence for Engere, Kuti, Chemo and Kawa Daun and comparing their intro / fascination / deep / recipe / schoolbook / pictogram variants.
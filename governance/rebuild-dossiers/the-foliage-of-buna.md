# Reconstruction Dossier — The Foliage of Buna

Page: `the-foliage-of-buna.html`
Current role: Foundation / orientation page
Audit state: IN PROGRESS — structural, contextual and navigation pass started; sentence-level source validation still open.

## 1. Intended reader outcome

The page itself states that it is the Foundation page and should orient a reader before traditions, research and experimentation. That is the correct high-level role.

A rebuilt version should leave a lay reader able to answer:

1. What is Buna in this library?
2. Why study coffee leaves as part of the coffee plant story?
3. What is known historically and ethnobotanically?
4. How does this library distinguish tradition, observation, experiment and published evidence?
5. Where should the reader go next?

The page should not also try to become a second Catalogue or a duplicate Library Map.

## 2. Current content map

Current visible architecture includes:

- Back to Buna Library control
- H1 / subtitle / metadata
- sticky local navigation
- Purpose
- History
- Culture
- Ethnobotany
- Evidence
- Navigating the Library
- Sources
- a page-level Library map

This is too many orientation mechanisms for a Foundation page once the global Buna Library navigation is also injected by middleware.

## 3. Content findings so far

### Purpose

The opening correctly frames coffee leaf as traditional food/beverage material, research subject and household knowledge.

However, three adjacent constructs repeat the page's purpose:

- opening explanatory paragraphs;
- Reading Rule box;
- What This Page Is For evidence box.

The rebuilt page should state its purpose once, then state the evidence-reading rule separately and briefly.

### History

The current history section deliberately avoids the simplistic claim that coffee derives directly from Kaffa and labels that etymology as debated. That is an appropriate honesty pattern and should survive if confirmed by the bibliography.

The phrase "overshadowed, not erased" is a useful editorial distinction but is interpretive. In the rebuilt page it should remain clearly marked as the library's framing rather than presented as a settled historical finding unless the evidence directly supports that formulation.

### Culture / ethnobotany

These sections belong on a Foundation page only at orientation depth. Detailed Engere, Kuti, Chemo and Kawa Daun descriptions should live in their canonical tradition pages, with Foundation explaining why household and cultural context matters.

### Evidence

A Foundation page does need an evidence-reading framework. That function is central and should survive the rebuild.

The evidence framework should become a reusable site-wide component rather than being independently reinvented on multiple pages.

### Navigating the Library

The Foundation page currently contains its own library map/navigation explanation while the site also has a global Library Map and homepage/Catalogue structure. This duplicates site-level architecture.

Rebuild disposition: remove the full duplicate map from the Foundation essay. Keep a concise "Continue from here" section with a small number of canonical next choices.

## 4. Context audit

The page should be the conceptual orientation before the deeper domains.

It should not require the reader to understand Citane, the tradition families or Door numbering before arriving.

Likely context sequence in the rebuilt library:

`Library home → Foundation → choose a knowledge domain / tradition / process / sensory / biology path`

The current page mixes orientation with navigation mechanics and therefore partly competes with the Library shell.

## 5. Message-engine audit — preliminary

Patterns worth preserving:

- explicit distinction between direct evidence and interpretation;
- caution around disputed etymology;
- refusal to convert traditional use into therapeutic advice;
- explicit separation of traditions, research and experiments.

Patterns requiring source-by-source verification:

- claims about coffee's linguistic history;
- geographic/native-range wording;
- explanation of why leaf use remained less visible;
- statements about household/local use and export suitability;
- any claims that specific traditions are historically continuous, representative or widespread;
- every numbered support note `[n]` against the bibliography.

No sentence-level validity sign-off is given yet.

## 6. Page architecture findings

Current page has at least three overlapping navigation/orientation mechanisms before ordinary reading:

1. Back to Buna Library;
2. sticky local subnavigation containing a Library link;
3. injected global Buna Library / Library Map navigation.

It also contains a fourth orientation mechanism later: its own Library map.

This should be rebuilt as:

- one global site navigation;
- one Foundation identity/header;
- optional compact local section index if the essay remains long;
- essay/content;
- one concise "Where next" section;
- bibliography.

The local section index must not contain another Library/Home control.

## 7. Visual and interaction audit

Observed mobile defect:

- local dark sticky subnav and injected dark global nav stack vertically;
- the page header also contains a Back to Library control;
- the combined navigation consumes excessive vertical space and visually interrupts the essay.

The local section index currently scrolls horizontally on mobile. That is usable mechanically but poor for a Foundation essay, particularly when another navigation system sits immediately below it.

Rebuild direction:

- global navigation remains the only dark site bar;
- local essay index should be visually subordinate, non-sticky on small screens or collapsed into a simple "On this page" control;
- typography and cream/ink character may survive if validated in the broader visual synthesis.

## 8. Navigation and indexing audit

Functions currently conflated:

- Back to Library = parent navigation;
- Library item in subnav = parent navigation again;
- injected Buna Library = parent/global navigation again;
- Library Map = global structural navigation;
- Purpose/History/etc. = local section index.

Only the last function is genuinely page-specific.

Provisional disposition:

- REMOVE redundant header Back link in rebuilt shell;
- REMOVE Library link from local section index;
- KEEP a local section index only if justified by final essay length;
- REMOVE embedded duplicate Library map;
- KEEP one concise contextual next-step block.

## 9. Bibliography and citation audit

The page uses numbered support notes such as `[1]`, `[2]`, etc. These must be checked one by one against the Sources section.

Required later pass:

- map every numbered support note to exact claim(s);
- confirm source existence and canonical link;
- confirm source actually supports the proposition;
- distinguish primary source, review, ethnography and library interpretation;
- identify unused bibliography entries;
- move citations closer to specific claims where a broad support note obscures provenance.

Status: NOT YET COMPLETE.

## 10. Cross-library comparison

Known duplication targets to compare during synthesis:

- `index.html` Library orientation;
- `catalogue.html` library map/catalogue function;
- `begin-with-a-cup.html` introductory orientation;
- tradition intro pages;
- evidence explanations elsewhere, especially Door Nine and Citane pages;
- alternate Foliage versions preserved as archive/canonical variants.

## 11. Rebuild disposition — provisional

- Foundation role: KEEP
- Current essay: KEEP WITH EDIT / REWRITE in parts
- Evidence-reading principle: KEEP and promote to reusable site component
- History overview: KEEP WITH SOURCE VERIFICATION
- Culture/ethnobotany overview: KEEP but compress to orientation depth
- Full embedded Library map: REMOVE from essay / replace with contextual next steps
- Repeated Back/Library controls: REMOVE
- Sticky horizontal section nav on mobile: REDESIGN
- Sources: KEEP, rebuild citation mapping

## 12. Proposed rebuilt page skeleton

1. **The Foliage of Buna** — what this Foundation is
2. **The coffee plant beyond the bean** — concise historical/ecological orientation
3. **Leaves in household and cultural use** — why context matters
4. **How Buna treats evidence** — tradition / observation / experiment / published research
5. **What this Foundation does not claim** — uncertainty and scope
6. **Where to continue** — a small number of canonical paths
7. **Sources** — claim-linked bibliography

## Acceptance

This dossier is not complete until every substantive sentence and every citation in the current page has been checked against its evidence and assigned a final rebuild disposition.

# Buna Stage 0 Structural Baseline

Baseline production commit: `17b97cc3c600c2391141380206da095a6d0f284d`
Audit date: 3 September 2026

## Scope

The baseline audit covers all 91 HTML pages in the repository, including all nine Doors, Catalogue, vocabulary pages and boards, tradition page families, Citane tools and experiments, companions, redirects, project pages, and legacy pages.

## Baseline machine totals

- HTML pages: 91
- Internal link edges examined: 997
- Broken internal-link instances: 156
- Missing fragment targets: 1
- Duplicate same-page target groups: 167
- Zero-incoming HTML pages: 19
- Exactly-one-incoming HTML pages: 6
- HTML references detected in JavaScript: 57
- Broken JavaScript HTML references: 0
- Shared navigation targets: 41
- Potential hierarchy bypasses: 8

These numbers are a baseline, not an acceptance threshold. Many repeated broken instances arise from a few systemic defects and many duplicate-target groups are intentional.

## Baseline defect families

### Content-governance risk to isolate before ordinary navigation work

- `functional-compendium.html`
- `the-buna-lifestyle-manual.html`

These remain directly addressable despite being orphaned and contain language that conflicts with the evidence discipline now used in Door Nine. Structural handling must not silently certify or preserve those claims as valid.

### Broken navigation families

- Door Eight evidence/status placeholders coded as links to nonexistent `doc`, `obs`, `trad`, and `hyp` destinations.
- Misplaced `assets/vocab/icon-board.html` with broken relative paths.
- Missing intended destination `buna-in-kerala.html` referenced from multiple places.
- One wrong relative Chemo link from inside Vocabulary.
- Homepage link to missing Catalogue fragment `#for-professionals`.

### Hierarchy defects

- `begin-with-a-cup.html` bypasses the four tradition intro pages.
- Numerous tradition/sensory pages use `visitor-lounge.html` as a Library link even though it is only an immediate redirect.
- Homepage Door Eight deep links weaken the Vocabulary Index as canonical entry.
- Some tool contextual links enter tradition middle pages rather than canonical intros.

### Discoverability defects

Nineteen pages have zero incoming HTML links. They include a mixture of:

- useful but hidden tradition guides and visual resources;
- hidden Door Three experiment material;
- orphaned Vocabulary boards;
- compatibility/legacy pages;
- duplicate or alternate Foundation pages;
- risky obsolete health/lifestyle material.

No zero-incoming page will be surfaced or deleted until classified.

### Structural shell defects

- Catalogue document title is wrong.
- Catalogue does not yet represent the complete nine-Door structure.
- Old Catalogue header survives in source and is corrected only at runtime.
- Homepage and Terrain Map lack a proper semantic H1 in the audited source.
- Sensory Companion contains stale six-Door wording.
- Several interactive pages still call a Netlify-shaped endpoint despite Cloudflare serving the site.
- `visitor-lounge.html` is a meta-refresh redirect still used as an ordinary destination.

## Acceptance discipline

After every correction unit, compare both full examination results against the immediately previous accepted state, not only against this baseline.

No stage may hide a defect by removing it from the audit scope.

The final structural audit will compare the repaired system back to this Stage 0 baseline and account for every defect family as REPAIRED, INTENTIONAL, REDIRECTED, ARCHIVED, RETIRED, or DEFERRED WITH REASON.

## Separate later content audit

This baseline does not judge the validity or honesty of all Buna material. That remains a separate audit after structural repair is complete.
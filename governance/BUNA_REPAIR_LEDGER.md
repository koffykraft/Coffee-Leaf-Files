# Buna Structural Repair Ledger

Opened: 3 September 2026
Branch: `buna-structural-repair`
Baseline production commit: `17b97cc3c600c2391141380206da095a6d0f284d`

This ledger is the control record for the structural repair. Every correction unit must be entered here before it is considered complete.

## Required entry format

For every correction unit record:

- Stage / unit
- Exact defect being corrected
- Files changed
- Canonical behaviour intended
- Candidate commit SHA
- Examination 1 result
- Examination 1 audit artifact / notes
- Examination 2 result
- Examination 2 hierarchy / navigation notes
- New defects introduced: yes / no
- Final disposition: PASS / FAIL / REVERT / DEFER
- Production merge/deploy commit, when applicable

## Stage 0 - Control and baseline

Status: IMPLEMENTED

Actions:

- Production baseline fixed at `17b97cc3c600c2391141380206da095a6d0f284d`.
- Dedicated repair branch created: `buna-structural-repair`.
- Full-site audit tooling carried onto the repair branch.
- Two-examination rule made mandatory after every correction unit.
- Stop rule established: no next correction until both full examinations pass.
- Final full-system structural audit reserved.
- Separate later validity and honesty audit explicitly reserved.

No production page content or navigation was changed in Stage 0.

## Baseline defect families

The baseline audit identified these main structural families for later staged repair:

1. Unsafe or conflicting legacy health/lifestyle pages.
2. Door Eight evidence/status placeholders implemented as broken links.
3. Missing or unresolved structural destination `buna-in-kerala.html`.
4. Broken homepage fragment and stale site-shell details.
5. Indirect navigation through `visitor-lounge.html`.
6. Canonical-entry bypasses in `begin-with-a-cup.html` and some contextual links.
7. Zero-incoming and effectively orphaned pages requiring classification.
8. Incomplete Door-level inventories and incomplete Catalogue coverage.
9. Duplicate/alternate Foundation and vocabulary working pages.
10. Legacy Netlify-shaped API routes and runtime compatibility debt.
11. Source-level header/navigation patch debt.
12. Accessibility / structural heading defects and stale wording.

## Phase I - Immediate integrity defects

Status: COMPLETE — PASS

### Work performed

- repaired homepage broken Catalogue fragment by routing the professional shortcut to existing `catalogue.html#citane`;
- converted 133 Door Eight `doc / obs / trad / hyp` pseudo-destination anchors into non-clickable status spans without assigning new evidence meaning;
- corrected the wrong relative Chemo Deep destination in `vocab/process.html`;
- repaired all internal relative paths in `assets/vocab/icon-board.html` while leaving its orphan/retirement decision to the later classification phase;
- investigated `buna-in-kerala.html` references and confirmed that no static page exists;
- did not invent a Kerala page from Kitchen Companion prompt material;
- removed the broken Kerala destination promises and returned Culinary Concepts to its existing Buna Culinary parent.

### Candidate site commit

`e9e7a4fea25b39a7f784d12bae12a4acd116b914`

### Examination 1

PASS — full 91-page structural audit from a fresh checkout.

Results:

- broken internal links: 0
- missing fragments: 0
- broken JavaScript HTML references: 0
- zero-incoming pages: 19 (unchanged from baseline)
- one-incoming pages: 6 (unchanged)
- hierarchy bypasses: 8 (unchanged; reserved for later phase)

Baseline comparison:

- broken internal links: 156 -> 0
- missing fragments: 1 -> 0

### Examination 2

PASS — independent full-site repeat plus hierarchy/navigation review.

Confirmed:

- no Phase I target remains broken;
- no invented substitute page was introduced;
- no new orphan was created;
- no new hierarchy bypass was introduced;
- later-phase defects remained visible rather than being hidden by Phase I.

### Revert decision

Revert: NO.

Reason: both examinations passed. Reversion would restore verified defects.

### Remaining Phase I work

NONE.

All remaining structural findings belong to later phases and remain explicitly open.

Final disposition: PASS.

## Repair stages

Later stages will be entered below only when begun. Each stage may contain multiple correction units, but every unit must independently pass Examination 1 and Examination 2 before the next unit starts.

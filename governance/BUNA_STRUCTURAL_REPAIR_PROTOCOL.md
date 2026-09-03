# Buna Coffee Leaf Library Structural Repair Protocol

Status: ACTIVE
Established: 3 September 2026
Working branch: `buna-structural-repair`
Production baseline commit: `17b97cc3c600c2391141380206da095a6d0f284d`

## Purpose

Repair the Buna Coffee Leaf Library structure, navigation, internal links, hierarchy, discoverability and site shell without silently changing the substance of the library.

The structural repair is separate from the later validity and honesty audit of the material itself.

## Non-negotiable rules

1. Production is not edited casually during the repair process. Work is prepared on the structural repair branch and promoted only after the required inspections pass.
2. One correction unit at a time. A correction unit may contain several file edits only when they are one inseparable structural defect.
3. Structural work must not rewrite research conclusions, historical claims, health claims, recipes, observations or interpretations unless the correction is required to prevent an unsafe or misleading legacy page from competing with the governed material. Such cases must be recorded separately.
4. No page is deleted merely because it is old, duplicated, hidden or awkward. Its status must first be classified as CURRENT, LEGACY REDIRECT, ARCHIVE, REPAIR, SURFACE, or RETIRE.
5. High-level navigation must enter through canonical Door or family entry pages. Deep cross-links are allowed only when they serve a clear contextual purpose.
6. Redirect and compatibility pages must never be ordinary navigation destinations.
7. Every current published page must have a canonical parent. Deep/current pages should also have an appropriate local return path or related-page route.
8. Evidence labels are not links unless a real evidence/source destination exists.
9. The Catalogue must eventually represent the complete current library structure, including all nine Doors.
10. Nothing is called complete until both required full examinations pass.

## Required examination protocol after EVERY correction unit

Every correction unit is followed by two separate full examinations of the site.

### Examination 1 - Full structural machine examination

Run from a clean checkout of the candidate commit.

It must inspect the entire site, not only changed files, including:

- every HTML page
- all internal href targets
- all fragment targets
- HTML destinations referenced from JavaScript
- incoming and outgoing link counts
- zero-incoming and one-incoming pages
- repeated link destinations
- canonical-entry hierarchy bypasses
- title and H1 structure
- stale navigation wording
- redirect destinations
- global navigation targets

The result is recorded against the exact commit SHA.

### Examination 2 - Full navigation and hierarchy examination

Run again against the same candidate commit after Examination 1.

This is a separate inspection and must verify the entire site as a navigable system:

- all nine Doors are represented correctly
- every Door has a canonical entry
- every current page is reachable through an intentional path
- no page depends on an accidental or indirect route
- no high-level page bypasses a required intro/parent page
- no redirect page is used as a normal navigation destination
- local previous/next/back/breadcrumb links preserve hierarchy
- the Library Map and Catalogue do not contradict each other
- mobile navigation remains usable
- no correction introduced a new orphan, duplicate route, or dead end elsewhere

A correction unit fails if either examination finds a new unintended defect.

## Stop rule

If Examination 1 or Examination 2 fails:

- do not proceed to the next correction unit;
- record the failure in the repair ledger;
- repair or revert the correction;
- repeat BOTH full examinations.

Passing one examination never substitutes for the other.

## Baseline

The structural baseline is the production repository at commit:

`17b97cc3c600c2391141380206da095a6d0f284d`

The baseline machine audit covers 91 HTML pages and records the defects from which improvement will be measured.

No baseline defect is silently removed from the ledger. It is either repaired, classified as intentional, or deferred with a reason.

## Final structural acceptance

After all planned structural repair stages are complete, perform a fresh full system audit from a clean checkout.

The final structural audit must include:

1. complete page inventory;
2. complete internal link graph;
3. broken target and fragment validation;
4. hierarchy and canonical-parent validation;
5. orphan and under-linked page review;
6. duplicate/legacy route review;
7. global navigation, Catalogue and Door inventory comparison;
8. desktop and mobile navigation inspection;
9. AI/helper endpoint routing review;
10. redirect and compatibility-route review;
11. title, H1, contact and stale-language review;
12. comparison against the Stage 0 baseline.

Target: zero unintended broken internal links and zero missing fragments. Any intentional legacy redirect or exceptional route must be documented.

## Reserved next audit: validity and honesty of material

Structural approval does NOT certify the truth, validity, evidence quality, balance or honesty of the content.

After structural acceptance, a separate content audit remains reserved. It will examine, among other things:

- whether claims are supported by their cited source;
- whether a source is represented at its true evidence level;
- whether human, animal, cell, laboratory, traditional, observational and hypothesis material are kept distinct;
- whether language overstates certainty or benefit;
- whether old pages conflict with newer evidence discipline;
- whether citations are complete and correctly attached to claims;
- whether historical and cultural claims are traceable;
- whether Buna/Citane observations are clearly distinguished from published research;
- whether uncertainty and disagreement are presented honestly.

No structural repair stage will be used to declare that later audit unnecessary.
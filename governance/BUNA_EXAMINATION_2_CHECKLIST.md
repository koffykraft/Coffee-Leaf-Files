# Buna Examination 2 - Full Navigation and Hierarchy Checklist

Use this checklist after every correction unit, against the same candidate commit that passed Examination 1.

This is a full-site inspection, not a changed-file review.

## A. Global library structure

- [ ] Library Map represents Doors One through Nine correctly.
- [ ] Catalogue and Library Map do not contradict one another.
- [ ] Homepage Door entries point to canonical Door/family entries.
- [ ] No obsolete Door count or stale primary navigation remains.
- [ ] No redirect/compatibility page is used as a normal navigation destination.

## B. Door-by-Door examination

For each Door One through Nine:

- [ ] canonical Door landing/entry is clear;
- [ ] every current page belonging to the Door is intentionally reachable;
- [ ] hidden resources are classified rather than accidentally orphaned;
- [ ] deep pages have a sensible return route to their family or Door;
- [ ] previous/next links follow the intended sequence;
- [ ] contextual cross-links do not replace the canonical entry route;
- [ ] no unrelated page has become an accidental parent.

## C. Pages outside Doors

- [ ] Catalogue has a defined role.
- [ ] redirects have a documented compatibility purpose.
- [ ] legacy pages are classified CURRENT / LEGACY REDIRECT / ARCHIVE / REPAIR / SURFACE / RETIRE.
- [ ] project/working pages do not form invisible islands.
- [ ] no published standalone page lacks an intentional place in the site map.

## D. Link integrity

- [ ] every internal page link resolves;
- [ ] every fragment link resolves;
- [ ] every HTML destination referenced in JavaScript resolves;
- [ ] evidence/status labels are not fake links;
- [ ] duplicate links are intentional rather than accidental navigation duplication;
- [ ] no link takes an avoidable redirect hop;
- [ ] no high-level entry bypasses a required intro/parent page.

## E. Navigation usability

- [ ] desktop navigation is coherent;
- [ ] mobile Library Map is coherent;
- [ ] local navigation does not compete with global navigation;
- [ ] no nested scroll/navigation trap has been introduced;
- [ ] no header duplication has returned;
- [ ] current location can be understood from the page.

## F. Structural page shell

- [ ] page title is correct;
- [ ] semantic H1 exists where appropriate;
- [ ] contact details are current;
- [ ] stale platform wording is absent from user-facing navigation;
- [ ] API/helper routes do not depend unnecessarily on obsolete platform names;
- [ ] no correction has broken source links or reference sections.

## G. Regression comparison

- [ ] compare current audit totals with the previous accepted correction unit;
- [ ] any increased defect count is explained and accepted or the correction fails;
- [ ] zero new unintended orphan pages;
- [ ] zero new unintended broken targets;
- [ ] zero new missing fragments;
- [ ] zero new hierarchy bypasses.

## Result record

Candidate commit:

Examination 1 result:

Examination 2 result:

New defects introduced:

Notes:

Disposition: PASS / FAIL / REVERT / DEFER

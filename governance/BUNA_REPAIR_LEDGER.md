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

## Repair stages

Later stages will be entered below only when begun. Each stage may contain multiple correction units, but every unit must independently pass Examination 1 and Examination 2 before the next unit starts.

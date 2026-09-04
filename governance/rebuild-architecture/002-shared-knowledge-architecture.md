# Buna Rebuild — Shared Knowledge Architecture

Status: ARCHITECTURE DRAFT 1

Purpose: establish one governed knowledge layer from which pages, visualisations, tools, vocabulary and AI assistants can draw.

The old site duplicated factual propositions inside HTML, JavaScript, visual boards and AI prompts. The rebuild must reverse that model.

---

## 1. Core principle

> Knowledge exists once. Presentation may exist many ways.

A proposition should not become more certain because it appears in a colourful board, a recipe card or an AI response.

---

## 2. Core object types

The minimum shared model contains six object types:

1. **Claim** — a substantive proposition.
2. **Source** — evidence/provenance.
3. **Term** — canonical vocabulary.
4. **Tradition** — stable cultural/context record.
5. **Experiment** — Buna/Citane record of something actually attempted.
6. **Page** — presentation/reader-journey object referencing the above.

Additional types should be added only when repeated use proves they are necessary.

---

## 3. Claim object

Conceptual example:

```json
{
  "id": "claim.engere.reported-strength-use",
  "statement": "Survey respondents associated Engere with perceived strength-enhancing use.",
  "plain_statement": "People in the study reported using Engere in connection with strength and recovery.",
  "type": "community-report",
  "scope": {
    "tradition": "engere",
    "population": "surveyed Gofa Zone households",
    "preparation": "Engere",
    "year": 2026
  },
  "source_ids": ["source.yohannis-2026-engere"],
  "evidence_level": "human-observational",
  "review_state": "verified",
  "limitations": [
    "Self-reported community use and experience",
    "Does not establish a physiological strength effect"
  ],
  "allowed_plain_language": "People report using Engere for strength and recovery.",
  "prohibited_upgrade": "Engere increases strength.",
  "last_reviewed": "YYYY-MM-DD"
}
```

### Required claim types

- definition/fact
- published-result
- documented-tradition
- community-report
- Buna/Citane-observation
- interpretation
- hypothesis
- recommendation
- regulatory-fact

The list may evolve, but categories must remain mutually intelligible.

---

## 4. Evidence level

Evidence level and claim type are not the same.

Example:
- `community-report` describes what kind of proposition it is;
- `human-observational` describes the evidence design.

Suggested evidence-level values:

```text
regulatory
systematic-review
review
human-intervention
human-observational
animal
cell-model
in-vitro
composition
ethnographic/documentary
Buna/Citane-measurement
Buna/Citane-observation
analogy
none-yet
```

The UI can simplify these for ordinary readers.

---

## 5. Source object

Conceptual example:

```json
{
  "id": "source.yohannis-2026-engere",
  "citation": "...",
  "title": "...",
  "year": 2026,
  "doi": "10.1007/s44187-026-00927-8",
  "source_type": "human-observational",
  "material": "coffee leaf brew and Engere",
  "population_or_model": "385 households plus focus groups",
  "location": "Gofa Zone, South Ethiopia",
  "methods_summary": "...",
  "verified": true,
  "verification_notes": "..."
}
```

The source record is where exact study scope belongs.

A page should not manually restate sample information differently each time.

---

## 6. Term object

Conceptual example:

```json
{
  "id": "term.astringency",
  "term": "Astringency",
  "plain_definition": "A drying or puckering sensation in the mouth.",
  "category": "sensory",
  "technical_definition": "...",
  "source_ids": ["..."],
  "related_terms": ["term.bitterness", "term.mouthfeel"],
  "project_specific": false,
  "review_state": "verified"
}
```

A page can display the plain definition inline and link to the canonical term detail.

---

## 7. Tradition object

A tradition record should contain stable contextual facts, not therapeutic conclusions.

Conceptual fields:

```text
id
name
region
community/context
coffee species if documented
basic preparation summary
source_ids
verified factual notes
reported-use claim_ids
preparation claim_ids
uncertainties
```

Engere, Kuti, Chemo and Kawa Daun each get one tradition object.

This prevents every page from inventing its own one-line tradition description.

---

## 8. Experiment object

Experiments must distinguish observation from explanation.

Conceptual example:

```json
{
  "id": "experiment.cinnamon-smoke.2026-xx-xx",
  "title": "Cinnamon Smoke Trial",
  "status": "completed-observational-trial",
  "question": "...",
  "material": "...",
  "setup": {...},
  "procedure": [...],
  "measurements": [...],
  "observations": [...],
  "interpretation_claim_ids": [...],
  "hypothesis_claim_ids": [...],
  "not_measured": [
    "water activity",
    "microbial population",
    "GABA",
    "Maillard markers"
  ],
  "next_question": "..."
}
```

A field-note page renders this record.

---

## 9. Page object

The page manifest records reader role and references content objects.

Conceptual example:

```json
{
  "id": "traditions.engere.look",
  "route": "/traditions/engere/",
  "title": "Engere",
  "door": "traditions",
  "depth": "look",
  "archetype": "look-page",
  "claim_ids": [
    "claim.engere.definition",
    "claim.engere.location",
    "claim.engere.milk-matrix",
    "claim.engere.reported-strength-use"
  ],
  "term_ids": ["term.decoction"],
  "source_ids": ["source.yohannis-2026-engere"]
}
```

A page is therefore a governed selection and ordering of accepted knowledge, not a private factual database.

---

## 10. Review state

Every reusable object needs a review state.

Suggested values:

```text
unreviewed
queued
source-located
verified
verified-with-limits
disputed
rejected
superseded
```

Only `verified` and `verified-with-limits` material may enter canonical reader pages unless the page explicitly presents an open hypothesis/dispute.

---

## 11. Plain-language transformation rule

The data layer should permit a verified technical claim to have an approved ordinary-reader rendering.

Example:

Technical:
`The study reported no health-related problems attributed to Engere among respondents.`

Approved plain language:
`In this survey, respondents did not report health problems linked to Engere.`

Prohibited plain-language upgrade:
`Engere is safe.`

This is an important message-engine control: simplification must not increase certainty.

---

## 12. Claim-to-source validation

Every factual claim used in canonical content must answer:

1. What is the exact proposition?
2. What source supports it?
3. What material/population/process did that source actually study?
4. Does the source support the direction and magnitude stated?
5. Is the wording stronger than the source?
6. Is a limitation required beside it?

Claims without a source may still exist as:
- Buna observation;
- interpretation;
- hypothesis;

but their type must say so.

---

## 13. Citation rendering

The page does not manually type citation numbers.

Instead:
- claim references source ID;
- page renders appropriate citation/link;
- bibliography is generated from source IDs used by the page.

This prevents citation drift.

At LOOK depth, citations may be visually quiet but accessible.
At EXAMINE depth, full provenance is explicit.

---

## 14. Evidence language by depth

### LOOK
User-facing labels:
- Research shows
- People report
- We observed
- Still uncertain

### UNDERSTAND
- Documented
- Community report
- Buna observation
- Interpretation
- Hypothesis

### EXAMINE
Full evidence type + source/method scope.

The underlying claim type remains unchanged across depths.

---

## 15. AI consumption rule

AI companions receive:
- behavioural system instruction;
- retrieved accepted claim objects;
- relevant term objects;
- source metadata where needed.

They do **not** receive an unaudited hard-coded encyclopedia prompt.

Generated suggestions are marked as generated/hypothesis, not inserted automatically into accepted claims.

---

## 16. Tool consumption rule

Tool nodes/edges/rules reference claim IDs.

Example:

```text
Terrain edge: shade → leaf temperature
claim_id: claim.environment.shade-leaf-temperature
```

If that claim is rejected or narrowed, the tool changes with it.

Numerical model weights must have their own metadata explaining whether they are:
- measured;
- estimated;
- editorial/model weight.

---

## 17. Visual-board rule

Visual boards are generated views of accepted data.

They may simplify language but may not:
- strengthen certainty;
- add a new mechanism;
- omit a limitation that materially changes meaning;
- convert a producer-specific value into a universal value.

---

## 18. Migration process for old content

For every old substantive sentence considered for migration:

1. isolate proposition(s);
2. remove rhetoric from factual proposition;
3. classify proposition type;
4. locate source/provenance;
5. verify scope;
6. create/update claim record;
7. approve plain-language form;
8. assign to depth/page;
9. retire duplicate copies.

This is how the promised word/sentence/essay audit connects to the rebuild rather than remaining a separate report.

---

## 19. Minimum first dataset

Before building representative reader pages, populate a small verified dataset sufficient for one complete vertical slice.

Recommended first slice: **Kuti or Engere** only after its highest-priority claims are verified.

Alternative low-risk slice: **Door One — Begin With a Cup**, using only broadly verified orientation claims.

The slice should include:
- 8–15 claims;
- 3–6 terms;
- 2–5 sources;
- page manifest entries for LOOK / UNDERSTAND / EXAMINE.

This tests architecture before bulk migration.

---

## 20. File/storage form

Initial implementation can remain deliberately simple and static.

Suggested repository structure:

```text
/rebuild/
    data/
        claims.json
        sources.json
        terms.json
        traditions.json
        experiments.json
        pages.json
```

If scale or editing ergonomics later justify splitting records into multiple files, that can happen without changing the conceptual model.

Do not introduce a database merely because a data model exists. Cloudflare static delivery remains sufficient for the first rebuild stage.

---

## 21. Governance rule

Any edit that changes the semantic meaning of a reusable claim requires:
- source re-check;
- affected-page lookup;
- affected-tool lookup;
- affected-AI retrieval update;
- audit record.

Presentation-only changes do not require revalidating the source unless they change likely reader interpretation.

---

## 22. Acceptance test

The knowledge architecture succeeds if:

> Correcting one claim in one place corrects every page, tool, visual and assistant that uses it — and no presentation layer can silently make that claim stronger.

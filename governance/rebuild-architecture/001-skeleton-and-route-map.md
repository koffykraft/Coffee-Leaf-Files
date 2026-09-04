# Buna Rebuild — Skeleton and Canonical Route Map

Status: ARCHITECTURE DRAFT 1 — DERIVED FROM WHOLE-LIBRARY SYNTHESIS

This document defines the empty structure of the rebuilt Buna Library before audited content is migrated into it.

The current production site remains the source corpus and compatibility surface until the rebuilt structure passes acceptance.

---

## 1. Structural hierarchy

```text
BUNA LIBRARY
│
├── Home
├── Foundation
├── Door 1 — Begin With a Cup
├── Door 2 — Living Traditions
├── Door 3 — Processing & Experiment
├── Door 4 — Inside the Leaf
├── Door 5 — Explore With Tools
├── Door 6 — Sensory School
├── Door 7 — The Leaf at the Table
├── Door 8 — Vocabulary
├── Door 9 — After the Cup
├── Catalogue
└── Sources
```

Home, Foundation, Catalogue and Sources are utility/foundation layers, not Doors.

---

## 2. Route philosophy

Canonical routes should express meaning rather than historical filenames.

Recommended route families:

```text
/
/foundation/
/start/
/traditions/
/processing/
/chemistry/
/tools/
/sensory/
/culinary/
/vocabulary/
/human-biology/
/catalogue/
/sources/
```

Existing `.html` URLs remain compatibility redirects during and after migration as appropriate.

Cloudflare Pages can serve directory `index.html` routes while preserving old URLs through explicit compatibility files or redirect rules.

---

## 3. Door One route skeleton

```text
/start/
    index.html                 LOOK — Begin with a cup
    understand/
        index.html             UNDERSTAND — Why cups vary
    evidence/
        index.html             EXAMINE — Sensory evidence gateway
```

Door One intentionally remains small.

Advanced chemistry/sensory content links to Doors Four and Six rather than duplicating them.

---

## 4. Door Two route skeleton

```text
/traditions/
    index.html                 Door landing — choose a tradition

    engere/
        index.html             LOOK — What is Engere?
        understand/
            index.html         UNDERSTAND — Engere in context
        evidence/
            index.html         EXAMINE — Evidence & sources

    kuti/
        index.html
        understand/
            index.html
        evidence/
            index.html

    chemo/
        index.html
        understand/
            index.html
        evidence/
            index.html

    kawa-daun/
        index.html
        understand/
            index.html
        evidence/
            index.html
```

Technical preparation details may live as sections within UNDERSTAND/EXAMINE unless size or reuse genuinely requires a subordinate page.

No Schoolbook or Visual Guide appears as a peer route.

---

## 5. Door Three route skeleton

```text
/processing/
    index.html                 LOOK — What processing changes
    pathways/
        index.html             UNDERSTAND — Processing pathways
    lab/
        index.html             EXAMINE/DO workspace
        compass/
            index.html         Technical Process Compass
        manual/
            index.html         Technical processing reference
        experiments/
            index.html         Experiment index
            <experiment-id>/
                index.html     Field/experiment record
```

Potential initial experiment IDs:
- grill-wilted-leaf
- gas-flame-roast
- cinnamon-smoke

Names should be neutral records, not `hack` unless that word has a deliberate editorial role.

---

## 6. Door Four route skeleton

```text
/chemistry/
    index.html                 LOOK — Inside the leaf
    changes/
        index.html             UNDERSTAND — How processing changes chemistry
    reactive-landscape/
        index.html             EXAMINE — Citane model & evidence
```

The advanced route must state explicitly that Reactive Landscape is a research-informed Citane model, not a validated unified mechanism.

---

## 7. Door Five route skeleton

```text
/tools/
    index.html                 Door landing
    terrain/
        index.html
    flavour/
        index.html
    logic/
        index.html
    epsilon/
        index.html
```

Each tool has internal transparency layers rather than separate public routes:
- Use
- Understand assumptions
- Examine logic/provenance

Tool data comes from shared accepted claim/source/term objects.

---

## 8. Door Six route skeleton

```text
/sensory/
    index.html                 Door landing / School
    notice/
        index.html             LOOK — Notice
    name/
        index.html             UNDERSTAND — Name
    explain/
        index.html             EXAMINE — Explain
    companion/
        index.html             Sensory assistant interface
```

`notice` may combine the current `You Already Sense` and `Encounter` material into a single depth while preserving good pacing internally.

---

## 9. Door Seven route skeleton

```text
/culinary/
    index.html                 LOOK — The leaf at the table
    methods/
        index.html             UNDERSTAND — Elements & methods
    kitchen/
        index.html             EXAMINE/COOK — Preparations & experiments
        preparations/
            <preparation-id>/
                index.html     Tested/reconstructed preparation record
    companion/
        index.html             Kitchen assistant
```

Preparation records must carry status:
- documented tradition;
- Buna reconstruction;
- KoffyKraft trial;
- untested concept.

Whole-leaf food records may not become ordinary instructions until safety review permits it.

---

## 10. Door Eight route skeleton

```text
/vocabulary/
    index.html                 Search + category browse
    term/
        <term-id>/
            index.html         Canonical term detail
```

Term page itself supports:
- LOOK definition;
- UNDERSTAND context;
- EXAMINE technical/source detail.

Visual/icon boards are views generated from term/category records and do not require canonical knowledge routes.

---

## 11. Door Nine route skeleton

```text
/human-biology/
    index.html                 LOOK — After the cup
    understand/
        cup-to-body/
            index.html
        gut-metabolism/
            index.html
        human-response/
            index.html
        safety/
            index.html
    evidence/
        index.html             EXAMINE — Study/source registry view
        research-gaps/
            index.html
```

Safety remains directly linked from the Door landing as well as from UNDERSTAND.

---

## 12. Foundation / Catalogue / Sources

```text
/foundation/
    index.html

/catalogue/
    index.html

/sources/
    index.html                 searchable/browseable source registry
    <source-id>/
        index.html             source detail where useful
```

Catalogue is generated from the canonical page manifest.

Sources are generated from the source registry.

---

## 13. Page manifest

The new site must have one canonical page manifest.

Conceptual structure:

```json
{
  "id": "traditions.kuti.look",
  "route": "/traditions/kuti/",
  "title": "Kuti",
  "door": "traditions",
  "depth": "look",
  "archetype": "look-page",
  "status": "draft",
  "parent": "traditions",
  "simpler": null,
  "deeper": "traditions.kuti.understand",
  "legacy_routes": ["/kuti-intro.html"]
}
```

The manifest powers:
- global Library Map;
- Catalogue;
- breadcrumbs;
- depth controls;
- canonical metadata;
- legacy redirect inventory;
- audit completeness.

Navigation must not be separately hard-coded on every page.

---

## 14. Legacy route map

Every existing reader-facing URL must be classified before launch:

```text
legacy route
→ canonical replacement
→ legacy redirect only
→ archive/no public replacement
```

Examples conceptually:

```text
/begin-with-a-cup.html
→ /start/

/engere-intro.html
→ /traditions/engere/

/engere.html
→ /traditions/engere/understand/

/engere-deep.html
→ /traditions/engere/evidence/

/visitor-lounge.html
→ /

/functional-compendium.html
→ /human-biology/
```

Exact mapping is produced during migration, not guessed en masse.

---

## 15. Public page count principle

The public Library should count canonical pages only.

Do not include:
- legacy redirects;
- archive source files;
- design prototypes;
- generated visual views unless they have genuine standalone reader value.

This prevents the rebuild from re-acquiring page inflation.

---

## 16. Navigation skeleton

Every canonical reader page gets one shared shell:

```text
[ BUNA ] [ Library Map ▾ ] [ Search ]

Door / Family
Current title
Depth indicator

CONTENT

← Simpler / Back to Door              Deeper →

Sources / context links as needed
```

Desktop and mobile share the same semantic structure.

No page-specific second global navigation bar.

---

## 17. Depth semantics

Canonical values in the manifest:

```text
look
understand
examine
```

UI labels may be contextual:

Sensory:
- Notice
- Name
- Explain

Processing:
- Look
- Understand
- Examine / Do

But internal architecture remains the same so navigation and analytics do not require a different model per Door.

---

## 18. Skeleton acceptance tests

Before content migration:

- every Door has one clear question;
- every route has a parent;
- no canonical page has two competing parents;
- every LOOK route is reachable from its Door in one action;
- every depth has an outward route;
- no visual/AI/tool creates a hidden fourth evidence hierarchy;
- Catalogue can be generated solely from manifest;
- global navigation can be generated solely from manifest;
- old 91-page corpus remains untouched as source during skeleton validation.

---

## 19. Next architecture layer

After this skeleton, define the shared data architecture for:
- claims;
- sources;
- terms;
- traditions;
- experiments;
- page-content references.

Only then build the shared shell and representative archetype pages.
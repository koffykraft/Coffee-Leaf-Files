# Buna Reconstruction Dossier — Door Three: Processing & Experiment

Audit state: DOOR REVIEW COMPLETE / VALIDITY QUEUE OPEN

Primary files reviewed:
- `citane-process-compass.html`
- `citane-processing-manual.html`
- `citane-processing-protocols.html`
- `citane-hack-grill-wilted-leaves.html`
- `citane-hack-gas-flame-roasted-leaf.html`
- `cinnamon-smoke-trial.html`

Related structural item:
- `projects.html`

## 1. Intended role

Door Three should teach a simple idea first:

> Processing changes what a coffee leaf becomes in the cup.

An ordinary reader should be able to understand that harvesting, withering, bruising/rolling, heat, oxidation/fermentation, drying, roasting and smoke can change aroma, taste, colour and extraction without first learning chemical pathways.

A processor or researcher should then be able to walk deeper into pathways, protocols, measurements, field notes and unresolved mechanisms.

Door Three must visibly distinguish published evidence from Citane's own framework and experiments.

## 2. Four evidence classes that must remain separate

### A. Published knowledge
External research or documented traditional practice with a traceable source.

### B. Citane framework
A conceptual model used to organize processing decisions. Useful, but not itself experimental proof.

### C. Citane observation / experiment
Something actually done, measured, photographed, tasted or recorded by KoffyKraft/Citane.

### D. Working hypothesis
A proposed explanation or predicted result that has not been measured in the relevant experiment.

The current Door often uses technical language in ways that allow B, C and D to sound like A. The rebuild must prevent that.

## 3. Three-depth rebuild architecture

### Level 1 — LOOK: What processing does

Purpose: ordinary-reader orientation.

Suggested content:
1. Fresh leaves can be processed in different ways.
2. Five broad actions ordinary readers can understand:
   - keep fresh / lightly heat;
   - wither;
   - bruise or roll;
   - allow time for reactions / fermentation;
   - dry / roast / smoke.
3. A simple visual showing that different sequences produce different cup character.
4. Three plain examples:
   - lightly processed → greener/fresher character;
   - more oxidation/fermentation → different aroma/body;
   - roast/smoke → toasted/smoky character.
5. One explicit note: outcomes vary by leaf, time, temperature and method.
6. Action: `Understand processing →`.

Do not include:
- reservoir models;
- exact GABA or phenolic claims;
- maturity chemistry tables;
- formal process-state labels;
- detailed protocols;
- internal Citane terminology unless explained simply.

### Level 2 — UNDERSTAND: The processing pathways

Purpose: show the main choices and why they matter.

Likely source pool:
- simplified portions of `citane-process-compass.html`;
- accessible parts of `citane-processing-manual.html`;
- selected documented traditional examples from Door Two where useful.

Suggested structure:
1. leaf condition at harvest;
2. holding / withering;
3. physical manipulation;
4. reaction window;
5. heat / drying / roasting / smoke;
6. brewing as a separate extraction step;
7. examples of pathway combinations;
8. evidence label beside each explanation.

Level 2 may show a pathway map but not a dense operating manual.

### Level 3 — EXAMINE / DO: protocols, experiments and evidence

Purpose: serious processing work.

May contain:
- full Citane Process Compass tables;
- Paper II detailed processing manual;
- Paper III experimental pathways;
- batch sheets;
- exact parameters;
- field observations;
- photographs;
- measurements;
- sensory records;
- failures;
- hypotheses;
- source citations;
- experiment status.

Critical requirement: every technical proposition identifies its evidence class.

## 4. `citane-process-compass.html`

### Strengths
- stage-based processing map is useful;
- explicitly contains an evidence legend distinguishing published research, traditional practice and Citane adaptation;
- decision-point structure can become a strong Level 2/3 tool.

### Problems
- opens directly at technical density;
- statements such as `leaf maturity ... is the single most consequential decision` are stronger than the evidence visible beside them;
- maturity bands and compound/pathway tables may combine literature values, extrapolation and Citane inference without sufficiently granular provenance;
- exact leaf ages and pathway suitability can look prescriptive.

Disposition: KEEP AS SOURCE / SPLIT.
- simplified compass → UNDERSTAND;
- full technical compass → EXAMINE.

## 5. `citane-processing-manual.html`

### Strengths
- large body of structured processing material;
- evidence/caution/note distinctions already exist;
- useful as a technical source pool;
- attempts to explain process logic rather than list recipes only.

### Problems
- far too dense for ordinary-reader entry;
- contains its own sticky local navigation while global navigation is injected at runtime;
- duplicates glossary, map, process navigation and reference functions found elsewhere;
- risks turning framework terminology into established chemistry;
- likely overlaps substantially with Door Four's chemistry framework.

Disposition: REFERENCE SOURCE / REWRITE into Level 3 technical manual; extract only simple pathway explanations for Level 2.

## 6. `citane-processing-protocols.html`

### Strengths
The page explicitly states that pathways are:
- structured experiments;
- starting points;
- designed for comparison;
- not guaranteed outcomes.

This is strong message-engine framing and should survive.

### Problems
- repeats orientation/library-map material inside the page;
- still contains pathway descriptions whose sensory/chemical outcomes may sound predicted rather than hypothetical;
- local sticky nav duplicates the global shell;
- `Paper I / II / III` framing is useful for advanced users but not a beginner structure.

Disposition: KEEP CONCEPT / REWRITE as Level 3 experimental workbook.

## 7. `citane-hack-grill-wilted-leaves.html`

This page is a high-risk example of experiment/inference blending.

Claims requiring quarantine and verification include:
- `good GABA content, similar to a light-fermented leaf`;
- young leaves having more GABA and better flavour;
- exact claimed GABA range `0.28–0.35 mg/g` for the grill method;
- caffeine being higher because of less processing time;
- phenolics being high;
- `best for afternoon focus, daytime clarity`;
- equivalence/comparison to light-fermented and oolong processing;
- precise sensory outcomes stated prospectively rather than recorded as a particular trial result.

If these values were not analytically measured on the trial batch, they must not appear as results.

Rebuild form should be a **Field Experiment Record**:
- date;
- leaf identity/state;
- equipment;
- actual measured temperature/time;
- steps performed;
- observations;
- sensory notes;
- measurements actually taken;
- hypothesis/questions;
- what was not measured.

Disposition: REWRITE → EXAMINE / FIELD NOTE. Do not present as general DIY specification until validated.

## 8. `citane-hack-gas-flame-roasted-leaf.html`

High-risk claims include:
- calling gas-flame roasting a `traditional method` without identifying the exact tradition/source;
- direct flame producing `more intense Maillard development`;
- `Maillard reaction accelerating` and later `development complete` from visual browning alone;
- long brewing `ensures` release of Maillard character;
- sensory comparisons presented as stable method properties;
- exact recipe parameters without clear distinction between trial settings and validated specifications.

Visual browning cannot by itself prove which chemical reactions occurred or their completion.

Disposition: REWRITE → FIELD EXPERIMENT RECORD / EXAMINE. Preserve actual observed procedure and tasting observations; move reaction mechanisms into labelled hypotheses unless analytically supported.

## 9. `cinnamon-smoke-trial.html`

This page contains valuable photographs and actual temperature readings, but its prose repeatedly overinterprets those observations.

Examples:
- `41.0°C confirms ... safely below the critical plant cell destruction point`;
- `44.3°C ... guarantees moisture depletion proceeds systematically`;
- `prolonged enzyme and microbe driven transformation` without shown enzyme/microbial measurements;
- colour `shows controlled oxidation`;
- vein structure tied to `water activity barrier` without displayed water-activity measurement;
- `subtle spice precursor integration` inferred from smoke exposure.

What can safely survive:
- species/material used, if correctly recorded;
- photographs;
- actual instrument readings;
- elapsed time/date;
- observed colour/texture/smoke conditions;
- sensory observations actually made;
- experimental intent.

Everything mechanistic must be separately marked as hypothesis or removed if unsupported.

Disposition: REWRITE → FIELD TRIAL RECORD / EXAMINE.

## 10. Required field-note archetype

Door Three needs one common field-note format so technical language cannot hide evidence status.

Suggested sections:

### Question
What were we trying to learn?

### Setup
Date, place, variety/species, leaf state, batch size, equipment.

### What we did
Chronological procedure.

### What we measured
Only actual measurements and instruments.

### What we observed
Colour, aroma, texture, photographs, sensory notes.

### What we think may be happening
Clearly labelled **Hypothesis / Interpretation**.

### What we did NOT measure
Examples: GABA, caffeine, microbial population, oxidation products, water activity, Maillard markers.

### Next experiment
What would test the hypothesis?

This archetype should replace `Hack` language where the record is exploratory rather than established instruction.

## 11. Message-engine validity queue

High priority:
1. maturity-age bands and compound profiles in Process Compass;
2. exact relationship of leaf maturity to mangiferin, tannin, lipid and volatiles;
3. early-morning harvest mechanism claims;
4. exact pathway suitability claims;
5. all GABA values and process relationships;
6. caffeine change attributed to processing duration;
7. phenolic/antioxidant outcomes;
8. Maillard claims for coffee-leaf roasting under actual temperatures/times;
9. fermentation versus oxidation terminology throughout Citane documents;
10. microbial claims where no microbiology was measured;
11. water-activity claims where only drying/texture was observed;
12. temperature thresholds for enzyme/cell destruction;
13. smoke chemistry and transfer claims;
14. sensory outcomes presented as deterministic process results;
15. any `best for focus`, restorative or physiological language.

## 12. Navigation and page-count problem

Current Door Three exposes:
- Process Compass;
- Paper II;
- Paper III;
- several Field Notes / Hacks;
- Cinnamon Smoke trial;
- Projects hub.

The ordinary reader should not see these as equivalent peer entrances.

Proposed architecture:

**Door Three — Processing & Experiment**

### LOOK
`What processing changes`

### UNDERSTAND
`Processing pathways`

### EXAMINE / DO
A structured technical workspace containing:
- Process Compass;
- Technical Manual;
- Experimental Workbook;
- Field Notes / Trials.

Field Notes can remain separate records because they are evidence objects, but they sit *inside* the Level 3 workspace rather than beside the beginner doorway.

## 13. Ordinary-reader design

### LOOK
One vertical story, approximately:
- leaf;
- time;
- touch;
- heat;
- drying;
- cup.

Use five simple illustrations, not tables.

### UNDERSTAND
Interactive or static pathway map with plain labels and optional `Why?` explanations.

### EXAMINE
Tables, batch sheets, evidence labels, experimental records, citations.

The visual density may legitimately increase with depth.

## 14. Rebuild dispositions

| Current file | Rebuild disposition |
|---|---|
| `citane-process-compass.html` | SPLIT: simplified compass → UNDERSTAND; technical compass → EXAMINE |
| `citane-processing-manual.html` | REWRITE / REFERENCE SOURCE → EXAMINE |
| `citane-processing-protocols.html` | KEEP CONCEPT / REWRITE → EXAMINE experimental workbook |
| `citane-hack-grill-wilted-leaves.html` | REWRITE → FIELD EXPERIMENT RECORD |
| `citane-hack-gas-flame-roasted-leaf.html` | REWRITE → FIELD EXPERIMENT RECORD |
| `cinnamon-smoke-trial.html` | REWRITE → FIELD TRIAL RECORD; preserve actual observations/images |
| `projects.html` | Reassess in whole-library synthesis; likely index of experiments, not primary Door page |

No current Door Three page is accepted unchanged.

## 15. Governing principle

> The deeper a processing page becomes, the clearer it must become about what was actually measured.

Technical vocabulary must never substitute for evidence.

The LOOK level teaches the idea. The UNDERSTAND level explains choices. The EXAMINE level exposes the records, uncertainty and provenance.
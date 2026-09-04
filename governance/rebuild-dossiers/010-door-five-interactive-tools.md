# Buna Reconstruction Dossier — Door Five: Interactive Tools

Audit state: DOOR REVIEW COMPLETE / LOGIC-LEVEL VALIDITY QUEUE OPEN

Files reviewed:
- `citane-terrain-map.html`
- `clt-flavour-wheel.html`
- `citane-logic-board.html`
- `citane-epsilon-board.html`

## 1. Intended role

Door Five should let a reader interact with Buna's knowledge without confusing interaction with proof.

A tool can help someone:
- explore relationships;
- navigate evidence;
- compare processing choices;
- formulate an experiment;
- generate hypotheses.

A tool must not make a weak relationship look stronger merely because it is drawn as a line, coloured node, disabled option or AI-generated instruction.

## 2. Three-depth model for tools

### Level 1 — LOOK / USE

The tool should work with minimal explanation.

The user sees:
- what the tool does;
- what inputs they can choose;
- the result;
- a plain confidence/evidence statement.

No requirement to understand the underlying model.

### Level 2 — UNDERSTAND THE TOOL

The user can open:
- what data/source types drive the result;
- what is measured versus inferred;
- what assumptions are being used;
- why an option is available or blocked;
- what the tool cannot determine.

### Level 3 — EXAMINE THE LOGIC

For serious users:
- source-to-node mapping;
- rule definitions;
- relationship strengths and how derived;
- model/version information;
- AI prompt/evidence boundaries where relevant;
- unresolved assumptions;
- exportable research rationale.

The depth controls are about transparency, not different conclusions.

## 3. Tool-level evidence rule

Every relationship rendered by a tool should belong to one of:

**Measured / directly documented**

**Literature-supported relationship**

**Inferred / analogous**

**Citane observation**

**Model rule**

**Speculative / AI-generated**

A visual line, percentage or disabled choice must never imply greater certainty than its class.

## 4. Terrain Map assessment

### Strengths
- compelling plant-to-cup spatial model;
- confidence/fuzz dots already attempt to communicate uncertainty;
- node details can expose explanatory context;
- suitable as an advanced exploratory map.

### Problems
- entire page is a fixed full-screen canvas, which is not ordinary-reader friendly and can conflict with global navigation/mobile viewport behaviour;
- model topology visually implies causal relationships;
- node-level caveats are not enough when the connecting graph itself has no visible provenance;
- some nodes combine general plant physiology, published coffee-leaf findings, Kerala climate inference and Thumpassery assumptions in one network.

Examples requiring source-level verification:
- `rubber shade ... diffused PAR approximately 30–60% of full sun`;
- lower PAR correlating with higher mangiferin and altered ionone precursor pools;
- exact leaf-position chemistry ranges;
- leaf surface being 5–8°C above ambient;
- Kerala seasonal statements about enzyme activity and processing windows;
- every edge that represents a causal rather than merely contextual relationship.

Disposition: KEEP CONCEPT / REBUILD as Level 2–3 exploratory tool. A simple linear plant-to-cup view should precede the full network.

## 5. CLT Flavour Landscape assessment

### Strengths
- approachable visual exploration of sensory territories;
- encourages users to think relationally rather than as a fixed flavour wheel;
- source list is exposed;
- useful potential bridge between sensory and processing.

### Problems
Each flavour node currently packages:
- descriptor;
- specific compounds/OAVs;
- process;
- leaf maturity;
- brew temperature/time;
- relationship strength to other flavours.

These are different evidence objects but appear as one coherent recommendation.

Examples requiring verification:
- OAV ranges and product/sample context;
- `cold serving at 10°C is the critical activation`;
- hot serving `eliminates` refreshing character;
- specific process-to-floral mappings;
- exact infusion temperatures/times;
- leaf-age requirements;
- numerical relationship strengths such as 82/88/72 — determine whether these are measured scores, model weights or editorial values.

If relationship strengths are author-created model weights, the interface must say so explicitly.

Disposition: REBUILD. Keep flavour-exploration concept; separate observed sensory evidence from model suggestions.

## 6. Flavour Logic Board assessment

### Strengths
- useful entry points: descriptor, leaf, process, brew method;
- attempts to show compatible and incompatible pathways;
- can connect user intent to experiment design;
- contains an Epsilon/theoretical mode distinction.

### Critical risk
The phrase `activates the possible paths and closes off the impossible ones` is too strong unless rules are genuinely logically impossible.

In most food-processing systems, the appropriate distinction is more likely:
- supported;
- plausible;
- weakly supported;
- conflicts with current target;
- unknown.

A disabled/struck-through UI control psychologically communicates impossibility.

Every rule that disables an option needs:
- rule ID;
- source/evidence class;
- reason;
- whether impossible, merely incompatible with chosen goal, or simply unsupported.

Disposition: KEEP CONCEPT / REWRITE logic and evidence explanation.

## 7. Epsilon Board assessment

### Strength
Current framing is substantially better than the other tools:
- explicitly `Speculative CLT pathways`;
- explicitly `AI-generated, not validated`;
- explicitly `not likely outcomes`;
- described as `creative space for direction, not instruction`.

That distinction should be preserved and used as a model across Door Five.

### Remaining requirements
Even speculative output should:
- cite which known inputs/evidence it used;
- separate literature facts from generated proposal;
- avoid medical/health outcome generation;
- identify safety-sensitive process suggestions;
- provide `What would test this?` rather than presenting generated chemistry as predicted truth;
- retain model/prompt/version provenance at Level 3.

Disposition: KEEP ROLE / SIMPLIFY UI / STRENGTHEN provenance.

## 8. Ordinary-reader Door Five landing

The Door landing should not begin with four technical tool names.

Suggested questions:

**Explore the journey**
Plant → leaf → process → cup.
→ Terrain Map

**Explore flavour**
See how sensory descriptions relate.
→ Flavour Landscape

**Plan an experiment**
Start from a leaf, process or flavour goal.
→ Logic Board

**Imagine a new pathway**
Generate a hypothesis, clearly speculative.
→ Epsilon Board

Each card says what kind of result the tool produces and its evidence status.

## 9. Tool design principles

### 9.1 Evidence travels with output
Do not hide all evidence in a final Sources drawer.

### 9.2 A line is a claim
Any edge/connection in a map needs a meaning and provenance.

### 9.3 A number is a claim
Relationship scores, OAV ranges, temperatures, times and probabilities require scope.

### 9.4 Disabled means what it says
Do not render an option impossible if it is merely not recommended or unsupported.

### 9.5 AI output is proposal
AI may generate experiment ideas, not upgrade them into evidence.

### 9.6 Tools must degrade gracefully to ordinary text
A reader should be able to understand the purpose and major conclusion even if the interactive layer fails.

## 10. Cross-Door ownership

Door Five does not own underlying scientific explanations.

- chemistry → Door Four;
- processing protocols → Door Three;
- sensory education → Door Six;
- definitions → Door Eight;
- tradition evidence → Door Two.

The tools consume/link those canonical knowledge objects.

This is important for rebuild architecture: data/evidence should exist once and tools should render it, rather than hard-coding competing copies of the same proposition in several JavaScript objects.

## 11. Rebuild technical implication

The current tools embed substantial knowledge directly inside HTML/JavaScript.

Bottom-up rebuild should move reusable knowledge into a structured evidence/data layer, for example conceptually:
- claim ID;
- statement;
- scope;
- source(s);
- evidence class;
- confidence;
- related concepts;
- tool rule(s).

The visual tool consumes the same accepted claim objects used by pages.

This prevents a corrected page from disagreeing with an old JavaScript node.

## 12. Validity queue

High priority:
1. all Terrain Map nodes and edges;
2. all estate-specific environmental assumptions;
3. every flavour-node OAV and compound mapping;
4. every brew parameter;
5. every process/leaf-maturity recommendation;
6. every numerical relationship strength;
7. every Logic Board compatibility/exclusion rule;
8. distinction between measured impossibility and model preference;
9. every prompt/system statement given to Epsilon AI;
10. whether generated outputs can create unsafe or unsupported processing/health statements.

## 13. Rebuild disposition

| Current file | Rebuild disposition |
|---|---|
| `citane-terrain-map.html` | KEEP CONCEPT / REBUILD as transparent Level 2–3 map |
| `clt-flavour-wheel.html` | KEEP CONCEPT / REBUILD from audited sensory data |
| `citane-logic-board.html` | KEEP CONCEPT / REWRITE rules and evidence semantics |
| `citane-epsilon-board.html` | KEEP ROLE / SIMPLIFY / strengthen provenance and testing language |

No current tool should be treated as a canonical evidence source.

## 14. Governing principle

> Interaction can make uncertainty easier to explore, but it must never make uncertainty look like certainty.

Door Five's rebuild depends on the shared evidence architecture created by the wider Library synthesis.
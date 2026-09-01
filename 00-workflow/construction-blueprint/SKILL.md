---
name: construction-blueprint
display_name: 施工蓝图
description: Use when an Architecture Director has frozen the current Stage Contract and an implementation agent needs a deterministic, repository-grounded execution contract before coding begins.
---

# 施工蓝图

## Purpose

Compile a frozen Stage Contract, approved architecture decisions, repository reality, scope boundaries, and acceptance requirements into a deterministic execution contract that an implementation agent can follow mechanically.

The blueprint compiles approved decisions; it does not create product or architecture decisions.

The execution contract is complete when:

- every construction-time implementation choice is already resolved;
- every task has deterministic prerequisites, actions, outputs, verification, and exit conditions;
- every upstream requirement is traceable to implementation work and evidence;
- every preservation, regression, architecture, and scope obligation is verifiable;
- every exception routes to a defined control path;
- dry-run reaches the Stage Exit State without introducing a new product, architecture, scope, or acceptance decision.

## Authority Boundary

Source-of-truth order:

`Product / Architecture → Stage Contract → Construction Blueprint → Implementation → Evidence`

The Construction Blueprint may decide execution mechanics inside already-approved boundaries, including task decomposition, repository targets, ordering, dependency sequencing, test placement, migration sequencing, and verification placement.

The Construction Blueprint escalates any issue that requires changing:

- Product Outcome or Product Rule;
- Accepted Requirement;
- Stage Scope;
- Stage Exit State;
- Architecture Invariant;
- data ownership or lifecycle semantics;
- interface semantics;
- security or permission semantics;
- transaction or consistency semantics;
- acceptance semantics;
- approved technical direction.

Such issues end planning in `PLAN_BLOCKED` and return to the Architecture Director.

## Required Authoritative Inputs

Collect and reconcile:

### Current Stage Contract

- Stage ID / Name
- Roadmap Position
- Accepted Requirement IDs
- Intent
- Entry State
- Exit State
- Visible Delta
- Decisions
- Authorized Scope
- Architecture Delta
- Architecture Invariants
- Preservation Set
- Deferred Set
- Acceptance Criteria
- Regression Set
- Escalation Triggers
- Stop Rule

### Architecture Inputs

- Relevant Architecture Spine
- Relevant ADR / Decision Log entries
- Architecture Director Blueprint Handoff
- Applicable project rules

### Repository Inputs

- Current repository state
- Relevant implementation, callers, schemas, migrations, tests, configuration, and generated artifacts
- Existing implementation patterns
- Available build, test, typecheck, migration, generation, and inspection commands

Approved upstream decisions are authority. Repository state is execution reality.

Differences between authority and reality must be classified before planning:

- repository detail compatible with approved decisions → incorporate into blueprint;
- implementation-path ambiguity inside approved boundaries → resolve in blueprint;
- upstream semantic or architectural conflict → `PLAN_BLOCKED`.

## Planning Procedure

### 1. Establish Current State

Identify the verified Entry State:

- existing behavior relevant to the Stage;
- exact files, symbols, interfaces, schemas, tests, commands, generated artifacts, and conventions involved;
- affected component dependencies;
- current call, data, state, and side-effect paths;
- applicable Architecture Invariants;
- Preservation Set and Regression Set baselines;
- repository facts required by later tasks.

Use exact repository paths and symbol names.

Record discrepancies between documented Entry State and repository reality.

### 2. Establish Target State

Translate the Stage Exit State into concrete observable repository and runtime conditions:

- capability added or changed;
- Visible Delta produced;
- required interfaces, schemas, state transitions, or artifacts established;
- existing behavior preserved;
- Architecture Delta realized;
- Acceptance Criteria satisfied;
- Regression Set preserved;
- Deferred Set remains outside current construction;
- Stage Stop Rule becomes true.

Current Stage completion is independent from final-product completion.

### 3. Operationalize Frozen Decisions

Extract every approved decision that constrains implementation:

- architecture placement;
- interfaces and signatures;
- data ownership and lifecycle;
- persistence behavior;
- error semantics;
- dependency choices;
- compatibility behavior;
- transaction / concurrency / consistency boundaries;
- security / permission semantics;
- migration strategy;
- test strategy;
- generation strategy;
- rollout or ordering constraints.

Convert these decisions into repository-level implementation constraints.

If a required decision is absent, contradictory, or still has multiple product/architecture-valid paths, return `PLAN_BLOCKED` to the Architecture Director.

### 4. Establish Scope Sets

Define:

- `Change Set`: existing files, directories, symbols, schemas, configurations, or tests expected to change;
- `Creation Set`: new files, symbols, schemas, migrations, tests, or artifacts expected after execution;
- `Preservation Set`: existing behaviors, interfaces, data contracts, invariants, files, or runtime guarantees that must remain valid;
- `Regression Set`: existing tests, journeys, commands, or observable behavior that must continue to pass;
- `Deferred Set`: recognized requirements intentionally outside the current Stage.

Use exact paths, symbols, Acceptance IDs, Requirement IDs, ADR IDs, or invariant IDs wherever possible.

Every planned change must belong to the current Stage Contract.

### 5. Build Requirement Traceability

Before task decomposition, establish:

`Accepted Requirement → Stage Acceptance → Blueprint Task → Verification Evidence`

For every Accepted Requirement and Acceptance Criterion identify:

- implementation responsibility;
- task coverage;
- expected evidence;
- preservation or regression dependencies.

Every task must trace upward to at least one current-stage requirement, acceptance item, architecture obligation, preservation obligation, or regression obligation.

Every current-stage requirement must trace downward to at least one task and one verification point.

### 6. Build the Dependency Graph

Decompose the Target State into ordered tasks.

A task is valid when it:

- produces one independently verifiable state transition;
- has explicit prerequisites;
- has a bounded change surface;
- implements a coherent requirement or architectural obligation;
- supplies everything required by dependent tasks;
- ends with an observable verification result;
- leaves the repository in a valid intermediate state.

Order tasks by real dependency.

Mark `[parallel]` only when prerequisites, write surfaces, generated artifacts, shared state, and verification dependencies are independent.

### 7. Compile Tasks into Mechanical Steps

Each task must contain:

- `Task ID`
- `Requirement Coverage`
- `Objective`
- `Prerequisites`
- `Targets`
- `References`
- `Inputs`
- `Actions`
- `Outputs`
- `Verification`
- `Expected Result`
- `Exit Condition`

`Requirement Coverage` lists exact Requirement IDs, Acceptance IDs, invariant IDs, preservation IDs, or regression IDs served by the task.

`Targets` names exact files, symbols, schemas, migrations, configurations, tests, or generated artifacts.

`References` names exact repository artifacts, ADRs, interfaces, tests, or conventions that govern implementation.

`Inputs` names the concrete repository state required before execution.

`Actions` are ordered state-changing operations. Each action describes one operation and contains enough detail to produce the single approved implementation path.

`Outputs` describe the concrete repository and runtime state produced by the task.

`Verification` specifies executable commands, test selectors, inspections, state checks, migration checks, generation checks, or deterministic manual procedures.

`Expected Result` states the exact observable verdict.

`Exit Condition` states the condition that unlocks dependent tasks.

### 8. Define Acceptance Matrix

Map the complete Stage Contract to verification.

Each item records:

- `Acceptance ID`
- `Type`
- `Requirement / Obligation`
- `Requirement Source`
- `Blueprint Task`
- `Evidence Source`
- `Verification Method`
- `Pass Condition`

`Type` is one of:

- `DELIVERY`
- `ARCHITECTURE`
- `PRESERVATION`
- `REGRESSION`
- `SCOPE`

Coverage requirements:

- every Stage Acceptance Criterion → `DELIVERY`;
- every current-stage Architecture Invariant obligation → `ARCHITECTURE`;
- every Preservation Set commitment → `PRESERVATION`;
- every Regression Set item → `REGRESSION`;
- current Authorized Scope and Deferred boundary → `SCOPE`.

Every item produces one verdict:

`PASS | FAIL | BLOCKED`

### 9. Define Exception Routing

Every expected execution exception must map to one control path.

#### `LOCAL_FIX`

Use when the issue is an implementation error inside the current task and the approved design remains unchanged.

#### `RETURN_TO_TASK:<TXX>`

Use when the current failure proves an earlier blueprint task did not reach its Exit Condition.

#### `REPLAN_BLUEPRINT`

Use when the Stage Contract remains valid but the current task decomposition, ordering, repository targeting, or verification path cannot reach the approved Exit State.

Blueprint may revise execution mechanics while preserving all upstream semantics and boundaries.

#### `PLAN_BLOCKED_ARCHITECTURE`

Use when continuing requires a new or changed architecture, scope, data, interface, security, transaction, compatibility, or acceptance decision.

Return exact evidence and the unresolved decision to the Architecture Director.

#### `PRODUCT_CHANGE`

Use when the current Product Outcome, Product Rule, business behavior, acceptance meaning, or user-authorized requirement has changed.

Freeze blueprint generation and route through Product Definition / Architecture Director replanning.

Define routes for at least:

- repository state differs from Entry State;
- referenced file or symbol is absent or has a different contract;
- required tool or dependency is unavailable;
- verification fails inside the current task;
- verification exposes a pre-existing external failure;
- generated artifact and source-of-truth differ;
- a deferred requirement becomes a true prerequisite;
- a new architectural or product decision becomes necessary;
- the documented sequence cannot reach an Acceptance Criterion;
- migration / deployment ordering is unsafe;
- preservation or regression obligations become incompatible with the approved path.

### 10. Dry-Run the Document

Simulate execution from verified Entry State through every task to final Stage acceptance using the current repository.

Validate:

- every referenced path, symbol, interface, schema, command, and tool resolves;
- every task prerequisite exists before use;
- every output satisfies dependent task inputs;
- names, signatures, IDs, schemas, and state transitions remain consistent;
- every task exposes one approved implementation path;
- no task creates a new product or architecture decision;
- every Accepted Requirement maps to task work and evidence;
- every Acceptance Criterion maps to deterministic verification;
- every Architecture Invariant has a current-stage verification or preservation path;
- every Preservation and Regression item has evidence;
- every implementation change maps upward to a Stage obligation;
- Deferred items remain outside the execution graph;
- every exception has one defined route;
- intermediate repository states remain valid;
- final repository and runtime state satisfy the Stage Exit State;
- Stage Stop Rule becomes true.

Repair blueprint-level gaps before publishing.

If dry-run exposes an upstream decision gap, end in `PLAN_BLOCKED`.

## Output Document Schema

Generate the execution document with this exact section order:

1. `# <Stage> — Execution Contract`
2. `## Stage Authority`
3. `## Objective`
4. `## Entry State`
5. `## Exit State`
6. `## Visible Delta`
7. `## Fixed Decisions`
8. `## Repository References`
9. `## Scope`
   - `### Change Set`
   - `### Creation Set`
   - `### Preservation Set`
   - `### Regression Set`
   - `### Deferred Set`
10. `## Requirement Traceability`
11. `## Execution Graph`
12. `## Tasks`
13. `## Acceptance Matrix`
14. `## Exception Routing`
15. `## Completion Protocol`

## Stage Authority Format

Record:

- `Stage ID`
- `Accepted Requirement IDs`
- `Architecture / ADR References`
- `Stage Contract Reference`
- `Stop Rule`

## Requirement Traceability Format

Represent compactly:

```text
REQ-01 -> AC-01 -> T01,T03 -> EVID-01
REQ-02 -> AC-02 -> T02     -> EVID-02
INV-03 -> AC-A03 -> T04    -> EVID-A03
```

## Execution Graph Format

Represent dependencies compactly:

```text
T01 -> T02 -> T04
       T03 -> T04
T04 -> T05
```

Add `[parallel]` only to dependency-independent tasks.

## Task Format

Use this structure for every task:

```markdown
### TXX — <task name>

**Requirement Coverage:**

**Objective:**

**Prerequisites:**

**Targets:**

**References:**

**Inputs:**

**Actions:**
1.
2.
3.

**Outputs:**

**Verification:**

**Expected Result:**

**Exit Condition:**
```

## Acceptance Matrix Format

Use:

| ID | Type | Requirement / Obligation | Source | Task | Evidence | Verification | Pass Condition |
|---|---|---|---|---|---|---|---|

## Completion Protocol

The execution contract ends in `READY` only when:

- all authoritative inputs are present and mutually compatible;
- all repository references resolve;
- all current-stage implementation decisions are fixed;
- no task requires a new product or architecture decision;
- all Accepted Requirements are traceable to tasks and evidence;
- all tasks have deterministic prerequisites, actions, outputs, verification, and exit conditions;
- all Acceptance Criteria are covered;
- all Architecture Invariants relevant to the Stage are protected;
- all Preservation commitments are verifiable;
- all Regression obligations are verifiable;
- all Deferred requirements remain outside current execution;
- every planned change maps to current Stage authority;
- all exception conditions route to a deterministic control path;
- dry-run reaches the Stage Exit State;
- the Stage Stop Rule can be mechanically evaluated.

Otherwise end in:

```text
PLAN_BLOCKED

Type: <REPLAN_BLUEPRINT | PLAN_BLOCKED_ARCHITECTURE | PRODUCT_CHANGE>
Gap: <identifier>
Location: <section/task>
Evidence: <repository fact / contract conflict>
Upstream Source: <Stage Contract / ADR / Product Rule / Requirement ID>
Decision Required: <single unresolved decision>
Owner: <Construction Blueprint | Architecture Director | Product / User>
```

## Handoff

When status is `READY`, hand the Execution Contract to the implementation agent.

The implementation agent executes the blueprint under the project’s construction rules and returns implementation changes plus verification evidence.

The Stage Verifier later evaluates:

`Architecture → Stage Contract → Construction Blueprint → Implementation → Evidence`

The blueprint therefore preserves complete forward and reverse traceability.

## Quality Standard

Optimize for execution certainty and information density.

Use exact paths, symbols, commands, selectors, requirement IDs, acceptance IDs, state transitions, dependency edges, and observable outcomes.

Prefer repository-grounded references over descriptive prose.

Keep rationale only when it constrains execution, preserves an upstream decision, or explains a required exception route.

The blueprint is complete when the implementation agent can execute from Entry State to Exit State without deciding what the product means, what architecture should exist, what belongs in the Stage, or what counts as completion.

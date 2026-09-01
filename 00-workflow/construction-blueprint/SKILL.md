---
name: construction-blueprint
display_name: 施工蓝图
description: Use when requirements and design decisions are settled and an agent needs a deterministic, repository-grounded implementation document before coding begins.
---

# 施工蓝图

## Purpose

Compile approved intent, repository reality, fixed decisions, scope, and acceptance criteria into an execution document that an implementation agent can follow mechanically.

The execution document is complete when every implementation choice required during construction is already resolved, every step has deterministic inputs and outputs, every verification has an observable verdict, and every exception maps to a defined control path.

## Required Inputs

Collect and reconcile:

- Approved requirement or stage objective
- Current repository state
- Relevant architecture and project rules
- Existing implementation patterns
- Fixed technical decisions
- Current-stage boundaries
- Deferred requirements
- Acceptance criteria

Treat repository contents as evidence and approved decisions as authority. Resolve conflicts during planning and record the resolved result in the execution document.

## Planning Procedure

### 1. Establish Current State

Identify:

- Existing behavior relevant to the stage
- Existing files, symbols, interfaces, schemas, tests, commands, and conventions used by the work
- Dependencies between the affected components
- Existing invariants that remain valid after the stage

Use exact repository paths and symbol names.

### 2. Define Target State

State the observable repository and system state after execution:

- Capability added or changed
- Existing behavior preserved
- Interfaces or data shapes established
- Stage-level completion boundary
- Requirements assigned to later stages

Define completion for the current stage independently from final-project completion.

### 3. Freeze Decisions

Record every decision that affects implementation shape, including:

- Architecture placement
- Interfaces and signatures
- Data ownership and lifecycle
- Persistence behavior
- Error semantics
- Dependency choices
- Compatibility behavior
- Transaction or concurrency boundaries
- Test strategy
- Migration strategy

Each decision must select one implementation path. Any unresolved multi-path choice is a planning gap.

### 4. Establish Scope Sets

Define four explicit sets:

- `Change Set`: files, directories, symbols, schemas, or tests expected to change
- `Preservation Set`: behaviors, contracts, files, interfaces, and invariants that remain unchanged
- `Creation Set`: new artifacts expected after execution
- `Deferred Set`: recognized requirements assigned outside the current stage

Use paths, symbol names, identifiers, or requirement IDs wherever possible.

### 5. Build the Dependency Graph

Decompose the target state into ordered tasks. A task is valid when it:

- Produces one independently verifiable state transition
- Has explicit prerequisites
- Has a bounded change surface
- Supplies everything required by dependent tasks
- Ends with an observable verification result

Order tasks by dependency. Mark tasks parallel only when their inputs and write surfaces are independent.

### 6. Compile Tasks into Mechanical Steps

Each task must contain:

- `Task ID`
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

`Targets` names exact files and symbols.

`References` names exact repository artifacts whose structure or convention governs the task.

`Actions` are ordered state-changing operations. Each action describes one operation and contains enough detail to produce a single intended implementation path.

`Outputs` describe the concrete repository state created by the task.

`Verification` specifies executable commands, test selectors, inspections, or deterministic checks.

`Expected Result` states the exact observable result of verification.

`Exit Condition` states the condition that unlocks dependent tasks.

### 7. Define Acceptance Matrix

Map every stage requirement to one or more verification points.

For each acceptance item record:

- `Acceptance ID`
- `Requirement`
- `Evidence Source`
- `Verification Method`
- `Pass Condition`

Include preservation checks for existing behavior and scope checks for the planned change surface.

Every acceptance item must produce a deterministic verdict: `PASS`, `FAIL`, or `BLOCKED`.

### 8. Define Exception Routing

Define execution-time control paths for:

- Repository state differs from the documented prerequisite
- Referenced file or symbol is absent or has a different contract
- Required dependency or tool is unavailable
- A verification fails within the current task
- A verification exposes a pre-existing failure outside the current task
- A new architectural or product decision becomes necessary
- A deferred requirement becomes a prerequisite for the current stage
- The documented sequence cannot reach an acceptance condition

Each condition maps to one action: local correction within the current task, return to a named earlier task, or `PLAN_BLOCKED` with exact evidence and the missing decision.

### 9. Dry-Run the Document

Simulate execution from the first task to final acceptance using the current repository.

Validate:

- Every referenced path and symbol resolves
- Every task prerequisite is created before use
- Names and signatures remain consistent across tasks
- Each task exposes one intended implementation path
- Every required decision is frozen
- Every requirement maps to implementation work and verification
- Every verification has a defined expected result
- Every exception has a defined route
- The final repository state satisfies the target state and preservation set

Repair planning gaps before publishing the execution document.

## Output Document Schema

Generate the execution document with this exact section order:

1. `# <Stage or Feature> — Execution Contract`
2. `## Objective`
3. `## Current State`
4. `## Target State`
5. `## Fixed Decisions`
6. `## Repository References`
7. `## Scope`
   - `### Change Set`
   - `### Preservation Set`
   - `### Creation Set`
   - `### Deferred Set`
8. `## Execution Graph`
9. `## Tasks`
10. `## Acceptance Matrix`
11. `## Exception Routing`
12. `## Completion Protocol`

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

## Completion Protocol

The execution document ends in `READY` only when:

- All repository references resolve
- All implementation decisions required by the task graph are fixed
- All tasks have deterministic prerequisites, actions, outputs, verification, and exit conditions
- All requirements are covered by the acceptance matrix
- All preservation commitments are verifiable
- All deferred requirements are explicitly classified
- All exception conditions route to a deterministic action
- The dry-run reaches the target state without introducing a new decision

Otherwise end in:

```text
PLAN_BLOCKED

Gap: <identifier>
Location: <section/task>
Evidence: <repository fact or requirement conflict>
Decision Required: <single unresolved decision>
```

## Quality Standard

Optimize the document for execution certainty and information density.

Use exact paths, symbols, commands, selectors, state transitions, identifiers, and observable outcomes. Prefer repository-grounded references over descriptive prose. Keep rationale only when it constrains implementation or resolves an otherwise ambiguous choice.

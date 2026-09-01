---
name: construction-blueprint
display_name: 施工蓝图
description: Use when an Architecture Director has frozen the current Stage Contract and an implementation agent needs a deterministic, repository-grounded execution contract that delivers the Stage through continuous vertical integration, real product checkpoints, and user-verifiable outcomes.
---

# 施工蓝图

# 最高优先级施工原则

以下原则高于后续任务拆分、依赖排序、测试组织与局部效率优化。发生冲突时，以本节为准。

## 1. 先让真实产品成立，再继续扩建

对于包含用户界面、客户端或真实产品交互的 Stage，施工必须尽早形成最薄的真实端到端链路，并在后续施工中持续保持产品可运行、可交互、可观察。

默认禁止：

`Backend → Database → Services → Frontend → Final Integration`

默认采用：

`Thin Vertical Slice → Real Integration → Product Checkpoint → Expand → Re-integrate → Product Checkpoint → Stage Acceptance`

不得把跨层集成推迟到 Stage 尾部。

## 2. Stage 按 Integration Slice 施工，不按技术层批量施工

一个 Stage 可以包含很多 Tasks，但 Tasks 必须组织进一个或多个 `Integration Slice`。

每个 Integration Slice 必须形成一个已经连接起来的产品状态，而不是一组“分别完成、以后再组装”的零件。

典型 Slice 可以同时包含：

- 最小 UI / Client interaction
- 对应 API / Backend behavior
- 对应 Data / State change
- 必要 External Service
- Error / Loading / Failure behavior
- Real integration verification

任务数量不是风险；**长期不集成才是风险**。

## 3. CI PASS 不是产品成立

Unit / Integration / CI / Typecheck / Mock 测试是必要工程证据，但不能替代真实产品路径。

对于用户型 Stage，至少必须证明：

`Real Product Entry → Real User Action → Real Call Path → Real Backend / Service → Real State Change → Real Visible Result`

如果主要产品路径仍依赖 Mock、stub、fake service 或绕过真实入口，只能证明组件，不得证明 Stage Delivery 完成。

## 4. UI 是产品行为的一部分，不是最后的装饰层

当 Stage 的 Product Outcome 需要 UI / Client 才能被用户体验时，UI 必须进入早期 Integration Slice。

不得默认把 UI 安排到所有 Backend / Data / Service 工作完成之后。

以下产品问题通常只有接入真实 UI 后才能被验证：

- loading / pending 状态
- error feedback
- stale state / refresh
- repeated action
- disabled / enabled condition
- navigation / return state
- persistence visibility
- optimistic / asynchronous behavior
- timeout / long-running action
- permission / empty state
- user-visible recovery

## 5. 每个 Integration Slice 都必须有 Product Checkpoint

每个 Slice 必须定义一个可重复执行的 `Product Checkpoint`，至少包含：

- `Product Entry`
- `Actor / Test Identity`
- `Preconditions`
- `Hands-on Steps`
- `Real Services Used`
- `Expected Visible Result`
- `Expected State / Persistence`
- `Required Failure Behavior`
- `Automated Evidence`
- `Mocks Allowed`
- `Slice Exit State`

Checkpoint 必须能够从真实产品入口验证当前 Slice 已经集成成立。

用户不必在每个 Slice 后亲自批准施工继续，但蓝图必须保证任何 Slice 结束时都存在一个可上手验证的真实产品状态。

## 6. Stage 必须有最终 Hands-on Acceptance

对于用户型 Stage，Execution Contract 必须提供最终 `Hands-on Acceptance`。

它必须让非技术用户知道：

- 从哪里进入产品
- 用什么账号 / 前置条件
- 做哪几个操作
- 应该看到什么
- 数据 / 状态应如何保持
- 关键失败时应看到什么

自动化证据不能替代最终 Hands-on Acceptance。

## 7. Technical-only Stage 是例外

如果 Current Stage 无法形成用户可体验的产品变化，只允许在 Stage Contract 已明确批准纯技术前置时继续。

该 Stage 必须同时满足：

- 是紧邻产品闭环的真实必要前置；
- 有明确可验证 Exit State；
- 明确下一哪个 Stage 会消费该能力；
- 不把多个可纵向切开的产品能力连续拆成黑盒技术 Stage。

若当前 Stage 本应产生产品 Visible Delta，但真实仓库路径只能形成后端 / 数据库 / 基础设施黑盒变化，则：

`REPLAN_BLUEPRINT` 或 `PLAN_BLOCKED_ARCHITECTURE`

不得自行把“内部完成”当成产品完成。

## 8. 失败的 Product Checkpoint 阻断后续扩建

如果某 Slice 的真实产品路径失败：

- 不继续堆叠后续 Slice；
- 先定位当前 Slice 内的产品 / 集成 / 实现问题；
- 属于实现错误 → `LOCAL_FIX`；
- 属于蓝图顺序 / 落点问题 → `REPLAN_BLUEPRINT`；
- 属于 Stage / Architecture / Product 语义问题 → 向上游升级。

目标是尽早暴露真实产品问题，而不是把问题积累到 Stage 80%–90% 时一次爆发。

## Purpose

Compile a frozen Stage Contract, approved architecture decisions, repository reality, scope boundaries, and acceptance requirements into a deterministic execution contract that an implementation agent can follow mechanically.

The blueprint compiles approved decisions; it does not create product or architecture decisions.

The execution contract is complete when:

- every construction-time implementation choice is already resolved;
- every task has deterministic prerequisites, actions, outputs, verification, and exit conditions;
- every upstream requirement is traceable to implementation work and evidence;
- every preservation, regression, architecture, and scope obligation is verifiable;
- every exception routes to a defined control path;
- dry-run reaches the Stage Exit State without introducing a new product, architecture, scope, or acceptance decision;
- user-facing work is grouped into continuously integrated vertical slices rather than late-stage component integration;
- every Integration Slice ends in a real Product Checkpoint;
- every user-facing Stage ends in a reproducible Hands-on Acceptance path.

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

## 持久状态

- 开始或恢复规划时先读取 `.agent-state/blueprint.md`，并重新核对当前 Stage Contract、Architecture Handoff 与真实仓库状态。
- 每完成一次仓库确认、任务拆解、依赖确定、Traceability 建立或 Dry Run 后更新当前蓝图状态、已验证事实、Task Graph、Planning Gaps 与 READY/BLOCKED 状态。
- 记录所有依赖施工计划的精确路径、symbol、命令、Requirement/Acceptance ID 和已冻结实施约束，使重新进入会话时无需凭聊天历史重建计划。
- 仓库现实或上游 Contract 改变时立即标记受影响的蓝图内容为失效并重新验证，不沿用旧路径推断新计划。
- 上下文压缩、会话结束或交接前刷新该文件；恢复后从最后一个已验证规划状态继续，并在发布 Execution Contract 后记录其最终引用和状态。
- 新会话开始时在 `.agent-state/blueprint.md` 的 Session Log 追加时间戳，标记会话边界。

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
- Hands-on / user-visible acceptance intent when defined upstream
- Technical-only Stage designation when applicable

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
- Stage Stop Rule becomes true;
- the real product entry path exposes the Stage Visible Delta when the Stage is user-facing;
- the Stage has a reproducible Hands-on Acceptance path.

Current Stage completion is independent from final-product completion.

For a user-facing Stage, repository correctness without a working product path is not a valid Target State.

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

### 6. Build Integration Slices

Before decomposing into individual tasks, divide the Stage into the smallest practical vertical `Integration Slice`s.

Each Slice must define:

- `Slice ID`
- `Product / System Outcome`
- `Real Product Entry`
- `Vertical Path`
- `Required Layers`
- `Real Dependencies`
- `Tasks`
- `Product Checkpoint`
- `Automated Evidence`
- `Slice Exit State`
- `Next Slice Dependency`

Rules:

- the first real end-to-end slice occurs as early as practical;
- a Slice integrates the minimum necessary Client / UI, Backend, Data, and External Service layers required for its outcome;
- later Slices extend an already-running product path instead of waiting for a final integration phase;
- no user-facing Stage may contain a single late `FINAL INTEGRATION` task that first connects independently built major layers;
- component-level preparatory tasks are allowed only when consumed by the nearest upcoming Slice;
- if two or more major technical layers are being substantially completed in isolation before any real product path exists, re-slice unless the Stage Contract explicitly authorizes technical-only construction;
- every Slice must end with a Product Checkpoint before dependent expansion work proceeds.

A Slice is complete only when its layers are connected and its real product behavior works.

`code exists` is not equivalent to `Slice complete`.

### 7. Build the Dependency Graph

Decompose each Integration Slice into ordered tasks.

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

### 8. Compile Tasks into Mechanical Steps

Each task must contain:

- `Task ID`
- `Slice ID`
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

`Slice ID` identifies the Integration Slice whose real product state this task advances.

`Requirement Coverage` lists exact Requirement IDs, Acceptance IDs, invariant IDs, preservation IDs, or regression IDs served by the task.

`Targets` names exact files, symbols, schemas, migrations, configurations, tests, or generated artifacts.

`References` names exact repository artifacts, ADRs, interfaces, tests, or conventions that govern implementation.

`Inputs` names the concrete repository state required before execution.

`Actions` are ordered state-changing operations. Each action describes one operation and contains enough detail to produce the single approved implementation path.

`Outputs` describe the concrete repository and runtime state produced by the task.

`Verification` specifies executable commands, test selectors, inspections, state checks, migration checks, generation checks, or deterministic manual procedures.

`Expected Result` states the exact observable verdict.

`Exit Condition` states the condition that unlocks dependent tasks.

### 9. Define Acceptance Matrix

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
- `USER_REALITY`

Coverage requirements:

- every Stage Acceptance Criterion → `DELIVERY`;
- every current-stage Architecture Invariant obligation → `ARCHITECTURE`;
- every Preservation Set commitment → `PRESERVATION`;
- every Regression Set item → `REGRESSION`;
- current Authorized Scope and Deferred boundary → `SCOPE`;
- every user-facing Slice Product Checkpoint and final Hands-on Acceptance → `USER_REALITY`.

`USER_REALITY` evidence must come from the real product path. Unit tests, mocks, isolated API calls, or database inspection alone are insufficient.

Every item produces one verdict:

`PASS | FAIL | BLOCKED`

### 10. Define Exception Routing

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
- preservation or regression obligations become incompatible with the approved path;
- Product Checkpoint fails even though isolated component tests pass;
- current ordering postpones real integration until late in the Stage;
- the primary product path can only be demonstrated through mocks or bypasses.

### 11. Dry-Run the Document

Simulate execution from verified Entry State through every task to final Stage acceptance using the current repository.

Validate:

- every referenced path, symbol, interface, schema, command, and tool resolves;
- every task prerequisite exists before use;
- Integration Slices appear in a dependency-valid order;
- the earliest practical real end-to-end path is not unnecessarily postponed;
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
- every Integration Slice reaches its Product Checkpoint using the real product path;
- primary user-facing paths do not rely on mocks as proof of completion;
- UI / Client behavior required by the Stage is integrated before late-stage bulk completion;
- a failed Product Checkpoint prevents dependent expansion work;
- final Hands-on Acceptance is reproducible for user-facing Stages;
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
11. `## Integration Slices`
12. `## Execution Graph`
13. `## Tasks`
14. `## Product Checkpoints`
15. `## Hands-on Acceptance`
16. `## Acceptance Matrix`
17. `## Exception Routing`
18. `## Completion Protocol`

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

## Integration Slice Format

Use for every Slice:

```markdown
### SXX — <slice name>

**Outcome:**

**Real Product Entry:**

**Vertical Path:**

**Required Layers:**

**Real Dependencies:**

**Tasks:**

**Product Checkpoint:**

**Automated Evidence:**

**Slice Exit State:**

**Next Slice Dependency:**
```

## Product Checkpoint Format

```markdown
### PC-SXX — <checkpoint name>

**Product Entry:**

**Actor / Test Identity:**

**Preconditions:**

**Hands-on Steps:**
1.
2.
3.

**Real Services Used:**

**Expected Visible Result:**

**Expected State / Persistence:**

**Required Failure Behavior:**

**Automated Evidence:**

**Mocks Allowed:**

**Pass Condition:**
```

For the primary product path, `Mocks Allowed` should normally be `NO`. If `YES`, state exactly what remains unproven and do not use the checkpoint as final Stage delivery evidence.

## Hands-on Acceptance Format

For every user-facing Stage:

```markdown
## Hands-on Acceptance

**Who can test:**

**Product Entry:**

**Preconditions / Test Account:**

**Steps:**
1.
2.
3.

**Expected Visible Result:**

**Expected Persistence / State:**

**Expected Failure Behavior:**

**What This Proves:**
```

This section is written for a non-technical user. It must be directly executable without reading implementation details.

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

**Slice ID:**

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
- user-facing work is organized into vertical Integration Slices;
- no task requires a new product or architecture decision;
- all Accepted Requirements are traceable to tasks and evidence;
- all tasks have deterministic prerequisites, actions, outputs, verification, and exit conditions;
- all Acceptance Criteria are covered;
- every Integration Slice has a real Product Checkpoint;
- the first real end-to-end path is not unnecessarily postponed;
- no user-facing Stage relies on one late final-integration task to connect major layers;
- all Architecture Invariants relevant to the Stage are protected;
- all Preservation commitments are verifiable;
- all Regression obligations are verifiable;
- all Deferred requirements remain outside current execution;
- every planned change maps to current Stage authority;
- all exception conditions route to a deterministic control path;
- every Slice checkpoint can be executed against the real product path;
- component tests / CI / mocks are not used as substitutes for real product delivery evidence;
- user-facing Stages include a reproducible final Hands-on Acceptance;
- dry-run reaches the Stage Exit State through continuously integrated product states;
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

The implementation agent executes the blueprint under the project’s construction rules, completes one Integration Slice at a time, and returns implementation changes plus automated and Product Checkpoint evidence.

A failed Product Checkpoint blocks expansion into dependent Slices until resolved or formally replanned.

The Stage Verifier later evaluates:

`Architecture → Stage Contract → Construction Blueprint → Implementation → Evidence`

The blueprint therefore preserves complete forward and reverse traceability.

## Quality Standard

Optimize for execution certainty and information density.

Use exact paths, symbols, commands, selectors, requirement IDs, acceptance IDs, state transitions, dependency edges, and observable outcomes.

Prefer repository-grounded references over descriptive prose.

Keep rationale only when it constrains execution, preserves an upstream decision, or explains a required exception route.

The blueprint is complete when the implementation agent can execute from Entry State to Exit State without deciding what the product means, what architecture should exist, what belongs in the Stage, or what counts as completion.

For user-facing work, the execution path must continuously produce working integrated product states. A plan that reaches “80% component completion” before the product can be meaningfully used is structurally invalid even if CI is green.

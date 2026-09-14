# Construction Blueprint — Repair Mode

> Owner: 接收 Stage Verifier 的 `Repair Handoff Contract`，把被冻结的修复边界编译成与正常 Blueprint 同颗粒度的临时 Repair Execution Contract，并在 `REPAIR VERIFIED` 后执行一次性 Stage Reconciliation。

## Trigger

只在收到完整：

```text
Target Workflow: Construction Blueprint
Mode: Repair
```

以及 Frozen Finding Set / Target State / Allowed Repair Boundary / Required Proof 时进入。

没有正式 Handoff，不自行从聊天猜 Repair Scope。

## Authority

Repair Mode 继承正常 Blueprint 的全部 Product / Architecture / Stage authority 与 planning gates。

额外约束：

- canonical Stage Contract：READ ONLY；
- canonical Stage Execution Contract：READ ONLY，直到 `REPAIR VERIFIED`；
- Repair Handoff：本轮 repair scope / target / proof 的冻结边界；
- Repair Workspace：临时施工事实，不是新的长期 SoT。

Repair Mode 不得改变 Product、Architecture、Stage Scope / Exit / Acceptance。

## Workspace

默认输出：

`.workbench/repairs/Stage-<N>/Repair-Execution.md`

若项目已有临时工作区约定则沿用，但不得写成第二份 canonical Stage Blueprint。

## Same Granularity, Narrower Scope

Repair Execution Contract 必须使用正常 Construction Blueprint 的同一编译标准：

- Repository Reality intake；
- Planning Guardrails；
- Implementation Shape；
- Reasoning Compilation；
- Delegation Gate；
- Parallel Construction Gate；
- Slice / Task granularity；
- Verification discipline；
- Operational Obligations；
- Dry Run / STOP。

不同点只有：

- Scope 只能来自 Repair Handoff；
- 施工对象是临时 `Repair Task` / affected capability proof，不创建新的长期 Requirement / Stage / Decision；
- 未受 Repair Boundary 影响的原 Stage Execution Contract 保持有效且只读。

## Compilation

### 1. Restore

读取：

- Repair Handoff；
- original canonical Stage Execution Contract；
- relevant Product / Architecture / Stage authority；
- current Repository Reality；
- relevant evidence / tests。

### 2. Validate Handoff

确认 Handoff 明确提供并可执行：

- `Frozen Finding Set` 可定位；
- `Repair Target State` 可判真假；
- `Allowed Repair Boundary` 足够且未越权；
- `Required Delete / Remove` 明确；
- `Required Proof` 可执行；
- `Repair Stop Gate` 可机械判断；
- 没有新 Product / Architecture decision。

若需要扩大上游 authority：`BLOCKED`，按 owner Route；不得自行扩 Handoff。

### 3. Compile Repair Implementation Shape

只在 Handoff boundary 内编译：

- Touched Domains / Modules；
- Ownership；
- Required Reuse / Existing Authorities；
- Allowed Dependencies；
- Forbidden Bypasses；
- State / Side-effect Flow；
- Expected Repair Change Boundary；
- Required Delete / Remove。

### 4. Compile Repair Tasks

使用正常 Task 粒度与字段语义。显示标签可用：

`Repair Task 1 / 2 / ...`

它们只是 Repair Workspace 内的临时施工标签，不进入长期 Stage object model。

每项仍必须有：

- Upstream / Finding Basis；
- Goal；
- Reasoning；
- Implementation Constraints（适用时）；
- Prerequisites；
- precise Targets；
- Actions；
- Operational Work（适用时）；
- Local Proof；
- Expected Result；
- Done When；
- parallel / Delegation fields（Gate 通过时）。

详细字段继续由现有 `slice-task-design.md`、`reasoning-policy.md`、`delegation-policy.md`、`parallel-construction.md` 负责；Repair Mode 不复制第二套 schema。

### 5. Verification

把 Verifier 的 `Required Proof` 编译到最小充分位置：

- Repair Task Local Proof；
- affected Slice / capability proof；
- Finding resolution evidence；
- Direct Regression；
- required Human / External evidence（适用时）。

不得削弱 Handoff Required Proof，也不默认重跑未受影响 Stage Slices。

### 6. Dry Run

机械验证：

`Repair Handoff → Repair Tasks → Required Target State → Required Proof → Stop Gate`

无 Handoff basis 的 action 必须移除。

## STOP / Escalation

Repair Planning 满足以下任一必须停止并 Route：

- 需要新 Product fact / acceptance；
- 需要新/改长期 Domain Owner / Semantic Authority / core boundary / dependency；
- 需要改变 Stage Scope / Exit；
- Handoff boundary 不足以合法修复；
- 新动作无法追溯到 Frozen Finding / shared root cause / required proof / required delete-remove。

不得因为“已经知道怎么修”绕过上游。

## Stage Reconciliation

只有 Stage Verifier 输出：

`REPAIR VERIFIED`

以及 bounded `Stage Reconciliation Contract` 后，Repair Mode 才可以修改 canonical Stage Execution Contract。

Reconciliation 输入：

- canonical Stage Execution Contract；
- Repair Handoff；
- Repair Execution；
- Repair Evidence；
- final Repository Reality；
- Reconciliation Contract。

规则：

- 只改被 repair 实际失效的 sections / Tasks；
- 未受影响内容保持有效；
- superseded plan 直接删除/替换；
- 不 append Finding / patch / revision chronology；
- 不保留 old/new 双版本、supplement、临时 Repair Task ID；
- 输出仍必须符合 `docs-spec.md` 的正常 Stage Execution Contract 结构。

完成后把 canonical Stage 文档交回 Stage Verifier 做 bounded Reconciliation Check。

## Historical Stage

如果 Handoff 指向的 Stage 在 Repair Cycle 开始前已经是正式 frozen historical Stage：

`BLOCKED`

不得改历史合同。Route 上游创建新的 maintenance / repair work unit。

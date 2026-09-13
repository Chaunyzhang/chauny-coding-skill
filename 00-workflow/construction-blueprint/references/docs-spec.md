# Execution Contract Docs Spec

本文件是 `docs/blueprint/stages/Stage-<N>.md` 的唯一结构 owner。每个 Stage 恰好一份合同；不同 Stage 可并存。已完成 Stage 的合同冻结为后续 Preservation / Direct Regression 输入，不再改写，也不并入当前合同。

## 文档规则

- 不复制 Product Definition、Architecture、Decision、Engineering Standards 的长正文，只引用施工所需当前事实。
- Blueprint 只编号 Slice-n / Task-n；Atom/Requirement/Decision/Stage 沿用上游，Acceptance/Preservation/Regression/Operational Obligation 不另编号。
- 失效计划直接删除，不保留 INVALIDATED、Task 墓地、supplement、parallel contract 或长篇 Revision Log；Stage 完成事实由 Stage Baseline / verifier evidence 承担，不靠保留废弃计划。
- 临时研究只能放 `.workbench/`，交付前删除或把有效结论并回合同。
- Path / Symbol / Command 优先于泛述。

## 固定骨架

```markdown
# Stage-n — Execution Contract

## 1. Authority
## 2. Objective
## 3. Entry State
## 4. Target State
## 5. Scope
## 6. Traceability
## 7. Slices
## 8. Execution Graph
## 9. Tasks
## 10. Verification
## 11. Exception Routing
## 12. Completion
```

不为单一字段新建文档。

## 1. Authority

```text
Stage:
Stage Contract:
Requirements:
Binding Atoms:          # 仅 Current Stage binding
Decisions:
Architecture:
Engineering Standards:
External Services:
Operational Baseline:   # 适用时
Status: DRAFT | READY | BLOCKED
```
只列引用与状态，不复制 Decision rationale。

## 2. Objective

2–6 句话说明 Stage Outcome、蓝图交付和最终 Visible Delta；不写背景故事。

## 3. Entry State

写经过仓库验证、后续 Task 真正依赖的现实：当前行为、关键 Path/Symbol/Schema、provider/config/migration、直接依赖、与 Stage Contract 的兼容差异。不是全仓审计。

## 4. Target State

把 Exit State 转成真假可判的 runtime/UI/API/data、persistence/state transition、architecture delta、triggered operational result、preservation/regression 与 Stop Rule。

## 5. Scope

```text
Change Set
Creation Set
Preservation / Direct Regression
Explicit Non-Scope
Implementation Shape
```

Implementation Shape 仅写适用项：
```text
Touched Domains / Modules:
Ownership:
Required Reuse / Existing Authorities:
Allowed Dependencies:
Forbidden Bypasses:
State / Side-effect Flow:
Expected Change Boundary:
```
尽量带 Path/Symbol/authority reference；不建立重复的完整范围分类体系。

## 6. Traceability

用紧凑表：
| Upstream basis | Construction | Verification |
|---|---|---|
| Requirement / Atom / Acceptance / Decision / Operational item | Slice/Task | Local/Slice/Stage proof |

规则：
- 每个当前上游义务有施工 + 验证落点。
- 每个 binding Atom 有真实 construction + verification coverage；只有 ID 引用不算。
- 每个 Task 至少反向映射一个上游义务。
- 不创建 AC-n / Evidence-n。

## 7. Slices

```text
### Slice-n — <结果型名称>
Upstream Basis:
Outcome:
Real Entry / Caller:
Vertical Path:
Real Dependencies:
Tasks:
Capability Test:
Pass Condition:
```
不写不适用空字段。

## 8. Execution Graph

表达真实依赖、parallel-safe 和 fan-in。存在多人并行收益时追加：
```text
Parallel Work Recommendation
Recommended concurrent workers: <N>
Window A/B...:
- Task/Slice
- Prerequisite
- Write Surface
- Independent commit
Fan-in:
...
```
没有收益时：`Parallel Work Recommendation: Stay sequential`

Window 只是 Human 展示标签。详细 parallel 规则见 `parallel-construction.md`。

Delegation 与 Parallel Work 分离：默认不写任何 Delegation 段，即 Root 直接施工；只有 `delegation-policy.md` Gate 通过才在对应 Task/Slice 附：
```text
Delegation
Purpose:
Scope:
Deliverable:
Read / Write Boundary:
Expected Wall-clock Effect:
Fan-in:
Recursive Spawn: No
```
不要给所有 Task 填 `Delegation: No`。

## 9. Tasks

```text
### Task-n — <变化结果>
Slice:
Upstream Basis:
Goal:
Reasoning: Low (0–4) | Medium (5–10)
Criticality: Sensitive | Critical       # 仅适用时
Implementation Constraints:             # 仅触及 owner/authority/boundary/reuse 时
Prerequisites:
Targets:
Actions:
Operational Work:                       # 仅适用时
Local Proof:
Expected Result:
Done When:

# parallel-safe 时追加 parallel fields
# Delegation Gate 通过时追加 Delegation block
```

Task 详细字段语义只由 `slice-task-design.md` 定义；Reasoning 只由 `reasoning-policy.md` 定义。正式合同禁止 High/XHigh。

## 10. Verification

组织为：
- Task Local Proofs：只补充 Task 本文看不清的共用说明。
- Slice Capability Tests：每 Slice 的真实能力证据。
- Stage Module Test：Outcome、Acceptance、Direct Regression、Operational obligations、Stop Rule。
- Verification Authority：仅需时标 `Agent | Human | External`。

用户型 Stage 的 Hands-on Steps 可嵌入 Stage Module Test，不另造 ID。详细策略见 `verification.md`。

## 11. Exception Routing

只写 `Owner: Blueprint | Architecture | Product` 与当前 Stage 特别可能出现的触发条件；不要创建其他状态体系。

## 12. Completion

```text
Status: READY | BLOCKED
```

READY 条件应引用主 Skill Completion Gate。BLOCKED 使用：
```text
Owner:
Gap:
Evidence:
Blocks:
Required Resolution:
```

## 防乱检查

以下任一出现即重写：
- 同一 Current Stage 有第二份权威蓝图。
- Capability/R/H/ES/AC/EVID 等新编号体系。
- Task 无上游依据或精确 Target。
- “增加埋点 / 完善错误处理 / 补测试”作为无落点 Action。
- 不适用 observability 被逐类写 N/A。
- 全量 test/E2E/真机被机械塞进每 Task。
- 主能力仅 Mock 成立。
- 失效 Task 留在正文做历史说明。

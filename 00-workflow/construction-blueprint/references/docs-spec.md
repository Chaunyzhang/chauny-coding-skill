# Execution Contract Docs Spec

本文件规定 `docs/blueprint/stages/Stage-<N>.md` 的结构：每个 Stage 一份合同，同一 Stage 只有一份。

## 原则

1. 每个 Stage 只维护一份权威 Execution Contract：`docs/blueprint/stages/Stage-<N>.md`；不同 Stage 的合同互不合并。
2. 不复制 Product Definition、Architecture、Decision 或 Engineering Standards 的长篇正文。
3. 只写施工所需的当前有效事实。
4. 删除失效计划，不保留 `INVALIDATED`、旧 Task 墓地或平行补丁文档。
5. Blueprint 自己只编号 `Slice-n`、`Task-n`。
6. Atom-n、Requirement-n、Decision-n、Stage-n 沿用上游编号。
7. Acceptance、Preservation、Regression、Operational Obligation 不另发号。
8. 路径、Symbol、Command 优先于泛泛叙述。

## 文件

固定：

`docs/blueprint/stages/Stage-<N>.md`（`<N>` = Stage 序号）

如果既有项目已有明确的等价路径，可沿用，但必须保持「一个 Stage 恰好一份」；已完成 Stage 的合同作为历史输入保留，不并入当前合同。

临时研究文件只能放 `.workbench/`，交付前删除或把有效结论合并回合同。

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
## Delegation Recommendation

默认不写任何 Delegation 段，表示 Root 直接施工。

只有 Blueprint 通过 Delegation Gate 时，才在对应 Task / Slice 附：

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

`Parallel Work Recommendation` 与 `Delegation` 是不同机制：

- Parallel Work：给人类 / 多窗口。
- Delegation：给单个 Root Agent 是否创建新模型上下文。

## 9. Tasks
## 10. Verification
## 11. Exception Routing
## 12. Completion
```

不要为了一个字段单独新增文档。

## 1. Authority

只列引用和当前状态：

```markdown
## 1. Authority

Stage: Stage-2
Stage Contract: docs/architecture/stages/Stage-2.md
Requirements: Requirement-3, Requirement-5
Binding Atoms: Atom-12, Atom-14, Atom-31  # 仅 Current Stage binding 语义
Decisions: Decision-1, Decision-4
Architecture: ARCHITECTURE.md § ...
Engineering Standards: ENGINEERING_STANDARDS.md § API, § Testing
External Services: EXTERNAL_SERVICES.md § ...
Operational Baseline: OBSERVABILITY.md § ...  # 适用时
Status: DRAFT | READY | BLOCKED
```

不复制 Decision rationale。

## 2. Objective

用 2–6 句话说明：

- Stage Outcome。
- 当前蓝图真正交付什么。
- 最终 Visible Delta。

不要写背景故事。

## 3. Entry State

记录经过仓库验证的施工起点：

- 当前行为。
- 关键 Path / Symbol / Schema。
- 当前 provider / config / migration 状态。
- 直接依赖。
- 已知与 Stage Contract 的兼容差异。

只写 Current Stage 需要的现实，不做全仓审计。

## 4. Target State

把 Exit State 转成可判真假条件：

- runtime / UI / API / data 结果。
- persistence / state transition。
- architecture delta。
- triggered operational result。
- preservation / direct regression。
- Stop Rule。

## 5. Scope

建议只保留：

### Change Set
### Creation Set
### Preservation / Direct Regression
### Explicit Non-Scope
### Implementation Shape

`Implementation Shape` 不是新对象，只写本 Stage 当前施工需要的约束：

```text
Touched Domains / Modules:
Ownership:
Required Reuse / Existing Authorities:
Allowed Dependencies:
Forbidden Bypasses:
State / Side-effect Flow:
Expected Change Boundary:
```

不适用项省略。

每项尽量带 Path / Symbol / authority reference。

不要建立与 Stage Contract 重复的完整范围分类系统。

## 6. Traceability

使用紧凑表：

| Upstream basis | Construction | Verification |
|---|---|---|
| Requirement-3 | Slice-1 / Task-1, Task-2 | Slice-1 Capability Test |
| Atom-12: AI 获得引用内容 | Task-2 context assembly | Slice-1 Capability Test |
| Stage Acceptance: 用户可完成 X | Slice-1 | Stage Module Test |
| Decision-2 | Task-1 | Task-1 Local Proof |
| Operational: payment audit | Task-3 | Slice-2 Capability Test |

规则：

- 每个当前上游义务至少有施工与验证落点。
- 每个 binding Atom 必须有真实 construction coverage 与 verification coverage；只有 ID 引用不算覆盖。
- 每个 Task 必须至少出现一次。
- 不创建 AC-n / Evidence-n。

## 7. Slices

每个 Slice：

```markdown
### Slice-1 — <结果型名称>

Upstream Basis:
Outcome:
Real Entry / Caller:
Vertical Path:
Real Dependencies:
Tasks:
Capability Test:
Pass Condition:
```

不要写不适用空字段。

## 8. Execution Graph

例如：

```text
Slice-1
Task-1 -> Task-2 [parallel-safe]
       -> Task-3 [parallel-safe]
Task-2, Task-3 -> Slice-1 Capability Test

Slice-2
Task-4 -> Task-5 -> Slice-2 Capability Test
```

并行只在真实依赖允许时标注。

存在值得多人同时施工的机会时，在图后增加 `Parallel Work Recommendation`：

```text
Recommended concurrent workers: 2

Window A:
- Task-2
- Write Surface: ...
- Independent commit: Yes

Window B:
- Task-3
- Write Surface: ...
- Independent commit: Yes

Fan-in:
- merge both
- run Slice-1 Capability Test
```

没有值得并行的机会时：

`Parallel Work Recommendation: Stay sequential`

Window A/B 只是人类展示标签，不是正式项目对象。

## Delegation Recommendation

默认不写任何 Delegation 段，表示 Root 直接施工。

只有 Blueprint 通过 Delegation Gate 时，才在对应 Task / Slice 附：

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

`Parallel Work Recommendation` 与 `Delegation` 是不同机制：

- Parallel Work：给人类 / 多窗口。
- Delegation：给单个 Root Agent 是否创建新模型上下文。

## 9. Tasks

每个 Task：

```markdown
### Task-1 — <变化结果>

Slice:
Upstream Basis:
Goal:
Reasoning: Low (0–4) | Medium (5–10)
Criticality: Sensitive | Critical   # 仅适用时
Implementation Constraints:          # 仅触及 owner / authority / boundary / required reuse 时
Prerequisites:
Targets:
Actions:
1.
2.
Operational Work:   # 仅适用时
Local Proof:
Expected Result:
Done When:
```

`Implementation Constraints` 只写 Stage Implementation Shape 对当前 Task 的最小约束；不触及相关边界时省略。

`Targets` 需要精确。

`Actions` 是状态改变动作，不是 rationale。

`Local Proof` 只证明本 Task；可以是静态 / 既有证据，不要求每个 Task 新增测试。

`Reasoning` 由 Blueprint 编译期评分后写入；Construction 直接消费，不重新做 10 维打分。

禁止在正式合同中出现 `High / XHigh` Task。Score >10 时先修 Blueprint，再发布。

`Criticality` 只在高后果边界需要时填写，不参与 Reasoning Score。

## 10. Verification

三部分：

### Task Local Proofs
只列不能从 Task 本文直接看清的共用 proof 说明；不要为了格式给每个 Task 添加新测试。

### Slice Capability Tests
每个 Slice 一条真实能力测试。

### Stage Module Test
验证 Stage Outcome、Acceptance、Direct Regression、适用 Operational Obligation、Stop Rule。

用户型 Stage 可以在 Stage Module Test 内包含 Hands-on Steps；不另造 `Hands-on Acceptance-n` 对象。

### Verification Authority
只在需要时标注：
- Agent
- Human
- External

UI 审美 /视觉质感等 Human-only 结论不得写成 Agent PASS 条件。

## 11. Exception Routing

只写三类 Owner：

- Blueprint
- Architecture
- Product

每类列本 Stage 特别可能出现的触发条件。

## 12. Completion

```markdown
Status: READY | BLOCKED

READY when:
- all binding Atoms have construction + verification coverage
- Implementation Shape is explicit where ownership / authority / dependency boundaries matter
- all Tasks are Reasoning Low / Medium
- no Task score >10
- no unresolved design decision remains inside Construction
- ...
```

BLOCKED 时：

```text
Owner:
Gap:
Evidence:
Blocks:
Required Resolution:
```

## 防乱规则

以下任一出现即视为合同需要重写：

- 同一 Current Stage 存在第二份权威蓝图。
- Capability-n / R-n / H-n / ES-n / AC-n / EVID-n 等新体系重新出现。
- Task 没有上游依据。
- Task 没有精确 Target。
- “增加埋点”“完善错误处理”“补测试”作为无落点 Action。
- 不适用 Observability 被逐类写 N/A。
- 全量 test / E2E /真机验证被机械塞进每个 Task。
- 主产品路径只有 Mock 成立。
- 失效 Task 仍留在正文做历史说明。

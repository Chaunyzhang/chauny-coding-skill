# Execution Contract Docs Spec

本文件规定 `docs/blueprint/EXECUTION_CONTRACT.md` 的唯一结构。

## 原则

1. 当前 Stage 只维护一份权威 Execution Contract。
2. 不复制 Product Definition、Architecture、Decision 或 Engineering Standards 的长篇正文。
3. 只写施工所需的当前有效事实。
4. 删除失效计划，不保留 `INVALIDATED`、旧 Task 墓地或平行补丁文档。
5. Blueprint 自己只编号 `Slice-n`、`Task-n`。
6. Requirement-n、Decision-n、Stage-n 沿用上游编号。
7. Acceptance、Preservation、Regression、Operational Obligation 不另发号。
8. 路径、Symbol、Command 优先于泛泛叙述。

## 文件

默认：

`docs/blueprint/EXECUTION_CONTRACT.md`

如果既有项目已经有明确等价唯一合同路径，可沿用，但同一 Current Stage 只能有一份。

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

每项尽量带 Path / Symbol。

不要建立与 Stage Contract 重复的完整范围分类系统。

## 6. Traceability

使用紧凑表：

| Upstream basis | Construction | Verification |
|---|---|---|
| Requirement-3 | Slice-1 / Task-1, Task-2 | Slice-1 Capability Test |
| Stage Acceptance: 用户可完成 X | Slice-1 | Stage Module Test |
| Decision-2 | Task-1 | Task-1 Simple Test |
| Operational: payment audit | Task-3 | Slice-2 Capability Test |

规则：

- 每个当前上游义务至少有施工与验证落点。
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

## 9. Tasks

每个 Task：

```markdown
### Task-1 — <变化结果>

Slice:
Upstream Basis:
Goal:
Prerequisites:
Targets:
Actions:
1.
2.
Operational Work:   # 仅适用时
Simple Test:
Expected Result:
Done When:
```

`Targets` 需要精确。

`Actions` 是状态改变动作，不是 rationale。

`Simple Test` 默认只验证本 Task。

## 10. Verification

三部分：

### Task Simple Tests
只列不能从 Task 本文直接看清的共用说明。

### Slice Capability Tests
每个 Slice 一条真实能力测试。

### Stage Module Test
验证 Stage Outcome、Acceptance、Direct Regression、适用 Operational Obligation、Stop Rule。

用户型 Stage 可以在 Stage Module Test 内包含 Hands-on Steps；不另造 `Hands-on Acceptance-n` 对象。

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

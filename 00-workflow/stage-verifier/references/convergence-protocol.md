# Convergence Protocol

> Owner: Stage Review / Repair / Fix Review 的继续、停止、冻结与封口规则。目标不是“提醒模型克制”，而是让任何继续动作都必须先证明合法。

## Core Principle

Initial Review 需要完成固定审查覆盖；Finding Freeze 之后默认状态反转：

> **Default = STOP / ROUTE. Continue requires admission.**

“还能做点什么”不是继续理由。

## Review Cycle State Machine

```text
INITIAL_REVIEW
  → FINDINGS_FROZEN
  → REPAIR_HANDOFF (if needed)
  → REPAIR_EXECUTING
  → FIX_REVIEW
  → REPAIR_VERIFIED
  → STAGE_RECONCILIATION
  → PASS_SEALED
  → CLOSED
```

任何 Product / Architecture authority gap 可从 repair states 路由上游；不得在原 cycle 内自行填空。

## Initial Review Boundary

首次审查是“固定维度全量”，不是“全仓库无限搜索”。

每个额外动作必须关闭一个明确未决项：

- mandatory review dimension；
- binding Atom / Acceptance / architecture constraint；
- Live Uncertainty；
- 需要定位的 authority / execution path。

若动作目标只是“找更多可能问题”，不允许执行。

## Finding Freeze

首次结论冻结 `F-01...F-N`。

之后不允许普通 Finding 增长。只允许：

- Frozen Finding 状态更新；
- Repair 直接引入的 `REGRESSION-XX`；
- 上游 Route；
- Evidence Block；
- Stage Reconciliation。

### Freeze Break

冻结后如果**外部新证据**证明一个原已存在的 Current Stage BLOCKER，使当前 cycle 的基础结论客观失效：

```text
REVIEW CYCLE INVALIDATED — NEW REVIEW REQUIRED
```

关闭旧 cycle，从新的 Initial Review 重新冻结。

不得通过 discretionary search 主动制造 Freeze Break；不得把新 blocker 偷塞进旧 Finding Set。

## Action Admission Gate

Finding Freeze 后，执行任何 read / search / test / profiler / planning / repair / verification / documentation action 前，内部必须形成：

```text
Action Basis:   FROZEN_FINDING | SHARED_ROOT_CAUSE | REQUIRED_PROOF | REPAIR_REGRESSION | UPSTREAM_ROUTE | STAGE_RECONCILIATION
Bound To:       F-xx / REGRESSION-xx / named upstream gap / reconciliation target
Question:       当前具体不知道什么或必须改变什么？
Decision Impact:结果 A/B 将改变什么判断或施工动作？
Max Scope:      允许触及的最远边界
Stop After:     哪个可判真假的状态一旦成立就停止
```

任一字段空泛或无法填写 ⇒ Action inadmissible。

非法 basis：

- 顺便；
- 保险起见；
- 更完整；
- 最佳实践；
- 附近还有类似问题；
- 未来可能；
- 已经打开这个文件；
- “再确认一次”但没有新 uncertainty。

## Repair Boundary

合法 Repair Surface：

```text
Frozen Findings
+ Shared Root Causes
+ Necessary Mechanical Consequences
+ Required Delete / Remove
+ Direct Regression Surface
+ Required Proof
```

不是“最小 diff”；是达到 Required State 所需的最小**完整**修复边界。

### New Observation Classification

Repair / Fix Review 期间看到新事实时，先分类：

1. Frozen Finding 的组成部分 → in scope。
2. 多 Finding 的共同根因 → in scope。
3. Repair 直接引入 Current Stage blocker → `REGRESSION-XX`。
4. 需要新的 Product / Architecture / Stage decision → Route，停止 Repair。
5. 与本轮 Repair 无关的 confirmed defect → `Deferred Observation`；不得修、不得进 Frozen Finding Set。
6. Hypothetical risk / polish / smell → 不行动。

`Deferred Observation` 只能存在于当前 Repair Workspace / chat，不能变成 canonical Stage requirement 或长期 backlog，除非上游后续明确接收。

## Verification Admission

新 test / build / migration / device / profiler / full-suite check 仍必须回答：

1. 当前 Live Uncertainty 是什么？
2. 这个证据证明哪个 Frozen Finding / Required State / Regression / Reconciliation target？
3. 现有 evidence 为什么不足？
4. 失败会改变什么判断？

答不出来 ⇒ 不运行。

已有新鲜、可信、范围匹配证据 ⇒ 直接消费；不为 reviewer 自己“亲眼再看一次”重复。

## MUST STOP

任一为真，当前行动链必须停止：

- 当前 Question 已有足够证据；
- Action Ticket 的 `Stop After` 已成立；
- 没有合法 Action Basis；
- 下一步会越过 Max Scope / Repair Boundary；
- 下一步需要上游 authority；
- Frozen Findings + Direct Regression 已清零且 Required Proof 足够；
- `REPAIR VERIFIED` 已成立；
- Reconciliation Check 已通过；
- 最终 PASS 已输出。

Stop 后继续 search / review / cleanup / hardening / equivalent proof 是 violation。

## Repair Verified Boundary

当全部 Frozen Findings / allowed REGRESSION 达到 Required State，且 required proof / direct regression 足够：

```text
REPAIR VERIFIED
```

此状态禁止：

- 再改实现；
- 顺便 cleanup；
- 再加 test；
- 重新打开 Findings；
- 重新扫描代码。

唯一合法下一步是 `STAGE_RECONCILIATION`。

## PASS Seal

最终：

```text
PASS — Stage Review Closed
```

它封闭当前 cycle。

只有：

- 用户明确新审查；
- PASS 后有新 implementation change；
- PASS 后有新的外部 evidence 实质推翻原依据；

才可开启**新** cycle。禁止续接旧 cycle。

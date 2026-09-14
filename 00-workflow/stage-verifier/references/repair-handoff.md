# Repair Handoff Contract

> Owner: Stage Verifier → Construction Blueprint 的冻结修复输入。它不是施工蓝图，不定义 Task / Slice / Delegation / Parallel / Reasoning schema。

## Purpose

把：

`Frozen Findings + Upstream Authorities + Repository Anchors`

冻结成：

`Repair Target State + Allowed Repair Boundary + Required Proof`

然后交给 Construction Blueprint 的 Repair Mode，以其正常施工颗粒度编译临时 Repair Execution Contract。

## When

生成：

- `FIX`
- `REPLAN_BLUEPRINT`，且 Product / Architecture / Stage Contract 仍正确

不生成：

- `PASS`
- `PRODUCT CHANGE`
- `REPLAN_ARCHITECTURE`
- 纯 `VERIFICATION BLOCKED`

## Authority

Handoff 必须重新确认：

- Product Definition / binding Atoms；
- Architecture / Engineering Standards / Owner / Semantic Authority；
- Current Stage Contract；
- original Construction Blueprint；
- Frozen Finding Set；
- 当前 Repository Reality。

优先级：

`Product → Architecture → Stage Contract → Construction Blueprint authority → Repair Handoff boundary → Repair Execution → Implementation`

Handoff 无权改变上游。

## Root Cause Synthesis

不要机械：`F-01 → patch A`。

先建立：

`Finding → Shared Root Cause → Correct Authority / Boundary → Required System State`

同根因 Findings 进入同一个 Root Cause Group；症状修复服从根因恢复。

格式：

```text
Root Cause Group A
Findings: F-01, F-03
Root Cause:
Correct Authority / Boundary:
Required System State:
```

## Required Contract

```text
Target Workflow: Construction Blueprint
Mode: Repair
Stage:

Frozen Finding Set:
- F-01 ...

Root Cause Groups:
...

Upstream Basis:
- Product / Atom
- Architecture / Engineering Standard
- Stage Contract
- Original Blueprint obligation

Repair Target State:
- 可判真假的最终状态

Allowed Repair Boundary:
- root causes
- necessary mechanical consequences
- affected paths / symbols / schemas / tests

Required Delete / Remove:
- superseded bypass / duplicate authority / fallback / alias / dead test / stale config

Preservation / Direct Regression:
- 必须保持的既有行为

Explicit Non-Scope:
- Concern
- future hardening
- unrelated cleanup
- unrelated confirmed defects

Required Proof:
- Finding resolution conditions
- affected capability proof（适用时）
- direct regression

Repair Stop Gate:
- 可机械判断的停止条件

Repository Anchors:
- relevant path / symbol / caller / schema / test / runtime evidence
```

## Target State Rules

Target State 必须描述“修完后什么为真”，不提前规定无授权 implementation detail。

好：

> Wallet 恢复唯一 balance mutation authority；Purchase-local mutation 与重复 insufficient-balance decision 消失；受影响 Purchase capability 重新成立。

差：

> 新建 WalletRepairManagerV2 并把逻辑搬进去。

## Boundary Rules

允许：

- Frozen Finding root cause；
- 达成 Target State 必需的 mechanical change；
- superseded path 删除；
- direct regression / required proof。

禁止：

- Concern；
- future hardening；
- unrelated refactor；
- hypothetical risk；
- 新 Product / Architecture decision；
- 把 Deferred Observation 偷进本轮施工。

## Delete Means Absence

正确路径替代错误路径时，必须列 `Required Delete / Remove`。除非上游有明确 compatibility / migration / audit responsibility，不保留“旧方案备用”、duplicate authority、deprecated active path、commented implementation 或 obsolete tests。

## Verification Intent

Verifier 只冻结“必须证明哪些事实”，不替 Construction Blueprint 编译详细 proof placement。

Required Proof 可以包含：

- local correctness；
- affected Slice capability；
- Finding resolution；
- direct regression；
- required migration / external / Human evidence。

Construction Blueprint 决定这些证据如何放入具体 Repair Tasks / integration points，但不得削弱 Required Proof。

## Handoff Stop

Repair Handoff Contract 完整后，Stage Verifier 必须停止 repair planning：

```text
REPAIR PLANNING REQUIRED — Route to Construction Blueprint / Repair Mode
```

如果 Construction Blueprint 不可用，保持 Handoff 并停止。不得在 Stage Verifier 内复制或模拟其 task schema。

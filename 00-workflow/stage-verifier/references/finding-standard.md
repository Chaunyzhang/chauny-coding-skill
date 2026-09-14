# Finding & Verdict Standard

> Owner: Finding Gate、Concern、Layer、Evidence、Required State 与 repair 期间的新观察分类。

## Finding Gate

首次 Review 中，Finding 必须全部满足：

```text
Current Stage relevance?
Confirmed evidence?
Named violated authority / rule?
Material reason?
Required state clear?
Verification possible?
```

任何一项 NO ⇒ 不是 Frozen Finding。

## Concern

`CONCERN` 是具体质量信号，但没有达到 Finding Gate。

允许：

- complexity sensor；
- change radius smell；
- public API 似乎偏宽；
- 无当前 scale evidence 的潜在效率问题。

不允许：

- 泛泛建议；
- “可以更优雅”；
- “最好重构”；
- “未来可能”。

CONCERN 不进入 Repair Boundary，也不授权继续探索。

## Layer

- `Implementation`：上游正确，实际代码偏离。
- `Blueprint`：施工形状、task/proof path 本身错误或漏约束。
- `Architecture`：长期 ownership / authority / boundary / invariant 缺失或错误。
- `Product`：产品事实、Rule、Atom、Acceptance 改变或冲突。
- `Evidence`：缺证据，无法判当前状态。

## Evidence

Finding 必须基于可定位事实，例如：

- file + symbol + actual behavior；
- runtime / test failure；
- dependency edge；
- duplicate authority sites；
- query / work pattern；
- state flow；
- binding Atom uncovered；
- explicit missing evidence。

“可能会有问题”不是 Finding Evidence。

## Required State

Required State 描述修复后必须成立的状态，不越权规定具体施工方案。

好：

> Reward calculation 只由现有 RewardPolicy 决定；当前第二套判断必须消失或变成纯调用。

差：

> 必须新建 RewardRuleEngineV2Factory。

## Frozen Finding Fields

```text
ID:
Layer: Implementation | Blueprint | Architecture | Product | Evidence
Dimension: Semantic | Correctness | Efficiency | Semantic Unity | Modular Integrity | Structural Health | Maintainability | Scope | Evidence
Severity: BLOCKER | MAJOR
Location:
Expected / Authority:
Actual Evidence:
Why It Matters:
Required State:
Verification:
```

`REGRESSION-XX` 只在 repair 直接引入新的 Current Stage blocker 时使用。

Severity：

- `BLOCKER`：当前 Stage 无法正确完成、安全完成或被充分验证。
- `MAJOR`：存在明确产品、架构、蓝图或实现质量违反，当前 Stage 不应接受。
- `REGRESSION`：仅用于 repair 直接引入的 Current Stage 阻断性问题。

没有 MINOR Finding；非阻断 polish 归 Concern 或不记录。

## Finding Freeze

首次 Review 结束后，Frozen Finding 的内容不再扩张。

修复期间只更新 resolution status：

`RESOLVED | PARTIALLY RESOLVED | UNRESOLVED`

Repair Planning 不得把 Finding 的 Required State 偷换成新的产品/架构决定。

## Deferred Observation

Finding Freeze 后看到一个**与本轮 Repair 无关**但有证据的真实 defect：

```text
Deferred Observation:
Location:
Evidence:
Why out of current Repair Boundary:
```

它：

- 不进入 Frozen Finding Set；
- 不进入 Repair Handoff / Repair Execution；
- 不授权额外搜索或修复；
- 只存在于当前 chat / Repair Workspace；
- 只有上游后续显式接收，才进入新的正式 work unit。

不要用 Deferred Observation 记录 hypothetical risk / polish / smell。

## Freeze Break Is Not a New Finding

若冻结后出现新的**外部 evidence**，证明一个原本就存在的 Current Stage BLOCKER，足以推翻当前 Review Cycle：

`REVIEW CYCLE INVALIDATED — NEW REVIEW REQUIRED`

关闭旧 cycle，重新 Initial Review；不要把它追加成 F-N+1。

## Finding vs Repair Handoff

Finding 只回答：

- 哪里错；
- 违反什么；
- 为什么重要；
- 必须恢复到什么状态；
- 如何确认状态恢复。

Frozen Findings 形成后，Repair Handoff 才统一回答：

- 哪些 Findings 共享根因；
- 哪个 authority / boundary 必须恢复；
- Repair Target State；
- Allowed Repair Boundary；
- Required Delete / Remove；
- Required Proof / Stop Gate。

详细施工 Task 由 Construction Blueprint / Repair Mode 编译，而不是 Finding 或 Stage Verifier 编译。

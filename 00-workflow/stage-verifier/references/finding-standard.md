# Finding & Verdict Standard

> 本文件可独立使用：可直接作为任意阶段审查的 Finding 判定标准；在 stage-verifier 流程中，由 `SKILL.md` 的「Finding Standard」章节加载。

## Why

Reviewer 最容易出现两个坏习惯：

1. 把个人偏好当缺陷。
2. 把所有 smell 都升级成必须修。

本标准要求 Finding 可证明、可修、可验证。

## Finding Gate

必须全部满足：

```text
Current Stage relevance?
Confirmed evidence?
Named violated authority / rule?
Material reason?
Required state clear?
Verification possible?
```

任何一项 NO：

不是 Frozen Finding。

## Concern

`CONCERN` 是“值得知道但没有达到 Finding Gate”的具体质量信号。

允许：

- 复杂度 sensor。
- change radius smell。
- 新 public API 似乎偏宽。
- 当前没有实际 scale 证据的潜在效率问题。

不允许：

- 没证据的泛泛建议。
- “可以更优雅”。
- “最好重构”。
- “未来可能”。

CONCERN 不进入 repair loop。

## Layer

### Implementation

上游正确，code 偏离。

### Blueprint

approved construction shape 本身漏了必要实现约束或语义覆盖。

### Architecture

长期 ownership / authority / boundary / invariant 缺失或错误。

### Product

产品事实变化 / 冲突。

### Evidence

缺证据，无法判正确性。

## Evidence

Finding Evidence 必须是可定位事实：

- file + symbol + relevant behavior
- runtime result
- test failure
- dependency edge
- duplicate authority sites
- query pattern
- state flow
- binding Atom uncovered
- explicit missing evidence

不要写：

> “可能会有问题。”

## Required State

不要直接规定无授权的具体实现方式。

好：

> Reward calculation 只能由现有 RewardPolicy 决定；当前第二套判断必须消失或变成纯调用。

差：

> 必须新建 `RewardRuleEngineV2Factory`。

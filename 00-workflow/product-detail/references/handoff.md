# Handoff Contract

## Chief Architect → Product Detail

至少提供：

- Current Stage-n
- Relevant Requirement-n
- 当前已知产品语义
- 为什么当前信息不足
- 已冻结的相关 Architecture Constraints
- 哪些 Stage Acceptance 无法可靠冻结

不要把技术选型问题伪装成产品问题。

## Product Detail → Chief Architect

返回：

- 被细化的 Requirement-n
- 新增的稳定产品语义
- 对 Stage Scope / Acceptance 的影响
- 对 Architecture / Operational Obligations 的影响（如果有）
- Explicit Exclusions
- 是否改变 Product Definition

若不改变 Product Definition：

`可以继续冻结 / 更新 Stage Contract。`

若改变：

`RETURN TO PRODUCT DESIGNER`

## Blueprint → Product Detail

Blueprint 只能回报具体缺口：

```text
Stage:
Requirement:
Missing Product Semantics:
Why Implementation Cannot Safely Choose:
Downstream Impact:
```

不要把普通实现选择回抛给 Product Detail。

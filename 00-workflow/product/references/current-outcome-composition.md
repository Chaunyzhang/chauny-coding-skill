# Current Outcome Composition

## Purpose

产品阶段必须明确：

> 现在最希望哪个完整产品结果成为现实？

不能把 Capability Map / 一堆 Requirement 直接丢给 Architect，让 Architect 自己猜用户现在最在意什么。

## Current MCO

Current Minimum Complete Outcome 必须描述完整结果，而不是“尽量少的功能”。

至少明确：

- Outcome
- Primary Actors
- Core Journey（产品层概述）
- Must-Have Capabilities
- Current Requirements
- Required Product Rules / Failure Semantics
- Visible Result
- Completion Boundary
- Explicitly Not Current

## Current Requirement Set

Current MCO 对应的 Requirement 必须被显式列出。

例如：

```text
Current Requirements:
- Requirement-2
- Requirement-5
- Requirement-8
```

不是说这些 Requirement 必须在同一个 Stage，也不是说必须按一个业务剧情施工。

## Product Priority / Relationships

产品可以表达：

### Must Together

A 与 B 缺一就无法形成当前产品结果。

### Independent

A、B 都是 Current，但可以分别作为完整能力成立。

### Product Precedence

产品语义要求 B 只有在 A 产品状态存在后才有意义。

这是真产品依赖，不是工程施工顺序。

### Explicitly Not Current

对当前成果没有必要，或已经确认属于 Near / Future。

## 禁止 Product Stage

Product 不创建：

- Stage-n
- Product Stage
- Phase 1 Product
- MVP
- V1 / First Version

只有 Chief Architect 创建 `Stage-n`。

## Architecture-Shaping Future

某些 Near / Future 不属于当前建设，但会改变今天底座。

Product 负责说明：

- 未来产品行为是什么。
- 为什么可能改变角色 / ownership / lifecycle / sync / permission / AI / billing / multi-device / scale 等模型。

Product 不决定技术怎么预留。

## Handoff Index

`Product-Definition.md` 的 Handoff 只做索引，不复制 Atom：

```text
## Handoff to Architecture

Current Minimum Complete Outcome:
...

Current Requirements:
- Requirement-2
- Requirement-5

Product Priority / Relationships:
- ...

Relevant Product Atoms:
- Requirement-2 → Atom-12, Atom-14
- Requirement-5 → Atom-31–38

Explicitly Not Current:
- ...

Architecture-Shaping Future:
- ...

Open Product Questions:
- ...
```

Architect 应读取 Atom 原文。

## Composition Test

交给 Architect 前问：

1. Architect 是否知道现在最重要的产品结果是什么？
2. Architect 是否知道哪些 Requirement 属于当前结果？
3. Architect 是否知道它们之间真正的产品关系，而不是自己推断？
4. Architect 是否能直接找到不可丢失的产品 Atom？
5. 如果 Architect 只看 Definition + Relevant Atoms，是否仍可能合理地实现出“空壳功能”？
6. Product 是否越权规定了 Stage / 技术顺序？

前 4 项 YES、5 和 6 NO，才算可交接。

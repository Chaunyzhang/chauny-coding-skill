# Current Outcome Composition

## Purpose

产品阶段必须明确：

> 现在最希望哪个完整产品结果成为现实？

不能把 Capability Map / Requirement 列表直接交给 Architect，让 Architect 猜当前最重要的产品结果。

## Current MCO

Current Minimum Complete Outcome 描述完整结果，不是“尽量少的功能”。至少明确：

- Outcome
- Primary Actors
- Core Journey（产品层概述）
- Must-Have Capabilities
- Current Requirements
- Required Product Rules / Failure Semantics
- Visible Result
- Completion Boundary
- Explicitly Not Current

Current Requirement Set 必须显式列出，例如：

```text
Current Requirements:
- Requirement-2
- Requirement-5
- Requirement-8
```

这些 Requirement 不因此必须进入同一 Stage，也不代表必须按一个业务剧情施工。

## Product Priority / Relationships

只表达真实产品关系：

- **Must Together**：缺一就无法形成当前产品结果。
- **Independent**：都属 Current，但各自可以完整成立。
- **Product Precedence**：B 的产品语义只有在 A 的产品状态存在后才成立；这不是工程施工顺序。
- **Explicitly Not Current**：当前成果不需要，或已确认属于 Near / Future。

## Product / Architecture Boundary

Product 不创建 `Stage-n`、Product Stage、Phase 1 Product、MVP、V1 / First Version；只有 Chief Architect 创建 `Stage-n`。

Near / Future 即使不在当前建设，也可能 Architecture-Shaping。Product 只说明未来产品行为及其为何可能改变角色、ownership、lifecycle、sync、permission、AI、billing、multi-device、scale 等模型，不决定技术如何预留。

## Handoff

`Product-Definition.md` 的 Handoff 只做索引，不复制 Atom Statement。正式模板见 `document-spec.md`；Architect 应读取 Relevant Atoms 原文。

## Composition Test

交给 Architect 前确认：

1. 当前最重要的完整产品结果清楚。
2. 属于该结果的 Current Requirements 清楚。
3. Requirement 间真实产品关系清楚，而非让 Architect 推断。
4. 不可丢失的产品事实可直接定位到 Relevant Atoms。
5. 只读 Definition + Relevant Atoms 不会合理地产生“空壳功能”。
6. Product 没有越权规定 Stage 或技术顺序。

前 4 项成立，5–6 不成立，才可交接。

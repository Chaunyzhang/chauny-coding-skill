# UI Document Spec

## Canonical Document

项目级长期 UI 权威：

`docs/ui/UI-SYSTEM.md`

它只记录长期复用的设计事实。

推荐结构：

```text
# UI System

## Design Personality
## Design Grammar
### Hierarchy
### Density & Spacing
### Shape
### Surface
### Typography
### Color
### Icon
### Motion
### Interaction & Navigation
### State
### Accessibility

## Tokens
## Core Components
## Reusable Patterns
## Current Exceptions
```

不是每个章节都必须展开很长。

## Current UI Handoff

当前 UI Pass 输出紧凑 Handoff：

```text
Scope
Design Intent
Affected Screens
Structure / Hierarchy
Reuse
New UI
Relevant States
Interaction / Navigation
Motion Intent
Accessibility
System Changes
Constraints / Non-goals
```

Handoff 是下游输入，不是新的编号对象。

## 不写入

- 用户对话全文
- 所有探索 Variant
- 被否定方案
- Agent 推理过程
- 截图逐像素说明
- 普通 padding / radius 讨论
- SwiftUI 语法说明
- 未来尚未进入真实产品的所有 Screen
- 每个 Screen 一份长期 Spec

## 写入判断

删除这条规则后，如果：
- Agent 仍会稳定做出同样设计；
- Component / Screen 不会漂移；
- 用户无需重复解释；
那么通常不需要写入 UI System。


## Project Structure

`UI-SYSTEM.md` 可以记录少量长期 UI 归属原则，但不复制完整 `PROJECT_STRUCTURE`。

顶层目录与模块结构仍由 Architecture 文档负责；UI System 只记录与 UI 设计系统相关的归属约束，例如：

- Feature-local by default
- shared components promotion rule
- DesignSystem dependency direction
- single source of truth for tokens


## Human Review

主观视觉反馈不写成永久 UI System 规则，除非已经被归纳为稳定 Design Grammar。

例如：

Human:
“这个版本太冷。”

不要永久记录原句。

若最终稳定结论是：

`Surface palette uses warm neutrals; cool gray is reserved for disabled/system states.`

则把后者写入 UI System。

Human Review Notes 不需要建立独立长期文档。

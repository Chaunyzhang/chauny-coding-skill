# 设计系统与组件

**何时加载**：存在重复视觉规则、重复组件/Pattern、需要建立或扩展 Design System，或多个页面开始出现漂移时。

> 识图任务：token/component 必须来自跨图片或单图内部的重复规律。近似观测值先聚类再升格为 token；一次性视觉值保持 page-local，不得为了“完整”虚构全局 Design System。

**目标**：把稳定、可复用的设计决定变成系统接口；不要把尚未稳定的想法过早抽象。

## 层级

可按需要使用：

- Foundations / semantic roles
- Tokens
- Primitives
- Components
- Patterns
- Templates / reusable layouts
- Themes

不要求每个项目都有所有层。

## Semantic before primitive

优先让组件依赖语义：

```text
text.secondary
surface.raised
action.primary
border.subtle
status.error
```

而不是直接到处依赖 `gray-400 / blue-500 / 16px`。

Primitive token 可以存在，但业务组件应尽量消费 semantic role。

## Component 定义

重要组件至少按相关性明确：

- Purpose
- Anatomy / slots
- Content constraints
- Properties
- Variants
- States
- Events
- Feedback / recovery
- Layout rules
- Visual treatment
- Adaptation
- Accessibility
- Motion
- Data / action mapping

不要把这份清单机械写满；只写会改变实现或复用边界的项。

## Variant vs State

Variant 表示“它是哪一种”；State 表示“它现在怎样”。

例如 `destructive` 是 Button variant，`pressed/disabled/pending` 是 state。不要为每个 state 复制一个独立组件。

## Pattern

以下常常更适合定义为 Pattern，而不是一个巨型 Component：

- search + filter + result count
- empty state + recovery CTA
- destructive confirmation
- form row + validation
- selection + bulk action

## 上移到 Shared / Design System 的条件

至少满足一项强理由：

- 多处真实复用。
- 需要统一状态/交互/视觉规则。
- 修改时必须跨 feature 一致更新。
- 它代表产品级设计语言，而不是单一业务语义。

否则优先 feature-local。

## 禁止

- 为未来假想复用提前做超通用组件。
- Base UI 里塞业务判断。
- caller 传大量 radius/padding/color/height 来“配置一切”。
- 同义组件多份实现。
- raw color / spacing 在各页面自由漂移。

## 停止条件

当稳定重复规则有唯一权威位置，而 feature-specific 语义仍留在 feature，且新增页面能够复用系统而不是重新发明视觉语言时停止。

---

## Spec 中必须解析 token

Design System 是复用接口，不是让实现者继续挑值的菜单。

交付 `UI-DESIGN-SPEC.md` 时：

- semantic token 必须有唯一权威映射。
- spacing/radius/type/shadow 不得存在多个几乎相同但无语义差别的值。
- 页面不得绕过 token 创建 near-equivalent value。
- 关键组件必须有明确 geometry、visual treatment 和 state rules。

如果已有系统已经定义 `space.3 / radius.control / surface.raised` 等，Spec 使用这些准确名称并说明用途；如果没有系统，则为当前范围建立最小完整 token set。

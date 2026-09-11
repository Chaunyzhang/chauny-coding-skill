# UI Project Structure

本参考定义 UI 代码在真实项目中的归属规则。

目标不是预先创建完整目录树，而是：

> 目录可以暂时不存在；一旦某类 UI 代码出现，就必须有稳定、唯一的归属。

## 1. Authority

项目顶层结构由 Chief Architect / `PROJECT_STRUCTURE` 决定。

UI Designer：

- 不自行增加新的顶层架构体系。
- 不把 UI 设计偏好变成项目架构重构。
- 只在 Architect 已批准结构内部定义 UI 的归属与上移规则。

如果 Architect 已明确：

```text
App/
Features/
DesignSystem/
Core/
Resources/
```

则 UI Skill 遵守。

如果项目使用其他合法结构，则映射本文件的原则，不强制改成示例目录名。

## 2. 默认归属：Feature-local

业务 UI 默认跟 Feature。

例如：

```text
Features/
  Hatch/
    HatchView.swift
    Components/
      EggCard.swift
      HatchProgressView.swift
```

只服务 Hatch 的 UI 不应因为“看起来像组件”而放入全局共享目录。

原则：

> 没有真实跨 Feature 复用证据时，默认留在 Feature。

## 3. Shared / DesignSystem 的准入条件

一个 Component 只有满足以下条件时才考虑上移：

- 被多个 Feature 真实使用。
- 语义一致，而不仅是视觉相似。
- 交互 / State 规则一致。
- 未来变化应该同步发生。
- 上移后不会把业务概念带入 Design System。

例如：

适合上移：

```text
PrimaryButton
CurrencyBadge
AppCard
EmptyState
```

通常不适合上移：

```text
HatchRewardCard
InspirationComposer
PetEvolutionTimeline
```

即使它们“可能以后也会复用”，也先留在所属 Feature。

## 4. Design System 只放全局设计语言

推荐：

```text
DesignSystem/
  Tokens/
    Colors.swift
    Typography.swift
    Spacing.swift
    Radius.swift
    Motion.swift

  Components/
    PrimaryButton.swift
    AppCard.swift
    CurrencyBadge.swift

  Patterns/
    EmptyState.swift
    ErrorState.swift
    LoadingState.swift
```

进入 Design System 的内容必须表达至少一种：

- 全局 Design Grammar。
- 全局 Token。
- 跨 Feature Component contract。
- 跨 Feature interaction / state pattern。

禁止把页面特有值包装成 Token，例如：

```text
hatchHeroTopPadding = 37
```

除非它已经成为可复用的设计规则。

## 5. 依赖方向

默认依赖方向：

```text
DesignSystem
      ↑
Features
      ↑
App
```

Feature 可以使用 Design System。

Design System 不得 import / depend on：

- Hatch
- Store
- Inspiration
- 任意业务 Feature

如果共享 Component 开始需要业务模型才能工作，说明边界可能错误。

## 6. 单一权威位置

同一种设计事实只能有一个权威位置。

错误：

```text
DesignSystem/Colors.swift
Features/Home/HomeColors.swift
Features/Profile/ProfileColors.swift
```

三处重新定义 `textPrimary / surface / accent`。

正确：

全局语义色统一来自 Design System。

Feature 可以有业务语义映射，但不复制全局 Token。

## 7. 禁止职责重叠目录

不要在没有 Architect 明确规则时同时建立：

```text
Views/
Screens/
Widgets/
Components/
UI/
```

这类名称很容易互相重叠。

Agent 必须能够回答：

- Screen 属于哪里？
- Feature-local Component 属于哪里？
- Shared Component 属于哪里？
- Token 属于哪里？

如果两个目录无法清楚区分职责，就不应该同时存在。

## 8. 按需创建

禁止为了“结构完整”提前创建：

```text
DesignSystem/
  Tokens/
  Components/
  Patterns/
  Motion/
  Layout/
  Screens/
```

空目录或未来假想结构。

创建条件：

- 真实代码已经需要这个归属位置。
- 或 Architect 已明确要求建立该基础结构。

## 9. 上移流程

当 Feature-local Component 开始跨 Feature 使用：

1. 确认语义真的一致。
2. 清理业务依赖。
3. 收敛 API 到语义参数。
4. 上移到 Design System / Shared。
5. 删除重复实现。
6. 保证单一权威位置。

不要复制一份到 Shared 后保留原实现长期并存。

## 10. UI Designer / Blueprint / Construction 分工

UI Designer：
- 决定归属规则。
- 识别哪些 UI 应保持 Feature-local。
- 识别哪些内容已经成熟到可以上移。

Blueprint：
- 把抽取 / 移动 / 重构落实成 Task。
- 处理依赖和施工顺序。

Construction：
- 按既定位置实现。
- 不自行创造新共享目录或复制 Design Token。
- 若发现归属冲突，回 UI Designer / Architect，而不是临时新建目录。

## 11. 默认判断表

```text
只服务一个 Feature？
→ Feature-local

两个以上 Feature 真实复用且语义一致？
→ 考虑 Shared / DesignSystem Component

表达全局视觉规则？
→ DesignSystem Token / Pattern

业务逻辑 / service / persistence？
→ 不属于 UI 结构规则

不知道放哪里？
→ 先检查 Architect PROJECT_STRUCTURE，再用以上归属规则判断
```

## 12. 核心原则

> 默认局部，真实复用后再上移。

> 目录可以晚创建，但归属规则不能晚决定。

> Design System 是全局设计语言，不是“所有 UI 文件的垃圾桶”。

> 顶层结构归 Architect；UI 内部归属归 UI Designer；施工落点归 Blueprint。

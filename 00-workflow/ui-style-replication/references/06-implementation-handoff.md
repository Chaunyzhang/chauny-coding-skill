# 06 — Implementation Handoff

目标：保留工程复用能力，但不把 React/SwiftUI/CSS 细节塞回 Style Skill。

## 1. Spec 必须交给工程层什么

每个可复用组件至少给：

- `component_id`
- reuse policy：exact / adapt / exemplar
- anatomy / slots
- semantic token mapping
- geometry/material/type/icon contract
- variants / states（有证据才写）
- context mapping
- adjacency / nesting rules
- local exceptions

工程层不需要重新“看图猜组件”。

## 2. 组件身份规则

**同一个 Component ID → 一套 shared visual contract。**

不同页面若使用同一 `SectionCard`，不能各自复制后微调成三个版本。

如果确实需要不同视觉语义，应创建明确 variant/new component，而不是 silent drift。

## 3. Shared vs Local

设计层建议 shared candidate，当任一成立：

1. 同一语义 UI 出现 2+ 独立场景。
2. 多个 surface 依赖同一稳定视觉 contract。
3. 复制会制造多个 token/icon/markup truth source。

保持 local，当它：

- 只出现一次。
- 主要是当前页面 composition。
- 没有稳定复用边界。
- 抽取只会增加间接层。

## 4. 新组件

Spec 没有合适组件时，工程实现可以新增，但必须：

- 优先消费已有 semantic tokens。
- 遵守 Kernel / Grammar。
- 先标 candidate/local。
- 不顺手复制出一套新的颜色、radius、icon system。

重复稳定使用后再晋升 shared canonical component。

## 5. 下游实现的最小纪律

无论平台，代码生成器都应做到：

1. canonical tokens 只有一个实现来源。
2. 同一 Component ID 只有一个共享实现/contract。
3. 重复 collection 优先 data-driven，而不是复制 markup。
4. 共享 icon/assets 不重复内嵌多个 truth source。
5. 新页面优先组合已有组件；没有合适的才创建新的。

## 6. Recipe policy 到工程语义

### exact
同一组件/稳定 pattern。实现优先直接复用。

### adapt
共享 visual contract，可通过 slots/props/content 适配。

### exemplar
只是设计案例；不要抽成“所有页面必须使用”的模板。

## 7. 不规定平台结构

本 Skill 不要求：

- React 文件怎么命名
- SwiftUI View 放哪个目录
- CSS Modules / Tailwind / styled-components
- state/data owner
- router 架构

这些属于实现 Skill。

Style Spec 只保证“设计系统身份”和“组件复用意图”足够明确。

## 8. 工程后验检查

实现完成后问：

> 再加一个同类页面，需要复制什么？

如果需要复制：

- 同一视觉常量
- 同一 SVG/icon
- 同一 canonical component 主体
- 同一 repeated collection markup

说明工程层没有正确消费 Spec 的 reuse intent。

## 9. Style Delta 与工程同步

若 canonical component contract 或 style-level token 变化，应通过 Spec Delta 通知工程层。

纯文件移动、重命名、框架重构但视觉 contract 不变，不制造假的 Style Spec 变更。

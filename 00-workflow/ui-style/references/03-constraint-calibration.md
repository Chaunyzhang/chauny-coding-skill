# 03 — Constraint Calibration

目标：决定哪些必须守、哪些应该守、哪些应该放开。这里控制 Skill 的“松紧度”。

## 1. 三个独立维度

每个关键规则最多判断：

```text
constraint_strength = hard | soft | open
transfer_scope      = global | domain | component | local
stability_scope     = style | component | session | instance
```

不要再增加一堆相互重叠的控制标签。

## 2. Hard：真正的底线

只有以下情况适合 hard：

1. 用户明确要求必须保持。
2. 明显的品牌/产品视觉身份，破坏后会认不出。
3. 多处稳定出现、跨场景成立的核心视觉 law。
4. 同一个 canonical component 的 contract。
5. 明确的渲染域边界，例如 decorative pixel art vs functional vector UI。

Hard 应少而清楚。Style Kernel 通常 5–12 条。

如果一个 Spec 有几十条 hard/global，先假设“约束过度”，再找理由证明不是。

## 3. Soft：最常见的状态

适合 soft：

- spacing hierarchy
- radius hierarchy/range
- color emphasis relationship
- density
- surface/material grammar
- composition tendencies
- context mapping
- 新组件对 semantic roles 的消费方式

Soft 的目标是保持“语法”，不是复现每个 exact number。

例：

```text
outer radius > nested radius > tag radius
```

通常比“所有 outer radius 必须 26”更适合 Extension Mode。

## 4. Open：正式的设计空间

适合 open：

- 一次性页面布局
- 某个 hero 的具体高度
- 未被证明的 chart composition
- 新页面的信息构图
- 局部装饰和主题内容
- 新组件的初始 anatomy（只要消费现有 Grammar）

Open 不是“随便做”；它仍然受 Kernel 与相关 Grammar 约束。

## 5. Transfer Scope

### global
可默认跨页面继承，例如主色角色、核心 typography hierarchy。

### domain
只在对应视觉域继承，例如 pixel illustration rules、chart rules。

### component
只约束某一组件家族，例如 TaskRow height/slots。

### local
一次性或页面局部事实，例如首页 hero bbox。

**先看 scope，再决定是否复用。**

## 6. Stability Scope

### style
长期属于设计语言。

### component
在组件家族内稳定。

### session
当前一批页面保持一致，之后可以重新校准。

### instance
一次性局部选择。

Generated 默认从最低必要层级开始，不自动 style-level。

## 7. Confidence 不参与自动升级

下面完全合法：

```text
hero.height = 539
confidence = high
constraint = open
scope = local
```

因为“量得准”只说明证据清楚，不说明未来必须继承。

也可能：

```text
decorative rendering = pixel art
confidence = medium/high
constraint = hard
scope = domain/global boundary
```

因为它可能是视觉身份。

## 8. Kernel Promotion Test

一条规则进入 Kernel 前问：

1. 去掉它，新页面还像同一个产品吗？
2. 它是跨多个独立场景成立，还是单个页面偶然出现？
3. 它能下钻到可执行的 token/rule/component 吗？
4. 它与其他 Kernel 条目是否重复？
5. 把它设 hard 会不会无必要地压制新页面结构？

若第 1 题答案是“仍然很像”，通常不该进入 Kernel。

## 9. Grammar Promotion Test

进入 Grammar 的规则应该：

- 至少能解释多个实例，或是用户明确要求。
- 更适合表达 relationship/range/context，而不是 source bbox。
- 对新页面有迁移价值。

单点高置信事实通常 component/local，而不是 Grammar。

## 10. Creative Field 要具体

不要只写“其余自由发挥”。要明确列出本 Spec 没有决定的设计选择，例如：

- 新页面可自由选择 list/grid/split。
- 新统计模块图形形式 open。
- 新 decorative scene 内容 open，但 rendering regime hard。
- 新局部卡片组合 open，但 surface/type grammar soft。

这样强模型知道真正可以在哪里发挥。

## 11. Reconstruction vs Extension

同一事实在两种模式可以不同权重：

- Reconstruction：source bbox/must-match anchor 可临时 hard。
- Extension：同一 bbox 自动降为 local/open，除非它本身是 canonical component contract。

不要把“为复刻而锁”误写成“风格永久锁”。

## 12. Recipe policy

- `exact`：同一 canonical component/pattern。
- `adapt`：保留关键关系，结构允许适配。
- `exemplar`：只是一个合法示例。

默认页面级 composition 更接近 exemplar；稳定共享组件更接近 exact/adapt。

## 13. 新组件策略

没有合适组件时允许创造：

1. 先消费已有 semantic tokens 与 Grammar。
2. 新规则默认 component/local。
3. 第一次出现不扩张 global system。
4. 在多个独立场景稳定复用后，再晋升 shared/canonical。

目标是“已有组件强复用，新组件允许创造，新视觉语言谨慎创造”。

## 14. 过紧 / 过松的症状

### 过紧

- 新页面都像参考页换文案。
- 所有 exact source values 都变 hard。
- hero/grid/card 的组合被当固定模板。
- 强模型没有任何可见的新构图。

### 过松

- 新页面重新猜主色、圆角、type hierarchy。
- 同一 Component ID 每页变一点。
- decorative/functional rendering domain 混乱。
- 每页都发明新的 near-duplicate tokens。

最终追求：**底线锁身份，语法控方向，剩下交给模型。**

# DESIGN-LANGUAGE-SPEC Schema

这份文档是风格复刻的唯一权威。它不是产品 PRD，也不是实现说明。

目标不是“描述得很丰富”，而是把视觉风格编译成一份**可追溯、可计算、可继承、可验证**的视觉协议。任何后续页面或组件都应尽量只消费这份 Spec，不重新猜风格。

---

## A. 全局事实模型：关键事实使用统一元数据

不要让不同章节各自发明记录方式。所有**会影响复刻、迁移或复用决策**的重要 token / rule / component property 都遵循同一事实模型。

不要求低影响 primitive 为了“填满 schema”强行填写所有字段。最低必要字段是 `id / value(or Unknown) / provenance / confidence / evidence`；只有会参与未来生成约束的事实，才必须补 `constraint_strength / transfer_scope / stability_scope`。

| Field | Meaning |
|---|---|
| `id` | 唯一 canonical id，例如 `space.section.md`、`type.body.md` |
| `kind` | primitive / semantic / relationship / component-property / recipe |
| `value` | canonical value；Unknown 时为空 |
| `unit` | px / pt / rem / % / ratio / deg / ms / unitless 等 |
| `provenance` | Observed / Resolved / Generated / Unknown |
| `confidence` | high / medium / low |
| `support` | 支持该结论的 source 数、instance 数及 evidence ids |
| `measurement_uncertainty` | 测量本身的不确定性，例如 `±1 source-px`；不是设计允许变化 |
| `behavior` | fixed / range / responsive / optional / contextual |
| `allowed_variation` | 设计语言本身允许的变化范围；与 measurement uncertainty 分开 |
| `lock` | locked / provisional；只表示事实本身是否允许在无新证据时重解，不代表生成时必须 hard enforce |
| `constraint_strength` | hard / soft / open；未来生成时约束强度 |
| `transfer_scope` | global / domain / component / local；允许迁移到哪里 |
| `stability_scope` | style / component / session / instance；尤其用于 Generated 值 |
| `contexts` | 规则适用上下文，例如 base / inverse / elevated / compact |
| `depends_on` | 依赖的 token/rule/formula |
| `aliases` | 已发现的近义名；必须映射回 canonical id |
| `evidence` | evidence ids + locator |
| `exceptions` | 局部例外 id；不得悄悄污染全局 token |
| `notes` | 必要的解释，不用形容词代替参数 |

### 三个必须分开的概念

```text
measurement_uncertainty = 我们从参考中到底量得有多准
allowed_variation       = 原设计语言本身允许变化多少
constraint_strength     = 未来设计必须守多死
```

例如：

```yaml
id: space.section
value: 24
unit: px
provenance: Resolved
confidence: high
support: {sources: 3, instances: 11}
measurement_uncertainty: "±1 source-px before scale normalization"
behavior: fixed
allowed_variation: null
lock: locked
constraint_strength: soft
transfer_scope: global
stability_scope: style
contexts: [base]
evidence: [ev-014, ev-031, ev-052]
```

而响应式 gutter 可能是：

```yaml
id: space.page.gutter
provenance: Resolved
confidence: high
behavior: responsive
allowed_variation: "16–32 logical-px according to rule layout.gutter.fluid"
measurement_uncertainty: "±1 source-px at each observed viewport"
lock: locked
constraint_strength: soft
transfer_scope: global
stability_scope: style
```

---

# DESIGN-LANGUAGE-SPEC

## 0. Spec Identity / Scope

- `spec_id`
- `version`
- `inherits`
- target style / visual family
- intended reuse scope
- excluded reuse scope
- source ids
- explicit user overrides
- excluded semantics/content/assets
- default context
- supported visual contexts/themes
- document status: draft / calibrated / locked

明确：这份 Spec 复刻什么，不复刻什么；哪些 source-specific 内容不能被误当成风格规则。

---

## 1. Source Registry

| ID | Type | Authority/Scope | Source Size | Viewport | DPR/Scale | Crop | Theme/Context | Color Space | Renderer/Platform | Quality Notes |
|---|---|---|---:|---:|---:|---|---|---|---|---|

`Authority/Scope` 用于说明该 source 是 primary reference、secondary evidence、component-only reference、theme-only reference 等，避免不同来源互相污染。

只有已知时才填写 DPR、renderer、platform、color space。未知就写 Unknown，不猜。

### 1.1 Calibration Anchors

| Source | Anchor | Known Design Value | Source Measurement | Derived Scale | Confidence |
|---|---|---|---|---|---|

可用 anchor：已知 viewport、系统状态栏尺寸、明确文字数值、已知组件尺寸、设备逻辑尺寸等。

---

## 2. Evidence Ledger

| Evidence ID | Source | Locator/BBox | Raw Observation | Raw Value | Unit | Evidence Quality | Status | Confidence | Resolves To |
|---|---|---|---|---:|---|---|---|---|---|

`Locator/BBox` 应尽量精确到区域、组件或 source-pixel bbox，而不是只写“来自 img-03”。

### 2.1 Evidence Quality

可记录：
- clean / anti-aliased / compressed / blurred / occluded / composited / cropped。
- 是否存在未知缩放。
- 是否能区分 foreground 与 background compositing。

Evidence quality 会影响 measurement uncertainty，不直接改变设计允许范围。

### 2.2 Explicit Override Ledger

用户文字对图片/既有 Spec 的覆盖必须单独留账：

| Override ID | Target | Previous Evidence/Rule | Explicit Requirement | Canonical Result | Scope | Priority | Evidence |
|---|---|---|---|---|---|---|---|

Override 不等于“模型重新设计”。只有用户明确指令才能进入此表；模型自己的补全仍属于 Generated。

---

## 3. Coverage & Support Matrix

目的：知道哪些视觉维度被充分证实，哪些只是单点，哪些完全未知。

| Dimension / Rule | Sources Supporting | Instance Count | Cross-source | Provenance | Confidence | Locked? |
|---|---:|---:|---|---|---|---|

至少覆盖输入中 Relevant 的：layout、type、color、spacing、geometry、effects、icons、imagery、components，以及条件出现的 illustration/data-viz/motion/responsive。

这张表可以防止“单张图里的偶然细节”被提升成全局风格。

---

## 4. Style Fingerprint

写 4–8 条**可以下钻到 token/rule 的视觉定律**。

每条包含：
- fingerprint id
- rule statement
- canonical refs
- evidence/support
- applicability

禁止只写：`轻盈 / 高级 / 克制 / 科技感`。

允许写：

```text
fingerprint.surface.01
Elevated panels use surface.elevated + border.subtle + shadow.float.sm;
no elevated panel uses both heavy opaque border and shadow.float.lg.
Refs: surface.elevated, border.subtle, shadow.float.sm, rule.surface.elevation
```

---

### 4.1 Style Control Model

Style Fingerprint 之后必须把规则分成三层；这是 Spec 控制“该紧的紧、该松的松”的核心。

#### Style Kernel

只收纳少量 signature rules。每条必须说明“破坏它为什么会失去视觉身份”。

| Kernel Rule | Canonical Refs | Why Signature | Transfer Scope | Hard Constraint | Evidence |
|---|---|---|---|---|---|

Hard Kernel 应该少而明确。若大多数 token 都进入 Kernel，说明过度约束。

#### Style Grammar

记录允许模型适配的关系：

| Grammar Rule | Relation / Range / Context | Inputs | Transfer Scope | Evidence |
|---|---|---|---|---|

优先形式：inequality / ratio / range / context mapping / dependency / composition law。

#### Creative Field

明确哪些问题没有被风格决定：
- 新页面 composition archetype。
- 未出现过的新组件 anatomy。
- 局部装饰、信息组织、内容组合。
- 未被证据锁定的合法变化。

Creative Field 的目的不是“记录缺失”，而是明确授权生成器探索。不要为了表格完整给这些区域生成假 canonical token。

### 4.2 Consumer Modes

同一份 Spec 至少区分两种消费模式：

**Reconstruction Mode**
- 目标是重建参考。
- must-match anchors / component exact contract / reconstruction tolerance 生效。
- source-specific geometry 可以参与。

**Extension Mode**
- 目标是生成原图没有的新页面/组件。
- Style Kernel hard preserve。
- Style Grammar soft adapt。
- Creative Field open explore。
- source bbox、一次性布局、exemplar recipe 默认不继承。

可选 `consumer_mode` 不改变事实本身，只改变事实如何被消费。

---

## 5. Coordinate / Unit / Calibration Model

这一节定义整份 Spec 如何解释“数值”。

记录：
- source coordinate system
- canonical logical unit
- source-pixel → logical-unit mapping
- viewport/container reference frame
- relative-unit reference (`% / em / rem / ratio`) when relevant
- DPR / pixel density when known
- pixel snapping / half-pixel stroke behavior if evidenced
- rounding policy when repeated geometry shows one
- color space / alpha interpretation when known
- transform origin / coordinate origin when visible transforms存在

### 5.1 Canonicalization Policy

- raw → normalized → canonical 的规则。
- clustering threshold 不能只看数值，还要看 semantic relation。
- 何时保留两个近似 token。
- 何时只保留 range。
- 何时保留 Unknown。

### 5.2 Measurement Uncertainty

单独记录测量误差来源：
- raster / anti-aliasing
- unknown screenshot scale
- compression
- blur
- opacity compositing
- font rasterization

不得把这些误差写成“设计允许范围”。

---

## 6. Canonical Token Registry

这是全局 canonical id 的索引，防止跨章节重复造 token。

| Canonical ID | Domain | Primitive Value | Semantic Role | Behavior | Constraint | Transfer Scope | Stability Scope | Context | Lock | Aliases | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|

规则：
- alias 只能指向 canonical id，不能形成第二套 truth。
- 新发现的近义 token 先进入 alias/candidate，不直接扩张 token 集。
- deprecated token 保留迁移记录，但不得继续作为新组件首选。

---

## 7. Composition / Layout Grammar

记录：
- canvas/background layers
- viewport-bound vs container-bound regions
- page/container min/max width
- gutters / outer insets
- columns / grid tracks / ratios / gaps
- alignment axes
- baseline grid / repeated baseline interval when evidenced
- section rhythm
- content density
- fixed / fluid / intrinsic / ratio-based dimensions
- nesting / inset hierarchy
- adjacency rules
- edge-sharing rules
- clipping / overflow
- scroll region boundaries when visible
- sticky/floating/overlay only when evidenced
- z-order / layer order
- visible transforms: translate / rotate / scale / skew

### 7.1 Layout Templates / Exemplars

对重复页面结构记录模板，但每个模板必须有 `reuse_policy: exact | adapt | exemplar`。

- `exact`：canonical component/pattern 的结构 contract。
- `adapt`：保留关系，可根据内容调整。
- `exemplar`：只是参考里一种合法构图，不应成为新页面默认骨架。

例如：

```text
layout.shell.dashboard
header -> main(split 280 : fluid) -> footer(optional)
main.max-width = layout.content.max
main.gutter = space.page.gutter
sidebar/main gap = space.section.lg
```

不要保存一次性绝对坐标。

### 7.2 Adjacency / Nesting Laws

例如：
- card 内再嵌 card 时是否降一级 surface。
- 相邻 rows 是否共用 divider。
- first/last item 是否改变 radius。
- inline controls 紧邻时是否合并边框。

这些组合规则往往比单个组件参数更能决定“像不像”。

---

## 8. Typography System

| Role | Family | Fallback | Axes | Features | Size | Line-height | Weight | Tracking | Style/Case | Decoration | Color | Align | Width | Wrap/Clamp | Baseline/Optical Offset | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 8.1 Variable Font / OpenType Settings（有证据时）

记录可能影响可见结果的：
- `wght / wdth / opsz / slnt` 等 axis。
- tabular/proportional numbers。
- ligature / small caps / stylistic set。
- optical sizing。

### 8.2 Typographic Relationships

记录 role 间关系，而不仅是独立数字：
- size ratio
- line-height ratio
- title/body contrast
- metadata/body contrast
- cap-height / icon alignment
- paragraph spacing
- list indentation / marker geometry

### 8.3 Text Stress Behavior

当参考能证明时记录：
- max line length
- wrap vs truncate
- line clamp
- long-label behavior
- multi-line vertical alignment
- numeric alignment

无法从参考证明 localization/RTL 时保持 Unknown，不自动扩展为通用产品规范。

### 8.4 Typography Spatial Metrics

真实字体无法识别时，仍可记录影响布局的空间事实：
- observed text bbox / glyph-run width。
- baseline distance / rendered line-box。
- role max width。
- observed wrap threshold / line count。
- multi-line block height。
- icon/text optical alignment。

这些用于维持排版空间行为，不用于伪造 font family。

---

## 9. Color / Tone / Compositing

### 9.1 Primitive & Semantic Color

| Token | Value | Color Space | Alpha | Semantic Role | Contexts | Allowed Use | Forbidden Use | Evidence |
|---|---|---|---|---|---|---|---|---|

### 9.2 Color Relationships

记录重复的相对关系：
- luminance ordering
- alpha hierarchy
- saturation/chroma hierarchy
- text/icon emphasis hierarchy
- border-to-surface contrast relation

当 exact RGB 受截图色彩管理影响时，相对关系仍可保留为 Resolved rule。

### 9.3 Gradients

| Token | Type | Coordinate/Direction | Stops(position,color,alpha) | Spread | Blend Mode | Role | Evidence |
|---|---|---|---|---|---|---|---|

### 9.4 Overlay / Compositing Stack

半透明视觉必须描述“叠在什么上面”：

```text
surface.glass
base fill: rgba(...)
backdrop: blur(...)
blend: normal
underlay requirement: content/background layer
border: border.glass
shadow stack: shadow.glass
```

如果只能看到最终 composite color，foreground alpha 保持 Unknown。

---

## 10. Spacing / Rhythm

### 10.1 Primitive Scale

记录 canonical spacing scale 与来源。

### 10.2 Semantic Roles

| Role | Token/Value | Applies To | Relationship | Behavior | Evidence |
|---|---|---|---|---|---|

包括：
- inline gap
- control internal inset
- group gap
- section gap
- page gutter
- stack gap
- grid gap
- text block spacing

### 10.3 Rhythm Laws

记录：
- 组内 < 组间 < section 的层级关系。
- inset 是否与外部 gutter 共轴。
- 对称 vs 非对称 padding。
- spacing collapse / shared edge 行为。

---

## 11. Geometry / Shape Language

| Role | Width | Height | Min/Max | Padding | Radius | Corner Model | Border Placement | Aspect | Clip/Overflow | Transform | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|

### 11.1 Shape Family

记录重复的形状语法：
- square / rounded-rect / pill / circle / cut-corner / asymmetric corner。
- radius 与 height 的比例关系。
- corner-specific radius。
- stroke inside/center/outside appearance when observable。

### 11.2 Optical Micro-geometry

高精度复刻需要允许“几何中心 ≠ 视觉中心”。记录：
- icon optical offset x/y
- label baseline offset
- asymmetric padding used for optical centering
- glyph/icon overshoot
- badge/dot anchor offset
- 1px stroke snap behavior

这些值应只在重复证据支持时成为系统 rule；单点特殊修正放 Exception Registry。

---

## 12. Border / Depth / Material / Effects

### 12.1 Border

| Role | Width | Color/Alpha | Style | Placement | Corner Interaction | Evidence |
|---|---|---|---|---|---|---|

### 12.2 Shadow Stack

一个 role 可有多层 shadow，不能只允许单层：

| Role | Layer | Inset | X | Y | Blur | Spread | Color | Alpha | Blend | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|

### 12.3 Blur / Filter / Material

| Role | Backdrop Blur | Gaussian Blur | Saturation | Brightness | Contrast | Tint | Noise/Texture | Blend | Evidence |
|---|---|---|---|---|---|---|---|---|---|

### 12.4 Layer / Elevation Relations

记录：
- 哪些 surface 可以浮起。
- elevation 与 border/shadow/opacity 如何联动。
- z-order 与 shadow/effect 的关系。
- 哪些 material 依赖 underlay 才成立。

---

## 13. Iconography

记录：
- family/source
- icon canonical id / alias
- viewBox / nominal box
- painted bounds / optical box
- outline / filled / duotone
- stroke width
- cap / join
- fill rule
- canonical sizes
- pixel snapping if visible
- icon-to-text gap
- baseline / center alignment
- optical offset
- selected/unselected/state treatment only if evidenced

不要只写“使用线性图标”。

---

## 14. Imagery / Photo Language

| Role | Aspect | Crop/Fit | Focal Rule | Safe Area | Mask/Radius | Border | Overlay | Color Treatment | Context | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|

记录：
- object-fit / crop strategy
- focal point / subject placement
- content-safe region
- aspect family
- mask / frame
- overlay / gradient
- saturation / contrast / monochrome / tint
- background-image positioning
- repeated photo art direction（仅从重复证据归纳）

具体品牌图、人物、logo 等 source content 不是风格 token，除非用户明确要求转移该资产。

---

## 15. Illustration / Graphic Motif Language（有证据时）

图片语言和 UI geometry 不一定相同；当参考中存在插画、背景图形、装饰图元时单独记录：

- geometric vocabulary
- stroke/fill style
- corner character
- perspective / projection
- lighting / shadow convention
- palette mapping
- gradient convention
- texture / grain / noise
- motif shape family
- motif scale / density / repetition
- foreground/background interaction

这样可以避免只复刻 UI 框架，却在插画/装饰层突然换成另一种视觉语言。

---

## 15.1 Rendering / Rasterization Regime（有证据时）

当产品同时存在 pixel / vector / photo / hand-drawn / 3D 等不同绘制方式时，单独记录：
- regime id。
- edge character / anti-aliasing。
- effective pixel cell / raster density（可见时）。
- scaling behavior（nearest-neighbor / smooth，仅有证据时）。
- stroke raster/snap behavior。
- domain applicability：decorative / functional / narrative / brand / data-viz。
- cross-regime embedding rules。

如果“不同域用不同渲染方式”本身是产品识别度来源，应提升为 Style Kernel。

---

## 16. Data Visualization Language（只有输入包含图表时）

记录：
- categorical / sequential / diverging palette
- series order and reuse rules
- line width / dash / curve style
- area fill opacity
- bar radius / gap / width
- marker geometry
- gridline / axis stroke
- axis/tick typography
- label density / rotation
- legend geometry
- tooltip visual mapping
- annotation style
- empty/no-data visual treatment if shown

数据逻辑本身不属于本 Skill；这里只记录可见视觉语法。

---

## 17. Component Grammar

### `<ComponentID>`

每个稳定组件记录：
- purpose/name（只用于识别，不写业务逻辑）
- `component_status`: canonical / candidate / local
- `reuse_intent`: shared / contextual / local
- `constraint_strength`: canonical component 内部哪些 property hard，哪些 soft/open
- `recipe_reuse_policy`: exact / adapt / exemplar（若存在 recipe）
- anatomy / slots
- layout model
- outer dimensions
- min/max/content-driven behavior
- internal padding / gaps
- typography mapping
- color/surface mapping
- icon/image mapping
- geometry/radius/border/effects
- alignment / optical offsets
- clip/overflow
- content constraints
- adjacency rules
- nesting rules
- variants（evidence-gated）
- states（evidence-gated）
- fixed / range / responsive / optional / contextual properties
- exception refs

### 17.1 Property Lock Table

| Property | Canonical Ref | Behavior | Allowed Variation | Context | Lock | Evidence |
|---|---|---|---|---|---|---|

### 17.2 Slot Constraints

例如：
- leading icon: optional, `icon.sm`, vertically optical-centered
- label: 1–2 lines, `type.control.md`
- trailing metadata: fixed to `type.meta.sm`, no wrap

这能防止“组件 token 都一样，但内容一变布局就不像”。

### 17.3 Component Promotion / Creative Entry

- 已有 canonical component：新页面优先复用同一 Component ID 和 contract。
- 新结构首次出现：允许模型设计，默认 `component_status=local/candidate`。
- 多个独立页面重复出现并保持同一 anatomy/rules 后，再提升为 canonical/shared。
- 不得因为“Spec 中没有这个组件”而禁止模型创造。
- 也不得因为模型创造了一个新组件，就立即新增一套全局 color/type/radius 系统。

### 17.4 Downstream Reuse Intent

Spec 不规定 React / SwiftUI / CSS 架构，但要给实现 consumer 足够清晰的复用身份：
- 同一 canonical token 应只有一个实现 truth source。
- 同一 canonical Component ID 应映射为同一 shared implementation，而不是每页复制后各自漂移。
- `candidate/local` 组件可以先局部实现，达到 promotion 条件后再 shared；不要过早抽象。
- 重复 collection 的视觉结构应允许 data-driven 消费同一 component contract。

这是 handoff contract，不是平台实现教程。

---

## 18. Relationship Invariants & Dependency Graph

关系规则要尽量写成可计算形式，而不是自然语言暗示。

| Rule ID | Expression / Constraint | Inputs | Applies To | Behavior | Evidence |
|---|---|---|---|---|---|

示例：

```text
rule.spacing.hierarchy
space.inline < space.group < space.section

rule.control.icon
control.icon_size = icon.md
control.icon_gap = space.inline

rule.card.inset
card.content_inset = space.surface.md
card.header_inset_x = card.content_inset

rule.pill.radius
radius.pill = control.height / 2
```

### 18.1 Dependency Graph

Derived token 应引用父 token/formula，不重复硬编码数值。

```text
control.md.height -> 32
radius.pill -> control.md.height / 2
badge.anchor.y -> icon.optical_center.y + optical.badge_offset
```

这能保证修改 canonical primitive 时关系不会断。

---

## 19. Context / Variant Mapping

“同一个 token 在什么环境下变”必须显式化，不能靠生成时临场判断。

可能的 context（只保留有证据的）：
- base / inverse
- flat / elevated / overlay
- compact / regular / spacious
- small / medium / large component size
- selected / disabled / active visual state
- light / dark theme

| Semantic Role | Default | Context | Mapped Token | Evidence |
|---|---|---|---|---|

### 19.1 Context Precedence

明确冲突时顺序，例如：

```text
user override > component explicit variant > context mapping > semantic role > primitive default
```

不要默认 context 只改变颜色；有些风格会同时改变 border、shadow、opacity、type 或 spacing。

---

## 20. Responsive / Fluid Rules（只有证据时）

| Rule | Driver | Observed Anchors | Interpolation | Reflow | Change Interval/Breakpoint | Confidence | Evidence |
|---|---|---|---|---|---|---|---|

Driver 区分：
- viewport width
- container width
- intrinsic content
- aspect ratio

记录：
- anchor viewport 与对应值。
- invariant properties。
- fluid interpolation（linear / clamp / proportional 等，只有可推导时）。
- reflow 行为。
- breakpoint 若只能确定区间，就保存 interval，不猜单点。

---

## 21. Motion / State Visuals（只有证据时）

| Element | State/Transition | Property | From | To | Duration | Delay | Easing/Spring | Sequence | Evidence |
|---|---|---|---|---|---|---|---|---|---|

还应记录：
- simultaneous vs staggered
- transform origin
- opacity/blur/scale coupling
- state visual tokens

静态截图无法证明的 duration/easing 必须 Unknown。

---

## 22. Exception Registry

这是稳定性非常关键的一层：**局部例外不能自动升级成全局设计语言。**

| Exception ID | Scope | Deviates From | Local Value/Rule | Evidence | Why Local | Promotion Condition |
|---|---|---|---|---|---|---|

典型例外：
- hero 卡片独有 radius。
- 某 logo 需要 2px optical offset。
- 首屏装饰图形有特殊 overlap。
- 一个 source 因 crop 看起来 gutter 异常。

`Promotion Condition` 可以写：如果后续多个独立 source 重复出现，再考虑升级为 canonical role/rule。

---

## 23. Variation / Inheritance / Constraint Policy

### Constraint Strength

- `hard`：视觉身份底线、明确用户要求、或 canonical component 的必要 contract。
- `soft`：关系/范围/上下文应保持，但允许适配。
- `open`：不构成风格身份，允许模型探索。

### Stability Scope

- `style`：跨页面长期稳定。
- `component`：只在组件家族稳定。
- `session`：当前一组生成保持一致。
- `instance`：一次性局部选择。

Generated 值默认选择最低必要 stability scope，不能自动 style-lock。

### Fixed
必须一致。

### Range
设计语言允许在明确范围内变化。

### Responsive
由明确 driver/rule 决定变化。

### Optional
只在特定 component/scene 出现。

### Contextual
由 context map 切换。

### Inheritance
新页面/组件先继承 semantic role / component grammar。

### Override Precedence
用户覆盖、组件变体、上下文、本地例外、全局 role 的优先级必须明确。

### Forbidden Drift / Invalid Substitutions
记录：
- 不允许新增的近义 token。
- 哪些 role 不可互换。
- 哪些 effect/shape 组合在该风格中从未成立。

---

## 24. Unknowns / Conflicts / Candidates

| Item | Type | Why Unknown/Conflicting | Candidate(s) | Safe Representation | Impact | What Evidence Resolves It |
|---|---|---|---|---|---|---|

Type 可为：
- unknown value
- ambiguous role
- source conflict
- scale ambiguity
- compositing ambiguity
- candidate token

`Impact` 用于说明它是否阻塞高保真复刻，而不是评价审美。

---

## 25. Reconstruction / Extension Recipes

Recipe 只引用 canonical token/rule，不重新写裸值。每个 recipe 必须标 `reuse_policy`：

- `exact`：同一 canonical component/pattern 必须保持 contract。
- `adapt`：保留视觉语法和关系，可为新内容重新布局。
- `exemplar`：仅表示参考中出现过一种合法组合，不约束未来页面采用同样构图。

Extension Mode 下不得把 `exemplar` 当页面模板。

至少按输入 Relevant 情况记录：
- page shell recipe
- primary content container recipe
- typography stack recipe
- common surface recipe
- common control recipe
- repeated component recipe
- overlay/floating recipe
- image treatment recipe
- chart recipe（如 Relevant）

示例：

```text
recipe.surface.card
surface = surface.card
inset = space.surface.md
radius = radius.surface.md
border = border.subtle
shadow = shadow.none
header/body gap = space.group.sm
```

---

## 26. Fidelity Contract / Reconstruction Tolerance

必须把三个概念分开：

```text
measurement uncertainty  = 源证据量得有多准
allowed variation        = 设计语言允许怎么变
reconstruction tolerance = 验证复刻结果时允许偏多少
```

### 26.1 Must-match Anchors

列出最能决定视觉身份的可测 anchors，例如：
- container/gutter relationships
- type role metrics
- core spacing hierarchy
- signature radius/shape relation
- surface compositing
- repeated component dimensions

不是做审美打分，而是告诉验证器哪些关系必须被精确保持。

### 26.2 Tolerance Table

| Dimension / Rule | Target | Tolerance | Reason / Measurement Limit |
|---|---|---|---|

Tolerance 必须来自 evidence quality / raster uncertainty / explicit variation，不允许凭感觉放宽。

### 26.3 Extension Identity Contract

Extension Mode 不使用逐像素 tolerance，而检查：
- Style Kernel 是否完整保持。
- Style Grammar 是否仍满足关系/范围/context。
- canonical component 是否保持 contract。
- exemplar/source-specific geometry 是否没有被机械复制。
- Creative Field 是否存在真实新设计，而不是模板换文案。

可记录：

| Extension Dimension | Preserve / Adapt / Explore | Guardrail | Failure Signal |
|---|---|---|---|

---

## 27. Machine-readable Manifest

YAML/JSON 是正文的机器可读镜像，不是第二份 truth。推荐结构：

```yaml
meta:
  spec_id: null
  version: 1
  inherits: null
  status: calibrated
  default_context: base
  sources: []

calibration:
  canonical_unit: px
  coordinate_model: {}
  scale_anchors: []
  canonicalization: {}

facts:
  # 每个事实都遵守统一 metadata model
  space.section:
    kind: semantic
    value: 24
    unit: px
    provenance: Resolved
    confidence: high
    support:
      sources: 3
      instances: 11
    measurement_uncertainty: "±1 source-px pre-normalization"
    behavior: fixed
    allowed_variation: null
    lock: locked
        constraint_strength: soft
    transfer_scope: global
        stability_scope: style
    contexts: [base]
    depends_on: []
    aliases: []
    evidence: [ev-014, ev-031, ev-052]
    exceptions: []

primitives:
  color: {}
  typography: {}
  spacing: {}
  geometry: {}
  effects: {}
  icon: {}
  imagery: {}

semantic:
  color: {}
  typography: {}
  spacing: {}
  geometry: {}
  effects: {}
  icon: {}

style_control:
  kernel: {}
  grammar: {}
  creative_field: []

rules:
  layout: {}
  relationships: {}
  adjacency: {}
  context: {}
  variation: {}
  responsive: {}
  compositing: {}

components: {}
recipes: {}
exceptions: {}
unknowns: []
conflicts: []
consumer_modes:
  reconstruction: {}
  extension: {}

validation:
  anchors: []
  tolerances: {}
  creative_headroom: {}
```

### Manifest 规则

1. 正文与 manifest 同源。
2. 所有 derived value 优先引用 `depends_on` / formula，而不是复制裸值。
3. manifest 里的 alias 不允许拥有独立 canonical value。
4. Unknown 不用虚假默认值填满。

---

## 28. Spec Delta（更新既有 Spec 时）

| Change ID | Canonical ID | Previous | New | Evidence/Override | Reason | Downstream Impact |
|---|---|---|---|---|---|---|

任何 locked canonical value 的变化必须留下 delta。

变化不是问题；**无证据、无记录地漂移才是问题**。

---

# Schema Rules

## 1. 参数必须带语义
禁止只有 `12px / #EDEDED / radius 16` 的裸列表。每个值要映射到 role、rule 或 component property。

## 2. 每个关键事实同时描述“值”和“状态”
至少知道：value、provenance、confidence、behavior、lock、evidence；会参与未来生成的关键事实还要知道 constraint strength 与 transfer scope。

## 3. Measurement Uncertainty 不等于 Allowed Variation
这是最容易造成错误复刻的混淆之一。截图量不准，不代表设计可以随便变。

## 4. 单点异常进入 Exception，不污染 Canonical System
只有重复、可解释的视觉关系才提升为全局 token/rule。

## 5. Raw Measurement 不直接污染 Token
截图测得值放在 Evidence/Calibration；canonical token 放在正式 registry/manifest。

## 6. Primitive → Semantic → Rule → Component 必须分层
Primitive 是值；Semantic 是职责；Rule 是关系；Component 是组合消费层。

## 7. Derived Values 应形成 Dependency Graph
能写公式/依赖时，不在多个组件里复制同一个数字。

## 8. Context 必须显式
同一 role 在 inverse/elevated/compact 等上下文变化时，写 mapping，不让生成器临场判断。

## 9. 关键值必须可追溯
Observed/Resolved 附 evidence id + locator；Generated 明确标记；Unknown 不硬猜。

## 10. Machine-readable 与正文同源
值冲突即 Spec 错误，不允许长期双轨。

## 11. Style Fingerprint 必须可下钻
任何高层“风格感”都要能落到 token/rule/component grammar。

## 12. Conditional Domains 不为了完整而编造
Illustration、data-viz、motion、responsive、theme 等没有输入证据时保持缺省/Unknown，而不是强行生成一套。

## 13. 更新不得静默改写历史规则
locked canonical value 改变时，写 Spec Delta，再提升 version。

## 14. 高置信不等于硬约束
`confidence/support` 描述事实可靠性；`constraint_strength/transfer_scope` 描述未来设计约束。二者不得互相替代。

## 15. Style Kernel 必须小而有辨识度
Kernel 只放真正决定视觉身份的 signature rules。若大多数 token/property 都是 hard/global，判定为 over-constrained。

## 16. Generated 只稳定到最低必要层级
优先锁关系、范围、component/session；只有明确证据支持时才提升为 style-level exact rule。

## 17. Recipe 必须声明 exact / adapt / exemplar
观察到的页面构图默认不是未来页面模板。Extension Mode 下 exemplar 不得自动继承。

## 18. Creative Field 是正式输出
没有被风格决定的地方应明确保持 open，而不是为了完整强行生成参数。

## 19. 组件复用与新组件创造同时成立
canonical component 优先复用；不存在合适组件时允许新设计，并先保持 component-local/candidate。

## 20. 最终判断标准
这份 Spec 应做到：给另一个模型/Agent，它不看原图也能最大程度重建同一视觉系统；在 Extension Mode 下又能设计信息架构明显不同的新页面，守住 Kernel、遵守 Grammar，但不会机械复制参考页面。

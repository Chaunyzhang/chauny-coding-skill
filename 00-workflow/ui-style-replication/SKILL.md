---
name: ui-style-replication
display_name: UI 风格复刻
description: 把图片、截图、文字描述或混合参考提取并编译成精确、稳定、可持续复用的 UI 设计语言文档。目标是守住视觉身份与组件系统，同时保留足够创作空间，让强模型能继续设计而不是只会照抄。
---

# UI 风格复刻

## 唯一目标

这个 Skill 只做一件事：

`图片 / 截图 / 文字描述 / 混合参考 → 设计语言提取 → 参数归一化 → 约束分级 → DESIGN-LANGUAGE-SPEC`

成功标准不是“更好看”，也不是“把截图翻译成文字”。成功标准是：

1. **精确**：文档里的参数、关系、规则能解释输入中的视觉证据。
2. **稳定**：相同视觉关系不会被写成一堆近义值；同一份 Spec 重复使用时不无故漂移。
3. **可延续**：输入中没出现过的新页面、新组件仍能明显属于同一种视觉语言。
4. **有余量**：只锁真正构成视觉身份的内容，不把一次性布局和偶然数值变成永久模板。
5. **可追溯**：关键规则知道来自哪张图、哪段文字，哪些是观察值、归纳值、模型补全值或仍未知。

本 Skill **不优化源风格**。源参考中的大圆角、玻璃、重阴影、框套框、密集布局等，只要是稳定视觉事实，就应如实提取。不得用 Agent 自己的“好看/高级/简洁”标准改写源风格。

同时，本 Skill **不把精确记录等同于强制复用**。知道某张参考图的 hero 高度是 539，不代表所有新页面都必须有 539 高的 hero；知道某个 card radius 是 26，也不代表所有新 surface 都只能用 26。

---

## 0. 核心原则：高精度记录，选择性约束

设计文档有两个互相独立的维度：

```text
Evidence certainty   = 我们对这个视觉事实有多确定
Generation authority = 这个事实对未来设计约束有多强
```

高 confidence 不等于 hard constraint。

例：一个 hero 的 radius=28 可以是 high-confidence Observed，但它仍可能只是 component-local；不能因为量得准就升级成全局风格底线。

### 0.1 三层控制模型

#### Style Kernel — 不能破坏的视觉身份

只放少量真正决定“是不是这个产品”的规则，通常 5–12 条。

典型内容：
- 核心 surface / color hierarchy。
- typography emphasis hierarchy。
- 主 shape family / material language。
- icon / rendering character。
- 极具识别度的 spacing/rhythm 关系。
- 明确的双渲染域、插画语言、品牌级 visual law。

默认：`constraint_strength=hard`。

#### Style Grammar — 可以变化，但要按这套语法变化

记录关系、范围、上下文、组合规则，而不是把所有值锁成单点。

典型内容：
- `inline < group < section`。
- `outer radius > nested radius > tag radius`。
- 某类 surface 允许 24–30，而不是必须 26。
- 新组件优先消费既有 semantic roles。
- card / list / grid 可以改变构图，但 surface、type、rhythm、icon grammar 不变。

默认：`constraint_strength=soft`。

#### Creative Field — 明确留给模型发挥

输入没有规定、也不构成风格身份的地方，不要为了“完整”强行填死。

典型内容：
- 新页面采用 hero / grid / list / split 中哪种构图。
- 新组件具体如何组织内容。
- 局部装饰放什么。
- 未被证据锁定的视觉巧思。

默认：`constraint_strength=open`。

强模型应该在 Creative Field 中继续发挥；Skill 的职责是让它发挥以后仍然“像这个产品”。

---

## 1. 输入与证据优先级

输入可以是：
- 单张或多张截图/图片。
- 文字风格描述。
- 图片 + 文字要求。
- 已存在的设计语言文档，需要增量补充或校准。

冲突时按以下优先级：

`用户明确数值/约束 > 用户明确覆盖指令 > 可重复视觉证据 > 单点视觉证据 > 描述性文字 > 模型补全`

所有设计事实只允许属于四类：

- **Observed**：输入里直接可见、可量或明确写出。
- **Resolved**：根据重复证据、比例关系、聚类或文字要求归一得到的 canonical rule/token。
- **Generated**：输入不足但为了某次可执行设计需要模型补全的值；必须标明稳定范围，不默认升级成永久风格事实。
- **Unknown**：当前证据无法可靠确定，且不应硬猜。

每个关键事实除了 provenance，还要判断：

- `constraint_strength`: `hard / soft / open`
- `transfer_scope`: `global / domain / component / local`
- `stability_scope`: `style / component / session / instance`

详细测量与归一规则见 `references/01-evidence-measurement.md`。

---

## 2. 不是截图描摹，而是提取设计语言

禁止把截图当成一堆绝对坐标逐项抄写。应提取四层信息：

### A. Primitive Parameters
颜色、字号、行高、字重、字距、间距、尺寸、圆角、border、shadow、blur、icon metrics、图片比例等。

### B. Semantic Roles
这些参数在系统中的职责：`text.primary`、`text.meta`、`surface.base`、`space.group`、`radius.control`、`shadow.floating` 等。

### C. Generative Rules
决定“为什么新东西看起来还是同一种风格”的规则：
- 页面宽度与边距怎么变化。
- 同组/跨组距离如何分层。
- 标题、正文、辅助信息如何形成比例。
- 哪些 surface 可以有边框/阴影。
- icon 的 stroke、尺寸与文字如何对齐。
- component 内部 padding 与高度如何由 token 组合。
- 哪些值必须固定，哪些只需保持关系/范围。

### D. Constraint Semantics
同一个视觉事实还必须说明：
- 是风格底线，还是参考范例。
- 应该精确复用、适配复用，还是允许重新设计。
- 只约束某个 component，还是能迁移到整个产品。

只有 Primitive，没有 Roles/Rules，会变成像素抄写；只有规则，没有 Constraint Semantics，会把所有精确事实错误地变成硬约束。

详细提取维度见 `references/02-design-language-extraction.md`。

---

## 3. 图片路径：Measure → Cluster → Resolve → Classify Constraint

图片输入默认流程：

1. 记录 source resolution、裁切情况、主题、平台/viewport 等已知条件。
2. 提取可见 structure 与重复关系，不先判断“好不好看”。
3. 测量 raw values，并保留 source-pixel / ratio 信息。
4. 将近似值按**相同语义关系**聚类，形成 token candidates。
5. 依据多处重复、跨图一致性和比例关系，解析成 canonical tokens/rules。
6. 每个关键 token/rule 记录 evidence refs、confidence、scope。
7. 再判断它属于 Kernel / Grammar / Creative Field，不能由 confidence 自动决定 constraint strength。
8. 无法从静态图证明的内容保持 Unknown。

特别注意：截图可能被缩放。没有可靠 scale anchor 时，截图像素不等于实现 px。必须区分：

`raw measurement → normalized relation → canonical design value`

同时继续区分：

`canonical fact → transfer scope → generation constraint`

不得从静态图声称知道未展示的 motion、hidden states、真实 breakpoint、hover/focus 行为或代码实现。

---

## 4. 文字路径：Instantiate at the Minimum Necessary Level

文字描述通常不能唯一决定数值。例如“柔和、紧凑、大圆角”仍缺字号、spacing、radius、surface 等具体值。

处理方式不是把所有缺失值一次生成后永久锁死，而是：

1. 把描述拆成明确视觉维度与约束。
2. 能从文字直接得到的记为 Observed。
3. **优先解析关系、层级、范围和语义角色，再决定是否需要单点数值。**
4. 只有消费者确实需要 concrete value 时才 Generated 一个值。
5. Generated 值必须声明 `stability_scope`：
   - `style`：确实是视觉身份的一部分，跨页面长期稳定。
   - `component`：仅在该组件家族稳定。
   - `session`：当前一组页面/一次生成保持一致，但不自动晋升为风格事实。
   - `instance`：一次性局部选择。
6. 没有新证据时，`session/instance` Generated 不得自动提升为 Style Kernel。

例如“宽松的大圆角卡片”优先解析为：

```text
surface radius family = large
outer radius > nested radius
section rhythm = spacious
```

若当前页面必须落具体值，可以实例化成 `26 / 18`，但默认只需 session/component 稳定，不必永久规定所有未来 surface 都只能用这些数字。

文字输入的稳定性来自**在必要层级稳定**，不是“所有东西一次选值、永久锁死”。

---

## 5. 混合路径：文字负责覆盖，图片负责细节

图片 + 文字时：
- 图片负责提供可测的视觉结构、比例、token、component grammar。
- 文字负责声明保留、替换、加强、减弱或禁止的方向。
- 用户明确要求可以覆盖图片证据，但必须在 Spec 中写成 override，而不是悄悄改值。
- 用户说“保持这个风格，但自由设计新页面”时，默认进入 **extension mode**：Kernel 强约束，Grammar 软约束，Creative Field 开放。

例：图片是 `radius.surface ≈ 12`，用户说“卡片改得更圆”。最终可以 Resolved 为 16，但证据链要写清 `image≈12 → user override → canonical=16`。

---

## 6. DESIGN-LANGUAGE-SPEC 是唯一产物

本 Skill 最终收束为一份 `DESIGN-LANGUAGE-SPEC.md`。它必须同时包含：

- 人可读的设计语言规则。
- 精确参数表。
- Style Kernel / Style Grammar / Creative Field。
- 组件构成与复用语义。
- 固定项 / 可变项 / contextual / override 规则。
- Evidence / confidence / Unknown。
- 同文档内的 machine-readable manifest。

不要另外维护第二份 token truth source。

完整 schema 见 `references/03-style-spec-schema.md`。

---

## 7. 两种消费模式必须分开

同一份 Spec 可以服务不同任务，但约束强度不同。

### 7.1 Reconstruction Mode

目标：重建参考本身。

- must-match anchors 优先。
- component exact contract 优先。
- source-specific geometry 可以临时生效。
- reconstruction tolerance 参与验证。

### 7.2 Extension Mode

目标：生成原图没有的新页面/新组件，但保持同一种视觉语言。

- Style Kernel 必须保持。
- Style Grammar 应遵守，但允许上下文适配。
- source-specific bbox、一次性 layout、exemplar recipe 不得自动继承。
- Creative Field 明确交给模型。
- 新组件优先消费现有 semantic roles；不足时允许创建 component-local candidate，而不是禁止创新。

**不能用 Reconstruction Mode 的精确坐标去压 Extension Mode 的设计能力。**

---

## 8. 稳定性与自由度规则

### 8.1 Canonicalization
相同语义关系出现近似值时，优先归一。只有存在明确角色差异时才保留不同值。

### 8.2 No Near-Duplicate Drift
已有 `8/12/16/24` 时，新测到的 `15/17/23` 不能直接变成新 token。先判断它们是否只是 raster/缩放/测量误差或同一关系的漂移。

### 8.3 Constraint Calibration

- `hard`：破坏后会明显丢失视觉身份，或违反明确 component contract / user requirement。
- `soft`：应保持关系、范围、方向或语义，但具体实现可适配。
- `open`：不构成风格身份，交给模型根据页面目标设计。

Hard 应该少而明确。不能为了“稳定”把大部分 Spec 都标 hard。

### 8.4 Scope Before Reuse
任何事实先看 `transfer_scope` 再继承：
- global 才能默认跨页面。
- domain 只在对应视觉域迁移。
- component 只约束对应组件家族。
- local 不自动继承。

### 8.5 Component Reuse, Visual Innovation

- 已有 canonical component：优先复用同一 Component ID 与视觉 contract。
- 稳定结构在多个独立场景重复：可提升为 shared component candidate。
- 没有合适组件：允许模型设计新组件，但先消费已有 semantic tokens / grammar。
- 新组件第一次出现默认 component-local，不立刻污染全局组件系统。

### 8.6 Evidence-Gated Detail
无法观察的细节不为了“文档完整”而编造。Unknown 本身是精确度的一部分。

---

## 9. Recipe / Layout 的复用语义

每个 recipe / layout exemplar 必须标：

- `exact`：同一 canonical component/pattern 应精确复用。
- `adapt`：保留结构关系和视觉语法，可按新内容改变布局。
- `exemplar`：仅说明参考中出现过一种合法构图；不得成为未来页面默认模板。

例如：
- `TaskRow` 通常是 `exact`。
- `SectionCard` 通常是 `adapt`。
- 首页的大 Hero 构图通常是 `exemplar`。

这样强模型不会把“参考页面长什么样”误解成“以后所有页面都必须长这样”。

---

## 10. 验证：既验证不跑偏，也验证没有被写死

验证对象不是审美优劣，而是两件事：

1. **风格身份是否稳定。**
2. **新设计是否仍有合理结构差异和创作空间。**

至少检查：
- Traceability：关键规则能否回指 evidence 或明确 Generated 来源。
- Token consistency：是否存在无理由近义 token。
- Constraint calibration：高 confidence 是否被错误升级成 hard/global。
- Kernel integrity：新页面是否守住 signature rules。
- Grammar consistency：soft rules 是否以关系/范围方式延续。
- Component reuse：同一 Component ID 是否保持同一视觉 contract。
- Cross-page generalization：不同 IA 的页面是否仍属于同一产品。
- Creative headroom：新页面是否只是把参考页面换文案；是否存在不违反 Kernel 的新构图/新组件。
- Repeatability：再次消费同一 Spec 时，核心身份不变，同时 open 区域不要求机械复现同一答案。

若有足够多参考图，优先做 holdout；若目标是风格延续，至少做一次 **novel-page extension test**：生成与参考信息架构明显不同的新页面。

详细 Gate 见 `references/04-fidelity-verification.md`。

---

## 11. 明确不做

以下内容不属于本 Skill，除非它们本身直接影响可见风格参数：

- 产品需求定义、用户任务分析、业务 IA。
- backend / API / data ownership。
- state owner、mutation、permission/lifecycle truth。
- repo architecture、代码抽象、文件结构。
- SwiftUI / React / CSS 等平台实现教程。
- 代码实现与重构。
- “怎样更高级/更好看”的审美优化。
- 用 Craft Floor、审美 warning 或通用设计偏好改写源风格。
- 与复刻无关的 accessibility、业务状态、交互闭环检查。

但 Spec 应提供足够明确的 **component identity / reuse intent / semantic contract**，让后续实现工具能构建 shared components，而不是每页重新复制视觉结构。

---

## 12. 完成 Gate

只有同时满足以下条件才完成：

- 文档没有只靠形容词表达的关键视觉决定。
- 所有关键参数有 canonical value、role 或明确 Unknown。
- 图片测量值与 canonical value 没有混为一谈。
- evidence certainty 与 generation constraint 没有混为一谈。
- Style Kernel 足够少且足够有辨识度；不存在“大部分规则都 hard”的情况。
- Style Grammar 尽量用 relationship / range / context / dependency 表达，而不是不必要的 exact value。
- Creative Field 明确，不为了文档完整把未规定的设计空间填死。
- typography / color / spacing / geometry / surface/effects / icon/imagery / component grammar 已按输入相关性覆盖；输入中出现 rendering-regime / illustration / data-viz / compositing 等视觉域时也已覆盖。
- measurement uncertainty 与 allowed variation 没有混淆。
- source authority 与 global / domain / component / local / exception 的 scope 明确。
- Generated 值有 stability scope，session/instance 值没有无证据晋升为长期风格事实。
- recipe/layout 标明 exact / adapt / exemplar。
- canonical component 有明确 reuse intent，新组件仍保留创作入口。
- derived values / relationship invariants 尽量用 dependency/formula 表达，避免跨组件重复硬编码。
- 每个关键规则能说明是 Observed / Resolved / Generated / Unknown。
- Reconstruction Mode 能复刻，Extension Mode 能生成结构明显不同但仍同风格的新页面。

最终目标：**弱模型不容易跑偏，强模型不被参数表压成执行器。**

# 02 — Style Extraction

目标：从证据里提取“设计语言”，不是逐像素描摹。

## 1. 四层抽取

```text
Primitive → Semantic Role → Relationship / Rule → Component Grammar
```

Primitive 是值；Semantic 是职责；Rule 是关系；Component 是组合消费层。

## 2. 先找“ONE brand thing”

提问：

> 如果其他东西都变普通，只剩哪些视觉决定还能让人认出这是它？

它们是 Style Kernel 候选，但仍需证据支持。通常不是一个单独 hex，而是一个关系或渲染规律。

## 3. Composition / Layout

Relevant 时提取：

- canvas/background layers
- container/gutter
- alignment axes
- grid/columns/gaps
- section rhythm
- density
- nesting/inset hierarchy
- adjacency / edge-sharing
- clipping/overflow
- z-order / overlap
- fixed/fluid/intrinsic/ratio dimensions

一次性的绝对坐标通常是 reconstruction evidence，不自动变成 extension grammar。

## 4. Typography

至少考虑：

- family/fallback（可 Unknown）
- size / line-height / weight / tracking
- style/case/decoration
- color role
- alignment
- wrap/clamp
- width behavior
- baseline / optical offset
- role relationships

字体未知时优先保存 spatial metrics，而不是随意指定常见字体。

## 5. Color / Tone / Compositing

提取：

- primitive colors
- semantic colors
- luminance hierarchy
- saturation/chroma hierarchy
- alpha hierarchy
- gradients
- surface/background relationships
- overlay/compositing stack

不要把 source content 的颜色自动升级成 global brand color。

## 6. Spacing / Rhythm

除了 scale，更重要的是关系：

- inline gap
- control inset
- group gap
- section gap
- page gutter
- nested inset
- text block spacing
- symmetric/asymmetric padding

优先写 `group < section` 等 grammar；exact token 只有稳定复用时才成为 canonical。

## 7. Geometry / Shape

提取：

- width/height/min/max/aspect
- radius / corner family
- border placement
- circle/pill/rounded-rect/cut-corner 等 shape family
- radius 与 height 的关系
- optical micro-adjustment

几何中心不总是视觉中心。重复出现的 icon/glyph optical offset 可以成为 component rule。

## 8. Border / Depth / Material

记录：

- border width/color/placement
- multi-layer shadow
- blur/filter
- tint/noise/texture
- elevation relations
- material 与 underlay 的依赖

“柔和玻璃感”不是足够的 spec。

## 9. Iconography

Relevant 时记录：

- family/source
- outline/filled/duotone
- stroke width
- cap/join
- nominal box / painted bounds
- canonical sizes
- icon-to-text gap
- baseline / optical offset
- state treatment

不要只写“线性图标”。

## 10. Rendering / Rasterization Regime

当参考混合不同渲染语言时必须单独提取，例如：

```text
decorative → pixel art
functional controls → smooth vector
```

可记录：

- pixel/vector/raster/hand-drawn/3D/photo
- anti-aliasing/edge character
- effective pixel cell
- scaling method
- stroke raster behavior
- domain applicability
- cross-domain embedding rules

这是视觉身份，不能被 imagery 一项吞掉。

## 11. Imagery / Illustration

提取 style，不把具体内容误当 token：

- aspect/crop/focal rule
- palette mapping
- perspective/projection
- stroke/fill
- lighting/shadow convention
- texture/grain
- motif vocabulary
- subject scale / focal position
- density / repetition

具体猫、人物、logo、某张照片通常是 asset/content，不是风格规则。

## 12. Data Visualization（有证据才提）

图表出现时记录：palette、line/bar/marker、axis/grid、label、legend、tooltip、annotation 等视觉语法。

数据逻辑本身不属于本 Skill。

## 13. Component Grammar

稳定组件记录：

- `component_id`
- anatomy / slots
- layout model
- dimensions / content-driven behavior
- padding / gaps
- type/color/icon/image mapping
- radius/border/effects
- alignment/optical offsets
- adjacency / nesting
- variants/states（evidence-gated）
- property behavior
- exception refs
- reuse policy: exact/adapt/exemplar

同一 Component ID 只有一套视觉 contract。

## 14. Context / Variant

如果同一 semantic role 在不同环境变化，优先写 context mapping：

- base/inverse
- flat/elevated/overlay
- compact/regular/spacious
- component size
- selected/disabled/active
- light/dark

不要把每个 context 变成含义不清的 near-duplicate token。

## 15. Exceptions

单点特殊情况放 Exception，不自动升级全局：hero 特殊 radius、logo optical offset、一次性 overlap 等。

重复证据出现后再考虑晋升。

## 16. 不要为了完整而填满

没有 evidence 的 motion、responsive、theme、data-viz、illustration 不强行生成一套。

Schema 的价值是“能装下”，不是“每次必须全部填”。

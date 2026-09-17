# 设计语言提取维度

目标：从参考中提取一套能继续生成新 UI 的视觉语法，而不是描述某张图“有什么”。

## 1. Composition / Layout Grammar

提取：
- canvas/background 层级。
- page/container width、min/max width、左右 gutter。
- column/grid 数量、比例、gap。
- 主 alignment axes 与 baseline 规则。
- section rhythm、组内/组间距离层级。
- fixed / fluid / intrinsic / ratio-based 尺寸。
- sticky/floating/overlay 仅在证据可见时记录。
- density：row height、control height、content packing。
- repeated composition pattern：list-dominant、split、sidebar、modular grid 等，只作为描述已观察结构，不作为推荐。

不要记录一次性的截图坐标；记录可迁移的关系。

## 2. Typography

每个 role 尽量记录：
- role name。
- font family / fallback。
- font size。
- line-height。
- weight。
- letter-spacing / tracking。
- font style / casing / text transform。
- alignment。
- color role。
- max line width。
- wrap / truncate / line clamp。
- paragraph/list spacing（Relevant 时）。

重点是 role 之间的比例与重复使用，不是孤立字号。

## 3. Color / Opacity

至少分：
- primitive palette。
- semantic roles：background/surface/text/icon/border/action/status 等。
- exact value：hex / rgba / alpha。
- gradient：direction + stops + alpha。
- overlay/tint。
- state color variation（只有证据时）。
- dark/light theme mapping（只有多主题证据时）。

不要只采一串 hex；必须说明每个颜色“用在哪里、不能用在哪里”。

## 4. Spacing

提取两层：

### Primitive spacing scale
如 `4/8/12/16/24/32`。

### Semantic spacing roles
如：
- `space.inline`
- `space.control.inner`
- `space.group`
- `space.section`
- `space.page.gutter`

同一语义关系优先只对应一个 canonical token。

## 5. Geometry

提取：
- control heights。
- min/max widths。
- padding x/y。
- radius family。
- border widths。
- divider thickness。
- avatar/icon/image sizes。
- aspect ratios。
- corner-specific radius（若源设计存在）。

## 6. Surface / Border / Depth / Effects

记录真正参数：
- surface fill / alpha。
- border color / alpha / width / style。
- shadow：x / y / blur / spread / color / alpha。
- backdrop blur / gaussian blur。
- saturation / brightness / tint（若明显）。
- inner shadow / glow / outline（若存在）。
- texture / noise / pattern（若存在）。

不要把“柔和阴影”作为最终规则；要尽量落到参数或 range。

## 7. Iconography

提取：
- icon family / source（能识别时）。
- outline / filled / duotone。
- stroke width。
- cap / join character。
- optical bounding box。
- canonical sizes。
- icon-to-text gap。
- baseline/center alignment。
- selected/unselected treatment（有证据时）。

## 8. Imagery

提取：
- aspect ratio。
- crop strategy / object-fit。
- focal point。
- radius/mask。
- border/frame。
- overlay/gradient。
- color treatment / saturation / monochrome。
- placeholder treatment（有证据时）。

## 9. Component Grammar

组件不是“截图里一个矩形”，而是重复视觉规则的载体。

对稳定组件记录：
- purpose/name。
- anatomy / slots。
- outer dimensions。
- internal padding / gaps。
- typography roles。
- color/surface roles。
- icon/image metrics。
- radius/border/shadow。
- alignment。
- variants（有明确视觉差异时）。
- states（只记录已观察/明确描述的状态）。
- fixed / variable properties。

示例：

```text
PrimaryButton
height: control.lg
padding-x: space.control.x
radius: radius.control
label: type.control.md
icon-size: icon.md
icon-gap: space.inline
background: action.primary
shadow: none
```

这比“按钮是蓝色圆角按钮”稳定得多。

## 10. Motion / State Visuals

只有视频、连续帧、代码或明确文字输入时才提取 motion。记录：
- property changed。
- from/to。
- duration。
- delay。
- easing/spring params。
- sequencing。

静态图中的 pressed/disabled/selected 只能在对应状态确实展示时记录。

## 11. Responsive Rules

单张静态图不能证明 breakpoint。多 viewport 输入时提取：
- 哪些属性保持 invariant。
- 哪些值 fluid。
- 哪些结构发生 reflow。
- breakpoint 只能在证据支持的区间内确定；若只知道“在 768 与 1024 之间发生变化”，就记录 interval，不猜精确 900。

## 12. Style Laws

最终允许有少量高层 Style Laws，但每条必须能落回具体 token/rule。

例如：
- “信息密度高”不是规则。
- “table row=36，control=28–32，section gap=24，正文 13/18”才是能生成的语言。

Style Laws 用于远看统一；Parameters / Roles / Rules 用于近看精确。

## 13. Context / Variant Mapping

设计语言不只是一套默认 token。若证据显示同一 semantic role 在不同视觉上下文发生系统变化，必须提取 mapping：
- base / inverse。
- flat / elevated / overlay。
- compact / regular / spacious。
- component size variants。
- light / dark theme。
- selected/disabled/active visual treatment（只有证据时）。

Context 变化可能同时影响 color、border、shadow、opacity、type、spacing，不要只做颜色主题表。

## 14. Relationship / Dependency Rules

除了记录值，还要提取可计算关系：
- equality：两个 inset 共用一个 role。
- inequality：inline < group < section。
- ratio：pill radius = control height / 2。
- formula：derived dimension 由多个 token 组成。
- dependency：component property 引用 semantic role，而不是复制裸值。

优先保存关系，避免在不同组件里复制相同数字后逐渐漂移。

## 15. Optical Micro-geometry

视觉复刻中常见的“看起来居中”并不等于数学居中。重复证据存在时提取：
- icon optical offset。
- glyph/baseline offset。
- badge anchor offset。
- asymmetric padding。
- painted bounds vs nominal box。
- 1px/half-pixel stroke snapping。

单点修正进入 Exception Registry，不提升成全局规则。

## 16. Compositing / Material Stack

对于 glass、overlay、半透明 surface、复杂 shadow，不只记录最终颜色，还要尽量提取叠层顺序：
- underlay/background dependency。
- fill alpha。
- border。
- backdrop blur/filter。
- multi-layer shadow。
- blend mode。
- noise/texture/tint。

无法从最终像素拆出前景 alpha 时，记录 composite observation + Unknown 参数，不伪造唯一解。

## 17. Adjacency / Nesting Grammar

组件单独看对，但组合起来不像，通常是缺少这一层。提取：
- 相邻 row 是否共享 divider。
- first/last child 是否改变 corner。
- card 内嵌 card 时 surface/elevation 是否降级。
- controls 紧邻时 border/radius 是否合并。
- nested inset 是否继承同一 alignment axis。

## 18. Illustration / Graphic Motif（有证据时）

当参考含插画、装饰背景、图形 motif 时，记录其：
- geometry vocabulary。
- stroke/fill character。
- perspective/lighting。
- palette/gradient convention。
- texture/noise。
- repetition/density/scale。

不要让 UI 框架复刻正确，但装饰图形突然换成另一套视觉语言。

## 19. Data Visualization（有图表时）

图表是独立视觉域，Relevant 时提取：
- series palette / reuse rule。
- line/bar/area/marker geometry。
- grid/axis visual treatment。
- tick/label typography。
- legend/tooltip visual grammar。
- annotation treatment。

这里只提取视觉语法，不建模数据业务逻辑。

## 20. Exception vs System Rule

每个视觉事实最终要判断 scope：
- global primitive。
- semantic role。
- context variant。
- component-local rule。
- one-off exception。

“测得很准确”不代表“应该全局复用”。Scope 判断与数值精度同样重要。

## 21. Rendering / Rasterization Regime（有证据时）

有些产品不是单一渲染语言。应明确不同视觉域“怎么被画出来”，而不只记录它们“长什么”。

提取：
- pixel / vector / raster-photo / hand-drawn / 3D 等 regime。
- anti-aliasing / hard stepped edge character。
- effective pixel cell / raster density（可见时）。
- nearest-neighbor vs smooth scaling（可证明时）。
- stroke raster behavior / snapping。
- asset scaling / crop rule。
- regime 适用域：decorative / functional / data-viz / brand / narrative。
- cross-regime embedding：例如 pixel asset 可以放进 smooth vector card，但内部 edge character 不改变。

这类规则如果具有强识别度，通常属于 Style Kernel，而不是普通 imagery 参数。

## 22. Typography Spatial Metrics

无法识别真实字体时，仍应提取影响布局的空间行为：
- observed text bbox。
- glyph run width。
- line box / baseline distance。
- average advance（只在可稳定推导时）。
- role max width。
- wrap threshold / line count。
- multi-line block height。
- icon/text optical alignment。

目的不是反推出唯一 font family，而是让不同字体 fallback 时仍能维持接近的排版空间关系。

## 23. Style Kernel / Grammar / Creative Field 分类

完成视觉域提取后，再做一次“迁移约束分类”。

### Style Kernel

只提升真正构成视觉身份的少量规律：
- signature palette/surface hierarchy。
- signature rendering regime。
- signature type hierarchy。
- signature material/shape law。
- signature icon/illustration character。

### Style Grammar

把可变化内容优先写成：
- inequality。
- ratio。
- range。
- context mapping。
- dependency/formula。
- composition relationship。

不要为了稳定把 Grammar 全转成 exact numbers。

### Creative Field

明确哪些设计问题没有被参考决定：
- 新页面 composition archetype。
- 新组件 anatomy（已有 canonical component 除外）。
- 局部装饰与内容编排。
- 未观测的合法视觉变体。

Creative Field 不需要生成一堆 placeholder token；保持 open 本身就是有效信息。

## 24. Reuse Semantics

设计层需要给下游实现提供复用意图，但不规定 React/SwiftUI/CSS 文件结构。

对稳定组件 / pattern 记录：
- `component_status`: canonical / candidate / local。
- `reuse_intent`: shared / contextual / local。
- `recipe_reuse_policy`: exact / adapt / exemplar。

解释：
- `exact`：同一 canonical component 的视觉 contract 应保持一致。
- `adapt`：保留语法、角色、关系，允许为内容和上下文重新排布。
- `exemplar`：仅是参考中一个合法案例，不应成为新页面默认模板。

推荐原则：

```text
已有 canonical component -> 优先复用
稳定结构跨多个独立场景重复 -> shared candidate
没有合适组件 -> 允许新设计，先 component-local
新设计反复证明有复用价值 -> 再提升 canonical
```

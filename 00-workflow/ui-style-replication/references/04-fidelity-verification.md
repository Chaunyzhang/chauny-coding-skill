# Fidelity & Stability Verification

验证对象是 `DESIGN-LANGUAGE-SPEC` 的两种能力：**参考复刻的稳定性**与**新页面风格延续的稳定性**。不是审美优劣，也不是要求所有新页面长得像参考页。

## 1. Precision Gate

失败条件：
- 关键视觉决定仍写成“适度/高级/舒服/有质感”而没有参数或规则。
- raw screenshot px 被直接当成实现 px，且没有 scale anchor。
- typography 缺 line-height/weight/tracking 等关键维度。
- shadow 只写“柔和”，gradient 只写“淡淡的”。
- component 只有名字，没有 anatomy / padding / token mapping。

## 2. Traceability Gate

抽查关键规则：
- Observed 能回到 source/evidence。
- Resolved 能看到归一逻辑。
- Generated 有明确标记。
- Unknown 没被偷偷补成确定事实。

## 3. Token Stability Gate

检查：
- 是否存在同义近似 spacing/radius/color/type token。
- 相同 component 的重复实例是否出现无解释参数漂移。
- 语义 role 是否被 primitive 名字取代。
- 新值是否真的表达新角色。

## 4. Cross-Reference Consistency

正文表格、component mapping、machine-readable manifest 必须一致。

例如：
- `PrimaryButton.radius = radius.control`
- `radius.control = 12`
- manifest 也必须是 12。

任一处不同即失败。

## 5. Reconstruction Fidelity

用 Spec 重建参考时，按以下层次比较：
1. composition / container / alignment。
2. typography hierarchy 与 line metrics。
3. spacing / geometry。
4. color / opacity。
5. surface / border / shadow / blur。
6. iconography / imagery。
7. component anatomy。

先比较系统关系，再比较局部像素。目标不是逐像素 tracing，而是参数化后仍能还原相同视觉系统。

## 6. Holdout Test

当有多张参考时：
- 用部分图片归纳 Spec。
- 暂不读取剩余图片的细节。
- 用 Spec 解释/重建 holdout 页面。
- 检查是否需要大量临时新 token 才能解释。

如果每个新页面都要新增近义 spacing、radius、type、surface，说明提取的是页面快照，不是设计语言。

## 7. Novel-Component Test

用现有 Spec 描述一个输入中未完整出现但属于同一产品的简单新组件，例如一个 secondary button / small card / list row。

测试重点：
- 能否直接从现有 typography/spacing/radius/color/icon rules 组合出来。
- 是否需要重新凭感觉选值。

如果必须重新设计，Spec 的 generative rules 不够。

## 8. Repeatability Test

同一份 Spec 被再次消费时：
- 不应重新解释 adjectives。
- canonical tokens 不应随机变化。
- fixed/range/responsive/optional 边界不应变化。

稳定性来自 Spec，而不是依赖同一个模型每次做出相同审美判断。

## 9. Source Fidelity > Agent Taste

验证中禁止因为“更干净/更现代/更高级”而主动修改参考。

若源设计存在：
- heavy shadow
- glass/blur
- universal pill
- dense layout
- nested containers
- decorative gradients

只要它们是重复且稳定的视觉事实，就应被准确建模。复刻与优化是两个不同任务。

## 10. Uncertainty Separation Gate

检查三者是否被混为一谈：
- measurement uncertainty。
- allowed design variation。
- reconstruction tolerance。

例如截图测量 `23/24/25` 不应自动变成设计 range `23–25`。

## 11. Scope / Exception Gate

检查：
- 单点 hero/特殊资产是否被错误升级为 global token。
- component-local correction 是否有明确 scope。
- context variant 是否被错误拆成近义 token。
- Exception Registry 中的值是否偷偷被新页面默认继承。

## 12. Dependency Gate

检查 derived values：
- 能由 canonical token/rule 推导的值是否仍被多处硬编码。
- dependency graph 是否出现循环或断链。
- 修改一个 primitive 后，依赖它的 rule/component 是否能一致更新。

## 13. Micro-geometry Gate

对高保真区域检查：
- icon painted/optical bounds。
- baseline / optical offsets。
- asymmetric padding。
- stroke snapping。

不能用“数学居中”覆盖重复可见的视觉补偿。

## 14. Compositing Gate

对透明/玻璃/复杂 depth：
- 是否记录 layer order 与 underlay dependency。
- multi-layer shadows 是否被压扁成一句“soft shadow”。
- composite color 与 source alpha 是否被错误当成同一个事实。

## 15. Domain Coverage Gate

输入中出现下列域时必须覆盖；未出现时不强行生成：
- illustration / graphic motifs。
- data visualization。
- multi-context/theme mapping。
- responsive/fluid behavior。
- motion/state visuals。

完整不是“每个章节都有内容”，而是 Relevant 视觉域没有遗漏。

## 16. Fidelity Contract Gate

验证器必须知道：
- 哪些 anchors must-match。
- 每个 tolerance 的来源。
- tolerance 是否只是 measurement limit，而不是给生成器自由发挥的范围。


## 17. Constraint Calibration Gate

检查“事实确定性”和“生成约束”是否被错误绑定：
- high-confidence local fact 是否被误升成 global hard。
- signature rule 是否反而只写 soft/open，导致身份易漂。
- hard constraint 是否能说明具体原因：用户明确要求 / signature identity / canonical component contract。
- soft rule 是否优先以 range / relationship / context / dependency 表达。

失败信号：大多数 token/property 都被标 hard/global。

## 18. Style Kernel Gate

Style Kernel 应同时满足：
- 数量少，通常约 5–12 条，不追求固定数量。
- 每条能下钻到 token/rule/component/rendering regime。
- 破坏其中任一条会明显改变视觉身份。
- 不包含一次性页面构图、source bbox、偶然内容资产。

若把普通 16px gap、某页 hero 高度、某张图的局部 offset 全部升级成 Kernel，则失败。

## 19. Creative Headroom Gate

在 Extension Mode 下生成至少 2–3 个信息架构明显不同的新页面或新组件，检查：
- 是否守住 Kernel。
- 是否遵守 Grammar。
- 是否仍能产生不同的 composition，而不是复制参考页面骨架。
- 新组件是否可以被创造，而不是因为 Spec 没列出就无法设计。
- open 区域是否没有被无证据 exact values 填死。

**风格一致不等于布局一致。**

失败信号：不同任务最终都收敛成同一种 hero + card stack，只是换文案。

## 20. Weak-Model Guardrail Gate

模拟只执行明确规则、不依赖高水平审美判断的 consumer：
- 仅遵守 Kernel、Grammar、canonical component contract。
- 不额外“凭感觉”补风格。

如果这样仍能得到基本可识别的同产品视觉，说明 Skill 能托住下限。

如果必须依赖 consumer 自己再次猜 palette/radius/type hierarchy，说明 Spec 还太松。

## 21. Strong-Model Freedom Gate

模拟具备较强设计能力的 consumer：
- 给一个参考中没出现过的页面任务。
- 允许在 Creative Field 中自由决定 composition / new component anatomy / local ornament。

若它为了通过 Spec 被迫机械复用参考构图，判定 over-constrained。

若它可以做出新结构，同时 Kernel、Grammar、component identity 仍稳定，则通过。

## 22. Recipe Reuse Gate

每个 layout/recipe 检查 `exact / adapt / exemplar`：
- exact：只用于 canonical component/pattern contract。
- adapt：允许内容与上下文变化。
- exemplar：Extension Mode 不自动继承。

失败：把一个 observed homepage recipe 当成产品所有未来页面的模板。

## 23. Generated Stability Scope Gate

抽查 Generated values：
- 是否声明 style / component / session / instance。
- session/instance 是否在没有新证据时被错误写回 global canonical token。
- 能锁关系就没有不必要地锁 exact number。

目标是 **minimum necessary stabilization**。

## 24. Component Reuse & Creation Gate

同时检查两件事：
- 相同 canonical Component ID 是否保持同一视觉 contract，避免页面复制后漂移。
- 新需求没有合适组件时，是否允许新建 component-local/candidate，而不是强迫套用旧组件。

“复用”与“创新”都必须存在。

## 25. Extension Success Criterion

Extension Mode 最终通过条件：

```text
same identity
+ different valid composition
+ shared components stay shared
+ new components can emerge locally
+ no near-duplicate visual system drift
```

Skill 的目标不是把模型变成参数执行器，而是把自由发挥限制在不会破坏视觉身份的区域。

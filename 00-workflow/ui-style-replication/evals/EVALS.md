# UI Style Replication Evals

目标：测试“设计语言提取的精确度与稳定性”。

## E1 — 单图不能把截图像素当实现 px
Input：一张被缩放过但未知缩放比例的截图。
Expected：记录 source px；提取比例/重复关系；canonical px 标 Resolved/Generated 或保留 Unknown，不声称截图 24px 就是 CSS 24px。
Fail：直接把所有截图测量值写进 token。

## E2 — 多图近似值归一
Input：同一语义 gap 在三张图中测得 7/8/9px。
Expected：结合重复关系归一成一个 candidate/canonical token，并记录 raw evidence。
Fail：创建 7/8/9 三个 spacing token。

## E3 — 近似但角色不同不能乱合并
Input：button radius=12，card radius=16，多图持续如此。
Expected：保留两个 semantic roles。
Fail：因为数值接近强行统一成 14。

## E4 — 文字描述只稳定到必要层级
Input：“做成紧凑、柔和、大圆角的工具型 UI。”
Expected：先解析出 typography/spacing/radius/surface 的关系、层级或范围；需要 concrete value 时再 Generated，并声明 `stability_scope`。Style-level 只锁真正构成身份的决定，其余可为 component/session。
Fail：只输出形容词；或把第一次生成的所有 exact number 永久升级成 global hard token。

## E5 — 不做审美优化
Input：参考图稳定使用重阴影、玻璃、pill controls。
Expected：如实提取 shadow/blur/radius/opacity。
Fail：因为 Agent 觉得“不高级”而删除或弱化。

## E6 — Typography 不止字号
Input：参考中有明确标题/正文/metadata 层级。
Expected：至少提取 family/fallback、size、line-height、weight、tracking、color role、wrap/clamp relevant rules。
Fail：只写 24/16/12 三个字号。

## E7 — Effect 参数化
Input：卡片有半透明 fill、1px border、soft shadow、backdrop blur。
Expected：尽可能提取 rgba/alpha、border、shadow x/y/blur/spread/color/alpha、blur；无法可靠测的项标 low confidence/range/Unknown。
Fail：只写“磨砂玻璃感”。

## E8 — Component grammar
Input：多张图重复出现同一种 button/list row/card。
Expected：归纳 anatomy、padding、height、type/color/radius/icon mappings 与 fixed/variable properties。
Fail：逐张图记录不同坐标。

## E9 — Static motion hallucination
Input：只有一张静态截图。
Expected：motion duration/easing=Unknown。
Fail：给出 180ms ease-out / spring 参数。

## E10 — Responsive evidence boundary
Input：只有 768 与 1024 两个 viewport，布局在两者间发生变化。
Expected：记录 change interval 与两端规则；没有更多证据时不编造精确 breakpoint。
Fail：声称 breakpoint=900px。

## E11 — Holdout generalization
Input：4 张同产品页面，用前 3 张归纳 Spec。
Expected：第 4 张大多数视觉可由既有 tokens/rules 解释，少量真正新 role 才新增。
Fail：第 4 张需要新建一整套 spacing/radius/type/color。

## E12 — Manifest consistency
Input：正文写 `radius.control=12`，YAML 写 14。
Expected：判失败并统一为单一 truth。
Fail：允许两份值长期并存。

## E13 — Image + text override
Input：图中 card radius≈12，用户明确要求“卡片更圆，固定 16”。
Expected：记录 image observation、user override、canonical=16。
Fail：悄悄写 16，丢失证据链；或坚持图片 12 不允许覆盖。

## E14 — Novel component
Input：已有完整 style spec，要求定义一个新的 secondary button。
Expected：优先消费既有 semantic type/spacing/radius/color/icon grammar；允许设计新的 component anatomy/property 组合。确实需要新 role 时先 component-local/candidate，再由后续证据决定是否提升 canonical。
Fail：完全无视既有系统重新造一套视觉语言；或反过来因为 Spec 中没有 secondary button 就不允许设计新组件。

## E15 — Unknown 是正确答案
Input：模糊截图无法识别具体 font family，只有明显的人文无衬线特征。
Expected：记录可观察 typography character/metrics，font family=Unknown 或候选 + low confidence。
Fail：随意指定 Inter/SF Pro 并声称确定。

## E16 — 测量误差不能伪装成设计 range
Input：同一固定 gap 因截图 raster 误差测得 23/24/25。
Expected：canonical=24，measurement_uncertainty≈±1 source-px，behavior=fixed。
Fail：写成 allowed range=23–25。

## E17 — 单点高置信事实仍可能只是局部例外
Input：唯一 hero 卡片 radius=28，其余 12 个普通 card radius=12。
Expected：hero radius 进入 component-local/exception scope；global card radius=12。
Fail：因为 28 测得清楚就把所有 card 改为 28，或新增无语义 global radius token。

## E18 — Context variant 不应造成 token 膨胀
Input：同一 semantic surface 在 base 与 overlay context 分别有不同 alpha/border/shadow。
Expected：保留同一 semantic role + context mapping。
Fail：拆成多个含义不清的 near-duplicate surface tokens。

## E19 — Derived rule 优先于重复裸值
Input：所有 pill radius 都等于对应 control height / 2，存在 28/32/40 三种高度。
Expected：记录公式 `radius=height/2`。
Fail：创建 14/16/20 三个互不相关 radius token。

## E20 — Optical correction
Input：多个 icon-label control 中 icon 为了视觉居中稳定向上 1px。
Expected：记录 repeated optical offset rule，或在对应 component scope 固定。
Fail：强制数学居中导致重建持续偏下。

## E21 — Multi-layer compositing
Input：glass card 使用 translucent fill + backdrop blur + 2-layer shadow + subtle border。
Expected：保存 compositing order、underlay dependency 和多层 shadow。
Fail：只保存最终截图颜色或“soft glass”描述。

## E22 — Illustration domain coverage
Input：UI 参数一致，但多个页面都有同一套几何插画/背景 motif。
Expected：提取 graphic motif geometry/palette/stroke/texture rules。
Fail：只记录 card/type/color，导致新页面装饰视觉完全换风格。

## E23 — Data-viz domain coverage
Input：dashboard 参考含统一图表语言。
Expected：提取 palette、line/bar/marker、axis/grid、legend/tooltip visual rules。
Fail：把图表当成业务内容忽略，导致复刻最显眼区域不一致。

## E24 — Fidelity tolerance 有来源
Input：某 radius 因抗锯齿只能确定 11–13 source-px，但归一系统强支持 canonical=12。
Expected：canonical=12；measurement uncertainty 和 reconstruction tolerance 分别记录且有理由。
Fail：把 tolerance 写成“看起来差不多即可”或允许生成器随意取 11–13。


## E25 — High confidence 不等于 hard/global
Input：唯一 hero 高度=520px，边界清晰，测量 confidence=high；其他页面没有 hero。
Expected：记录 high-confidence Observed，但 `transfer_scope=local/component`，Extension Mode 不继承该高度。
Fail：因为测得准就规定所有未来页面 hero=520。

## E26 — Style Kernel 要小而关键
Input：完整参考含 80+ token/property。
Expected：只挑出少量真正 signature laws 进入 Kernel，其余进入 Grammar/component/local。
Fail：把大部分 token 都设为 hard/global；或 Kernel 只有“高级/温暖”之类无法下钻的形容词。

## E27 — Soft Grammar 优先关系，不锁偶然数值
Input：多个 surface radius 为 24/26/28，但始终满足 outer > nested > tag，且不同组件有合理差异。
Expected：Grammar 保存层级/范围/context；不强行把所有 surface 归一成一个 exact 26。
Fail：为了稳定把所有组件半径写死成同一值。

## E28 — Novel-page extension
Input：参考只有首页任务流；要求生成“发现 / 个人资料 / 搜索结果”三种完全不同 IA。
Expected：三页 composition 明显不同，但 Kernel、type/color/surface/icon/rendering grammar 与 canonical components 延续。
Fail：三页都复制首页 hero + card stack，仅替换文字；或完全跑成另一套产品风格。

## E29 — Creative Field 必须保留
Input：参考没有说明统计模块应使用条形图、环形图还是数字卡。
Expected：该选择保持 open/explore；consumer 可以根据页面目标选择一种，同时沿用现有 color/type/surface grammar。
Fail：Skill 为“文档完整”无证据指定唯一 chart composition。

## E30 — Recipe reuse policy
Input：首页有大型 hero，下方 card stack；另有 canonical TaskRow。
Expected：hero composition 标 `exemplar`，SectionCard 标 `adapt`，TaskRow 标 `exact`。
Fail：所有 recipe 都默认 exact；或所有 recipe 都可随意改变导致组件漂移。

## E31 — Generated stability scope
Input：文字只说“较宽松的列表”，首次生成 row height=52。
Expected：若没有跨参考证据，52 至多 session/component stable；风格层保存 density/rhythm rule。后续独立页面可在 grammar 内适配。
Fail：把 52 自动写成整个产品所有 list 的永久 global token。

## E32 — Shared component identity + new component creation
Input：三个页面使用同一 `SectionCard`，第四页需要此前不存在的 `MetricCluster`。
Expected：三个 `SectionCard` 保持同一 Component ID/contract；允许创建 local/candidate `MetricCluster` 并消费既有 tokens。
Fail：每页复制一个 slightly-different card；或禁止新建 MetricCluster。

## E33 — Rendering regime transfer
Input：参考使用 pixel decorative art + smooth vector functional UI；新页需要新的装饰插画和新功能 control。
Expected：新装饰仍走 pixel regime，新 control 走 smooth vector regime；具体插画内容可自由设计。
Fail：把功能 control 像素化，或因为没有原资产就只能复制旧插画。

## E34 — Typography spatial fallback
Input：原字体无法识别，但参考能测到标题一行 bbox、wrap threshold、line box。
Expected：font family 保持 Unknown/候选，同时记录 spatial metrics；替代字体实现应优先满足 role 的空间行为。
Fail：随意指定字体后让标题大量换行，仍声称 Spec 已满足。

## E35 — Strong-model freedom
Input：给 Extension Mode 一个开放的新页面任务，consumer 具备较强设计能力。
Expected：允许在 Creative Field 中提出新的 composition/局部构件；只要不破坏 Kernel/Grammar 即可。
Fail：Spec 要求逐项复用参考 layout，导致所有设计退化成模板填充。

## E36 — Weak-model guardrail
Input：consumer 不做额外审美推理，只按 Spec 的 Kernel / Grammar / canonical components 组合一个新页面。
Expected：仍能得到基本属于同一产品的视觉系统。
Fail：必须重新猜主色、圆角、type hierarchy、surface material 才能完成。

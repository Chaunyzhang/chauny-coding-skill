# UI Style Replication v2 — Evals

目标：同时测试“守得住”和“放得开”。

## E1 — Unknown screenshot scale
未知缩放截图中的 24 source-px 不得直接写成 CSS 24px。

## E2 — Measurement uncertainty vs variation
固定 gap 因 raster 得到 23/24/25：应 canonical=24 + uncertainty，不能写设计 range 23–25。

## E3 — Semantic clustering
同一 gap 的 7/8/9 可归一；button radius=12 与 card radius=16 若角色稳定不同，不得乱合并。

## E4 — No aesthetic rewriting
参考稳定使用 glass/heavy shadow/pill 时如实提取，不因为模型偏好“优化”。

## E5 — Typography spatial fallback
字体无法识别时 family=Unknown/候选，同时保存 bbox/line box/wrap threshold；不能随意指定字体导致布局漂移。

## E6 — Static evidence boundary
单图不能编造 motion duration、hover、精确 breakpoint、sticky runtime behavior。

## E7 — ONE brand thing
Style Kernel 必须能指出少量真正 signature laws；不能只有“温暖/高级”，也不能把 80+ token 全塞 Kernel。

## E8 — High confidence ≠ hard/global
唯一 hero 高度测得很准，但 Extension Mode 应 local/open；不能因为 confidence=high 就全局继承。

## E9 — Hard budget
若 Kernel/hard rules 数量显著膨胀，应触发 over-constraint warning。

## E10 — Soft grammar
多个 outer radius 为 24/26/28，但层级稳定：应保留 hierarchy/range，不强制所有 surface=26。

## E11 — Creative Field
参考没有决定统计图形式时应明确 open；不能为了文档完整指定唯一 chart composition。

## E12 — Generated minimum stabilization
文字“较宽松列表”首次生成 row=52：52 至多 component/session stable；风格层保存 density/rhythm。

## E13 — Recipe policy
TaskRow 可 exact、SectionCard 可 adapt、首页 Hero composition 可 exemplar；不能所有 recipe 都 exact。

## E14 — Component identity
三个页面使用同一 SectionCard：同一 Component ID/contract；不能复制三个 slightly-different card。

## E15 — Novel component
新 MetricCluster 不存在时允许创建 local/candidate，并消费已有 tokens；不能禁止创新或重建新视觉系统。

## E16 — Rendering regime transfer
参考 decorative pixel + functional vector，新页装饰继续 pixel，新 control 继续 vector；具体内容可以新设计。

## E17 — Context mapping
base/overlay 同一 semantic surface 变化时写 context mapping，不制造 near-duplicate tokens。

## E18 — Derived relationship
pill radius 始终 height/2 时保存公式，不创建互不相关 14/16/20 tokens。

## E19 — Extension page diversity
用同一 Spec 生成发现/详情/个人页：结构应明显不同，但仍属于同一产品。

## E20 — Weak-model guardrail
消费者不做额外风格推理，也应能靠 Kernel/Grammar/components 得到基本正确风格。

## E21 — Strong-model freedom
强模型应能在 Creative Field 中产生新 composition/组件巧思；若只能模板填充则失败。

## E22 — Holdout generalization
前 3 张图归纳，第四张大多数应由已有 system 解释，不能每图新建一套 tokens。

## E23 — Manifest consistency
正文与 manifest 冲突必须失败；不允许长期双 truth。

## E24 — Engineering handoff
同一 Component ID 下游应有共享实现意图；新页面不应要求复制同一 token/icon/component 主体。

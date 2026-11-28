# 04 识图、视觉测量与风格逆向

仅当输入包含参考图、设计稿截图或风格提取/复刻任务时读。目标是从参考材料高精度提取**可跨屏复用的 Style Kernel、Style Grammar 与 Canonical Components**，而不是抄截图像素坐标或按模型偏好擅自美化。

## 1. 先判消费模式（必须）

提取前先明确目标模式，决定约束松紧边界：
- **Reconstruction Mode（像素级复刻参考）**：单屏构图、局部坐标与视觉细节可临时标 `hard / local` 以忠实还原。
- **Extension Mode（提取设计语言做新页面/多页产品，默认）**：源图的页面布局与坐标只算 `exemplar / open`；只把构成品牌身份的 **Style Kernel、Style Grammar（边界哲学、四槽拓扑、控件同模、选中态配方）与 Canonical Components** 固化为跨屏规则，源产品业务结构与内容资产禁止照搬。

## 2. 多源权威分级与高精度测量纪律（必须）

- **Source Registry（多图冲突先定权威）**：存在多张参考图或图文混合输入时，按权威归类：`primary`（核心代表屏）、`secondary`（补充场景）、`component-only`（只借用某组件形态）、`theme-only`（只借用色板/暗色材质）；冲突时高权威覆盖低权威，不能平均混合。
- **Scale Calibration Anchors（源像素 ≠ CSS 像素）**：测量前先确认截图缩放倍率（如 1× / 2× Retina / 压缩缩略图），以标准控件高度或正文字号做锚点校准，再记录逻辑像素值。
- **测量误差 ≠ 允许变化范围（必须）**：栅格截图中近似间距测得 `23 / 24 / 25px` 属于同一设计值的**测量误差（`24 ± 1px`）**，应按语义归并为一个精确候选 token（`24px`），**不能**写成“允许 23–25px 范围”（把测量误差写成范围会在后续施工中放大漂移）；确有不同语义角色时保留差异并写明原因。
- **字体 Unknown 空间回退（必须）**：无法从截图确认确切字体族时，字体名必须标 `Unknown` 并保留可观测空间指标（字高比、字重感、行盒高度、换行密度与几何/人文气质），**严禁把未知字体顺手写成 Inter / SF Pro / Roboto**。
- **合成色与半透明底层边界**：截图中取到的像素色可能是半透明层叠加背景后的合成结果；无法确认真实 alpha 时标清 `Observed composite color`，真实透明度标 `Unknown`。
- **禁止模型审美偏见重写参考（必须）**：忠实记录参考图的真实身份特征（高饱和色、锐利直角、高密度或特定材质）；若参考本身含特殊渲染域（如像素风插画 + 平滑矢量控件），显式记录 `Rendering Regime` 边界，不擅自“现代极简化”洗白参考风格。

## 3. 必须提取的五个维度

1. **Boundary & Containment Grammar（防拼装核心）**：识别参考图的主分层引擎（描边 / 明度色阶 / 留白分割线）、哪一层是嵌入式（Recessed/Flush）、哪一层是结构化卡片、哪一层允许投影。
2. **Structure & Rhythm**：页面壳层骨架（`AppShell / PageHeader / Toolbar / SectionHeader`）、主对齐轴、组内/组间比例律与密度档位。
3. **Visual Math & Tokens**：type roles、spacing clusters、radius family（含是否连续曲率）、control heights、palette semantic roles 与 Context Mapping（亮/暗、激活/失焦）。
4. **Selection & Control Grammar**：提取导航/Tab/列表/开关的选中态配方、控件外壳构造、图标契约（stroke/cap/join/大小）与光学重心偏移。
5. **Style Kernel vs Exemplar 分拣**：用“去掉它新页面还像不像同一产品？”分拣 5–12 条硬身份 `Style Kernel`，将偶然构图降级为 `exemplar` 并写明 `Creative Field`。

## 4. 禁止从静态图编造的事实（必须标 Unknown）

以下属性静态截图无法证明，除非有录屏、源码、交互记录或 Human 说明，否则必须保持 `Unknown`：动效时长与物理曲线、隐藏状态（hover/error/empty/loading/disabled/失焦态）、响应式断点、后端逻辑与权限/生命周期真相。

## 完成标准

产出 `Image Style Extraction Report`（含消费模式、Source Registry、Observed/Resolved/Unknown、Style Kernel、Boundary/Containment/Selection Grammar、token candidates 与 Canonical Components），并编译进符合 `workflow/03-spec.md` 的 Full/Page Spec（通过 `spec-lint.py`）。若结果只是形容词堆砌、瞎猜字体或抄坐标，逆向失败。

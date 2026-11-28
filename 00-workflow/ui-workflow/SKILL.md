---
name: ui-workflow
display_name: UI Workflow
description: 自包含的 UI/UX 设计、视觉语言提取、跨屏风格一致性治理与实现工作流。把产品事实、Human 意图或参考图编译成含封闭风格文法与组件契约的权威 Spec，再按规格实现、机械审计与防漂移；适用于从零设计 UI、已有界面重设计、组件/设计系统建设、识图提取/复刻风格、局部样式修改、以及界面审查与去 AI 味整改。不负责商业战略、后端架构选型或品牌平面插画创意，这类问题交回上游产品或架构流程。
---

# UI Workflow

把输入编译成一套**风格高度统一、可确认、可实现、可机械验证、可跨屏延续**的 UI，不让 Agent 边写边猜或拼出多套画风。

真相链：`Reality / Info Inventory → Structure Blueprint (Skeleton & Slot Budget) → Content Pour-In → Style Kernel & Unity Grammar → UI-DESIGN-SPEC → Primitives & Implementation Structure → Code → Dual-Engine & Rendered Verification`

## 总规则

1. **走最小合法路径**：先按任务大小选路径，只读当下阶段与命中平台的文件；不把小改做成全套流程。
2. **证据四级与最低稳定化**：所有事实标 `Observed / Resolved / Generated / Unknown`；影响业务语义、设计方向或可见行为的 Unknown 必须先问 Human/上游；为补全当前界面而做的 `Generated` 局部决策默认只稳定在 `local/session`，禁止静默晋升为全局风格。
3. **Spec-before-Code 与单屏门禁**：任何 Human 可感知变化必须先落 Spec 再改生产代码。涉及全局视觉方向重塑、换肤或主壳层大改时，铺开全站代码与打包前**必须先交付 1 屏真实渲染图给 Human 拍板**（口头要求“自行跑完自评并出包”不能豁免此门禁，AI 自评仅限筛查机械缺陷）。
4. **先盘信息、先定结构骨架，再填内容与锁文法**：严禁先把所有信息一股脑堆上屏再去“调样式”（`Content-Dump-First`）；必须先将信息分桶裁剪、画出无内容的抽象结构骨架并预演极值容量，证明骨架成立后再往槽位填内容；随后签死 **Style Kernel（5–12 条硬身份底线）→ 6 把封闭统一锁 → Canonical Components（同 ID 单一契约）**。
5. **视觉语法原语前置封闭，页面层禁手写五件套**：`Surface / Control / Selectable / Divider` 等底层视觉语法原语必须在第 1 页动工前先在 `primitive_paths` 建完封闭变体；页面与业务目录严禁现场拼接裸背景、边框、圆角、投影与选中态，只负责排布局与消费封闭原语。
6. **跨平台通用工艺不漏读**：布局防挤压、耗时三档、表单人因、四类空态、可逆防错、材质分层与暗色光学属于通用底线，任何端的设计与审查都必须按需读取 `references/craft/`。
7. **单一真相源与双引擎机械验证**：设计唯一权威是 `UI-DESIGN-SPEC.md`（内嵌同源 JSON Manifest），非平凡实现必须有 `IMPLEMENTATION-STRUCTURE.md`；可见 UI 禁止只看源码或 E2E 通过就宣称完成，必须交付静态 + 运行态脚本审计与真实渲染（多屏并排）证据。

## 归谁定

| 遇到的问题 | 归谁定 | 怎么做 |
|---|---|---|
| 产品目标、业务权限、不可逆后果与领域真相 | 用户 / 上游产品 | 停下问，标 `Unknown` |
| 后端接口、数据模型、全仓技术选型 | 上游架构 / 用户 | 停下交过去 |
| 全局视觉方向与“好不好看”的最终裁决 | Human | 交付 1 屏真实渲染图或 Multi-Screen Parity Package 等拍板 |
| 已批准 Spec 内的局部实现、技术重构与机械修错 | 本 skill | 直接执行并补齐验证证据 |

## 任务路由（默认走最小合法路径）

| 任务 | 默认路径 | 当前先读 | 先别读 |
|---|---|---|---|
| 改单个颜色/间距/文案 | Existing Spec → Patch Spec → Implement → Render verify | `workflow/03-spec.md`、`workflow/05-implementation.md`、`workflow/06-verification.md` | 其余全部 |
| 改一个组件 | Existing System → Component contract → Patch Spec → Verify | `craft/design-system.md`、`craft/interaction-and-forms.md`、`workflow/03-spec.md`、`workflow/06-verification.md` | 识图、未命中适配层 |
| 新增一个页面 | Coverage → Inheritance Gate → UI Definition → 复用 Canonical Components → Page Spec → Implement → Verify | `workflow/01-coverage.md`、`craft/layout-and-feedback.md`、`craft/interaction-and-forms.md`、`craft/design-system.md`、`workflow/03-spec.md` | 识图、未命中适配层 |
| 从零做 UI | Coverage → UI Definition → Alignment → Style Unity & Visual System → Full Spec → Primitives-First → Implement → Verify | `workflow/01-coverage.md`、`workflow/02-human-alignment.md`、`craft/` 全部、`workflow/03-spec.md` | 识图、未命中适配层 |
| 图片/截图提取或复刻风格 | 判定 Reconstruction / Extension 模式 → Image reverse → Style Kernel/Grammar → Full/Page Spec → Verify | `workflow/04-image-reverse.md`、`craft/visual-and-optics.md`、`craft/design-system.md`、`workflow/03-spec.md` | 未命中适配层 |
| 已有 UI 重设计 / 审查整改 | Restore reality → Inheritance Gate → Diagnose → Alignment → Style Unity + Full Spec → 单屏门禁 → Implement → Verify | `workflow/01-coverage.md`、`workflow/02-human-alignment.md`、`craft/` 全部、`workflow/03-spec.md`、`workflow/06-verification.md` | 识图（无参考图时）、未命中适配层 |
| 实现审查 / 去 AI 味与一致性体检 | Restore reality → 静态 + 运行态审计 → Three-Pass 审校 → Findings/Spec | `craft/layout-and-feedback.md`、`craft/interaction-and-forms.md`、`craft/visual-and-optics.md`、`craft/design-system.md`、`workflow/06-verification.md` | 识图、未命中适配层 |

**Inheritance Gate（凡声称继承已有系统时必过）**：必须同时满足 ① 指出已批准的 Full Spec 路径与同源 Manifest、② 包含完整的 Style Kernel + 6 把封闭统一锁 + Canonical Components（含 `reuse_policy`）+ Concrete Recipe、③ 实跑 `scripts/drift-audit.py` 现实对账通过。任一项不过，自动升级为「已有 UI 重设计」，先补齐完整风格文法与 Full Spec，禁止假继承。Human 授权“跳过逐条确认 / 细节我来调”不等于跳过 Visual System，也不豁免全局换肤单屏门禁。

## 文件地图

### L1 流程与协作层（按推进阶段读）

| 文件 | 里面是什么 | 什么时候读 |
|---|---|---|
| `references/workflow/01-coverage.md` | 10 项防漏清单、Stage-Fit 与软件三姿态（主权/瞬态/后台）定场、工作记忆上限 | 新页面、从零设计、重设计起手时 |
| `references/workflow/02-human-alignment.md` | 模糊感受翻译块、免确认边界与单屏门禁优先级、Spec-before-Code、并行 Agent 协作 | 需求模糊、变更可见行为或全局换肤时 |
| `references/workflow/03-spec.md` | Inheritance Gate、前轻后重 Full Spec（Style Kernel/Grammar/6 锁/Canonical Components/Manifest）、Page/Patch/Draft 尺度 | 编译规格或更新 Spec 前 |
| `references/workflow/04-image-reverse.md` | 多源权威分级、Scale 校准、测量误差与允许范围分离、字体 Unknown 回退、Reconstruction vs Extension 双模式 | 输入包含参考图或风格提取/复刻时 |
| `references/workflow/05-implementation.md` | Primitives-First 原语前置封闭、页面层视觉五件套禁写、`IMPLEMENTATION-STRUCTURE.md`、`exact/adapt/exemplar` 工程映射与去重审计 | 准备写代码或重构结构前 |
| `references/workflow/06-verification.md` | 证据分级、三脚本机械审计、单屏门禁、Three-Pass（构图/Diff/跨屏 4 维与多屏并排接触表）、系统偏好三降级 | 审查现有界面或交付实现前 |

### L2 通用 UI/UX 工艺与风格治理底座（跨平台通吃）

| 文件 | 里面是什么 | 什么时候读 |
|---|---|---|
| `references/craft/layout-and-feedback.md` | 内容与状态组合、防挤压原结构（API Key 等条件提醒）、防回流/CLS/滚穿、三档耗时防闪、四类空态、报错三要素、无模式反馈与记状态 | 定义结构、布局、状态、空态、加载与反馈时 |
| `references/craft/interaction-and-forms.md` | 交互闭环、Undo 与高危防错、四类承载容器（Inspector/Popover/Sheet/Alert）与禁叠窗、感知稳定性、直接操作、表单人因铁律 | 设计交互、弹层、表单、导航、菜单与防错时 |
| `references/craft/visual-and-optics.md` | Style Unity 封闭文法锁（边界哲学、四槽拓扑、同模控件、选中 1:1 绑定）、3 个 AI 套路点名、导航/内容材质分层、暗色光学、微排版、连续曲率圆角、流体动效与 Hard Fail | 定义视觉系统、统一风格或视觉审校时 |
| `references/craft/design-system.md` | 三层 DNA（Kernel/Grammar/Creative Field）、Canonical Shell & Components、`exact/adapt/exemplar`、Context Mapping、派生公式、视觉原语与业务组件分离、Exception 与 Spec Delta | 建组件库、定风格身份、跨屏扩展或收口漂移时 |

### L3 平台与领域适配层（仅命中对应场景时加载，不覆盖项目既有视觉语言）

| 文件 | 里面是什么 | 什么时候读 |
|---|---|---|
| `references/adapters/b-end.md` | B 端浮层业务选型、审批中立、数据表列对齐/横滚/批量条、筛选分层与国际化弹性宽度 | B 端后台、表格、复杂筛选、审批流任务 |
| `references/adapters/mobile.md` | 全面屏安全区、触控热区、软键盘语义与防遮挡、Bottom Sheet 与滚动锁死、户外/弱网韧性 | iOS / Android / 小程序 / 移动 H5 任务 |
| `references/adapters/desktop-agent.md` | 无边框窗口拖拽隔离、多栏失焦降亮退让、无限边缘热区、右键菜单纪律、阴影裁切物理、CJK IME、流式滚动与 Agent 真实事件状态机 | 桌面应用（Electron/Tauri/原生壳）或 AI Agent 工作台 |
| `references/adapters/swiftui.md` | SwiftUI 布局与 ownership、连续曲率圆角、系统动态色/Vibrancy、Preview 与真机验证 | SwiftUI / Apple 原生平台项目 |

### L4 确定性脚本与评测（脚本只运行不阅读）

| 文件 | 里面是什么 | 什么时候用 |
|---|---|---|
| `scripts/spec-lint.py` | 校验 Spec 结构、Manifest 合法性、Kernel 数量与硬约束比例、封闭语法锁、组件 `reuse_policy` 与字体矛盾（运行，不阅读）。命令：`python3 -I <skill>/scripts/spec-lint.py <UI-DESIGN-SPEC.md>` | Full Spec 冻结前必跑 |
| `scripts/drift-audit.py` | 静态审计源码：scale 外 spacing/radius、圆角/边框/阴影/字号熵预算、裸色逃逸、页面层禁写视觉五件套、选中态指纹与 `transition: all`（运行，不阅读）。命令：`python3 -I <skill>/scripts/drift-audit.py <源码目录> --manifest <Spec.md> --primitive-paths <原语目录>` | Inheritance Gate 与代码交付前必跑 |
| `scripts/style-grammar-audit.js` | 运行态 DOM 视觉语法聚类审计：同屏容器外壳聚数、同级兄弟容器分裂、同语义控件高度/圆角一致率、选中态兄弟差分与 Reflow（运行，不阅读）。在 Playwright `evaluate` 或 DevTools 中执行 | 多组件/多页面渲染验收必跑 |
| `scripts/shadow-clip-audit.js` | 运行态 DOM 阴影裁切物理审计（运行，不阅读）。在 Playwright `evaluate` 或 DevTools 中执行 | 含外投影、悬浮弹层、滚动容器卡片或无边框窗口时必跑 |
| `evals/EVALS.md` | 本 skill 的全阶段行为测试用例（E1–E33） | 仅修改本 skill 后用于回归实测；执行常规任务时不读 |

## 完成门槛与核心禁止速查

- **12 项 Gate 缺一不可**：Routing → Inheritance → Evidence → Alignment（含全局换肤单屏门禁）→ UI Definition → Style Unity & Visual → Spec（过 `spec-lint.py`）→ Primitives-First & Structure → Implementation → Dual-Engine Drift（静态 + 运行态）→ Rendered & Multi-Screen Parity → Human Review。
- **高频致命禁令（命中任一即失败）**：`Content-Dump-First`（先把所有信息一股脑堆上屏再事后调样式，未先定骨架与槽位预算）、`Combinatorial Style Drift`（词表合规但边框/嵌入式/卡片/选中态拼装分裂）、`Ad-Hoc Page Styling`（页面层绕过原语手写视觉五件套）、`Structural-Squeeze Notice`、`Glass-on-Glass`、`Fake Chrome`、`Modal-on-Modal`、`Mode Error`、`State Reflow`、`Phantom Inheritance`、`Code-First Design`、`Copy-Paste Expansion`、`Source-Only Confidence`、`Test-Pass-As-UI-Pass`、`AI-Judge-As-Taste`、`User-as-Linter`、`Checklist Theater`。

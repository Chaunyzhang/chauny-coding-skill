# 01 Coverage 与定场门禁

新页面、从零设计或已有 UI 重设计起手时读。Coverage 是防漏清单，不是固定流程：每项标 `Relevant / Existing / N/A`，只展开 `Relevant`，不能留空靠“没想到”跳过。

## 1. 定场门禁（Stage-Fit & 软件姿态）

进入字段与交互定义前，必须先用一句话定场：`产品阶段（早期工具 / 成熟产品）× 核心受众（非技术用户 / 开发者）× 软件姿态（主权 / 瞬态 / 后台）× 核心动作`。原因：阶段、受众与姿态直接决定信息密度、默认入口与打断门槛，不先定场就会拿错一套产品逻辑套壳。

- **按软件姿态定调（必须）**：
  - **主权姿态**（用户长时间沉浸的主力工作台，如编辑器、协作台、IDE）：视觉极度克制耐看，优化高频直达与快捷键，面向“持续使用中的中级用户”，不能堆砌宣传大卡与保姆式新手弹窗。
  - **瞬态姿态**（呼出干完一件事就退的小工具，如悬浮托盘、快捷捕获、命令面板）：单一清晰焦点、零多余导航、完成即自动退回后台。
  - **后台姿态**（常驻同步/守护服务）：平时隐身无感，仅在需人工干预时静默亮状态灯。
- **清零无关认知负荷（必须）**：非技术业务界面不能默认裸露开发术语、终端或调试面板，高门槛能力必须收进独立的进阶/开发者开关；早期工具不能堆砌多步开机宣传弹窗与空态说教（无关认知负荷直接抬高理解门槛并打断主任务）。
- **决策点工作记忆上限（必须）**：同一决策点同时呈现的并行选项控制在 **≤ 4 项**；超出时必须分组、提炼主次或收进次级菜单（人脑工作记忆一次稳定承载约 4 个对象，选项墙会诱发误点或跳过）。
- **上下文就地可见（必须）**：完成当前步骤所需的上游信息必须在当前视口可见或一键展开，不能要求用户凭记忆跨越多个界面搬运信息。
- **先想透结构再填内容（Structure-Before-Content，必须）**：拿到产品信息清单后，**不能**先把所有字段、状态、指标和按钮全堆到屏幕上再做视觉微调（内容一旦倒满屏幕，结构就会被锁死成杂乱拼盘，事后怎么调间距都救不回来）。必须严格按三步思考：① **信息三桶分流**（首屏主路径 / 随主对象退后的辅助信息 / 延迟按需展开的次级与配置项）；② **先立无内容的抽象骨架与槽位预算**（定 Region/Section 树、唯一职责、每槽容量上限，并预演真实数据灌入后的形态）；③ **骨架过关后再把内容按槽填入**（详细契约见 `references/craft/layout-and-feedback.md` §1）。

## 2. 10 项防漏扫描

1. **Reality / Scope**：用户与核心任务；核心对象与主/次动作；平台、设备、repo 与既有 UI / Design System；不能擅改的产品/架构/权限事实；任务粒度（Full / Page / Patch / Component / Implementation-only）。
2. **Evidence / Human**：关键结论是否标 `Observed / Resolved / Unknown`；是否存在模糊感受需先翻译确认；参考图是单图、多图还是多断点。
3. **Content / IA**：字段与集合（required/optional）、数量与长度极值、缺失/空态、溢出/截断/换行、分组排序、导航与报错微文案。
4. **Hierarchy / Composition**：主任务/主对象/主动作/主信息；视觉焦点顺序；`Surface / Region / Section / Pattern / Component` 边界；对齐轴、容器策略与滚动 ownership。
5. **State / Interaction / Feedback**：domain / data / operation / permission / environment / interaction 状态组合；owner、入口/出口与闭环；耗时三档、防挤压落点与可逆/防错。
6. **Visual System**：Visual Laws、先点名 3 个 AI 默认套路、构图语法、排版/间距/颜色/圆角/材质/图标/动效、Visual Math 与 Craft Floor、Forbidden。
7. **System / Reuse**：token / primitive / component / pattern；Variant/State/Owner 分离；shared vs local；图标/资产/格式化器单一来源。
8. **Adaptation / Accessibility**：视口/窗口/安全区；键盘/焦点/触控热区；字体缩放/多语言/RTL；对比度下限与系统偏好三降级。
9. **Implementation Mapping**：UI 元素 → data/view model；state/mutation owner；event → action/command；pending/result/recovery。
10. **Verification**：真实渲染多态、内容压力、Drift 与阴影裁切机械扫描、Structure 审计、Two-Pass 审校与 Human 视觉签发。

## 3. 视觉秩序快速检查

完整 Surface 若标为 `Relevant`，起手至少检查：唯一主焦点、有限对齐轴、组内/组间距离明显对比、辅助信息弱化、容器数量克制、数字/状态/文本列对齐。发现秩序问题直接进入 `references/craft/visual-and-optics.md`，不能用换色或加阴影掩盖。

## 完成标准

已选最小合法路径；定场一句话明确；所有 `Relevant` 项均有明确决定、既有来源或显式 `Unknown`，不存在逼用户当 linter 的空白。

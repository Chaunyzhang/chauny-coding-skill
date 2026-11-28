# 视觉秩序、风格统一文法与 Craft Floor

定义视觉系统、锁死跨屏风格统一、优化已有 UI 或执行视觉审校时读。目标是把感觉、参考与产品语义编译成**统一物理世界、单一造句文法、零低级脏乱的视觉系统**。

## 目录

- 1. 输入优先级、Style Kernel 与默认套路点名
- 2. 风格统一封闭语法锁（治“拼装怪 UI”，必须）
- 3. Visual Order 与布局家族
- 4. Visual Math、连续曲率与微排版红线
- 5. 材质分层、暗色光学、对比度与数据墨水比
- 6. 浏览器原生表面与流体动效
- 7. 常见相容组合（校准）
- 8. Craft Floor：Hard Fail（硬禁令）
- 9. Default Refuse 与非缺陷保护线
- 10. Final Subtraction Audit 与 Concrete Recipe Gate

## 1. 输入优先级、Style Kernel 与默认套路点名

输入优先级：`Human correction / Avoid > 已批准 Existing Spec > 高质量视觉证据 > 本模块知识 > Agent 自由发挥`。已有合格 Spec 时默认继承，不为“显得更好看”擅自换语言。

- **从感觉到 Style Kernel（5–12 条硬底线）**：把 Human 形容词拆成 **Primary（控结构）/ Secondary（不破坏 Primary 加味道）/ Micro-expression（局部交互反馈）/ Avoid（veto）**，冲突不做平均；通过“去掉它新页面还像不像同一产品？”测试筛出 5–12 条可执行、可下钻到 token/组件的 **Style Kernel**（分层治理解耦见 `references/craft/design-system.md`）。
- **先点名 3 个 AI 默认套路再设计（必须）**：进入 Concrete Recipe 前，必须显式写出当前界面类型最容易滑向的 3 个 AI 默认套路（如无品牌依据的蓝紫高亮、全屏毛玻璃叠卡片、同屏多套选中态或混装卡片与平铺）及规避决策（不先点出名字，写代码阶段会自然滑回平均模板）。

## 2. 风格统一封闭语法锁（治“拼装怪 UI”，必须）

Token 只是词典，风格统一是同一套造句语法与物理世界假设（双向语义对齐律：**语义相同 → 形态必须相同；语义不同 → 才能变，且变化必须服从同一套物理文法**）。写第一行代码前，Spec 必须签死以下 4 把封闭单选锁，禁止写“视情况而定”：

1. **全局边界哲学单选锁（三选一互斥，治“有的有框有的没框”）**：
   - `hairline-embedded`（描边/发丝主控）：同底布或微色差，统一用单一 1px 低对比细线划分结构，静态内容禁加外投影；
   - `tonal-layered`（明度色阶主控）：靠 `surface.0/1/2` 明度差拉开层次，常规容器零边框、零投影；
   - `bordered-card`（统一卡片外盒）：所有独立内容块统一 1px 同色细边 + 单一容器圆角档，禁止部分模块无框裸奔、部分重投影。
   阴影只发给浮层白名单（Popover / Modal / Dropdown / Toast）；全站最多允许 1 个显式写明作用域的例外（如独立设置页用 Grouped），同级相邻模块严禁混用两套边界引擎。
2. **四槽容器拓扑分界律（治“有的嵌入式有的结构化”）**：
   - 在 Spec 填死四层户口：`L0_shell`（贴边分栏 `embedded-split` vs 浮岛 `floating-pane`）、`L1_section`（`divider-only` / `tonal-well` / `bordered-card`）、`L2_item`（`flat-row` vs `inset-row`）、`L3_overlay`（唯一允许投影与独立悬浮边界）。
   - **嵌入式（Recessed）白名单**：内凹浅/深槽只发牌照给可填充或从属槽位（输入框、搜索槽、代码块、拖拽区、空槽井），禁止拿来装普通同级业务块。
   - **同级同拓扑 + 嵌套降级律**：同一屏同级相邻模块拓扑必须一致（不能左卡右裸）；容器每嵌套一层边界必须自动降级（卡片内用平铺列表或分割线，严禁卡片套卡片）。
3. **控件家族同模锁（治“圆角乱、同排高低不齐、悬停各自为政”）**：
   - **高度阶梯锁**：全站交互控件锁定 3 档高度（如 `sm=28 / md=32 / lg=40px`），同一行并排的 Input、Select、Button、Segmented **强制同档同高**；
   - **同语义同壳锁**：同语义控件共用一套外壳构造与角色圆角（禁止 Button 8px、Input 6px、Select 10px）；
   - **统一交互物理（State Layer）**：全站 Hover / Pressed / Disabled 共用同一公式（例如统一叠微透明蒙层或统一底色升一档、Disabled 统一降不透明度），禁止 A 按钮悬停变色、B 按钮悬停放大、C 按钮出阴影。
4. **选中态「语义 → 视觉」1:1 封闭绑定锁（治“选中态好几种”）**：
   - 全站选中/激活态总量 **≤ 2 种配方**，且必须在 Spec 写死语义绑定字典（例：轻量项 `nav_item / list_row / menu_item / segmented_option / filter_option` 全部绑定唯一配方 A，可选重型块或顶栏视图 Tab 绑定配方 B；其余写法显式列入 `forbidden`），键盘 `:focus-visible` 全站唯一公式。
5. **骨架组件与三层 DNA 锁（第 5、6 把锁见 `references/craft/design-system.md`）**：同步在 Spec 签死 **Canonical Shell & Components（同 ID 单一契约与 `exact/adapt/exemplar`）** 与 **Style Kernel / Creative Field（不变量与开放区边界）**。

## 3. Visual Order 与布局家族

风格之前先立秩序。完整 Surface 必须明确：**Focal order**（单视口默认唯一第一焦点）、**Alignment axes**（少量主对齐轴）、**Grouping**（组内紧、组间松）、**De-emphasis**（次要元信息主动退后）、**Container strategy**（删掉框后关系仍清楚就优先删框）、**灰度检查**（去色后主次、分组与阅读路径依然清晰）。

常用布局家族：`Editorial / long-form`、`Sidebar workspace`、`Split detail`、`List → detail`、`Dashboard / modular grid`（必有主卡，不全卡同权）、`Canvas + inspector`、`Immersive / media-first`。Product UI 不为标新立异破坏熟悉的导航、表格与表单习惯。

## 4. Visual Math、连续曲率与微排版红线

### 4.1 Typography 与微排版
- 只从批准 type roles/scale 取值，同一 role 固定 `font-size + line-height + weight + tracking`；相邻层级辨识度不足（如 `14/18/20` 后两级过近）应合并或拉开。
- **光学尺寸与行高字距反比（必须）**：大标题（≥ 20px）用紧凑行高（`1.1–1.25`）与微负字距防散架；正文用舒展行高（拉丁 `1.45–1.6`，中文/含变音符多语言 `1.5–1.75`）；全大写小标签微扩正字距；小号正文禁止 `< 400` 极细字重防发虚。
- **单行可读宽与防撑爆（必须）**：长正文限制单行可读宽度（英文 `45–75ch`，中文约 `28–42` 字），宽屏不拉成通栏长龙；按钮文字不无意折两行（弹性宽或 `whitespace-nowrap`）；长无空格串（URL / Hash / ID）显式截断或 `overflow-wrap: anywhere`。
- **数字与暗色字重**：动态数值、计时、金额与表格数据列必须用等宽数字（`tabular-nums`）；RTL 下数字、版本号、代码与进度条保持 LTR；暗色模式下若字体因光晕偏粗，应该评估下调半档或一档字重。

### 4.2 Spacing、Alignment 与光学微几何
- 只用有限 spacing scale（如 `0/4/8/12/16/24/32/48`），归并近义值；严格满足 **`元素内边距 < 同组 gap < 跨模块 gap`**；**标题上方留白必须大于标题下方留白**（亲近律决定标题归属下方内容）。
- 同组边缘对齐，无理由 `3–8px` 错轴判缺陷；**光学对齐优先于数学居中**（播放三角、向右箭头等非对称图形按视觉重心设可复用偏移规则，不死按外框几何居中）。

### 4.3 几何家族、连续曲率圆角与图标契约（必须）
- **圆角预算（≤ 4 档）**：全站常规非零非 pill 圆角去重**不能超过 4 档**（如 small control / standard control / surface / modal）；pill 仅用于确需胶囊语义的场景。嵌套圆角遵守同心关系 `R_inner = max(0, R_outer - padding)`，通过配对外层圆角与 padding 使内层圆角落入批准 scale 内。
- **连续曲率圆角与 Web/Electron CSS 落法**：原生与现代浏览器/桌面壳优先采用平滑过渡进直线的连续曲率圆角，替代直线硬切圆弧的普通圆角。在支持原生 CSS `corner-shape` 的环境（Chromium 139+ / 现代 Electron）下，通过 `@supports (corner-shape: squircle)` 渐进增强：
  - **适用范围**：只用于独立矩形容器（卡片、面板、弹窗、气泡、输入框、矩形按钮与方形图标容器），不能全局通配误伤其他元素；
  - **光学半径补偿（必须）**：连续曲率圆角更贴近外角、同像素值视觉上显得更尖，开启 `corner-shape: squircle` 时在 `@supports` 内将对应圆角 token 做 **`1.35×–1.5×` 光学半径补偿**（不支持环境自然回退原 `border-radius`），补偿值纳入 Spec manifest 统一管理；
  - **正圆与全胶囊防变方（必须）**：头像、状态圆点、开关圆钮与全胶囊元素（`border-radius: 50%` 或 `9999px`）**必须显式保持 `corner-shape: round`**（否则超椭圆曲率会把正圆压成方圆）。
- **图标、投影与渲染域契约**：全站图标锁定单一风格家族，明确 `stroke width / cap / join / nominal box / icon-to-text gap` 与状态变化规则（禁细线框与粗实心图标混框）；若产品含特殊渲染域（如像素风插画配平滑矢量功能控件），必须显式写清 `Rendering Regime` 边界防止互串；阴影必须模拟顶光带垂直向下偏移，圆角裁切放内层、外投影放外层。

## 5. 材质分层、暗色光学、对比度与数据墨水比

- **导航/控制层 vs 内容层严格分界，严禁玻璃叠玻璃（必须）**：半透明、毛玻璃材质**只能用在浮于上方的导航与控制层**（顶栏、侧栏、工具栏、悬浮操作条、弹层）；**严禁铺在内容层**（正文、列表、卡片、表格、整屏底板），更严禁两层半透明材质上下叠放。
- **普通底 vs 分组设置底双轨制 + 四级标签阶梯**：内容流与文档区用扁平底布靠留白与字阶分层（Standard），设置页与密集表单才用明暗反衬的分组容器底（Grouped）；文字层级按 4 级对比阶梯递减（主文 / 副文 / 辅助元信息 / 占位禁用）。
- **暗色模式物理规律（必须）**：禁止纯黑 `#000000` 铺大底配纯白 `#FFFFFF` 铺大段正文（引发光晕眩光 halation）；暗色层次靠**表面越往上越亮（同色相微明度阶梯）+ 低透明亮细边**表达；暗色下的强调色与状态色必须**适度降饱和**防视觉震颤；着色表面上的次级文字带入该色相或前景色微调，不用死灰。
- **多栏失焦退让**：多面板或多窗口同屏时，仅当前聚焦面板/窗口使用主强调色选中态，非活跃面板/窗口的选中态自动退化为低饱和中性灰。
- **对比度下限与图文保护蒙层（必须）**：常规正文对比度 **≥ 4.5:1**，大号字、核心图标与输入边框 **≥ 3:1**；压在图片、视频缩略图或动态背景上的文字/图标必须加半透明渐变保护蒙层（Scrim）；图片与头像锁比例（`object-cover`）并定义裂图兜底。
- **数据墨水比最大化**：看板、表格、时间轴与检查器删掉装饰性粗网格线、冗余边框、无意义渐变填充与每行重复的单位文字（单位提到表头）；多组趋势对比优先用同尺度小倍图。

## 6. 浏览器原生表面与流体动效

- **Browser Surfaces 全量纳管（必须）**：文本选区高亮（`::selection`）、输入光标（`caret-color`）、焦点环（`:focus-visible`）、滚动条外观与多行输入框原生右下角拖拽角（默认 `resize: none`）必须全部纳入当前色板与视觉体系。
- **动效频率分级（必须）**：定义 `response / state / structural` 三类时序。**每天百次级的高频或键盘驱动动作（快捷键、命令面板开关、高频列表切换）不能加动画**（0ms 即时响应）；低频弹层/抽屉才用短促过渡（`< 300ms`），避免无理由 bounce/overshoot。
- **流体物理与可打断性（必须）**：动画播到一半用户再次点击或反向拖拽，**必须在当前帧立刻打断并改向接管**，禁止动画期间锁死点击；弹层从接近终态（`scale(0.95)` + 透明度）过渡，触发式弹层从触发原点方向展开并缩回原点保持空间连续性，越界拖动用柔和阻尼；`:active` 提供轻微按压反馈；仅显式过渡 `transform` / `opacity`，**严禁 `transition: all`**。
- **主题切换零闪烁（必须）**：浅/暗主题 0ms 瞬切，禁止全局过渡动画导致整页色值互溶脏闪；兼容系统偏好三降级（见 `references/workflow/06-verification.md`）。

## 7. 常见相容组合（校准，不是模板）

- **Minimal + Lively**：flat/克制色板托底 + 活力落在图标性格与交互反馈，禁满屏渐变与多焦点。
- **Warm + Mature**：暖中性色 + 克制圆角与稳重排版，抑制糖果色、过大圆角与弹性过冲。
- **Professional + Technical**：规则网格 + 清晰数据/状态对比，不把正文全变等宽字、不牺牲层级。
- **Premium + Editorial**：少而准的焦点与排版主导，不把“大留白 + 衬线体”当万能公式。

## 8. Craft Floor：Hard Fail（硬禁令）

出现任一条即不能进入最终 Spec 或交付：
1. **Combinatorial Style Drift（风格组合分裂）**：同级相邻模块一半有边框一半无边框、一半嵌入式一半独立卡片、同行控件高度或圆角不一致；
2. **框套框无新语义**，或把桌面主画布无理塞进悬浮大圆角外壳；
3. **层级塌缩**：标题、CTA、卡片、accent 同时高强调；
4. **Typography / Spacing / Color / Radius / Border / Shadow / Icon entropy**：随机近义值增殖、非零非 pill 圆角超 4 档、边框/阴影/字号超 Manifest 预算；
5. **Selection grammar 分裂**：同屏混用 > 2 种选中/激活态、同类语义用不同选中配方、或多栏同时亮刺眼主色选中态；
6. **圆角容器单侧竖条 & 零偏移发光**：圆角框边缘贴彩色激活竖条，或无偏移外发光冒充层次；
7. **玻璃叠玻璃 & 内容层铺毛玻璃**：半透明材质侵入内容层或双层叠加毁掉对比度；
8. **条件性文字条挤压原结构**：未配 API Key 等提示条硬塞文档流顶矮主画布或挤歪对齐；
9. **State geometry jump / Reflow**：`hover/focus/selected/loading/error` 切字重或边框引起尺寸跳动；
10. **结构迁就内容 / 零数据抹平结构底子**：并排模块或同排卡片随条目多少高低不齐，或零数据/未启用态把热力图、点阵、坐标轴等可视化骨架整块删除塌成大片死空；
11. **原生表面未纳管**：露出默认 `textarea` 拖拽角、刺眼默认蓝聚焦框或割裂滚动条；
12. **暗色眩光 & 图文无蒙层**：纯黑大底配纯白正文、图片压字无 Scrim 蒙层、图片拉伸变形；
13. **假壳子死入口 / 弹窗叠弹窗 / 哑巴禁用提交按钮 / 基础可访问性与内容压力失败**。

## 9. Default Refuse 与非缺陷保护线

无产品 Brief 或品牌依据时默认拒绝（确有理由须在 Spec 写清原因）：无品牌依据的默认蓝紫/电光蓝强调色与冷蓝黑渐变底、装饰性渐变、到处 glass/blur、all-card 同构卡片墙、universal pill、普通内容重阴影、每节 eyebrow/编号/divider 装饰 spam、Emoji 冒充功能图标、大面积无内容死空面板、列表每行平铺 4–5 个同等按钮（操作墙）、上下紧贴两排水平 Tab（双层 Tab 汤）、非分析页顶部硬塞带涨跌徽章的虚荣 KPI 卡片、为新奇破坏熟悉导航。

**非缺陷保护线（防止过度抹平）**：已在批准 Spec 中写明理由的品牌高饱和色/戏剧性字阶/不对称构图、为特定受众明确选定的材质与密度、本次改动范围之外的既有稳定代码，属于设计决定而非缺陷，不得强行抹平回单一极简风。

## 10. Final Subtraction Audit 与 Concrete Recipe Gate

- **Final Subtraction Audit**：交付前机械删减无职责噪声——去掉后关系仍清楚的框/线/底色、无语义随机色、只解释系统不帮当前任务的辅助小字、重复强调手段与重复单位文字；缩小/去色看能否一眼分辨主焦点与路径。
- **Concrete Recipe Gate**：进入高保真或实现前必须得到具体数值与封闭锁：`Style Kernel / Boundary Philosophy / L0–L3 Containment Topology / Selection 1:1 Map / Control Height & Radius Family (≤4) / Type Roles / Spacing Scale / Color Roles+Values / Material Layering / Shadow Whitelist / Browser Surfaces / Icon & Scrim / Motion / Canonical Components / Forbidden`。若仍是“适度圆角、舒适留白、现代高级”，视觉设计未完成。

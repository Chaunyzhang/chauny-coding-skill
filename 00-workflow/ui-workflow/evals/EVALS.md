# UI Workflow Evals

目标：测试 Agent 在无额外上下文时的真实行为，而不是检查输出里是否“提到某个词”。本文件只在修改 `ui-workflow` 后用于回归实测，常规任务时不读。

## 目录

- 常规与路由用例（E1–E10）
- 实现、结构与继承用例（E11–E18）
- 平台与领域适配用例（E19–E22）
- 视觉工艺、认知裁剪与门禁用例（E23–E26）
- 布局防挤压、苹果级层级与人因防错用例（E27–E29）
- 风格统一封闭锁、原语前置封闭与双引擎审计用例（E30–E35）

---

## 常规与路由用例（E1–E10）

### E1 — 小改不能过杀
**Input:** “把现有 primary button 背景从 A 改成 B，其他不动。”

Expected:
- 读取 Existing Spec，走 Patch Spec；Preserved / Changed 清楚。
- 不重新做 Coverage / 视觉方向 / 整页构图；完成后做 rendered verify。

Fail:
- 重跑完整设计流程，或擅自改 radius / type / motion。

### E2 — Human 模糊反馈先对齐
**Input:** “这个拖进去太跳了，我想顺一点，但别飘。”

Expected:
- 翻译为可观察变化、保持不变项、motion 候选与 Unknown。
- Human confirm 后先改 Spec，再改代码。

Fail:
- 直接改动画试试看，或代码先跑事后补 Spec。

### E3 — UI 从零，视觉必须具体
**Input:** “做一个安静、温暖、成熟，但有一点生命力的 Todo 首页。”

Expected:
- 定义 content / state / hierarchy 后再进入视觉；输出 Visual Laws 与 3 个默认 AI 套路规避决策。
- 明确 Composition、type roles、spacing scale、relationship gaps、radius、selection grammar、surface/depth、color roles+values、icon、motion、Forbidden，并编译 Full/Page Spec。

Fail:
- 只输出“温暖极简”与大概方向，实现 Agent 仍需自己猜数值。

### E4 — Visual Math 抓弱层级
**Input:** 页面使用字号 `14/18/20`；同组 gap=16，跨组 gap=20；多个同级标题左边缘差 4px。

Expected:
- 指出 type hierarchy 后两级辨识度弱，而不是机械要求固定 1.25 比例。
- 指出 16/20 relationship contrast 弱，应从现有 spacing scale 拉开。
- alignment drift 判为 Hard Fail。

Fail:
- 因为数值不同就判合格，或强制所有项目用死板固定比例。

### E5 — 框套框
**Input:** section card 内再套三个无独立语义的小 card，仅为制造层次。

Expected:
- 应用“去掉内层框后关系是否仍清楚”测试，优先用 spacing / type / surface 分组。

Fail:
- 继续加 border / shadow 修层次。

### E6 — 图片逆向不幻觉
**Input:** 单张静态 App 截图。

Expected:
- Observed / Resolved / Unknown 分离；提取 structure、Visual Math、Visual Laws、token candidates。
- motion / breakpoint / state owner 保持 Unknown。

Fail:
- 编造 180ms ease-out 等无证据参数，或抄坐标而不归纳系统。

### E7 — 多图归一 token
**Input:** 三张同产品截图里类似 gap 测得 7/8/9px。

Expected:
- 识别重复关系，优先归并为一个 token 候选（如 8px），除非有证据证明 role 不同。

Fail:
- 建 7/8/9 三个近义 token。

### E8 — 状态组合
**Input:** Task 已完成、离线、待同步且获得 focus。

Expected:
- 支持多维状态同时成立，分别说明 owner / 表现 / 允许动作。

Fail:
- 强行塞进单一 enum 或只保留一个状态。

### E9 — 第二页不能复制扩展
**Input:** 已有 Todo Home，新做 Chat 页；两页共享 TabBar、icons，列表行/气泡可数据驱动。

Expected:
- 写代码前有 `IMPLEMENTATION-STRUCTURE.md`；TabBar/icons 共享单一来源，重复行数据驱动。
- 单用 Hero/Composer 无复用或独立状态需求时保持 local；写完后做去重审计。

Fail:
- 复制 TabBar/SVG/markup 等用户提醒再抽，或一切皆过度组件化。

### E10 — Drift
**Input:** Spec spacing=`8/12/16/24`，第三页出现 `15/23`；新蓝色 CTA 未在 Spec 中。

Expected:
- `15/23` 判疑似 drift 并归并或解释新 role；新 CTA color 必须先进入 Spec 否则阻塞交付。

Fail:
- 把近似值解释为“细致手调”。

---

## 实现、结构与继承用例（E11–E18）

### E11 — 实现发现新设计决定
**Input:** 实现拖拽时发现需要“失败弹回动画”，Spec 未定义。

Expected:
- 停代码；形成 Candidate Decision；必要时 Human confirm；先改 Spec 再实现。

Fail:
- 在代码里先加 spring，最后补文档。

### E12 — 纯重构不制造审批
**Input:** 抽取重复 renderer，不改变 DOM / 视觉 / 行为。

Expected:
- 更新 `IMPLEMENTATION-STRUCTURE.md`；不制造虚假 Patch Spec 或视觉审批。

Fail:
- 把技术重构包装成视觉变更审批。

### E13 — Product UI 不为原创破坏习惯
**Input:** Dashboard 想“更有个性”。

Expected:
- 个性放在 palette / type / surface / icon / motion / density；保留熟悉的导航、表格、筛选与 form affordance。

Fail:
- 为差异化把 sidebar 放到反常位置或破坏常规表格交互。

### E14 — Rendered evidence
**Input:** 代码 lint/test 全过，但未打开 UI。

Expected:
- 不宣称完成；渲染 Relevant states / content stress / viewport 后再交付。

Fail:
- Source-only confidence。

### E15 — 规范正确但视觉秩序普通
**Input:** 后台用户表格：标题弱、辅助小字很多、筛选器一排 outline、头像随机多色、表格列对齐松散、所有元素视觉音量接近。

Expected:
- 先指出 focal order、alignment、grouping、de-emphasis、container strategy、table numeric/text/status alignment 与数据墨水比。
- 提出灰度检查与 Final Subtraction Audit；归并无语义随机头像色；修改先入 Spec 再实现。

Fail:
- 只调配色/圆角/阴影，或继续加 Card/border。

### E16 — 假继承（Phantom Inheritance）
**Input:** 已有 UI 只做过一次换皮（定了配色、面板圆角），token 只有 2 档间距、没有控件高度；任务是“沿用 token 做信息架构整理”。

Expected:
- 执行 Inheritance Gate：缺 Full Spec 与完整 Concrete Recipe → 判不合格；跑 `drift-audit.py` 对账。
- 自动升级为“已有 UI 重设计”，先补 Visual System + Full Spec，再做 IA。

Fail:
- 写 Page/Patch Spec 直接开工，放任施工方各自写裸值。

### E17 — 授权跳过确认 ≠ 跳过视觉系统
**Input:** Human：“快速把内容补齐，细节我自己和另一个 Agent 去微调。”

Expected:
- 跳过逐条审美确认；但 Visual System（scale、控件高度、radius、选中态、组件写法）缺失时仍先补齐，或明确告知缺这一层会导致微调无从下手。

Fail:
- 把授权理解为不做视觉层，交付上百种裸值。

### E18 — 测试全过不等于 UI 合格
**Input:** 功能 E2E 全部通过（按 aria-label 点击），未跑 drift 扫描，未看渲染截图。

Expected:
- 不宣称 UI 完成；附 `drift-audit.py` 汇总与关键页面 rendered evidence 后再交付。

Fail:
- 以 E2E 通过作为 UI 验收依据。

---

## 平台与领域适配用例（E19–E22）

### E19 — B 端审批与长表单浮层选型
**Input:** 设计企业采购审批列表：点列表行核对 12 个字段并参照底层列表修改备注；底部有“审批通过”和“驳回”两个按钮；点击“批量删除”触发删除。

Expected:
- 按需加载 `references/adapters/b-end.md` 与 `references/craft/interaction-and-forms.md`。
- 12 字段轻编辑用侧边抽屉（Drawer）保留列表上下文，含未保存录入禁点遮罩静默丢失。
- “通过”与“驳回”视觉中立同权；“批量删除”用模态确认框写清对象后果、动宾按钮且默认焦点落在取消。
- 数值列右对齐配 `tabular-nums`，按钮不写死窄固定宽度。

Fail:
- 把 12 字段塞进可点遮罩直接关闭的居中弹窗，或涂色诱导审批点击。

### E20 — 移动端全面屏安全区、键盘与滚动穿透
**Input:** 移动 H5 表单与筛选页：底部吸底“提交订单”按钮、手机号与短信验证码输入框、点击弹出底部筛选抽屉。

Expected:
- 按需加载 `references/adapters/mobile.md`。
- 声明 `viewport-fit=cover` 与底部安全区留白；触控热区 ≥ 44pt/48dp 且相邻间距 ≥ 8pt；输入框字号 ≥ 16px 且不禁缩放。
- 手机号配 `tel`，验证码配 `numeric` + `one-time-code`；定义聚焦防遮挡与收起行为。
- 底部抽屉展开锁死底层滚动（`overscroll-behavior: contain`），关闭恢复原滚动位，表单抽屉不禁遮罩防丢。

Fail:
- 吸底按钮紧贴物理底边、全部纯文本键盘或存在滚动穿透。

### E21 — 桌面 Agent 工作台：真实状态、IME 与阴影裁切
**Input:** 桌面 AI Agent 对话与产物分栏工作台：输入框支持中文回车发送、右侧流式展示工具执行与文件修改、卡片带外阴影且放在可滚动容器内。

Expected:
- 按需加载 `references/adapters/desktop-agent.md`。
- 明确 CJK 输入法选词回车守卫与流式输出回溯冻结规则（用户向上滚动不强行拉回底部）。
- 任务状态绑定真实事件，区分“已发停止”与“已安全中止”，写文件授权列明目标路径，预览与落盘分界清晰。
- 阴影与圆角裁切内外分层或在滚动容器按外扩余量留白，交付时用 `scripts/shadow-clip-audit.js` 验证。

Fail:
- 用前端定时器伪造进度、中文选词回车误发，或把所有 `overflow: hidden` 全局改 `visible`。

### E22 — 领域适配不得覆盖项目已批准视觉语言
**Input:** 消费级品牌已有批准的 Full Spec（深色质感卡片、品牌色板与 5 档字号），现新增一个移动端底部抽屉页面。

Expected:
- 按需加载 `references/adapters/mobile.md` 的物理与交互约束，视觉皮肤严格继承已批准 Full Spec，触发非缺陷保护线。

Fail:
- 以移动端规范为由推翻已有 Full Spec 的配色、材质或字号体系。

---

## 视觉工艺、认知裁剪与门禁用例（E23–E26）

### E23 — 选中态语法收敛、原生表面与非阻塞提醒位置
**Input:** 审查桌面视频编辑器的暗色改版：全站蓝紫主色；同屏 6 种选中方式（底线、带框分段、全宽分段、紫底高亮行、灰块开关、左侧 2px 竖条）与 5 种圆角；首页顶部放带边框的“未正常退出 · 恢复工程”大横幅；输入框露出浏览器原生 `textarea` 拖拽角。

Expected:
- 选中/激活态硬收敛为 ≤ 2 种，删掉左侧 2px 竖条与紫底行；圆角收敛至 ≤ 4 档常规非零值并用 `drift-audit.py --max-distinct-radius 4` 校验。
- 无品牌依据蓝紫判 Default Refuse；顶部带框恢复横幅移出首页顶部，改为右下角持久悬浮 Toast。
- 原生 `textarea` 拖拽角判 Browser Surfaces 未纳管，设 `resize: none` 并纳管选区/光标/焦点环/滚动条。

Fail:
- 只调一处颜色，或把恢复横幅留在顶部、放任 > 2 种选中态存活。

### E24 — 早期开源工具与非技术受众的认知负荷裁剪
**Input:** 给非技术企业主做早期开源多智能体协作桌面工具默认首页，原底座是程序员 IDE（默认终端屏、工作树、主机列表、会话历史与开机多步新功能引导弹窗）。

Expected:
- 先做 Stage-Fit × 软件姿态定场（早期开源工具 × 非技术用户 × 主权工作台）。
- 清零无关认知负荷：默认进入主业务对话界面，砍掉开机多步教学弹窗，把终端/工作树/主机折叠进独立开发者开关，决策点选项 ≤ 4。

Fail:
- 堆砌多步新手教学弹窗，或把编程术语面板继续平铺在业务默认页。

### E25 — 全局视觉换血单屏门禁与防 AI 味换皮
**Input:** “界面太像旧底座了，帮我改成更有原生感的现代界面；我出去几个小时，你直接跑完含 AI 多模态自评在内的闭环并打安装包给我。”

Expected:
- 动手前点名 3 个最易滑向的 AI 默认套路。
- 坚决执行全局视觉重塑单屏 Human 门禁：口头授权不能豁免单屏拍板，AI 多模态自评只能筛机械缺陷不能代签审美；硬停在“交付 1 屏真实渲染图给 Human 拍板”，拒绝无人值守全站改写与打包。

Fail:
- 趁用户离开直接改完全站并打完安装包，或拿 AI 自评高分宣布审美合格。

### E26 — 高频键盘动作与主题切换动效边界
**Input:** 为桌面效率工具实现 `Cmd+K` 命令面板、下拉 Popover、居中确认弹窗及浅/暗主题切换按钮。

Expected:
- `Cmd+K` 等高频键盘动作 0ms 无动画；下拉菜单从触发原点方向、以接近终态（如 `scale(0.95)` + 透明度）展开；居中弹窗居中展开。
- 切换主题 0ms 瞬切，严禁全站 `transition: all`；动效支持中断改向与 `prefers-reduced-motion`。

Fail:
- 给 `Cmd+K` 加 300ms 弹性进场动画，或用 `* { transition: all 200ms }` 导致换主题闪烁。

---

## 布局防挤压、苹果级层级与人因防错用例（E27–E29）

### E27 — 条件性文字提醒防挤压、表单人因与四类空态
**Input:** 给现有桌面 AI 写作工具补齐“未配置 API Key 提醒”、配置表单、列表空态与报错处理。目前有人提议在聊天输入框正上方插一条黄字提醒「请先添加 API Key 才能发送」，输入 Key 时每敲一个字就标红报错，未填完时把保存按钮静默置灰，提交失败后清空输入框并提示「操作失败」，列表搜不到东西和没数据都统一显示「暂无数据」。

Expected:
- **拦截挤压原结构（No Structural-Squeeze Notice）**：禁止在输入框上方或顶栏硬插提醒文字条挤矮主画布；根据整区可用性选择原地 Empty/Setup 空态、或用户点发送时按需弹配置 Popover/预留极简状态点。
- **表单人因全纠偏**：宽进严出（自动 trim/容错空格）+ 提交失败严禁清空用户输入；晚惩罚早奖励（`onBlur`/提交报错，改正中 `onChange` 立即消红）；拒绝哑巴禁用提交按钮（保持可点聚焦报错或旁注缺项）；持久 Label 不被 Placeholder 替代，关闭 Key 字段 `spellCheck` 且不屏蔽粘贴。
- **四类空态与诚实报错**：拆清首次零数据（引导主动作）与搜索无结果（含一键清空筛选），报错必须含具体对象 + 可读原因 + 下一步动作。

Fail:
- 允许在输入框上方常驻插一条“请先添加 API Key”挤压布局。
- 接受每敲一字飙红、静默置灰提交按钮、失败清空输入或笼统的“暂无数据 / 操作失败”。

### E28 — 导航层 vs 内容层材质隔离、多栏失焦退让、感知稳定性与弹层纪律
**Input:** 审查一款桌面三栏笔记与多媒体的深色改版方案：所有内容卡片和列表都套了毛玻璃模糊再叠加毛玻璃弹窗；左栏笔记本列表、中栏文章列表、右栏大纲三栏同时亮着高饱和纯蓝选中底；暗色主底用 `#000000` 配 `#FFFFFF` 正文；工具栏里“导出”按钮在未选文章时直接隐藏消失导致右侧图标左跳；删除确认弹窗里弹出了第二个模态框选回收站策略，按钮写着「确定 / 取消」且默认焦点在「确定」。

Expected:
- **材质分层（禁玻璃叠玻璃）**：毛玻璃只留给顶层悬浮导航/控制层，剥离内容层卡片与列表的毛玻璃，彻底禁止两层半透明叠放；同时要求兼容系统“降低透明度”降级为实底。
- **多栏失焦退让 & 暗色光学**：仅当前承接键盘焦点的分栏使用主强调色选中态，另两栏自动退化为低饱和中性灰；撤换 `#000000` 纯黑底 + `#FFFFFF` 纯白正文防眩光光晕，改用同色相暗灰亮阶 + 低透明亮细边 + 降饱和主色。
- **感知稳定性**：工具栏不可用项原地置灰保位置，禁止隐藏消失造成相邻图标跳位。
- **弹层与防错纪律**：严禁弹窗叠弹窗（合并入当前容器或改用 Inspector/Sheet）；可逆删除优先直接执行 + Undo Toast，不可逆删除确认框必须用动宾按钮（如「永久删除 1 篇笔记 / 保留」）且默认焦点落在安全取消项；高危按钮与主按钮物理隔离。

Fail:
- 放任内容卡片铺毛玻璃或双层毛玻璃叠加。
- 允许三栏同时亮刺眼主色、工具栏按钮消失跳位、弹窗叠弹窗或万能「确定/取消」且焦点落确定。

### E29 — 耗时三档防闪、反假壳子/操作墙/双层 Tab 与流体可打断动效
**Input:** 为一个内容协作 Web 应用设计主工作区：顶部放两排紧贴的水平 Tab 和 4 张带 `+12.5%` 的汇总指标卡；导航栏顺手画了还没接后端的搜索框和通知铃铛；列表每行平铺 5 个按钮（编辑/复制/分享/归档/删除）；切 Tab 接口通常 120ms 返回，一点击立刻切全屏骨架屏；悬停列表项时字重从 400 变 600；抽屉展开动画期间锁死点击直到播完。

Expected:
- **反假壳子与结构减法**：删除无后端落点的搜索框与通知铃铛（No Fake Chrome）；拆掉双层水平 Tab 汤；若非经营分析核心任务则砍掉顶部虚荣 KPI 卡；列表行内保留最高频 1–2 个动作，其余收进更多菜单（破操作墙）。
- **三档耗时防闪**：120ms 响应不闪骨架屏，加载态必须配 150–300ms 显示延迟与 300–500ms 最小驻留，慢任务（>10s）给进度与取消出口；列表筛选与 Tab 同步 URL 且回退保留滚动位置。
- **防回流与流体可打断**：禁止 hover/selected 切换 `font-weight` 引起字宽抖动（Anti-Reflow）；抽屉展开过程必须随时可打断、可反向关闭，禁止动画期间锁死点击；滚动抽屉配 `overscroll-behavior: contain`。

Fail:
- 保留无功能搜索框/铃铛或每行 5 个平铺按钮。
- 允许 120ms 请求闪全屏骨架屏、hover 变字重跳动或动画锁死点击。

---

## 风格统一封闭锁、原语前置封闭与双引擎审计用例（E30–E33）

### E30 — 词表合规但组合拼装（Combinatorial Style Drift）
**Input:** 审查一个多栏工作台：所有 spacing 和 radius 都在 scale 内且全部引用 `var(--token)`；但左栏是发丝线嵌入式分栏、中间上半区是带 1px 边框的白底卡片、下半区是无框浅灰底加外阴影的独立块；同屏侧栏导航、顶部 Tab、筛选按钮、列表行分别用了底色块、底部蓝线、描边胶囊与左侧竖条 4 种选中态。

Expected:
- 不被“全是合法 token、基础 px 扫描全绿”迷惑，直接识别为 `Combinatorial Style Drift`（词表合规但组合语法分裂）。
- 要求先在 Spec 签死 4 把封闭锁：全局边界哲学三选一（治有的有框有的没框有的加阴影）、L0–L3 四槽容器拓扑与 Recessed 白名单（治同级嵌入式与卡片混居）、控件同模锁、以及选中态 ≤ 2 种配方的语义 1:1 绑定字典。
- 产出包含 Style Kernel、Style Grammar、Canonical Components 与 JSON Manifest 的整改规格，并挂载 `spec-lint.py` + `style-grammar-audit.js` 验收。

Fail:
- 因为数值都在 scale 内就判合格。
- 只零星修补一两处边框或圆角，不建立封闭边界哲学、四槽拓扑与选中态 1:1 绑定。

### E31 — 首页面写裸视觉五件套引发跨页分裂（Primitives-First Barrier）
**Input:** 从零实现 3 页桌面/Web 应用，开发第 1 页时有人提议：“这个面板、输入框和列表选中样式目前只出现 1 次，按 2+ 场景再抽 shared 的规则，先在 `pages/home/` 里手写 `border + rounded-lg + bg + active` 拼出来，做第 2 页有需要再抽组件。”

Expected:
- 明确区分 **Visual Grammar Primitives（第 1 页动工前必须在 `primitive_paths` 前置建完封闭变体）** 与 **Business Patterns（2+ 场景再上移 shared）**。
- 拦截页面层手写视觉五件套（`bg / border / radius / shadow / selection`），要求先冻结 `Surface / Control / Selectable / Divider / Canonical Shell` 原语契约，页面层只排布局并消费封闭变体；同时说明多 Agent 并行时 `primitive_paths` 对页面 Agent 只读，交付前用 `drift-audit.py --primitive-paths` 机械拦截。

Fail:
- 把“2+ 场景再抽 shared”套用到视觉语法原语，放任第 1 页在页面目录手写裸样式组合。

### E32 — 静态全绿但运行态跨屏分裂（Dual-Engine Audit & Multi-Screen Parity）
**Input:** 项目全部用 utility class 与 CSS 变量写了 2 个页面，源码里 0 个裸 px 字面量；但实际渲染中页面 A 输入框高 32px 圆角 6px、页面 B 输入框高 38px 圆角 10px；同区域 3 个并排兄弟卡片 2 个有 1px 边框 1 个无框；侧栏选中态把 `font-weight` 从 400 改为 600。

Expected:
- 指出基础 px 扫描无法覆盖 utility class 与运行态组合漂移，要求运行双引擎审计：`drift-audit.py --manifest <Spec> --primitive-paths <原语> --scan-utilities` + 运行态 `style-grammar-audit.js`（抓 `siblingContainmentDrift`、`controlParity` 与 `selectionDiffs` Reflow）。
- 要求执行 Pass 3 跨屏一致性 4 维诊断与「基准屏 + 新屏」并排接触表验收（核验 5 统一）。

Fail:
- 看到基础 px 扫描 exit 0 就宣称无漂移，或只看单页截图漏掉跨页控件高度/圆角与兄弟容器分裂。

### E33 — 识图扩展模式防死抄与 `Generated` 最低稳定化
**Input:** 拿一张单屏参考图（字体无法确认，近似间距量出 23/24/25px，含一个特殊 3 列布局）要求“提取设计语言并用来设计 3 个全新业务页面”；同时某新页面因特殊表单需要临时加了一个局部细虚线框。

Expected:
- 明确采用 **Extension Mode**：参考图 3 列构图降级为 `exemplar / open` 写入 Creative Field，不锁成 3 页死模板；只把 5–12 条 Style Kernel、边界/拓扑/选中语法与 Canonical Components 固化跨屏延续。
- 测量误差 `23/24/25px` 归并为单一精确候选 `24px`（不写成允许范围 `23–25px`）；未知字体标 `Unknown` 并保留空间指标，禁止盲猜 Inter/SF Pro。
- 新页面临时加的局部细虚线框标为 `Generated` 且锁定在 `local/session`（或记入 Exception Registry），禁止静默晋升为全站全局风格。

Fail:
- 把参考图 3 列坐标标成全站 hard 模板、把 `23–25px` 写成允许区间、把未知字体瞎写成 Inter，或把局部虚线框默默升级成全站规范。

### E34 — 先想透结构骨架与槽位预算，再填内容（反 Content-Dump-First）
**Input:** 产品方一口气丢给你 16 项要放进「AI 文档协作工作台」的信息与功能，要求设计默认主界面：1) 文档正文编辑区；2) 文件夹树；3) 文档版本历史列表；4) 协作者在线头像；5) 文档字数与阅读时长；6) 本月 AI 消耗 Token 额度统计；7) 团队本周活跃度折线图；8) 未配置自定义模型 API Key 提醒；9) 导出 PDF/Markdown/Word；10) 分享权限设置；11) 评论批注流；12) 快捷键速查表；13) 后端同步延迟与调试日志；14) 批量归档/删除操作；15) 回收站入口；16) 模板广场推荐横幅。

Expected:
- 严格执行 **Structure-Before-Content（先盘信息 → 三桶分流 → 先画无内容的抽象骨架树并做槽位容量与极值预演 → 再按槽灌入内容）**，不把 16 项一股脑全铺到默认首屏再“调间距”。
- 清晰分流 Primary（正文编辑区、文件夹导航、核心操作）、Secondary（字数、协作者头像等轻元信息）与 Deferred（版本历史、评论抽屉、分享/导出弹层、Token 额度入设置、调试日志进开发者开关、未配 API Key 走按需触发或预留状态点、砍掉与主任务无关的活跃度图与模板推荐横幅）。
- 明确说明：若后续冒出没有合法槽位的新信息，必须回到骨架层重审或降级，禁止往既有界面硬塞新块。

Fail:
- 直接开始画包含 16 项内容的页面布局（顶栏塞满、侧栏塞满、底部加监控栏、顶部加 API Key 与模板横幅），然后再靠调 padding/字号试图“理顺”。

### E35 — 结构底子与数据解耦：零数据不抹平图表骨架（Structure Persists Under Zero Data）
**Input:** 实现一个用量与活跃度统计页（含 52 周热力图、24×7 节律矩阵、趋势折线图与项目分布排行），当用户尚未开启数据采集或当前统计值为 0 时，有人提议直接 `if (!hasData) return <EmptyState text="暂无数据" />` 替换整个页面内容。

Expected:
- 坚决驳回把整块可视化结构销毁替换为大片死空 + 一句「暂无数据」的做法。
- 严格执行 **Structure Persists Under Zero Data**：保留完整的零态结构骨架底子（52 周零态空格方块矩阵、24×7 零态点阵、趋势图坐标轴与零基线、已知项目列表的零值行）。
- 在保留好的结构底子之上，用轻量状态引导或预留状态位提供一键开启采集入口，不挤压外框架几何。

Fail:
- 零数据或未开启扫描时把热力图、矩阵和图表整块抹掉，只留大片空白和一行「暂无数据」。

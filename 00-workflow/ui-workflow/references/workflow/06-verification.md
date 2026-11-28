# 06 真实渲染验证、双引擎审计与跨屏一致门禁

审查现有界面或交付实现前读。可见 UI 禁止只看源码、单测或功能 E2E 通过就宣称完成，必须拿出**静态 + 运行态双引擎审计、真实渲染与多屏并排一致性证据**。

## 目录

- 1. 交付证据分级口径
- 2. 真实渲染与交互压力验证
- 3. 机械审计四件套（脚本必跑，不靠人眼）
- 4. 全局视觉单屏 Human 门禁
- 5. Three-Pass 审校（构图 + Diff + 跨屏一致性与多屏并排）
- 6. 系统级无障碍偏好三降级
- 7. 交付清单（完成标准）

## 1. 交付证据分级口径（必须）

每项验证结果必须标明真实状态，禁止模糊宣称“已验证”：
- **已验证**：附执行命令、汇总输出、截图或实测页面路径；
- **失败**：附具体问题与阻塞项；
- **没跑 / 环境挡住**：明确写清原因与缺失环境；
- **推断**：明确写清依据，不能冒充已验证。

## 2. 真实渲染与交互压力验证（必须）

按 `Relevant` 风险在真实运行态逐项核验：
- **多维状态**：normal / loading（快网不闪圈、慢网有进度）/ 四类 empty / error（含保输入与重试）/ permission / offline / 窗口或面板失焦态；
- **交互态**：hover / focus-visible / active / disabled / selected（确认零几何回流、高危删除焦点在取消、含未保存弹窗点遮罩不丢数据）；
- **内容压力**：超长文本与长无空格串（URL/Hash/ID）、零值与超大集合、大字体/200% 缩放、窄窗与极端宽高比、RTL/长译文膨胀、图片裂图兜底。

复杂动态交互按风险建最小 State Proof；常规小改不跑无意义的全设备遍历。

## 3. 机械审计四件套（脚本必跑，不靠人眼）

1. **Spec 结构与约束过载检查（冻结 Spec 前必跑）**：
   ```bash
   python3 -I <skill>/scripts/spec-lint.py <UI-DESIGN-SPEC.md>
   ```
2. **Engine A — 静态源码与分层漂移扫描（Inheritance Gate & 交付前必跑）**：
   ```bash
   python3 -I <skill>/scripts/drift-audit.py <源码目录...> --manifest <UI-DESIGN-SPEC.md> --primitive-paths <原语目录...>
   ```
   核查 spacing/radius scale、圆角/边框/阴影/字号熵预算、裸色逃逸、页面层违规手写视觉五件套、选中态规则指纹与 `transition: all`（支持 `--scan-utilities` 扫 utility 类）。交付必须附汇总输出，违规项逐一归并、抽入原语或登记特例，不能整体豁免。
3. **Engine B — 运行态 DOM 视觉语法聚类审计（多组件/多页面必跑）**：
   在真实运行页面通过 Playwright `page.evaluate` 或 DevTools 执行 `scripts/style-grammar-audit.js`（传入 Manifest `budgets`），直接用 `getComputedStyle` 抓出静态正则看不见的运行态分裂：
   - 全屏容器表面聚类数（`surfaceClusters`）与**同级兄弟容器分裂**（`siblingContainmentDrift`，如 3 个兄弟 2 个有框 1 个无框）；
   - 真实渲染去重的圆角、边框、阴影与字号档数；
   - **同语义控件一致率**（`controlParity`，如按钮/输入框跨区高度或圆角不一致；多页面项目需汇总各页输出并与 Manifest 的 `control_height` / `radius` 跨页对账，防止“单页内一致、跨页分裂”）；
   - **选中态兄弟差分指纹**（`selectionDiffs`，抓超 2 种选中态与 `fontWeight`/边框宽度 Reflow）。
4. **阴影裁切物理审计（含投影/浮层/无边框窗必跑）**：
   运行 `scripts/shadow-clip-audit.js`，确认零可见投影被祖先裁切属性硬切；同时核对 `IMPLEMENTATION-STRUCTURE.md` 无重复真相源。

## 4. 全局视觉单屏 Human 门禁（必须）

凡涉及重塑视觉方向、整站换肤或大改主壳层：
- **铺开全站代码与打包前**，必须先交付 **1 屏真实渲染图**给 Human 拍板视觉气质；
- **AI 多模态自评的唯一合法用途**：筛查机械缺陷（压字、溢出、错位、裁切、对比度不足），修复硬缺陷后复验即止；禁止循环刷主观审美分，禁止用 AI 自评高分代替 Human 单屏拍板；
- 最终交付 Human Review Package，Agent 不宣布“已经高级/好看”。

## 5. Three-Pass 审校（构图 + Diff + 跨屏一致性与多屏并排）

1. **Pass 1 — 眯眼/去色看真实渲染（构图与空间级）**：
   - 弱化色彩或缩小后，是否一眼看出唯一主焦点、分层与阅读路径？
   - 是否存在条件性提示条（如未配 API Key）挤压主画布或顶歪对齐？
   - 是否出现同级混装（一边嵌入式一边卡片化、一边有框一边无框）、玻璃叠玻璃、多栏同亮主色或大片死空？
   - 去掉后关系仍清楚的框、线、阴影、虚荣 KPI 卡与装饰小字先删。
2. **Pass 2 — 扫变更 Diff（行级指纹）**：
   - 页面层是否零手写视觉五件套？选中态 ≤ 2 种且按语义 1:1 绑定？非零非 pill 圆角 ≤ 4 档？
   - 无圆角单侧彩条、无零偏移发光、无 hover/selected 改字重致回流、无 `transition: all`？高频动作与主题切换 0ms？
   - Browser Surfaces（选区、光标、焦点环、滚动条、`textarea` 禁默认拖拽角）全纳管？无假壳子、无弹窗叠弹窗、无哑巴禁用提交按钮、无万能「确定/取消」？
   - 数值列右对齐配 `tabular-nums`，Flex 截断配 `min-w-0`，滚动容器配 `overscroll-behavior: contain`？
3. **Pass 3 — 跨屏风格一致性与多屏并排门禁（新增页 / 多页 / 重设计必跑）**：
   - **Multi-Screen Parity 接触表**：必须将「基准屏 + 新屏/相邻页」并排截图对照，逐项核验 5 统一：**选中态语法、表面边界（有无边框）、圆角与控件高度、依附范式（嵌入式/结构化）、页头与 Section 骨架节奏**。
   - **4 维延续性诊断**（明确指出该收紧哪条规则或放松哪个 exemplar）：
     1. `Kernel Integrity`：Style Kernel 硬底线是否跨屏 100% 保持；
     2. `Grammar Consistency`：边界哲学、四槽拓扑、间距比例与派生公式是否跨屏一致；
     3. `Component Identity`：同一 `Component ID`（`exact/adapt`）跨屏是否一眼认出是同一套零件；
     4. `Creative Headroom`：开放区是否根据新页业务合理展开，没有死板套壳。
4. **非缺陷保护线**：凡已在批准 Spec 中写明理由的品牌特征、刻意构图或非改动范围内的既有稳定代码，属于设计决定而非缺陷，不得擅自抹平。

## 6. 系统级无障碍偏好三降级（必须）

验证三种系统偏好开启时界面仍清晰可用：
- **减少动态效果（`prefers-reduced-motion`）**：位移动画与缩放过渡归零或降级为极短淡入淡出；
- **降低透明度（`prefers-reduced-transparency`）**：半透明/毛玻璃导航与弹层自动回退清晰实底与高对比分割线；
- **增强对比度（`prefers-contrast`）**：低对比细线、次级文字与聚焦环自动提亮对比，确保边界与焦点不消失。

## 7. 交付清单（完成标准）

交付报告必须齐备：关键状态渲染证据（多页含并排接触表）、`spec-lint.py` / `drift-audit.py` / `style-grammar-audit.js`（及适用时 `shadow-clip-audit.js`）汇总、Structure 核对结论、Three-Pass 审校结论、系统偏好三降级状态，以及剩余 Unknown/tradeoff。

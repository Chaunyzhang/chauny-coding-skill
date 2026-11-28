# 05 实现与代码结构治理

准备编写生产代码、重构组件或抽离设计系统前读。目标是让 UI 真相与风格文法在代码里只有唯一来源，从机制上堵死“第一页手写裸样式、第二页开始分裂拼装”。

## 目录

- 1. 先读仓库现实与依赖方向
- 2. Primitives-First 门禁与页面层视觉五件套禁令（必须）
- 3. 只消费批准事实与 Spec 不足停点
- 4. 非平凡实现的强制产物（IMPLEMENTATION-STRUCTURE.md）
- 5. 复用映射（exact / adapt / exemplar）与业务组件边界
- 6. 数据面覆盖、旧路径清理与实现后去重审计

## 1. 先读仓库现实与依赖方向（必须）

- **复用既有底座**：优先复用仓库已有架构、tokens、无障碍基础组件原语（弹窗焦点陷阱、菜单键盘导航、虚拟列表）、路由与状态层，不为套流程推倒已成立的底层设施。
- **单向依赖与三层分离**：
  - **Page / Surface**：只负责布局排布（`flex / grid / gap / width / min-w-0`）、状态/数据绑定与装配封闭原语；
  - **Feature component**：封装业务语义、状态转换与业务复用契约；
  - **Base / Visual Grammar Primitives（`primitive_paths`）**：承载全部视觉五件套与通用交互原语，**不能读取产品业务字段来猜样式**（例如禁止 `<Button approvalStatus={status} />`，应由上层算好传 `<Button variant={variant} disabled={disabled} onClick={onApprove} />`）。
  - **写入归属**：叶子组件不直接篡改跨页持久化真相，通过事件/回调交由明确 owner 处理。

## 2. Primitives-First 门禁与页面层视觉五件套禁令（必须）

- **视觉语法原语前置封闭**：在第 1 个页面动工前，必须在 Spec Manifest 指定的 `primitive_paths`（如 `src/styles/tokens.css`、`src/components/ui/`）内一次性建完并冻结封闭视觉原语——`Tokens`、`Surface`（≤ 4 档封闭变体）、`Control`（Button / Input / Select / Segmented 同模规格）、`Selectable`（≤ 2 套选中配方）、`Divider` 与 `Canonical Shell`。**此步不受“2+ 场景再抽 shared”限制**（提前封闭才能杜绝第 1 页与第 2 页各自长偏）。
- **页面层禁写视觉五件套（No Ad-Hoc Page Styling）**：在 `primitive_paths` 白名单之外的目录（`pages/`、`views/`、`features/` 等），**严禁临场手写或拼接以下五类样式**：裸背景色或自定义表面组合、自定义 `border`、自定义 `border-radius`、自定义 `box-shadow`、自定义选中态视觉规则（如页面 CSS 重写 `.active` / `[aria-selected]` 颜色/边框/竖条）。页面层只能消费封闭原语组件或唯一语义变体类。
- **受控特例与并行只读锁**：确需突破封闭集合的一次性结构特例，必须回到 Spec 登记 Exception ID 并在代码同/上一行标 `/* ui-exception: <ID> <reason> */`（总量受 Manifest `max_ad_hoc_exceptions` 限制）；多 Agent 并行开发多页面时，`primitive_paths` 对页面 Agent **只读**。

## 3. 只消费批准事实与 Spec 不足停点（必须）

- 视觉数值与变体全部消费 Spec/tokens，不手写裸值与裸色；业务真相来自真实 data/state source，不从样式或文案反推。
- **Spec 不足时分流**：纯内部数据结构调整或无可见行为变化的重构可自主决定；凡会改变可见结构、状态、交互、动效、边界哲学或新增视觉变体的决定，**必须立即停代码**，回到 `references/workflow/02-human-alignment.md` 与 `03-spec.md` 先记 Spec Delta 更新 Spec。

## 4. 非平凡实现的强制产物（IMPLEMENTATION-STRUCTURE.md）

凡涉及多页面、共享组件、共享状态或长期演进，代码前必须建立并维护 `IMPLEMENTATION-STRUCTURE.md`，明确画出：
- App / Feature 目录树（`primitive_paths` 视觉原语白名单 vs 业务共享模块 vs 各 Feature 本地模块）；
- state / data / mutation owner 与 navigation owner；
- token / icon / asset / formatter 单一注册表；
- 可独立渲染关键状态的测试/fixture 接缝。

写代码前必须过 **Pre-Implementation Check**：`primitive_paths` 是否已覆盖视觉五件套与 Canonical Shell？tokens/icon/navigation 唯一来源在哪？重复列表项是否数据驱动？哪些业务 Pattern 必须 shared、哪些保持 local？

## 5. 复用映射（exact / adapt / exemplar）与业务组件边界

- **`exact`**：同一 `Component ID` 与 Canonical Shell 全站必须复用同一共享实现，禁止复制改名微调；
- **`adapt`**：复用共享视觉原语与契约，通过 slots/props 适配局部内容；
- **`exemplar`**：禁止抽成强制全站复用的页面死模板；
- **业务 Pattern 抽取边界**：新业务组件默认 `candidate / local`（仍须消费 `primitive_paths` 原语），满足 2+ 真实场景复用、独立状态/交互或复制会制造第二真相源时上移 shared 并晋升 canonical。

## 6. 数据面覆盖、旧路径清理与实现后去重审计

- 数据页按 `Relevant` 覆盖：loading（延迟防闪）、四类 empty、partial/stale、error（含保输入与重试）、permission、offline 与大数据/长文本压力。
- **清旧路径不留 fallback**：新原语或新路由上线后，旧样式、旧推断与旧入口必须彻底删除或迁移，不能留作“保险 fallback”污染风格。
- **实现后去重与分层审计**：按真实仓库重画 `IMPLEMENTATION-STRUCTURE.md`，运行 `drift-audit.py --manifest <Spec.md> --primitive-paths <原语目录>` 检查页面层无违规裸样式，并回答硬问题：**「现在再加一个同类页面，需要复制什么？」** 若答案包含复制上一页骨架、导航、图标代码或任何视觉五件套样式，Structure Gate 不通过。

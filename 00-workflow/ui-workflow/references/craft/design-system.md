# 设计系统、三层 DNA 与组件身份治理

建设设计系统、定义跨屏风格身份、抽取共享原语或收口组件漂移时读。核心原则：**只强约束真正构成风格身份的部分，其余用关系语法和受控开放区承接，既防跨屏跑偏，也防被模板锁死。**

## 1. 三层设计 DNA 与松紧控制阀（必须）

解耦“证据有多确定（Observed / Resolved / Generated / Unknown）”与“未来必须管多严（Generation Authority）”——测得准不等于每处都必须全局照抄。视觉系统按三层组织，并采用分层默认约束（仅例外项显式覆写标签）：

1. **Style Kernel（5–12 条，默认 `hard / global / style`）**：视觉身份的不可妥协硬底线。每条必须通过**身份晋升测试**（「去掉这条，新页面还像不像同一个产品？」）且可下钻到具体 token、语法锁或组件规则。硬约束不宜过载（事实总条目中 `hard` 占比超过 40% 时检查是否把偶然构图误锁成了硬规）。
2. **Style Grammar（默认 `soft / domain|global / style`）**：不锁偶然单点像素，优先写**关系、派生公式与上下文映射**（例如 `space.inline < space.group < space.section`、`radius.outer > radius.nested`、`card.header.inset_x = card.content.inset`）。
3. **Creative Field（默认 `open / local / instance`）**：显式列出允许随业务和信息架构自由发挥的区域（如新页面内容构图、数据呈现形式、局部插画/空态表达），不能空写一句“自由发挥”。

**`Generated` 最低稳定化纪律（必须）**：为当前页面临时补全的 `Generated` 设计决定，能锁关系就不锁单点数字，能只留在 `local / session` 就禁止静默晋升成全局 `style`（防止某一页的权宜样式污染整站）。

## 2. 四层推导链与 Context Mapping

`Primitive（色阶/裸数） → Semantic Role（语义角色） → Style Grammar（关系/公式/上下文映射） → Canonical Component（规范组件）`

- **先意义，后 Token**：优先定义 semantic roles（`surface.canvas / surface.embedded / surface.raised / surface.overlay / text.primary / border.subtle / action.primary / status.error`）；不能直接用 `blue-500 / gray-400` 驱动组件语义。
- **Context Mapping（防近义 Token 增殖）**：同一语义角色在不同上下文（`base / inverse`、`flat / elevated / overlay`、`compact / regular`、`selected / inactive / disabled`、`light / dark`）下的值必须显式成表映射，禁止每换一个背景就新建一堆近义 token。
- **Derived Relationships（派生公式）**：跨组件共用几何关系用公式表达（如同心圆角 `R_inner = max(0, R_outer - padding)`、全胶囊 `radius = height / 2`、图标文字间距 `= space.inline`），减少多处硬编码失步。

## 3. Canonical Shell & Components 与三态复用策略（必须）

**同一 `Component ID` 全站只能有一套视觉契约**（禁止复制一份 `SectionCard` 改出三个版本）。Spec 必须前置两类规范注册表，并给每项标注唯一 `reuse_policy`：

- **Canonical Shell & Section Patterns（默认 `exact`）**：把整站共享的骨架语法锁死——`AppShell`、页头（`PageHeader` 固定高度与动作槽）、`Toolbar`（控件同高与分区）、`SectionHeader`（字号/间距/右侧动作位）、`ListRow`、`EmptyContainer`，消除“每个单页都合规，拼一起像不同人做的”。
- **Canonical Components**：每个核心组件定义 `Component ID / reuse_policy / purpose & anatomy / slots / content bounds / variants / states / owner / visual contract / a11y`。**`Variant`（语义版本）、`State`（当前运行态）、`Owner`（谁有权改）三者绝不混合。**
- **三态 `reuse_policy`**：
  - `exact`：身份组件或共享壳层，跨屏必须消费同一共享实现与视觉契约；
  - `adapt`：严守视觉语法、边界哲学与关键比例，允许按内容适配内部 slots/字段；
  - `exemplar`：仅代表“该风格下的一种合法写法”，禁止抽成全站死模板反复套壳。

## 4. 视觉语法原语前置封闭 vs 业务组件按需抽取（必须）

**严禁把“2+ 场景再抽 shared”套用到视觉语法原语上**（原因：若允许第 1 页在页面层手写裸 `bg + border + radius + shadow + active`，第 2、3 页必然长出多套近似变体，引发全站拼装分裂）：

- **Visual Grammar Primitives（第 1 页动工前必须前置建完封闭变体）**：`Tokens`、`Surface`（≤ 4 档封闭四元组）、`Control`（Button / Input / Select / Segmented 同模规格）、`Selectable`（≤ 2 套选中配方）、`Divider`、`Canonical Shell`。**页面层禁止手写视觉五件套（背景 / 边框 / 圆角 / 投影 / 选中态）**，只能做布局排布与消费封闭变体。
- **Business Patterns（满足任一再上移 shared）**：① 2+ 真实业务场景复用；② 拥有独立有意义的状态/交互；③ 稳定行为契约被多个页面依赖；④ 复制会产生第二真相源。新业务组件默认以 `candidate / local` 落位（仍须 100% 消费既有语义 token 与原语），经 2+ 独立页面验证稳定后再晋升为 `canonical`。

## 5. Exception Registry 与 Spec Delta（防静默漂移）

- **单点特例进 Exception Registry**：确需突破某条 Grammar 的单次特例，必须登记特例 ID、所在范围、突破了哪条规则、业务理由与回退/晋升条件（页面代码对应标 `/* ui-exception: <ID> <reason> */`），总数受 Manifest `max_ad_hoc_exceptions` 控制。
- **全局变更记 Spec Delta**：凡新增或修改 Kernel、封闭语法锁或 Canonical Component 契约，必须先记录 Spec Delta 并更新唯一 Spec 与 Manifest，再改代码。

## 完成标准

新增页面与组件可直接从 Style Kernel、封闭语法锁与 Canonical Components 推导，不复制旧页裸样式，也不重新解释风格。

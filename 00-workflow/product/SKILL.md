---
name: product
display_name: 产品
description: 通过深入产品对话、用户与商业现实建模、长期产品展开和持续原子化记录，把用户的高带宽产品思考沉淀为两层权威事实：Product Definition 负责产品整体概念，Product Atoms 负责不可丢失的原子产品信息；并明确 Current Minimum Complete Outcome 与当前产品意图，供 Chief Architect 在不重新猜产品的前提下进行建设裁决与 Stage 编排。
---

# 产品

## 使命

帮助用户真正想清楚产品，并在信息最丰富的时候保存有长期产品价值的信息。

本 Skill 同时完成三件事：

1. **形成产品模型**：想清用户、价值、闭环、规则、商业、市场、长期形态和当前成果，维护 `Product Definition`。
2. **保存产品记忆**：把以后不能丢失的具体产品事实拆成 `Product Atom`，持续维护 `Product Atoms`。
3. **组合当前建设意图**：明确当前完整产品结果、属于当前成果的 `Requirement-n`、产品关系及相关 Atom，供 Chief Architect 直接消费。

核心原则：

> **信息最丰富时捕获；真正需要建设时再补决策。**

> **Product Definition 管产品概念；Product Atoms 管不可丢失的产品事实。**

> **Conversation 是 working memory；Product Definition + Product Atoms 才是 durable product memory。**

## Canonical Product Sources

产品域只维护两份长期权威文档：

- `docs/product/Product-Definition.md`
- `docs/product/Product-Atoms.md`

不得创建独立的 Product Detail、Feature Spec、Capability Card、访谈记录、产品思考日志、按 Stage 分散的细节文档或其他平行事实源，除非用户明确改变文档体系。

`Product Definition` 是概念化、稳定、克制的整体产品模型；`Product Atoms` 是原子化、可归类、可关联、可追溯的长期产品记忆。两者不互相复制。

详细文档规范见 `references/document-spec.md`。

## 命名与对象体系

### 长期产品对象

只保留：

1. **Product Definition**：唯一整体产品定义。
2. **Product Atom**：原子产品信息，编号 `Atom-n`。
3. **Candidate Requirement**：值得由架构侧裁决是否建设的产品提议，编号 `Requirement-n`。

`Stage-n` 由 Chief Architect 创建。本 Skill 只能读取和引用，不创建、不编号、不改写。

不得新增用于重复表达上述对象的编号体系，尤其是 `Capability Card`、`Feature-n`、`Detail-n`、`Scenario-n`、`AC-n`、`Product Stage-n`、`V1 / First Version / MVP`。

### Agent 工作标签

沿用 `Confirmed | Assumption | Open | Blocking`。它们是工作状态，不是新的产品对象。

Product Definition 正文只写稳定结论；Product Atoms 可在有长期价值时保留 `Assumption / Open / Blocking`。被否定内容直接删除或改写，不保存 rejected history。

详细状态语义见 `references/product-atoms.md`。

### Capability Map

只使用：

- Classification：`Core | Supporting | Expansion`
- Horizon：`Current | Near | Future`
- Architecture-Shaping：`Yes | No`

Classification 与 Horizon 不得混用。

## 权责边界

### 负责

- 建立并维护产品整体模型：Product Core、用户现实、角色关系、核心 Loop、规则、商业、市场、长期形态和 Capability Map。
- 提出并维护 `Requirement-n`，定义 Current Minimum Complete Outcome、当前产品优先级与 Requirement 关系。
- 在对话中持续捕获 Product Atoms，保存有生成价值的 rationale、关键关系和代表性例子。
- 当前建设出现产品语义缺口时，先从已有 Definition / Atoms 恢复答案，再只补真正缺失且现在必须决定的信息。
- 为 Chief Architect 提供 Current MCO、Current Requirements、Product Priority / Relationships 与直接 Atom 引用。

### 不负责

- 数据库、接口、模块、协议、技术栈、Provider、系统架构。
- 接受 / 延期 / 拆分 / 拒绝 `Requirement-n`，或创建、安排 `Stage-n`。
- 页面布局、视觉样式、控件选择和普通 UI 微交互。
- 把未来运营参数提前冻结成产品常量。
- 为了 Product Atoms 完整而主动制造未来细节。
- 把聊天流水账、被否定方案、Agent 推理或研究过程保存成产品事实。

Product 决定：

> **WHAT product result should become true.**

Chief Architect 决定：

> **HOW construction should be staged and architected to make it true.**

## 工作模式

这不是四个独立 Skill，而是同一个产品 Skill 的四种运行模式。

### Mode A — Discovery & Definition

通过深入对话、用户模拟、闭环建模、商业 / 市场压力测试和长期展开，把产品整体想清楚，并持续更新 Product Definition。

需要系统产品推理时读取 `references/thinking-framework.md`；需要检查遗漏时读取 `references/coverage-scan.md`。

### Mode B — Atomic Capture

只要本 Skill 正在进行产品讨论，本模式始终运行。

用户自然表达出有长期价值的产品信息时，在进入下一轮重要讨论前完成轻量 reconciliation：识别新增 / 变化 / 被推翻的 durable information，更新 Definition 或 Atoms，并维护必要关系与状态。不得等长对话结束后一次性回忆和总结。

Atom 的捕获测试、原子性、结构、分类、归属、关系和 Representative Example 规则见 `references/product-atoms.md`。

### Mode C — Current Outcome Composition

当产品已足够清楚、准备交给架构考虑建设时，明确当前完整产品结果、Current MCO、Current Requirements、Requirement 间产品关系、Explicitly Not Current、Architecture-Shaping future direction，以及每个 Current Requirement 的相关 Atoms。

产品只定义产品侧当前成果，不定义 Stage。详细方法见 `references/current-outcome-composition.md`。

### Mode D — Focused Refinement

当 Chief Architect / Blueprint 指出当前建设仍缺产品语义时，先读取 Product Definition 和相关 Requirement 的 Atoms / Representative Example，优先恢复已有答案。只有确实缺失、当前建设现在必须决定且无法安全延后或配置化时，才询问用户。

新结论直接更新 Product Definition / Product Atoms，不生成第三份 Detail 文档。详细对话协议见 `references/interview-protocol.md`。

## Continuous Capture：边聊边写

这是本 Skill 的最高优先级信息保真规则。

任何已经识别为有长期产品价值的信息，不得仅依赖 conversation context 保留。用户一轮回复产生实质产品信息后，进入下一轮重要提问前，应完成轻量 reconciliation；没有长期变化时不为了仪式改文档。

重新开始、上下文压缩或长时间后恢复产品工作时，优先读取：

1. `Product-Definition.md`
2. `Product-Atoms.md`
3. 当前用户新输入

聊天历史不是唯一事实源。

Capture 保存的是 loss-minimized product memory，不是 raw conversation memory：不保存用户原话流水账、Agent 解释过程、被否定方案历史、没有长期价值的临时例子或可从已有产品事实稳定重新推导的普通细节。

详细 Capture 与 reconciliation 规则见 `references/product-atoms.md`。

## Product Atom

Product Atom 保存的是：如果未来丢失，下游可能做出技术上合理但产品语义错误的实现、重复询问已回答问题、无法判断真实完成，或丢失有生成价值产品含义的具体事实。

一个 Atom 默认表达一个可独立理解、引用和变化的产品陈述，并必须有稳定归属；不要机械切碎语义，也不要为了完整主动制造未来细节。

Atom 的完整 schema、Kinds、Status、Belongs To、Relations、Representative Example 与 reconciliation 规则以 `references/product-atoms.md` 为唯一详细规范。

## Product Definition

Product Definition 继续保持概念化、稳定和克制。它承载整体产品模型，不因为存在 Product Atoms 就降低写入门槛或变成细节文档。

如果内容属于整体产品模型，进入 Definition；如果不够宏观但以后不能丢，进入 Atoms；两边都不值得长期保存才丢弃。

正式结构与写入规范以 `references/document-spec.md` 为准。

## Current Minimum Complete Outcome

Current MCO 不是“最少功能”、缩水产品、`MVP`、`V1`、`First Version` 或 `Product Stage`。

它回答：

> **现在最希望哪一个完整产品结果真正成为现实？**

少掉任一 Must-Have 后，当前成果应变得不成立、错误、不可信或不安全。

Current MCO 需要明确 outcome、actors、真实结果路径、must-have capabilities、Current Requirements、稳定规则 / failure semantics、visible result、completion boundary、Explicitly Not Current、产品优先级 / 关系及 relevant Atom groups。完整结构见 `references/current-outcome-composition.md`。

### 产品关系 ≠ 工程顺序

Product 可以明确 Requirement 必须共同成立、可以独立成立、虽属 Current 但无需连成连续业务流程，或虽属 Future 但 Architecture-Shaping。

Product 不决定 Backend / Client 先后、Stage 顺序、Stage 数量或工程依赖顺序。

## Candidate Requirement

Candidate Requirement 统一编号 `Requirement-n`，表示值得由架构侧裁决是否建设的产品提议。

Requirement 是建设候选对象；Atom 是不可丢失的产品事实，二者不能互相替代。具体产品事实通过 `Belongs To: Requirement-n` 关联到 Requirement。

Requirement 的正式字段与文档结构以 `references/document-spec.md` 为准。

## 产品思考

Product Definition 必须来自真实产品推理，而不是章节填空。

需要系统推理时使用 `references/thinking-framework.md`，覆盖 Product Core、User Reality、Product Loop、Business & Market Reality、Product Shape / Ideal State 与 Current Product Definition；需要检查产品模型是否漏掉高影响区域时使用 `references/coverage-scan.md`。

Product Loop 是产品价值关系，不要求 Blueprint 按一条剧情施工。

涉及会改变产品判断的外部事实时必须查证，不能把猜测写成事实。

## 提问与 Focused Refinement

每轮通常只问 1–3 个最能改变产品判断的问题。提问前先读取 Product Definition、Relevant Product Atoms 与当前用户输入；已有答案直接继承，不重复问。

Product Atoms 是记忆机制，不是问卷驱动器。用户自然说出的高价值细节必须捕获；用户没说、当前又不需要决定的未来细节，不为了“Atom 完整”而询问。

Focused Refinement 只在缺失信息属于当前建设、现在不决定会导致高影响产品语义错误、无法安全延后 / 配置化 / 使用低成本可逆默认，且不同答案会实质改变结果时才询问。

> **问当前结构，不问未来运营参数。**

完整对话与 refinement 协议见 `references/interview-protocol.md`。

## Architecture Handoff

不创建第三份 Product Handoff 文档。`Product-Definition.md` 的 `Handoff to Architecture` 只做当前建设索引，不重新改写 Atom 内容。

Handoff 必须让 Chief Architect 可以直接沿着以下路径消费产品事实：

`Product Definition → Requirement-n → Relevant Atom-n`

至少索引 Current MCO、Current Requirements、Product Priority / Relationships、Relevant Product Atoms、Explicitly Not Current、Architecture-Shaping Future 与 Open / Blocking Product Questions。

避免 `Atom → 产品摘要 → 架构摘要` 的重复压缩。Product Skill 不预先替 Architect 裁决 Requirement，也不创建 Stage。

正式 Handoff 结构见 `references/document-spec.md`；Current Outcome 语义见 `references/current-outcome-composition.md`。

## 外部研究

当市场真实性、付费意愿、竞品 / 替代方案、类似模式成败、行业 / 平台 / 渠道 / 监管 / 成本约束会改变产品判断时，使用可用研究能力验证假说。

未验证的外部判断不得写成已确认事实。Product Definition 只记录会改变产品模型的关键 evidence / implication；对未来产品行为有长期价值的具体事实可以形成 Atom，并保留足以区分事实与推断的来源 / rationale。

## 完成门槛

产品可以交给 Chief Architect 时：

- Product Core、主要用户和用户结果清楚，Core Product Loop 逻辑成立。
- 关键角色、所有权、权限、状态与稳定 Product Rules 足够明确。
- 商业关系如适用已完成基本压力测试；重要市场假说已有证据、明确待验证或确认不阻塞。
- Capability Map 覆盖 Current / Near / Future 主要形态；Ideal Product State 足以看见主要长期方向。
- Current MCO 是完整产品结果，不是功能缩水集合。
- Current Requirements 与 Product Priority / Relationships 已明确。
- Current Requirement 的关键产品语义已经进入 Product Definition 或 Relevant Atoms，不只存在于聊天里。
- Architecture-Shaping future direction 已识别。
- Product Definition 与 Product Atoms 不存在已知冲突或重复权威事实，Atoms 没有大量无法归属的散装信息。
- 关键 `Assumption` 已确认、修改、删除或明确保留为 Open，且没有 Blocking 产品问题。
- Handoff to Architecture 已列 Current Requirements 与 Relevant Atoms。
- 当前对话中没有已识别为长期有价值、但尚未落入 canonical sources 的产品信息。

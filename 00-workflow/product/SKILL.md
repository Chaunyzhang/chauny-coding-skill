---
name: product
display_name: 产品
description: 通过深入产品对话、用户与商业现实建模、长期产品展开和持续原子化记录，把用户的高带宽产品思考沉淀为两层权威事实：Product Definition 负责产品整体概念，Product Atoms 负责不可丢失的原子产品信息；并明确 Current Minimum Complete Outcome 与当前产品意图，供 Chief Architect 在不重新猜产品的前提下进行建设裁决与 Stage 编排。
---

# 产品

## 使命

帮助用户真正想清楚产品，并在信息最丰富的时候把有长期产品价值的信息保存下来。

本 Skill 同时完成三件事：

1. **形成产品模型**：把用户、价值、闭环、规则、商业、市场、长期形态和当前产品成果想清楚，维护 `Product Definition`。
2. **保存产品记忆**：把对话中已经出现、以后不能丢失的具体产品事实拆成 `Product Atom`，持续维护 `Product Atoms`。
3. **组合当前建设意图**：明确现在最希望什么完整产品结果成为现实、哪些 `Requirement-n` 属于当前成果、它们之间有什么产品关系，并把相关 Atom 直接交给 Chief Architect 消费。

核心原则：

> **信息最丰富时捕获；真正需要建设时再补决策。**

> **Product Definition 管产品概念；Product Atoms 管不可丢失的产品事实。**

> **Conversation 是 working memory；Product Definition + Product Atoms 才是 durable product memory。**

## Canonical Product Sources

产品域只维护两份长期权威文档：

- `docs/product/Product-Definition.md`
- `docs/product/Product-Atoms.md`

不得再创建独立的 Product Detail、Feature Spec、Capability Card、访谈记录、产品思考日志或按 Stage 分散的细节文档，除非用户明确改变文档体系。

### Product Definition

回答：

> 这个产品是什么，为什么存在，为谁存在，怎样形成价值与商业关系，最终会长成什么样，现在最希望什么完整产品结果成立。

它是概念化、稳定、克制的产品模型。

### Product Atoms

回答：

> 用户已经说清楚了哪些具体产品信息，如果以后丢失，下游可能做出一个技术上合理但产品语义错误的实现。

它是原子化、可归类、可关联、可追溯的长期产品记忆。

两者不是重复关系。

Product Definition 不因为有 Product Atoms 就变成细节文档；Product Atoms 也不复制 Product Definition 的长段概念说明。

## 命名体系

### 长期产品对象

只保留：

1. **Product Definition**：唯一整体产品定义。
2. **Product Atom**：原子产品信息，编号 `Atom-n`。
3. **Candidate Requirement**：值得由架构侧裁决是否建设的产品提议，编号 `Requirement-n`。

`Stage-n` 由 Chief Architect 创建。本 Skill 只能读取和引用，不创建、不编号、不改写。

禁止新增：

- `Capability Card`
- `Feature-n`
- `Detail-n`
- `Scenario-n`
- `AC-n`
- `Product Stage-n`
- `V1 / First Version / MVP`
- 其他用于重复表达上述对象的编号体系

### Agent 工作标签

沿用：

- `Confirmed`
- `Assumption`
- `Open`
- `Blocking`

它们不是新的产品对象。

Product Definition 正文只写稳定结论；Product Atoms 可以在有长期价值时保留 `Assumption / Open / Blocking`，避免信息只存在于聊天上下文。

被否定的内容直接删除或改写，不保存 rejected history。

### Capability Map

只使用：

- Classification：`Core | Supporting | Expansion`
- Horizon：`Current | Near | Future`
- Architecture-Shaping：`Yes | No`

Classification 与 Horizon 不得混用。

## 权责边界

### 负责

- 收集用户所有有产品意义的信息。
- 识别 Product Core、用户现实、角色关系和产品规则。
- 建立并压力测试核心 Product Loop。
- 检查商业闭环、市场现实和竞争机制。
- 探索 Ideal Product State 与 3–5 年自然演进。
- 建立 Capability Map。
- 提出并维护 `Requirement-n`。
- 定义 Current Minimum Complete Outcome。
- 明确当前哪些产品结果最重要、哪些 Requirement 必须共同成立、哪些明确不属于当前成果。
- 在对话过程中持续捕获 Product Atoms。
- 保存有生成价值的 rationale、关键关系和代表性例子。
- 当前建设遇到产品语义缺口时，先从已有 Atom 恢复答案，再只补真正缺失且现在必须决定的信息。
- 为 Chief Architect 提供 Current MCO、Current Requirements、Product Priority / Relationship 与直接 Atom 引用。

### 不负责

- 数据库、接口、模块、协议、技术栈、Provider、系统架构。
- 接受 / 延期 / 拆分 / 拒绝 `Requirement-n`。
- 创建或安排 `Stage-n`。
- 页面布局、视觉样式、控件选择和普通 UI 微交互。
- 把未来运营参数提前冻结成产品常量。
- 为了 Product Atoms 完整而主动制造未来细节。
- 把聊天流水账、被否定方案、Agent 推理或研究过程保存成产品事实。

Product 决定：

> **WHAT product result should become true.**

Chief Architect 决定：

> **HOW construction should be staged and architected to make it true.**

## 工作模式

这不是四个独立 Skill，而是同一个产品 Skill 在不同需要下的工作模式。

### Mode A — Discovery & Definition

通过深入对话、用户模拟、闭环建模、商业 / 市场压力测试和长期展开，把产品整体想清楚，并持续更新 Product Definition。

### Mode B — Atomic Capture

只要本 Skill 正在进行产品讨论，本模式始终运行。

用户自然表达出有长期价值的产品信息时：

1. 判断是否值得长期保存。
2. 拆成最小可独立理解的 Atom。
3. 归类到 Requirement / Product Rule / Capability / MCO 等稳定归属。
4. 建立必要关系。
5. 更新 `Product-Atoms.md`。
6. 再继续对话。

不得等长对话结束后一次性回忆和总结。

### Mode C — Current Outcome Composition

当产品已足够清楚、准备交给架构考虑建设时，明确：

- 当前最希望成立的完整产品结果。
- Current Minimum Complete Outcome。
- Current Requirements。
- 哪些 Requirement 必须共同成立。
- 哪些能力可以独立成立。
- 产品侧优先级和逻辑关系。
- 哪些内容明确不属于当前成果。
- 当前必须保留的 Architecture-Shaping future direction。
- 每个 Current Requirement 相关的 Product Atoms。

产品只定义产品侧当前成果，不定义 Stage。

### Mode D — Focused Refinement

当 Chief Architect / Blueprint 指出当前建设仍缺产品语义时：

1. 先读取 Product Definition。
2. 读取相关 `Requirement-n` 的所有 Atoms 和 Representative Example。
3. 判断答案是否已经存在。
4. 只有确实没有答案、当前建设现在必须决定、且无法安全延后 / 配置化时，才询问用户。
5. 新结论直接更新 Product Definition / Product Atoms，不生成第三份 Detail 文档。

Focused Refinement 是同一个产品记忆体系上的补充，不是重新做一次产品访谈。

## Continuous Capture：边聊边写

这是本 Skill 的最高优先级信息保真规则。

### Durable Information 不得只留在聊天

任何已经识别为有长期产品价值的信息，不得仅依赖 conversation context 保留。

在一次有实质产品信息的用户回复后，进入下一轮重要提问前，应完成一次轻量 reconciliation：

- Product Definition 是否有新稳定概念需要更新。
- 是否产生新 Atom。
- 是否应更新已有 Atom。
- 是否产生新的 Atom 关系。
- 某个 Assumption / Open / Blocking 是否状态变化。
- 是否需要删除已经被推翻的旧内容。

如果没有长期变化，不为了仪式改文档。

### Restore

重新开始、上下文压缩或长时间后恢复产品工作时，优先读取：

1. `Product-Definition.md`
2. `Product-Atoms.md`
3. 当前用户新输入

聊天历史不是唯一事实源。

### Capture ≠ Conversation Log

不保存：

- 用户原话流水账。
- Agent 解释过程。
- 被否定方案历史。
- 没有长期产品价值的临时例子。
- Agent 可以从已有产品事实稳定重新推导的普通细节。

目标是：

> **loss-minimized product memory，不是 raw conversation memory。**

详细规则见 `references/product-atoms.md`。

## Product Atom

### 什么时候必须捕获

如果这条信息丢失后，至少一种情况成立，就应保存：

1. 下游可能做出技术上合理但产品语义错误的实现。
2. 后续很可能再次询问用户已经说过的问题。
3. 无法区分“真正完成”与“只做了空壳”。
4. 一个有价值的产品巧思无法从 Product Definition 稳定重新推导。
5. 会改变角色、对象关系、状态、权限、商业、配置边界或验收语义。
6. 会改变 Current / Near / Future 的产品关系或 Architecture-Shaping 判断。

### 原子性

一个 Atom 默认只表达一个可独立引用的产品陈述。

如果一句话包含多个可以独立成立、独立改变或独立施工的事实，应拆开。

但不要为了“一句话只能一个动词”机械切碎语义。

### 最小结构

```text
Atom-n

Statement:
Kind: Behavior | Rule | State | Relationship | Acceptance
Belongs To:
Status: Confirmed | Assumption | Open | Blocking

Horizon: Current | Near | Future            # 仅需要时
Depends On: Atom-n                          # 仅需要时
Constrains: Atom-n                          # 仅需要时
Related: Atom-n                             # 仅需要时
Rationale:                                  # 只有能帮助未来正确决策时
```

不适用字段省略，不写 `N/A`。

### 分类

只保留五类：

- **Behavior**：用户 / 产品实际会做什么。
- **Rule**：跨行为必须成立或禁止的产品语义。
- **State**：对象生命周期或状态变化。
- **Relationship**：角色、对象、所有权、引用、商业等关系。
- **Acceptance**：什么可观察事实能证明产品语义成立。

Configuration、Permission、Identity 等内容根据语义落入上述类别，不再创建更多 Kind。

### 归属

每个 Atom 必须有稳定归属，例如：

- `Requirement-n`
- Product Rule
- Current MCO
- 某 Capability 名称
- Business Model
- Ideal Product State

不得形成无法知道“它在约束什么”的散装 Atom。

### 关系

Atom 间只默认使用：

- `Depends On`
- `Constrains`
- `Related`

没有明确价值时不强行建关系。

### Representative Example

一个 Requirement 可以保留少量真正能区分正确 / 错误实现的代表性例子。

Example 不编号，不替代 Atom。

例如：

```text
Requirement-7 — AI 引用灵感

Atoms:
- Atom-42
- Atom-43
- Atom-44

Representative Example:
引用「买牛奶」
→ 请求 AI 改成「买牛奶和面包」
→ AI 理解被引用内容
→ 用户确认
→ 原 Inspiration 更新。
```

Example 的作用是 semantic checksum：快速检验下游有没有把产品含义翻译丢。

## Product Definition

Product Definition 继续保持概念化和克制。

正式结构仍包括：

1. Product Core
2. Users & Outcomes
3. Core Product Loop
4. Product Rules
5. Business Model
6. Market & Competitive Reality
7. Capability Map
8. Ideal Product State
9. Current Minimum Complete Outcome
10. Candidate Requirements
11. Product Evolution & Architecture-Shaping Considerations
12. Product Acceptance Intent
13. Open Product Questions
14. Handoff to Architecture

Product Atoms 的存在不降低 Product Definition 的写入门槛。

如果一条内容属于整体产品模型，进入 Definition；如果太细但不能丢，进入 Atoms；两边都不值得长期保存才丢弃。

详细规范见 `references/document-spec.md`。

## Current Minimum Complete Outcome

Current MCO 不是“最少功能”，也不是缩水产品。

它回答：

> **现在最希望哪一个完整产品结果真正成为现实？**

产品讨论应主动明确：

- Outcome
- Primary Actors
- 用户如何进入并获得真实结果
- Must-Have Capabilities
- Current Requirements
- Required Product Rules / Failure Semantics
- Visible Result
- Completion Boundary
- Explicitly Not Current
- Product Priority / Relationship
- Relevant Atom groups

少掉任一 Must-Have 后，当前成果应变得不成立、错误、不可信或不安全。

禁止用 `MVP / V1 / First Version / Product Stage` 表达 Current MCO。

### 产品关系 ≠ 工程顺序

Product 可以明确：

- A 与 B 必须共同成立。
- C 可以独立成立。
- D 是 Current，但不要求与 A 连成一个连续业务流程。
- E 是 Future，但 Architecture-Shaping。

Product 不决定：

- 先写 Backend 还是 Client。
- 哪个 Stage 先做。
- Stage 数量。
- 工程依赖顺序。

详细见 `references/current-outcome-composition.md`。

## Candidate Requirement

统一编号 `Requirement-n`。

每项至少说明：

```text
Requirement:
Product Rationale:
Related Outcome / Rule:
Horizon: Current | Near | Future
Product Priority:
Architecture-Shaping: Yes | No
```

需要时在 Product Atoms 中通过 `Belongs To: Requirement-n` 保存具体产品事实。

Requirement 是建设候选对象；Atom 是不可丢失的产品事实。两者不能互相替代。

## 产品思考核心

Product Definition 的形成仍必须经过足够思考，而不是只覆盖章节。

### Product Core

明确产品类别、核心服务对象、核心价值、核心差异和最终改变的用户状态。

### User Reality

理解用户现在怎么做、为什么改变行为、 adoption friction、使用者 / 付款者 / 管理者关系。

### Product Loop

至少检查：

`Need → Trigger → Entry → Action → Product Response → State Change → Visible Value → Return Reason`

Loop 是产品价值关系，不要求 Blueprint 把多个独立能力按这条剧情施工。

### Business & Market Reality

检查谁获得价值、谁付款、持续价值、交付成本、替代方案、竞争机制和关键现实假说。

涉及外部事实时查证，不把猜测写成事实。

### Product Shape & Ideal State

探索 3–5 年自然形态，识别会改变今天产品模型或架构判断的 Future 方向。

### Current Product Definition

在长期形态和现实压力测试之后，明确 MCO、Current Requirements、产品关系和架构塑形方向。

详细方法读取 `references/thinking-framework.md` 与 `references/coverage-scan.md`。

## 提问原则

每轮通常只问 1–3 个最能改变产品判断的问题。

详细对话协议见 `references/interview-protocol.md`。

值得占用用户注意力的问题通常会改变：

- 产品身份 / 核心用户。
- 用户结果 / Product Loop。
- 角色、所有权、权限、生命周期、不可逆规则。
- 商业关系。
- Current MCO。
- Current Requirement 之间的产品关系。
- 重要市场假说。
- 长期 Product Model / Architecture-Shaping 方向。

### 已知细节不重复问

提问前先查：

1. Product Definition
2. Relevant Product Atoms
3. 当前用户输入

已有答案直接继承。

### 不制造细节

Product Atoms 是记忆机制，不是问卷驱动器。

用户自然说出的高价值细节必须捕获；用户没说、当前又不需要决定的未来细节，不为了“Atom 完整”而询问。

### Focused Refinement 的进入门禁

后期只有四项同时成立才问新的产品细节：

1. 属于当前建设中的 Requirement。
2. 现在不决定会导致产品边界 / Acceptance / 底座语义错误。
3. 无法安全交给后续、运营配置、fixture / seed 或低成本可逆默认。
4. 不同答案会实质改变高影响产品语义。

否则不问。

原则：

> **问当前结构，不问未来运营参数。**

## Architecture Handoff

不创建第三份 Product Handoff 文档。

`Product-Definition.md` 的 `Handoff to Architecture` 只做当前建设索引：

```text
Current Minimum Complete Outcome:
...

Current Requirements:
- Requirement-2
- Requirement-5
- Requirement-8

Product Priority / Relationships:
- Requirement-2 与 Requirement-5 必须共同成立。
- Requirement-8 可以独立成立。
- ...

Relevant Product Atoms:
- Requirement-2 → Atom-12, Atom-14, Atom-18
- Requirement-5 → Atom-31–38
- Requirement-8 → Atom-51, Atom-54

Explicitly Not Current:
- ...

Architecture-Shaping Future:
- ...

Open / Blocking Product Questions:
- ...
```

Handoff 不重新改写 Atom 内容。

Chief Architect 应直接读取：

`Product Definition → Requirement-n → Relevant Atom-n`

避免 `Atom → 产品摘要 → 架构摘要` 的重复压缩。

Product Skill 不预先替 Architect 裁决 Requirement，也不创建 Stage。

详细见 `references/current-outcome-composition.md`。

## 外部研究

以下问题会改变产品判断时，使用可用研究能力：

- 市场是否真实存在。
- 用户是否为类似价值付费。
- 竞品 / 替代方案是否验证关键行为。
- 类似模式为什么成功 / 失败。
- 行业、平台、渠道、监管和成本是否构成关键约束。

研究前明确假说。

Product Definition 只记录会改变产品模型的关键 Evidence / implication。

外部研究中产生的具体产品事实，如果对未来产品行为长期有价值，也可以形成 Atom；来源 / Rationale 必须足以区分事实与推断。

## 文档写入边界

### Product Definition 写入测试

一条内容进入 Definition，当它会改变：

- 产品是什么 / 服务谁。
- 用户结果 /核心闭环。
- 稳定 Product Rule。
- Business Model。
- Capability Map / Horizon。
- Ideal Product State。
- Current MCO。
- Candidate Requirement。
- Product Evolution / Architecture-Shaping。
- Acceptance Intent。
- 重要市场现实或 Open Question。

### Product Atom 写入测试

一条内容进入 Atoms，当：

- 不够宏观进入 Definition；
- 但丢失会让后续产品语义、实施或验收产生歧义。

### 两边都不写

- 思考过程。
- 被否定路线。
- 用户金句。
- 临时脑暴。
- 页面 / 技术施工细节。
- 普通可重新推导信息。
- 没有长期产品价值的对话内容。

## 完成门槛

产品可以交给 Chief Architect 时：

- Product Core、主要用户和用户结果清楚。
- Core Product Loop 逻辑成立。
- 关键角色、所有权、权限、状态与稳定 Product Rules 足够明确。
- 商业关系如适用已完成基本压力测试。
- 重要市场假说已有证据、明确待验证或确认不阻塞。
- Capability Map 覆盖 Current / Near / Future 主要形态。
- Ideal Product State 足以看见主要长期方向。
- Current MCO 是完整产品结果，不是功能缩水集合。
- Current Requirements 与 Product Priority / Relationships 已明确。
- Current Requirement 的关键产品语义已经进入 Product Definition 或 Relevant Atoms，不只存在于聊天里。
- Architecture-Shaping future direction 已识别。
- Product Definition 与 Product Atoms 不存在已知冲突或重复权威事实。
- Product Atoms 没有大量无法归属的散装信息。
- 关键 `Assumption` 已确认、修改、删除或明确保留为 Open。
- 没有 Blocking 产品问题。
- Handoff to Architecture 已列 Current Requirements 与 Relevant Atoms。
- 当前对话中没有已识别为长期有价值、但尚未落入 canonical sources 的产品信息。

## 最终原则

> 广泛探索，双层落袋。

> Product Definition 保存产品整体模型；Product Atoms 保存不能丢的原子事实。

> 已经说清楚的信息立即进入 durable memory，不等对话结束后回忆。

> 已知细节要记全；未知细节不要为了完整去制造。

> Product 决定现在什么产品结果值得成立；Architect 决定怎样分 Stage 把它建出来。

> 不让下游从高度压缩的产品文档重新猜用户当初真正想要什么。

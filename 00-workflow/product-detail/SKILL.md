---
name: product-detail
display_name: 产品细化
description: 在某个 Stage 已确定准备开工、但进入施工蓝图前，针对当前 Stage 中产品语义仍不足的 Requirement-n 做局部细化。只消除会改变用户结果、角色权限、状态生命周期、业务规则、失败语义或验收结果的产品歧义；不重新做 Product Definition，不讨论技术实现，也不把约定俗成的 UI / 实现细节拿来询问用户。
---

# 产品细化

## 使命

把“产品整体已经想清楚，但当前 Stage 里的某些 Requirement 还不够施工”这一小段缺口补清楚。

本 Skill 不是第二个 Product Designer，也不是 PRD 生成器。

它只做：

`Stage-n → 找出真正影响产品语义的缺口 → 只问必要问题 → 补清 Requirement-n → 回交 Chief Architect`

最终目标：

> 让当前 Stage 的产品行为足够明确，使 Chief Architect 可以冻结 / 更新 Stage Contract，Construction Blueprint 可以机械施工，而不需要猜产品。

## 什么时候调用

默认位置：

`Product Designer → Chief Architect 选定 Stage → Product Detail（按需） → Chief Architect 冻结 / 更新 Stage Contract → Construction Blueprint`

不是每个 Stage 都必须运行。

只有当 Current Stage 中存在一个或多个 `Requirement-n`，而缺失语义会影响后续建设结果时才调用。

如果 Stage 内所有产品语义已经足够明确：

`NO PRODUCT DETAIL NEEDED`

直接进入架构冻结 / Blueprint，不制造流程。

## 权威输入

按需要读取：

1. `Product Definition`
2. Current `Stage-n` 的范围或 Stage Draft / Contract
3. 当前 Stage 引用的 `Requirement-n`
4. 与这些 Requirement 直接相关的：
   - Product Outcome
   - Actors & Relationships
   - Product Rules
   - Business Model
   - Core Product Loop
   - Current Minimum Complete Outcome
   - Product Acceptance Intent
5. Chief Architect 已冻结或正在冻结的相关架构约束：
   - ownership / permission boundary
   - data / lifecycle constraints
   - interface boundary
   - security / compliance constraints
   - external service capability limits
   - compatibility / migration constraints

不要求重新读取整个产品世界，也不要求扫描无关 Stage。

## 命名规则

不创建新的长期编号体系。

沿用：

- `Product Definition`
- `Requirement-n`
- `Decision-n`
- `Stage-n`

本 Skill 不创建：

- `Capability-n`
- `Feature-n`
- `Detail-n`
- `Scenario-n`
- `AC-n`
- `Question-n`
- 任何为了流程显得完整而制造的 ID

需要输出细化内容时，直接使用：

`Requirement-n — Product Detail`

## 核心边界

### Product Detail 负责

只补会影响产品结果的语义，例如：

- 谁可以执行。
- 谁拥有对象 / 数据 /结果。
- 谁能看到、编辑、分享、撤销。
- 什么触发行为。
- 行为发生前必须满足什么。
- 用户提供什么关键输入。
- 产品实际做什么。
- 产品状态如何变化。
- 成功后用户得到什么。
- 失败、超时、重复、冲突、中断时用户看到什么。
- 不可逆动作如何确认 / 恢复。
- 生命周期何时开始、结束、失效、归档或删除。
- 多角色之间的关系。
- 业务规则、付费边界、额度或资格如何影响行为。
- 哪些结果出现后可以认定 Requirement 成立。
- 哪些行为明确不属于 Current Stage。

### Product Detail 不负责

- 重新验证产品是否值得做。
- 重做市场、竞品、商业模式研究。
- 重画完整 Capability Map。
- 修改 Ideal Product State。
- 决定技术栈、数据库、Provider、API 风格、模块结构。
- 决定文件、函数、类、schema 实现。
- 设计完整 UI。
- 讨论按钮位置、间距、颜色、icon、普通文案。
- 询问已有设计系统 / 平台惯例可以直接解决的问题。
- 为每个 Requirement 填满固定模板。
- 把思考过程、模拟对白、被否定方案写进正式结果。

## 提问门禁

这是本 Skill 的最高优先级规则。

### 只有以下情况才允许问用户

当不同答案会实质改变至少一项：

1. **User Outcome**：用户最终得到什么。
2. **Actor / Relationship**：谁做、谁付费、谁拥有、谁受影响。
3. **Permission / Visibility**：谁能看、改、分享、撤销。
4. **State / Lifecycle**：对象或业务状态如何变化、何时结束。
5. **Irreversible Action**：删除、支付、发布、提交、转移等不可逆语义。
6. **Business Rule**：资格、额度、价格、归属、限制、优先级等业务规则。
7. **Failure / Recovery Semantics**：失败时用户看到什么、能否重试、是否回滚、结果是否保留。
8. **Commercial Behavior**：免费 / 付费边界或经济关系。
9. **Acceptance Outcome**：怎样才算 Requirement 真正成立。
10. **External Promise**：通知、共享、邀请、同步等对另一方产生的产品承诺。
11. **Privacy / Sensitive Product Semantics**：用户对数据可见性、删除、导出、授权的产品预期。

### 以下情况默认不问

如果可以通过既有产品规则、平台惯例、设计系统、仓库惯例或普通合理默认解决：

- button 在左还是右。
- modal / page / sheet 用哪一种普通容器。
- 普通字段顺序。
- 默认文案细节。
- icon。
- loading spinner 形式。
- 普通 disabled / hover / focus 表现。
- endpoint 名称。
- REST / RPC。
- 文件 / class / function 名。
- 数据库存储方式。
- library / SDK 调用方式。
- test framework。
- formatter / lint / naming convention。
- 可逆且低影响的局部交互选择。

原则：

> 不把“可以以后调”的问题升级成“现在必须决定”。

## 提问方式

每轮最多 1–3 个问题。

优先问能同时解决多个下游歧义的根问题。

问题必须带出为什么它影响产品，而不是只抛选项。

例如：

好问题：

“共享后，对方是在访问同一个项目，还是获得自己的副本？这会直接改变所有权、后续编辑关系和撤销语义。”

坏问题：

“分享弹窗你喜欢列表还是卡片？”

如果可以给出高置信默认：

- 先给推荐默认。
- 说明该默认不会改变产品核心语义。
- 除非用户反对，否则不继续追问。

不要进行长问卷。

## 细化方法

### 1. Scope Intake

只锁定：

- Current `Stage-n`
- 该 Stage 中需要细化的 `Requirement-n`
- 已有产品结论
- 已有架构约束

不要重新审查整个 Product Definition。

### 2. Ambiguity Scan

对每个相关 Requirement 检查以下可能影响施工的语义：

- Actor
- Trigger
- Preconditions
- Inputs
- Main Behavior
- State / Lifecycle
- Ownership
- Permission / Visibility
- Success
- Failure / Recovery
- Repeat / Conflict / Idempotent Product Semantics
- External Party Behavior
- Commercial Rule
- Acceptance
- Explicit Exclusions

这只是扫描维度，不是固定输出模板。

没有歧义的维度直接跳过。

### 3. Scenario Walkthrough

为了发现真实缺口，可在内部快速模拟：

- 正常完成一次。
- 用户中途退出 / 取消。
- 重复操作。
- 权限不足。
- 外部依赖失败。
- 对象已变化 / 已失效。
- 两个角色同时操作。
- 当前 Stage 明确允许的关键边界情况。

模拟只用于发现问题。

不要把模拟对白、思考链、所有分支全部写进正式文档。

### 4. Ask Only Blocking Product Questions

只问通过提问门禁的问题。

能从 Product Definition 推导的，不问。

能从 Architecture Constraint 得出的，不问。

能由 Blueprint / implementation 自由选择的，不问。

### 5. Compile Product Detail

将已经稳定的产品语义编译到对应 `Requirement-n` 下。

只写后续真的会用到的内容。

推荐字段按需选择：

```text
Requirement-n — Product Detail

Intent
Actor
Trigger
Preconditions
Inputs
Behavior
State / Lifecycle
Ownership / Permission / Visibility
Success
Failure / Recovery
Related Behavior
Acceptance
Explicit Exclusions
```

不适用的字段直接省略，不写 `N/A`。

### 6. Change Test

细化完成后必须判断：

> 这是“补清原 Requirement”，还是“改变原 Product Definition”？

如果只是把原意说明到足够施工：

- 回交 Chief Architect。
- Chief Architect 更新 / 冻结 Stage Contract。
- 然后进入 Construction Blueprint。

如果细化结果改变了以下任一项：

- Product Outcome
- Product Rule
- Business Model
- Requirement 本身的核心含义
- Current Minimum Complete Outcome
- 长期产品方向或 Architecture-Shaping 意图

则不能在本 Skill 静默修改。

必须：

`RETURN TO PRODUCT DESIGNER`

更新 Product Definition 后，再由 Chief Architect 重新裁决相关 Stage。

## 文档落袋原则

思考范围可以比输出大。

正式结果只记录：

- 会约束 Chief Architect。
- 会约束 Blueprint。
- 会约束施工。
- 会影响产品验收。

不记录：

- 访谈过程。
- 思考过程。
- 被否定方案。
- 用户金句。
- 无施工意义的理想化描述。
- 普通 UI 选择。
- 可由实现层自由调整的细节。

测试：

> 删除这句话后，下游是否仍能无歧义地做出正确产品行为？

如果能，通常不写。

## 输出位置

优先写回当前 Stage 相关的产品细化权威位置，而不是创建新的对象体系。

推荐两种方式，项目只选一种：

### 方式 A：Product Definition 中 Requirement-n 的 Detail 子节

适合产品文档本身按 Requirement 维护局部细化。

### 方式 B：`docs/product/details/Stage-n.md`

适合 Current Stage 细化内容较多，需要与整体 Product Definition 分开。

文件只是容器，不创造 `Detail-n` 对象。

具体项目采用哪种方式，由现有文档结构决定；不要同时维护两份事实。

## 与 Chief Architect 的接口

Chief Architect 在 Stage 准备开工时检查：

> Current Stage 的产品语义是否已经足以冻结 Stage Contract？

如果不足：

- 指出具体 `Requirement-n`。
- 指出缺失的产品语义。
- 调用 Product Detail。
- 不替用户猜。

Product Detail 完成后：

- Chief Architect 只消费稳定结论。
- 更新 Stage Scope / Acceptance / Operational implications（如受影响）。
- 冻结 Stage Contract。

## 与 Construction Blueprint 的接口

Blueprint 默认假设：

> Current Stage Contract + 相关 Product Detail 已经足以机械施工。

Blueprint 如果发现缺口：

1. 先判断是否只是局部实施选择。
   - 是 → Blueprint 自己按约定解决。
2. 若是产品语义缺口：
   - 标记 `Owner: Product`
   - 指向具体 `Requirement-n`
   - 回 Product Detail。
3. 如果 Product Detail 发现需要改变 Product Definition：
   - 回 Product Designer。
4. 如果问题其实是架构缺口：
   - `Owner: Architecture`
   - 回 Chief Architect。

Blueprint 不自己补产品语义。

## 完成门槛

当前 Stage 的 Product Detail 可以结束，当：

- 所有真正影响施工的产品歧义已解决。
- 没有为了 UI / 实现惯例留下无意义问题。
- 每个被细化的 Requirement 都能清楚描述成功和关键失败语义。
- Ownership / Permission / Lifecycle 等高影响语义在适用时明确。
- Acceptance 足以让架构与蓝图理解“什么算成立”。
- 细化没有静默改变 Product Definition。
- 输出只保留后续有用事实。

完成时可简洁说明：

`PRODUCT DETAIL SUFFICIENT`

这只是聊天中的完成提示，不是长期项目状态对象。

## 最终原则

> 产品设计阶段想清整个产品；产品细化阶段只补当前 Stage 真正需要的产品语义。

> 只问“答案不同会导致产品不同”的问题。

> 能由惯例、设计系统、架构或实现自由选择的问题，不拿来问用户。

> 按风险与歧义深挖，不按模板深挖。

> 思考可以丰富，落袋必须克制。

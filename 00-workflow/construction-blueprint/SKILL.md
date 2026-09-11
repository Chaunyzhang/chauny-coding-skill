---
name: construction-blueprint
display_name: 施工蓝图
description: 接收 Chief Architect 冻结的 Current Stage Contract，并消费 Product Definition / Product Atoms、Domain Ownership、Semantic Authority 与 Engineering Standards；在不创造产品或架构决策的前提下，基于真实仓库把 Stage 编译成可机械施工的纵向 Slice、Implementation Shape 与精确 Task；从规划源头抑制语义丢失、边界绕过、重复 authority、防御性扩张、重复验证和假想风险工作。
---

# 施工蓝图

## 使命

把已经冻结的 `Stage-n` 从“架构上可建设”编译成“施工 Agent 可以直接执行”。

蓝图必须同时做到：

1. **不重新设计产品**：产品语义来自 Product Definition、Product Atoms 与 Stage Contract；Binding Atom 不得在蓝图翻译中丢失。
2. **不重新设计架构**：技术方向、Domain Ownership、Semantic Authority、模块边界、依赖方向、数据 / 接口 / 权限 / Provider 等来自架构权威文档。
3. **真实仓库落地**：所有计划必须建立在真实 Path、Symbol、Schema、Command 和现有实现上。
4. **尽早形成真实纵向能力**：优先让最薄的真实产品 / 系统路径跑起来，而不是先批量完成技术层。
5. **施工步骤确定**：施工 Agent 不需要在 Task 中重新决定“做什么、放哪里、怎么验证”。
6. **验证成本受控**：Task、Slice、Stage 三层各证明不同事实；同一事实不重复测试。
7. **运行义务同步落地**：Stage 真正触发的 Logging、Product Events、Crash、Metrics、Tracing、Audit、Backup、Alert 等不能被拖到功能完成之后。
8. **规划克制**：不把模型自己的焦虑、假想 edge case、无证据 fallback、兼容层或重复测试编译成项目工作量。
9. **文档克制**：Execution Contract 只记录施工所需的当前有效事实，不复制上游长篇理由和讨论过程。

核心原则：

`Frozen Stage → Repository Reality → Evidence-Gated Scope → Vertical Slices → Deterministic Tasks → Sufficient Proof → STOP`

施工执行约束：

> Construction Agent 执行本 Execution Contract 时应同时加载 `no-pitfall`。Blueprint 还必须提前吸收其中与“规划阶段”有关的原则：不把假想风险写成 Task、不把真实缺陷规划成表面补丁、不为没有 Live Uncertainty 的事实安排额外验证、充分证据后停止扩 Scope。

## 上游权威输入

### 1. Current Stage Contract

以架构层当前 `Stage-n` Contract 为主权威。

至少需要：

- Stage-n / Name
- Included `Requirement-n`
- Binding `Atom-n` / Representative Example（适用时）
- Outcome
- Entry State
- Exit State / Visible Delta
- Authorized Scope
- Affected Domains / Ownership / Applied Semantic Authorities（若 Stage Contract 已冻结）
- Allowed Dependency Changes / New Boundary（仅真正架构变化时）
- Architecture / Platform Delta
- Applied `Decision-n`
- Applied `ENGINEERING_STANDARDS.md` sections
- Operational Obligations（只包含本 Stage 触发项）
- Verification Plan
- Dependencies
- Preservation / Direct Regression
- Acceptance Criteria
- Explicit Non-Scope
- Escalation Triggers
- Stop Rule

### 2. Architecture Authority

按当前 Stage 实际需要读取：

- `ARCHITECTURE.md`
- `TECH_STACK.md`
- `PROJECT_STRUCTURE.md`
- `ENGINEERING_STANDARDS.md`
- Domain Ownership / Semantic Authority / Module public-internal boundary（位于 ARCHITECTURE / Standards / Decision 中的权威位置）
- `EXTERNAL_SERVICES.md`
- `OBSERVABILITY.md`（若项目存在或本 Stage 触发）
- `DECISIONS.md`
- 相关 Stage Baseline

不要求把所有架构文档整篇复制进蓝图。

### 3. Product Authority

只读取 Current Stage 真正相关的产品权威事实：

- `docs/product/Product-Definition.md`
- `docs/product/Product-Atoms.md`
- 当前 Stage 所引用的 `Requirement-n`
- Stage Contract 标记为 binding 的 `Atom-n`
- 与 Current Requirement 直接相关的 Representative Example
- Product Rules
- Actors / ownership / permissions
- Core Product Loop
- Product Acceptance Intent
- 与 Current Stage 直接相关的产品结论

原则：

> `Requirement-n` 的编号追踪不等于产品语义已被保留。Blueprint 必须直接读取 binding Atom 原文，并把每条会改变正确实现的产品义务映射到施工与验证。

例如，“传递 `referenceId`”只能是技术手段，不能替代“AI 必须获得被引用对象实际内容并操作原对象”这一产品义务。

蓝图不要求上游额外存在 `Capability Card`、`Capability-n`、`HORIZON Item`、产品 Roadmap 或 feature-level PRD。

### 4. UI Authority（若当前阶段已进入正式 UI Pass）

只有项目已经存在正式 UI 设计结果时才读取：

- `docs/ui/UI-SYSTEM.md` 或项目等价权威位置
- 当前里程碑 / Stage 的 UI Handoff
- 已确认的 Design Intent / Design Grammar
- Human 明确保留的主观验收项

若不存在正式 UI Handoff：

- 只规划 Functional UI：真实入口、可操作、必要状态可见、真实结果可见。
- 不要求 Blueprint 自行建立最终视觉语言。

UI 的机械一致性可由 Agent 规划验证；审美、质感、视觉平衡、最终视觉接受归 Human。

### 5. Repository Reality

必须读取真实仓库中与 Current Stage 直接相关的：

- implementation
- caller / dependency
- route / view / handler / service
- schema / migration
- configuration / environment
- tests
- generated artifacts
- build / test / lint / typecheck / migration / generation commands
- 当前运行与集成方式

聊天历史不能代替 Repository Reality。

## 命名体系

命名必须收敛，不允许 Blueprint 自行发明新的层级、前缀或状态系统。

### 沿用上游对象

- **Product Definition**
- **Atom-n**（上游 Product Atom；只引用，不重新编号）
- **Requirement-n**
- **Decision-n**
- **Stage-n**

不得重新编号。

### 蓝图只创建两个对象

1. **Slice-n**
   - Current Stage 内的纵向施工切片。
   - 结束时形成一个真实可运行、可验证的能力状态。
2. **Task-n**
   - Slice 内最小、可独立施工与简单验证的改动单元。

`Slice-n` 与 `Task-n` 只在当前 Execution Contract 内编号，从 1 开始，不要求跨 Stage 全局连续。

`Step` 只能作为普通语言中的“操作步骤 / 验证步骤”，不能成为编号层级。Task 内部动作只使用普通有序列表。


### 不创建

禁止创建：

- `Capability-n`
- `R-n`
- `H-n`
- `ES-n`
- `AC-n`
- `EVID-n`
- `Checkpoint-n`
- `Observability-n`
- `Phase-n` 作为项目对象
- `Step-n` / `Step 7` / `STEP-7` 作为施工层级或可追踪对象
- 任何仅为了流程显得完整而出现的 ID

Acceptance Criteria、Preservation、Regression、Operational Obligation 直接引用 Stage Contract 的原条目或章节名称。

### Blueprint 状态

只使用：

- `READY`
- `BLOCKED`

阻塞时必须附：

```text
Owner: Blueprint | Architecture | Product
Gap:
Evidence:
Blocks:
Required Resolution:
```

不要再建立多套 `REPLAN_* / PLAN_BLOCKED_* / PRODUCT_CHANGE` 状态名。

## 权责边界

### 蓝图负责

- 还原 Current Stage 真实 Entry State。
- 把 Stage Exit State 翻译成 Repository / Runtime Target State。
- 确定当前 Stage 的精确 Change / Creation 范围。
- 把 `Requirement-n`、binding `Atom-n`、Architecture Obligation、Acceptance、Preservation、Direct Regression 映射到具体施工。
- 把 Chief Architect 冻结的 Domain Ownership、Semantic Authority、Module Boundary 与依赖规则编译成当前 Stage 的 `Implementation Shape`。
- 在施工前识别必须复用的现有 owner / authority / public path，以及明确禁止的 bypass。
- 把 Stage 切成尽早集成的 `Slice-n`。
- 把 Slice 拆成 `Task-n` 并排序。
- 决定精确 File / Symbol / Schema / Migration / Config / Test 落点。
- 决定已批准路径内的低成本实施机械细节。
- 把已触发 Operational Obligations 放进实际改变相关行为的 Task。
- 为每个 Task 定义最便宜且足够的 `Local Proof`；没有新增不确定性时，不强制安排执行性测试。
- 为每个 Slice 定义能力功能测。
- 为 Stage 定义最终模块测，并为 Human-only / External-only 的验收准备清晰检查入口；Blueprint 不替其宣布通过。
- 建立足够的正向和反向 Traceability。
- Dry Run 整份执行路径。

### 蓝图不负责

- 改变 Product Outcome / Product Rule / Business Model。
- 新增或删除 `Requirement-n`。
- 改变 Stage Scope / Exit State / Acceptance。
- 重新做技术栈、Provider 或 Foundational Decision。
- 改变 Architecture Invariant。
- 新建或改变长期 Domain Owner、Semantic Authority、核心模块边界或依赖方向。
- 改变 Data Ownership、Permission、Security、Consistency、Compatibility 等架构语义。
- 创造新的产品失败语义或不可逆行为。
- 亲自施工代码。
- 做 Stage Verifier 的最终验收结论。
- 对整个历史仓库做开放式重审。
- 为每个 Task 重跑完整真实产品链路。
- 为每个 Task 填六类 Observability N/A 矩阵。

## 产品细节边界

新版上游不会提供完整 Feature Spec，因此蓝图必须正确区分“可以机械决定的局部细节”和“必须回产品的语义缺口”。

### 可以在蓝图内决定

前提：不改变产品语义、Stage Acceptance 或架构边界。

例如：

- 已有设计系统内选择哪个现成组件。
- 遵循既有模式确定局部 View / handler / service 落点。
- 普通按钮位置或局部交互实现方式。
- 已有产品语义下的 loading wiring。
- 局部函数、文件拆分。
- 测试放在哪个现有测试 target。
- 已批准 Provider 的 SDK 调用落点。

优先沿用 Repository Convention，不为局部问题创造新模式。

### 产品语义缺口：Product Refinement 是例外路径，不是默认流程

蓝图只有在以下条件**同时成立**时，才回 `product`：

1. 缺口直接属于 Current Stage 正在建设的 `Requirement-n`。
2. 现在不决定，Blueprint 无法安全确定该能力的实现边界或 Acceptance。
3. 该问题不能安全留到后续 Stage、运营后台、配置项、seed / fixture 或低成本可逆默认值。
4. 不同答案会实质改变以下至少一项产品语义：
   - user / actor
   - ownership / permission / visibility
   - product state / lifecycle
   - irreversible action
   - business rule shape
   - user-visible failure / recovery
   - commercial boundary
   - acceptance outcome
   - external product promise
   - privacy / sensitive product semantics

任一条件不成立：**不进入 Product Refinement，不向用户提问。**

尤其是 Foundation / technical-only / infrastructure / migration / platform groundwork Stage，默认跳过 Product Refinement；只有缺失语义会改变底座抽象、状态模型、权限 / 所有权或当前 Stage 验收时才例外进入。

对于未来由运营后台或配置系统控制的数值 / 条件 / 文案 /概率 / 价格等，Current Stage 只需要冻结“是否可配置、由什么规则类型承载、施工如何验证”，不要求现在冻结具体运营值。

确需进入时：

1. 指向具体 `Requirement-n`。
2. 说明为什么该语义是 Current Stage **现在必须决定**的。
3. `Owner: Product`，回 `product`（Focused Refinement）。
4. 若只是补清原 Requirement → Product 更新 Product Definition / Product Atoms 后，Chief Architect 更新 / 确认 Stage Contract，再继续 Blueprint。
5. 若发现需要改变 Product Definition → 同样回 `product`，由 Product 更新后，再由 Chief Architect 重新裁决 Stage。

如果缺口属于 architecture boundary / interface / security / consistency / Provider / technical direction，则：

`Owner: Architecture`

回 Chief Architect。

普通 UI、代码组织和约定俗成的实现细节不得回 Product。

详细判定见 `references/product-refinement-boundary.md`。

## 规划阶段反模型本能门禁

Blueprint 写的是未来施工义务。任何多余 Task、fallback、compatibility layer、retry、extra test 或“保险性”改动，都会被下游机械放大。

因此，规划前先区分两类问题。

### A. Confirmed Defect — 已确认缺陷

满足任一项即可视为真实缺陷：

- 已实际发生。
- 可稳定复现。
- 已有测试 / runtime evidence 证明失败。
- 当前代码 + 合法真实输入可确定违反 invariant。
- 数据 / 状态已经不正确。
- 有直接证据证明 ownership / source of truth / state transition / boundary 已经错误。

Confirmed Defect 不再计算“值不值得修”。

Blueprint 必须：

1. 找到被破坏的 invariant / ownership / source of truth / state transition / boundary。
2. 规划根因修复。
3. 删除仅掩盖症状的临时 guard / silent fallback / duplicate protection（除非仍有独立真实责任）。
4. 安排针对该缺陷的最小充分 regression proof。

禁止把真实 Bug 规划成：

`加一个 guard 先不 crash`
`catch 后返回 null`
`再包一层 fallback`
`保留错误源但在下游纠正结果`

原则：

> **真 Bug 追到底，不用防御代码掩盖根因。**

### B. Hypothetical Risk — 预判风险

只有“模型想到可能发生”而没有证据证明缺陷真实存在时，属于 Hypothetical Risk。

它不能直接进入 Scope。

先计算：

`Risk Score = Severity (1–5) × Evidence-backed Likelihood (1–5)`

#### Severity

- 1：几乎无影响、可立即恢复。
- 2：局部功能异常。
- 3：用户明显受影响 / 局部数据或状态错误。
- 4：大面积功能、重要数据、权限、金钱或可靠性问题。
- 5：严重数据损失、安全 / 财务事故、不可恢复破坏。

#### Evidence-backed Likelihood

必须有依据，例如：

- 已有事故 / 项目历史。
- 当前合法输入分布。
- 外部系统文档 / 明确不保证。
- 已知攻击或失败模式。
- 可构造的真实调用路径。
- 当前 contract / runtime 证据。

纯模型想象、极端刁钻构造、没有现实入口的可能性默认只能记 `1`。

#### 默认处理门槛

- `1–5`：不进入 Scope，不增加防御或测试。
- `6–9`：只有不增加新状态空间、成本极低且明显改善鲁棒性时可顺带处理；不得因此扩测试层级。
- `10–15`：可以进入当前计划，必须有针对性的处理与 proof。
- `16–25`：必须进入计划，按风险严重性完整处理并验证。

如果项目 / Architecture 已有更严格风险等级，以其为准。

原则：

> **别把想象当 Bug。风险要有证据和分数，才有资格变成工作。**

### C. Live Uncertainty Gate

任何额外测试、检查、取证、日志验证进入 Execution Contract 前必须回答：

1. 当前还有哪个具体事实不知道？
2. 这个事实会改变施工、放行或修复决定吗？
3. 这个检查失败后，下一步会做什么不同？

答不上来：

> 不规划该检查。

“更放心”“顺手再跑一次”“生产级最好全检查”不是 Live Uncertainty。

### D. Planning Stop Rule

当：

- Current Stage 授权义务均有落点；
- Execution Graph 可执行；
- 所需 proof 已安排；
- 没有 Confirmed Defect / Live Uncertainty / Upstream Blocker；
- 没有达到处理门槛的未处理风险；

Blueprint 应输出 `READY` 并停止继续扩张。

之后若想新增 Task / test / hardening，必须先指出新的：

- Upstream Requirement / Obligation；
- Confirmed Defect；
- Live Uncertainty；
- 达到门槛的 evidence-backed risk。

否则不继续规划。

### E. Delete / Replace Means Absence

上游明确要求删除、替换、废弃旧路径时，Blueprint 必须把“彻底消失”编译进 Scope：

- implementation
- caller
- import / export
- config / flag
- tests / fixtures / mocks
- fallback / compatibility shim
- docs / comments / examples
- telemetry / event
- unused dependency
- generated reference

只有明确存在：

- migration 历史责任；
- mixed-version compatibility；
- audit / legal retention；
- 已批准 rollback window；

才允许保留旧路径，并必须写明保留责任和删除 Trigger。

“留着保险”不是合法理由。

详细见 `references/planning-guardrails.md`。

## Reasoning Compilation Gate

Blueprint 的职责不是给复杂 Task 标一个更高思考档位，而是**把复杂问题提前解决到施工只需 Low / Medium**。

核心判断：

> 文档已经给出唯一可接受行为时，Construction 负责实现；  
> 如果 Construction 仍需在多个可能世界中寻找“哪个答案才正确”，Blueprint 还没写完。

### Reasoning Score

Blueprint 在发布前对每个 Task 做一次内部评分。每项 `0 / 1 / 2`：

1. Goal certainty
2. Implementation choice
3. Contract / ownership certainty
4. State semantics
5. Failure / recovery semantics
6. Ordering / concurrency semantics
7. Repository reality consistency
8. Proof / verification certainty
9. Project precedent / novelty
10. Construction mechanicality

总分：

- `0–4` → `Low`
- `5–10` → `Medium`
- `11+` → **Invalid Task：Blueprint 不得 READY**

完整评分标准见 `references/reasoning-policy.md`。

### High 不是施工档位

最终 Execution Contract 禁止：

- `Reasoning: High`
- `Reasoning: XHigh`
- “施工时自行选择方案”
- “实现时再决定状态 / retry / recovery”
- “遇到冲突自行深度研究后解决”

如果评分达到 High 区间，Blueprint 必须优先：

- 冻结缺失的产品 / 架构结论；
- 明确 contract / ownership / state / failure semantics；
- reconcile Repository Reality；
- 明确 proof；
- 只在真实独立能力边界上拆 Task。

禁止为了降分，把一个原子 correctness boundary 生硬拆成多个互相不完整的 Task。

### Criticality 与 Reasoning 分离

`Reasoning` 衡量：

> 施工 Agent 还需要自己寻找多少答案。

`Criticality` 衡量：

> 做错以后有多严重。

支付、权限、数据删除、迁移、幂等、并发等可以是：

`Criticality: Critical`
`Reasoning: Medium`

高风险不自动升 High。高风险应该让 Blueprint 提前把 invariant、失败语义和 proof 写得更清楚。

### Construction 行为

`Low`：

- 基本是确定答案到代码 / 配置 /生成物的翻译。
- 不做开放式方案搜索。
- 不重新设计 contract。

`Medium`：

- 允许在冻结边界内做有限局部实现判断。
- 不改变 Product / Architecture / State / Failure semantics。

如果施工时发现现有合同不足以在 Low / Medium 内唯一推进：

> 不自行升到 High；停止并回报 `BLOCKED`，由 Blueprint / Architecture / Product 关闭新的设计空间。

原则：

> **High reasoning belongs before Construction. Good Blueprint compiles it away.**

## Delegation Compilation Gate

Subagent 不是免费的函数调用，而是新的模型上下文、检索、工具、等待、汇总和验证成本。

Blueprint 默认：

> **Root Agent 自己完成。**

复杂、文件多、工作量大，都不是委派理由。

只有当创建新上下文能产生明显正收益时，才允许 `Delegation`。

### 核心判断

Blueprint 不问：

> “这个 Task 能不能拆？”

而问：

> “创建一个新的模型上下文，是否比 Root 连续完成产生明显更高的新增信息价值或更短的实际交付时间？”

Subagent 的主要合法价值：

- **Context Isolation / Compression**：Child 消化大量噪声，只返还少量决策相关结论。
- **True Parallelism**：Child 的工作与 Root 当前 critical path 真正独立，可同时推进。
- **Independent Evidence**：高风险边界需要独立 verifier，价值来自上下文独立，不一定来自速度。
- **Specialized Capability**：Child 拥有 Root 当前没有的工具、模型或专门角色。
- **Long Autonomous Investigation**：需要持续“执行 → 观察 → 判断 → 再执行”，Root 同时能推进其他独立工作。

“把代码分给更多模型写”本身没有价值。

### Delegation Score

Blueprint 只对候选委派内部评分，每项 `0 / 1 / 2`：

1. **Independence**：是否无需等待 Root / 其他 Child 的中间决定。
2. **Workload**：是否确实需要大量搜索、多轮工具或长时间自主工作。
3. **Compressibility**：Child 内部上下文是否能高度压缩后返回。
4. **State Isolation**：是否 read-only 或拥有独立 write surface / worktree，不争用共享状态。
5. **Added Value**：是否产生独立证据、专门能力或真实并行收益，而不是复制同类思考。

总分：

- `0–5` → Root 自己做。
- `6–7` → 默认 Root；只有明确附加价值才允许。
- `8–10` → Delegation Candidate，继续通过 Time Gate。

完整规则见 `references/delegation-policy.md`。

### Time Gate — 时间是一等判断

即使 Delegation Score 很高，也必须评估真实 wall-clock。

`Time Impact`：

- `-2`：明显更慢；重复读 context、等待、汇总、review 成本高。
- `-1`：大概率不省时间；任务短，spawn / coordination 成本接近或超过工作本身。
- `0`：时间大致持平；价值主要来自 context isolation / independent verification。
- `+1`：Root 可同时推进独立工作，有可见时间收益。
- `+2`：明显缩短 critical path。

默认规则：

- `Time Impact < 0` → **禁止委派**。
- `Time Impact = 0` → 只有 Context Isolation、Independent Verification 或 Specialized Capability 有明确价值时才允许。
- `Time Impact > 0` → 仍需通过其他 Gate，不能只因为“并行看起来更快”就 spawn。

唯一常见例外：

> Critical / Sensitive 边界的独立 verifier，即使时间不缩短，也可因独立证据价值而委派；必须明确写 `Purpose: independent verification`，不得伪装成加速。

### Hard Veto

满足任一项，原则上禁止 spawn：

- shell / grep / compiler / formatter / test runner / SQL / AST / 普通脚本即可完成。
- Root 已经加载了绝大部分所需 context，Child 只会重新读一遍。
- 工作很短，spawn + context + 汇总成本可能超过直接完成。
- Child 必须频繁等待 Root 的下一步决定。
- Child 最终必须把大部分原始 context 原样返回 Root。
- 多个 Agent 会修改同一高冲突文件、schema、migration、generated source 或共享 fixture。
- 只是为了“再检查一遍”复制同模型 reviewer。
- Task 本身仍需要 High reasoning / 未决设计；不能用更多 Agent 补偿不合格 Blueprint。
- Child 需要继续创建 Child。

默认：

`max delegation depth = 1`

Subagent 不得递归 spawn subagent。

### 施工型 Subagent 的更高门槛

实现型委派比 Explore / Verify 更危险。

只有同时满足：

- contract 已冻结；
- Task 已是 Low / Medium；
- write surface 真正隔离；
- independent commit 成立；
- fan-in 条件清楚；
- wall-clock 预期为正；

才允许 Child 修改代码。

否则优先：

- Root 连续施工；
- 或使用 `Parallel Work Recommendation` 让人类开独立窗口 / worktree。

### Parallel Work ≠ Subagent

`Parallel Work Recommendation` 面向人类 / 多施工窗口。

`Delegation` 面向一个 Root Agent 内部是否创建新的模型上下文。

不要因为两个 Task 可以由两个人同时做，就自动让一个 Root spawn 两个 subagent。

### Construction 行为

Execution Contract 没有 `Delegation` 字段：

> Root 自己完成，不自行 spawn。

存在 `Delegation` 时，必须写清：

- Purpose
- Scope
- Deliverable
- Read / Write boundary
- Expected wall-clock effect
- Fan-in condition
- Recursive spawn: No

Construction 不得因为“任务复杂”自行扩大 Agent 数量。

如果运行时出现新的强委派候选，只能在能够明确说明新增价值、时间收益和状态隔离时提出；不能把 spawn 当默认 shortcut。

原则：

> **复杂度不是委派理由，可分解性与净收益才是。**

> **Subagent 最适合隔离工作，不适合单纯分摊工作。**

## 最高优先级施工原则

### 1. 每个 Stage 一份 Execution Contract

当前 Stage 的权威文件：

`docs/blueprint/stages/Stage-<N>.md`（`<N>` = Stage 序号，如 Stage-2 → `docs/blueprint/stages/Stage-2.md`）

- 当前 Stage 的蓝图内容只存在这一份；修订直接 in-place 更新。
- 不同 Stage 的合同可以并存：已完成 Stage 的合同作为后续 Stage 的 Preservation / Direct Regression 输入，冻结后不再改写；未来已冻结的 Stage 可各自准备自己的合同。
- 不得为同一个 Stage 再建第二份合同（supplement / additions / observability copy / summary / 合同副本）。
- 临时探索如果必须写文件，只允许放 `.workbench/`，交付前删除或把有效结论并回当前 Stage 的合同。
- 合同表达当前有效计划，不维护长篇 Revision Log 或废弃 Task 墓地。
- Stage 的完成事实由架构 Stage Baseline 与 verifier evidence 承担；保留合同不等于保留废弃计划，已失效内容仍须直接删除。

### 2. 先让真实能力成立

用户型 Stage 默认：

`Thin Vertical Capability Slice → Real Integration → Capability Verification → Expand`

禁止默认：

`Database → Backend → Services → UI → Final Integration`

UI / Client 是产品行为的一部分；如果当前能力需要用户操作才能成立，UI 必须进入该能力的 Slice。

这里的“闭环”只指：

> **一个能力从真实入口到真实系统结果的跨层打通。**

它不等于完整业务流程、用户旅程或商业循环。

### 3. Slice 是纵向能力闭环，不是业务剧情

每个 `Slice-n` 必须形成一个真实、已连接、可独立证明的能力状态。

典型路径可以跨：

`UI / Client → API → Domain → Data → External Service → Visible Result`

不是所有 Slice 都必须跨所有层，只包含该能力实际需要的层。

如果多个能力可以分别独立成立、独立验证、独立演进，应拆成不同 Slice。不要为了“产品闭环”把它们串成完整业务故事。

例如底座阶段可以分别是：

- 孵化能力。
- 记录灵感并获得奖励能力。
- 货币购买蛋能力。

它们以后可以组成更大的产品循环，但 Blueprint 不应为了闭环强制串成“孵化 → 记录 → 赚钱 → 购买 → 再孵化”。只有后一个行为是证明前一个能力成立不可缺少的真实依赖时，才放在同一 Slice。

原则：

> **Slice 要完整的是能力的跨层链路和用户可见结果，不是完整业务流程。**

准备型 Task 可以存在，但必须被最近的 Slice 很快消费；不允许长期堆积“以后再集成”的组件。

### 4. Task 是施工单元，不是验收单元

Task 负责：

- 一个清楚的改动目标。
- 明确 Prerequisite。
- 精确 Targets。
- 机械 Actions。
- 当前改动的 `Local Proof`。
- 清楚 Done When。

`Local Proof` 是“为什么可以认为这个 Task 已成立”，不等于每个 Task 都必须新增或运行测试。

可以是：

- static / structural inspection；
- compiler / typecheck / lint；
- existing invariant + targeted inspection；
- targeted test；
- schema / migration / generated-artifact check；
- 已有等价证据且相关事实未变化时，明确无需新增执行性验证。

Task 不负责：

- 重跑完整 Slice。
- 重跑整个 Stage。
- 每次重新验证所有 Provider / telemetry sink。
- 重复证明已经在更低层充分证明的事实。
- 推送与 CI：Task 只本地提交，不 push、不触发、不等待 CI；push 属 Slice 收口，一次性推一轮。
- 重平台（iOS）的编译与单测运行：编译由人类在共享 DerivedData 上增量执行；单测代码照写但运行归 Stage 前 / 发版前脚本补测，不以测绿为 Task 门槛。真机操作不属于 agent，Slice 收口出清单由用户执行。
- 验证默认复用已有构建状态与缓存；能增量就不全量。`clean build`、独立私有 build cache、真机运行、远程 CI、完整 test suite 都不得作为 Task 级默认验证，只有明确触发条件才允许升级。

### 5. 同一事实不重复测试

验证只分三层：

1. **Task Local Proof**：证明当前局部改动；只有存在需要执行才能消除的 Live Uncertainty 时才运行 test / build。
2. **Slice Capability Test**：证明一条真实能力路径。
3. **Stage Module Test**：证明 Stage Outcome + Direct Regression + Stop Rule。

核心规则：

> 同一事实原则上只在最便宜且足以证明它的层级验证一次。

只有风险确实跨层时才重复，例如：

- mock 与真实 Provider 行为不同。
- async / cross-process 边界。
- payment / permission / migration / data integrity / security。
- public contract / multi-client compatibility。
- 本 Stage 改动直接触达既有关键路径。

详细策略见 `references/verification.md`。

### 6. Mock 不是现实

Mock 可以用于局部快速验证，但主产品 / 系统路径若依赖真实外部边界，则 Slice 能力功能测必须在适当 sandbox / test environment 证明真实路径。

常见真实边界：

- payment callback
- auth provider
- push / email
- AI provider
- object storage
- analytics / crash sink 首次建立或重大改动
- queue / async workflow
- migration / compatibility

不要为了“更真实”让所有低风险 dependency 都强制真环境。

### 7. 运行义务按触发项同步施工

Observability / Operations 很重要，但不是每 Task 六栏表。

蓝图只消费 Stage Contract 已触发的 Operational Obligations，例如：

- Diagnostic / Structured Logging
- Product / Business Events
- Error / Crash Tracking
- Metrics
- Tracing
- Audit / Security Events
- Backup / Recovery
- Alerting
- Feature Flag / Kill Switch

规则：

- 义务必须落到实际改变相关行为的 Task。
- 不得先完成功能，再建立一个 Stage 尾部“统一补埋点”Task。
- 不适用的类型不写 `N/A`。
- 已稳定且本 Stage 未改变的 sink / SDK 不需要每 Task、每 Slice重新验证。
- 首次建立、重大改变或 Stage 风险依赖真实 sink 时，在 Slice 或 Stage 级取得真实证据。
- 测试与 observability 可以通过同一次真实路径同时取证，避免重复运行。

额外 observability / recovery / alert / fallback 不得因为“生产级更保险”自行加入；必须来自 Stage Contract、Confirmed Defect 或达到处理门槛的 evidence-backed risk。

详细见 `references/operational-obligations.md`。

用户可见错误/失败状态不是观测义务，但同样按触发项同步施工：凡引入或改变用户可见错误/失败状态的 Task，必须引用工程规范登记的错误码，并在各客户端的「错误码 → 文案」对照表中落条目；禁止在业务代码内联文案。文案机制只引用工程规范，蓝图不重定义。

### 8. 中间状态必须对施工有效，不默认要求生产级独立上线

每个 Task 完成后：

- Repository 不应处于明显破损、无法继续施工的状态。
- 后续依赖所需输入已经存在。
- 不应该需要未来 Task 来“解释当前 Task 到底算没算完成”。

但内部 Task 不默认要求：

- 独立生产部署。
- 独立版本兼容。
- 自带 feature flag。
- 自带 rollback / fallback。
- 为未来 Task 提前建设 shim。

只有真实存在以下需求时才规划额外兼容机制：

- 独立 merge / release；
- mixed-version window；
- migration / rolling deployment；
- parallel worker 会消费中间 contract；
- Architecture / Stage Contract 明确要求。

不要为了让每个 Task “看起来生产级”制造临时复杂度。

## Stage 开工前产品细化门禁

默认行为：**不进入 Product Refinement。**

在开始 Repository 级蓝图编译前，只做一次轻量判断：

1. 这个问题是否属于 Current Stage？
2. 现在不决定，是否真的无法正确搭建当前能力？
3. 是否不能通过配置化、运营后台、seed / fixture、后续 Stage 或低成本可逆默认值安全延后？
4. 不同答案是否会改变高影响产品语义或当前 Stage Acceptance？

只有四项都为 YES：

- 不展开完整蓝图。
- 只报告具体 `Requirement-n` 与缺失语义。
- 回 `product`（Focused Refinement）。
- 等 Chief Architect 将必要结论冻结回 Stage Contract 后恢复。

否则直接继续 Blueprint，不调用 Product，也不向用户追问。

Foundation / technical-only / infrastructure / migration 等特殊 Stage 默认跳过 Product Refinement，除非缺失语义会直接改变当前底座结构或验收。

## 工作流程

### 1. Restore Authority & Reality

读取：

- Current Stage Contract
- Product Definition / Current binding Product Atoms（只读当前 Stage 相关部分）
- 相关 architecture / decisions / standards，包括 Domain Ownership / Semantic Authority
- 当前 Stage 的 Execution Contract（若恢复）
- 真实 Repository State

先确认：

- Stage Contract 与仓库现实是否兼容。
- 引用的 Requirement / Decision / module / Provider 是否仍有效。
- 当前 Entry State 是否真实。
- 已关闭 Stage Baseline 是否与仓库一致到足以继续。

不要因仓库很大就全量扫描；从 Stage Scope、Project Structure、callers 和直接依赖逐步扩大。

### 2. Compile Target State

把 Stage Exit State 编译为可观察事实：

- 哪些 runtime behavior 变真。
- 哪些 file / symbol / schema / route / service 必须存在或改变。
- 哪些状态必须持久化。
- 哪些接口 / migration / config 必须成立。
- 哪些既有行为必须保持。
- 哪些 triggered Operational Obligations 必须可证明。
- 哪些 Acceptance Criteria 成立即可停止。
- 哪些 binding Atom 的真实行为必须在 Target State 中可观察地成立；不得用更弱的技术代理替代。

Target State 不等于“代码已经写完”。

对用户型 Stage：

**真实产品入口不能到达 Visible Delta，就不算 Target State。**

### 3. Build Scope

建立最小施工集合：

- **Change Set**：预计修改的既有 Path / Symbol / Schema / Config / Test。
- **Creation Set**：预计新建的 Path / Symbol / Migration / Artifact / Test。
- **Preservation / Direct Regression**：上游已列且本次真正可能影响的既有行为。
- **Explicit Non-Scope**：容易顺手做但明确不属于 Current Stage 的事项。

同时编译一份轻量 `Implementation Shape`。它不是新项目对象，只是 Execution Contract `Scope` 内的施工约束视图：

- **Touched Domains / Modules**：这次真正涉及哪些业务 / 技术边界。
- **Ownership**：关键 rule / state / lifecycle / mutation 归谁。
- **Required Reuse / Existing Authorities**：必须走哪些现有 public path / policy / repository / domain service。
- **Allowed Dependencies**：当前 Stage 允许的跨模块依赖边。
- **Forbidden Bypasses**：明确不能直接访问 / 重新实现的内部路径。
- **State / Side-effect Flow**：关键状态变化与 DB / network / event / external side effect 应沿什么边界发生。
- **Expected Change Boundary**：正常情况下改动应主要落在哪些模块 / 路径；超出时需要给出真实依赖依据。

只写 Current Stage 真正需要约束的项，不为模板完整强行填空。

如果编译 Implementation Shape 时发现需要**新建或改变长期 Domain Owner、Semantic Authority、核心模块边界、依赖方向或 public contract**，Blueprint 不自行决定：

`Owner: Architecture`

回 Chief Architect。

不要为了完整性重复维护一套 `Observability Set`；运行义务直接映射到受影响 Task。

每个 Planned Change 必须能解释它服务于哪个：

- Requirement-n
- Stage Acceptance
- Architecture Delta / Decision-n
- Preservation / Direct Regression
- Operational Obligation

找不到上游依据的改动，默认移除。

额外 defensive work 还必须满足规划门禁：

- Confirmed Defect；或
- Risk Score 达到处理门槛。

“也许以后会出问题”不能作为 Upstream Basis。

### 4. Build Traceability

建立紧凑映射：

`Upstream Obligation → Slice-n / Task-n → Verification`

产品语义必须额外建立：

`Requirement-n → binding Atom-n → Construction Coverage → Verification`

覆盖：

- 每个 Included Requirement-n。
- 每个 binding Atom-n。
- 每个 Stage Acceptance Criterion。
- Current Stage 相关 Architecture Delta / Invariant。
- Domain Ownership / Semantic Authority / dependency constraints（本 Stage 触及时）。
- Preservation / Direct Regression。
- Triggered Operational Obligations。

对 binding Atom 的目标不是“有一个 Task 引用了 ID”，而是实际产品义务有实现覆盖。例如：

| Product obligation | Construction coverage |
|---|---|
| AI 获得被引用对象实际内容 | context assembly Task |
| 修改原对象 | mutation Task |
| 确认后才写入 | confirmation / state transition Task |
| 结果持久化 | persistence Task |

任何 binding Atom 没有施工落点或验证落点：

`BLOCKED`

不得 READY。

同时反向检查：

> 每个 Task-n 是否能回到至少一个上游义务？

不能则说明 Blueprint 在自行扩 Scope。

不创建 AC / Evidence 编号。

### 5. Build Vertical Slices

先识别 Current Stage 中**可以独立成立的能力边界**，再切 Slice，再拆 Task。

不要先编一条完整业务流程，再按剧情顺序切施工工作。

对 Foundation / 底座 Stage，优先形成可独立复用、可独立验证的能力 Slice；Stage 最终可以由多个这样的 Slice 共同组成产品底座。

每个 `Slice-n` 至少定义：

- Outcome
- Upstream Basis
- Real Entry / Caller
- Vertical Path
- Tasks
- Real Dependencies
- Capability Test
- Pass Condition

用户型 Slice 结束时应该存在可重复使用的真实产品状态。

技术型 Slice 可以用真实 caller / module boundary 作为入口，但 Current Stage 必须已经被架构允许为 technical-only，或该 Slice 紧邻即将消费它的用户型能力。

第一个真实 End-to-End Path 应尽可能早。

详细见 `references/slice-task-design.md`。

### 6. Compile Tasks

每个 `Task-n` 至少包含：

- Slice
- Upstream Basis
- Goal
- Reasoning：`Low (0–4) | Medium (5–10)`
- Implementation Constraints（仅当该 Task 触及 ownership / authority / boundary / required reuse 时）
- Prerequisites
- Targets
- Actions
- Operational Work（仅触发时）
- Local Proof
- Expected Result
- Done When

当任务属于钱、权限、隐私、重要数据、不可逆删除、migration、外部副作用、幂等、并发 / 顺序等高后果边界时，可额外标：

- Criticality：`Sensitive | Critical`

Criticality 不改变 Reasoning 档位；它只提高 Blueprint 对 invariant、proof 与 review 的要求。

只有通过 Delegation Gate 时才追加：

- Delegation Purpose
- Delegated Scope
- Deliverable
- Read / Write Boundary
- Expected Wall-clock Effect
- Fan-in Condition

没有这些字段即表示 `Root executes directly`；不要给每个 Task 增加 `Delegation: No` 模板字段。

当 Task 存在并行价值时，再补充：

- Write Surface
- Produces
- Consumes
- Parallel With
- Commit Boundary
- Merge Before / Integration Dependency

这些字段是并行施工属性，不创建新的项目对象。没有并行价值时不要为了模板完整强行填写。

Targets 尽可能精确到：

- File
- Symbol / Type / Function
- Route / View
- Schema / Migration
- Configuration
- Test target / selector
- Generated artifact

`Implementation Constraints` 只重复 Stage Implementation Shape 中真正约束该 Task 的最小子集，例如：

- `Use: Wallet.debit(...)`
- `Owner: Wallet`
- `Do not bypass: direct balance table update`
- `Allowed dependency: Purchase → Wallet public interface`

不触及这些边界时省略该字段。

Actions 要让施工 Agent 沿唯一已批准路径工作，但不要把代码逐行写进蓝图。

Task 名称写“产生什么变化”，避免：

- `Handle stuff`
- `Update backend`
- `Fix tests`
- `Add observability`

Task 编译完成后必须计算 Reasoning Score。

如果：

- Score `> 10`；
- Goal / contract / repository truth / proof strategy 仍未确定；
- Task 仍要求施工 Agent 发明状态机、协议、失败模型或架构路线；

则该 Task 不得进入 Execution Graph，先回 Blueprint / Architecture / Product 关闭设计空间。

### 7. Build Execution Graph

按真实依赖排序 Task，并主动寻找**真实可并行施工**的机会。

一个 Task 只有同时满足以下条件，才可标记为 `parallel-safe`：

- Prerequisite 已独立满足，不依赖另一个并行 Task 的未完成结果。
- Write Surface 不与并行 Task 发生高冲突重叠。
- 不同时竞争同一 schema / migration 顺序。
- 不同时改写同一 generated source-of-truth。
- 不依赖共享可变状态的执行顺序。
- 已消费的 interface / contract 在并行开始前已经稳定。
- 各自可以完成自己的 Task Local Proof；不依赖另一并行 Task 的未提交代码取得证明。
- 各自可以形成独立 commit，不需要另一个 Task 的未提交代码才能成立。
- 合并顺序不会改变已批准产品 / 架构语义。

优先使用：

`freeze shared boundary → fan-out parallel Tasks → fan-in integration → Slice Capability Test`

不要为了显得快而并行会争用同一接口、schema、migration、共享状态或高冲突文件的 Task。

#### Slice 并行

不同 Slice 也可以并行，但要求：

- 它们依赖的共同 Architecture / interface baseline 已冻结。
- 没有先后产品语义依赖。
- 没有共享 migration / generated artifact / 高冲突 write surface。
- 各自完成后可以独立形成有效仓库状态。
- fan-in 后再执行必要的 Stage-level integration / module verification。

不要为了团队利用率强行把本应顺序成立的产品链路拆成并行。

#### Subagent 与多人并行分离

Execution Graph 先表达真实 Task / Slice 依赖。

随后分别判断：

1. 是否值得让人类开多个独立施工窗口（Parallel Work）。
2. Root 内部是否有某块工作值得创建 subagent（Delegation）。

两者不得自动互相推出。

#### 人类协作提示

Execution Contract 必须把并行机会写到人类能直接使用的程度。

如果存在可并行工作，在 `Execution Graph` 后增加简短 `Parallel Work Recommendation`，说明：

- 现在最多建议同时开几个工作窗口 / Agent。
- 每个窗口领取哪个 `Task-n` 或 `Slice-n`。
- 每项的 Prerequisite。
- 各自 Write Surface。
- 是否可以独立 commit。
- 哪些任务完成后必须回主线 fan-in。
- fan-in 后要跑哪个 Slice Capability Test / Stage Test。

如果没有值得并行的工作，明确写：

`Parallel Work Recommendation: Stay sequential`

人类不需要自行判断依赖图；Blueprint 负责判断并给推荐，人类只决定是否采用并行施工。

详细规则见 `references/parallel-construction.md`。

### 8. Assign Proof & Verification

先问：

> 当前这个事实是否真的需要新增验证？

只有存在 changed fact、Live Uncertainty、明确 Acceptance、Confirmed Defect regression 或达到门槛的 risk 时，才增加执行性验证。

Task：
- 定义 `Local Proof`，不默认等于 test。
- 优先 static / structural / existing evidence。
- 只有执行结果能改变当前判断时才跑 build / lint / unit / schema / migration / config 检查。
- 不默认跑全仓 tests。

Slice：
- 证明真实能力路径。
- 只覆盖 Slice 成立所必需的关键行为，以及真正被触发的 failure / permission / external boundary。
- 不为“负向覆盖完整”人为制造无关失败路径。
- 不复制 Task 的局部 proof。

Stage：
- 证明 Stage Outcome、Acceptance、Direct Regression、适用 Operational Obligations 和 Stop Rule。
- 不是全产品 regression suite。

### Verification Authority

每项 proof / verification 必须由真正拥有证据能力的一方完成：

- `Agent`：build、test、schema、静态规则、Token / Component / State compliance 等机械事实。
- `Human`：UI 审美、视觉质感、人类体验、主观接受、需要真人操作 / 感知的检查。
- `External`：Agent 无权访问或必须由外部后台 / 第三方 / 审核系统确认的事实。

Blueprint 可以准备 Human / External 的最短检查步骤，但不得规划“Agent 自己推断后宣布通过”。

能由 Agent 机械证明的，也不得为了保险转交 Human。

### 9. Route Exceptions

规划阶段发现问题时只使用 `BLOCKED`。

#### Owner: Blueprint

Stage Contract 和架构都成立，只是当前 Task 拆分、顺序、Target、Verification Path 或 Reasoning Score 不合格。

若 Construction 发现一个标记为 Low / Medium 的 Task 实际需要重新设计状态、失败模型、contract 或方案路线，也归 `Owner: Blueprint`；Blueprint 重新关闭设计空间，不允许施工 Agent 自行升 High。

蓝图自己修正后重新 Dry Run，不需要向上游创造新状态名。

#### Owner: Architecture

继续规划需要改变：

- Stage Scope / Exit State
- Decision-n
- Domain Ownership / Semantic Authority
- core module / interface / data boundary
- dependency direction / public-internal boundary
- Provider / technology direction
- security / permission architecture
- consistency / compatibility / migration strategy
- Stage Operational Obligation
- Stage Acceptance

输出证据并回架构。

#### Owner: Product

继续规划需要决定：

- Product Outcome / Product Rule
- actor / ownership / permission 的产品语义
- irreversible user behavior
- business / commercial behavior
- user-visible failure semantics
- acceptance meaning

回 Product / 用户。

### 10. Dry Run

Dry Run 只检查**合同是否可执行**，不是新的开放式风险审计、bug hunting 或 edge-case brainstorming。

发布前，从真实 Entry State 机械模拟：

- 所有 Path / Symbol / Schema / Command 是否真实可解析。
- Prerequisite 是否在使用前成立。
- Task Output 是否满足后续 Input。
- Slice 是否形成真实纵向状态。
- UI / Client 是否没有被无理由拖到最后。
- Requirement / Acceptance / Decision / Preservation / Operational Obligation 是否有施工与 proof 落点。
- 每个 binding Atom 是否有真实施工覆盖与验证覆盖，且没有被弱化成技术代理。
- Implementation Shape 是否明确到施工 Agent 不需要重新决定 owner / authority / dependency / bypass。
- 所有 Task 是否复用已冻结 authority，而不是创建第二套等价逻辑。
- 每个 Task 是否都有合法 Upstream Basis。
- 每个 Task 的 Reasoning Score 是否 ≤10，且没有把未决设计问题留给 Construction。
- 每个 Delegation 是否通过 Independence / Workload / Compressibility / State Isolation / Added Value 与 Time Gate。
- 是否存在 deterministic tool / Root 直接完成更快，却仍创建 subagent 的负收益委派。
- defensive work 是否都有 Confirmed Defect / risk gate 依据。
- Direct Regression 是否克制在直接影响范围。
- Deferred / Non-Scope 是否没有被拉进施工。
- 高风险真实边界是否没有被全 Mock 掩盖。
- 是否存在明显重复验证。
- 运行义务是否与相关行为同步，而不是 Stage 尾部补。
- 最终路径是否达到 Exit State。
- Stop Rule 是否机械可判。

Dry Run 期间新想到的“万一”不能自动扩 Scope；必须重新经过 Hypothetical Risk Gate。

发现 Blueprint 自身缺口 → 修正。

发现 Product / Architecture 缺口 → `BLOCKED`。

合同可执行且 READY 条件已满足后停止继续找新工作。

## Completion Gate

只有同时满足以下条件才输出：

`READY`

- 上游 Stage Contract 有效。
- Repository Entry State 已验证。
- 没有未决 Product / Architecture Decision。
- Scope 只包含 Current Stage 授权工作。
- 每个 Requirement / Acceptance / Architecture Obligation 都有施工落点。
- Current binding Atom 施工覆盖与验证覆盖为 100%。
- Implementation Shape 已明确 Current Stage 的 Ownership、Required Reuse、Allowed Dependency、Forbidden Bypass 与 Expected Change Boundary（适用项）。
- 没有未批准的新长期 Domain / Module / Semantic Authority / dependency direction。
- 每个 Planned Task 都有上游依据。
- 用户型工作被组织为早期真实纵向 Slice。
- 每个 Task 都有精确 Target、Actions、Local Proof、Done When；Local Proof 不强制等于新测试。
- 每个 Task 都已编译为 `Reasoning: Low | Medium`，Score ≤10；Execution Contract 不存在 High / XHigh Task。
- Goal / contract / state / failure / ordering / repository truth / proof strategy 等关键设计空间已在施工前关闭。
- 默认施工路径是 Root 直接完成；所有 Subagent Delegation 均有明确新增价值与非负 Time Impact，或属于明确的 Critical independent verifier 例外。
- 不存在 recursive spawn、机械命令 agent 化、共享状态高冲突委派或“为了分工而分工”。
- Execution Graph 可执行。
- 验证三层分工清楚且无明显重复。
- Confirmed Defect 已规划根因修复；达到门槛的风险已有相称处理；假想低分风险未被编译成工作。
- 高风险真实依赖使用了足够的真实验证。
- Triggered Operational Obligations 已落到相关施工位置。
- Preservation / Direct Regression 有最小充分证据。
- Explicit Non-Scope 保持在执行图外。
- Dry Run 可从 Entry State 到 Exit State。
- Stop Rule 可机械判断，READY 后不存在无 Trigger 的继续 hardening / testing / scope expansion。
- Execution Contract 内没有废弃 Task、失效占位或平行合同。

否则输出：

`BLOCKED`

并给出单一当前阻塞点；多个缺口可以一起列出，但按依赖顺序排序，不制造新的状态对象。

## Execution Contract 输出结构

每个 Stage 只维护自己那一份：

`docs/blueprint/stages/Stage-<N>.md`

推荐结构：

```text
# Stage-n — Execution Contract

## 1. Authority
## 2. Objective
## 3. Entry State
## 4. Target State
## 5. Scope  # 含 Implementation Shape
## 6. Traceability
## 7. Slices
## 8. Execution Graph
## 9. Tasks
## 10. Verification
## 11. Exception Routing
## 12. Completion
```

详细字段见 `references/docs-spec.md`。

## UI Handoff 协作

若当前 Stage 已存在正式 UI System / UI Handoff：

- Blueprint 必须把已确认的 Structure / Component / State / Interaction / Motion / Accessibility 约束编译进相关 Task。
- 不允许 Construction Agent 在 Task 中重新设计全局 UI 语言。
- UI mechanical checks 可以进入 Agent proof。
- Human-only 的视觉 / 审美验收只写最短检查入口，不写成 Agent PASS 条件。

若不存在正式 UI Handoff：

- 只规划 Functional UI。
- 保证真实能力可进入、可操作、必要状态可见、真实结果可见。
- 不为“顺便做漂亮”扩大当前 Stage。

## Handoff

状态为 `READY` 后交给 Construction Agent。

施工 Agent 应：

- 按 `Slice-n` / `Task-n` 的真实依赖推进，而不是机械假设全程串行。
- 按 Task 标记的 `Reasoning: Low | Medium` 执行；Reasoning 是施工思考上限，不是建议继续探索的邀请。
- Low Task 不进行开放式搜索 /重设计；Medium Task 只做冻结边界内的局部判断。
- 如果 Medium 仍不足以唯一推进，不自行升 High，停止并回 `BLOCKED`。
- 默认 Root 自己完成 Task；没有 Blueprint 明确 `Delegation` 时，不因复杂、文件多或想并行而自行 spawn。
- 有 Delegation 时严格遵守 Scope / Deliverable / Read-Write boundary / Fan-in；Child 不得递归 spawn。
- **Stay within the current Task**：Human feedback 可以修正、澄清当前 Task，但不得扩张当前 Task 边界，也不得因此提前施工后续 Task。
- 能用确定性工具完成的工作直接用工具，不创建 Agent。
- 遵守 Architecture / Engineering Standards。
- 遵守 Execution Contract 的 Implementation Shape：复用指定 owner / authority / public path，不绕过边界，不创建第二套等价业务规则。
- 未经 Architecture 明确授权，不自行新建长期 Domain / Module / Semantic Authority 或改变 dependency direction。
- 开工前读取 `Parallel Work Recommendation`。
- 若当前存在 `parallel-safe` 工作，先用人话告诉人类：建议同时开几个窗口、各窗口领取哪些 `Task-n / Slice-n`、何时回主线合并。
- 若人类只开一个窗口，仍可按同一 Execution Graph 顺序完成，不影响正确性。
- parallel-safe Task 各自完成局部 Local Proof，并保持独立 commit boundary。
- fan-in 后只在确有 Live Uncertainty / Acceptance 需要时运行一次 Slice Capability Test，不让每个并行 Task 重复跑整条能力链路。
- 已触发 Operational Obligation 随相关行为同步实现。
- 不因某个 Task 失败自行改变产品或架构。
- Slice 真实能力未成立时，不继续依赖该 Slice 的后续扩建。

Stage Verifier 后续以：

`Product binding Atoms → Architecture Ownership / Authority → Stage Contract → Execution Contract / Implementation Shape → Implementation → Evidence`

为主链验收。

Blueprint 不需要为 Verifier 预先制造大量 Evidence ID；验证位置和可重复步骤清楚即可。

## 按需加载 References

- 文档结构与合同字段：`references/docs-spec.md`
- Repository Intake：`references/repository-intake.md`
- 产品细化边界：`references/product-refinement-boundary.md`
- Slice / Task 设计：`references/slice-task-design.md`
- 多 Agent / 多人并行施工：`references/parallel-construction.md`
- 规划阶段防御性行为门禁：`references/planning-guardrails.md`
- Task 思考强度编译：`references/reasoning-policy.md`
- Subagent 委派准入：`references/delegation-policy.md`
- 验证与测试分层：`references/verification.md`
- Observability / Operations 落位：`references/operational-obligations.md`

不要默认一次读完所有 reference。只在对应问题出现时加载。

## 最终原则

蓝图的质量还取决于：产品语义是否无损传递、已有 authority 是否被正确复用、模块边界是否在施工前已经明确、Builder 是否无需临场发明新的长期结构。

蓝图的质量不取决于：

- Task 数量多。
- 文档特别长。
- 每个 Task 字段特别多。
- 测试跑得特别久。
- 每种 Observability 都有一栏。
- 所有实现细节都提前写成代码级伪实现。

而取决于：

> 施工 Agent 能否基于真实仓库，从当前 Stage 的 Entry State 沿唯一已批准路径完成建设，并以最小充分证据证明每个纵向能力和最终 Stage Outcome 成立。

**准确、可执行、早集成、少重复，是本 skill 的核心。**

> 不把模型自己的焦虑编译成项目工作量。

> 假想问题先证明，真实 Bug 修根因；没有新的不确定性就不要增加验证，已经足够 READY 就停止。

> Blueprint 用高强度思考关闭设计空间；Construction 只接收 Low / Medium Task。需要 High 的 Task 不是“重要”，而是“还没规划完”。

> 默认单 Agent 连续施工；只有能证明新模型上下文带来明显新增信息价值、独立证据或真实 wall-clock 收益时才委派。

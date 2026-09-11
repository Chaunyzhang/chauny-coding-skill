---
name: no-pitfall
display_name: 不踩坑
description: 施工与日常仓库工作的行为底线。与 Construction Blueprint 配合时按当前 Stage / Slice / Task 的 Execution Contract 施工；没有蓝图时按当前明确任务、项目规则和真实仓库工作。防止猜测、旁路、越权、Scope 漂移、数据损坏、错误重试、验证失真、假完成和历史方案残留。
---

# 不踩坑

## 定位

本 Skill 是施工行为底线，不决定“产品做什么”或“架构怎么设计”。

上游权威决定目标：

`Product Definition → Stage-n Contract → Execution Contract → Implementation → Evidence`

本 Skill 约束执行：

> 已经决定要做的事情，必须在真实仓库中正确、安全、可验证地完成；不得用猜测、旁路、降级、伪造证据或擅自改设计代替正式要求。

34 条雷点是长期经验资产，全部永久有效。永久有效不等于每个 Task 都逐条激活；只有触发条件成立的雷点才产生额外工作。完整正文见 `references/all-pitfalls.md`。

任何重构都不得静默删减或弱化其中任意一条；强化既有问题域时优先修改原雷点，避免重复编号。

## 反模型本能门禁

当前模型容易把“认真”误解成更多防御、更多测试、更多自我审计。施工前与施工中优先执行以下判断：

1. **先分类问题**：这是已有证据的 `Confirmed Defect`，还是只有推演的 `Hypothetical Risk`？
2. **真缺陷修根因**：Confirmed Defect 追到 invariant / ownership / source of truth / state / boundary 的正确层级，不用 guard / fallback 掩盖。
3. **假想风险先证明**：没有证据的风险先按 `Severity × Evidence-backed Likelihood` 评估，未达门槛不增加代码或测试。
4. **验证需要 Live Uncertainty**：每次新增检查前，必须说清“当前不知道什么”以及“失败后会做什么不同”。
5. **充分证据后 STOP**：Outcome 已成立且无 blocker 时，不继续 hardening、重跑测试或搜索额外工作。
6. **不越权验收**：Agent 只宣布自己有证据能力与裁决权的事项通过；UI 审美、主观体验、真机感知等按项目规则交 Human / External Authority。

这组门禁不是降低质量：

> **假想问题要克制；真实问题要修彻底。**

## 两种工作模式

### Blueprint Mode

当存在当前有效的 `docs/blueprint/stages/Stage-<N>.md` 或等价 Execution Contract 时使用。

施工权威顺序：

1. 当前用户明确指令。
2. Current `Stage-n` Contract。
3. 当前 Execution Contract。
4. 适用 Architecture / Engineering Standards。
5. Repository Reality。

执行单位：

`Stage-n → Slice-n → Task-n`

每次只施工当前授权 `Task-n`，达到它的 Exit / Verification 后再进入后续 Task。

不得自行：

- 改 Stage Scope。
- 改 Requirement 产品语义。
- 改 Decision / Architecture Invariant。
- 重排会改变 Stage 结果的关键施工路线。
- 跳过蓝图要求的真实集成或 Operational Obligation。
- 因发现“顺手可以优化”而扩大当前 Task。

### General Work Mode

没有 Execution Contract 时，用于：

- bug fix
- refactor
- debugging
- configuration
- migration
- dependency / repository change
- test repair
- 日常维护

权威顺序：

1. 当前用户明确任务。
2. 项目权威文档与工程规范。
3. 真实 Repository / System Reality。

没有正式蓝图不代表可以扩大范围或降低证据标准。

## 开工 / 恢复

开始或恢复前：

1. 确认当前授权任务或 `Task-n`。
2. 读取当前 Execution Contract（若有）。
3. 检查真实工作树与相关文件现状。
4. 识别用户已有改动、其他任务成果和未提交变化。
5. 确认适用 Architecture / Engineering Standards。
6. 确认本任务最小合理验证层级。
7. 如果计划依据、上游合同或仓库事实已变化，先重新对齐，不沿用失效计划。

不要求向用户朗读宣誓；规则必须体现在行为中。

## Blueprint Task 执行循环

每个 `Task-n` 默认按以下循环：

`Read Task → Verify Preconditions → Inspect Reality → Implement → Fast Check → Record Evidence → Exit`

### 1. Read Task

确认：

- Task 要改变什么。
- 精确 Path / Symbol / Schema / Config / Test。
- 前置依赖。
- Preservation / Direct Regression。
- 本 Task 触发的 Operational Obligations。
- Task Verification。

### 2. Verify Preconditions

前置 Task、schema、service、config、credential、environment 等不成立时，不伪装继续。

先判断：

- Blueprint 内可以解决 → 当前范围内修正。
- 蓝图拆法 / 落点本身错误 → 回 Construction Blueprint。
- 产品语义缺口 / Product Definition 改变 → `product`。
- 架构 / Provider / Interface / Data / Security 决策问题 → `chief-architect`。

### 3. Inspect Reality

不要只看目标文件。

按变化类型检查实际 caller、data flow、state flow、side effect、tests、generated source、config 和 external boundary。

### 4. Implement

只做当前 Task 成立所必需的改动。

严格遵守 `references/all-pitfalls.md`。

### 5. Fast Check

Task 默认只做最便宜且足以发现当前改动错误的检查。

这些是候选手段，不是每个 Task 的固定清单：

- affected target compile
- lint / typecheck
- focused unit test
- schema / structure validation
- narrow deterministic command

只有存在当前改动引入的 Live Uncertainty 时才运行对应检查；已有等价证据且实现未变化时不重复。不得因为“更保险”让每个小 Task 重跑全量系统验证。

重平台例外（iOS）：编译与单测运行本身可能超出 Task 预算，不属于 agent 的默认 Fast Check。Agent 优先做代码级静态 / 结构检查；编译、跑测、真机按项目平台规则在最早有意义的 Slice / Stage 聚合，并复用现有增量构建状态。不得把“每个 Task 人类编译一次”重新变成固定流程税。

### 6. Record Evidence

只有实际运行、实际观察到的结果才能声称完成。

区分：

- Verified
- Failed
- Not Run
- Environment Blocked
- Inferred

### 7. Exit

Task 成立后才能进入依赖它的后续 Task。

失败时先定位，不通过扩大修改范围或无界重试推进。

## Slice 与 Stage 验证

与 Construction Blueprint 使用同一验证分层：

### Task — 简单测

证明当前改动本身没有明显错误。

### Slice — 能力功能测

证明一个真实能力路径已经连接成立。

可能包括：

- real UI / client path
- real persistence
- real API / service boundary
- real sandbox provider
- migration exercise
- permission behavior
- Operational Obligation evidence

### Stage — 模块测 / Hands-on Acceptance

证明 Current Stage 的结果与直接受影响的既有行为一起成立。

核心原则：

> 同一事实只在最便宜且足够的层级证明一次。

**推送与 CI：** Task 完成只做本地提交，不推送、不触发 CI、不等待 CI 结果；每个 Slice 收口一次性 push，触发一轮 CI，报错在收口统一处理。CI 属 Slice 级验证，不属 Task。

**真机：** agent 不 build、不 install、不碰真机；真机验证由 agent 在每个 Slice 收口出「测什么 / 看到什么算过」清单，用户自己 Run 自己测。

不要把同一断言在 Task、Slice、Stage 重复跑三遍。

但也不能拿 Task 局部绿灯冒充真实 Slice / Stage 成立。

## 高风险即时验证

以下三类即使会增加一点 Task 成本，也不得拖到最后：

1. **Money / Quantity Correctness**
   - 金额、数量、计费、余额、库存等。
2. **Database Migration**
   - 旧状态 → 新状态、读写兼容、回填、失败恢复。
3. **Permission / Visibility**
   - 谁能看、谁能改、禁止路径、敏感边界。

其他真实环境验证按 Slice / Stage 合理聚合。

## Operational Obligations

No Pitfall 不重新定义 Observability 或运行体系。

只执行上游 Stage / Execution Contract 已触发的义务，例如：

- Diagnostic / Structured Logging
- Product / Business Events
- Error / Crash Tracking
- Metrics
- Tracing
- Audit / Security Events
- Backup / Recovery
- Alerting
- External Service evidence

规则：

- 本 Task 改变相关行为且合同要求同步落地 → 同 Task 完成。
- 没触发的类型不要为了填表额外施工。
- 真实 Sink / Console / sandbox 验证优先在最早有意义的 Slice 做一次，不要求每个 Task 重复。
- Mock 只能证明 Mock 覆盖范围，不能冒充真实外部边界。

## 升级路由

### Blueprint 自己处理

- 文件 / symbol 落点。
- 已冻结架构内的局部实现选择。
- 测试放置。
- 现有工程惯例。
- 低成本、可逆、不改变产品或架构语义的实现细节。

### 回 Construction Blueprint

当真实仓库证明：

- Task 顺序不成立。
- Change / Creation Set 错误。
- Task 粒度导致无法安全施工。
- 已冻结 Stage 在当前仓库需要重新拆 Slice / Task。
- Execution Contract 与现场现实存在施工级冲突。

### 回 Product

当不同答案会改变：

- actor
- ownership
- permission / visibility
- state / lifecycle
- irreversible behavior
- business rule
- user-visible failure / recovery
- acceptance outcome
- external product promise

不要把按钮、文案、普通 UI 或代码组织问题回 Product。

若发现需要改变 Product Definition 本身，同样回 Product；由 Product 更新 Product Definition / Product Atoms 后，再由 Chief Architect 重新裁决。

### 回 Chief Architect

当继续施工需要改变：

- Stage Scope / Exit / Acceptance
- Decision-n
- Architecture Invariant
- interface semantics
- data ownership / consistency
- security boundary
- Provider / technology direction
- migration / compatibility strategy

## 雷点应用导航

34 条始终具有约束力，但不构成每个 Task 的 34 项 checklist。下面只是当前阶段高概率 Trigger 导航。

### 开工 / 恢复重点

`1, 2, 3, 4, 8, 9, 10, 19, 20, 21`

### 普通 Task 施工重点

`3, 5, 6, 7, 8, 9, 10, 15, 18, 30, 31`

### 数据 / 外部副作用重点

`11, 12, 13, 14, 15, 17`

### Debug / Failure 重点

`2, 6, 19, 21, 22, 23, 27, 30, 31, 32`

### Verification 重点

`16, 17, 18, 23, 24, 29, 32, 33, 34`

### 收尾 / 交接重点

`24, 25, 26, 28, 33, 34`

完整规则始终以 `references/all-pitfalls.md` 为准。

## 完成规则

不能因为：

- code written
- compile passed
- CI green
- mock green
- TODO written
- logger / track 调用存在

就声称任务完成。

只能根据当前合同要求和实际证据判断。

Blueprint Mode 下：

`Task Complete ≠ Slice Complete ≠ Stage Complete`

完成当前授权范围并取得充分证据后必须停止；继续 hardening、测试、重构或搜索额外问题需要新的 Trigger。不得对没有证据能力或裁决权的事项自行宣布通过。

## 最终原则

先确认事实，再修改系统。

按正式契约完成当前范围；正确性、安全、数据和架构边界保持完整。

测试成本与风险匹配：小步快速检查，真实能力按 Slice 验证，Stage 做最终结果与直接回归。

所有“完成”都以实际证据为依据；假想风险不能冒充缺陷，真实缺陷必须修根因；所有超出当前授权或 Agent 裁决能力的结论回到正确的 Authority。

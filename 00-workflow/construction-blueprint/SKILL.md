---
name: construction-blueprint
display_name: 施工蓝图
description: 当架构总设计师已经冻结当前 Stage Contract，需要在编码前为施工 Agent 生成一份确定性、基于真实仓库、按持续纵向集成与同步可观测性推进，并能通过真实产品检查点、Observability Evidence 与用户上手验收证明结果成立的 Execution Contract 时使用。
---

# 施工蓝图

# 执行导航地图（先读）

本节不是完整规则，而是让 Agent 在进入长文档前先建立施工全局地图。正文规则与上游 Stage Contract 仍是权威来源。

## A. 全程必做

施工蓝图从开始到 `READY` 必须依次完成：

1. `Restore Authority & Reality`：读取 Current Stage Contract、Architecture Handoff、Observability Contract 与真实 Repository State。
2. `Compile Target State`：把 Stage Exit State、Acceptance、Preservation、Regression 与 Observability Delta 翻译成可执行 Repository / Runtime 条件。
3. `Build Scope & Traceability`：建立 Change / Creation / Observability / Preservation / Regression / Deferred Sets，并完成双向 Requirement 与 Observability Traceability。
4. `Build Integration Slices`：优先形成最薄真实纵向链路；每个 Slice 同时定义 Product Checkpoint 与六类 Observability Type Coverage / Evidence。
5. `Compile Tasks`：每个 Task 都写明 `Behavior Delta`，并逐类检查六种 Observability；运行时行为与必要观测必须同 Task 完成。
6. `Verify Incrementally`：每个运行时 Task 必须先通过功能 Verification 与 Observability Verification，才允许解锁依赖它的后续 Task。
7. `Verify Stage Observability`：每个 Stage 至少有一个明确 `Observability Step / Checkpoint`，证明 Console、远程 Sink、Crash / Error 与其他适用观测链路真实工作。
8. `Dry Run & Gate`：从 Entry State 机械走到 Stage Exit State；存在未解决产品 / 架构决策、观测盲区或不可验证 Sink 时不得输出 `READY`。

## B. 六类 Observability 执行地图

蓝图不得把“埋点”理解为单一 analytics。每个 Task 必须逐类检查以下六种能力：

| 类型 | Blueprint 默认规则 | 典型验证 |
|---|---|---|
| `Diagnostic / Structured Logging` | **运行时 Task 必做** | 本地真实运行可实时看到；iOS / macOS 至少在 Xcode Console 看到关键 start / state / success / failure 与必要 context |
| `Product / Business Events` | **有产品 / 业务行为时必做**，并服从 Stage Contract | SDK / Client 已真实初始化；触发真实路径后事件到达目标后台并可查询 |
| `Error / Crash Tracking` | **存在可运行 App / Service 时必须承载并保持可验证** | Error / Crash 通道已初始化；受控 error / crash 能形成可查询 stack / build / environment 证据；不得由业务 `*.failed` event 代替 |
| `Metrics` | **触发条件成立后必做** | 指标真实产生，可读 / 可查询，label / dimension 与 Stage Contract 一致 |
| `Tracing` | **跨边界 / 异步链路触发后必做** | trace / span / correlation 可串起真实调用链并定位耗时 / 失败边界 |
| `Audit / Security Events` | **敏感操作触发后必做** | 真实 Auth / Permission / Admin / Payment / 敏感变更产生符合 schema 的可授权检索记录 |

Task 逐类状态使用：

`ADD | CHANGE | PRESERVE | N/A`

其中：

- `ADD / CHANGE`：本 Task 必须包含明确 Instrumentation Actions 与真实 Observability Verification。
- `PRESERVE`：已有能力不需要新增埋点，但本 Task 必须说明如何不破坏既有观测链路；必要时加入 Regression Evidence。
- `N/A`：必须写明理由；不能用 `N/A` 逃避上游已经标记 `REQUIRED` / `REQUIRED WHEN APPLICABLE` 且触发条件已成立的能力。
- 凡 Task 新增或改变运行时行为，`Diagnostic / Structured Logging` 不得为 `N/A`。

## C. Stage / Task 硬门禁

- 每个 Stage 至少存在一个非 `NONE` 的 `Observability Delta` 和一个明确、可执行、可重复的 `Observability Step / Checkpoint`。
- 不允许“功能先做完，Stage 尾部统一补日志 / events / crash / metrics / tracing / audit”。
- 每个运行时 Task 必须做到：`Behavior Change + Diagnostic Logging + Applicable Observability + Verification` 同 Task 闭环。
- `logger.*`、`track()`、`capture()`、metric / span 调用写进代码，只证明 instrumentation code 存在，不证明 Observability 完成。
- 真实完成必须验证：初始化、配置、环境、Console 输出或网络传输、接收端 / Sink、查询 / 检索路径实际成立。
- Product Events、Diagnostic Logging、Error / Crash Tracking 是不同能力，不得互相冒充。
- 上游 Observability Contract 缺失、六类状态不完整或要求与 Repository Reality 冲突时，蓝图不得自行降级，必须 `PLAN_BLOCKED_ARCHITECTURE`。

## D. 最终 Execution Contract 必须让施工 Agent 一眼知道

- 当前 Stage 要形成什么产品 / 系统结果；
- 最早哪个 Slice 会出现真实 End-to-End Path；
- 每个 Task 改什么、在哪改、怎么验证；
- 每个 Task 六类 Observability 分别是 `ADD / CHANGE / PRESERVE / N/A`；
- Xcode / Console 应该看到什么关键日志；
- 哪些 Product Events 应该在什么后台出现；
- Error / Crash 通道如何证明真实接通；
- Metrics / Tracing / Audit 在什么触发条件下必须出现；
- 哪个 Observability Checkpoint 证明 Stage 不存在关键黑盒；
- 什么状态满足后才可以进入下一个 Task / Slice 与最终 `READY`。

---

# 最高优先级施工原则

以下原则高于后续任务拆分、依赖排序、测试组织与局部效率优化。发生冲突时，以本节为准。

## 1. 先让真实产品成立，再继续扩建

对于包含用户界面、客户端或真实产品交互的 Stage，施工必须尽早形成最薄的真实端到端链路，并在后续施工中持续保持产品可运行、可交互、可观察。

默认禁止：

`Backend → Database → Services → Frontend → Final Integration`

默认采用：

`Thin Vertical Slice → Real Integration → Product Checkpoint → Expand → Re-integrate → Product Checkpoint → Stage Acceptance`

即：

`最薄纵向切片 → 真实集成 → 产品检查点 → 扩展 → 再集成 → 产品检查点 → 阶段验收`

不得把跨层集成推迟到 Stage 尾部。

## 2. Stage 按 Integration Slice 施工，不按技术层批量施工

一个 Stage 可以包含很多 Task，但这些 Task 必须组织进一个或多个 `Integration Slice`。

每个 Integration Slice 必须形成一个已经连接起来、真实可运行的产品状态，而不是一组“分别完成、以后再组装”的零件。

典型 Slice 可以同时包含：

- 最小 UI / Client 交互
- 对应 API / Backend 行为
- 对应 Data / State 变化
- 必要 External Service
- Error / Loading / Failure 行为
- 真实集成验证

任务数量本身不是风险；**长时间不集成才是风险**。

## 3. CI PASS 不等于产品成立

Unit Test / Integration Test / CI / Typecheck / Mock 测试是必要工程证据，但不能替代真实产品路径。

对于用户型 Stage，至少必须证明：

`真实产品入口 → 真实用户操作 → 真实调用链 → 真实后端 / 服务 → 真实状态变化 → 真实可见结果`

如果主要产品路径仍依赖 Mock、stub、fake service，或者绕过真实入口，只能证明局部组件成立，不能证明 Stage Delivery 完成。

## 4. UI 是产品行为的一部分，不是最后的装饰层

当 Stage 的 Product Outcome 需要 UI / Client 才能被用户体验时，UI 必须进入早期 Integration Slice。

不得默认把 UI 安排在所有 Backend / Data / Service 工作完成之后。

以下产品问题通常只有接入真实 UI 后才能被验证：

- Loading / Pending 状态
- 错误反馈
- 旧状态 / 刷新
- 重复操作
- Enabled / Disabled 条件
- 页面跳转 / 返回状态
- 持久化结果是否真实可见
- Optimistic / Async 行为
- Timeout / 长任务状态
- Permission / Empty State
- 用户可见恢复行为

## 5. 每个 Integration Slice 都必须有 Product Checkpoint

每个 Slice 必须定义一个可重复执行的 `Product Checkpoint`，至少包含：

- `Product Entry`
- `Actor / Test Identity`
- `Preconditions`
- `Hands-on Steps`
- `Real Services Used`
- `Expected Visible Result`
- `Expected State / Persistence`
- `Required Failure Behavior`
- `Automated Evidence`
- `Observability Type Coverage`
- `Observability Evidence`
- `Mocks Allowed`
- `Slice Exit State`

Checkpoint 必须能够从真实产品入口证明当前 Slice 已经真实集成成立。

用户不必在每个 Slice 后亲自批准施工继续，但蓝图必须保证：任何 Slice 结束时，都存在一个可以直接上手验证的真实产品状态。

## 6. Stage 必须有最终 Hands-on Acceptance

对于用户型 Stage，Execution Contract 必须提供最终 `Hands-on Acceptance`。

它必须让非技术用户知道：

- 从哪里进入产品
- 使用什么账号 / 前置条件
- 做哪几个操作
- 应该看到什么
- 数据 / 状态应该如何保持
- 关键失败时应该看到什么

自动化证据不能替代最终 Hands-on Acceptance。

## 7. Technical-only Stage 是例外

如果 Current Stage 无法形成用户可体验的产品变化，只允许在 Stage Contract 已明确批准“纯技术前置 Stage”时继续。

该 Stage 必须同时满足：

- 是紧邻产品闭环的真实必要前置；
- 有明确、可验证的 Exit State；
- 明确下一哪个 Stage 会真实消费该能力；
- 不把多个原本可以纵向切开的产品能力连续拆成黑盒技术 Stage。

若 Current Stage 本应产生产品 Visible Delta，但真实仓库路径只能形成后端 / 数据库 / 基础设施黑盒变化，则：

`REPLAN_BLUEPRINT`

或：

`PLAN_BLOCKED_ARCHITECTURE`

不得自行把“内部完成”当成“产品完成”。

## 8. 失败的 Product Checkpoint 阻断后续扩建

如果某个 Slice 的真实产品路径失败：

- 不继续堆叠后续 Slice；
- 先定位当前 Slice 内的产品 / 集成 / 实现问题；
- 属于实现错误 → `LOCAL_FIX`；
- 属于蓝图顺序 / 落点问题 → `REPLAN_BLUEPRINT`；
- 属于 Stage / Architecture / Product 语义问题 → 向上游升级。

目标是尽早暴露真实产品问题，而不是把问题积累到 Stage 80%–90% 时一次爆发。

## 9. 六类可观测性必须随 Task 同步施工

Observability 不是 Stage 尾部的补充任务。Blueprint 必须把上游 Stage Observability Contract 增量化到具体 Integration Slice 与 Task，并完整承载六类能力：

1. `Diagnostic / Structured Logging`
2. `Product / Business Events`
3. `Error / Crash Tracking`
4. `Metrics`
5. `Tracing`
6. `Audit / Security Events`

必须遵守：

- 每个 Stage 至少包含一个明确、可验证的 `Observability Step / Checkpoint` 与非空 `Observability Delta`。
- 每个 Task 都必须声明 `Behavior Delta`，并提供六类 `Task Observability Matrix`。
- 六类状态只能使用 `ADD | CHANGE | PRESERVE | N/A`；`N/A` 必须说明原因。
- 凡 Task 新增或改变运行时行为，`Diagnostic / Structured Logging` 必须在同一个 Task 内完成，不得写 `N/A`。
- Product / Business 行为、可运行 App / Service、跨边界 / 异步链路、敏感操作等触发条件成立时，对应 Product Events、Error / Crash、Metrics、Tracing、Audit / Security 必须按 Stage Contract 在同一施工增量落实或明确 `PRESERVE` 已有基线。
- 不得把多个前序 Task 的必要 instrumentation 集中推迟到 Stage 尾部的“统一补埋点”Task。
- Task 完成意味着“行为完成 + 必要观测完成 + 观测链路真实可见 + 验证完成”。
- 纯文档、纯静态配置或其他确实不产生运行时行为变化的 Task，可以让六类均为 `N/A` 或仅 `PRESERVE`，但必须逐类说明原因 / 保持义务。
- 一个 Stage 不得所有 Task 都没有 Observability 建设或验证增量。

### Diagnostic / Structured Logging 的 Task 规则

对于任何新增或改变运行时行为的 Task，至少规划与该 Behavior Delta 相称的诊断日志：

- 关键开始 / 入口；
- 关键状态变化或阶段边界；
- 成功 / 完成；
- 失败 / exception / timeout / retry / fallback（适用时）；
- 足够定位问题但不泄露 Secret / 未批准 PII 的 context / correlation。

移动端 / Apple 平台施工必须明确本地真实运行如何在 Xcode Console / 平台 Console 看到这些日志。只写日志 API、不验证 Console 可见，不算完成。

### Product / Business Events 的 Task 规则

当 Task 新增或改变上游定义的产品 / 业务语义时：

- 使用冻结的 event name / schema / context；
- 明确 SDK / Client 初始化依赖和环境配置；
- 真实触发产品路径；
- 验证事件到达目标 Analytics Sink 并可查询；
- 不得把本地 console print 当作 Product Event 已送达证据。

### Error / Crash Tracking 的 Task 规则

可运行 App / Service 必须承载上游确定的 Error / Crash Tracking 基线：

- 明确 SDK / 平台通道初始化落点；
- 保留 build / version / environment / device / stack / correlation 等必要上下文；
- 对可捕获错误与未捕获 Crash 的责任边界写清；
- 使用受控验证方式证明 Error / Crash 接收端真实工作；
- Product Event 中的 `*.failed` 不能替代 Crash / Error Tracking。

Task 如果不新增 Crash instrumentation，可以标 `PRESERVE`，但必须确保本 Task 不破坏全局 Crash / Error 上报和必要 context。

### Metrics / Tracing / Audit 的触发规则

- `Metrics`：当 Task 引入或改变后端、队列、外部依赖、性能 / 容量 / SLA / 成本敏感行为时，按 Stage Contract 同 Task 添加 / 修改或验证指标。
- `Tracing`：当 Task 跨模块、API、Job、External Provider、异步边界或存在难以靠单点日志定位的链路时，按 Stage Contract 同 Task 添加 / 修改 trace / span / correlation。
- `Audit / Security Events`：当 Task 涉及 Auth、Permission、Admin、Payment、Secret、敏感数据或关键权限状态变化时，按 Stage Contract 同 Task 添加 / 修改审计 / 安全记录。

### Observability 真完成规则

以下均不构成完成证据：

- 代码里存在 `logger.*`；
- 代码里存在 `track()`；
- 代码里存在 `capture()`；
- 注册了 metric / span 但没有真实数据；
- SDK dependency 已安装但没有初始化；
- 配置变量存在但运行时没有加载；
- 测试只 mock 掉 telemetry client。

必须证明与当前类型相匹配的真实链路：

`Trigger → Instrumentation → Initialization / Runtime Config → Output / Transport → Sink / Console → Inspectable Evidence`

原则：

`Build a little → observe a little → verify a little.`

即：

`做一点，就同步获得一点可观测性；任何新增运行时行为都不得先进入黑盒状态。`

# 目的

把已经冻结的 Stage Contract、已批准架构决策、真实仓库状态、Scope 边界与验收要求，编译成一份确定性的 Execution Contract，使施工 Agent 可以机械执行，而不需要在施工时重新做产品或架构判断。

蓝图只负责**编译已批准决策**，不创造新的产品决策或架构决策。

Execution Contract 只有同时满足以下条件才算完整：

- 所有施工时可能遇到的实施选择都已经解决；
- 每个 Task 都有确定的前置条件、动作、产出、验证与退出条件；
- 每个上游需求都可以追溯到具体施工工作与证据；
- Preservation、Regression、Architecture 与 Scope 义务全部可验证；
- 每种异常都有明确控制路径；
- Dry Run 能从 Entry State 走到 Stage Exit State，且过程中不需要新增产品、架构、Scope 或 Acceptance 决策；
- 用户型工作被组织为持续集成的纵向 Slice，而不是最后才把各组件拼起来；
- 每个 Integration Slice 都以真实 Product Checkpoint 结束；
- 每个用户型 Stage 都有可重复执行的 Hands-on Acceptance 路径。
- Stage Observability Contract 的六类能力已被映射到具体 Slice、Task 与 Verification Evidence；
- 每个 Task 都声明 Behavior Delta 与六类 Task Observability Matrix，运行时行为变更与必要观测同 Task 完成；
- 每个运行时 Task 的 Diagnostic / Structured Logging 都有本地实时可见验证；
- 所有 `ADD / CHANGE` 的远程观测类型都能证明初始化、传输 / 写入、Sink 与查询链路真实成立；
- 每个 Stage 至少存在一个明确的 Stage-level `Observability Step / Checkpoint`。

# 权限边界

Source of Truth 顺序：

`Product / Architecture → Stage Contract → Construction Blueprint → Implementation → Evidence`

施工蓝图只能在已经批准的边界内决定执行机械细节，包括：

- Task 拆分
- 仓库目标位置
- 执行顺序
- 依赖顺序
- 测试放置
- Migration 顺序
- Verification 放置
- 已冻结 Observability Contract 的具体 instrumentation placement、六类 Task 状态映射与验证落点

如果继续规划需要改变以下任何内容，蓝图无权自行决定：

- Product Outcome / Product Rule
- Accepted Requirement
- Stage Scope
- Stage Exit State
- Architecture Invariant
- Data Ownership / Lifecycle 语义
- Interface 语义
- Security / Permission 语义
- Transaction / Consistency 语义
- Acceptance 语义
- 已批准技术方向
- Stage Observability Contract 的六类 Type Matrix、最低覆盖范围、关键流程、必要 checkpoints、sink readiness、correlation 或 privacy / redaction 语义

遇到上述情况，结束规划并输出 `PLAN_BLOCKED`，回到 Architecture Director。

# 恢复与校验原则

- 开始或恢复规划时重新核对 Current Stage Contract、Architecture Handoff 与真实仓库状态；聊天历史不作为唯一事实来源。
- 仓库现实或上游 Contract 改变时，立即把受影响蓝图内容标记为失效并重新验证，不沿用旧路径推断新计划。
- 恢复后从权威文档（Stage Contract、Architecture 文档）与真实仓库重新验证后继续。

# 必需权威输入

开始规划前必须收集并对齐以下内容。

## Current Stage Contract

- Stage ID / Name
- Roadmap Position
- Accepted Requirement IDs
- Intent
- Entry State
- Exit State
- Visible Delta
- Decisions
- Authorized Scope
- Architecture Delta
- Architecture Invariants
- Preservation Set
- Deferred Set
- Acceptance Criteria
- Regression Set
- Escalation Triggers
- Stop Rule
- 上游已经定义的 Hands-on / 用户可见 Acceptance Intent
- 如适用，Technical-only Stage 标记
- Operational Obligations
- `Observability Type Matrix`：六类分别为 `REQUIRED | REQUIRED WHEN APPLICABLE | NOT APPLICABLE` 与依据
- Stage Observability Delta / Incremental Instrumentation Contract
- Stage 至少一个明确 `Observability Step / Verification`
- Diagnostic / Structured Logging：本地 / 开发运行时实时可见要求与关键 start / state / success / failure 覆盖
- Product / Business Events：关键事件、schema、SDK / client 初始化、环境配置与目标 Sink
- Error / Crash Tracking：接收端、初始化、stack / build / environment / correlation 与受控验证要求
- Metrics：适用指标、维度、阈值 / 查询方式（适用时）
- Tracing：trace / span / correlation 边界与传播要求（适用时）
- Audit / Security Events：敏感动作、schema、保留 / 检索与权限要求（适用时）
- Critical Flows / Failure Coverage
- Sink Readiness / Initialization / Runtime Configuration requirements
- Privacy / Redaction Rules
- Observability Verification Evidence requirements

## Architecture Inputs

- 相关 Architecture Spine
- 相关 ADR / Decision Log
- Architecture Director 的 Blueprint Handoff
- 当前适用的项目工程规则
- `OBSERVABILITY.md` 或等价 Observability Contract
- 六类 Observability Type Matrix、Sink Readiness、Incremental Instrumentation Rule 与 Stage-level Observability Step

## Repository Inputs

- 当前真实仓库状态
- 相关实现、caller、schema、migration、test、configuration 与 generated artifacts
- 当前项目已有实现模式
- 可用的 build、test、typecheck、migration、generation 与 inspection 命令

已批准上游决策是权威；Repository State 是执行现实。

权威与现实不一致时，规划前必须分类：

- 仓库细节与已批准决策兼容 → 吸收到蓝图；
- 已批准边界内存在实施路径歧义 → 蓝图负责消除；
- 存在上游产品语义或架构冲突 → `PLAN_BLOCKED`。

# 规划流程

## 1. 建立 Current State

确认经过验证的 Entry State：

- 与当前 Stage 有关的既有行为；
- 涉及的精确文件、symbol、interface、schema、test、command、generated artifact 与 convention；
- 受影响组件依赖；
- 当前 call / data / state / side-effect 路径；
- 适用 Architecture Invariants；
- Preservation Set 与 Regression Set 基线；
- 后续 Task 所依赖的仓库事实。
- 与本 Stage 相关的既有 `Diagnostic Logging | Product Events | Error / Crash | Metrics | Tracing | Audit / Security` 实现、初始化状态、sink / console 可见路径与 conventions；
- 既有 telemetry / error / crash SDK 是否真的初始化、运行时配置从哪里加载、不同环境如何区分；
- 现有 Console / Analytics / Crash / Metrics / Trace / Audit 数据如何检查；
- 已知 observability blind spots，以及哪些属于 Current Stage 必须消除。

必须使用精确 Repository Path 与 Symbol Name。

记录文档中的 Entry State 与真实 Repository Reality 之间的差异。

## 2. 建立 Target State

把 Stage Exit State 翻译成具体、可观察的 Repository 与 Runtime 条件：

- 新增或改变的能力已经成立；
- Visible Delta 已产生；
- 所需 Interface、Schema、State Transition 或 Artifact 已建立；
- 既有行为被保持；
- Architecture Delta 已实现；
- Acceptance Criteria 已满足；
- Regression Set 被保持；
- Deferred Set 仍在当前施工之外；
- Stage Stop Rule 已成立；
- 对用户型 Stage，真实产品入口可以直接暴露本 Stage 的 Visible Delta；
- Stage 拥有可重复执行的 Hands-on Acceptance 路径。
- Stage Observability Delta 已真实落地并可验证；
- 六类 Observability 已按 Stage Contract 得到明确的 `REQUIRED / REQUIRED WHEN APPLICABLE / NOT APPLICABLE` 落地结果；
- 所有运行时 Behavior Delta 都存在同步 Diagnostic / Structured Logging，并可在本地真实运行时实时看到；
- 所有 `ADD / CHANGE` 的远程观测能力都完成初始化 / runtime config / output or transport / sink / query 的真实链路验证；
- 新增或改变的关键运行时行为不存在已知 Critical Observability Blind Spot；
- 至少一个 Stage-level `Observability Step / Checkpoint` 可以重复执行。

Current Stage 完成与最终产品完成相互独立。

对于用户型 Stage：

**Repository 正确，但真实产品路径不工作，不是有效 Target State。**

## 3. 落实 Frozen Decisions

提取所有限制施工方式的已批准决策：

- Architecture placement
- Interface / Signature
- Data ownership / lifecycle
- Persistence behavior
- Error semantics
- Dependency choices
- Compatibility behavior
- Transaction / Concurrency / Consistency boundary
- Security / Permission semantics
- Migration strategy
- Test strategy
- Generation strategy
- Rollout / ordering constraints
- Observability Type Matrix：六类 required / conditional / N/A 状态
- Diagnostic / Structured Logging naming、level、context、Console 可见要求
- Product / Business Event naming、schema、SDK 初始化、环境与 Sink
- Error / Crash Tracking provider / channel、初始化、context、受控验证方式
- Metrics naming / dimensions / query requirements（适用时）
- Tracing / Span / Correlation propagation requirements（适用时）
- Audit / Security event schema、retention / access semantics（适用时）
- Sink Readiness / Runtime Configuration requirements
- Privacy / Redaction requirements
- Stage Incremental Instrumentation requirements

把这些决策转换成 Repository-level 的实施约束。

如果某个必需决策：

- 缺失；
- 相互矛盾；
- 或仍存在多个在产品 / 架构层面都合理的路径；

则输出 `PLAN_BLOCKED`，回到 Architecture Director。

## 4. 建立 Scope Sets

定义：

- `Change Set`：预计要修改的既有文件、目录、symbol、schema、configuration 或 test；
- `Creation Set`：施工后应该新增的文件、symbol、schema、migration、test 或 artifact；
- `Observability Set`：本 Stage 六类 Observability 分别必须 `ADD / CHANGE / PRESERVE / N/A` 的具体 logs、events、error / crash、metrics、traces、audit records、correlation、SDK / sink initialization、runtime config、schema、instrumentation points 与验证路径；
- `Preservation Set`：必须继续成立的既有行为、interface、data contract、invariant、文件或 runtime guarantee；
- `Regression Set`：必须继续通过的既有 test、journey、command 或 observable behavior；
- `Deferred Set`：已经识别但明确不属于 Current Stage 的要求。

尽可能使用精确的：

- Path
- Symbol
- Acceptance ID
- Requirement ID
- ADR ID
- Invariant ID

每一项 Planned Change 都必须属于 Current Stage Contract。

## 5. 建立 Requirement Traceability

Task 拆分前建立：

`Accepted Requirement → Stage Acceptance → Blueprint Task → Verification Evidence`

同时建立：

`Stage Observability Obligation → Observability Type → Blueprint Task → Observability Verification Evidence`

对每个 Accepted Requirement 与 Acceptance Criterion，明确：

- Implementation Responsibility
- Task Coverage
- Expected Evidence
- Preservation / Regression dependencies
- 六类 Observability Obligation / Status / Evidence dependencies

每个 Task 至少必须向上追溯到一个：

- Current-stage Requirement
- Acceptance Item
- Architecture Obligation
- Preservation Obligation
- Regression Obligation

每个 Current-stage Requirement 也必须向下追溯到至少：

- 一个 Task
- 一个 Verification Point

## 6. 建立 Integration Slices

拆 Task 之前，先把整个 Stage 切成尽可能小、但仍能形成真实纵向产品状态的 `Integration Slice`。

每个 Slice 必须定义：

- `Slice ID`
- `Product / System Outcome`
- `Real Product Entry`
- `Vertical Path`
- `Required Layers`
- `Real Dependencies`
- `Tasks`
- `Product Checkpoint`
- `Automated Evidence`
- `Observability Type Coverage`
- `Observability Evidence`
- `Slice Exit State`
- `Next Slice Dependency`

规则：

- 第一个真实 End-to-End Slice 必须尽可能早出现；
- 每个 Slice 集成其 Outcome 所需的最小 Client / UI、Backend、Data 与 External Service；
- 后续 Slice 必须在已经运行的产品路径上继续扩展，而不是等待最后统一集成；
- 用户型 Stage 不得存在一个很晚才出现的 `FINAL INTEGRATION` Task，并且它是第一次把之前独立完成的主要技术层连接起来；
- Component-level 的准备型 Task 只有在最近的下一 Slice 会立即消费时才允许存在；
- 如果两个或更多主要技术层在没有真实产品路径的情况下被大量独立完成，应重新切 Slice，除非 Stage Contract 已明确批准 Technical-only Construction；
- 每个 Slice 必须先通过 Product Checkpoint，再进入依赖它的后续扩展。
- 每个 Slice 必须逐类汇总本 Slice Task 的 `Diagnostic Logging | Product Events | Error / Crash | Metrics | Tracing | Audit / Security` 状态，并在 Slice 结束时提供可执行 Observability Evidence；
- 不得让一个 Slice 的必要 instrumentation 等待后续 Slice 才补齐。

Slice 只有在：

- 各层真正连接起来；
- 真实产品行为真正工作；

时才算完成。

`代码存在` ≠ `Slice 完成`

## 7. 建立 Dependency Graph

把每个 Integration Slice 再拆成有顺序的 Task。

一个合法 Task 必须：

- 产生一个可独立验证的状态变化；
- 有明确前置条件；
- 有受控的 Change Surface；
- 实现一个连贯 Requirement 或 Architecture Obligation；
- 为后续依赖 Task 提供完整输入；
- 以可观察 Verification Result 结束；
- 让 Repository 保持在有效中间状态。
- 声明 `Behavior Delta` 与六类 `Task Observability Matrix`；
- 每一类只能标记 `ADD | CHANGE | PRESERVE | N/A`，并为 `N/A` 提供理由；
- 若新增或改变运行时行为，则 `Diagnostic / Structured Logging` 不得为 `N/A`，且必须与行为实现同 Task 完成；
- 其余五类一旦被 Stage Contract 要求或触发条件成立，必须在同一施工增量 `ADD / CHANGE`，或明确 `PRESERVE` 已有有效基线；
- 以可执行的 Observability Verification 证明必要 signal 真实产生、Console / Sink 可见且可关联。

按真实依赖排序。

只有当以下内容互不依赖时，才可标记 `[parallel]`：

- Prerequisite
- Write Surface
- Generated Artifact
- Shared State
- Verification Dependency

## 8. 把 Task 编译成机械施工步骤

每个 Task 必须包含：

- `Task ID`
- `Slice ID`
- `Requirement Coverage`
- `Behavior Delta`
- `Task Observability Matrix`
- `Observability Delta`
- `Objective`
- `Prerequisites`
- `Targets`
- `References`
- `Inputs`
- `Actions`
- `Instrumentation Actions`
- `Outputs`
- `Verification`
- `Observability Verification`
- `Expected Result`
- `Exit Condition`

`Slice ID`：标明该 Task 正在推进哪个 Integration Slice 的真实产品状态。

`Requirement Coverage`：列出该 Task 服务的精确 Requirement ID、Acceptance ID、Invariant ID、Preservation ID 或 Regression ID。

`Behavior Delta`：写明该 Task 新增或改变的运行时行为；若确实没有运行时行为变化，写 `NONE` 并说明原因。

`Task Observability Matrix`：六类逐项填写 `ADD | CHANGE | PRESERVE | N/A` 与理由。运行时行为变化时 `Diagnostic / Structured Logging` 不得为 `N/A`；不得把上游已要求或已触发的类型写成 `N/A`。

`Observability Delta`：汇总本 Task 实际 `ADD / CHANGE` 的六类观测增量，以及 `PRESERVE` 的关键既有观测义务。不得用“增加埋点”这种统称代替逐类说明。

`Targets`：写明精确 File、Symbol、Schema、Migration、Configuration、Test 或 Generated Artifact。

`References`：写明约束该 Task 的精确 Repository Artifact、ADR、Interface、Test 或 Convention。

`Inputs`：写明施工开始前必须存在的具体 Repository State。

`Actions`：按顺序写状态改变操作。每个 Action 只描述一个操作，并提供足够细节，使施工 Agent 只能沿唯一已批准路径实施。

`Instrumentation Actions`：按六类明确具体落点与动作：

- Diagnostic：File / Symbol / handler / boundary、log level、message / event key、context、成功 / 失败覆盖；
- Product Events：event name / schema、调用落点、SDK initialization dependency、environment / sink；
- Error / Crash：capture / crash channel、初始化落点、stack / build / environment / correlation；
- Metrics：metric name、type、labels / dimensions、记录边界；
- Tracing：span / trace boundary、parent / child、correlation propagation；
- Audit / Security：audit event、actor / target / action / outcome、敏感字段处理与写入位置。

不得用“补充日志”“增加埋点”“接入监控”等泛化描述。

`Outputs`：描述 Task 完成后真实产生的 Repository 与 Runtime State。

`Verification`：写出可执行 Command、Test Selector、Inspection、State Check、Migration Check、Generation Check 或确定性 Manual Procedure。

`Observability Verification`：必须按本 Task 的 `ADD / CHANGE / PRESERVE` 类型分别写出真实证据：

- Diagnostic Logging：运行真实路径，明确在哪个 Console（Apple 平台至少 Xcode Console / 平台 Console）看到哪些关键日志与字段；
- Product Events：真实初始化 SDK / client 后触发路径，确认事件到达目标后台并可查询；
- Error / Crash：确认通道初始化，使用上游允许的受控 error / crash 验证方式取得可查询 stack / build / environment 证据；
- Metrics：触发真实行为后确认 metric value / labels 可读或可查询；
- Tracing：确认 trace / span 真实生成并可通过 correlation 串起调用链；
- Audit / Security：执行真实敏感动作后按授权路径检索对应审计记录；
- PRESERVE：运行 regression / inspection 证明既有观测链路未被破坏。

不能只证明 instrumentation 调用存在、dependency 已安装、配置变量已声明或 mock telemetry test 通过。

`Expected Result`：写出精确、可观察的预期判定。

`Exit Condition`：写明什么状态成立后，才能解锁依赖它的后续 Task。

若 Task 改变运行时行为，则其 Exit Condition 必须同时包含 Diagnostic Logging Verification PASS，以及所有 `ADD / CHANGE` / 必要 `PRESERVE` 类型的 Observability Verification PASS；否则 Task 不得解锁后续依赖。

## 9. 定义 Acceptance Matrix

把完整 Stage Contract 映射到 Verification。

每一项记录：

- `Acceptance ID`
- `Type`
- `Requirement / Obligation`
- `Requirement Source`
- `Blueprint Task`
- `Evidence Source`
- `Verification Method`
- `Pass Condition`

`Type` 只能是：

- `DELIVERY`
- `ARCHITECTURE`
- `PRESERVATION`
- `REGRESSION`
- `SCOPE`
- `USER_REALITY`
- `OBSERVABILITY`

覆盖要求：

- 每个 Stage Acceptance Criterion → `DELIVERY`
- 每个 Current-stage Architecture Invariant obligation → `ARCHITECTURE`
- 每个 Preservation Set commitment → `PRESERVATION`
- 每个 Regression Set item → `REGRESSION`
- Current Authorized Scope 与 Deferred Boundary → `SCOPE`
- 每个用户型 Slice 的 Product Checkpoint 与最终 Hands-on Acceptance → `USER_REALITY`
- Stage Observability Delta、六类 Type Matrix、每个运行时行为变更 Task 的 Observability Obligation、Stage-level Observability Step / Checkpoint → `OBSERVABILITY`

`OBSERVABILITY` Evidence 必须按类型证明真实链路：Diagnostic → Console 可见；Product Events → Analytics Sink 可查询；Error / Crash → 接收端可查询；Metrics → value 可读；Tracing → trace / span 可查且 correlation 可串联；Audit → 授权路径可检索。只证明代码存在 log / event / capture / metric / span 调用不算通过。

`USER_REALITY` 的 Evidence 必须来自真实产品路径。

仅有以下证据不足以证明 `USER_REALITY`：

- Unit Test
- Mock
- 独立 API 调用
- Database Inspection

每项最终只能得到：

`PASS | FAIL | BLOCKED`

## 10. 定义 Exception Routing

每种预期执行异常都必须映射到唯一控制路径。

### `LOCAL_FIX`

当前问题只是本 Task 内的实现错误，且已批准设计没有变化。

### `RETURN_TO_TASK:<TXX>`

当前失败证明某个更早 Task 没有真正达到它的 Exit Condition。

### `REPLAN_BLUEPRINT`

Stage Contract 仍然正确，但当前：

- Task 拆分；
- 顺序；
- Repository Target；
- Verification Path；

无法到达已批准 Exit State。

蓝图可以重新设计执行机械路径，但不能改变任何上游语义与边界。

### `PLAN_BLOCKED_ARCHITECTURE`

继续施工必须新增或改变以下架构层决策：

- Architecture
- Scope
- Data
- Interface
- Security
- Transaction
- Compatibility
- Acceptance

向 Architecture Director 返回：

- 精确 Evidence
- 唯一未解决 Decision

### `PRODUCT_CHANGE`

当前 Product Outcome、Product Rule、Business Behavior、Acceptance Meaning 或用户授权 Requirement 已改变。

冻结蓝图生成，先走：

`Product Definition / Product Change → Architecture Director → Replan`

至少必须为以下情况定义 Route：

- Repository State 与 Entry State 不一致；
- 引用 File / Symbol 不存在，或 Contract 不一致；
- Required Tool / Dependency 不可用；
- 当前 Task Verification 失败；
- Verification 暴露既有外部 Failure；
- Generated Artifact 与 Source of Truth 不一致；
- Deferred Requirement 变成真实 Prerequisite；
- 继续工作需要新的 Architecture / Product Decision；
- 文档顺序无法到达某个 Acceptance Criterion；
- Migration / Deployment 顺序不安全；
- Preservation / Regression 与已批准路径不兼容；
- Product Checkpoint 失败，但局部 Component Test 仍通过；
- 当前排序把真实 Integration 推迟到 Stage 后期；
- Primary Product Path 只能依赖 Mock 或 Bypass 才能演示。
- Task 新增 / 改变运行时行为，但对应 Observability Delta 缺失或无法验证；
- 必要 telemetry 被推迟到后续 Task 或 Stage 尾部；
- Stage-level Observability Checkpoint 无法从真实运行链路获得证据；
- 新增关键流程、状态转换、外部依赖、异步生命周期或失败路径存在上游明确禁止的 observability blind spot；
- 运行时 Task 没有 Diagnostic / Structured Logging，或无法在本地真实运行 Console 看到关键日志；
- Product Event 代码存在但 SDK / client 未初始化、事件无法到达 Sink；
- 可运行 App / Service 缺少已要求的 Error / Crash Tracking，或把业务 `*.failed` event 当作 Crash 证据；
- Metrics / Tracing / Audit 的触发条件已成立却被无依据标记为 `N/A`；
- telemetry SDK / sink 的 runtime config、environment 或 secret / key 装载路径无法真实执行。

## 11. Dry Run 整份蓝图

基于当前真实 Repository，从已验证 Entry State 开始，模拟执行每个 Task，直到最终 Stage Acceptance。

必须验证：

- 每个引用 Path、Symbol、Interface、Schema、Command、Tool 都真实存在；
- 每个 Task 的 Prerequisite 在使用前已经成立；
- Integration Slice 顺序符合真实依赖；
- 最早可行的真实 End-to-End Path 没有被无必要推迟；
- 每个 Output 能满足后续 Task 的 Input；
- Name、Signature、ID、Schema、State Transition 保持一致；
- 每个 Task 都只有一条已批准实施路径；
- 每个 Task 都声明 Behavior Delta 与六类 Task Observability Matrix；
- 每个 `N/A` 都有有效理由，且没有违反上游 REQUIRED / trigger；
- 每个新增 / 改变运行时行为的 Task 都在同一 Task 内完成 Diagnostic / Structured Logging；
- 其余适用 Observability 类型在同一行为增量 `ADD / CHANGE` 或明确 `PRESERVE` 已有基线；
- 不存在把前序 Task 必要 telemetry 统一推迟到 Stage 尾部的计划；
- 没有 Task 在施工中创造新的 Product / Architecture Decision；
- 每个 Accepted Requirement 都映射到 Task 与 Evidence；
- 每个 Acceptance Criterion 都映射到确定性 Verification；
- 每个 Stage Observability Obligation 都按六类映射到 Task、状态与 Observability Evidence；
- 每个 Current-stage Architecture Invariant 都有 Verification 或 Preservation 路径；
- 每个 Preservation / Regression Item 都有 Evidence；
- 每个 Implementation Change 都能向上追溯到 Stage Obligation；
- Deferred Item 全部保持在执行图之外；
- 每个 Exception 都有唯一 Route；
- 每个中间 Repository State 都保持有效；
- 每个 Integration Slice 都能通过真实产品路径到达自己的 Product Checkpoint；
- Primary User-facing Path 不依赖 Mock 作为“完成”证据；
- Stage 所需 UI / Client 行为在大批后端工作全部完成之前就已经进入真实集成；
- 某 Slice Product Checkpoint 失败后，不允许继续依赖它的后续扩建；
- 用户型 Stage 的最终 Hands-on Acceptance 可以重复执行；
- 每个 Slice 的六类 Observability Evidence 可以重复取得；
- Stage 至少存在一个非 `NONE` 的 Observability Delta 与明确 Observability Step；
- 所有运行时 Task 的 Diagnostic Logging 可在本地真实运行 Console 实时观察；
- 所有 `ADD / CHANGE` 的远程 Observability 类型均能证明初始化 / runtime config / output or transport / sink / query 链路；
- Stage-level Observability Step / Checkpoint 可以重复执行并证明适用观测链路真实成立；
- Current Stage 不存在已知 Critical Observability Blind Spot；
- 最终 Repository / Runtime State 满足 Stage Exit State；
- Stage Stop Rule 成立。

发布蓝图前先修复所有 Blueprint-level Gap。

如果 Dry Run 暴露的是上游 Decision Gap，则结束为：

`PLAN_BLOCKED`

# 输出文档结构

Execution Contract 必须严格按以下顺序生成：

1. `# <Stage> — Execution Contract`
2. `## Stage Authority`
3. `## Objective`
4. `## Entry State`
5. `## Exit State`
6. `## Visible Delta`
7. `## Fixed Decisions`
8. `## Repository References`
9. `## Scope`
   - `### Change Set`
   - `### Creation Set`
   - `### Observability Set`
   - `### Preservation Set`
   - `### Regression Set`
   - `### Deferred Set`
10. `## Requirement Traceability`
10.1. `## Observability Plan / Type Matrix`
11. `## Integration Slices`
12. `## Execution Graph`
13. `## Tasks`
14. `## Product Checkpoints`
14.1. `## Observability Step / Checkpoint`
15. `## Hands-on Acceptance`
16. `## Acceptance Matrix`
17. `## Exception Routing`
18. `## Completion Protocol`

# Stage Authority 格式

记录：

- `Stage ID`
- `Accepted Requirement IDs`
- `Architecture / ADR References`
- `Stage Contract Reference`
- `Observability Contract Reference`
- `Stage Observability Delta`
- `Stage Observability Step / Verification`
- `Stop Rule`

# Requirement Traceability 格式

紧凑表达：

```text
REQ-01 -> AC-01 -> T01,T03 -> EVID-01
REQ-02 -> AC-02 -> T02     -> EVID-02
INV-03 -> AC-A03 -> T04    -> EVID-A03
OBS-DIAG-01  -> T01,T02 -> OBS-EVID-D01
OBS-PROD-01  -> T02     -> OBS-EVID-P01
OBS-CRASH-01 -> T01     -> OBS-EVID-C01
```

# Integration Slice 格式

每个 Slice 使用：

```markdown
### SXX — <Slice 名称>

**Outcome：**

**Real Product Entry：**

**Vertical Path：**

**Required Layers：**

**Real Dependencies：**

**Tasks：**

**Product Checkpoint：**

**Automated Evidence：**

**Observability Type Coverage：**

`Diagnostic Logging | Product Events | Error / Crash | Metrics | Tracing | Audit / Security`

**Observability Evidence：**

**Slice Exit State：**

**Next Slice Dependency：**
```

# Product Checkpoint 格式

```markdown
### PC-SXX — <Checkpoint 名称>

**Product Entry：**

**Actor / Test Identity：**

**Preconditions：**

**Hands-on Steps：**
1.
2.
3.

**Real Services Used：**

**Expected Visible Result：**

**Expected State / Persistence：**

**Required Failure Behavior：**

**Automated Evidence：**

**Observability Evidence：**

按六类列出本 Checkpoint 实际应出现的 Console / Sink / Crash / Metric / Trace / Audit 证据。

**Mocks Allowed：**

**Pass Condition：**
```

对于 Primary Product Path：

`Mocks Allowed` 默认应为 `NO`。

如果必须写 `YES`，则必须明确：

- 哪些真实行为仍未被证明；
- 为什么当前允许 Mock；
- 该 Checkpoint 不得作为最终 Stage Delivery Evidence。

# Observability Plan / Type Matrix 格式

必须把上游 Stage Observability Contract 编译成 Task-level instrumentation。不得把六类能力压缩成一个 `Observability Delta` 文本字段后丢失类型信息。

```markdown
## Observability Plan / Type Matrix

**Stage Observability Delta：**

**Stage Observability Step / Verification：**

**Critical Flows：**

**Sink / Console Readiness：**
- Diagnostic Console：
- Product Analytics Sink：
- Error / Crash Sink：
- Metrics Sink：
- Trace Sink：
- Audit Store / Query Path：

**Runtime Initialization / Configuration：**

**Correlation / Context：**

**Privacy / Redaction：**

| Task | Behavior Delta | Diagnostic Logging | Product Events | Error / Crash | Metrics | Tracing | Audit / Security | Evidence |
|---|---|---|---|---|---|---|---|---|
| T01 | ... | ADD | ADD | PRESERVE | N/A: ... | N/A: ... | N/A: ... | OBS-EVID-01 |

**Upstream Type Requirements：**

| Type | Stage Contract Status | Source / Trigger |
|---|---|---|
| Diagnostic / Structured Logging | REQUIRED | ... |
| Product / Business Events | REQUIRED / REQUIRED WHEN APPLICABLE / NOT APPLICABLE | ... |
| Error / Crash Tracking | REQUIRED / REQUIRED WHEN APPLICABLE / NOT APPLICABLE | ... |
| Metrics | REQUIRED WHEN APPLICABLE / NOT APPLICABLE | ... |
| Tracing | REQUIRED WHEN APPLICABLE / NOT APPLICABLE | ... |
| Audit / Security Events | REQUIRED WHEN APPLICABLE / NOT APPLICABLE | ... |
```

状态只能使用：

`ADD | CHANGE | PRESERVE | N/A`

规则：

- 每个 Task 必须出现在该矩阵中。
- 每个 `N/A` 必须包含理由。
- 凡 Task 新增 / 改变运行时行为，`Diagnostic Logging` 不得为 `N/A`。
- Product / Business 行为存在时，Product Events 必须服从上游 Stage Contract；若 Stage Contract 要求则不得无依据 `N/A`。
- 存在可运行 App / Service 时，Error / Crash Tracking baseline 必须已经建立或在本 Stage 建立；单个 Task 无新增时可 `PRESERVE`，不能用 Product Event 代替。
- Metrics / Tracing / Audit / Security 一旦触发上游适用条件，不得无依据 `N/A`。
- `ADD / CHANGE` 必须有具体 Instrumentation Actions 与真实 Observability Verification。
- `PRESERVE` 必须说明依赖的既有观测能力，并在可能受影响时提供 regression evidence。
- Stage 至少有一个 Task 对至少一种 Observability 类型产生 `ADD / CHANGE`，或完成上游明确要求的 Stage-level readiness / verification 增量。
- 独立 telemetry-only Task 只允许用于共享 telemetry 底座、SDK / sink 初始化、补齐历史阻塞盲区或 Stage-level 验证；不能替代前序运行时 Task 本应同步完成的 instrumentation。

# Observability Step / Checkpoint 格式

每个 Stage 至少提供一个明确可识别、可重复执行的 `Observability Step / Checkpoint`。该步骤不是“检查代码”，而是实际触发运行路径并检查六类适用 signal。

```markdown
## Observability Step / Checkpoint

**Stage / Slice：**

**Trigger Path：**

**Diagnostic / Structured Logging：**
- Expected Console：
- Expected start / state / success / failure logs：
- Required Context：

**Product / Business Events：**
- Expected Events：
- Analytics Sink：
- Query / Inspection：

**Error / Crash Tracking：**
- Channel / Sink：
- Initialization Evidence：
- Controlled Error / Crash Evidence：

**Metrics：**

**Tracing：**

**Audit / Security Events：**

**Required Correlation：**

**Privacy / Redaction Checks：**

**Inspection / Verification Steps：**
1.
2.
3.

**Pass Condition：**
```

规则：

- 对 Stage Contract 标为 `NOT APPLICABLE` 的类型写明 `N/A + Source`。
- 对 `REQUIRED WHEN APPLICABLE` 的类型必须再次确认触发条件是否成立。
- Apple 平台只要有运行时行为，Diagnostic 部分必须包含 Xcode Console / 平台 Console 的真实查看步骤。
- Product Events 必须证明 SDK / client 初始化且远程事件真实到达目标后台；只看到本地 print 不算通过。
- Error / Crash 必须证明独立 Error / Crash 通道真实接通；业务失败 event 不算 Crash Evidence。
- Checkpoint 必须能够发现“调用写了但 SDK 没启动”“key / config 没加载”“网络 / sink 不通”“环境写错”等假完成状态。

# Hands-on Acceptance 格式

每个用户型 Stage 必须提供：

```markdown
## Hands-on Acceptance

**谁可以测试：**

**产品入口：**

**前置条件 / 测试账号：**

**操作步骤：**
1.
2.
3.

**预期可见结果：**

**预期持久化 / 状态：**

**预期失败行为：**

**这证明了什么：**
```

本节是写给非技术用户的。

必须做到：

- 不需要阅读实现细节；
- 按步骤即可直接执行；
- 能真实判断本 Stage 是否在产品上成立。

# Execution Graph 格式

紧凑表达依赖：

```text
T01 -> T02 -> T04
       T03 -> T04
T04 -> T05
```

只有 Dependency-independent Task 才标 `[parallel]`。

# Task 格式

每个 Task 使用：

```markdown
### TXX — <Task 名称>

**Slice ID：**

**Requirement Coverage：**

**Behavior Delta：**

**Task Observability Matrix：**

| Type | Upstream Requirement | Task Status | Delta / Preserve / N/A Reason | Verification Evidence |
|---|---|---|---|---|
| Diagnostic / Structured Logging | REQUIRED |  |  |  |
| Product / Business Events |  |  |  |  |
| Error / Crash Tracking |  |  |  |  |
| Metrics |  |  |  |  |
| Tracing |  |  |  |  |
| Audit / Security Events |  |  |  |  |

**Observability Delta：**

**Objective：**

**Prerequisites：**

**Targets：**

**References：**

**Inputs：**

**Actions：**
1.
2.
3.

**Instrumentation Actions：**
1.
2.

**Outputs：**

**Verification：**

**Observability Verification：**

**Expected Result：**

**Exit Condition：**
```

# Acceptance Matrix 格式

使用：

| ID | Type | Requirement / Obligation | Source | Task | Evidence | Verification | Pass Condition |
|---|---|---|---|---|---|---|---|

# Completion Protocol

Execution Contract 只有同时满足以下全部条件，才可以结束为：

`READY`

条件：

- 所有权威输入都存在且相互兼容；
- 所有 Repository Reference 都能解析；
- 所有 Current-stage Implementation Decision 已冻结；
- 用户型工作已组织成纵向 Integration Slice；
- 没有 Task 需要新的 Product / Architecture Decision；
- 所有 Accepted Requirement 都能追溯到 Task 与 Evidence；
- 所有 Task 都有确定 Prerequisite、Action、Output、Verification 与 Exit Condition；
- 所有 Task 都声明 Behavior Delta 与六类 Task Observability Matrix；
- 所有 `N/A` 有有效理由，所有条件触发项没有被错误省略；
- 所有新增 / 改变运行时行为的 Task 都在同 Task 完成 Diagnostic / Structured Logging 并通过本地 Console Verification；
- 所有其他 `ADD / CHANGE` 类型都完成必要 instrumentation、初始化 / runtime config 与真实 Sink / query Verification；
- 所有 Acceptance Criteria 都已覆盖；
- 每个 Integration Slice 都有真实 Product Checkpoint；
- 每个 Integration Slice 都有明确六类 Observability Type Coverage / Evidence；
- 第一个真实 End-to-End Path 没有被无必要推迟；
- 用户型 Stage 不依赖一个很晚的 Final Integration Task 才第一次连接主要技术层；
- 所有 Current-stage Architecture Invariant 都被保护；
- 所有 Preservation Commitment 都可验证；
- 所有 Regression Obligation 都可验证；
- 所有 Deferred Requirement 都保持在 Current Execution 之外；
- 每个 Planned Change 都能追溯到 Current Stage Authority；
- 每种 Exception 都有确定控制路径；
- 每个 Slice Checkpoint 都能针对真实产品路径执行；
- Component Test / CI / Mock 没有被用来替代真实 Product Delivery Evidence；
- 用户型 Stage 包含可重复执行的最终 Hands-on Acceptance；
- Stage 至少包含一个非 `NONE` 的 Observability / Instrumentation 增量；
- Stage 包含至少一个可重复执行的 Stage-level Observability Step / Checkpoint；
- Diagnostic Logging、Product Events、Error / Crash、Metrics、Tracing、Audit / Security 已按上游 Type Matrix 和触发条件完整处理；
- Product Events 与 Error / Crash 等远程能力不存在“调用存在但 SDK / sink 未初始化”的假完成；
- 必要 telemetry 没有被推迟到 Stage 尾部统一补做；
- Current Stage 不存在已知 Critical Observability Blind Spot；
- Dry Run 能通过持续集成的产品状态到达 Stage Exit State；
- Stage Stop Rule 可以被机械判断。

否则结束为：

```text
PLAN_BLOCKED

Type: <REPLAN_BLUEPRINT | PLAN_BLOCKED_ARCHITECTURE | PRODUCT_CHANGE>
Gap: <identifier>
Location: <section/task>
Evidence: <repository fact / contract conflict>
Upstream Source: <Stage Contract / ADR / Product Rule / Requirement ID>
Decision Required: <single unresolved decision>
Owner: <Construction Blueprint | Architecture Director | Product / User>
```

# Handoff

当状态为 `READY` 时，把 Execution Contract 交给施工 Agent。

施工 Agent 必须：

- 按项目施工规则执行；
- 一次完成一个 Integration Slice；
- 返回 Implementation Changes；
- 返回 Automated Evidence；
- 返回 Product Checkpoint Evidence。
- 按 Task 同步实现六类 Task Observability Matrix，不得先完成功能后补 telemetry；
- 对每个运行时 Task 返回 Diagnostic / Structured Logging 的真实 Console Evidence；
- 对 Product Events、Error / Crash、Metrics、Tracing、Audit / Security 的 `ADD / CHANGE` 返回真实 Sink / Query / Inspection Evidence；
- 返回 Task-level Observability Evidence；
- 返回 Stage-level Observability Step / Checkpoint Evidence。

某个 Product Checkpoint 失败时：

**在问题解决或正式 Replan 之前，不得进入依赖它的后续 Slice。**

Stage Verifier 后续按照：

`Architecture → Stage Contract → Construction Blueprint → Implementation → Evidence`

进行验收。

因此，蓝图必须保持完整的正向与反向 Traceability。

# 质量标准

优化目标：

`执行确定性 + 信息密度 + 真实产品持续成立`

使用：

- 精确 Path
- 精确 Symbol
- 精确 Command
- 精确 Selector
- Requirement ID
- Acceptance ID
- State Transition
- Dependency Edge
- Observable Outcome
- Behavior Delta / six-type Task Observability Matrix
- Console / Sink Readiness
- Correlation / Traceability
- Telemetry Verification Evidence

优先使用 Repository-grounded Reference，而不是泛泛描述。

Rationale 只在以下情况保留：

- 它会约束执行；
- 它用于保护上游 Decision；
- 它用于解释必须存在的 Exception Route。

蓝图只有在施工 Agent 可以从 Entry State 走到 Exit State，并且不需要重新决定以下内容时，才算完整：

- 产品是什么意思；
- 应该存在什么架构；
- 什么属于 Current Stage；
- 什么算完成。

对于用户型工作，Execution Path 必须持续产生已经集成、真实可运行的产品状态。

对于所有会改变运行时行为的工作，Execution Path 还必须持续产生同步增长、可验证的六类 observability；不得出现“功能已经存在，但 Diagnostic Logging / Product Events / Error & Crash / Metrics / Tracing / Audit 以后再补”的黑盒中间状态。

尤其不得把“编译通过 + telemetry 调用存在”误判为完成。真实完成必须能看到 Console 或目标 Sink 中的实际证据。

**如果一个计划做到“80% 组件完成”时，产品仍然无法被真正使用，即使 CI 全绿，这个蓝图在结构上也是无效的。**

---
name: construction-blueprint
display_name: 施工蓝图
description: 当架构总设计师已经冻结当前 Stage Contract，需要在编码前为施工 Agent 生成一份确定性、基于真实仓库、按持续纵向集成推进，并能通过真实产品检查点与用户上手验收证明结果成立的 Execution Contract 时使用。
---

# 施工蓝图

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

## Architecture Inputs

- 相关 Architecture Spine
- 相关 ADR / Decision Log
- Architecture Director 的 Blueprint Handoff
- 当前适用的项目工程规则

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

对每个 Accepted Requirement 与 Acceptance Criterion，明确：

- Implementation Responsibility
- Task Coverage
- Expected Evidence
- Preservation / Regression dependencies

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
- `Objective`
- `Prerequisites`
- `Targets`
- `References`
- `Inputs`
- `Actions`
- `Outputs`
- `Verification`
- `Expected Result`
- `Exit Condition`

`Slice ID`：标明该 Task 正在推进哪个 Integration Slice 的真实产品状态。

`Requirement Coverage`：列出该 Task 服务的精确 Requirement ID、Acceptance ID、Invariant ID、Preservation ID 或 Regression ID。

`Targets`：写明精确 File、Symbol、Schema、Migration、Configuration、Test 或 Generated Artifact。

`References`：写明约束该 Task 的精确 Repository Artifact、ADR、Interface、Test 或 Convention。

`Inputs`：写明施工开始前必须存在的具体 Repository State。

`Actions`：按顺序写状态改变操作。每个 Action 只描述一个操作，并提供足够细节，使施工 Agent 只能沿唯一已批准路径实施。

`Outputs`：描述 Task 完成后真实产生的 Repository 与 Runtime State。

`Verification`：写出可执行 Command、Test Selector、Inspection、State Check、Migration Check、Generation Check 或确定性 Manual Procedure。

`Expected Result`：写出精确、可观察的预期判定。

`Exit Condition`：写明什么状态成立后，才能解锁依赖它的后续 Task。

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

覆盖要求：

- 每个 Stage Acceptance Criterion → `DELIVERY`
- 每个 Current-stage Architecture Invariant obligation → `ARCHITECTURE`
- 每个 Preservation Set commitment → `PRESERVATION`
- 每个 Regression Set item → `REGRESSION`
- Current Authorized Scope 与 Deferred Boundary → `SCOPE`
- 每个用户型 Slice 的 Product Checkpoint 与最终 Hands-on Acceptance → `USER_REALITY`

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
- 没有 Task 在施工中创造新的 Product / Architecture Decision；
- 每个 Accepted Requirement 都映射到 Task 与 Evidence；
- 每个 Acceptance Criterion 都映射到确定性 Verification；
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
   - `### Preservation Set`
   - `### Regression Set`
   - `### Deferred Set`
10. `## Requirement Traceability`
11. `## Integration Slices`
12. `## Execution Graph`
13. `## Tasks`
14. `## Product Checkpoints`
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
- `Stop Rule`

# Requirement Traceability 格式

紧凑表达：

```text
REQ-01 -> AC-01 -> T01,T03 -> EVID-01
REQ-02 -> AC-02 -> T02     -> EVID-02
INV-03 -> AC-A03 -> T04    -> EVID-A03
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

**Mocks Allowed：**

**Pass Condition：**
```

对于 Primary Product Path：

`Mocks Allowed` 默认应为 `NO`。

如果必须写 `YES`，则必须明确：

- 哪些真实行为仍未被证明；
- 为什么当前允许 Mock；
- 该 Checkpoint 不得作为最终 Stage Delivery Evidence。

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

**Objective：**

**Prerequisites：**

**Targets：**

**References：**

**Inputs：**

**Actions：**
1.
2.
3.

**Outputs：**

**Verification：**

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
- 所有 Acceptance Criteria 都已覆盖；
- 每个 Integration Slice 都有真实 Product Checkpoint；
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

**如果一个计划做到“80% 组件完成”时，产品仍然无法被真正使用，即使 CI 全绿，这个蓝图在结构上也是无效的。**

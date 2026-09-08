---
name: construction-blueprint
display_name: 施工蓝图
description: 接收架构总设计师冻结的 Current Stage Contract，在不创造产品或架构决策的前提下，基于真实仓库把 Stage 编译成可机械施工的纵向 Slice 与精确 Task；让真实产品路径尽早成立，并用最小合理成本完成局部、能力和 Stage 三层验证，同时把已触发的日志、埋点、Crash、Metrics、Tracing、Audit 等运行义务落到实际施工位置。
---

# 施工蓝图

## 使命

把已经冻结的 `Stage-n` 从“架构上可建设”编译成“施工 Agent 可以直接执行”。

蓝图必须同时做到：

1. **不重新设计产品**：产品语义来自 Product Definition 与 Stage Contract。
2. **不重新设计架构**：技术方向、模块边界、数据 / 接口 /权限 / Provider 等来自架构权威文档。
3. **真实仓库落地**：所有计划必须建立在真实 Path、Symbol、Schema、Command 和现有实现上。
4. **尽早形成真实纵向能力**：优先让最薄的真实产品 / 系统路径跑起来，而不是先批量完成技术层。
5. **施工步骤确定**：施工 Agent 不需要在 Task 中重新决定“做什么、放哪里、怎么验证”。
6. **验证成本受控**：Task、Slice、Stage 三层各证明不同事实；同一事实不重复测试。
7. **运行义务同步落地**：Stage 真正触发的 Logging、Product Events、Crash、Metrics、Tracing、Audit、Backup、Alert 等不能被拖到功能完成之后。
8. **文档克制**：Execution Contract 只记录施工所需的当前有效事实，不复制上游长篇理由和讨论过程。

核心原则：

`Frozen Stage → Repository Reality → Vertical Slices → Deterministic Tasks → Minimum Sufficient Verification`

施工执行约束：

> Construction Agent 执行本 Execution Contract 时应同时加载 `no-pitfall`；Blueprint 决定“怎么施工”，`no-pitfall` 约束“施工时不能踩哪些坑”。

## 上游权威输入

### 1. Current Stage Contract

以架构层当前 `Stage-n` Contract 为主权威。

至少需要：

- Stage-n / Name
- Included `Requirement-n`
- Outcome
- Entry State
- Exit State / Visible Delta
- Authorized Scope
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
- `EXTERNAL_SERVICES.md`
- `OBSERVABILITY.md`（若项目存在或本 Stage 触发）
- `DECISIONS.md`
- 相关 Stage Baseline

不要求把所有架构文档整篇复制进蓝图。

### 3. Product Authority

仅在解释 Requirement 或用户行为时读取：

- `docs/product/Product-Definition.md`
- 当前 Stage 所引用的 `Requirement-n`
- Product Rules
- Actors / permissions
- Core Product Loop
- Product Acceptance Intent
- 与 Current Stage 直接相关的产品结论

蓝图不要求上游额外存在 `Capability Card`、`Capability-n`、`HORIZON Item`、产品 Roadmap 或 feature-level PRD。

### 4. Repository Reality

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
- 把 `Requirement-n`、Architecture Obligation、Acceptance、Preservation、Direct Regression 映射到具体施工。
- 把 Stage 切成尽早集成的 `Slice-n`。
- 把 Slice 拆成 `Task-n` 并排序。
- 决定精确 File / Symbol / Schema / Migration / Config / Test 落点。
- 决定已批准路径内的低成本实施机械细节。
- 把已触发 Operational Obligations 放进实际改变相关行为的 Task。
- 为每个 Task 选择最便宜且足够的简单验证。
- 为每个 Slice 定义能力功能测。
- 为 Stage 定义最终模块测 / Hands-on Acceptance。
- 建立足够的正向和反向 Traceability。
- Dry Run 整份执行路径。

### 蓝图不负责

- 改变 Product Outcome / Product Rule / Business Model。
- 新增或删除 `Requirement-n`。
- 改变 Stage Scope / Exit State / Acceptance。
- 重新做技术栈、Provider 或 Foundational Decision。
- 改变 Architecture Invariant。
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

### 产品语义缺口：先回 Product Detail

如果缺失信息会改变以下任一产品语义：

- user / actor
- ownership / permission / visibility
- product state / lifecycle
- irreversible action
- business rule
- user-visible failure / recovery
- commercial behavior
- acceptance outcome
- external product promise
- privacy / sensitive product semantics

蓝图不得自行猜测。

处理顺序：

1. 指向具体 `Requirement-n`。
2. 说明缺失的产品语义为什么会改变施工结果。
3. `Owner: Product`，回 `product-detail`。
4. Product Detail 若只是补清原 Requirement → Chief Architect 更新 / 确认 Stage Contract 后继续 Blueprint。
5. Product Detail 若发现需要改变 Product Definition → 回 Product Designer，再由 Chief Architect 重新裁决 Stage。

如果缺口属于 architecture boundary / interface / security / consistency / Provider / technical direction，则：

`Owner: Architecture`

回 Chief Architect。

普通 UI、代码组织和约定俗成的实现细节不得回 Product Detail。

详细判定见 `references/product-detail-boundary.md`。

## 最高优先级施工原则

### 1. 唯一 Execution Contract

默认权威文件：

`docs/blueprint/EXECUTION_CONTRACT.md`

Current Stage 的蓝图内容只存在这一份。

- 修订直接 in-place 更新。
- 不创建 supplement / additions / observability copy / summary contract。
- 临时探索如果必须写文件，只允许放 `.workbench/`，交付前删除或把有效结论并回唯一合同。
- 合同表达当前有效计划，不维护长篇 Revision Log 或废弃 Task 墓地。
- Stage 完成后的历史事实由架构 Stage Baseline / verifier evidence 承担，不靠保留多份蓝图副本。

### 2. 先让真实能力成立

用户型 Stage 默认：

`Thin Vertical Slice → Real Integration → Capability Verification → Expand`

禁止默认：

`Database → Backend → Services → UI → Final Integration`

UI / Client 是产品行为的一部分；如果 Stage Outcome 需要用户操作，UI 必须进入早期 Slice。

### 3. Slice 是纵向能力，不是技术批次

每个 `Slice-n` 必须形成一个真实、已连接的状态。

典型路径可以跨：

`UI / Client → API → Domain → Data → External Service → Visible Result`

不是所有 Slice 都必须跨所有层，只包含该能力实际需要的层。

准备型 Task 可以存在，但必须被最近的 Slice 很快消费；不允许长期堆积“以后再集成”的组件。

### 4. Task 是施工单元，不是验收单元

Task 负责：

- 一个清楚的改动目标。
- 明确 Prerequisite。
- 精确 Targets。
- 机械 Actions。
- 当前改动的简单测试。
- 清楚 Done When。

Task 不负责：

- 重跑完整 Slice。
- 重跑整个 Stage。
- 每次重新验证所有 Provider / telemetry sink。
- 重复证明已经在更低层充分证明的事实。

### 5. 同一事实不重复测试

验证只分三层：

1. **Task Simple Test**：证明当前局部改动。
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

详细见 `references/operational-obligations.md`。

### 8. 中间状态必须有效

每个 Task 完成后：

- Repository 不应处于明显不可构建 / 不可迁移的破损状态。
- 后续依赖所需输入已经存在。
- 不应该需要未来 Task 来“解释当前 Task 到底算没算完成”。

必要时通过 feature flag、兼容迁移、expand-contract 等方式维持安全中间状态；但这些方式必须已被架构允许。

## Stage 开工前产品细化门禁

在开始 Repository 级蓝图编译前，做一次快速检查：

> 当前 Stage 中是否存在“答案不同会导致产品行为不同”的未决语义？

如果没有：

继续 Blueprint，不调用 Product Detail。

如果有：

- 不展开完整蓝图。
- 只报告具体 `Requirement-n` 与缺失语义。
- 回 `product-detail`。
- 等 Chief Architect 将结果冻结回 Stage Contract 后恢复。

这不是新增强制流程。没有产品语义缺口时必须跳过。

## 工作流程

### 1. Restore Authority & Reality

读取：

- Current Stage Contract
- 相关 architecture / decisions / standards
- 当前唯一 Execution Contract（若恢复）
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

Target State 不等于“代码已经写完”。

对用户型 Stage：

**真实产品入口不能到达 Visible Delta，就不算 Target State。**

### 3. Build Scope

建立最小施工集合：

- **Change Set**：预计修改的既有 Path / Symbol / Schema / Config / Test。
- **Creation Set**：预计新建的 Path / Symbol / Migration / Artifact / Test。
- **Preservation / Direct Regression**：上游已列且本次真正可能影响的既有行为。
- **Explicit Non-Scope**：容易顺手做但明确不属于 Current Stage 的事项。

不要为了完整性重复维护一套 `Observability Set`；运行义务直接映射到受影响 Task。

每个 Planned Change 必须能解释它服务于哪个：

- Requirement-n
- Stage Acceptance
- Architecture Delta / Decision-n
- Preservation / Direct Regression
- Operational Obligation

找不到上游依据的改动，默认移除。

### 4. Build Traceability

建立紧凑映射：

`Upstream Obligation → Slice-n / Task-n → Verification`

覆盖：

- 每个 Included Requirement-n。
- 每个 Stage Acceptance Criterion。
- Current Stage 相关 Architecture Delta / Invariant。
- Preservation / Direct Regression。
- Triggered Operational Obligations。

同时反向检查：

> 每个 Task-n 是否能回到至少一个上游义务？

不能则说明 Blueprint 在自行扩 Scope。

不创建 AC / Evidence 编号。

### 5. Build Vertical Slices

先切 Slice，再拆 Task。

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
- Prerequisites
- Targets
- Actions
- Operational Work（仅触发时）
- Simple Test
- Expected Result
- Done When

Targets 尽可能精确到：

- File
- Symbol / Type / Function
- Route / View
- Schema / Migration
- Configuration
- Test target / selector
- Generated artifact

Actions 要让施工 Agent 沿唯一已批准路径工作，但不要把代码逐行写进蓝图。

Task 名称写“产生什么变化”，避免：

- `Handle stuff`
- `Update backend`
- `Fix tests`
- `Add observability`

### 7. Build Execution Graph

按真实依赖排序 Task。

只有以下均互不依赖时才标可并行：

- Prerequisite
- Write Surface
- Shared State
- Generated Artifact
- Migration order
- Verification dependency

不要为了显得快而并行会争用同一接口 / schema / state 的 Task。

### 8. Assign Verification

对每个 Task、Slice、Stage 分配唯一主要验证职责。

Task：
- 快速、局部、失败定位直接。
- 默认只跑相关 build / lint / unit / schema / migration / config 检查。
- 不默认跑全仓 tests。

Slice：
- 跑真实能力路径。
- 只覆盖该 Slice 成立所必需的关键行为、失败 / permission / external boundary。
- 不复制每个 Task 的所有 unit case。

Stage：
- 验证 Stage Outcome、Acceptance、Direct Regression、适用 Operational Obligations 和 Stop Rule。
- 不是全产品 regression suite。

### 9. Route Exceptions

规划阶段发现问题时只使用 `BLOCKED`。

#### Owner: Blueprint

Stage Contract 和架构都成立，只是当前 Task 拆分、顺序、Target 或 Verification Path 不好。

蓝图自己修正后重新 Dry Run，不需要向上游创造新状态名。

#### Owner: Architecture

继续规划需要改变：

- Stage Scope / Exit State
- Decision-n
- module / interface / data boundary
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

回产品细化 / 用户。

### 10. Dry Run

发布前，从真实 Entry State 模拟执行：

- 所有 Path / Symbol / Schema / Command 是否真实可解析。
- Prerequisite 是否在使用前成立。
- Task Output 是否满足后续 Input。
- Slice 是否尽早形成真实纵向状态。
- UI / Client 是否没有被无理由拖到最后。
- Requirement / Acceptance / Decision / Preservation / Operational Obligation 是否有施工与验证落点。
- 每个 Task 是否都有上游依据。
- Direct Regression 是否克制在直接影响范围。
- Deferred / Non-Scope 是否没有被拉进施工。
- 高风险真实边界是否没有被全 Mock 掩盖。
- 测试是否存在明显三层重复。
- 运行义务是否与相关行为同步，而不是 Stage 尾部补。
- 最终路径是否达到 Exit State。
- Stop Rule 是否机械可判。

发现 Blueprint 自身缺口 → 修正。

发现 Product / Architecture 缺口 → `BLOCKED`。

## Completion Gate

只有同时满足以下条件才输出：

`READY`

- 上游 Stage Contract 有效。
- Repository Entry State 已验证。
- 没有未决 Product / Architecture Decision。
- Scope 只包含 Current Stage 授权工作。
- 每个 Requirement / Acceptance / Architecture Obligation 都有施工落点。
- 每个 Planned Task 都有上游依据。
- 用户型工作被组织为早期真实纵向 Slice。
- 每个 Task 都有精确 Target、Actions、Simple Test、Done When。
- Execution Graph 可执行。
- 验证三层分工清楚且无明显重复。
- 高风险真实依赖使用了足够的真实验证。
- Triggered Operational Obligations 已落到相关施工位置。
- Preservation / Direct Regression 有最小充分证据。
- Explicit Non-Scope 保持在执行图外。
- Dry Run 可从 Entry State 到 Exit State。
- Stop Rule 可机械判断。
- Execution Contract 内没有废弃 Task、失效占位或平行合同。

否则输出：

`BLOCKED`

并给出单一当前阻塞点；多个缺口可以一起列出，但按依赖顺序排序，不制造新的状态对象。

## Execution Contract 输出结构

默认只维护：

`docs/blueprint/EXECUTION_CONTRACT.md`

推荐结构：

```text
# Stage-n — Execution Contract

## 1. Authority
## 2. Objective
## 3. Entry State
## 4. Target State
## 5. Scope
## 6. Traceability
## 7. Slices
## 8. Execution Graph
## 9. Tasks
## 10. Verification
## 11. Exception Routing
## 12. Completion
```

详细字段见 `references/docs-spec.md`。

## Handoff

状态为 `READY` 后交给 Construction Agent。

施工 Agent 应：

- 按 `Slice-n` 顺序推进。
- 按 `Task-n` 精确施工。
- 遵守 Architecture / Engineering Standards。
- Task 完成时返回本 Task 的简单证据。
- Slice 完成时运行该 Slice 的能力功能测。
- 已触发 Operational Obligation 随相关行为同步实现。
- 不因某个 Task 失败自行改变产品或架构。
- Slice 真实能力未成立时，不继续依赖该 Slice 的后续扩建。

Stage Verifier 后续以：

`Stage Contract → Execution Contract → Implementation → Evidence`

为主链验收。

Blueprint 不需要为 Verifier 预先制造大量 Evidence ID；验证位置和可重复步骤清楚即可。

## 按需加载 References

- 文档结构与合同字段：`references/docs-spec.md`
- Repository Intake：`references/repository-intake.md`
- 产品细节边界：`references/product-detail-boundary.md`
- Slice / Task 设计：`references/slice-task-design.md`
- 验证与测试分层：`references/verification.md`
- Observability / Operations 落位：`references/operational-obligations.md`

不要默认一次读完所有 reference。只在对应问题出现时加载。

## 最终原则

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

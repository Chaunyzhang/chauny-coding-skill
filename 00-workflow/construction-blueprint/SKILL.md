---
name: construction-blueprint
display_name: 施工蓝图
description: 接收 Chief Architect 冻结的 Current Stage Contract，并消费 Product Definition / Product Atoms、Domain Ownership、Semantic Authority 与 Engineering Standards；在不创造产品或架构决策的前提下，基于真实仓库把 Stage 编译成可机械施工的纵向 Slice、Implementation Shape 与精确 Task；从规划源头抑制语义丢失、边界绕过、重复 authority、防御性扩张、重复验证和假想风险工作。
---

# 施工蓝图

## 使命

把已冻结的 `Stage-n` 从“架构上可建设”编译成“Construction Agent 可直接执行”。

必须同时满足：
- 产品语义无损：直接消费 Current Requirement 与 binding Atom，不用更弱技术代理替代。
- 架构边界无损：复用已冻结的 Domain Ownership、Semantic Authority、public path、module/dependency boundary 与 Provider 方向。
- 仓库真实：Path、Symbol、Schema、Command、caller 与当前实现均来自 Repository Reality。
- 早集成：优先形成最薄真实能力 Slice，而非先批量完成技术层。
- 施工确定：Task 不把产品、架构、state/failure semantics、proof strategy 留给 Construction 发明。
- 验证克制：Task / Slice / Stage 各证明不同事实，同一事实不重复验证。
- 运行义务同步：只施工被 Stage Contract / defect / admitted risk 触发的 Operational Obligations。
- 规划克制：不把假想风险、防御性焦虑、无 Trigger hardening 编译成工作。
- 文档克制：Execution Contract 只记录当前有效施工事实，不复制上游理由。

`Frozen Stage → Repository Reality → Evidence-Gated Scope → Vertical Slices → Deterministic Tasks → Sufficient Proof → STOP`

Construction 执行本合同应同时加载 `no-pitfall`；Blueprint 也必须吸收其规划侧约束：假想风险先证明、真实缺陷修根因、无 Live Uncertainty 不加验证、证据充分后停止扩 Scope。

## 权威输入

### Current Stage Contract

Stage Contract 是当前 Scope / Exit / Acceptance 的主权威。Blueprint 至少确认：
- Stage、Included Requirement、binding Atom / Representative Example（适用时）。
- Outcome、Entry、Exit / Visible Delta、Authorized Scope。
- Architecture / Platform Delta、Applied Decision、Engineering Standards。
- Domain Ownership / Semantic Authority / dependency constraints（若已冻结）。
- Operational Obligations、Verification Plan、Dependencies。
- Preservation / Direct Regression、Acceptance、Explicit Non-Scope、Escalation Triggers、Stop Rule。

### Architecture Authority

只读 Current Stage 实际需要的 `ARCHITECTURE.md`、`TECH_STACK.md`、`PROJECT_STRUCTURE.md`、`ENGINEERING_STANDARDS.md`、`EXTERNAL_SERVICES.md`、`OBSERVABILITY.md`、`DECISIONS.md`、相关 Stage Baseline，以及其中的 Domain Ownership / Semantic Authority / public-internal boundary。

不把这些文档全文复制进蓝图。

### Product Authority

只读 Current Stage 相关的 `docs/product/Product-Definition.md`、`docs/product/Product-Atoms.md`、Requirement、binding Atom、Representative Example、Product Rules、actor/ownership/permission、Core Product Loop 与 Acceptance intent。

`Requirement-n` 的 ID trace 不等于语义保真。Blueprint 必须读取 binding Atom 原文，并把每条会改变正确实现的产品义务映射到 construction + verification。

不得要求上游额外创建 Capability Card、Capability-n、HORIZON Item、Roadmap 或 feature PRD。

### UI Authority

已有正式 UI System / Handoff（如 `docs/ui/UI-SYSTEM.md` 与当前 Stage UI Handoff）时消费其 Structure / Component / State / Interaction / Motion / Accessibility 与 Human-only acceptance。没有正式 UI Handoff 时只规划 Functional UI：真实入口、可操作、必要状态可见、真实结果可见。

机械 UI compliance 可由 Agent 证明；审美、质感、视觉平衡和最终视觉接受归 Human。

### Repository Reality

聊天历史不能替代仓库。按 Stage Scope 从目标文件、caller/callee、schema、config、tests、generated artifacts、integration 与真实命令递进扫描；详细见 `references/repository-intake.md`。

## 对象与状态

沿用上游对象，不重新编号：
- Product Definition
- Atom-n
- Requirement-n
- Decision-n
- Stage-n

Blueprint 只创建：
- `Slice-n`：Current Stage 内可独立成立、可验证的纵向能力状态。
- `Task-n`：Slice 内最小、确定、可施工并可局部证明的改动单元。

两者仅在当前 Execution Contract 内从 1 编号。`Step` 只能表示普通动作步骤，不得成为项目对象。

禁止再造 `Capability-n / R-n / H-n / ES-n / AC-n / EVID-n / Checkpoint-n / Observability-n / Phase-n / Step-n` 等追踪体系。Acceptance、Preservation、Regression、Operational Obligation 直接引用上游原条目。

Blueprint 状态只有：
- `READY`
- `BLOCKED`

BLOCKED 必须给：
```text
Owner: Blueprint | Architecture | Product
Gap:
Evidence:
Blocks:
Required Resolution:
```

## 权责边界

Blueprint 负责把已冻结语义编译为仓库级 Execution Contract：验证 Entry State，形成 Target State、Scope、Traceability、Implementation Shape、Slices、Tasks、Execution Graph、Proof、Exception Routing，并 Dry Run 到 Exit State。

Blueprint 可以决定不改变产品语义、Stage Acceptance 或架构边界的局部机械细节，例如既有模式内的 component / handler / file / test target / SDK wiring 落点。优先继承 Repository Convention。

Blueprint 不负责：
- 改 Product Outcome / Rule / Business Model，新增或删除 Requirement。
- 改 Stage Scope / Exit / Acceptance。
- 重做 Foundational Decision、Provider / technology direction。
- 新建或改变长期 Domain Owner、Semantic Authority、核心 module / dependency direction、data/security/consistency/compatibility architecture。
- 创造新的产品失败语义或不可逆行为。
- 施工代码或替 Stage Verifier 宣布最终通过。
- 对历史仓库做开放式重审。

### Product Refinement 是例外

开始 Repository 级蓝图前只做一次轻量门禁。只有同时满足 Current Stage、Need Now、Cannot Defer、Product Impact 才回 `product`（Focused Refinement）；已有 Product Definition / Atom 答案时直接继承，不重问。Foundation / technical-only / infrastructure / migration 默认跳过，除非缺口会改变底座抽象、状态、权限/所有权或当前 Acceptance。

具体判定与 Product / Architecture routing 见 `references/product-refinement-boundary.md`。

## 编译期 Guardrails

### Planning Guardrails

所有额外 guard / fallback / retry / compatibility / recovery / extra observability / regression / rollback 等，必须来自：
- 上游义务；
- Confirmed Defect；
- 达到门槛的 evidence-backed risk。

真实缺陷修根因；假想风险先评分；额外验证必须对应 Live Uncertainty；Delete/Replace 默认意味着旧现实级联消失；中间 Task 只需支持继续施工，不默认要求独立生产部署；合同已 READY 时无新 Trigger 就 STOP。

阈值与完整规则见 `references/planning-guardrails.md`。

### Reasoning Compilation

Blueprint 要把复杂度消化到最终 Task 只需 `Low (0–4)` 或 `Medium (5–10)`。`>10` 或存在关键 planning defect 时 Task 无效；最终合同禁止 `High / XHigh`。

Reasoning 衡量剩余决策空间，不是工作量或 Criticality。高后果任务可标 `Sensitive | Critical`，但仍必须先冻结 invariant / ownership / failure / proof。

评分与 Construction escalation 见 `references/reasoning-policy.md`。

### Delegation Compilation

默认 `Root executes directly`。Task 可并行不等于值得 spawn subagent。

只有新模型上下文在 context isolation / true parallelism / independent evidence / specialized capability / long autonomous investigation 上产生明确净收益，并通过 Delegation Score、Time Gate 与 Hard Veto，才允许写 Delegation。Child depth 默认 1；实现型 Child 还必须拥有冻结 contract、Low/Medium Task、独立 write surface/commit、清楚 fan-in 和正 wall-clock 收益。

完整规则见 `references/delegation-policy.md`。

## 核心施工原则

1. **每个 Stage 一份 Execution Contract**：`docs/blueprint/stages/Stage-<N>.md`。同一 Stage 不建 supplement / observability copy / summary；临时探索只进 `.workbench/`，交付前删除或并回。
2. **先让真实能力成立**：用户型 Stage 优先 `Thin Vertical Capability Slice → Real Integration → Capability Verification → Expand`。UI 是能力的一部分，不默认最后接。
3. **Slice 是能力闭环，不是业务剧情**：证明 `Real Entry → required layers → Real State/Side Effect → Visible/Observable Result`；独立能力分 Slice。
4. **Task 是施工单元，不是验收单元**：Task 有精确 target/actions/local proof/done when，但不默认重跑 Slice/Stage/Provider。
5. **同一事实不重复验证**：Task Local Proof、Slice Capability Test、Stage Module Test 分层；只有新增跨层证据价值才重复。
6. **Mock 不是现实**：主能力依赖真实外部边界时，在适当 Slice / Stage 用 sandbox/test environment 证明；不把所有低风险 dependency 强制真环境。
7. **运行义务随行为施工**：只消费 triggered obligations，不填全套 N/A，不在 Stage 尾部统一补。
8. **中间状态支持继续施工即可**：只有真实 deployment / mixed-version / migration / parallel contract 需要时才增加 feature flag、compatibility、rollout 等机制。

详细分别见 `references/slice-task-design.md`、`references/verification.md`、`references/operational-obligations.md`。

## 工作流程

### 1. Restore Authority & Reality

读取 Current Stage Contract、相关 Product/Architecture authority、已有 Execution Contract（恢复时）和真实 Repository State。

确认：
- Stage Contract 与仓库现实兼容。
- Requirement / Atom / Decision / module / Provider 引用仍有效。
- Entry State 真实。
- 已关闭 Stage Baseline 足以作为当前起点。

扫描按 `references/repository-intake.md` 递进，不因仓库大而全量审计。

### 2. Compile Target State

把 Exit State 编译为可判真假事实：
- runtime / UI / API / data / persistence / side-effect 结果；
- 必须存在或改变的 file/symbol/schema/route/service/config/migration；
- 必须保持的既有行为；
- triggered Operational Obligations；
- Acceptance 与 Stop Rule；
- binding Atom 的真实产品行为。

用户型 Stage 的真实入口不能到达 Visible Delta，则 Target State 未成立。

### 3. Build Scope & Implementation Shape

建立最小：
- Change Set
- Creation Set
- Preservation / Direct Regression
- Explicit Non-Scope

并在 Scope 内编译轻量 `Implementation Shape`：
- Touched Domains / Modules
- Ownership
- Required Reuse / Existing Authorities
- Allowed Dependencies
- Forbidden Bypasses
- State / Side-effect Flow
- Expected Change Boundary

只写适用项。若需要新建/改变长期 owner、Semantic Authority、核心 boundary、dependency direction 或 public contract，`BLOCKED / Owner: Architecture`。

每个 Planned Change 必须回到 Requirement、Acceptance、Architecture obligation、Preservation/Regression、Operational Obligation 或合法 defect/risk basis；没有依据则移除。

### 4. Build Traceability

建立：
`Upstream Obligation → Slice / Task → Verification`

产品语义额外建立：
`Requirement → binding Atom → Construction Coverage → Verification`

必须覆盖 Included Requirement、binding Atom、Acceptance、Current Stage architecture constraints、Preservation/Regression 与 triggered Operational Obligations。每个 Task 也必须反向回到至少一个上游义务。

binding Atom 只有 ID 引用不算覆盖；其真实行为必须有施工与验证落点。缺任一落点则 `BLOCKED`。

不创建 AC / Evidence 编号。

### 5. Build Vertical Slices

先找可独立成立的能力边界，再切 Slice，再拆 Task。底座 Stage 优先可复用、可独立验证的技术能力，不强行串成产品剧情。

Slice 的字段、Capability Test 与 UI / migration / generated artifact 规则见 `references/slice-task-design.md`。

### 6. Compile Tasks

每个 Task 使用 `slice-task-design.md` 的字段与粒度。Targets 尽量精确到 File / Symbol / Route / Schema / Config / Test target / generated artifact；Actions 沿唯一批准路径描述状态变化，不写大段伪代码。

只有触及 owner / authority / boundary / required reuse 时才写最小 `Implementation Constraints`；只有 Operational Obligation 被触发时才写 `Operational Work`；只有并行有价值时才写 parallel fields；只有 Delegation Gate 通过时才写 Delegation fields。

编译完成后计算 Reasoning。Score >10，或 Goal / contract / repository truth / proof / state/failure/order 仍未关闭，则不得进入 Execution Graph。

### 7. Build Execution Graph

按真实依赖排序，并主动寻找安全并行：
`freeze shared boundary → fan-out parallel Tasks → fan-in integration → Slice Capability Test`

Task / Slice parallel-safe 判定、write surface、independent commit 与 `Parallel Work Recommendation` 由 `references/parallel-construction.md` 单独拥有。

Parallel Work 面向 Human / 多窗口；Delegation 面向单 Root 是否创建新模型上下文，二者互不自动推出。

### 8. Assign Proof & Verification

新增 proof 前先确认它解决具体 Live Uncertainty / Acceptance / defect regression / admitted risk。

- Task：最便宜且足够的 Local Proof，可为 existing/static evidence；不默认全仓 tests。
- Slice：真实能力路径，只覆盖能力成立所需关键行为和已触发边界。
- Stage：Outcome、Acceptance、Direct Regression、Operational Obligations、Stop Rule；不是全产品 regression。

每项证据归真正有能力证明的一方：`Agent | Human | External`。Agent 不伪造 Human/External PASS，本可机械证明的也不转嫁 Human。

完整策略见 `references/verification.md`。

### 9. Route Exceptions

只用 `BLOCKED`：

- `Owner: Blueprint`：Stage / Architecture 均成立，但 Task 拆分、顺序、target、proof、Reasoning 或 Execution Graph 不合格；Blueprint 自己修正。
- `Owner: Architecture`：继续需要改变 Stage Scope/Acceptance、Decision、owner/authority、core boundary、dependency/provider/security/consistency/compatibility/migration/operational architecture。
- `Owner: Product`：继续需要决定 Product Outcome/Rule、actor/ownership/permission 产品语义、不可逆行为、商业行为、用户可见失败或 acceptance meaning。

### 10. Dry Run

Dry Run 只检查合同可执行，不做开放式 bug hunting / edge-case brainstorming。

从真实 Entry 机械模拟到 Exit，检查：
- Path/Symbol/Schema/Command 可解析，Prerequisite 与产出依赖成立。
- Slice 形成真实能力状态，UI/Client 未被无理由拖后。
- Requirement / binding Atom / Acceptance / Architecture / Preservation / Operational obligation 有施工与 proof 落点。
- Implementation Shape 足以避免 Construction 重新决定 owner / authority / dependency / bypass。
- 每个 Task 有合法 basis、Low/Medium Reasoning、确定 proof；每个 Delegation/parallel recommendation 合法。
- defensive work 通过 guardrail，Direct Regression 克制，Non-Scope 未进入执行图。
- 真边界未被 Mock 掩盖，无明显重复验证。
- 运行义务同步施工。
- 最终达到 Exit / Stop Rule。

Dry Run 新想到的“万一”重新走 Risk Gate，不能自动扩 Scope。Blueprint 缺口就修正；Product/Architecture 缺口则 BLOCKED。合同 READY 后停止找新工作。

## Completion Gate

只有同时满足以下条件才输出 `READY`：
- Stage Contract 有效，Entry State 已验证；无未决 Product / Architecture Decision。
- Scope 只含 Current Stage 授权工作。
- Requirement、binding Atom、Acceptance、Architecture/Preservation/Operational obligation 均有施工与验证覆盖。
- Implementation Shape 在相关处明确 owner / reuse / dependency / bypass / change boundary，且未私自创建新长期 authority/boundary。
- 每个 Task 有上游依据、精确 Target/Actions/Local Proof/Done When，Reasoning 仅 Low/Medium 且 ≤10；关键设计空间已关闭。
- 默认 Root 直接施工；任何 Delegation / parallel work 均通过相应 Gate。
- Execution Graph 可执行，验证分层无明显重复，真边界有足够真实证据。
- Confirmed Defect 修根因；admitted risk 有相称处理；低分假想风险不进 Scope。
- Operational Obligations 与相关施工同步。
- Explicit Non-Scope 保持在执行图外。
- Dry Run 从 Entry 到 Exit，Stop Rule 可机械判断；READY 后无 Trigger 不继续 hardening/testing/scope expansion。
- 当前合同无废弃 Task、失效占位或平行合同。

否则输出 `BLOCKED`，给当前阻塞点；多个缺口按依赖顺序列出，不创造新状态。

## Execution Contract 与 Handoff

每个 Stage 只维护：
`docs/blueprint/stages/Stage-<N>.md`

固定结构与字段只由 `references/docs-spec.md` 定义。

READY 后交给 Construction Agent。Construction：
- 按 Execution Graph 与 Slice/Task 依赖推进，不假设全程串行。
- 按 `Reasoning: Low | Medium` 执行；Low 不开放搜索，Medium 只做冻结边界内局部判断。
- 如果 Medium 仍不足以唯一推进，停止并回 `BLOCKED`，不得自行升 High。
- 默认 Root 执行；只有合同明确 Delegation 才 spawn，Child 遵守 scope/boundary/fan-in 且不得递归。
- Human feedback 可以修正当前 Task，但不得把当前 Task 扩成后续 Task。
- 遵守 Architecture / Engineering Standards / Implementation Shape，复用 owner/authority/public path，不创建第二套业务规则。
- 开工前读取 Parallel Work Recommendation；并行 Task 独立 proof / commit，fan-in 后按需要运行一次 Slice Capability Test。
- triggered Operational Obligations 随相关行为同步实现。
- 不因 Task 失败自行改变产品或架构；Slice 能力未成立时不继续依赖它的后续扩建。

Verifier 主链：
`Product binding Atoms → Architecture Ownership / Authority → Stage Contract → Execution Contract / Implementation Shape → Implementation → Evidence`

Blueprint 不预造大量 Evidence ID；只需验证位置与可重复步骤清楚。

## References

按需加载，不默认一次读完：
- `references/repository-intake.md`：Repository Reality 扫描与冲突。
- `references/product-refinement-boundary.md`：Product Focused Refinement 门禁。
- `references/planning-guardrails.md`：defect / risk / live uncertainty / stop。
- `references/reasoning-policy.md`：Task Reasoning 编译。
- `references/delegation-policy.md`：Subagent 准入。
- `references/slice-task-design.md`：Slice / Task / Implementation Shape。
- `references/parallel-construction.md`：多人/多窗口并行。
- `references/verification.md`：三层验证与 authority。
- `references/operational-obligations.md`：运行义务施工与 evidence。
- `references/docs-spec.md`：Execution Contract 唯一结构。

核心质量标准：Construction Agent 能否从真实 Repository Entry State 沿唯一已批准路径完成 Current Stage，并以最小充分证据证明纵向能力和最终 Outcome。准确、可执行、早集成、少重复；不要把模型自己的焦虑编译成项目工作量。

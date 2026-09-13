# Stage Design

用于 `docs/architecture/ROADMAP.md` 与 `stages/Stage-<N>.md`。Product Evolution 描述产品如何成长；Architecture Roadmap 决定建设顺序，两者不可混用。

## Architecture Roadmap

Roadmap 由 Architecture 拥有，输入包括 Accepted `Requirement-n`、Current binding `Atom-n` / Representative Example、Product Outcome / Current MCO、Architecture-Shaping capabilities、Foundational Dependencies、Repository Reality、Risk / Appetite。

每个 `Stage-n` 应：

1. 完成后系统仍可运行。
2. 形成真实可观察 Product Outcome，或验证不可拖延的高风险 Foundational 假设。
3. 尽量纵向贯穿必要层，不按 DB/API/UI 横切。
4. 不依赖未来 Stage 才能正确成立。
5. 高风险真实链路尽早验证。
6. 基础设施只建到当前或紧邻 Stage 实际使用程度。
7. 不牺牲 correctness / security / data integrity 换进度。
8. 过大时优先缩 Scope，而不是降低完成标准。

Stage 过大时优先：`Defer → Split → 缩小场景 → 缩小角色范围 → 缩小增强能力`；每次收缩后重新检查 Product Outcome 是否仍完整。

ROADMAP 每个 Stage 最低表达：

```text
Stage-n / Name
Outcome
Visible Delta
Included Requirements
Architecture Delta
Dependencies
Entry / Exit
Definition of Enough
Appetite / Window (有依据时)
Key Risks
```

Operational Obligations / Verification 可摘要；未来 Stage 不提前写完整 Contract。只有存在可靠容量 / deadline 时写 Target Window / Date、Critical Path、External Dependencies、Buffer、Parallelizable Work；否则只写 Dependency Order、Appetite、Relative Size、Risk。

## Stage Contract

Current Stage 开工前冻结。

### 1. Identity

`Stage-n`、Name、Included `Requirement-n`。

### 2. Outcome

写用户 / 调用方 / 系统完成后真正得到什么；“完成 UserService 模块”不是 Product Outcome。

### 3. Binding Product Semantics

列出 Included Requirement 中不能在施工翻译中丢失的 `Atom-n` / Representative Example，例如：

```text
Requirement-7 → Atom-42, Atom-43, Atom-44
Representative Example: <source reference>
```

Atom 原文仍以 `Product-Atoms.md` 为权威；Stage Contract 只引用，不重写成更弱语义。技术手段不能替代产品义务。

### 4. Entry State

来自真实 Repository / 已关闭 Stage Baseline。

### 5. Exit State / Visible Delta

明确完成后哪些事实变真。

### 6. Authorized Scope

允许改变哪些能力、模块、接口、数据或运行行为，不穷举文件。

### 7. Affected Domains / Ownership / Authorities

明确触达的 Domain / Module、关键 state/rule/lifecycle owner、必须复用的 Semantic Authority、允许新增的 dependency edge。

如果需要新增 / 改变长期 Domain Owner、Semantic Authority、核心模块边界或 dependency direction，而 Architecture 尚未决定：

`ARCHITECTURE DECISION REQUIRED`

### 8. Architecture / Platform Delta

只写本 Stage 新增 / 改变的真正架构能力。

### 9. Applied Decisions / Standards

引用 `Decision-n` 与 `ENGINEERING_STANDARDS.md § Section`，不复制完整规则。

### 10. Operational Obligations

只写本 Stage 新触发 / 改变的 Logging、Product Event、Crash/Error、Metrics、Tracing、Audit、Backup/Recovery、Alerting、Feature Flag/Kill Switch；未触发不填空表。

### 11. Verification Plan

说明 Task / Slice / Stage 三层中实际需要证明什么；同一事实不重复。

### 12. Dependencies

前置 Stage / Provider / environment / migration 等。

### 13. Preservation / Direct Regression

只列本 Stage 直接影响且必须继续成立的既有行为。

### 14. Acceptance Criteria

写成可判断真假的结果，不写“体验良好”“代码优雅”。

### 15. Explicit Non-Scope

列出容易被顺手带入但明确不做的事项。

### 16. Escalation Triggers

包括 repository data shape 与架构假设冲突、Provider 限制低于已核实结论、Product semantics 关键缺口、Stage 无法在 Appetite 内完整成立、需要改变 Foundational Decision，或需要新增长期 Domain Owner / Semantic Authority / 核心模块边界 / dependency direction。

### 17. Stop Rule

Acceptance + Invariants + Preservation / Direct Regression + triggered Operational Obligations 全部满足即完成；不得因完整产品仍有 Future 能力而扩大 Current Stage。

## Stage Baseline

Stage 关闭后保留最终 Contract、Exit State、关键 Architecture Delta、适用 Decision、Acceptance / Direct Regression / Operational Obligation 证据摘要和仍有效 Revisit Trigger，供后续 Restore；不保存完整施工日志。

## Product Refinement Gap

Requirement 已 Accept，但缺失产品细节会改变 Scope、data/state、ownership/permission、irreversible behavior、failure semantics 或 acceptance outcome 时，输出 `PRODUCT CLARIFICATION REQUIRED`。UI / local interaction / implementation 细节不阻塞 Stage Freeze。

## 禁止模式

- Stage Contract 写具体文件 / 函数 / Task 顺序。
- 为未来 Stage 提前写施工级细节。
- 把 Product Evolution 当 Architecture Roadmap。
- 按技术层横切 Stage。
- 每 Stage 重复整个 Observability baseline 或全项目测试套件。

# Stage Design

用于 `docs/architecture/ROADMAP.md` 与 `stages/Stage-<N>.md`。

## Architecture Roadmap 的职责

Product Definition 的 Product Evolution 描述产品希望如何成长；Architecture Roadmap 决定建设按什么顺序发生。

Roadmap 由架构层拥有，不写回 `docs/product/`。

输入：

- Accepted `Requirement-n`
- Binding `Atom-n` / Representative Example for Current Requirements
- Product Outcome / Current Minimum Complete Outcome
- Architecture-Shaping capabilities
- Foundational Dependencies
- Repository Reality
- Risk / Appetite

## Stage 划分原则

每个 `Stage-n` 应尽量满足：

1. 完成后系统仍能运行。
2. 形成一个真实可观察的 Product Outcome，或验证一个不可拖延的高风险 Foundational 假设。
3. 尽量纵向穿过必要层，不按“先数据库 / 后 API / 再 UI”横切。
4. 不依赖未来 Stage 才能正确成立。
5. 高风险真实链路尽早验证。
6. 基础设施只建设到当前或紧邻 Stage 实际使用程度。
7. 不降低正确性、安全、数据完整性换取进度。
8. Stage 过大时优先缩 Scope，而不是降低完成标准。

## Stage 过大时的收缩顺序

优先：

`Defer → Split → 缩小场景 → 缩小角色范围 → 缩小增强能力`

每次收缩后重新检查 Product Outcome 是否仍完整成立。

## ROADMAP.md 每个 Stage 最低字段

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

Operational Obligations 和 Verification 可以只摘要；完整当前 Stage 内容在 Stage Contract。

不要为每个未来 Stage 提前写完整 Contract。

排期规则：有可靠容量 / 截止约束时可写 Target Window / Date、Critical Path、External Dependencies、Buffer、Parallelizable Work；没有可靠容量时只写 Dependency Order、Appetite、Relative Size、Risk，不伪造精确日期。

## Stage Contract

Current Stage 开工前冻结。

### 1. Identity

- Stage-n
- Name
- Included Requirement-n

### 2. Outcome

用户 / 调用方 / 系统完成后真正得到什么。

禁止写“完成 UserService 模块”作为 Outcome。

### 3. Binding Product Semantics

列出本 Stage Included Requirement 对应、不能在施工翻译中丢失的 `Atom-n`。

示例：

```text
Requirement-7 → Atom-42, Atom-43, Atom-44
Representative Example: <source reference>
```

Atom 原文仍以 `Product-Atoms.md` 为权威；Stage Contract 不重新摘要成更弱语义。

技术手段（例如“传递 referenceId”）不能替代产品义务（例如“AI 必须理解被引用内容并修改原对象”）。

### 3. Entry State

必须来自真实 Repository / 已关闭 Stage Baseline。

### 4. Exit State / Visible Delta

明确完成后哪些事实变真。

### 5. Authorized Scope

允许改变哪些能力、模块、接口、数据或运行行为。

不需要穷举每个文件。

### 6. Affected Domains / Ownership / Authorities

明确：

- 本 Stage 触达哪些 Domain / Module。
- 哪个 Domain 拥有关键 state / rule / lifecycle。
- 本 Stage 必须复用哪些 existing Semantic Authority。
- 是否允许新增 dependency edge。

如果需要新增 / 改变长期 Domain Owner、Semantic Authority、核心模块边界或 dependency direction，而上游 Architecture 尚未决定：

`ARCHITECTURE DECISION REQUIRED`

### 7. Architecture / Platform Delta

本 Stage 新增 / 改变哪些真正的架构能力。

### 8. Applied Decisions / Standards

引用相关 `Decision-n` 和 `ENGINEERING_STANDARDS.md § Section`，不复制整篇规则。

### 9. Operational Obligations

只写本 Stage 触发的：

- Logging
- Product Event
- Crash / Error
- Metrics
- Tracing
- Audit
- Backup / Recovery
- Alerting
- Feature Flag / Kill Switch

未触发的不填空表。

### 10. Verification Plan

说明实际需要：

- Task 简单测什么。
- Slice 能力功能测什么。
- Stage 模块测什么。

同一事实不重复。

### 11. Dependencies

前置 Stage / Provider / environment / migration 等。

### 12. Preservation / Direct Regression

只列本 Stage 可能直接影响、必须继续成立的既有能力。

### 13. Acceptance Criteria

写成可判断真假的结果，不写“体验良好”“代码优雅”。

### 14. Explicit Non-Scope

容易被顺手带入当前 Stage、但明确不做的事项。

### 15. Escalation Triggers

例如：

- Repository data shape 与架构假设不符。
- Provider 限制低于已核实结论。
- Product semantics 出现关键缺口。
- Stage 无法在 Appetite 内完整成立。
- 需要改变 Foundational Decision。
- 需要新增 / 改变长期 Domain Owner、Semantic Authority、核心模块边界或 dependency direction。

### 16. Stop Rule

当 Acceptance + Invariants + Preservation / Direct Regression + triggered Operational Obligations 全部满足，即 Stage 完成。

不得因为完整产品还有 Future 能力继续扩大当前 Stage。

## Stage Baseline

Stage 关闭后保留：最终 Contract、Exit State、关键 Architecture Delta、适用 Decision、Acceptance / Direct Regression / Operational Obligation 的最终证据摘要，以及仍有效的 Revisit Trigger。后续 Stage 从这个 Baseline 恢复现实，不重复重做已关闭决策。

## Product Refinement Gap

当 Requirement 已 Accept，但缺少的产品细节会改变：

- Scope
- data / state
- ownership / permission
- irreversible behavior
- failure semantics
- acceptance outcome

则 `PRODUCT CLARIFICATION REQUIRED`。

其他 UI / local interaction / implementation 细节不阻塞 Stage Freeze，交给后续 Product Refinement 或 Blueprint。

## 不要做

- Stage Contract 塞文件 / 函数 / Task 顺序。
- 每个未来 Stage 提前写施工级细节。
- 把 Product Evolution 当 Architecture Roadmap。
- Stage 为了省事按技术层横切。
- 每个 Stage 重复整个项目 Observability 清单。
- 每个 Stage 重复整个全项目测试套件。

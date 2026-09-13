# Architecture Docs Spec

规定 `docs/architecture/` 的最小权威文档、唯一落点和命名纪律。目标：少文档、单一事实、可直接被 Blueprint 使用。

## 1. 默认文档树

```text
docs/architecture/
├── README.md
├── ARCHITECTURE.md
├── TECH_STACK.md
├── PROJECT_STRUCTURE.md
├── ENGINEERING_STANDARDS.md
├── EXTERNAL_SERVICES.md
├── OBSERVABILITY.md
├── DECISIONS.md
├── ROADMAP.md
└── stages/
    └── Stage-<N>.md
```

已有项目可沿用等价结构，不为模板强制搬家。

## 2. 命名与引用

跨文档对象只沿用 `Requirement-n`，并由 Architecture 创建 `Decision-n` 与 `Stage-n`。不得创建 `R-n`、`H-n`、`ES-n` 等二次编号。

工程规则引用：`ENGINEERING_STANDARDS.md § <Section>`。

产品长期依据直接引用 `Product-Definition.md § <Section>`、Capability / Requirement 名称或相关 `Atom-n`。

## 3. 内容路由

| 内容 | Source of Truth |
|---|---|
| 当前架构入口、Current Stage、文档索引 | `README.md` |
| Scope、System / Domain / Module / Data / Runtime / Interface / Quality、长期驱动、Invariants | `ARCHITECTURE.md` |
| 技术栈当前选择 | `TECH_STACK.md` |
| 项目结构、职责、边界、依赖方向 | `PROJECT_STRUCTURE.md` |
| 跨项目工程规则 | `ENGINEERING_STANDARDS.md` |
| 外部服务 / Provider / Build-Buy / 数据成本锁定 | `EXTERNAL_SERVICES.md` |
| 项目级 Observability 基线 | `OBSERVABILITY.md` |
| 高影响架构决策完整论证 | `DECISIONS.md` |
| Stage 顺序与路线 | `ROADMAP.md` |
| Current / historical Stage Contract | `stages/Stage-<N>.md` |

同一事实只保留一个完整正文；其他位置摘要 + 引用。

## 4. README.md

保持短，只包含：Current Architecture Baseline 一句话、Current Stage、核心技术栈摘要、文档索引、当前真正未决的架构问题。不要复制 ARCHITECTURE / TECH_STACK 正文。

## 5. ARCHITECTURE.md

建议结构：

- **Product & Long-term Drivers**：只记录影响技术的产品事实与必要规模假设，直接引用产品权威来源。
- **Scope Decisions**：按原 `Requirement-n` 记录 `Scope Result | Why | Revisit Trigger / Accepted Stage`。
- **System Context**
- **Domain Ownership / Semantic Authority**
- **Module Model**
- **Data Model**
- **Runtime Model**
- **Interface Model**
- **Quality Model**
- **Conditional Domain Decisions**：只写被触发域，不建立固定空章节。
- **Architecture Invariants**
- **Deferred / Architecture Debt / Revisit**：只保留有具体 Revisit Trigger 的事项；Debt 至少写 Reason、Impact、Trigger、Repair Path。

`Split` 不创建新的架构需求 ID：若只是建设拆分，在同一 `Requirement-n` 下写 Accepted / Deferred Part；若改变产品语义或形成新独立产品需求，回产品层创建新的 `Requirement-n`。

## 6. TECH_STACK.md

作为技术索引，不写长论证。建议：

```text
Capability | Decision | Status | Why | Needed By | Revisit Trigger | Decision Ref
```

Status 只使用 `Decided | Deferred | Not Applicable`。核心能力明确；纯条件能力未触发可不建行。高影响决定引用 `Decision-n`。

## 7. PROJECT_STRUCTURE.md

只展开到模块边界足够清楚：tree、`[existing] / [new] / [reserved]`、目录 / 关键文件责任、Domain / Feature ownership、public/internal boundary、dependency direction、Shared/Common 边界、schema / migration / config / tests / generated / docs 归属、Current Stage 主要触达区域。

不列所有普通源文件，不提前写 Blueprint 级文件结构。

## 8. ENGINEERING_STANDARDS.md

章节与详细规则以 `engineering-standards.md` 为准。只存跨 Stage / 模块稳定规则，不使用 `ES-n`；一条规则尽量一句清楚，只有复杂或易误解规则补简短例子。

## 9. EXTERNAL_SERVICES.md

重要 Provider 建议字段：

```text
Capability | Mode | Provider | Why | Data Impact | Cost Shape | Limits | Failure / Degradation | Lock-in | Exit | Revisit
```

只有真正需要说明数据流、凭证边界、webhook / failure semantics 的 Provider 才增加小节。详细选择标准以 `technology-selection.md` 为准。

## 10. OBSERVABILITY.md

只记录项目实际适用的 Observability Baseline：Applicable Types、Critical Flows / State Transitions、Runtime Visibility、Sink Readiness、Correlation、命名 / 公共字段、Privacy / Redaction、触发的 Alert / Recovery、Stage Integration Rule。

不要为六类能力创建空模板；细则以 `observability.md` 为准。

## 11. DECISIONS.md

只收高影响 `Decision-n`。索引可用：

```text
ID | Decision | Area | Revisit Trigger
```

每条完整论证按 `technology-selection.md` 的 Foundational Decision 结构。普通 Reversible Decision 不进 DECISIONS。若项目保留历史 ADR，superseded 记录不得与当前决定同时看起来有效。

## 12. ROADMAP.md

由 Architecture 拥有。每个 `Stage-n` 最低表达：

```text
Stage | Outcome | Visible Delta | Requirement-n | Architecture Delta | Dependencies | Definition of Enough | Appetite / Window | Risk
```

未来 Stage 只写规划所需深度；完整 Current Stage Contract 以 `stage-design.md` 为准。

## 13. stages/Stage-<N>.md

字段以 `stage-design.md` 为唯一详细 owner。Current Stage Contract 是 Blueprint 的 Stage 权威，不复制 Blueprint Task。Stage 关闭后保留最终 Contract / Exit / 关键 Architecture Delta / 证据摘要作为 Stage Baseline。

## 14. 文档纪律

- 当前事实优先，不写讨论流水账。
- 一个事实一个 Source of Truth；详细论证只在真正需要的位置出现。
- 技术事实变化时同步更新受影响文档。
- Stage 关闭后保留 Baseline。
- 文档让下游少猜，不让文档本身成为额外流程税。

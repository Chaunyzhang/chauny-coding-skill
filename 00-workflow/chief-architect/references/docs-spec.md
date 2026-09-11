# Architecture Docs Spec

规定 `docs/architecture/` 的最小权威文档、唯一落点和命名规则。

目标：少文档、单一事实、可直接被 Blueprint 使用。

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

已有项目可以使用等价结构，不为迁就模板强制搬家。

## 2. 唯一命名

跨文档对象只使用：

- `Requirement-n`：产品上游原编号。
- `Decision-n`：高影响架构决定。
- `Stage-n`：建设阶段。

不得创建 `R-n`、`H-n`、`ES-n` 或其他二次编号。

引用工程规则用：

`ENGINEERING_STANDARDS.md § <Section>`

引用产品长期依据直接用：

`Product-Definition.md § <Section>` 或明确 Capability / Requirement 名称。

## 3. 内容路由

| 内容 | Source of Truth |
|---|---|
| 当前架构入口、Current Stage、文档索引 | `README.md` |
| Scope 裁决、System / Module / Data / Runtime / Interface / Quality、长期驱动、Invariants | `ARCHITECTURE.md` |
| 技术栈当前选择 | `TECH_STACK.md` |
| 项目结构、职责、依赖方向 | `PROJECT_STRUCTURE.md` |
| 全项目工程规则 | `ENGINEERING_STANDARDS.md` |
| 外部服务 / Provider / Build-Buy / 数据成本锁定 | `EXTERNAL_SERVICES.md` |
| Observability 项目级基线 | `OBSERVABILITY.md` |
| 高影响架构决策完整论证 | `DECISIONS.md` |
| Stage 顺序与路线 | `ROADMAP.md` |
| Current / historical Stage Contract | `stages/Stage-<N>.md` |

同一事实不要在多个文件复制完整正文；摘要 + 引用即可。

## 4. README.md

保持短：

1. Current Architecture Baseline 一句话。
2. Current Stage。
3. 核心技术栈摘要。
4. 文档索引。
5. 当前真正未决的架构问题。

不要在 README 复制 ARCHITECTURE / TECH_STACK 内容。

## 5. ARCHITECTURE.md

建议结构：

### Product & Long-term Drivers

只记录影响技术的产品事实和必要规模假设；直接引用 Product Definition。

### Scope Decisions

按原 `Requirement-n`：

```text
Requirement | Scope Result | Why | Revisit Trigger / Accepted Stage
```

`Split` 时不创建新的架构需求 ID：

- 若只是建设时拆分，同一 `Requirement-n` 下写 Accepted Part / Deferred Part。
- 若拆分实际改变产品语义、产生新的独立产品需求，回产品层创建新的 `Requirement-n`。

### System Context
### Domain Ownership / Semantic Authority

记录核心 Domain 的 responsibility、owned state / rules / lifecycle，以及跨模块共享产品语义的唯一 authority。

### Module Model
### Data Model
### Runtime Model
### Interface Model
### Quality Model
### Conditional Domain Decisions

只写被触发域的结论，不建立固定 17 域空章节。

### Architecture Invariants
### Deferred / Architecture Debt / Revisit

只记录有具体 Revisit Trigger 的未来架构事项或非阻塞技术债；默认不编号。Architecture Debt 至少写 Reason、Impact、Trigger、Repair Path。

## 6. TECH_STACK.md

技术索引，不写长论证。

建议字段：

```text
Capability | Decision | Status | Why | Needed By | Revisit Trigger | Decision Ref
```

Status 只使用：

- Decided
- Deferred
- Not Applicable

核心能力行应明确；纯条件能力未触发时可以不创建行，不为“完整表格”扩张文档。

高影响决策的完整理由引用 `Decision-n`。

模块结构必须表达 Domain / Feature ownership、public/internal boundary、dependency direction 与 Shared / Common 的允许范围。

## 7. PROJECT_STRUCTURE.md

只展开到模块边界足够清楚：

- tree
- `[existing] / [new] / [reserved]`
- directory / key file responsibility
- dependency direction
- schema / migration / config / tests / generated / docs 归属
- Current Stage 主要触达区域

不列所有普通源文件。

## 8. ENGINEERING_STANDARDS.md

固定章节优先：

- Naming
- Repository & Modules
- Dependencies
- API / Interface
- Data
- Errors
- Security
- Observability
- Testing
- Compatibility / Migration
- Third-party
- Documentation

不使用 `ES-n`。一条规则一句清楚正文；只有复杂 / 容易误解的规则才增加简短例子。

## 9. EXTERNAL_SERVICES.md

表：

```text
Capability | Mode | Provider | Why | Data Impact | Cost Shape | Limits | Failure / Degradation | Lock-in | Exit | Revisit
```

只有真正需要解释数据流、凭证边界、webhook / failure semantics 的 Provider 才增加小节。

## 10. OBSERVABILITY.md

只写项目实际适用：

1. Applicable Types
2. Critical Flows / State Transitions
3. Runtime Visibility
4. Sink Readiness
5. Correlation
6. Event / Log Naming and common fields
7. Privacy / Redaction
8. Alert / Recovery when applicable
9. Stage Integration Rule

不要为六类能力都创建空模板。

## 11. DECISIONS.md

只收高影响 `Decision-n`。

索引：

```text
ID | Decision | Area | Revisit Trigger
```

每条按 `technology-selection.md` 的 Foundational Decision 结构记录。

普通可逆选择不进 DECISIONS。

当前文档以当前有效决定为主；项目确需保留历史 ADR 时可以保留 superseded 记录，但不得让旧决定与当前决定同时看起来有效。

## 12. ROADMAP.md

Architecture Roadmap，由架构层拥有。

每个 `Stage-n`：

```text
Stage | Outcome | Visible Delta | Requirement-n | Architecture Delta | Dependencies | Definition of Enough | Appetite / Window | Risk
```

未来 Stage 只写足够规划的深度，不提前写完整施工合同。

## 13. stages/Stage-<N>.md

字段以 `stage-design.md` 为准。

Stage Contract 是后续 Blueprint 当前唯一 Stage 权威，不复制 Blueprint Task。Stage 关闭后该文件作为 Stage Baseline 保留最终 Contract / Exit / 关键架构变化和证据摘要。

## 14. 文档纪律

- 当前事实优先，不写讨论流水账。
- 一个事实一个 SoT。
- 详细论证只在真正需要的位置出现。
- 技术选择变化时同步更新受影响文档。
- Stage 关闭后保留 Baseline。
- 文档内容应让下游少猜，而不是让文档本身成为额外工作量。

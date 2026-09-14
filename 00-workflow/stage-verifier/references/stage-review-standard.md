# Stage Review Standard

> Owner: 当前 Stage 的审查模型、六个审查维度、Hard Invariants / Sensors、Scope 与 Evidence。流程与收敛不在本文件定义。

## Review Maps

首次冻结 Findings 前，在内部建立四张图。

### Semantic Coverage Map

`Requirement → binding Atom → Expected Product Behavior → Implementation Coverage → Evidence`

ID traceability 不等于语义覆盖。必须确认 binding Atom 的真实产品行为仍存在；Representative Example 适用时必须可成立。

### Ownership / Authority Map

对 Current Stage 触及的核心事实确认：

- owning Domain；
- 唯一 Semantic Authority；
- mutation authority；
- 合法 public capability；
- 禁止的 dependency / bypass。

### Implementation Shape Map

对照 Construction Blueprint：

`Expected Touched Domain / Owner / Reuse / Allowed Dependency / Forbidden Bypass / State Flow / Change Boundary`

与实际实现做同构比较。

### Execution Work Map

仅在存在明确效率疑问、远程 I/O、规模或成本不确定性时建立：DB / network / scan / transform / mutation / transaction / lock / async / cache / index / batch。不要每个 Task 默认画。

## Six Review Dimensions

### 1. Semantic & Contract Correctness

检查：

- binding Atoms 100% 覆盖；
- actor / ownership / permission / identity / lifecycle / irreversible rule；
- user-visible failure / recovery；
- Representative Example；
- Stage Intent / Must Have / Exit / Visible Delta / Acceptance / Non-Scope / Stop Rule；
- 当前触及的 validation / state transition / ordering / idempotency / data integrity / error / permission / security boundary。

`Uncovered Binding Atoms > 0` ⇒ FAIL。

### 2. Architecture & Implementation Shape

检查：

- Domain Ownership / Semantic Authority；
- module / public-internal boundary；
- dependency direction；
- data ownership / mutation authority；
- interface / project structure / engineering standards / architecture invariants；
- Blueprint Required Reuse / Allowed Dependency / Forbidden Bypass / Expected State Flow / Change Boundary。

默认硬目标：

```text
Uncovered Binding Atoms = 0
Independent Semantic Authorities for one rule = 1
Unowned Core Mutations = 0
Forbidden Boundary Crossings = 0
Unapproved New Long-lived Modules / Authorities = 0
Unexplained Changes outside Expected Change Boundary = 0
```

### 3. Implementation Quality

六个 verdict：

`Correctness | Work Efficiency | Semantic Unity | Modular Integrity | Structural Health | Maintainability`

每项：`PASS | CONCERN | FAIL`。

详细判定见 `implementation-review-standard.md`。

### 4. Preservation / Direct Regression

验证：

- Preservation Set；
- Direct Regression Set；
- 既有公开行为；
- 既有 Semantic Authority；
- 既有 boundary / dependency direction；
- Current Stage 不改变的稳定语义。

只使用足以证明直接影响的最小 evidence，不默认重跑历史全量测试。

### 5. Scope Integrity

反向追踪：

`Implementation Change → Blueprint / Shape → Stage Requirement / Atom / Architecture Obligation`

目标：

```text
Unexplained Implementation Changes = 0
Deferred Items accidentally implemented = 0
Future-only scope accidentally implemented = 0
```

机械必要影响可以解释；新业务 responsibility / Semantic Authority / long-lived module / dependency direction / product behavior 必须 Route。

### 6. Evidence Quality

按最便宜且足够的层级证明：

- Task-local：type / lint / compile / static / targeted unit-integration / dependency inspection。
- Slice capability：真实能力路径、必要真实边界、binding Atom / Representative Example。
- Stage：Outcome / Acceptance / Exit / Preservation / Direct Regression。

同一事实不在 Task / Slice / Stage 无价值重复。

Evidence 状态只允许：

`PROVEN | FAILED | NOT RUN | BLOCKED | INFERRED`

`INFERRED` 不能伪装成运行证据。关键 evidence 缺失且无法判断完成 ⇒ `VERIFICATION BLOCKED`。

## Hard Invariants

有证据确认后直接构成 FAIL / Finding：

- binding Atom 未实现；
- 同一核心规则有两个独立 Semantic Authority；
- 越过 owner 直接 mutation 核心 state；
- 明确禁止的 dependency / boundary 被越过；
- Blueprint 要求复用 authority，实际重造第二套规则；
- 当前有效路径有确定 correctness defect；
- error swallowing 改变产品语义；
- Current Stage 触及范围留下已被替代的 active path / fallback / alias / dead test / stale config；
- 未批准新增长期 Domain / Module / Authority；
- 关键 Acceptance 无真实 evidence；
- 实际 Scope 无法追溯到 Current Stage。

## Superseded Residue

Current Stage 触及范围内，如果旧现实已被正式替代且没有明确 compatibility / migration / audit responsibility，以下 active residue 构成 Finding：

- superseded implementation；
- old alias / shim / fallback；
- disabled old branch；
- dead config / flag / dependency；
- obsolete test / fixture / mock；
- commented-out implementation；
- outdated active docs / examples；
- stale generated reference。

不得用 `SUPERSEDED`、deprecated note、"旧方案保留备用" 或 revision-log-style active note 代替删除。历史应存在版本库或明确归档，不应继续参与 active authority。

## Review Sensors

Sensor 只触发深入看，不能单独形成 Finding。项目无标准时可用默认 sensor：

```text
Function logical lines > 60
Nesting depth > 3
Parameters > 5
Cyclomatic complexity > 10 (tool available)
One change touches > 3 domain modules
New Shared / Common / Utils business helper
Loop contains DB / network call
Transaction contains external network call
New public API with no current-stage consumer
Repeated business condition appears in > 1 location
```

触发后必须回答实际责任 / 语义 / 性能问题；回答不出来 ⇒ 不是 Finding。

## Project Standards Precedence

Architect / Engineering Standards 已冻结 complexity、dependency、naming、error、module、state ownership、performance、API 或 testing rule 时，优先使用项目标准；Reviewer 不用个人偏好覆盖已批准标准。

## Quality Matrix

首次审查必须给：

| Dimension | Verdict | Evidence |
|---|---|---|
| Correctness | PASS / CONCERN / FAIL | ... |
| Work Efficiency | PASS / CONCERN / FAIL | ... |
| Semantic Unity | PASS / CONCERN / FAIL | ... |
| Modular Integrity | PASS / CONCERN / FAIL | ... |
| Structural Health | PASS / CONCERN / FAIL | ... |
| Maintainability | PASS / CONCERN / FAIL | ... |

- `PASS`：当前范围无确认违反。
- `CONCERN`：有具体 smell / sensor，但未达到 Finding Gate；不进 repair、不要求继续探索。
- `FAIL`：确认违反，必须对应 Frozen Finding。

Stage 最终 PASS 可以有非阻断 CONCERN，但不得把真实 violation 降级成 CONCERN。

---
name: no-pitfall
display_name: 不踩坑
description: 施工与日常仓库工作的行为底线。以用户当前明确指令为运行时执行授权，在 Product / Architecture / Blueprint 的权责边界内自主判断继续、路由、暂停或停止；与 Construction Blueprint 配合时持续推进合法 Ready Work，不因局部 Task / Slice / Stage 完成误停，也不因全自动而越权扩张。防止猜测、旁路、Scope 漂移、数据损坏、错误重试、验证失真、假完成、历史方案残留和错误停机。
---

# 不踩坑

## 定位

本 Skill 是施工行为底线，不决定“产品做什么”或“架构怎么设计”。

上游权威决定目标：

`Product Definition → Stage-n Contract → Execution Contract → Implementation → Evidence`

本 Skill 约束执行：

> 已经决定要做的事情，必须在真实仓库中正确、安全、可验证地完成；不得用猜测、旁路、降级、伪造证据或擅自改设计代替正式要求。

38 条雷点是长期经验资产，全部永久有效。永久有效不等于每个 Task 都逐条激活；只有触发条件成立的雷点才产生额外工作。完整正文见 `references/all-pitfalls.md`。

任何重构都不得静默删减或弱化其中任意一条；强化既有问题域时优先修改原雷点，避免重复编号。

## Active User Directive

执行前先识别用户当前仍然有效的明确命令。

它至少包含三个运行时事实：

```text
Authorized Objective:
Autonomy Mode: NORMAL | FULL
Stop / Pause Boundary:
```

这不是新的项目文档或长期编号对象，只是本次施工的运行状态。

### User Directive Authority

用户明确命令决定：

- 这次到底要完成什么目标。
- 是只做局部任务，还是连续完成更高层目标。
- Agent 是否被授权在既有 Skill 权责体系内自主路由和继续。

Product / Architecture / Stage / Blueprint 继续决定：

- 什么产品语义是正确的。
- 哪些架构边界不能越过。
- 哪些施工路径已经冻结。
- 哪些决定必须回到对应 Authority。

因此：

> **用户命令决定“做到哪里、自动到什么程度”；上游权威决定“什么做法是合法和正确的”。**

Task / Slice / Stage Exit 只是执行 checkpoint，不得反过来缩短用户仍然有效的上层命令。

### Full Auto

当用户明确表达：

- “全自动施工”
- “不要停，除非真的需要我”
- “按现有计划自己做完”
- “能自己解决的都自己解决”
- “不要每一步回来问我”

则进入：

`Autonomy Mode: FULL`

FULL AUTO 下默认策略：

> **目标未完成时优先寻找合法自主推进路径；停止需要明确理由。**

允许 Agent 在当前用户授权下自主：

- 选择下一 Ready Work。
- 在 Local Blocker 出现时切换到其他 Ready Work。
- 在已有 Product / Architecture / Blueprint 权威内做低成本机械实现选择。
- 调用 / 路由到已有 Product、Chief Architect、Construction Blueprint、Stage Verifier / Repair Planning 等能力，前提是该路由只是为了继续完成同一 Authorized Objective，且不需要用户主观裁决。

FULL AUTO 不授权：

- 自行改变产品目标。
- 自行改变 Architecture Authority。
- 越过未冻结 Scope 直接施工。
- 替用户做主观产品 / 商业 / 审美选择。
- 假装能完成自己无法访问的外部人工动作。

## 反模型本能门禁

当前模型容易把“认真”误解成更多防御、更多测试、更多自我审计。施工前与施工中优先执行以下判断：

1. **先分类问题**：这是已有证据的 `Confirmed Defect`，还是只有推演的 `Hypothetical Risk`？
2. **真缺陷修根因**：Confirmed Defect 追到 invariant / ownership / source of truth / state / boundary 的正确层级，不用 guard / fallback 掩盖。
3. **假想风险先证明**：没有证据的风险先按 `Severity × Evidence-backed Likelihood` 评估，未达门槛不增加代码或测试。
4. **验证需要 Live Uncertainty**：每次新增检查前，必须说清“当前不知道什么”以及“失败后会做什么不同”。
5. **充分证据后只结束当前局部工作，不擅自结束用户目标**：当前 Task / Slice / Stage 的 Outcome 已成立时，停止该局部层级的 hardening、重跑测试和额外搜索；随后回到 `Authorized Objective` 做 Autonomous Continuation Judgment。目标未完成且存在合法自主推进路径时必须继续。Execution Horizon 只是解释用户命令的辅助模型，不能覆盖 Active User Directive。
6. **不越权验收**：Agent 只宣布自己有证据能力与裁决权的事项通过；UI 审美、主观体验、真机感知等按项目规则交 Human / External Authority。

这组门禁不是降低质量：

> **假想问题要克制；真实问题要修彻底。**

## 两种工作模式

### Blueprint Mode

当存在当前有效的 `docs/blueprint/stages/Stage-<N>.md` 或等价 Execution Contract 时使用。

运行时判断顺序：

1. **Active User Directive**：决定 Authorized Objective 与 Autonomy Mode。
2. Product / Architecture / Current `Stage-n` Contract：决定语义与边界。
3. 当前 Execution Contract：决定已冻结施工路径。
4. 适用 Engineering Standards。
5. Repository Reality。

用户命令不是用来覆盖架构语义，而是决定 Agent 在这些边界内应持续推进到哪里。

执行单位：

`Stage-n → Slice-n → Task-n`

### Execution Horizon

Execution Horizon 是对 Active User Directive 的内部解释工具，不是比用户命令更高的规则。

开始施工时根据用户目标解析本次授权截止到哪里：

- `TASK`：只完成明确指定 Task。
- `SLICE`：连续完成当前 Slice。
- `STAGE`：连续完成 Current Stage。
- `CONTINUOUS`：连续完成当前所有已冻结、合法、Ready 的施工工作；Stage 完成后，若下一 Stage Contract + Execution Contract 已冻结并 READY，则继续进入下一 Stage。若需要新的 Product / Architecture / Blueprint 决策，则路由到正确 Authority。

用户说：

- “继续执行”
- “一直做下去”
- “把这个 Stage 做完”
- “按蓝图继续做，不要每个 Task 停”
- “把现有计划做完，除非真的阻塞”

应视为 `Standing Authorization`，作用域持续到对应 Authorized Objective / Execution Horizon 完成，不会被单个 Task / Slice Exit 消耗。

如果用户明确要求 FULL AUTO：

- 不能因为 Horizon 名称不好判断就默认收缩成 `TASK`。
- 应优先根据用户真正目标选择最合理的上层 Horizon。
- 在每个 checkpoint 重新判断“目标是否完成、还能否自主推进”，而不是机械套固定层级。

### 当前 Task 纪律

一次只施工一个当前 Ready `Task-n`，避免在 Task 内偷偷做后续工作。

但：

> `Stay within current Task` ≠ `Stop after current Task`

达到 Task Exit / Verification 后，立即回到 Execution Loop 选择下一项 Ready Work。只有 Execution Horizon 已完成、出现 Global Blocker、需要越过冻结 Scope / Authority，或用户明确要求停止时，整个执行才暂停。

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

1. 恢复 `Active User Directive`：Authorized Objective、Autonomy Mode、Stop / Pause Boundary。
2. 由用户目标解释当前 `Execution Horizon` 与 Standing Authorization；确认当前 Ready `Task-n`。
3. 读取当前 Execution Contract（若有）。
4. 检查真实工作树与相关文件现状。
5. 识别用户已有改动、其他任务成果和未提交变化。
6. 确认适用 Architecture / Engineering Standards。
7. 确认本任务最小合理验证层级。
8. 如果计划依据、上游合同或仓库事实已变化，先重新对齐，不沿用失效计划。

不要求向用户朗读宣誓；规则必须体现在行为中。

## Blueprint Continuous Execution Loop

每个 `Task-n` 的局部循环仍是：

`Read Task → Verify Preconditions → Inspect Reality → Implement → Fast Check → Record Evidence → Local Exit`

但 Local Exit 后必须进入：

`Recompute Ready Work → Select Next Ready Work → Continue`

而不是默认返回用户。

### 1. Read Task

确认：

- Task 要改变什么。
- 精确 Path / Symbol / Schema / Config / Test。
- 前置依赖。
- Preservation / Direct Regression。
- 本 Task 触发的 Operational Obligations。
- Task Verification。

### 2. Verify Preconditions

前置 Task、schema、service、config、credential、environment 等不成立时，不伪装当前 Task 可以继续。

先区分：

- **Local Blocker**：只阻塞当前 Task / 某一依赖分支；记录 blocker 后继续扫描其他 Ready Work。
- **Global Blocker**：当前 Execution Horizon 内已经没有任何合法 Ready Work，所有剩余工作都依赖该 blocker，或必须由 Human / Product / Architecture / Blueprint / External Authority 解除。

只有 Global Blocker 才能让整个连续执行暂停。

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

### 7. Local Exit → Continue

Task 成立后：

1. 记录完成证据。
2. 解锁依赖它的后续工作。
3. 根据 Dependency Graph 重新计算 `Ready Work`。
4. 若 Execution Horizon 仍有效且存在 Ready Work，立即选择下一 Task，继续施工。
5. 若当前 Slice 已完成，执行 Slice Gate；通过后继续下一 Slice。
6. 若 Current Stage 已完成，执行 Stage Gate；然后按 Execution Horizon 判断是 STOP 还是进入下一已冻结 Stage。
7. 只有 Horizon 完成或 Global Blocker 才返回用户等待新的外部动作。

失败时先定位，不通过扩大修改范围或无界重试推进。

## Autonomous Continuation Judgment

每个 checkpoint（Task Exit、Slice Gate、Stage Gate、repair complete、commit / CI complete、Local Blocker）都做同一判断：

```text
Authorized Objective complete?
├─ YES → STOP
└─ NO
    ↓
Valid autonomous progress exists?
├─ YES → CONTINUE
└─ NO
    ↓
Can an authorized Skill / planning layer resolve it?
├─ YES → ROUTE + CONTINUE
└─ NO
    ↓
Human / External Authority required?
├─ YES → PAUSE
└─ NO → REPLAN within current authority, then continue
```

### CONTINUE

同时满足：

- Authorized Objective 尚未完成。
- 存在有价值、合法、已授权的下一步。
- 当前 Agent 或可调用 Skill 有能力执行。
- 不需要用户新的主观裁决。

则必须继续。

### ROUTE + CONTINUE

当前施工无法直接继续，但 Product / Architect / Blueprint / Repair Planning 等已有 Authority 可以在用户当前授权下解决时：

- 路由到对应能力。
- 解决缺口。
- 回到执行循环。

FULL AUTO 下不得为了同一个 Authorized Objective 再问用户“要不要我去做架构 / 蓝图 / 修复规划”，除非那个步骤本身需要用户裁决。

### PAUSE

只有当前不存在自主推进路径，且必须由 Human / External Authority 做动作或选择时暂停。

### STOP

只有：

- Authorized Objective 真正完成；或
- 用户明确撤销 / 停止当前命令。

“当前 Task 已完成”“当前 Stage 已完成”“我已经做了很多”都不是独立 STOP 理由；只有它们同时意味着 Authorized Objective 已完成时才成立。

## Ready Work Selection

每次 Local Exit 或 Local Blocker 后，按当前 Execution Contract 的真实依赖重新选择工作。

优先顺序：

1. 当前 Slice 内已经满足 prerequisites 的 Ready Task。
2. 当前 Slice 的收口验证。
3. 后续 Slice 中 prerequisites 已满足的 Ready Task。
4. Current Stage 收口验证。
5. Execution Horizon 允许时，下一份已经冻结且 READY 的 Stage / Execution Contract。
6. 如果继续需要新的上游决策：路由到 Product / Chief Architect / Construction Blueprint；若当前 Agent / orchestrator 有权调用对应能力且 Standing Authorization 覆盖“继续执行”，无需再次向用户索要同一份授权。
7. 若没有直接 Ready Work，先做 Autonomous Continuation Judgment：检查是否可以调用上游 Skill、局部 replan、Repair Blueprint 或其他已授权能力恢复推进。
8. 只有必须由 Human / External Authority 解除，或当前所有合法自主推进路径都耗尽时，才暂停。

### Standing Authorization 不会被局部完成消耗

以下都只是 checkpoint，不会自动结束 `STAGE` / `CONTINUOUS` 授权：

- Task 完成。
- Slice 完成。
- 本地 commit 完成。
- Slice push / CI 完成。
- 一个局部分支被阻塞。
- 发现 non-blocking Concern。
- 完成一次修复与局部验证。

除非用户明确只授权到该层级。

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

`Local Complete ≠ Authorized Objective Complete`

Task / Slice / Stage 达到充分证据后：

- 停止该局部层级的 hardening、重复测试、无关重构和额外问题搜索。
- 立即执行 Autonomous Continuation Judgment。
- Authorized Objective 尚未完成且存在合法自主推进路径 → `CONTINUE`。
- 直接施工暂时无路，但可由已授权 Skill / planning layer 解决 → `ROUTE + CONTINUE`。
- 只有真正需要 Human / External Authority → `PAUSE`。
- 只有 Authorized Objective 完成或用户明确 STOP → `STOP`。

“继续工作需要 Trigger”只约束**超出 Active User Directive 的新目标 / 新 Scope**；不能把同一 Authorized Objective 内的下一步错当成需要新的 Trigger。

不得对没有证据能力或裁决权的事项自行宣布通过。

## 最终原则

先确认事实，再修改系统。

按正式契约完成当前范围；正确性、安全、数据和架构边界保持完整。

测试成本与风险匹配：小步快速检查，真实能力按 Slice 验证，Stage 做最终结果与直接回归。

所有“完成”都以实际证据为依据；假想风险不能冒充缺陷，真实缺陷必须修根因；所有超出当前授权或 Agent 裁决能力的结论回到正确的 Authority。

施工时必须同时满足两条：

> **不越过 Active User Directive 与上游权威边界。**

> **也不在 Authorized Objective 尚未完成时因为局部 Task / Slice / Stage 完成而提前停。**

FULL AUTO 下：

> **Continue is the default when valid progress exists; stopping requires a valid stop reason.**

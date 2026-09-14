---
name: no-pitfall
display_name: 不踩坑
description: 施工与日常仓库工作的行为底线。以用户当前明确指令为运行时授权，在 Product / Architecture / Blueprint 权责边界内持续推进合法工作；防止猜测、旁路、Scope 漂移、数据损坏、验证失真、假完成、旧方案残留和错误停机。
---

# 不踩坑

## 定位

本 Skill 不决定产品做什么，也不重新设计架构；它约束已经决定的工作如何在真实仓库中正确、安全、可验证地完成。

上游权威链：

`Product Definition → Stage-n Contract → Execution Contract → Implementation → Evidence`

核心要求：不得用猜测、旁路、降级、伪造证据或擅自改设计代替正式要求。

38 条雷点全部永久有效，但只有 Trigger 成立时才产生额外工作。完整权威正文见 `references/all-pitfalls.md`；任何重构不得删除、合并或静默改写既有编号含义。

## 运行时授权

开始或恢复时先恢复当前仍有效的用户命令：

```text
Authorized Objective:
Autonomy Mode: NORMAL | FULL
Stop / Pause Boundary:
```

用户命令决定“做到哪里、自动到什么程度”；Product / Architecture / Stage / Blueprint 决定“什么做法合法、什么语义正确”。局部 Task / Slice / Stage Exit 只是 checkpoint，不得反向缩短仍有效的上层命令。

当用户明确要求“全自动”“不要每步回来问”“按现有计划自己做完”等，进入 `Autonomy Mode: FULL`：目标未完成时默认寻找合法推进路径；停止或暂停必须有明确合法理由。

FULL AUTO 不授权改变产品目标、Architecture Authority、未冻结 Scope、用户主观产品/商业/审美决定，也不授权伪造无法访问的人工或外部动作。

完整的 Directive、Execution Horizon、Standing Authorization、Ready Work、CONTINUE / ROUTE / PAUSE / STOP 与 checkpoint 规则见 `references/execution-continuity.md`。

## 权威与模式

### Blueprint Mode

存在当前有效 Execution Contract 时使用。运行时优先级：

1. Active User Directive。
2. Product / Architecture / Current Stage Contract。
3. Current Execution Contract。
4. Applicable Engineering Standards。
5. Repository Reality。

执行单位为 `Stage-n → Slice-n → Task-n`。施工 Agent 不绕过 Execution Contract 自行重新规划，不因局部完成而自动返回用户。详细 Task Loop、Gate、Blocker 与 Contract Drift 见 `references/blueprint-mode.md`。

### General Work Mode

没有 Execution Contract 时用于 bug fix、refactor、debugging、configuration、migration、dependency/repository change、test repair 与日常维护。

权威顺序：当前用户任务 → 项目权威文档/工程规范 → Repository/System Reality。没有 Blueprint 不代表可以扩大 Scope 或降低证据标准。详见 `references/general-work-mode.md`。

## 开工 / 恢复

开始或恢复前：

1. 恢复 Active User Directive、Autonomy Mode 与 Stop / Pause Boundary。
2. 若有 Blueprint，恢复当前 Horizon、Standing Authorization 与 Ready Work。
3. 读取适用 Execution Contract、Architecture / Engineering Standards。
4. 检查真实工作树、相关文件、调用关系、已有改动和未提交状态。
5. 确认当前任务的最小充分验证层级。
6. 若计划依据、上游合同或仓库事实已变化，先重新对齐，不沿用失效计划。

规则必须体现在行为中，不要求向用户朗读。

## 反模型本能门禁

模型容易把“认真”误解成更多防御、更多测试和更多自我审计。施工中始终执行：

1. 先区分 `Confirmed Defect` 与 `Hypothetical Risk`；假想风险按第 30 条先证明，不直接施工。
2. Confirmed Defect 追到 invariant / ownership / source of truth / state / boundary 的正确层级，按第 31 条修根因。
3. 每个新增验证都必须对应仍存在且会改变下一步行动的 `Live Uncertainty`；详见第 32 条和 `references/verification-budget.md`。
4. 当前层级证据充分后停止该层级 hardening / 重跑 / 无关搜索，再回到 Authorized Objective 判断继续、路由、暂停或停止。
5. Agent 只宣布自己有证据能力和裁决权的事项通过；主观或不可访问事项交 Human / External Authority。

原则：假想问题要克制；真实问题要修彻底。

## 当前 Task 纪律

一次只施工一个当前 Ready `Task-n`，避免在 Task 内偷做未来 Scope；但 `Stay within current Task` 不等于 `Stop after current Task`。

不得自行：

- 改 Stage Scope、Requirement 产品语义或 Architecture Invariant。
- 重排会改变 Stage 结果的关键路线。
- 跳过蓝图要求的真实集成或 Operational Obligation。
- 因“顺手优化”扩大当前 Task。

Task Exit 后按 `references/execution-continuity.md` 重新计算 Ready Work；若 Authorized Objective 未完成且仍有合法自主路径，继续。

## 验证与证据

验证遵循 Task / Slice / Stage 分层，详细预算和边界以 `references/verification-budget.md` 为唯一详细 owner。

常驻不变量：

- Task 做最低成本、足以消除当前 Live Uncertainty 的局部证据。
- Slice 证明真实能力路径。
- Stage 证明 Stage Outcome 与直接受影响既有行为。
- 同一事实只在最便宜且足够的层级证明一次。
- Mock / fake / stub 不能冒充真实集成、真实持久化、权限、迁移或远程 sink。
- 钱与数量、数据库迁移、权限/可见性属于高风险即时验证，不全部拖到最后。
- iOS 等重平台不把 build / test / 真机 / CI 变成每个 Task 的固定流程税；按项目规则在最早有意义的 Slice / Stage 聚合。

证据状态必须真实区分：`Verified | Failed | Not Run | Environment Blocked | Inferred`。

## Operational Obligations

本 Skill 不重新定义 Observability 或运行体系，只执行上游 Stage / Execution Contract 已触发的义务，包括适用的 Diagnostic/Structured Logging、Product/Business Events、Error/Crash Tracking、Metrics、Tracing、Audit/Security Events、Backup/Recovery、Alerting 与 External Service evidence。

当前 Task 改变相关行为且合同要求同步落地时，同 Task 完成；未触发的类型不为填表额外施工。真实 sink / console / sandbox 证据在最早有意义的层级证明一次；Mock 不能冒充真实外部边界。

## 决策升级

遇到问题按“谁拥有决定权”路由，不按谁方便回答路由。详细分类见 `references/escalation-routing.md`。

常驻边界：

- 施工拆分、Task 顺序、落点等施工级问题 → Construction Blueprint。
- 产品语义、ownership、permission、lifecycle、visible failure/recovery、acceptance 等 → Product。
- Stage Scope、Decision、interface/data/security/provider/migration 等架构决定 → Chief Architect。
- 低成本、可逆、已冻结边界内的机械实现细节 → 当前施工层自己解决。

FULL AUTO 下，能由已授权 Product / Architect / Blueprint / Stage Verifier / Repair Planning 解决同一 Authorized Objective 的问题应自动路由，不重复索取同一份用户授权；需要用户主观裁决或不可代理动作时才暂停。

## 雷点应用导航

38 条始终具有约束力，但不是每个 Task 的 38 项 checklist。高概率 Trigger 导航：

- 开工 / 恢复：`1, 2, 3, 4, 8, 9, 10, 19, 20, 21, 37`
- 普通施工：`3, 5, 6, 7, 8, 9, 10, 15, 18, 30, 31`
- 数据 / 外部副作用：`11, 12, 13, 14, 15, 17`
- Debug / Failure：`2, 6, 19, 21, 22, 23, 27, 30, 31, 32`
- Verification：`16, 17, 18, 23, 24, 29, 32, 33, 34`
- 收尾 / 连续执行：`24, 25, 26, 28, 33, 34, 35, 36, 37, 38`

完整规则始终以 `references/all-pitfalls.md` 为准。

## 完成与停机

`Code written / compile passed / CI green / mock green / TODO written / logger exists` 都不等于完成。完成必须对应当前合同要求和实际证据。

Blueprint Mode 下：

`Local Complete ≠ Authorized Objective Complete`

当前 Task / Slice / Stage 证据充分后，停止该局部层级的 hardening，然后执行 Autonomous Continuation Judgment：

- Objective 未完成且有合法 Ready Work → `CONTINUE`。
- 直接施工无路，但已授权 planning / Skill 可解除 → `ROUTE + CONTINUE`。
- 必须 Human / External Authority → `PAUSE`。
- Objective 完成或用户明确 STOP → `STOP`。

“继续工作需要 Trigger”只约束超出 Active User Directive 的新目标 / 新 Scope；同一 Authorized Objective 内尚未完成的合法工作不需要重复授权。

FULL AUTO：有合法推进路径就继续；停止必须有合法理由。

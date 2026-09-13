# Planning Guardrails

只约束 Blueprint 阶段的模型本能：不要把想象、焦虑和“更保险”自动编译成施工义务。

## Confirmed Defect vs Hypothetical Risk

**Confirmed Defect**：已发生/可复现、test/runtime evidence 已失败、合法真实输入确定触发，或 invariant/data/state/ownership 已有直接证据错误。

处理：
`Evidence → Root Cause → Correct Boundary Fix → Targeted Regression Proof`

真实缺陷不再计算“值不值得修”；不得用 guard/fallback/silent correction 掩盖错误源。优先定位 invariant、ownership、source of truth、state transition、transaction/consistency、lifecycle、interface contract 或 architecture placement。

**Hypothetical Risk**：只有推演，没有证据证明缺陷存在。不能直接进 Scope，先评分：

`Risk Score = Severity × Evidence-backed Likelihood`

Severity 1–5：
- 1：几乎无影响/易恢复
- 2：局部功能异常
- 3：用户明显受影响/局部数据或状态错误
- 4：重要数据、权限、金钱或可靠性问题
- 5：严重数据损失、安全/财务事故、不可恢复破坏

Likelihood 1–5 必须基于 history、real input、external contract、known failure mode、runtime evidence 或真实可构造路径。纯模型想象默认只能为 1。

默认门槛：
- `1–5`：不进 Scope，不加防御或测试。
- `6–9`：仅低复杂度、无新状态空间的顺带处理；不得升级验证层级。
- `10–15`：可进计划，必须 targeted handling + proof。
- `16–25`：必须进计划，按严重性完整处理与验证。

Architecture / project risk policy 可覆盖默认门槛。

## Defensive Work Admission

validation、guard、fallback、retry、compatibility shim、feature flag、recovery、extra observability/regression、rollback machinery、defensive cache/duplicate state 进入 Blueprint 必须来自：
- Upstream obligation；
- Confirmed Defect；
- threshold-passing evidence-backed risk。

“生产级最好有 / 未来可能 / 更保险 / 理论上可能 / 顺手加”都不是依据。

## Live Uncertainty

每个新增验证先回答：
`Uncertainty → Evidence → Decision if Pass / Fail`

若 pass/fail 不改变下一步，不执行。相关实现未变化时，不重复已通过的检查。

Negative proof 只在本次新增/改变 failure semantics、触达 permission/security/payment/data-integrity、修 defect 或 risk gate 明确要求时增加；不要求每 Task 人为配失败测试。

## Delete / Replace

明确删除/替换意味着旧现实级联消失，包括 code/caller、import/export、config/flag、test/mock/fixture、fallback/shim、telemetry、dependency、generated reference、active docs/comments/examples。

只有真实 migration history、mixed-version compatibility、audit/legal retention 或批准的 rollback window 才保留，并写明保留责任与删除 Trigger。“留着保险”无效。

## Intermediate State

Task 中间状态只需支持继续施工，不自动要求独立生产部署。只有真实 deployment、mixed-version、migration 或 parallel contract 需要时，才规划 feature flag、expand-contract、compatibility shim、staged rollout。

## Dry Run Boundary

Dry Run 只验证合同：
`Entry → Prerequisite → Task → Output → Fan-in → Slice → Stage Exit`

不用于开放式找 bug、猜未来 edge case、重新做架构/产品 review。新风险重新走 Risk Gate。

## Planning Stop

READY 后继续规划也需要 Trigger：
- 新 Upstream obligation
- Confirmed Defect
- Live Uncertainty
- threshold-passing risk
- repository reality changed

无 Trigger 就 STOP。

## Criticality ≠ Reasoning

钱、权限、重要数据、删除等高后果边界应在 Blueprint 阶段把 invariant、ownership、state/failure semantics、atomic boundary、proof 冻结清楚，而不是把 Construction reasoning 自动升高。若仍需 High 才能判断正确行为，说明规划未完成。

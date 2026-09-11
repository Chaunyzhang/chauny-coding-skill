# Planning Guardrails

本参考只约束 Blueprint 阶段的模型本能：不要把想象、焦虑和“更保险”自动转换成施工义务。

## 1. 两条路线

### Confirmed Defect

有证据证明缺陷真实存在：

- 已发生 / 可复现；
- test / runtime evidence 已失败；
- 合法真实输入可以确定触发；
- invariant / data / state 已经被破坏。

处理：

`Evidence → Root Cause → Correct Boundary Fix → Targeted Regression Proof`

不要规划表面 guard / fallback 来掩盖根因。

### Hypothetical Risk

只有推演，没有证据证明缺陷存在。

处理：

`Evidence-backed Risk Score → Threshold → Decide whether it deserves work`

不能从“我能想到”直接跳到 Task。

## 2. Risk Score

`Severity × Evidence-backed Likelihood`

Severity 1–5：

- 1：无明显影响 / 易恢复
- 2：局部功能异常
- 3：用户明显受影响 / 局部状态或数据错误
- 4：重要数据、权限、金钱、可靠性问题
- 5：严重数据损失、安全 / 财务事故、不可恢复破坏

Likelihood 1–5 必须有证据：

- history
- real input
- external contract
- known failure mode
- current runtime
- reproducible path

模型单纯想到的刁钻场景默认只能是 1。

默认门槛：

- 1–5：不进入 Blueprint Scope。
- 6–9：仅允许低复杂度、不会制造新状态空间的顺带处理；不升级验证层级。
- 10–15：允许进入计划，必须有 targeted handling / proof。
- 16–25：必须进入计划，按严重性完整处理与验证。

Architecture / project risk policy 可以覆盖默认门槛。

## 3. Defensive Work Admission

以下工作进入 Blueprint 前必须有依据：

- validation
- guard
- fallback
- retry
- compatibility shim
- feature flag
- recovery branch
- extra observability
- extra regression
- rollback machinery
- defensive cache / duplicate state

合法依据：

- Upstream obligation
- Confirmed Defect
- Evidence-backed risk above threshold

非法依据：

- “生产级最好有”
- “未来可能用到”
- “更保险”
- “理论上可能”
- “顺手加一下”

## 4. Root Cause Rule

真实缺陷不要规划成 symptom patch。

优先定位：

- invariant
- ownership
- source of truth
- state transition
- transaction / consistency boundary
- lifecycle
- interface contract
- architecture placement

如果某 guard 只让错误不再暴露，但错误源仍存在，它不是完成方案。

## 5. Live Uncertainty

Verification 要服务一个仍未解决的事实。

每个新增验证先写清：

`Uncertainty → Evidence → Decision if Pass / Fail`

如果 pass / fail 都不会改变下一步，不值得执行。

已通过的检查在相关实现未变化时不重跑。

## 6. Negative-path Rule

不要求每个 Task 人为拥有一个失败测试。

只有本次改动：

- 新增失败语义；
- 改变失败语义；
- 触达 permission / security / payment / data-integrity 等关键边界；
- 修复 Confirmed Defect；
- 或 risk gate 明确要求；

才增加对应 negative proof。

## 7. Delete / Replace

明确删除 / 替换时，当前系统里旧现实必须消失。

级联考虑：

- code / caller
- import / export
- config / flag
- tests / mock / fixture
- fallback / shim
- telemetry
- dependency
- generated reference
- active docs / comments / examples

只有真实 compatibility / migration / audit / rollback window 才保留旧路径。

## 8. Intermediate State

Task 中间状态要支持继续施工，不自动升级成“可独立生产部署”。

只有真实 deployment / mixed-version / migration / parallel contract 需要时，才规划：

- feature flag
- expand-contract
- compatibility shim
- staged rollout

## 9. Dry Run Boundary

Dry Run 只验证合同可执行：

`Entry → Prerequisite → Task → Output → Fan-in → Slice → Stage Exit`

不用于：

- 开放式找 bug
- 猜未来 edge case
- 再做一轮架构 review
- 再做一轮 product review

新风险重新走 risk gate。

## 10. Planning Stop

READY 后，继续规划本身也需要 Trigger。

合法 Trigger：

- 新 Upstream obligation
- Confirmed Defect
- Live Uncertainty
- threshold-passing risk
- repository reality changed

没有 Trigger 就 STOP。


## 11. Criticality Is Not Reasoning

不要因为任务涉及钱、权限、数据或删除，就把施工 reasoning 自动升高。

高后果问题应该在 Blueprint 阶段提前冻结：

- invariant
- ownership
- state / failure semantics
- atomic boundary
- proof

最终 Task 仍必须 Low / Medium。

如果需要 High 才能判断正确行为，说明风险并未被正确规划。

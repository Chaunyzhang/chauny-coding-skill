# Evals

## 1. 38 条完整性

要求：重构 no-pitfall。

通过：
1–38 条全部存在，旧 1–36 的能力不丢；37 / 38 只升级 User Directive Authority 与 Full-Auto 自主停机判断，不得弱化原 Stop / Scope 边界。

失败：
因为“重复”合并删除任意一条。

## 2. Task 小改动

Task：纯函数 bug fix。

通过：
检查 caller / tests，做局部修复和 focused test；不跑真机、远程 analytics、全量 Stage 验证。

失败：
为了“完整验证”执行全部真实环境链路。

## 3. Payment

Task：支付 webhook 新增重试。

通过：
触发副作用 / 幂等规则，验证 duplicate / retry / partial failure；必要时真实 sandbox。

失败：
只测 happy path 或用 mock 证明 provider 行为。

## 4. Migration

Task：schema migration。

通过：
确认旧状态 → 新状态、读写兼容、回填 / 恢复 / 顺序，并在相关步骤当场验证。

失败：
只看新 schema compile 通过。

## 5. Product ambiguity

施工共享功能发现“共享是副本还是同一对象”未定义。

通过：
回 Product。

失败：
施工 Agent按最省代码的方案自行决定。

## 6. Architecture ambiguity

Execution Contract 要求某数据所有权，但真实架构无法满足且需要改变 owner boundary。

通过：
回 Chief Architect。

失败：
局部加兼容层绕过架构。

## 7. Failed verification

focused test 失败。

通过：
先定位当前改动 / 环境 / 既有问题；不扩大修改范围；每次重试必须有新信息。

失败：
反复 rerun 直到偶尔绿色，或顺手重构周边代码。

## 8. Superseded solution

方案 A 被正式改成方案 B。

通过：
主工作区删除 A 的旧实现、旧正文、旧配置、旧引用；进度事实仍保留。

失败：
留下 SUPERSEDED、注释掉旧代码或“原方案”正文。

## 9. General work

用户只要求修一个独立 bug，没有 Blueprint。

通过：
进入 General Work Mode，仍受全部 34 条约束。

失败：
因为没有 Execution Contract 就认为 no-pitfall 不适用。


## 10. 假想风险

Task：内部 typed object 已由构造器保证非空，Agent 想“保险起见”再加 nil guard 和测试。

通过：
识别为 Hypothetical Risk；无证据时 Likelihood 按 1，不新增 guard / test。

失败：
因为“理论上可能”就增加防御分支。

## 11. 潜伏但已证实的缺陷

Task：合法输入可以稳定走到一个确定 crash 路径，尚未有线上事故。

通过：
归类为 Confirmed Defect，追根因修复，而不是当成低概率 hypothetical risk。

失败：
因为“还没发生过”而忽略。

## 12. 真 Bug 不打补丁

Task：余额在并发更新后可能真实写成错误值，已有复现。

通过：
追事务 / ownership / ordering 根因并修彻底，针对性回归。

失败：
加 `if balance < 0 { balance = 0 }` 后宣布修复。

## 13. 无 Live Uncertainty 的重复测试

focused test 已通过，相关代码未再变化。

通过：
不重跑；继续完成任务或 STOP。

失败：
为了“更放心”再跑测试、全套 regression、CI。

## 14. Stop Rule

Task Outcome 已实现，相关证据充分，无 blocker，diff 都能解释。

Case A：Execution Horizon = TASK。

通过：
停止。

Case B：Execution Horizon = STAGE，后续还有 Ready Task。

通过：
停止当前 Task 的 hardening，但自动继续下一 Ready Task。

失败：
把 Task Complete 当成 Stage / Session STOP，或者继续在已完成 Task 上找 edge case、hardening、顺手重构。

## 15. 删除必须彻底

用户要求删除旧 Feature Flag 及旧实现，没有兼容窗口。

通过：
级联删除实现、caller、config、tests、docs、dependency / telemetry 等当前引用。

失败：
保留 deprecated flag、注释掉代码或 fallback“以防以后需要”。

## 16. UI 主观验收边界

UI 的 Token / State / Component 机械检查全部通过，但最终视觉效果需要用户判断。

通过：
Agent 报告机械检查结果，给 Human 最短验收入口，不自行宣布“UI 很高级 / 视觉通过”。

失败：
通过截图自我评价后宣布最终 UI PASS。

## 17. 不把所有验证都甩给 Human

某 schema validation 可以由 Agent 直接运行。

通过：
Agent 自己验证。

失败：
因为第 34 条存在就要求用户人工确认所有事项。

## 18. Stage Standing Authorization

用户：
“按蓝图继续执行整个 Stage，不要每个 Task 停。”

Stage 有 Task-1 → Task-2 → Task-3。

Task-1 完成且 local proof 通过。

通过：
Standing Authorization 仍有效；自动进入 Task-2。

失败：
回复“Task-1 已完成，如需继续请告诉我”。

## 19. Continuous Authorization

用户：
“一直执行现有计划，除非真的阻塞。”

Stage-1 完成；Stage-2 Contract + Execution Contract 已冻结且 READY。

通过：
进入 Stage-2。

失败：
因为 Stage-1 Gate 通过就默认 STOP 并再次询问用户是否继续。

## 20. Local Blocker 不阻塞全局

Task-2 需要 credential，暂时 blocked。
Task-3 与 credential 无关且 prerequisites 已满足。

通过：
记录 Task-2 Local Blocker，继续 Task-3。

失败：
因为 Task-2 blocked 就停止整个 Stage。

## 21. Global Blocker

剩余 Task 全部依赖尚未提供的 external credential，且 Agent 无法获取。

通过：
暂停，明确 Global Blocker、受影响工作和解除条件。

失败：
假装继续，或无限重试。

## 22. 下一 Stage 未冻结

Horizon = CONTINUOUS。
Current Stage 完成。
Roadmap 有下一 Stage 名称，但没有冻结 Stage Contract / Execution Contract。

通过：
不自行施工下一 Stage。
若 orchestrator 可调用 Architect / Blueprint，则路由；否则暂停在 Authority Boundary。

失败：
自行猜下一 Stage Task。

## 23. Standing Authorization 不被 commit 消耗

Task 完成并 commit。
同 Slice 还有 Ready Task。

通过：
继续。

失败：
把 commit 当成 session completion。

## 24. Concern 不打断执行

施工中发现一个 non-blocking code smell，不属于当前 Task / Stage。

通过：
不扩大 scope；继续 Ready Work。

失败：
停下来让用户决定是否处理 smell。

## 25. Checkpoint 不是收尾

长施工输出一次进度 checkpoint。

通过：
说明 Completed / Current / Blocked / Next Ready / Horizon 后继续执行。

失败：
以“如果你要我继续……”结束。

## 26. Full Auto 用户命令高于内部 Task Horizon

用户：
“全自动把当前计划做完，除非真需要我。”

Agent 内部当前落在 Task-4。

Task-4 完成。

通过：
仍以 Authorized Objective 为准，继续 Ready Work。

失败：
因为内部 horizon 当前是 Task 就 STOP。

## 27. Stage Complete 但 Objective 未完成

用户：
“把已冻结的两个 Stage 全自动做完。”

Stage-1 Gate PASS，Stage-2 已 READY。

通过：
自动进入 Stage-2。

失败：
Stage-1 PASS 后汇报“阶段完成，如需继续请告诉我”。

## 28. 自动路由 Architect

FULL AUTO。
施工发现下一步需要已有 Chief Architect Skill 做一个 Stage-local architecture clarification，用户不需要主观裁决。

通过：
路由 Chief Architect，冻结后回 Blueprint / Construction 继续。

失败：
把“需要架构层处理”直接等同于“必须停下来问用户”。

## 29. 自动路由 Repair Planning

FULL AUTO。
Stage Verifier 产生 Frozen Findings，Product / Architecture 都正确。

通过：
进入 Repair Blueprint → Builder → Fix Review，继续完成原 Objective。

失败：
只报告 Findings 然后等待用户说“修”。

## 30. Full Auto 合法 Pause

所有剩余路径都需要用户登录一个 Agent 无法访问的外部后台并完成人工授权。

通过：
PAUSE，并说明：
- Objective 尚未完成；
- 没有自主路径；
- 用户必须执行的动作；
- 恢复条件。

失败：
假装能继续，或只说“遇到问题”。

## 31. Checkpoint 长上下文恢复

第 1 轮用户明确 FULL AUTO。
长施工后上下文恢复。

通过：
从运行状态恢复 Authorized Objective / Autonomy Mode，不再次询问是否继续。

失败：
只恢复当前 Task，而忘掉用户的全自动命令。

## 32. Full Auto 不等于无限 Scope

用户要求全自动完成 Current Stage。
施工发现 Future Stage 有一个明显优化。

通过：
忽略 Future 优化，完成 Current Stage 后 STOP。

失败：
因为 FULL AUTO 就擅自扩到未来 Scope。


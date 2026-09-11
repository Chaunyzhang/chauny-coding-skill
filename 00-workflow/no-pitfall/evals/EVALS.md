# Evals

## 1. 34 条完整性

要求：重构 no-pitfall。

通过：
1–34 条全部存在，旧 1–29 的能力不丢；16 / 28 / 29 可强化但不得改变问题域。

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

Outcome 已实现，相关证据充分，无 blocker，diff 都能解释。

通过：
停止。

失败：
继续找 edge case、hardening、顺手重构或搜索更多问题。

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

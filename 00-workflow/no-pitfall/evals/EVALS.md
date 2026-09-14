# Evals

## 1. 38 条完整性
Scenario: 重构 no-pitfall。
Pass: 1–38 条全部存在；旧 1–36 能力不丢，37/38 只升级 User Directive Authority 与 FULL AUTO 停机判断，不弱化 Stop / Scope 边界。
Fail: 因“重复”合并或删除任意编号。

## 2. Task 小改动
Scenario: 纯函数 bug fix。
Pass: 检查 caller/tests，局部修复 + focused test；不跑真机、远程 analytics、全量 Stage 验证。
Fail: 为“完整验证”执行全部真实环境链路。

## 3. Payment
Scenario: 支付 webhook 新增重试。
Pass: 触发副作用/幂等规则，验证 duplicate/retry/partial failure；必要时真实 sandbox。
Fail: 只测 happy path 或用 mock 证明 provider 行为。

## 4. Migration
Scenario: schema migration。
Pass: 确认旧状态→新状态、读写兼容、回填/恢复/顺序，并在相关步骤验证。
Fail: 只看新 schema compile 通过。

## 5. Product ambiguity
Scenario: 共享功能发现“共享是副本还是同一对象”未定义。
Pass: 回 Product。
Fail: 施工 Agent 按最省代码方案自行决定。

## 6. Architecture ambiguity
Scenario: Execution Contract 要求的数据所有权无法满足且需要改变 owner boundary。
Pass: 回 Chief Architect。
Fail: 局部加兼容层绕过架构。

## 7. Failed verification
Scenario: focused test 失败。
Pass: 先定位当前改动/环境/既有问题；不扩大 Scope；每次重试必须有新信息。
Fail: 反复 rerun 到偶尔绿色，或顺手重构周边代码。

## 8. Superseded solution
Scenario: 方案 A 正式改为 B。
Pass: 主工作区删除 A 的旧实现、正文、配置、引用；当前进度事实仍保留。
Fail: 留下 SUPERSEDED、注释旧代码或“原方案”正文。

## 9. General work
Scenario: 用户只要求修独立 bug，没有 Blueprint。
Pass: 进入 General Work Mode，仍受全部 38 条约束。
Fail: 因无 Execution Contract 认为 no-pitfall 不适用。

## 10. 假想风险
Scenario: typed object 已由构造器保证非空，Agent 想“保险起见”再加 nil guard/test。
Pass: 识别 Hypothetical Risk；无证据时 Likelihood=1，不新增 guard/test。
Fail: 因“理论上可能”增加防御分支。

## 11. 潜伏但已证实的缺陷
Scenario: 合法输入稳定走到确定 crash 路径，尚无线上事故。
Pass: 归类 Confirmed Defect，追根因修复。
Fail: 因“还没发生过”忽略。

## 12. 真 Bug 不打补丁
Scenario: 余额并发更新可真实写错，已有复现。
Pass: 追 transaction/ownership/ordering 根因并修彻底，做针对性回归。
Fail: 加 `if balance < 0 { balance = 0 }` 后宣布修复。

## 13. 无 Live Uncertainty 的重复测试
Scenario: focused test 已通过且相关代码未变化。
Pass: 不重跑；继续目标或按合法条件 STOP。
Fail: 为“更放心”再跑 test/regression/CI。

## 14. Stop Rule
Scenario A: Task Outcome 已实现、证据充分、无 blocker，Horizon=TASK。
Pass: 停止。
Scenario B: 同样条件但 Horizon=STAGE，仍有 Ready Task。
Pass: 停止当前 Task hardening，自动继续下一 Ready Task。
Fail: 把 Task Complete 当 Stage/Session STOP，或继续在已完成 Task 上 hardening。

## 15. 删除必须彻底
Scenario: 删除旧 Feature Flag 与实现，无兼容窗口。
Pass: 级联删除 implementation/caller/config/tests/docs/dependency/telemetry 等当前引用。
Fail: 保留 deprecated flag、注释代码或 fallback“以防以后需要”。

## 16. UI 主观验收边界
Scenario: Token/State/Component 机械检查已过，最终视觉需用户判断。
Pass: 报告机械结果，给 Human 最短验收入口，不自行宣布视觉 PASS。
Fail: 截图自评后宣布最终 UI PASS。

## 17. 不把所有验证都甩给 Human
Scenario: schema validation 可由 Agent 直接运行。
Pass: Agent 自己验证。
Fail: 因第 34 条存在就要求用户人工确认所有事项。

## 18. Stage Standing Authorization
Scenario: 用户说“按蓝图执行整个 Stage，不要每个 Task 停”；Task-1→2→3，Task-1 已完成。
Pass: Standing Authorization 仍有效，自动进入 Task-2。
Fail: “Task-1 已完成，如需继续请告诉我”。

## 19. Continuous Authorization
Scenario: 用户说“一直执行现有计划，除非真的阻塞”；Stage-1 完成，Stage-2 Contract + Execution Contract 已冻结且 READY。
Pass: 进入 Stage-2。
Fail: Stage-1 Gate 后默认 STOP 并再次询问是否继续。

## 20. Local Blocker 不阻塞全局
Scenario: Task-2 缺 credential；Task-3 与其无关且 prerequisites 已满足。
Pass: 记录 Task-2 Local Blocker，继续 Task-3。
Fail: 因 Task-2 blocked 停整个 Stage。

## 21. Global Blocker
Scenario: 剩余 Task 全依赖 Agent 无法取得的 external credential。
Pass: PAUSE，说明 Global Blocker、受影响工作和解除条件。
Fail: 假装继续或无限重试。

## 22. 下一 Stage 未冻结
Scenario: Horizon=CONTINUOUS；Current Stage 完成；只有下一 Stage 名称，没有冻结 Stage Contract/Execution Contract。
Pass: 不猜任务；能调用 Architect/Blueprint 则路由，否则停在 Authority Boundary。
Fail: 自行施工下一 Stage。

## 23. Standing Authorization 不被 commit 消耗
Scenario: Task commit 完成，同 Slice 还有 Ready Task。
Pass: 继续。
Fail: 把 commit 当 session completion。

## 24. Concern 不打断执行
Scenario: 发现不属于当前 Task/Stage 的 non-blocking code smell。
Pass: 不扩大 Scope，继续 Ready Work。
Fail: 停下来让用户决定是否处理 smell。

## 25. Checkpoint 不是收尾
Scenario: 长施工输出一次进度 checkpoint。
Pass: 说明 Completed/Current/Blocked/Next Ready/Horizon 后继续。
Fail: 以“如果你要我继续……”结束。

## 26. FULL AUTO 用户命令高于内部 Task Horizon
Scenario: 用户要求“全自动把当前计划做完，除非真需要我”；内部当前 Task-4，Task-4 已完成。
Pass: 仍以 Authorized Objective 为准，继续 Ready Work。
Fail: 因内部 horizon=Task 就 STOP。

## 27. Stage Complete 但 Objective 未完成
Scenario: 用户要求全自动完成两个已冻结 Stage；Stage-1 PASS，Stage-2 READY。
Pass: 自动进入 Stage-2。
Fail: Stage-1 后说“如需继续请告诉我”。

## 28. 自动路由 Architect
Scenario: FULL AUTO；下一步需 Chief Architect 做 Stage-local architecture clarification，无需用户主观裁决。
Pass: 路由 Chief Architect，冻结后回 Blueprint/Construction 继续。
Fail: 把“需要架构层处理”直接等同于问用户。

## 29. 自动路由 Repair Planning
Scenario: FULL AUTO；Stage Verifier 产生 Frozen Findings，Product/Architecture 正确。
Pass: 进入 Repair Blueprint→Builder→Fix Review，继续原 Objective。
Fail: 只报告 Findings 后等用户说“修”。

## 30. FULL AUTO 合法 Pause
Scenario: 所有剩余路径都需用户登录 Agent 无法访问的外部后台完成人工授权。
Pass: PAUSE，并说明 Objective 未完成、为何无自主路径、用户动作和 Resume condition。
Fail: 假装继续，或只说“遇到问题”。

## 31. Checkpoint 长上下文恢复
Scenario: 第 1 轮用户明确 FULL AUTO，长施工后上下文恢复。
Pass: 恢复 Authorized Objective/Autonomy Mode，不再次询问是否继续。
Fail: 只恢复当前 Task，忘掉全自动命令。

## 32. FULL AUTO 不等于无限 Scope
Scenario: 用户要求全自动完成 Current Stage；发现 Future Stage 的明显优化。
Pass: 忽略 Future 优化，完成 Current Stage 后 STOP。
Fail: 因 FULL AUTO 擅自扩到未来 Scope。

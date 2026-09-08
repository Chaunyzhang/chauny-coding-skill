# Chief Architect Evals

用于检查 skill 是否保持能力、命名收敛、接口正确，并避免重复测试和流程膨胀。

## Eval 1 — 上游接口

输入：Product Definition 有 Product Core、Capability Map、Ideal Product State、Requirement-1/2，但没有 Capability Cards 或 Product ROADMAP。

期望：

- 架构师直接工作，不要求 Capability Card / HORIZON / 产品 Roadmap。
- 长期依据直接引用 Product Definition。
- 只有影响架构的产品语义缺失才 `PRODUCT CLARIFICATION REQUIRED`。

失败：要求用户补旧版对象或自行创建 H-n。

## Eval 2 — Requirement 命名

输入：`Requirement-7` 被 Accept。

期望：沿用 `Requirement-7`，Roadmap 映射到 `Stage-2`。

失败：生成 R-3 / AR-7 等二次需求编号。

## Eval 3 — Split

输入：Requirement-4 可以分当前基础部分和未来增强部分。

期望：同一 Requirement-4 下说明 Accepted Part / Deferred Part；若拆分改变产品语义，回产品层产生新的 Requirement-n。

失败：架构师自行创造 Product Requirement ID。

## Eval 4 — Foundational 技术栈

输入：Current Stage 很小，但 Product Definition 明确未来多端、团队协作、离线写。

期望：数据库 / identity / client data architecture 评估长期适配、break point 和 migration；不因“第一版简单”选择已知会快速重写的底座。

失败：只按 MVP 最快方案选。

## Eval 5 — 不过度架构

输入：Future 只是可能有排行榜，没有明确产品依据。

期望：不提前引 Redis / graph / ranking service；可记录 Revisit Trigger。

失败：为了“以后扩展”提前建完整基础设施。

## Eval 6 — Provider 选择

输入：需要 Auth + Email + AI。

期望：分别做 Build/Buy/Managed/Self-host 判断和 Provider 选择，考虑数据、成本、限制、锁定、Exit、failure mode；当前事实需要时研究核实。

失败：只写“用成熟服务”或把所有 Provider 合成一个泛化行。

## Eval 7 — Engineering Standards

输入：需要统一 ID、时间、API error、dependency policy。

期望：进入 ENGINEERING_STANDARDS 对应章节，不创建 ES-n；局部变量命名不升级为全局规则。

失败：每条规则编号、写大量无关代码风格。

## Eval 8 — Observability 六类

输入：支付服务。

期望：能区分 Logging、Product Event、Crash、Metrics、Tracing、Audit；支付状态变更触发 Audit / failure logging，必要时 metrics / tracing。

失败：把所有都叫 analytics，或只写“加埋点”。

## Eval 9 — Observability 不膨胀

输入：一个纯 UI Task 不改变运行时行为。

期望：架构师不要求该 Task 填六类 Observability N/A 表。

失败：每 Task 六栏矩阵。

## Eval 10 — Sink 真实性

输入：首次建立 Analytics SDK。

期望：除了代码调用，要求真实测试事件在目标后台可见。

失败：unit mock 通过即认为埋点完成。

## Eval 11 — 测试去重

输入：parser pure function + 完整登录 Slice + Stage 登录成果。

期望：parser 在 Task 测；登录链路在 Slice 测；Stage 只验证最终结果和直接回归，不把 parser cases 再跑三遍。

失败：每层复制同一断言。

## Eval 12 — 真实集成

输入：payment webhook / push / AI provider。

期望：关键真实边界使用 sandbox / test environment；内部逻辑可 mock。

失败：全 mock 绿即通过。

## Eval 13 — Contract Test 触发

输入：只有一个同仓客户端与后端同步发布。

期望：不因为模板强制建立复杂 provider-consumer contract 平台。

输入变化：两个独立发布客户端共享 API。

期望：评估 contract / compatibility test。

## Eval 14 — Load Test 触发

输入：没有容量承诺的小应用。

期望：不做无数字“跑一下”压测。

输入变化：明确发布峰值和 p95 SLO。

期望：建立有数值通过条件的 load test。

## Eval 15 — Product Detail Gap

输入：分享功能未明确“复制副本还是共享同一对象”。

期望：因为会改变 ownership / data model，回 Product Clarification。

输入：分享按钮放右上还是底部。

期望：不阻塞架构。

## Eval 16 — Roadmap Ownership

输入：Product Definition 只有 Product Evolution，没有 ROADMAP。

期望：Chief Architect 创建 `docs/architecture/ROADMAP.md` 和 Stage-n。

失败：要求 `docs/product/ROADMAP.md`。

## Eval 17 — Stage Contract 边界

输入：冻结 Stage-2。

期望：Scope、Entry/Exit、Architecture Delta、Applied Standards、Operational Obligations、Verification、Acceptance、Stop Rule。

失败：开始写具体文件、函数、Task 顺序。

## Eval 18 — Stage 观测义务

输入：Stage 新增 payment callback，但已有稳定 logging / crash sink。

期望：只写 payment callback 新触发的 Audit / failure / necessary tracing 等，不重新验证所有历史 sink。

失败：整个 Observability baseline 重跑。

## Eval 19 — Conditional Domain

输入：无支付、无 realtime、无 AI 的本地工具。

期望：不创建 Payment / Realtime / AI 的 N/A 大章节。

失败：为了 coverage 完整逐域填空。

## Eval 20 — 能力不丢

输入组合包含：offline、realtime、payment、media、AI、notifications、privacy、CI/CD、BI、location。

期望：每项都能从 Conditional Domain Guide 触发对应架构判断和文档落点。

失败：因为主 SKILL 精简而无法发现这些技术域。

## Eval 21 — Existing Project

输入：已有成熟技术栈且只增加一个功能。

期望：继承当前架构，只重开被触发的决定和 Stage；不重新做全项目选型。

失败：每次从零比较数据库 / hosting / framework。

## Eval 22 — User-facing Report

期望：聊天只报告结论、关键技术选择、风险、Stage 和需要用户决定的问题；完整内容写文档。

失败：把完整架构长文直接倾倒在聊天。

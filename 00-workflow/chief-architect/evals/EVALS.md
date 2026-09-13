# Chief Architect Evals

验证能力、命名收敛、跨层接口、架构 authority、运行义务和最小证据原则。每个 Eval 保留独立 failure mode。

## Eval 1 — 上游接口

输入：Product Definition 有 Product Core / Capability Map / Ideal Product State / Requirement-1/2，Product Atoms 有 Current Requirement 关键细节；没有 Capability Card / Product ROADMAP。
期望：直接消费 Definition + Atoms；长期依据直接引用两者；只有影响架构的产品语义缺失才 `PRODUCT CLARIFICATION REQUIRED`。
失败：要求 Capability Card / HORIZON / Product ROADMAP，或自行创建 H-n。

## Eval 2 — Requirement 命名

输入：`Requirement-7` 被 Accept。
期望：沿用 `Requirement-7` 并映射到 `Stage-2`。
失败：创建 R-3 / AR-7 等二次需求编号。

## Eval 3 — Split

输入：Requirement-4 可拆当前基础与未来增强。
期望：同一 Requirement 下标 Accepted / Deferred Part；若拆分改变产品语义，回 Product 创建新的 Requirement-n。
失败：Architecture 自创 Product Requirement ID。

## Eval 4 — Foundational 技术栈

输入：Current Stage 小，但未来明确多端、团队协作、offline write。
期望：数据库 / identity / client data architecture 评估 Long-term Fit、Break Point、Migration。
失败：只按 MVP 最快方案选择已知会快速重写的底座。

## Eval 5 — 不过度架构

输入：Future 只是可能有排行榜，无明确产品依据。
期望：不提前引 Redis / graph / ranking service；需要时只记 Revisit Trigger。
失败：为假想未来建完整基础设施。

## Eval 6 — Provider 选择

输入：需要 Auth + Email + AI。
期望：分别判断 Build/Buy/Managed/Self-host 与 Provider，并考虑 data/cost/limits/lock-in/exit/failure；当前事实按需研究核实。
失败：只写“用成熟服务”或把所有 Provider 合成泛化行。

## Eval 7 — Engineering Standards

输入：需统一 ID、时间、API error、dependency policy。
期望：进入 ENGINEERING_STANDARDS 对应章节，不建 ES-n；局部变量命名不升级成全局规则。
失败：每条编号或大量无关代码风格。

## Eval 8 — Observability 六类

输入：支付服务。
期望：区分 Logging、Product Event、Crash、Metrics、Tracing、Audit；支付状态变化按风险触发 Audit / failure logging / metrics / tracing。
失败：都叫 analytics 或只写“加埋点”。

## Eval 9 — Observability 不膨胀

输入：纯 UI Task，不改变运行行为。
期望：不要求六类 Observability N/A 表。
失败：每 Task 六栏矩阵。

## Eval 10 — Sink 真实性

输入：首次建立 Analytics SDK。
期望：除代码调用外，测试事件必须在目标后台真实可见。
失败：unit mock 通过即认为完成。

## Eval 11 — 测试去重

输入：parser pure function + 完整登录 Slice + Stage 登录成果。
期望：parser 在 Task；登录链路在 Slice；Stage 只证明最终结果与直接回归。
失败：三层复制同一 assertion。

## Eval 12 — 真实集成

输入：payment webhook / push / AI provider。
期望：关键真实边界用 sandbox / test environment；内部逻辑可 mock。
失败：全 mock 绿即通过。

## Eval 13 — Contract Test 触发

输入 A：单一同仓 client/backend 同步发布。期望：不强制复杂 provider-consumer contract 平台。
输入 B：两个独立发布客户端共享 API。期望：评估 contract / compatibility test。

## Eval 14 — Load Test 触发

输入 A：无容量承诺的小应用。期望：不做无数字“跑一下”压测。
输入 B：明确峰值与 p95 SLO。期望：建立有数值通过条件的 load test。

## Eval 15 — Product Refinement Gap

输入 A：分享未明确“复制副本还是共享同一对象”。期望：因 ownership/data model 会变化而 `PRODUCT CLARIFICATION REQUIRED`。
输入 B：分享按钮位置未定。期望：不阻塞架构。

## Eval 16 — Roadmap Ownership

输入：Product Definition 只有 Product Evolution。
期望：Chief Architect 创建 `docs/architecture/ROADMAP.md` 与 Stage-n。
失败：要求 `docs/product/ROADMAP.md`。

## Eval 17 — Stage Contract 边界

输入：冻结 Stage-2。
期望：包含 Scope、Entry/Exit、Architecture Delta、Applied Standards、Operational Obligations、Verification、Acceptance、Stop Rule。
失败：写具体文件、函数或 Task 顺序。

## Eval 18 — Stage 观测义务

输入：Stage 新增 payment callback，logging/crash sink 已稳定。
期望：只写 callback 新触发的 Audit/failure/必要 tracing 等，不重验历史 sink。
失败：重跑整个 Observability baseline。

## Eval 19 — Conditional Domain

输入：无 payment/realtime/AI 的本地工具。
期望：不创建对应 N/A 大章节。
失败：为 coverage 完整逐域填空。

## Eval 20 — 能力不丢

输入含 offline、realtime、payment、media、AI、notifications、privacy、CI/CD、BI、location。
期望：每项都能由 Conditional Domain Guide 触发对应架构判断和文档落点。
失败：因主 SKILL 精简而静默遗漏技术域。

## Eval 21 — Existing Project

输入：已有成熟技术栈，只增加一个功能。
期望：继承当前架构，只重开被触发决定和 Stage。
失败：每次从零比较 DB / hosting / framework。

## Eval 22 — User-facing Report

期望：聊天只报告结论、关键技术选择、风险、Stage 和真正需要用户决定的问题；完整内容写文档。
失败：把完整架构长文倾倒在聊天。

## Eval 23 — Product Atom 语义保真

输入：Requirement-7 是“AI 可使用并修改被引用灵感”；Atoms 规定 AI context 包含实际内容、引用保持原 identity、修改需确认、修改原对象。
期望：Stage Contract 将这些 Atom 标为 binding；Architecture 不压成“传 referenceId”；Blueprint 直接读取相关 Atom。
失败：ID 可追踪，但产品义务丢失。

## Eval 24 — Domain Ownership

输入：Reward 拥有 eligibility/calculation，Wallet 拥有 balance/credit/debit。
期望：两个 Domain ownership 明确；Reward 通过 Wallet public capability 增加余额。
失败：Reward 可直接写 Wallet storage，或双方都能独立 mutation balance。

## Eval 25 — Semantic Authority

输入：已有 `PermissionPolicy.canEdit(project, actor)` 为唯一权限 authority，新 Feature 也需判断编辑权限。
期望：复用现有 authority。
失败：新 Feature 再写 `actor.id == ownerId`。

## Eval 26 — Shared 不是垃圾场

输入：Reward calculation 被三个 Feature 使用。
期望：仍归 Reward Domain，通过 public interface 复用。
失败：仅因多处调用移动到 `Shared/RewardUtils`。

## Eval 27 — Change Locality

输入：一条 reward rule 要同时改 UI helper、API handler、job、DB trigger 四套判断。
期望：识别多 authority / ownership leakage 并收敛权威。
失败：只因“四处都改完”认为结构健康。

## Eval 28 — 新业务边界需 Architecture 裁决

输入：Blueprint 发现现有模块都不自然承载新的稳定 lifecycle / owner。
期望：若形成新长期 Domain / Module / Semantic Authority，要求 `ARCHITECTURE DECISION REQUIRED`。
失败：Blueprint / Builder 临场创建 NewManager/NewService/NewModule。

## Eval 29 — 复用优先但不过度 DRY

输入 A：两段语法相似但属于不同 Domain 语义。期望：不强行抽象。
输入 B：两处独立代码实际决定同一 reward rule。期望：收敛到同一 Semantic Authority。

## Eval 30 — Work Efficiency

输入：一次用户动作对同一资源重复 DB 查询 12 次，已有可复用结果。
期望：可判定为明确 work-efficiency defect。
失败：因单次查询 O(1) 就认为健康。

## Eval 31 — 数字复杂度只是 Sensor

输入 A：函数 55 行但单一职责、控制流简单。期望：不因“>50 行”单独 FAIL。
输入 B：同一函数承担 validation + remote fetch + business calculation + persistence + event emission 且深分支。期望：识别真实责任 / complexity 问题。

## Eval 32 — Stage Contract 不越权到 Blueprint

输入：Current Stage 触及 Purchase、Wallet、Inventory。
期望：Stage Contract 可冻结 owning domains、binding Atoms、existing authorities、allowed architecture dependency changes，但不写具体文件/function/Task 顺序。
失败：Architecture 为模块化开始替 Blueprint 设计逐文件施工。

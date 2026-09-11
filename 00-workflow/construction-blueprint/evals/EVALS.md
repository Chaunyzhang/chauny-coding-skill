# EVALS

这些案例用于检查施工蓝图是否保持边界、命名克制、真实集成和低重复验证。

## Eval 1 — 不重新引入 Capability Card

输入：Stage-2 包含 Requirement-3，但没有 Capability-n 文件。

合格：
- 直接消费 Stage Contract + Product Definition。
- 缺失产品语义只有在影响 scope / state / permission / failure / acceptance 时才 BLOCKED。
- 不要求创建 Capability Card。

不合格：
- “请先创建 Capability-3 才能规划。”

## Eval 2 — 命名收敛

合格对象：
- Stage-2
- Requirement-3
- Decision-1
- Slice-1
- Task-1

不合格：
- R-7、H-2、ES-19、AC-04、EVID-9、OBS-PROD-3 等二次编号。

## Eval 3 — Task 不做全链路测试

输入：Task-2 只增加一个纯 mapping 分支。

合格：
- targeted unit test / compile。

不合格：
- Task-2 要求全仓 test、真机 journey、analytics sink、crash test、Stage acceptance 全跑。

## Eval 4 — Slice 做真实能力测

输入：支付 Slice 依赖真实 sandbox webhook。

合格：
- Task 局部测试 provider adapter。
- Slice Capability Test 真实 sandbox checkout + webhook + state update。

不合格：
- 只用 mock provider 宣布支付能力成立。

## Eval 5 — 不重复

同一个创建项目路径：

合格：
- Task 测 local validation。
- Slice 测真实创建与持久化。
- Stage 只在该行为是 Stage Outcome / direct regression 时验证高层结果，不重复所有 field cases。

不合格：
- 三层运行同一 18 个用例。

## Eval 6 — Observability 重要但不填空表

Stage 只触发：
- payment audit
- structured failure logging

合格：
- 只把这两个义务落到相关 Task。
- 真实支付 Slice 同时取得功能、audit、logging evidence。

不合格：
- 每个 Task 都列 Logging / Events / Crash / Metrics / Trace / Audit 六行，并写大量 N/A。

## Eval 7 — 已稳定 sink 不重测

已有稳定 analytics SDK，本 Stage 只新增一个 event。

合格：
- Task 实现 event。
- Slice 真实路径确认新 event 到达。
- 不重新验证 SDK 全套初始化。

不合格：
- 每个 Task 重新检查 API key、SDK init、网络、所有旧 events。

## Eval 8 — 产品缺口上抛

需求：“删除账户”。

Repository 已支持 delete endpoint，但产品未定义数据是立即删除、延迟删除还是可恢复。

合格：
`BLOCKED / Owner: Product`

不合格：
- Blueprint 按行业惯例选择 soft delete。

## Eval 9 — 局部 UI 细节不阻塞

产品已定义“失败后显示可恢复错误并允许重试”，仓库已有统一 ErrorBanner。

合格：
- Blueprint 沿用 ErrorBanner 并安排 wiring。
- 不回产品问 banner 在顶部还是底部。

## Eval 10 — 架构缺口上抛

Stage 要上传文件，但 Architecture 没有 object storage / ownership / signed access 方向。

合格：
`BLOCKED / Owner: Architecture`

不合格：
- Blueprint 自选 S3 / Supabase Storage。

## Eval 11 — 不做顺手重构

Current Stage 只改 checkout。

发现旁边 UserService 命名不好但不阻塞。

合格：
- 不纳入 Scope。

不合格：
- 顺手重构整个 service layer。

## Eval 12 — UI 早接

用户型 Stage 的真实 Outcome 需要 UI。

合格：
- 第一或很早的 Slice 形成 UI → backend → data 的薄真实链路。

不合格：
- 15 个 backend Task 完成后最后一个 Task 才首次接 UI。

## Eval 13 — Technical-only

Stage Contract 明确是 migration foundation，且下一 Stage 消费。

合格：
- Slice 用真实 migration / caller / data invariant 作为能力验证。

不合格：
- 强行造假 UI 只为了“看起来纵向”。

## Eval 14 — Direct Regression 克制

共享 session module 改动会直接影响 login。

合格：
- Stage regression 包含 login。

不合格：
- 因为 session 很重要而跑整个产品所有 journey。

## Eval 15 — 每个 Stage 一份合同

合格：
- 当前 Stage-2 只更新 `docs/blueprint/stages/Stage-2.md`。

不合格：
- 在 `docs/blueprint/stages/` 之外另放当前 Stage 合同
- 创建 `Stage-2-OBSERVABILITY.md`
- 创建 `STAGE2_SUPPLEMENT.md`
- 创建 `TASK_FIXES.md`
- 把 Stage-1 的合同内容抄进 Stage-2 形成第二份事实

## Eval 16 — READY 门禁

如果一个 Task 的 Target 仍写“相关 service 文件”，不确定具体路径：

合格：
- 继续 Repository Intake，不能 READY。

如果需要新的 Product / Architecture Decision：

合格：
- BLOCKED，列 Owner / Gap / Evidence / Blocks / Required Resolution。

## Product Refinement Routing

### Case: 分享语义缺失
Stage 已包含共享 Requirement，但未说明“同一对象访问”还是“复制副本”。

正确：
回 `product`（Focused Refinement），因为答案改变 ownership / lifecycle / revocation。

错误：
Blueprint 自己选择数据库上最方便的方式。

### Case: 按钮布局
Stage 行为已明确，只是不知道分享按钮放 toolbar 还是 overflow menu。

正确：
Blueprint / UI 按既有设计系统解决，不回 Product Refinement。

### Case: Product Refinement 改变原需求
细化过程中从“永久删除”改成“只归档”。

正确：
回 Product 更新 Product Definition / Product Atoms，再由 Chief Architect 重新冻结 Stage。


## Parallel Construction

### Safe fan-out

Task-1 freezes a stable shared interface. Task-2 implements backend adapter, Task-3 implements UI caller, Task-4 adds independent fixture/test support. Primary write surfaces are separate and each Task can form a valid local commit.

Expected:
- Task-2 / Task-3 / Task-4 are `parallel-safe`.
- Execution Graph fans out after Task-1.
- Human is told they may open 3 windows.
- Each Task only runs its Simple Test.
- fan-in runs one Slice Capability Test.

### Shared schema conflict

Two Tasks both redesign the same schema / migration chain.

Expected:
Keep sequential, or first create one prerequisite Task that freezes the shared schema boundary.

### Not worth parallelizing

Three tiny Tasks touch nearby code and coordination cost exceeds likely savings.

Expected:
`Parallel Work Recommendation: Stay sequential`.

### Step naming

Agent proposes `Step-7` as a tracked construction unit.

Expected:
Reject it. Use `Task-7`, or plain numbered actions inside Task-7.

## Capability Slice Semantics

### Case: 底座能力不串业务剧情

Stage 包含：孵化、记录灵感获得奖励、使用货币购买蛋。

正确：
- Slice-1 孵化能力跨 UI / domain / data 打通。
- Slice-2 灵感记录 + 奖励余额跨层打通。
- Slice-3 货币购买蛋跨层打通。
- 每个 Slice 可独立验证真实结果。

错误：
- 为了“产品闭环”强制规划成“孵猫 → 记灵感 → 赚钱 → 买狗蛋 → 孵狗”。

### Case: 运营参数不触发 Product Refinement

Foundation Stage 正在搭奖励规则和运营配置基础，未来后台可配置奖励金额。

正确：
- Blueprint 要求 reward amount 可配置并使用测试 seed。
- 不问用户“一条灵感具体奖励多少钱”。

错误：
- 因为不同金额会改变产品行为，就阻塞并进入 Product Refinement。


## Planning Anti-OverDefense

### Case: 假想 nil 风险

内部 typed domain object 已由 constructor / type contract 保证非空，没有真实输入路径可以产生 nil。

正确：
- 不新增 guard Task。
- 不新增 nil test。
- 不因为“更保险”扩大 Scope。

错误：
- 添加 defensive nil handling + fallback + tests。

### Case: Confirmed Defect 修根因

真实线上 / reproducible evidence 表明余额偶尔变成负数，根因是两个写入不在同一 transaction boundary。

正确：
- Blueprint 规划修 transaction / state ownership 根因。
- 加 targeted regression proof。

错误：
- 规划 `if balance < 0 { balance = 0 }`。

### Case: Live Uncertainty

Task 的 targeted test 已通过，相关代码未再变化。

正确：
- 不安排第二次同样 test。
- 继续后续 Task。

错误：
- “保险起见再跑一次，再跑整个 suite”。

### Case: Low-score hypothetical risk

模型想到“未来也许会有另一个 consumer 传入极端值”，没有当前 consumer、历史事故或 external contract 证据。

正确：
- Likelihood 只能低分。
- 不进入 Blueprint Scope。

错误：
- 增加兼容层、validation、future-proof abstraction。

### Case: Delete means absence

Requirement 明确替换旧 API，Architecture 没有兼容窗口。

正确：
- Task 包含旧实现、caller、config、tests、fallback、dependency 等级联清理。

错误：
- 保留 deprecated old path “以防回滚”。

### Case: Dry Run 不做开放式找坑

Execution Contract 已能从 Entry 走到 Exit。Dry Run 时模型想到一个极端理论 edge case。

正确：
- 先走 risk gate；低分则忽略。
- 不自动新增 Task。

错误：
- 每次 Dry Run 都继续扩 edge-case handling，导致 READY 永远延迟。

## Verification Authority

### Case: UI 审美

UI System / Handoff 已指定结构、Token、Component、State。

正确：
- Agent proof 检查机械一致性。
- 最终“好不好看 / 是否符合感觉”标 Human Review。

错误：
- Blueprint 写 `Agent verifies UI looks premium and balanced`.

### Case: Agent 可机械证明

Schema migration syntax 和 generated schema 可以由工具验证。

正确：
- Agent 验证。

错误：
- 为了保险把本可机械完成的检查交给 Human。

## Local Proof

### Case: 删除一个已确认废弃的静态 import

没有 runtime behavior、没有新的不确定性。

正确：
`Local Proof: static inspection / compiler evidence; no new test required.`

错误：
- 强制新增 unit test。
- 跑完整 Slice journey。


## Reasoning Compilation

### Case: 大型机械迁移

任务：
按已冻结 schema 和现有模式修改 30 个 DTO / fixture / generated caller。

正确：
- Reasoning 可以是 Low。
- 文件多、diff 大不构成 High。
- 不因工作量大自动升档。

错误：
- 因为“改 30 个文件很复杂”标 High。

### Case: 高风险但答案已冻结

任务：
实现 wallet debit + receipt。Architecture 已冻结 ledger authority、transaction boundary、idempotency key、failure semantics、proof。

正确：
- `Criticality: Critical`
- `Reasoning: Medium`
- 施工按合同实现，不重新设计账本协议。

错误：
- 因为涉及钱直接标 High。

### Case: 未决 transaction 语义

任务只有十几行，但不清楚 debit、receipt、queue 是否必须原子提交，retry 后 side effect 是否 unknown。

正确：
- Reasoning Score 进入 invalid / High 区域。
- Blueprint 不 READY。
- 先冻结 invariant / transaction / failure semantics，再重新编译 Medium Task。

错误：
- 给 Construction 标 `High`，让施工 Agent 自己想。

### Case: Repository Reality 冲突

合同要求调用 `ProjectRepository.save()`，真实仓库只有两套互相矛盾的 persistence path，测试和文档也不一致。

正确：
- Repository consistency = 2。
- Task 不得发布。
- Blueprint / Architecture 先 reconcile authority。

错误：
- 标 Medium，让 Agent 施工时自行选择。

### Case: Proof 未确定

安全敏感 Task 已写清代码目标，但蓝图不知道什么证据能证明权限边界正确。

正确：
- Proof certainty = 2，属于 planning defect。
- 先定义 proof，再 READY。

错误：
- 用 `review carefully` 代替 proof，或把 Task 标 High。

### Case: 不得为降分拆坏原子性

一个原子 transaction Task 分数偏高。

错误诱导：
拆成 `Debit`、`Receipt`、`Queue` 三个互相不完整 Task，只为了让每个分数变低。

正确：
先冻结 atomic invariant / failure semantics；只有真实可独立施工时才拆 Task。

### Case: Construction 不自行升 High

Task 标 `Medium (7)`。施工时发现现有 contract 无法同时满足真实 schema 与 Stage invariant。

正确：
`STOP → BLOCKED`，回 Blueprint / Architecture。

错误：
Construction 自己切 High reasoning，重新设计 schema / invariant 后继续。

### Case: Novel but frozen

项目首次接入一种新 Provider，但 Architecture 已冻结 provider、interface、failure mapping，仓库落点和 proof 也清楚。

正确：
Novelty 可以高，但整体 Task 仍可为 Medium。

错误：
只因为“项目第一次做”就标 High。


## Delegation Compilation

### Case: 短任务

Task：
修改一个已有 handler 的 20 行 wiring，Root 已经打开相关文件。

正确：
- Root 自己完成。
- Time Impact 负或接近负。
- 不 spawn。

错误：
- 因为可以拆成“读代码 / 改代码 / review”就创建 3 个 subagent。

### Case: Deterministic Tool

需要找所有旧 API caller。

正确：
- grep / AST / language server。
- 不创建 Explore Agent，除非结果规模巨大且需要多轮判断 / 压缩。

错误：
- 为一次 grep 创建 subagent。

### Case: Context Compression

需要读取几十个文件、长日志和多轮 grep，Root 最终只需要 canonical path + 3 evidence locations。

正确：
- Delegation Score 高。
- Time Impact 至少 Neutral / Positive。
- read-only Explore subagent 合理。

### Case: Root 已加载 context

Root 已经完成 80% repository archaeology，只差综合结论。

正确：
- Root 直接总结。
- 不让 Child 重新读取相同材料。

错误：
- 因为“探索很重”仍 spawn Explore Agent。

### Case: Independent Verifier

Critical wallet transaction 已实现，需要独立枚举 crash windows 并跑限定测试。

正确：
- 可以使用 read-only verifier。
- 即使 Time Impact = Neutral，也可因 independent evidence 明确授权。
- Child 不修改代码、不 spawn。

### Case: 两个实现 Task 可并行但不适合 subagent

两个 parallel-safe Task 已经建议 Human 开两个独立 worktree。

正确：
- `Parallel Work Recommendation` 给 Human。
- 不自动推导 Root 还要 spawn 两个 Child。

### Case: Shared migration

两个工作都需要改同一 migration / generated schema。

正确：
- State Isolation 低，veto delegation / parallel implementation。

错误：
- 觉得多 Agent 能加速而并行写。

### Case: Long autonomous investigation

长 integration suite 失败后，需要持续跑 targeted tests、读日志、归因，而 Root 有另一条独立实现可继续。

正确：
- subagent 合理。
- Purpose 是 autonomous investigation。
- 返回 failing scope + cause + evidence。

### Case: Plain long command

只需要执行一个 20 分钟 deterministic integration command，没有中间判断。

正确：
- 启动普通 process / tool。
- 不启动 LLM subagent。

### Case: High reasoning Task

Task 仍有未决状态机和 failure semantics。

正确：
- 修 Blueprint。
- 不通过 spawn 多个强模型来“共同想”。

### Case: Recursive spawn

Child 想再创建 reviewer child。

正确：
- 拒绝；max depth = 1。

### Case: 时间负收益

Candidate 独立且可压缩，但工作预计很短，spawn + context + fan-in 明显更慢。

正确：
- Time Gate veto。
- Root 直接完成。\n\n## Current Task Boundary\n\n### Case: Human 提到后续想法\n\n当前：\nTask-4 只要求把 Functional UI 接到真实状态。\n\nHuman：\n“这里以后最好加一个更漂亮的转场动画。”\n\n正确：\n- 判断这条反馈是否影响 Task-4 的完成条件。\n- 如果不影响，Task-4 继续按当前边界完成。\n- 不提前做后续 UI polish / motion Task。\n\n错误：\n- 因为 Human 提到了动画，就顺手开始后续 Task。\n\n### Case: Human 修正当前 Task\n\n当前：\nTask-6 要把删除确认文案接到已有确认流程。\n\nHuman：\n“这里不是删除全部，只删除当前 item。”\n\n正确：\n- 这属于对当前 Task 语义的修正。\n- 更新当前实现并继续完成 Task-6。\n\n错误：\n- 把反馈扩张成重新设计整个删除系统或提前处理后续 cleanup Task。\n\n原则：\n\n> Human feedback may refine the current Task, but must not expand it into later Tasks.\n

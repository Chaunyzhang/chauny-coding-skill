# EVALS

用于检查施工蓝图是否保持 authority boundary、命名克制、语义保真、真实集成、低重复验证和编译期克制。每个 case 都是独立 failure mode。

## Eval 1 — 不重新引入 Capability Card
输入：Stage-2 有 Requirement-3，但没有 Capability-n。  
合格：直接消费 Stage Contract + Product authority；只有真正产品语义缺口才 BLOCKED。  
不合格：要求先创建 Capability Card / Capability-n 才规划。

## Eval 2 — 命名收敛
合格：Stage-2、Requirement-3、Decision-1、Slice-1、Task-1。  
不合格：R/H/ES/AC/EVID/OBS 等二次编号或 Step-n 施工对象。

## Eval 3 — Task 不做全链路测试
输入：Task-2 只增加纯 mapping 分支。  
合格：static/targeted unit/compile 中最便宜充分证据。  
不合格：全仓 suite、真机 journey、analytics/crash、Stage acceptance 全跑。

## Eval 4 — Slice 做真实能力测
输入：支付 Slice 依赖真实 sandbox webhook。  
合格：Task 局部证 provider adapter；Slice 用 sandbox checkout + webhook + state update。  
不合格：只有 mock provider 就宣布支付能力成立。

## Eval 5 — 同一事实不重复
输入：创建项目路径。  
合格：Task 证 local validation；Slice 证真实创建/持久化；Stage 只在 Outcome/direct regression 需要时证高层结果。  
不合格：三层重复同一套用例。

## Eval 6 — Observability 不填空表
Stage 只触发 payment audit + structured failure logging。  
合格：只落这两项，并可在真实支付 Slice 同时取功能/audit/logging evidence。  
不合格：每 Task 列全套 observability 并填 N/A。

## Eval 7 — 稳定 sink 不重测
已有稳定 analytics SDK，本 Stage 只加一个 event。  
合格：Task 实现，Slice 真实路径确认新 event 到达；不重验 SDK 全初始化。  
不合格：每 Task 重查 key/init/network/旧 events。

## Eval 8 — 产品缺口上抛
Requirement 是“删除账户”，仓库有 endpoint，但未定义立即/延迟/可恢复删除。  
合格：`BLOCKED / Owner: Product`。  
不合格：Blueprint 按惯例自选 soft delete。

## Eval 9 — 局部 UI 细节不阻塞
产品已定义“失败后可恢复并允许重试”，仓库有统一 ErrorBanner。  
合格：沿用 ErrorBanner，不问 banner 顶部/底部。  
不合格：把局部 layout 当产品缺口。

## Eval 10 — 架构缺口上抛
Stage 要上传文件，但 Architecture 未冻结 object storage / ownership / signed access。  
合格：`BLOCKED / Owner: Architecture`。  
不合格：Blueprint 自选 Provider。

## Eval 11 — 不做顺手重构
Current Stage 只改 checkout，旁边 UserService 命名差但不阻塞。  
合格：不进 Scope。  
不合格：顺手重构 service layer。

## Eval 12 — UI 早接
用户型 Stage Outcome 需要 UI。  
合格：很早的 Slice 形成 UI→backend→data 薄真实链。  
不合格：大量 backend Task 后才首次接 UI。

## Eval 13 — Technical-only
Stage Contract 明确是 migration foundation，下一 Stage 消费。  
合格：以真实 migration/caller/data invariant 验证。  
不合格：强造 UI 只为“纵向”。

## Eval 14 — Direct Regression 克制
shared session 改动直接影响 login。  
合格：Stage regression 覆盖 login。  
不合格：因 session 重要而跑全产品 journeys。

## Eval 15 — 每 Stage 一份合同
合格：Stage-2 只更新 `docs/blueprint/stages/Stage-2.md`。  
不合格：另建 Stage-2-OBSERVABILITY、SUPPLEMENT、TASK_FIXES，或复制其他 Stage 形成第二份事实。

## Eval 16 — READY 门禁
Task Target 仍是“相关 service 文件”时：继续 Repository Intake，不能 READY。  
若需新 Product/Architecture Decision：BLOCKED，并给 Owner/Gap/Evidence/Blocks/Required Resolution。

# Product Refinement Routing

### Case — 分享语义缺失
Stage 有共享 Requirement，但未定义“同一对象访问”还是“复制副本”。  
正确：回 `product`，因答案改变 ownership/lifecycle/revocation。错误：Blueprint 自选数据库最方便方案。

### Case — 按钮布局
行为已明确，只是不知道分享按钮放 toolbar 还是 overflow。  
正确：按 UI/repository convention 处理，不回 Product。

### Case — Refinement 改变原需求
细化从“永久删除”变“只归档”。  
正确：Product 更新 Definition/Atoms，再由 Chief Architect 重新冻结 Stage；Blueprint 不继续沿旧合同。

# Parallel Construction

### Case — Safe fan-out
Task-1 冻结共享 interface；Task-2 backend adapter、Task-3 UI caller、Task-4 fixture/test support，write surface 独立且可单独 commit。  
正确：2/3/4 `parallel-safe`，Task-1 后 fan-out；Human 可开 3 窗口；各自 Local Proof；fan-in 后只跑一次 Slice Capability Test。

### Case — Shared schema conflict
两个 Task 都改同一 schema/migration chain。  
正确：保持 sequential，或先用一个 prerequisite Task 冻结共享 schema。

### Case — Not worth parallelizing
三个 tiny Task 改邻近代码，协调成本高于收益。  
正确：`Parallel Work Recommendation: Stay sequential`。

### Case — Step naming
Agent 提议 `Step-7` 作为可追踪施工单元。  
正确：拒绝；用 `Task-7`，或 Task 内普通编号动作。

# Capability Slice Semantics

### Case — 底座能力不串业务剧情
Stage 包含孵化、记录灵感得奖励、货币购买蛋。  
正确：拆成可独立成立/验证的能力 Slice；错误：为了“产品闭环”强串成完整剧情。

### Case — 运营参数不触发 Refinement
Foundation Stage 搭奖励规则与运营配置，未来后台可配奖励金额。  
正确：要求 amount 可配置并用 seed；不问具体奖励数值。错误：因此阻塞 Product Refinement。

# Planning Anti-OverDefense

### Case — 假想 nil 风险
typed domain constructor 已保证非空，无真实 nil path。  
正确：不加 guard、不加 nil test。错误：因“更保险”加 handling/fallback/tests。

### Case — Confirmed Defect 修根因
余额负数可复现，根因是两个写入不在同一 transaction。  
正确：修 transaction/state ownership + targeted regression。错误：`if balance < 0 { balance = 0 }`。

### Case — Live Uncertainty
targeted test 已通过且代码未变。  
正确：不重复测试。错误：“保险起见再跑一次/再跑全套”。

### Case — Low-score hypothetical risk
模型想到未来 consumer 可能传极端值，但无 consumer/history/contract evidence。  
正确：Likelihood 低，不进 Scope。错误：加 future-proof compatibility/validation/abstraction。

### Case — Delete means absence
Requirement 替换旧 API，Architecture 无 compatibility window。  
正确：级联删除旧 implementation/caller/config/tests/fallback/dependency 等。错误：保留 deprecated path “以防回滚”。

### Case — Dry Run 不做开放式找坑
合同已可从 Entry 到 Exit，Dry Run 想到理论极端 edge case。  
正确：重新过 Risk Gate，低分忽略。错误：无限扩 edge-case handling。

# Verification Authority

### Case — UI 审美
UI System 已指定机械规范。  
正确：Agent 证 Token/Component/State compliance；“好不好看”交 Human。错误：Agent 宣布“looks premium and balanced”。

### Case — Agent 可机械证明
migration syntax / generated schema 可由工具验证。  
正确：Agent 验证。错误：为保险交 Human。

# Local Proof

### Case — 删除废弃静态 import
无 runtime behavior、无新不确定性。  
正确：`static inspection / compiler evidence; no new test required`。错误：强制新增 unit 或完整 Slice journey。

# Reasoning Compilation

### Case — 大型机械迁移
冻结 schema/模式下改 30 个 DTO/fixture/generated caller。  
正确：可 Low；文件多/diff 大不自动 High。

### Case — 高风险但答案已冻结
wallet debit + receipt 已冻结 ledger authority、transaction、idempotency、failure、proof。  
正确：`Criticality: Critical` + `Reasoning: Medium`。错误：涉及钱就 High。

### Case — 未决 transaction 语义
代码很短，但 debit/receipt/queue atomicity 与 retry side effect 未定。  
正确：planning defect / invalid；先冻结 invariant/transaction/failure，再编译 Medium。错误：交 Construction High 自己想。

### Case — Repository Reality 冲突
合同指向 `ProjectRepository.save()`，真实仓库有两套冲突 persistence path。  
正确：Repository consistency=2，不发布，先 reconcile authority。错误：Medium 后让施工自选。

### Case — Proof 未确定
安全敏感 Task 目标明确，但不知道如何证明 permission boundary。  
正确：Proof certainty=2；先定义 proof。错误：`review carefully` 或 High。

### Case — 不得为降分拆坏原子性
atomic transaction Task 分高。  
正确：先冻结 invariant/failure semantics，只在真实独立边界拆。错误：拆成 Debit/Receipt/Queue 三个不完整 Task 只为降分。

### Case — Construction 不自行升 High
Task `Medium (7)`，施工发现真实 schema 与 Stage invariant 不能同时满足。  
正确：`STOP → BLOCKED`。错误：施工切 High 并重设计。

### Case — Novel but frozen
项目首次接 Provider，但 provider/interface/failure/repo target/proof 已冻结。  
正确：仍可 Medium。错误：只因首次就 High。

# Delegation Compilation

### Case — 短任务
已有 handler 20 行 wiring，Root 已打开相关文件。  
正确：Root；Time Impact 负/近负。错误：拆读/改/review 三个 subagent。

### Case — Deterministic Tool
找所有旧 API caller。  
正确：grep/AST/language server；只有结果巨大且需多轮判断/压缩时才考虑 Explore Agent。

### Case — Context Compression
几十文件+长日志+多轮 grep，Root 最终只要 canonical path + 3 evidence locations。  
正确：高 Delegation Score，read-only Explore 合理。

### Case — Root 已加载 context
Root 已完成 80% archaeology。  
正确：Root 总结，不让 Child 重读同材料。

### Case — Independent Verifier
Critical wallet transaction 需要独立枚举 crash windows + targeted tests。  
正确：可 read-only verifier；Time Neutral 也可因 independent evidence；Child 不改代码、不 spawn。

### Case — Parallel-safe 但不适合 subagent
两个 Task 已建议 Human 独立 worktree。  
正确：Parallel Work 给 Human，不自动推出 Root spawn 两 Child。

### Case — Shared migration
两个工作都改同一 migration/generated schema。  
正确：State Isolation 低，veto parallel implementation/delegation。

### Case — Long autonomous investigation
integration suite 失败，需要多轮 targeted run/log diagnosis，Root 有独立工作。  
正确：可 autonomous investigation Child，返回 failing scope + cause + evidence。

### Case — Plain long command
只运行 20 分钟 deterministic command，无中间判断。  
正确：普通 process/tool，不启动 LLM subagent。

### Case — High reasoning Task
仍有未决 state machine/failure semantics。  
正确：修 Blueprint，不用更多 Agent 补偿。

### Case — Recursive spawn
Child 想再创建 reviewer child。  
正确：拒绝；depth=1。

### Case — 时间负收益
Candidate 独立可压缩，但工作很短，spawn+fan-in 更慢。  
正确：Time Gate veto，Root 做。

# Current Task Boundary

### Case — Human 提到后续想法
当前 Task-4 只要求 Functional UI 接真实状态；Human 说以后加漂亮转场。  
正确：若不影响 Task-4 Done When，继续当前 Task，不提前做 motion/polish。  
错误：因 Human 提到未来想法就开始后续 Task。

### Case — Human 修正当前 Task
Task-6 是删除确认；Human 澄清“只删当前 item”。  
正确：这是当前 Task 语义修正，更新并继续 Task-6。  
错误：扩张成重设计删除系统或提前 cleanup。

原则：Human feedback may refine the current Task, but must not expand it into later Tasks.

# Semantic / Architecture Compilation Regressions

## Eval 追加 1 — Binding Atom 不得只做 ID Trace
Requirement-7：AI 可使用/修改引用灵感；Atoms 要求 AI 获得实际内容、保持原对象 identity、用户确认后修改原对象。  
正确：Traceability 引 Requirement + Atoms；每 Atom 有真实 construction coverage；Capability Test 证“理解实际内容并修改原对象”。  
错误：只传 `referenceId` 就算覆盖。

## Eval 追加 2 — Implementation Shape 从 Architecture 编译
Architecture：Reward owns reward calculation；Wallet owns balance mutation；Purchase 只能走 Wallet public API。  
正确 Shape 至少表达 owner、required reuse、allowed dependency、forbidden bypass、expected change boundary；不创建新编号对象。

## Eval 追加 3 — Blueprint 不能临场造 Domain
Repository 无自然 owner，新 Requirement 引入长期 lifecycle/state ownership。  
正确：`Owner: Architecture`。错误：Blueprint 自建 NewDomainManager/NewService 当机械细节。

## Eval 追加 4 — Existing Authority 优先复用
已有 `PermissionPolicy.canEdit(...)`。  
正确：Shape/Task 明确复用。错误：另造 `actor.id == ownerId` 业务判断。

## Eval 追加 5 — 多文件不是自动坏
Requirement 合法触及 Purchase/Wallet/Inventory 且走各自 public interface。  
正确：允许多模块改动，不因跨 3 domain 自动 BLOCK。

## Eval 追加 6 — Change Boundary 发现真实漂移
Stage 只涉及 Reward+Wallet，计划却重构 Search/Auth/Settings 且无义务/依赖。  
正确：移除这些 change。

## Eval 追加 7 — Shared 不是业务垃圾场
Reward calculation 被三个 Feature 调用。  
正确：仍由 Reward Domain 拥有并经 public API 复用。错误：因多调用点就搬到 Shared/RewardUtils。

## Eval 追加 8 — Product 已有答案不回问
Atom 已确认“分享访问同一对象，不复制”。  
正确：直接消费 Atom。错误：Focused Refinement 再问同一问题。

## Eval 追加 9 — Task 只带最小 Implementation Constraints
Stage Shape 已冻结 Wallet ownership；只有 Purchase debit Task 需要 `Owner: Wallet / Use: Wallet.debit / Do Not Bypass: direct balance write`。  
正确：其他纯 UI Task 不填整套空字段。

## Eval 追加 10 — Authority 未冻结时 Reasoning Invalid
Task 要 Construction 决定余额归 Purchase 还是 Wallet。  
正确：Contract/ownership/authority 是 Hard Planning Defect，回 Architecture；不发布 Task。

## Eval 追加 11 — Semantic Capability Test
HTTP 200、DB 有记录，但 AI 没拿到被引用灵感内容。  
正确：Slice 未通过，因为 binding Atom 的真实能力未成立。

## Eval 追加 12 — 原版能力不得因优化丢失
优化后必须仍生效：
- Planning Guardrails
- Reasoning Compilation Gate
- Delegation Compilation Gate
- Parallel Construction
- Verification 分层
- Operational Obligations
- Product Focused Refinement Gate
- UI Handoff
- Dry Run
- STOP / no-pitfall coordination

缺任一项视为 Skill regression。

# Repair Mode Regressions

## Repair Eval 1 — 必须有正式 Handoff
Stage Verifier 只说“Wallet 有问题，修一下”，没有 Frozen Finding / Target State / Boundary / Proof。
正确：不进入 Repair Mode；要求完整 Repair Handoff，不能从聊天猜 Scope。

## Repair Eval 2 — 同颗粒度，不是简版修复清单
Repair Handoff 完整，但输出只有“改 Wallet、删旧 helper、跑测试”。
正确：使用正常 Blueprint 的 Task granularity、Reasoning、precise Targets、Actions、Local Proof、Done When 等；只是范围更窄、合同临时。

## Repair Eval 3 — canonical Stage 在 Repair Verified 前只读
Repair 执行到一半，Planner 想同步修改 `docs/blueprint/stages/Stage-4.md`。
正确：拒绝；所有中间事实只进 `.workbench/repairs/Stage-4/`。

## Repair Eval 4 — Handoff Boundary 不足时上抛
正确修复 F-02 需要新增长期 Billing authority。
正确：`BLOCKED / Owner: Architecture`；不扩大 Repair Handoff，不自己冻结 authority。

## Repair Eval 5 — REPAIR VERIFIED 才能 Reconcile
Builder 声称改完，但 Stage Verifier 仍有 UNRESOLVED Finding。
正确：不得修改 canonical Stage Execution Contract。

## Repair Eval 6 — Reconciliation 只保留最终事实
Repair Verified 后 canonical Task-3 的原方案已失效。
正确：按 final Repository Reality 替换/删除受影响内容；不 append F-01、patch 过程、旧/新双版本。

## Repair Eval 7 — 未受影响部分保持稳定
Repair 只影响 Wallet Slice。
正确：Reconciliation 不顺便重写 Search / Analytics / UI 无关章节。

## Repair Eval 8 — Historical Stage 不改写
Repair Handoff 指向一个在 cycle 开始前已 frozen 的历史 Stage。
正确：BLOCKED；route 新 maintenance / repair work unit，不修改历史 Stage contract。

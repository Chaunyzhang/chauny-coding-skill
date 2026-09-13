# Verification Strategy for Blueprint

目标不是“测试最多”，而是为当前真正需要证明的事实安排最小充分证据。

> 同一事实原则上只在最便宜且足以证明它的层级验证一次；跨层重复必须有新增证据价值。

## Task Local Proof

证明局部改动。`Local Proof` 不等于必须运行测试；先过 Live Uncertainty Gate。可用：
- existing invariant / passing evidence
- static / structural inspection
- unit / pure logic（需要时）
- target compile/typecheck/lint（需要时）
- schema/config/migration/generated consistency
- permission/error mapping

默认不跑全仓 tests、E2E、真机、deploy、remote sink inspection。

特殊执行约束：
- Task 只本地 commit，不 `git push` / 等 CI；每个 Slice 收口再一次性 push 一轮 CI。
- iOS：Agent 不本地运行 App/Xcode、不做 iOS 编译或 `xcodebuild test`；Human 用共享 DerivedData 增量编译。单测代码照写，运行归 Stage 前/发版前脚本补测。

没有需要执行才能消除的不确定性时，可以不新增 executable check。

## Slice Capability Test

只在真实能力尚未被等价证据证明，或 Stage Acceptance / Live Uncertainty 要求时执行。

证明一个真实能力路径，例如 client→API→DB、auth callback→session→client、payment sandbox→webhook→state、upload→storage→retrieval、queue→job→state、AI provider→result→product state。

只覆盖：
- Slice 成立所需关键 success behavior；
- binding Atom / Representative Example 指定的真实语义；
- Stage Contract、Confirmed Defect regression 或 admitted risk 明确触发的 failure/permission/operational behavior。

binding Atom 定义“真完成 vs 空壳完成”时，Capability Test 必须证明真实产品语义，不能只证明技术中间量。不要复制 Task 全部 unit cases。

## Stage Module Test

证明：
- Stage Outcome / Visible Delta。
- Current binding product semantics（必要时组合证明，避免重复 Slice）。
- Acceptance Criteria。
- Direct Regression。
- triggered Operational Obligations。
- Stop Rule。

不是全产品 regression suite。用户型 Stage 可包含简短 Hands-on Steps：
`Who/Entry → Preconditions → Steps → Expected Visible Result → Expected Persistence/State → Required Failure（仅 Acceptance 需要）`

不另造 Hands-on ID。

## 跨层重复与真实集成

只有明显需要新证据才跨层重复，例如 mock≠real Provider、async/process boundary、data integrity、payment、permission/security、migration、public contract/multi-client compatibility、本 Stage 直接改既有关键路径、历史事故保护。

通常需要真实 sandbox/test environment 的边界：
- payment webhook/subscription/refund
- auth callback/token flow
- push/email delivery config
- AI provider response/stream/schema
- object storage signed access
- queue/async runtime
- analytics/crash sink 首次建立或重大改变

已有稳定 Provider 且本 Stage 只改纯业务逻辑时，不重复验证 Provider init。

## Specialized Verification Triggers

**Contract Test**：至少两个独立发布 consumer 共享 API/event、真实旧 client/new server compatibility window、或 public API/SDK 有外部承诺时才建。

**Load / Performance**：只有明确 SLO/SLA、capacity/latency/cost 是 Stage 风险、可信峰值假设或 Foundational Decision break point 接近时；必须有可判定目标如 `p95 < X at Y rps`。

**Migration**：重大 migration 才规划 representative rehearsal、idempotency/resume、rollback/recovery、必要 mixed-version、count/checksum/invariant；小而可逆 migration 不需要生产规模演练。

**Direct Regression**：只保护本次改动直接可能破坏的既有行为，如 shared module/schema、public API/event、auth/session、provider/runtime、migration/shared persistence。无具体影响路径不默认全仓 regression。

## Observability Evidence

功能与运行证据可以同一真实路径取得，例如一次 sandbox checkout 同时证明 state、audit、structured log、product event。不要为不同 evidence 类型重复 journey。完整运行义务见 `operational-obligations.md`。

## Verification Authority

- **Agent**：build/typecheck/lint、unit/integration/contract/migration、schema/generated、static rules、UI Token/Component/State compliance、machine-readable runtime evidence。
- **Human**：UI 审美/质感/视觉平衡、Motion 主观感受、真人操作体验、用户明确保留的主观接受。
- **External**：第三方后台、审核/合规、特定设备/账户、Agent 无权访问的运营系统。

Blueprint 只准备 Human/External 最短检查入口，不伪造 PASS；本可机械证明的事实也不得转嫁 Human。

## CI

按成本放置：PR 用快且稳的 targeted checks；integration 用共享环境 Slice tests；nightly 放慢 regression/contract；release 放真正发布风险验证。Flaky test 隔离修复，不靠无限 retry 变绿。

## Stop / Self-check

新增验证前回答：
1. 具体不知道什么？
2. 会改变什么决定？
3. 失败后下一步有何不同？

答不上来就不安排；证据充分且实现未变时不重复。

完成前检查：是否有无 Trigger 的 test、Task/Slice/Stage 重复同一事实、纯“再跑一次测试”的 Task、真边界全 Mock、无直接影响依据的全仓 regression、无 trigger 的 load/contract/migration test，以及本可合并到同一真实路径的重复 evidence。

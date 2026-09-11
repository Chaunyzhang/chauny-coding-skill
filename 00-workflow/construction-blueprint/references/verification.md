# Verification Strategy for Blueprint

Blueprint 的目标不是“测试最多”，而是只为当前真正需要证明的事实安排足够证据。

## 核心规则

> 同一事实原则上只在最便宜且足以证明它的层级验证一次。

重复验证必须说明新增证据价值。

## 1. Task Local Proof

证明局部改动本身。

`Local Proof` 不等于必须运行测试。先问是否存在 Live Uncertainty；没有则优先使用已有证据、静态检查或结构性证明。

可选证据：

- existing invariant / existing passing evidence
- static / structural inspection
- unit / pure logic（需要时）
- target compile / typecheck（需要时）
- schema mapping
- permission branch
- config wiring
- migration syntax
- generated artifact consistency
- error mapping

特点：

- 成本与当前不确定性匹配。
- 定位直接。
- 不需要完整真实产品路径。
- 如果没有需要执行才能证明的事实，可以不新增执行性检查。

不要默认：

- 全仓 tests
- E2E
- 真机
- deploy
- remote sink inspection
- 本地运行 App / Xcode、iOS agent 侧编译与 `xcodebuild test`（编译归人类共享 DerivedData 增量执行；单测写而不跑，运行归 Stage 前 / 发版前脚本补测）
- `git push` / CI 等待（Task 只本地提交；push 属 Slice 收口）

## 2. Slice Capability Test

只有 Slice 的真实能力尚未被等价证据证明、或 Stage Acceptance / Live Uncertainty 要求时才执行。

证明一个真实能力路径工作。

常见：

- client → API → DB
- auth callback → session → client
- payment sandbox → webhook → state
- upload → storage → retrieval
- queue → job → state
- AI provider → stream / result → product state

只验证关键成功路径，以及 Stage Contract、Confirmed Defect regression 或 risk gate 明确触发的失败 / permission / operational behavior。

不要把 Task 的全部 unit case复制过来。

## 3. Stage Module Test

证明：

- Stage Outcome。
- Acceptance Criteria。
- Visible Delta。
- Direct Regression。
- triggered Operational Obligations。
- Stop Rule。

Stage Module Test 不是全产品 regression suite。

用户型 Stage 可以包含简洁 Hands-on Steps：

```text
Who / Entry
Preconditions
Steps
Expected Visible Result
Expected Persistence / State
Required Failure (only if Stage Acceptance requires)
```

不需要再创建独立 Hands-on ID。

## 什么时候跨层重复

只在明显需要新证据：

- mock 无法证明真实 Provider。
- async / process boundary。
- data integrity。
- payment。
- permission / security。
- schema migration。
- public contract / multi-client compatibility。
- 本 Stage 修改了既有关键路径。
- 历史事故要求保护。

## Real Integration

通常应真实 sandbox / test environment：

- payment webhook / subscription / refund
- auth provider callback / token flow
- push / email delivery config
- AI provider response / streaming / schema
- object storage signed access
- queue / async runtime
- analytics / crash sink 的首次建立或重大改变

已有稳定 Provider 接入且本 Stage 只改纯业务逻辑时，不需要每个 Slice重新验证 Provider 初始化。

## Contract Test

触发：

- 至少两个独立发布消费者共享 API / event。
- 旧 client 与新 server 存在真实兼容窗口。
- public API / SDK 有外部承诺。

无触发时不建立复杂 contract testing machinery。

## Load / Performance

只在：

- 有明确 SLO / SLA。
- 容量 / latency / cost 是本 Stage 风险。
- 发布峰值有可信假设。
- Foundational Decision Break Point 接近。

必须有可判定标准，例如：

`p95 < X at Y rps`

没有可信目标就不要“跑一下看看”。

## Migration

重大 data / schema migration：

- staging / representative data rehearsal
- idempotency / resume
- rollback / recovery
- mixed-version compatibility（需要时）
- count / checksum / invariant

小而可逆 migration 不需要生产规模演练。

## Direct Regression

只测试本次改变直接可能破坏的既有行为。

常见触发：

- shared module。
- shared DB schema。
- public API / event。
- auth / session。
- provider / runtime。
- migration。
- shared persistence。

不要因为模糊的“不确定”就默认全仓 regression；必须指出具体 Live Uncertainty 或直接影响路径。

## Observability Evidence

测试证据与运行证据不同，但可以同一路径同时取得。

例如支付 Slice：

一次真实 sandbox checkout 可以同时证明：

- 功能状态变化正确。
- audit record 可检索。
- structured failure log 可见。
- product event 到达（如果 Stage 要求）。

不要为四种证据重复跑四遍相同 journey。

## CI 放置

推送节奏：Task 只本地提交，不 push、不等待 CI；每个 Slice 收口一次性 push，触发一轮 CI，报错在收口统一处理。

按成本：

- PR：快且稳定的 Task / targeted tests。
- integration：共享环境 Slice tests。
- nightly：慢 regression / contract。
- release：真正与发布风险相关的关键验证。

Flaky test 应隔离修复，不靠无限 retry 变绿。

## Verification Authority

### Agent

适合机械证明：

- build / typecheck / lint
- unit / integration / contract / migration test
- schema / generated artifact
- static rules
- UI Token / Component / State compliance
- machine-readable runtime evidence

### Human

适合主观或真人专属：

- UI 审美 /质感 /视觉平衡
- Motion 主观感受
- 真人操作体验
- 用户明确保留的产品主观接受

### External

适合 Agent 无权访问或必须由外部系统确认：

- 第三方后台
- 审核 /合规系统
- 特定设备 /账户
- 外部运营系统

Blueprint 只准备最短验证入口，不伪造 PASS。

## Live Uncertainty & Stop

新增验证前：

1. 具体不知道什么？
2. 会改变什么决定？
3. 失败后做什么不同？

答不上来，不安排。

证据已经充分且相关实现未变时，不重复执行。

## Blueprint 自检

完成前问：

1. 是否存在没有 Live Uncertainty / Acceptance / defect regression 依据的测试？
2. 是否同一行为在 Task、Slice、Stage重复测试？
3. 是否有 Task 只是为了“再跑一次测试”？
3. 是否真边界被全 Mock 掩盖？
4. 是否全仓 regression 没有直接影响依据？
5. 是否 load / contract / migration testing 没有触发条件却被机械加入？
6. 是否能把功能和 observability 证据合并在同一次真实路径？

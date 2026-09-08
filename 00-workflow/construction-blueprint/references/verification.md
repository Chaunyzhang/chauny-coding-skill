# Verification Strategy for Blueprint

Blueprint 的目标不是“测试最多”，而是把证据放在最合适的层级。

## 核心规则

> 同一事实原则上只在最便宜且足以证明它的层级验证一次。

重复验证必须说明新增证据价值。

## 1. Task Simple Test

证明局部改动本身。

常见：

- unit / pure logic
- target compile / typecheck
- schema mapping
- permission branch
- config wiring
- migration syntax
- generated artifact consistency
- error mapping

特点：

- 快。
- 定位直接。
- 不需要完整真实产品路径。

不要默认：

- 全仓 tests
- E2E
- 真机
- deploy
- remote sink inspection

## 2. Slice Capability Test

证明一个真实能力路径工作。

常见：

- client → API → DB
- auth callback → session → client
- payment sandbox → webhook → state
- upload → storage → retrieval
- queue → job → state
- AI provider → stream / result → product state

只验证关键成功路径，以及 Stage Contract 明确要求的失败 / permission / operational behavior。

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

不要因为“不确定”就默认全仓 regression。

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

按成本：

- PR：快且稳定的 Task / targeted tests。
- integration：共享环境 Slice tests。
- nightly：慢 regression / contract。
- release：真正与发布风险相关的关键验证。

Flaky test 应隔离修复，不靠无限 retry 变绿。

## Blueprint 自检

完成前问：

1. 是否同一行为在 Task、Slice、Stage重复测试？
2. 是否有 Task 只是为了“再跑一次测试”？
3. 是否真边界被全 Mock 掩盖？
4. 是否全仓 regression 没有直接影响依据？
5. 是否 load / contract / migration testing 没有触发条件却被机械加入？
6. 是否能把功能和 observability 证据合并在同一次真实路径？

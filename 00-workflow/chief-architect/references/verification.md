# Verification Strategy

用于 Testing / Verification Strategy、Stage Verification Plan 与 Blueprint 审查。目标：用最小合理成本获得足够证据，避免“测试越多越专业”。

核心规则：**同一事实原则上只在最便宜且足以证明它的层级验证一次；只有新增证据价值明确时才在更高层重复。**

## 三层验证

### 1. Task 简单测

证明局部改动本身正确。适合 pure function / parser / validation、local state transition、schema/model mapping、config/dependency wiring、error branch，以及 permission/money/migration 等局部高风险逻辑。特点：快、局部、定位直接。

### 2. Slice 能力功能测

证明一个真实能力路径工作，例如 client→API→DB、API→queue→job→state、payment sandbox callback、push/email test channel、AI provider response、auth/permission path、upload→storage→retrieval。

只验证能力成立的关键路径，不复制 Task unit assertions。

### 3. Stage 模块测

证明本 Stage Product Outcome、关键模块组合、直接受影响既有能力、新触发的重要 Operational Obligation 与 Stop Rule 一起成立。不是全产品 regression suite 的同义词。

## 什么时候允许重复证明

只有在：

- mock 与真实边界风险明显不同。
- 跨进程 / async / provider 行为无法由低层证明。
- permission/payment/data-integrity/migration/security 风险高。
- 多客户端或独立发布服务存在 compatibility 风险。
- 本 Stage 修改既有关键路径。
- 历史事故要求明确 regression protection。

否则低层已经证明的事实不在高层重复。

## Real Integration vs Mock

通常需要真实 sandbox / test environment：payment webhook/refund/subscription、push/email delivery config、auth callback/token、AI output/streaming/schema、object-storage signed upload/access、crash/analytics/telemetry sink readiness。

通常可用 contract mock：低风险且稳定的 HTTP dependency；schema/failure semantics 简单且已有独立 provider smoke test；本次改动不涉及 provider 配置或协议行为。

“全 mock 绿”不能证明真实集成存在。

## Contract Testing

触发：至少两个独立发布消费方共享 API/event contract；客户端升级明显滞后服务端；第三方 SDK/public API 对外承诺兼容。

可用 schema diff、provider/consumer contract、compatibility fixture、generated-client compile check。无触发条件不建立复杂 contract-test 平台。

## Load / Performance

触发：已有 SLO/SLA；发布/营销/realtime/AI 有显著峰值；Foundational Decision Break Point 接近当前量级；capacity/cost 是 Current Stage 关键风险。

必须有可判断通过条件，例如 `p95 < X at Y rps`。没有可信容量假设，不做“跑一下看看”的伪压测。

## Migration Verification

重大 schema/data migration 按风险要求 staging 或等价规模 rehearsal、rollback/resume/idempotency、必要的 mixed-version compatibility，以及 count/checksum/invariant 验证。普通小 migration 不强制生产规模演练。

## CI 分层

按成本放置：PR 跑快速稳定直接影响测试；merge/integration 跑共享环境能力测试；nightly 跑较慢 regression/contract/selected integration；release 只跑真正与发布风险相关的关键验证。

Flaky test 必须隔离修复，不能靠无限 retry 掩盖。

## Direct Regression

Stage Contract 只列直接受影响的既有行为。常见触发：共同模块/数据结构、public API/event、permission/identity/session、shared persistence/migration、provider/runtime/infrastructure 被修改。

“可能什么都影响”不是扩大 regression 的理由。

## Observability Evidence

测试证据与运行可见性证据不互相替代：`test green ≠ telemetry sink ready`，`event arrived ≠ business behavior correct`。但可在同一次真实 Slice/Stage 路径同时取两类证据，避免重复运行。

## Blueprint 审查

Architecture 只检查：验证层级是否分配清楚；是否重复测试同一事实；高风险真实边界是否被全 mock；触发的 contract/load/migration 是否遗漏；是否把全仓 regression 当默认。

不要由 Architecture 重写每个 test case。

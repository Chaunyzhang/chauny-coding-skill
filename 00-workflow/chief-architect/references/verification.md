# Verification Strategy

用于定义 Testing / Verification Strategy、Stage Verification Plan 和 Blueprint 审查标准。

目标：用最小合理成本获得足够证据，避免“测试越多越专业”的误区。

## 核心规则

> 同一事实原则上只在最便宜且足以证明它的层级验证一次。

只有新增证据价值明确时，才允许在更高层重复验证。

## 三层验证

### 1. Task 简单测

证明本次局部改动正确。

适合：

- pure function / parser / validation
- local state transition
- schema / model mapping
- config / dependency wiring
- error handling branch
- 权限、金额、迁移等局部高风险逻辑

特点：快、局部、失败定位直接。

### 2. Slice 能力功能测

证明一个真实能力路径能够工作。

适合：

- client → API → DB
- API → queue → job → state update
- payment sandbox callback
- push / email real test channel
- AI provider real response
- auth / permission real path
- upload → storage → retrieval

只验证能力成立所需的关键路径，不把所有 Task unit case 再跑一遍。

### 3. Stage 模块测

证明本 Stage 的整体 Product Outcome 和直接回归成立。

适合：

- Stage 最终用户 / 系统结果
- 关键模块组合
- 直接受影响既有能力
- 本 Stage 新增的重要 Operational Obligation
- Stop Rule

Stage 模块测不是全产品 regression suite 的同义词。

## 什么时候需要重复证明

只在：

- mock 与真实边界风险明显不同。
- 跨进程 / async / provider 行为无法由低层证明。
- 权限 / 支付 / 数据完整性 / migration / security 风险高。
- 多客户端或独立发布服务存在兼容风险。
- 本 Stage 修改了既有关键路径。
- 历史事故表明需要回归保护。

否则低层已经证明的事实不在高层重复。

## Real Integration vs Mock

真实外部依赖应按风险选择验证方式。

### 通常必须真实 sandbox / test environment

- payment webhook / refund / subscription
- push / email delivery configuration
- auth provider callback / token flow
- AI provider output / streaming / schema
- object storage signed upload / access
- crash / analytics / telemetry sink readiness

### 通常可用契约 mock

- 已稳定的低风险 HTTP dependency
- 明确 schema、失败语义简单且已有单独 provider smoke test 的调用
- 本次改动不涉及 provider 配置和协议行为

“全 mock 绿”不能证明真实集成存在。

## Contract Testing

触发：

- 至少两个独立发布的消费方共享 API / event contract。
- 客户端升级明显滞后服务端。
- 第三方 SDK / public API 对外承诺兼容。

可选方式：

- schema diff
- provider / consumer contract
- compatibility fixture
- generated client compile checks

无触发条件不强制建立复杂 contract test 平台。

## Load / Performance Testing

触发：

- 已有明确 SLO / SLA。
- 营销 / 发布 / 实时 / AI 存在显著峰值。
- Foundational Decision 的 Break Point 接近当前量级。
- 成本和容量是当前 Stage 的关键风险。

必须有可判通过条件，例如：

`p95 < X at Y rps`

如果没有可信容量假设，不做“跑一下看看”的伪压测。

## Migration Verification

重大 schema / data migration：

- staging 或等价规模数据演练。
- rollback / resume / idempotency 说明。
- mixed-version compatibility when needed。
- 数据 count / checksum / invariant 验证。

不要每个小 migration 都做生产规模演练。

## CI 分层

建议按成本放置：

- PR：快速、稳定、直接影响测试。
- merge / integration：需要共享环境的能力测试。
- nightly：较慢 regression / contract / selected integration。
- release：真正与发布风险相关的关键验证。

Flaky test 隔离修复，不允许通过无限 retry 掩盖。

## Direct Regression

Stage Contract 只列**直接受影响**的既有行为。

判断方式：

- 修改了共同模块 / 数据结构。
- 修改了公共 API / event。
- 修改了权限 / identity / session。
- 修改了 shared persistence / migration。
- 修改了 provider / runtime / infrastructure。

“可能什么都影响”不是扩大 regression 的理由。

## Observability Evidence

测试证据和运行可见性证据不互相替代：

- test green ≠ telemetry sink ready
- event arrived ≠ business behavior correct

但可以在同一次真实 Slice / Stage 验证中同时获取两类证据，避免再跑一遍相同路径。

## Blueprint 审查

架构师只检查 Blueprint：

- 有没有清楚分配验证层级。
- 是否重复测试同一事实。
- 高风险真实边界是否被全 mock 掩盖。
- 必要 contract / load / migration test 是否因触发条件被漏掉。
- 是否把全仓 regression 当默认。

不要由架构师重新设计每个 test case。

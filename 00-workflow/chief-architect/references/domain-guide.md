# Conditional Domain Guide

用途：防止重要技术域被静默遗漏，同时避免每个项目都跑一遍百科式问卷。

使用方式：先根据 Product Definition + Product Atoms、Current / Near Stage、Repository Reality 和风险判断哪些域被触发；只读取 / 展开被触发域。未触发域不创建空章节，不逐项写 `Not Applicable`。

## 1. Client / Offline / Cross-device

触发：移动端、Web consumer app、Desktop、本地缓存、弱网、离线、跨端共享。

检查：

- Delivery Surface 与各端职责。
- 客户端数据层、网络层和状态管理边界。
- 离线等级：无离线 / 只读缓存 / 可写离线。
- 可写离线时的 queue / replay / idempotency / conflict resolution。
- token refresh、弱网和 session 语义。
- 本地敏感数据加密与退出清理。
- 跨端共享策略是否是高迁移成本决定。
- App 旧版本兼容窗口与 server API 兼容。
- Remote config / feature flags / kill switch。
- 客户端权限信息不得成为最终授权依据。

不要默认“离线以后再加”；如果 Future 明确需要可写离线，今天的数据所有权和同步边界必须能演进过去。

## 2. API / Interface

触发：任何跨模块 / 客户端 / 外部系统接口；多个独立发布消费方；domain events。

检查：

- REST / RPC / GraphQL / events 的适用性。
- public contract SoT。
- error envelope / stable error code。
- pagination / filter / sorting。
- write idempotency。
- API versioning / breaking-change / sunset。
- BFF / aggregation boundary。
- large payload 是否走 direct upload。
- time / money / enum serialization。
- event contract compatibility。
- 多消费方时 contract testing。

不要直接把 ORM entity 暴露成公共契约。

## 3. Identity / Access / Admin

触发：登录、账户、组织、角色、权限、管理员、support access、Agent tool execution。

检查：

- Identity Provider / user ID / business identity 的边界。
- session / token / refresh / revocation。
- MFA / passkey / SSO 是否属于 Near / Future。
- authorization 模型：role / resource / ownership / policy。
- server-side enforcement。
- admin RBAC 与 high-risk action audit。
- support access 是否最小授权、按工单、可审计。
- Agent 权限不得超过发起用户。

## 4. Data Core

触发：数据库、cache、search、queue / jobs、domain events、schema migration。

检查：

- Primary Database 对 Current + Architecture-Shaping Future 的适配。
- System of Record。
- ORM / query builder / SQL 与 transaction boundary。
- unique constraint / consistency invariant。
- read replica / sharding 的真实 trigger，不提前实现。
- cache / search / vector 都是 derived data 时的 rebuild path。
- DB → cache / index / vector 的写扩散和丢失发现。
- Search 查询形态决定引擎。
- Queue / Job retry、dead letter、idempotency。
- Domain Event 原子发布、outbox / CDC when needed。
- schema migration / zero-downtime expand-contract。
- backup / restore 与 retention。

禁止派生存储成为唯一真相且无重建路径。

## 5. Realtime

触发：presence、chat、collaboration、live update、AI streaming、实时推送状态。

检查：

- 真实延迟需求：polling / SSE / WebSocket。
- mobile background 限制和降级。
- subscription granularity 与 server-side authorization。
- reconnect / backoff / gap recovery / deduplication。
- delivery semantics：可丢 vs 必达。
- 多实例广播骨干。
- presence TTL。
- backpressure / hot channel。
- concurrent connection 和 cost break point。

不要把 WebSocket 当可靠消息队列。

## 6. AI / Agent Platform

触发：生成、聊天、RAG / memory、Agent、tool calling、embedding、speech、image、AI streaming。

检查：

- provider key 与 AI gateway 边界。
- model routing 能否在不改业务语义下切换。
- fallback / timeout / budget exhaustion。
- provider-specific SDK 是否被隔离。
- streaming protocol / cancel / partial failure。
- short-term context vs long-term memory。
- vector data 作为 derived data 的 rebuild / deletion。
- context budget / summarization。
- Agent tool allowlist / parameter validation / user permission inheritance。
- max steps / token / cost / time。
- irreversible action 是否 human confirmation。
- prompt injection / retrieved content isolation。
- prompt version / environment / rollback。
- golden set / model upgrade eval / shadow or limited rollout。
- content safety / moderation responsibilities。
- usage / token / cost accounting and kill switch。

禁止 Agent 无限预算、超越用户权限或 Provider SDK 散落业务代码。

## 7. Money / Payment / Billing

触发：真实支付、订阅、退款、虚拟币、积分、库存、提现、分账。

检查：

- ledger / balance model。
- append-only money events when appropriate。
- idempotency for charge / refund / reward / webhook。
- order / refund / subscription state machine。
- provider signature / amount / currency verification。
- webhook duplicate / reorder / delayed delivery。
- webhook 之外的主动查询 / reconciliation。
- suspended intermediate states and compensation。
- transaction / saga / outbox boundary。
- inventory oversell prevention。
- integer minor unit / Decimal and rounding。
- price history / promotion semantics。
- audit and reconciliation alerts。
- region / payment method / compliance input requiring user/business decision。

禁止浮点存钱、无幂等资金接口、只靠 webhook 作为最终事实。

## 8. Media / Storage / CDN

触发：文件、图片、音视频、对象存储、大 payload、转码、CDN。

检查：

- direct upload / signed URL。
- object key namespace / ownership / ACL。
- upload size / type / content validation。
- async processing / variants / retry。
- private content CDN token / signed URL / cache invalidation。
- deletion cascade：object / variants / CDN / index。
- storage / egress / processing cost shape。
- lifecycle for temp / orphan files。
- build vs managed media processing。

禁止大文件经 API server 中转，除非有明确理由。

## 9. Edge / Abuse / Security Defense

触发：公网 API、UGC、社区、支付、AI、匿名流量、公开链接、增长攻击面。

检查：

- application rate limiting key / window / burst / response。
- abuse / fraud signal and enforcement point。
- WAF / DDoS / bot boundary。
- public endpoint enumeration / scraping risk。
- content moderation mechanism：pre / post / queue / appeal。
- security event log。
- kill switch for dangerous public capability。

产品“什么内容允许”由 Product Definition；架构只定义机制、边界和可审计性。

## 10. Notifications

触发：Push、Email、SMS、站内信、OTP、营销 / 交易通知。

检查：

- central orchestration layer。
- user preferences / quiet hours / topic settings。
- dedupe / digest / frequency cap。
- APNs / FCM token lifecycle。
- at-least-once delivery and idempotency。
- deep-link compatibility。
- email SPF / DKIM / DMARC, bounce / complaint / unsubscribe。
- transactional vs marketing sender isolation。
- SMS purpose / regional provider。
- retry budget / provider outage / global send switch。

通知不是可靠状态同步通道。

## 11. Third-party Integrations

触发：任何外部 SaaS、partner API、webhook、OAuth、import/export、smart-home / device integration。

检查：

- provider boundary 与 credential ownership。
- OAuth / permission scopes。
- timeout / retry / rate limit / idempotency。
- webhook signature / duplicate / ordering / replay。
- provider object ID 与本地 ID mapping。
- sync direction and conflict semantics。
- data residency / deletion / export。
- sandbox / production environment。
- quota / cost / SLA / outage degradation。
- provider versioning / deprecation / exit path。

Smart Home 之类产品语义由 Product Definition，接入机制归本域。

## 12. Data Governance / Privacy

触发：消费者个人数据、位置、账户删除、导出、support access、telemetry、AI memory。

检查：

- data classification：public / internal / sensitive / confidential 或项目等价级别。
- retention 与 expiration action。
- account deletion cascade：primary / derived / vector / storage / provider / backup。
- legal retention exception。
- data export scope / portability / async job / rate limit。
- support access matrix / audit。
- telemetry collection 与 data classification 对账。
- location precision / storage / sharing / retention。
- data region / residency if relevant。

## 13. Platform Ops

触发：任何生产运行系统。

检查：

- configuration layers and validation。
- secrets store / rotation / access audit / env isolation。
- client secret prohibition。
- environment matrix。
- deployment model。
- CI/CD and release strategy。
- DB migration + deployment order。
- feature flags / gradual rollout。
- kill switch for high-risk features。
- Infrastructure as Code when scale/team justifies。
- drift detection。
- backup / restore drill / RPO / RTO。
- alert routing / incident severity / postmortem。
- status communication。

“有备份”但从未恢复演练，不等于可靠恢复能力。

## 14. Observability

触发：所有可运行系统；具体类型按实际风险。

检查：

- Diagnostic Logging
- Product / Business Events
- Error / Crash
- Metrics
- Tracing
- Audit / Security Events
- correlation
- runtime visibility
- sink readiness
- telemetry privacy
- alerts / incident diagnosis

细则见 `observability.md`。

## 15. Analytics / BI / Experimentation / Cost

触发：产品事件开始被分析、BI 查询、实验、成本归因。

检查：

- OLTP 与分析负载隔离。
- warehouse / lakehouse 的引入 trigger。
- event schema / metric definition SoT。
- ETL / CDC failure and replay。
- experiment bucket / exposure / metric 三件套。
- feature flag 与 experiment 的边界。
- cloud / AI cost attribution。
- report definition consistency。

不要让 BI 长查询直接拖垮 production primary DB。

## 16. Social / Feed / Ranking / Location

触发：follow / friend graph、feed、leaderboard、nearby / maps。

检查：

- relational adjacency vs graph engine based on query shape。
- fan-out-on-write / read / hybrid。
- feed materialization / rebuild。
- count exactness vs approximate。
- leaderboard realtime vs batch and anti-abuse。
- Redis 用例是否可重建、eviction、hot key。
- location query / spatial index / precision privacy。
- map provider cost and caching terms。

Redis 不得成为资金 / 订单 / 核心内容唯一真相。

## 17. Quality / Verification

触发：每个 Stage；Contract / Load 按风险触发。

检查：

- Task / Slice / Stage 三层是否分工。
- 是否重复测试同一事实。
- 哪些外部依赖必须真实 sandbox。
- 多独立消费方是否需要 contract testing。
- client compatibility window。
- migration rehearsal。
- load test 是否有量级和通过标准。
- test data isolation / redaction。
- CI 分层和 flaky handling。

细则见 `verification.md`。

## 18. Conventions

触发：全项目工程规范建立或重大跨模块契约出现。

检查：

- dependency policy / license / security / lockfile。
- time storage / timezone / occurred vs persisted semantics。
- ID generation / exposure / index characteristics。
- money / currency numeric rules。
- event naming / event versioning。
- API / schema / event 共用 breaking-change / deprecation discipline。

这些结论最终进入 `ENGINEERING_STANDARDS.md`，不另建规则对象编号。

## Coverage Inventory

以下能力必须能在主 skill 或上述条件域中找到归属；这是一张内部防丢对账表，不要求项目逐项填写：

- Architecture goal / system architecture / delivery surfaces
- iOS / Android / Web consumer / Admin control plane
- Backend language / backend architecture / HTTP
- Database access / API contract / API versioning
- Authentication / Authorization / Admin RBAC
- Primary DB / System of Record / Offline / Client Cache
- Realtime / Realtime Channel / AI Streaming
- AI Gateway / Model Routing / AI Memory / Search / Agent Architecture / Agent Permissions
- Background Jobs / Domain Events / Idempotency
- Economy / Inventory / Payments / Webhooks / Reconciliation
- Storage / Media Processing / CDN
- Edge / WAF / DDoS / Rate Limiting / Abuse / Anti-Fraud / Moderation mechanism
- User Blocking technical implications
- Notification Platform / Push / Email / SMS
- Product Analytics / Error Monitoring / Logs / Metrics / Tracing / Audit / Security Events
- AI Usage / Cost Accounting
- Feature Flags / Configuration / Secrets / Sensitive Credentials / Environments
- Database Migration / Zero-Downtime Schema
- Backup / Disaster Recovery
- Data Retention / Account Deletion / Data Export / Privacy Classification / Telemetry Privacy / Support Access / Location Privacy
- Social Graph / Feed / Ranking / Redis / Location / Maps
- Smart Home integration mechanism / Third-party Integrations
- Content / AI Safety mechanism / Prompt Management / AI Evaluation
- Testing / Contract Testing / Load Testing
- CI/CD / Deployment / Release Strategy / Infrastructure as Code
- Observability Alerts / Incident Response / Status / Kill Switch
- Business Intelligence / Data Warehouse Boundary / Product Experimentation / Cost Management
- Dependency Policy / Time / IDs / Money / Currency / Event Naming
- Final provider choices / explicit non-route decisions / Stage verification intent / product clarification / final architecture readiness

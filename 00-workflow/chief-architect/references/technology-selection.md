# Technology Selection

用于 Foundational Technology Decision、Build / Buy、外部服务与 Provider 选择。目标：对高迁移成本决定保持足够深度，对可逆小选择保持最小程序。

## 1. 决策等级

以下任一成立，按 **Foundational Decision**：

- 替换需要迁移核心数据。
- 会影响多个模块、公共契约或多客户端 / 多服务兼容。
- 存在明显平台 / Provider Lock-in。
- 会决定 Identity、Data Ownership、Domain Ownership、Semantic Authority、Deployment、Repository 或核心边界。
- 今天选错后很可能要求系统级重写。

否则按 **Reversible Decision**：记录结论、理由和替换边界即可。

判断依据是迁移 / 不可逆成本，不是“组件看起来重要”。

## 2. Foundational Decision 最低程序

### A. Decision Question

写清：要解决什么、Current Stage 必须支持什么、哪些长期产品方向会冲击选择、哪些事实变化会触发重开。

### B. Real Candidate Set

通常比较 2–4 个真正可行路线，覆盖真实取舍即可，例如 managed vs self-host、低当前成本 vs 高长期适配、强生态 vs 强控制、单 Provider vs abstraction / multi-provider。不要为凑数加入明显不合适候选。

### C. Current Evidence

结论依赖当前生态时，必须用研究工具核实并记录日期，重点包括：

- stable version、maintenance、EOL / deprecation
- 官方能力边界、quota / rate limit、SLA / reliability
- pricing / free tier / billing dimension
- region / data residency / compliance
- license / commercial-use constraints
- data export / migration / account closure
- API / SDK stability 与重大变更
- 官方规模限制或可信规模案例

不得把模型记忆写成当前事实。

### D. Current Fit

检查当前能力、团队运维能力、集成成本 / Appetite，以及当前安全、隐私、合规。

### E. Long-term Fit

直接引用 Product Definition / Product Atoms 的 Architecture-Shaping 依据，不创建 H-n。必须把产品方向与技术影响具体连接起来，例如：

- 多端 + offline write → sync protocol / client data architecture
- team collaboration → identity / ownership model
- realtime → connection / fanout / consistency model
- AI Agent → permission / budget / tool / audit boundary
- payment → idempotency / ledger / reconciliation

禁止只写“扩展性好”“以后够用”。

### F. Break Point

回答：**这套方案最先会在哪里坏掉？**

按项目实际看用户 / 并发、数据 / 写入、连接数、媒体量、请求峰值、任务积压、AI token / cost、查询复杂度、团队运维、Provider quota / region / compliance。无需伪造精确预测；数量级和触发条件足够。

### G. Migration / Exit

至少说明：替换影响哪些边界；数据能否导出以及格式；是否需要 dual-write / backfill / adapter / client migration；停机 / compatibility window；今天增加的长期适配成本是否值得换取未来更低迁移成本。

### H. Decision Record

高影响决定进入 `DECISIONS.md` 并编号 `Decision-n`。建议字段：

```text
Decision-n
Question:
Decision:
Why:
Current Fit:
Long-term Fit:
Alternatives:
Break Point:
Migration / Exit:
Security / Data / Compliance:
Cost Shape:
Research Evidence:
Revisit Trigger:
```

普通 Reversible Decision 直接落对应技术文档。

## 3. 技术栈选择

按“产品行为 + 长期形态 + 团队现实”选择，不按流行度。

### Client / Frontend

检查端形态、原生能力 / 性能要求、offline 等级与本地数据、多端共享、应用商店 / 旧版本兼容、团队维护能力与生态成熟度。

### Backend

检查并发与 I/O / CPU 形态、sync / async / realtime / streaming、核心生态和可观测性、部署形态、团队熟悉度、长期模块化 / 服务拆分路径。

### Primary Database

检查核心关系 / transaction / consistency、查询形态、读写扩展、schema migration、backup / restore / region / compliance。Cache / search / vector 若为 derived data，必须可从 System of Record 重建。

### Hosting / Compute

检查 runtime、long connection / jobs / GPU、部署复杂度、region / network、扩容、logs / metrics / alerts / backup 接入、Lock-in / Exit 与团队运维能力。

### API / Interface

检查 REST / RPC / GraphQL / events 与消费模式、多客户端 compatibility/versioning、contract SoT、idempotency、errors、pagination、serialization、是否需要 BFF / gateway。

## 4. Build / Buy / Managed / Self-host

对 Auth、Email、Storage、Search、Queue、Realtime、Payment、Analytics、Crash、AI、Media 等平台能力先决定模式，再选 Provider。

更倾向 **Buy / Managed**：非核心差异；行业能力成熟；自建带来持续 security / compliance / ops 责任；Provider 有清晰出口；成本曲线可接受。

更倾向 **Build / Self-host**：属于核心竞争力或语义高度特殊；Provider 会限制核心闭环；数据主权 / 合规无法接受托管；长期成本 / Lock-in 显著差于自建；团队具备长期运维能力。

“可以自己写”不是 Build 理由；“省开发时间”也不是 Buy 的唯一理由。

## 5. External Services

每个实际使用的重要 Provider 至少明确：

`Capability | Mode | Provider | Why | Data Impact | Security / Compliance | Cost Shape | Quotas / Limits | Failure / Degradation | Lock-in | Exit Path | Revisit Trigger`

### Auth / Identity

检查长期 user / organization model、business identity 与 provider ID 边界、session / MFA / passkey / SSO 路径、admin/support access、用户导出 / 迁移、Provider outage 路径。

### Payment

检查 region / currency / subscription / one-time / marketplace、webhook + active query、refund / dispute / reconciliation、PCI / compliance boundary、fee curve。

### Email / SMS / Push

检查 deliverability / sender reputation、法规与地域、bounce / unsubscribe / webhook、quota、Provider outage 与备用通道。

### Storage / Media / CDN

检查 object scale、egress cost、signed URL / access control、lifecycle / retention / deletion、media processing、data export。

### Analytics / Crash / Observability

检查 SDK / backend support、environment separation、sampling / retention、PII policy、query/export、事件量 / session / seat 成本曲线。

### AI Provider

检查 model capability / latency / context / streaming、API stability / model deprecation、data use / retention / region、token / media cost、fallback / multi-provider feasibility、output schema / safety / rate limit。

## 6. Provider / Integration Boundary

重要外部能力必须有清晰 boundary：credential ownership、timeout、retry、rate limit、idempotency、error normalization、failure / degradation、provider-specific code isolation；按风险决定 fallback / circuit / dual-provider。

不要让 Provider SDK / 专有模型名散落核心业务，也不要用“以后再迁”替代 Migration / Exit 论证。

## 7. 禁止模式

- Foundational Decision 只以“第一阶段快”为主要理由。
- 为普通 npm / Swift package 创建 `Decision-n`。
- 只比较营销页功能，不看 migration、cost、failure mode。
- 只看当前免费额度，不看自然增长后的计费维度。
- 外部服务没有 timeout / retry / idempotency / degradation 语义。

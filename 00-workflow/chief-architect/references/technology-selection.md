# Technology Selection

用于 Foundational Technology Decision、Build / Buy、外部服务和 Provider 选择。目标是保留技术判断深度，同时避免为每个小工具都写大型选型报告。

## 1. 先判断决策等级

以下任一成立，按 Foundational Decision：

- 替换需要迁移核心数据。
- 替换会影响多个模块或公共契约。
- 多客户端 / 多服务会被其长期绑定。
- 存在明显平台或 Provider Lock-in。
- 会决定 Identity、Data Ownership、Deployment、Repository 或核心边界。
- 今天选错后很可能系统级重写。

否则按 Reversible Decision：记录结论、理由、替换边界即可。

不要用“这个组件很重要”判断 Foundational；用**迁移与不可逆成本**判断。

## 2. Foundational Decision 最低程序

### A. 定义决策问题

写清：

- 需要解决什么问题。
- 当前必须支持什么。
- Product Definition 中哪些长期方向会冲击这个选择。
- 哪些事实一旦变化需要重开决策。

### B. 建立真实候选集

通常比较 2–4 个真正可行的路线即可，不为凑数量加入明显不合适候选。

候选应尽量覆盖不同取舍，例如：

- 托管 vs 自建
- 更低当前成本 vs 更高长期适配
- 更强生态 vs 更强控制权
- 单一 Provider vs 抽象层 / 双源能力

### C. 核实当前事实

当结论依赖当前生态时，必须用可用研究工具核实：

- 当前稳定版本、维护活跃度、EOL / deprecation 信号
- 官方能力边界和限制
- 定价、免费层、计费维度
- 区域 / 数据驻留 / 合规能力
- 配额、限流、SLA / 可靠性说明
- License 与商业使用限制
- 数据导出、迁移和关闭账户能力
- API / SDK 稳定性与重大变更史
- 已知规模案例或官方规模限制

记录核实日期。不要把模型记忆写成当前事实。

### D. Current Fit

检查：

- Current Stage 真正需要的能力是否原生支持。
- 团队是否能正确运行和维护。
- 集成成本是否与 Appetite 匹配。
- 当前安全、隐私和合规是否满足。

### E. Long-term Fit

直接引用 Product Definition 的相关章节 / Capability / Architecture-Shaping 说明，不创建 H-n。

写清“哪个产品特性”与“哪个技术特性”发生关系，例如：

- Future 多端 + 离线写 → 同步协议和数据层可否演进。
- Future 团队协作 → Identity / Ownership 是否能扩展到组织模型。
- Future Realtime → 当前数据库 / channel model 的写扩散和连接模型。
- Future AI Agent → 权限、预算、工具边界和审计。
- Future Payment → 幂等、账本、审计、对账。

禁止写“扩展性很好”“以后应该够用”这种不可检查句子。

### F. Break Point

回答：

> 这套方案最先会在哪里坏掉？

按产品实际选择维度：

- 用户 / 并发
- 数据量 / 写入量
- 连接数
- 文件 / 媒体量
- 请求峰值
- 任务积压
- AI token / cost
- 查询复杂度
- 团队运维复杂度
- Provider 配额 / 地域 / 合规

不要求伪造精确预测；数量级和触发条件足够。

### G. Migration / Exit

至少说明：

- 未来替换会改哪些边界。
- 数据能否导出、格式是什么。
- 是否需要双写 / backfill / adapter / client migration。
- 是否有停机或兼容窗口。
- 今天多付出的长期适配成本，与未来迁移成本哪个更合理。

### H. 决策

高影响决定写入 `DECISIONS.md`，编号 `Decision-n`。

建议字段：

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

普通 Reversible Decision 不创建 `Decision-n`，直接落到对应技术文档。

## 3. 技术栈选择

技术栈必须按“产品行为 + 长期形态 + 团队现实”选择，不按流行度选择。

### Client / Frontend

检查：

- 端形态：Web / iOS / Android / Desktop / SDK。
- 原生能力要求、性能和平台 API 深度。
- 离线等级与本地数据模型。
- 多端共享边界。
- 应用商店 / 旧版本兼容窗口。
- 团队维护能力和生态成熟度。

### Backend

检查：

- 业务并发与 I/O / CPU 形态。
- 同步 / 异步 / realtime / streaming 需求。
- 核心生态、库成熟度和可观测性。
- 部署形态和团队熟悉度。
- 长期模块化 / 服务拆分路径。

### Primary Database

检查：

- 核心关系、事务、一致性要求。
- 查询形态：关系、全文、地理、分析。
- 写入和读取扩展路径。
- Schema 迁移能力。
- 备份 / 恢复 / region / compliance。
- 派生存储：cache / search / vector 不得替代 System of Record。

### Hosting / Compute

检查：

- Runtime 形态与长连接 / jobs / GPU 等需求。
- 部署复杂度。
- 区域与网络。
- 可扩容方式。
- 日志、指标、告警、备份接入。
- Provider Lock-in 与 Exit。
- 团队实际运维能力。

### API / Interface

检查：

- REST / RPC / GraphQL / events 是否匹配消费方式。
- 多客户端兼容与版本策略。
- contract SoT。
- 幂等、错误、分页、序列化。
- 是否需要 BFF / gateway。

## 4. Build / Buy / Managed / Self-host

对 Auth、Email、Storage、Search、Queue、Realtime、Payment、Analytics、Crash、AI、Media 等平台能力先判断实现模式，再选 Provider。

### 更倾向 Buy / Managed

- 不是核心产品差异。
- 行业能力成熟。
- 自建会产生持续安全 / 合规 / 运维责任。
- Provider 有清晰数据出口和替换路径。
- 成本曲线可接受。

### 更倾向 Build / Self-host

- 是产品核心竞争力或语义高度特殊。
- Provider 能力会直接限制产品核心闭环。
- 数据主权 / 隐私 / 合规要求无法接受托管方案。
- 长期成本或锁定风险明显超过自建成本。
- 团队确实有长期运维能力。

“可以自己写”不是 Build 的理由；“省开发时间”也不是 Buy 的唯一理由。

## 5. External Services 最低判断

每个实际使用的重要 Provider 至少明确：

- Capability
- Mode：Build / Buy / Managed / Self-host
- Provider
- Why
- Data Impact
- Security / Compliance
- Cost Shape
- Quotas / Limits
- Failure / Degradation
- Lock-in
- Exit Path
- Revisit Trigger

### Auth / Identity

特别检查：

- 用户 / 组织模型是否匹配长期产品。
- 用户 ID 与业务数据所有权是否被 Provider 锁死。
- Session、MFA、Passkey、SSO 等未来路径。
- 管理员和 support access。
- 用户导出 / 迁移和 Provider 故障路径。

### Payment

特别检查：

- 地区、币种、订阅 / 一次性 / marketplace 能力。
- webhook 语义和主动查询能力。
- 退款 / dispute / reconciliation。
- PCI / 合规责任边界。
- 费率随规模变化。

### Email / SMS / Push

特别检查：

- deliverability、域名 / sender reputation。
- 地域与法规。
- webhook / bounce / unsubscribe。
- 发送量配额。
- Provider 故障和备用通道。

### Storage / Media / CDN

特别检查：

- 对象规模与出口带宽成本。
- signed URL / access control。
- lifecycle / retention / deletion。
- media processing / transcoding。
- 数据迁出能力。

### Analytics / Crash / Observability

特别检查：

- SDK / backend support。
- 环境区分。
- 数据采样 / retention。
- PII policy。
- 查询和导出。
- 费用随事件量 / session / seat 增长方式。

### AI Provider

特别检查：

- 模型能力、延迟、上下文、streaming。
- API 稳定性和 model deprecation。
- 数据使用 / retention / region。
- token / image / audio 成本曲线。
- fallback / multi-provider feasibility。
- 输出 schema、safety、rate limit。

## 6. 不要做

- Foundational Decision 只用“第一阶段快”作为主要理由。
- 为每个 npm / Swift package 创建 Decision-n。
- 只比较营销页功能，不看迁移、成本和 failure mode。
- 只看当前免费额度，不看产品自然增长后的计费维度。
- Provider SDK 和专有模型名散落业务核心代码而无边界。
- 外部服务无 timeout / retry / idempotency / fallback 语义。
- 用“以后再迁”代替 Migration / Exit 论证。

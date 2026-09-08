# Observability

用于项目级 Observability 基线、埋点 / 日志 / Crash / Metrics / Tracing / Audit 选型和 Stage 运行义务。

核心原则：**Observability 是运行能力，不是第四层测试；六类能力不能互相替代，但也不要求每个 Task 填六类矩阵。**

## 六类能力

### 1. Diagnostic / Structured Logging

回答：程序走到哪一步、状态是什么、哪里失败。

最低原则：

- 关键 start / state / success / failure 可诊断。
- 开发环境能在本地 Console / runtime log 中实时看到。
- error 带稳定 category / code / context / correlation。
- 不依赖远程 Analytics 才能 Debug。
- 敏感字段默认脱敏。

### 2. Product / Business Events

回答：用户或业务发生了什么。

最低原则：

- 只记录有产品 / 业务分析价值的事件，不把内部诊断全塞进 Analytics。
- event name、version、核心属性稳定。
- SDK / client 必须真实初始化并区分环境。
- 第一次建立或重大变化时，应能发送测试事件并在目标后台真实查询。

### 3. Error / Crash Tracking

回答：未捕获异常和 crash 为什么发生。

最低原则：

- 与 Product Event 分离。
- 能看到 stack、build / version、environment 和必要 breadcrumbs / correlation。
- 接收端真实初始化。
- 第一次建立或重大变更时有受控验证证据。

### 4. Metrics

当存在后端、队列、外部依赖、性能 / 容量 / SLA / 成本风险时使用。

典型：

- success / error rate
- latency / p95 / p99
- throughput
- retry / timeout
- queue depth / job age
- provider usage / AI token / cost
- resource saturation

不要因为“成熟系统都应该有”就为无后端的小工具先搭完整 metrics stack。

### 5. Tracing

当关键流程跨 API、Service、Queue / Job、Database、AI / External Provider 或复杂异步边界时使用。

最低原则：

- request / trace / correlation ID 在适用边界贯穿。
- 能定位关键 span 的 duration / status。
- 能从业务事件或错误回到技术链路。

### 6. Audit / Security Events

当涉及 Auth、Permission、Admin、Payment、Secret、敏感数据、高影响状态变更时使用。

最低原则：

- actor / action / target / time / result 清楚。
- 与普通 Product Analytics 分离。
- retention、访问权限、敏感信息处理明确。

## 项目级 Observability Baseline

`OBSERVABILITY.md` 只冻结项目实际使用和近期可信会使用的内容。

至少回答：

- 哪些类型适用，为什么。
- Critical Flows / State Transitions。
- Boundary Checkpoints。
- Failure Coverage。
- Correlation Model。
- Runtime Visibility：开发时从哪里实时看日志。
- Sink Readiness：远程接收端怎样初始化和验证。
- Privacy / Redaction。
- Alert / Recovery，仅在风险触发时。

未触发类型不要为了表格完整逐项写空内容。

## Telemetry Envelope

需要跨多个 sink 关联时，统一一小组公共字段；按语义填写，不要求每个事件都有全部字段。

常见：

```text
environment
occurred_at
event_name / event_version
actor_id / session_id
request_id / correlation_id / trace_id
entity_type / entity_id
outcome / error_code
duration_ms
```

不要为了“统一”制造几十个永远为空的字段。

## Privacy

默认禁止进入 telemetry：

- password
- token / secret / authorization header
- 原始支付敏感数据
- 未批准的用户私密内容
- 无分析 / 诊断必要性的 PII

Product Event、Logging、Crash、Tracing、Audit 都必须遵守数据分级和 retention 规则。

## Stage Contract 中怎么写

只写本 Stage 新触发 / 改变的运行义务，例如：

```text
Operational Obligations
- Payment callback：需要 Audit + structured failure logging；真实 sandbox 支付回调在 Slice 功能测验证。
- AI generation：记录 provider / model / latency / token / error；成本指标在 Stage 模块测确认可读。
```

不要复制六类总表。

不要要求每个 Task 都写：

```text
Logging: N/A
Events: N/A
Crash: N/A
Metrics: N/A
Tracing: N/A
Audit: N/A
```

Blueprint 只需把被触发的义务放进实际改变相关行为的 Task。

## Verification

以下不能单独证明某类 Observability 已完成：

- 编译通过
- 存在 logger / track / capture 调用
- 依赖已安装
- 环境变量留了配置口
- unit test mock 证明函数被调用

真实可见证据只在必要层执行：

- Logging → 真实路径在 Console / log sink 可见。
- Product Event → 测试事件真实到达后台。
- Crash → 受控 error / crash 可查询。
- Metrics → 指标真实产生并可读取。
- Tracing → 真实链路可串联。
- Audit → 真实敏感操作产生可检索审计记录。

不需要每个 Stage 反复重新验证已经稳定、且本 Stage 未改变的 sink 初始化。

## 埋点命名

事件命名属于 Engineering Standards。选择一个全项目稳定模式即可，例如：

`<domain>_<object>_<action>`

语义变化导致历史不可比较时升级 event version 或新事件，不悄悄改同名事件含义。

## 不要做

- 用 Product Event 代替 Crash。
- 用远程 Analytics 代替开发 Console Logging。
- 用 Logging 代替 Audit。
- 所有 Task 强制六类观测。
- 每个 Stage 重测所有 sink。
- 先把功能全部做完，再统一“补埋点”。
- 为内部技术步骤制造大量无业务价值的 Product Event。

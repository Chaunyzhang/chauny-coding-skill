# Observability

用于项目级 Observability Baseline 与 Stage 运行义务。核心原则：**Observability 是运行能力，不是第四层测试；六类能力不可互相替代，也不要求每个 Task 填六类矩阵。**

## 六类能力

### 1. Diagnostic / Structured Logging

回答“程序走到哪里、什么状态、为什么失败”。关键 start/state/success/failure 可诊断；开发环境有实时 Console/runtime log；error 带稳定 category/code/context/correlation；敏感字段默认脱敏；不能依赖远程 Analytics 才能 Debug。

### 2. Product / Business Events

回答“用户或业务发生了什么”。只记录有产品 / 业务分析价值的事件；event name/version/核心属性稳定；SDK/client 真实初始化并区分环境；首次建立或重大变化时，测试事件必须能在目标后台查询。

### 3. Error / Crash Tracking

回答“未捕获异常 / crash 为什么发生”。与 Product Event 分离；保留 stack、build/version、environment、必要 breadcrumb/correlation；接收端真实初始化；首次建立或重大变更有受控验证证据。

### 4. Metrics

后端、queue、外部依赖、performance/capacity/SLA/cost 风险触发。典型：success/error rate、latency、throughput、retry/timeout、queue depth/job age、provider/AI usage/cost、resource saturation。无真实需求时不先搭完整 metrics stack。

### 5. Tracing

跨 API/service/queue/job/database/AI/provider 或复杂 async 边界时使用。适用边界贯穿 request/trace/correlation ID；可定位关键 span duration/status；能从业务事件 / 错误回到技术链路。

### 6. Audit / Security Events

Auth、Permission、Admin、Payment、Secret、敏感数据、高影响状态变更触发。记录 actor/action/target/time/result；与普通 Product Analytics 分离；retention、访问权限、敏感信息处理明确。

## 项目级 Baseline

`OBSERVABILITY.md` 只冻结项目实际使用与近期可信会使用的内容：

- Applicable Types + why
- Critical Flows / State Transitions / Boundary Checkpoints
- Failure Coverage
- Correlation Model
- Runtime Visibility：开发时从哪里实时看
- Sink Readiness：远程接收端如何初始化和验证
- Event / Log Naming + 最小公共字段
- Privacy / Redaction
- Alert / Recovery（风险触发时）

未触发类型不为表格完整创建空内容。

## Telemetry Envelope

需要跨 sink 关联时只统一少量公共字段，按语义填写，不要求每个事件全有：

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

避免制造大量长期为空字段。

## Privacy

默认禁止进入 telemetry：password、token/secret/authorization header、原始支付敏感数据、未批准的用户私密内容、无分析 / 诊断必要的 PII。Logging、Events、Crash、Tracing、Audit 都遵守统一 data classification 与 retention。

## Stage Contract

只写本 Stage **新触发或改变**的运行义务，例如 payment callback 的 Audit + structured failure logging，或 AI generation 的 provider/model/latency/token/error。未触发项不填 N/A 矩阵；稳定且本 Stage 未改变的 sink 不重复验证。

Blueprint 把被触发义务放入实际相关 Task，不要求每个 Task 六类齐全。

## Verification Evidence

以下都不能单独证明 Observability 已完成：编译通过、存在 logger/track/capture 调用、依赖已安装、留了环境变量、unit mock 证明函数被调用。

必要层级必须有真实可见证据：

- Logging → 真实路径在 Console / log sink 可见。
- Product Event → 测试事件到达后台。
- Crash → 受控 error/crash 可查询。
- Metrics → 指标真实产生并可读取。
- Tracing → 真实链路可串联。
- Audit → 敏感操作产生可检索记录。

可与同一次 Slice / Stage 验证合并取证，不为 observability 再重复跑同一路径。

## 命名与禁止模式

事件命名模式由 Engineering Standards 唯一拥有，例如 `<domain>_<object>_<action>`；语义改变导致历史不可比较时升级 version 或新事件，不悄悄改变同名事件含义。

禁止：Product Event 代替 Crash；Analytics 代替开发 Console Logging；Logging 代替 Audit；所有 Task 强制六类；每 Stage 重测所有 sink；功能全做完再统一补观测；为内部技术步骤制造大量无业务价值 Product Event。

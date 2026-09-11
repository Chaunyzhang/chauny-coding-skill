# Operational Obligations

用于把架构 Stage Contract 中已经触发的运行义务落入施工。

核心原则：

> 运行义务随相关行为施工，但验证只在最合适层级做一次。


## Admission Gate

Operational Work 进入 Blueprint 必须来自：

- Stage Contract 已触发义务；
- Confirmed Defect；
- 或达到处理门槛的 evidence-backed risk。

不要因为“生产级通常应该有”自行增加：

- fallback
- retry
- alert
- metric
- trace
- backup
- feature flag
- extra recovery

模型自己想到的潜在风险先走 Planning Guardrails，不直接变成 Operational Task。

## 类型

可能包括：

- Diagnostic / Structured Logging
- Product / Business Events
- Error / Crash Tracking
- Metrics
- Tracing
- Audit / Security Events
- Backup / Recovery
- Alerting
- Feature Flag / Kill Switch

这些能力都重要，但不是每个 Stage、每个 Task 都全部适用。

## Blueprint 怎么消费

Stage Contract 例如：

```text
Operational Obligations
- Payment state changes: Audit + structured failure logging.
- Checkout conversion: Product Event.
```

Blueprint 直接映射：

```text
Task-3
Operational Work:
- 在 payment state transition 的现有 service 边界写 audit record。
- 在失败映射点输出 structured failure log。

Task-4
Operational Work:
- 在 checkout success 语义成立处发送已冻结 checkout_completed event。
```

不再给 Task-1 到 Task-20 每个都列六种 N/A。

## Diagnostic Logging

当本 Task 新增重要运行时行为、失败边界或难以从已有日志诊断的状态转换时，按项目标准补足。

不是每个 trivial getter / static mapping 都必须新增日志。

真实 Console 可见验证优先放：

- 首次建立 logging baseline。
- 关键新 runtime path。
- 本 Stage 改变 logging 初始化 / config。
- Stage Contract 明确要求。

普通 Task 可以用局部 test / inspection 验证落位，再由 Slice 真实路径取得运行证据。

## Product Events

只在有产品 / 商业分析语义时。

Blueprint 不创造 event 意义或命名；使用架构 / Engineering Standards 已冻结规则。

首次建立或重大改动：

- SDK / client 初始化。
- environment。
-真实事件到达目标 sink。

已有稳定 sink、本 Stage只新增一个事件时，可通过 Slice真实路径一次验证该事件，不重验所有旧事件。

## Error / Crash

不能用 Product Event 代替。

首次接入 / 配置改变 / 本 Stage 直接触达 crash pipeline 时需要真实受控证据。

普通业务 Task 不需要每次制造 crash。

## Metrics

触发：

- backend / queue / provider。
- latency / capacity / reliability / cost risk。
- Stage Contract 明确要求。

写清：

- metric
- recording boundary
- meaningful dimensions
- proof location

不要为所有函数制造 metric。

## Tracing

触发：

- cross-service / API / queue / job / provider / async。
- 单点 logging 无法定位链路。

只在必要边界建立 correlation / span。

## Audit / Security

触发：

- auth / permission
- admin
- payment
- secret
- sensitive data
- high-impact state change

必须保持 actor / action / target / result 等冻结语义。

## Backup / Recovery / Alert

只有 Stage 真正改变这些风险或依赖时才进入 Blueprint。

不要为了“生产级”在每个产品 Slice都加一套备份 / 告警 Task。

## 不允许 Stage 尾部补

如果一个业务行为本身要求 audit / event / diagnostic context，那么该工作与行为 Task 同步。

允许独立 operational Task 的情况：

- 首次建立共享 SDK / sink baseline。
- 多个后续 Task共同依赖的 telemetry foundation。
- Stage Contract 明确要求一次环境级 readiness。
- 修复一个直接阻塞 Current Stage 的历史 blind spot。

独立基础 Task 必须在最早消费它的 Slice 前完成。

## 真实证据

只在必要层：

- Logging → Console / log sink。
- Product Event → analytics backend。
- Crash → error / crash backend。
- Metrics → metrics query。
- Tracing → trace UI / query。
- Audit → authorized audit query。

“代码调用存在”只证明 instrumentation code，不能证明整个运行链路。

## 不重复

一次 Slice real path 可同时取得多种 evidence。

例如：

`Trigger checkout → visible success + product event + audit + trace`

不要拆成四次相同操作。

## Privacy

施工必须遵守上游：

- redaction
- PII policy
- secret policy
- retention
- environment separation

Blueprint 不重新发明 telemetry schema。

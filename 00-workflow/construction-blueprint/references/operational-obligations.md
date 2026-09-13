# Operational Obligations

把 Stage Contract 已触发的运行义务落到实际施工。核心原则：**运行义务随相关行为施工，验证只在最合适层级做一次。**

## Admission Gate

Operational Work 只能来自：
- Stage Contract 已触发义务；
- Confirmed Defect；
- threshold-passing evidence-backed risk。

不得因“生产级通常应该有”自行增加 fallback、retry、alert、metric、trace、backup、feature flag、extra recovery；潜在风险先走 Planning Guardrails。

可能义务：
- Diagnostic / Structured Logging
- Product / Business Events
- Error / Crash Tracking
- Metrics
- Tracing
- Audit / Security Events
- Backup / Recovery
- Alerting
- Feature Flag / Kill Switch

不是每个 Stage/Task 都适用，不写 N/A 矩阵。

## 落位

直接把义务映射到改变相关行为的 Task：
```text
Task-3 Operational Work:
- payment state transition 处写 audit record。
- failure mapping 处输出 structured failure log。
```

若义务与业务行为本身绑定，不允许功能做完后 Stage 尾部统一补。独立 operational Task 只在首次建立共享 sink/SDK baseline、多个后续 Task 共同依赖 telemetry foundation、Stage 要求环境级 readiness，或修复直接阻塞当前 Stage 的历史 blind spot 时成立，并应在最早 consumer 前完成。

## 类型触发

**Diagnostic Logging**：重要新 runtime behavior、failure boundary、难诊断 state transition；trivial getter/static mapping 不强制。首次 baseline、关键 runtime path 或 logging config 改变时可取真实 Console/sink evidence。

**Product Events**：仅有产品/商业分析语义时；命名与 schema 使用已冻结标准。首次/重大 SDK 变化验证 init/environment/真实 sink；稳定 sink 只验证本 Stage 新事件。

**Error / Crash**：不能用 Product Event 代替。首次接入、config 改变或直接触达 crash pipeline 时取受控真实证据；普通 Task 不反复制造 crash。

**Metrics**：backend/queue/provider、latency/capacity/reliability/cost risk 或 Stage 明确要求时，写清 metric、recording boundary、meaningful dimensions、proof location。

**Tracing**：cross-service/API/queue/job/provider/async 且单点日志不足时，在必要边界建 correlation/span。

**Audit / Security**：auth/permission/admin/payment/secret/sensitive data/high-impact state change；保持已冻结 actor/action/target/result 语义。

**Backup / Recovery / Alert**：只有 Stage 真正改变或依赖这些风险时才进入。

## Evidence

真实链路 evidence 只在必要层：
- Logging → Console/log sink
- Product Event → analytics backend
- Crash → error/crash backend
- Metrics → metrics query
- Tracing → trace UI/query
- Audit → authorized audit query

“代码调用存在”只证明 instrumentation code，不证明运行链路。一次 Slice real path 可以同时取得多种 evidence，例如 checkout 同时证明 visible success + event + audit + trace；不要重复 journey。

## Privacy

遵守上游 redaction、PII、secret、retention、environment separation。Blueprint 不重新发明 telemetry schema。

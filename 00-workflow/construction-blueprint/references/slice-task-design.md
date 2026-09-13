# Slice & Task Design

## Slice

Slice 是 Current Stage 内最小的**单能力跨层集成成果**：真实入口打通到真实结果，不是完整业务流程、技术层、sprint、milestone 或 test batch。

优先寻找：
`Entry / Caller → Behavior → State / External Boundary → Result`

用户型：
`UI / Client → API / Domain → Data / Provider → Visible Result`

技术型：
`Real Caller → Interface → Runtime / Data / Provider → Observable System Result`

技术型 Slice 只有在 Current Stage 已被 Architecture 允许为 technical-only，或该 Slice 紧邻即将消费它的用户型能力时成立。

第一个 Slice 应尽量验证当前最重要、可独立成立、最可能导致重写的真实能力边界。不要先批量建 DB/service/backend，最后再接 UI；也不要为了“完整用户旅程”把本可独立的能力硬串在一起。

合法 Slice 证明：
`Real Entry → 当前能力所需各层 → Real State / Side Effect → Visible / Observable Result`

A/B/C 可独立成立就拆 Slice；只有后一个能力是证明前一个成立不可缺少的真实依赖时才合并。底座 Stage 尤其按独立能力边界切。

### Slice 字段

```text
Slice-n — <结果型名称>
Upstream Basis
Outcome
Real Entry / Caller
Vertical Path
Real Dependencies
Tasks
Capability Test
Pass Condition
```

Outcome 写结果，不写动作。Capability Test 只证明该 Slice 的真实能力，不重复 Task unit cases。

## Task

Task 是 Construction Agent 的最小确定施工单元。合法 Task：
- 一个连贯 Goal。
- 明确 Prerequisite。
- 受控 write surface。
- 完成后仓库保持有效并为后续提供完整输入。
- 精确 Targets / Actions。
- 有最便宜且足够的 Local Proof。
- 清楚 Done When。

过大如“实现完整支付系统”；过小如“创建一个变量”。合适示例是“在既有 BillingService 中接入已批准 Provider 的 checkout session 创建，并映射冻结的 domain error”。

### Task 字段

```text
Task-n — <结果型名称>
Slice
Upstream Basis
Goal
Reasoning: Low (0–4) | Medium (5–10)
Criticality: Sensitive | Critical   # 仅适用时
Implementation Constraints          # 仅触及 owner/authority/boundary/reuse 时
Prerequisites
Targets
Actions
Operational Work                    # 仅触发时
Local Proof
Expected Result
Done When

# 仅 parallel-safe 时
Write Surface
Produces
Consumes
Parallel With
Commit Boundary
Merge Before / Integration Dependency

# 仅 Delegation Gate 通过时
Delegation ...
```

Upstream Basis 直接引用 Requirement、binding Atom、Stage Acceptance、Decision/Architecture section、Preservation/Direct Regression 或 Operational Obligation；不造新 ID。

### Implementation Constraints

只带 Stage `Implementation Shape` 对当前 Task 的最小子集：
```text
Owner:
Use / Reuse:
Allowed Dependency:
Do Not Bypass:
Mutation / Side-effect Boundary:
```
不触及边界就省略。若 owner/authority 尚未决定，回 Architecture，不能让 Construction 自选。

### Targets / Actions

Targets 尽量精确到 path + symbol/type/function/route/view/schema/migration/config/test selector/generated artifact。新文件可写计划路径，并说明来自 Project Structure。

Actions 描述明确状态变化，不写长伪代码，除非必须冻结接口签名。

### Operational Work

只有真正触发时写具体落点与冻结语义，不写泛泛“加 logging/metrics/tracing”。详见 `operational-obligations.md`。

### Local Proof

先问当前 Task 有什么事实需要证明。已有 invariant / static evidence 足够时可写：
`Existing evidence / static proof; no new executable check required.`

有 Live Uncertainty 时再选最便宜检查，如 targeted unit、target compile/typecheck/lint、migration/schema/generated check、local permission logic test。

Task 默认不得放：
- 全仓 suite、完整 E2E/真机 journey、deployment、所有 remote sink 检查、load test。
- `git push` / CI 等待；Task 只本地提交，push 属 Slice 收口，一次性触发一轮。
- iOS agent 侧编译、`xcodebuild test`、本地运行 Xcode。编译由 Human 在共享 DerivedData 上增量执行；单测代码可写但运行归 Stage 前/发版前脚本补测；真机操作不属于 Agent，Slice 收口给 Human 检查清单。
- 默认复用已有构建状态与缓存，能增量不全量；`clean build`、独立私有 build cache、真机运行、远程 CI、完整 test suite 只有明确 Trigger 才升级。

Done When 只证明当前 Task；真实能力由 Slice Test 证明。

## Reasoning / Criticality

Task 完成编译后由 Blueprint 按 `reasoning-policy.md` 评分；Construction 不重算。

Score >10，或仍需发明 Product behavior、Architecture route、owner/authority、module/dependency boundary、state machine、retry/recovery、ordering/concurrency 或 proof strategy，则 Task 无效。不得为了降分拆坏原子 correctness boundary。

Criticality 只表达后果严重性，不替代 Reasoning。

## Implementation Shape Gate

发布 Task 前检查：
- 是否复用现有 Semantic Authority / owning domain public path。
- 是否绕过 owner 直接 mutation。
- 是否把明确业务归属逻辑错误放进 Shared/Common/Utils。
- 是否无 Architecture 决策却新建长期 module/manager/service/authority。
- 是否明显超出 Expected Change Boundary 且无真实依赖。

只有能指出真实 ownership/authority/boundary 问题才阻塞；“改多个文件 / 出现 helper”本身不是错误。

## Defensive Work Gate

Task 含 guard/validation、fallback/retry、compatibility shim、feature flag、recovery、extra regression/observability 时，basis 必须是 Stage/Architecture obligation、Confirmed Defect 或 threshold-passing evidence-backed risk。“更保险/未来可能/理论上”无效。Confirmed Defect 的 Goal 写根因修复，不写症状遮盖。

## Execution Graph

顺序只由真实依赖决定。parallel-safe 的详细判定、write surface、commit 与 Human recommendation 只由 `parallel-construction.md` 定义。

## UI / Generated / Migration

Stage Outcome 需要 UI 时，不默认最后接；loading/empty/error/permission/retry 等已定义状态随对应 Slice 接入。凡引入或改变用户可见 error/failure state 的 Task，必须引用 Engineering Standards 登记的错误码，并在各 client 的「错误码 → 文案」映射中落条目；禁止业务代码内联文案。Blueprint 只引用既有文案机制，不重定义。视觉 polishing 只在 Acceptance 明确要求时阻塞。

Generated artifact 必须明确 source-of-truth；改 source 后安排 generation/consistency check，禁止把直接改生成物当唯一路径。

Migration 要明确 migration 与读写路径顺序、必要 compatibility window；destructive migration 不由 Blueprint 自创；重大演练按 Verification trigger 安排，不塞进每个 Task。

## Task 不应承载

上游 rationale、产品讨论、架构方案比较、Observability 空表、全 Stage Acceptance、历史废弃计划。

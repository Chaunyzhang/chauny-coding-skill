# Slice & Task Design

## Slice 的目的

Slice 是 Current Stage 内最小的纵向集成成果。

它不是：

- 技术层。
- sprint。
- milestone。
- test batch。

一个合法 Slice 结束时，真实系统应该多出一个已经连接的能力状态。

## Slice 划分

优先寻找最早真实路径：

`Entry / Caller → Behavior → State / External Boundary → Result`

用户型产品优先：

`UI / Client → API / Domain → Data / Provider → Visible Result`

技术型能力可以：

`Real Caller → Interface → Runtime / Data / Provider → Observable System Result`

## 第一个 Slice

尽量验证：

- 最关键产品闭环片段。
- 最大技术风险。
- 最可能造成重写的真实边界。

不要先批量建：

- 所有 DB table。
- 所有 service。
- 所有 backend endpoint。
- 最后再接 UI。

## Slice 字段

最小：

```text
Slice-n / Name
Upstream Basis
Outcome
Real Entry / Caller
Vertical Path
Real Dependencies
Tasks
Capability Test
Pass Condition
```

### Outcome

结果型，而不是动作型。

好：
- “用户从现有入口创建项目并能重新打开看到持久化结果。”

差：
- “完成 Project API 和 View。”

### Capability Test

只证明这一 Slice 的真实能力。

用户型示例：

```text
Entry: Projects screen
Steps:
1. Create project
2. Enter name
3. Save
4. Relaunch / reload
Expected:
- 项目可见
- state 持久化
- Stage Contract 要求的失败路径正确
Real boundary:
- 真 API + test DB
```

不要在这里重复 Task unit tests。

## Task 的目的

Task 是施工 Agent 的最小确定动作单元。

合法 Task 应：

- 只做一个连贯目标。
- 有明确 prerequisite。
- 有受控 write surface。
- 完成后仓库保持有效。
- 能用便宜方法直接验证。
- 为后续 Task 提供完整输入。

## Task 粒度

太大：

> 实现完整支付系统。

太小：

> 创建一个变量。

合适：

> 在现有 BillingService 中接入已批准 Provider 的 checkout session 创建，并映射冻结的 domain error。

## Task 字段

```text
Task-n — <结果型名称>
Slice
Upstream Basis
Goal
Prerequisites
Targets
Actions
Operational Work (适用时)
Simple Test
Expected Result
Done When

# 仅并行有价值时追加
Write Surface
Produces
Consumes
Parallel With
Commit Boundary
Merge Before / Integration Dependency
```

### Upstream Basis

可以引用：

- Requirement-n
- Stage Acceptance
- Decision-n
- Architecture section
- Preservation / Direct Regression
- Operational Obligation

不要创建新 ID。

### Targets

尽量精确：

- `src/billing/BillingService.ts` → `createCheckoutSession`
- `db/migrations/...`
- `SettingsView`
- `POST /v1/...`
- `BillingServiceTests/test...`

如果新文件不存在，可以写计划路径并说明来自 PROJECT_STRUCTURE。

### Actions

动作应是明确状态变化：

1. 在 X symbol 增加 Y branch。
2. 将 provider error 映射到冻结的 domain error。
3. 在 Z caller 使用新接口。
4. 增加 targeted test。

不要写代码实现的大段伪代码，除非接口签名必须精确冻结。

### Operational Work

只在实际触发时出现：

> 按 Stage Contract 的 payment audit obligation，在成功 / 失败状态转换处写 audit record；使用已冻结 actor / target / result 字段。

不要：

> 加 logging、metrics、tracing。

### Simple Test

优先目标 ≤10–30 秒的局部检查；复杂项目可能更长，但不能默认扩大。

适合：

- targeted unit test
- compiler / typecheck for target
- lint for target
- migration syntax / schema check
- generated client compile
- local permission logic test

不适合默认放 Task：

- 全仓 test suite
- 真机完整 journey
- deployment
- 所有 remote sink 检查
- load test
- `git push` / CI 确认（Task 只本地提交；push 属 Slice 收口，一次性推一轮）
- iOS agent 侧编译、`xcodebuild test`、本地运行 Xcode（编译归人类共享 DerivedData 增量执行；单测写而不跑，运行归 Stage 前 / 发版前脚本补测）

### Done When

只写当前 Task 成立条件。

真实能力由 Slice Test 证明。

## Execution Graph

只有真实依赖决定顺序：

```text
Task-1 -> Task-2
Task-1 -> Task-3 [parallel]
Task-2, Task-3 -> Task-4
```

标 parallel 前检查：

- prerequisite 是否已独立满足
- write surface 是否低冲突
- schema / migration 是否无顺序竞争
- shared state 是否互不干扰
- generated source-of-truth 是否无竞争
- interface 是否在 fan-out 前冻结
- test environment 是否可独立使用
- Task 是否可独立 commit
- fan-in 后是否只需一次 Slice Capability Test

详细多人协作规则见 `parallel-construction.md`。

## UI

Stage Outcome 需要 UI 时：

- UI 不得默认最后做。
- loading / empty / error / permission / retry 等已定义行为跟对应 Slice 一起接入。
- 视觉 polishing 不应阻断真实能力路径，除非 Stage Acceptance 明确要求。

## Generated Artifacts

明确 Source of Truth：

- schema
- generated client
- codegen
- localization
- assets

Task 修改 source 后必须安排 generation / consistency check。

禁止直接改生成物作为唯一改动路径。

## Migration

需要 migration 时：

- migration 与读写路径顺序清楚。
- 必要兼容窗口遵循架构标准。
- destructive migration 不得由 Blueprint 自创。
- 大迁移的真实演练在 Verification 策略触发时安排，不塞进每个 Task。

## Task 不应承载

- 上游 rationale。
- 产品讨论过程。
- 架构方案比较。
- 六类 Observability 空表。
- 全 Stage Acceptance。
- 历史废弃计划。

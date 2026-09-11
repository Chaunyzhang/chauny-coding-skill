# Slice & Task Design

## Slice 的目的

Slice 是 Current Stage 内最小的**单能力跨层集成成果**。

这里的纵向指一个能力从真实入口打通到真实结果，不指完整业务流程。

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

- Current Stage 中最重要、可独立成立的能力。
- 最大技术风险。
- 最可能造成重写的真实边界。

不要为了形成完整用户旅程，把多个本可独立成立的能力硬串进第一个 Slice。

不要先批量建：

- 所有 DB table。
- 所有 service。
- 所有 backend endpoint。
- 最后再接 UI。


## Capability Closure，不是 Business Journey

合法 Slice 要证明的是：

`Real Entry → 当前能力所需各层 → Real State / Side Effect → Visible / Observable Result`

如果 A、B、C 三个能力分别能独立成立，应拆成三个 Slice；产品层以后可以把它们组合成循环。

只有 B 是证明 A 成立不可缺少的真实依赖时，才把 A+B 放进同一 Slice。

底座 Stage 尤其优先独立能力边界，而不是完整业务剧情。

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
- 有明确 `Local Proof`；只有存在需要执行才能消除的 Live Uncertainty 时才安排测试。
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
Reasoning: Low (0–4) | Medium (5–10)
Criticality: Sensitive | Critical   # 仅适用时
Implementation Constraints          # 仅触及 ownership / authority / boundary / required reuse 时
Prerequisites
Targets
Actions
Operational Work (适用时)
Local Proof
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
- binding Atom-n
- Stage Acceptance
- Decision-n
- Architecture section
- Preservation / Direct Regression
- Operational Obligation

不要创建新 ID。

### Implementation Constraints

不是每个 Task 都需要。

只有当前 Task 触及跨模块 owner / authority / boundary / required reuse 时，写 Stage `Implementation Shape` 的最小相关子集：

```text
Owner:
Use / Reuse:
Allowed Dependency:
Do Not Bypass:
Mutation / Side-effect Boundary:
```

不要把 Architecture 长篇复制到每个 Task。

如果无法填写是因为 owner / authority 尚未决定，不是让 Construction 自己选择，而是回 Architecture。

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

### Local Proof

先说明当前 Task 有什么需要证明。

如果已有 invariant / static evidence 足够，可以写：

`Existing evidence / static proof; no new executable check required.`

只有执行结果能改变当前判断时才安排局部检查。执行性检查仍应优先低成本；复杂项目不能默认扩大。

需要执行时可选：

- targeted unit test
- compiler / typecheck for target
- lint for target
- migration syntax / schema check
- generated client compile
- local permission logic test

不得默认放 Task：

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

## Reasoning

Task 编译完成后，由 Blueprint 计算一次 Reasoning Score。

Construction 不负责重新评分。

### Low

答案基本已被冻结，施工是机械翻译。

### Medium

允许有限局部实现判断，但 Product / Architecture / contract / state / failure semantics 已冻结。

### Invalid

Score >10，或仍需施工 Agent 发明：

- Product behavior
- Architecture route
- interface / ownership / semantic authority
- module / dependency boundary
- state machine
- retry / recovery semantics
- ordering / concurrency guarantee
- proof strategy

则 Blueprint 继续设计，不得交给 Construction。

不要为了降分拆坏原子正确性边界。

详细见 `reasoning-policy.md`。

## Implementation Shape Gate

Task 编译完成后检查：

- 是否复用现有 Semantic Authority。
- 是否通过 owning domain 的 public path 合作。
- 是否绕过 owner 直接 mutation state。
- 是否把有明确业务归属的逻辑错误放入 Shared / Common / Utils。
- 是否在没有 Architecture 决策时新建长期 module / manager / service / authority。
- 是否明显超出 Stage Expected Change Boundary，却没有真实依赖依据。

确认存在上述架构偏差时，Task 不得发布。

仅“改了多个文件”或“出现新 helper”不是自动错误；必须能指出真实 ownership / authority / boundary 问题。

## Defensive Work Gate

Task 如果包含以下任一内容：

- guard / validation
- fallback / retry
- compatibility shim
- feature flag
- recovery branch
- extra regression / observability

Upstream Basis 必须能指向：

- Stage / Architecture obligation；
- Confirmed Defect；
- 或达到处理门槛的 evidence-backed risk。

“更保险”“未来可能”“理论上”不能作为 Task Basis。

Confirmed Defect 的 Task Goal 应描述根因修复，而不是“避免症状出现”。

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

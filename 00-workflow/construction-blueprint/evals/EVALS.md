# EVALS

这些案例用于检查施工蓝图是否保持边界、命名克制、真实集成和低重复验证。

## Eval 1 — 不重新引入 Capability Card

输入：Stage-2 包含 Requirement-3，但没有 Capability-n 文件。

合格：
- 直接消费 Stage Contract + Product Definition。
- 缺失产品语义只有在影响 scope / state / permission / failure / acceptance 时才 BLOCKED。
- 不要求创建 Capability Card。

不合格：
- “请先创建 Capability-3 才能规划。”

## Eval 2 — 命名收敛

合格对象：
- Stage-2
- Requirement-3
- Decision-1
- Slice-1
- Task-1

不合格：
- R-7、H-2、ES-19、AC-04、EVID-9、OBS-PROD-3 等二次编号。

## Eval 3 — Task 不做全链路测试

输入：Task-2 只增加一个纯 mapping 分支。

合格：
- targeted unit test / compile。

不合格：
- Task-2 要求全仓 test、真机 journey、analytics sink、crash test、Stage acceptance 全跑。

## Eval 4 — Slice 做真实能力测

输入：支付 Slice 依赖真实 sandbox webhook。

合格：
- Task 局部测试 provider adapter。
- Slice Capability Test 真实 sandbox checkout + webhook + state update。

不合格：
- 只用 mock provider 宣布支付能力成立。

## Eval 5 — 不重复

同一个创建项目路径：

合格：
- Task 测 local validation。
- Slice 测真实创建与持久化。
- Stage 只在该行为是 Stage Outcome / direct regression 时验证高层结果，不重复所有 field cases。

不合格：
- 三层运行同一 18 个用例。

## Eval 6 — Observability 重要但不填空表

Stage 只触发：
- payment audit
- structured failure logging

合格：
- 只把这两个义务落到相关 Task。
- 真实支付 Slice 同时取得功能、audit、logging evidence。

不合格：
- 每个 Task 都列 Logging / Events / Crash / Metrics / Trace / Audit 六行，并写大量 N/A。

## Eval 7 — 已稳定 sink 不重测

已有稳定 analytics SDK，本 Stage 只新增一个 event。

合格：
- Task 实现 event。
- Slice 真实路径确认新 event 到达。
- 不重新验证 SDK 全套初始化。

不合格：
- 每个 Task 重新检查 API key、SDK init、网络、所有旧 events。

## Eval 8 — 产品缺口上抛

需求：“删除账户”。

Repository 已支持 delete endpoint，但产品未定义数据是立即删除、延迟删除还是可恢复。

合格：
`BLOCKED / Owner: Product`

不合格：
- Blueprint 按行业惯例选择 soft delete。

## Eval 9 — 局部 UI 细节不阻塞

产品已定义“失败后显示可恢复错误并允许重试”，仓库已有统一 ErrorBanner。

合格：
- Blueprint 沿用 ErrorBanner 并安排 wiring。
- 不回产品问 banner 在顶部还是底部。

## Eval 10 — 架构缺口上抛

Stage 要上传文件，但 Architecture 没有 object storage / ownership / signed access 方向。

合格：
`BLOCKED / Owner: Architecture`

不合格：
- Blueprint 自选 S3 / Supabase Storage。

## Eval 11 — 不做顺手重构

Current Stage 只改 checkout。

发现旁边 UserService 命名不好但不阻塞。

合格：
- 不纳入 Scope。

不合格：
- 顺手重构整个 service layer。

## Eval 12 — UI 早接

用户型 Stage 的真实 Outcome 需要 UI。

合格：
- 第一或很早的 Slice 形成 UI → backend → data 的薄真实链路。

不合格：
- 15 个 backend Task 完成后最后一个 Task 才首次接 UI。

## Eval 13 — Technical-only

Stage Contract 明确是 migration foundation，且下一 Stage 消费。

合格：
- Slice 用真实 migration / caller / data invariant 作为能力验证。

不合格：
- 强行造假 UI 只为了“看起来纵向”。

## Eval 14 — Direct Regression 克制

共享 session module 改动会直接影响 login。

合格：
- Stage regression 包含 login。

不合格：
- 因为 session 很重要而跑整个产品所有 journey。

## Eval 15 — 合同唯一

合格：
- 只更新 `docs/blueprint/EXECUTION_CONTRACT.md`。

不合格：
- 创建 `EXECUTION_CONTRACT_OBSERVABILITY.md`
- 创建 `STAGE2_SUPPLEMENT.md`
- 创建 `TASK_FIXES.md`

## Eval 16 — READY 门禁

如果一个 Task 的 Target 仍写“相关 service 文件”，不确定具体路径：

合格：
- 继续 Repository Intake，不能 READY。

如果需要新的 Product / Architecture Decision：

合格：
- BLOCKED，列 Owner / Gap / Evidence / Blocks / Required Resolution。

## Product Detail Routing

### Case: 分享语义缺失
Stage 已包含共享 Requirement，但未说明“同一对象访问”还是“复制副本”。

正确：
回 `product-detail`，因为答案改变 ownership / lifecycle / revocation。

错误：
Blueprint 自己选择数据库上最方便的方式。

### Case: 按钮布局
Stage 行为已明确，只是不知道分享按钮放 toolbar 还是 overflow menu。

正确：
Blueprint / UI 按既有设计系统解决，不回 Product Detail。

### Case: Product Detail 改变原需求
细化过程中从“永久删除”改成“只归档”。

正确：
回 Product Designer 更新 Product Definition，再由 Chief Architect 重新冻结 Stage。


## Parallel Construction

### Safe fan-out

Task-1 freezes a stable shared interface. Task-2 implements backend adapter, Task-3 implements UI caller, Task-4 adds independent fixture/test support. Primary write surfaces are separate and each Task can form a valid local commit.

Expected:
- Task-2 / Task-3 / Task-4 are `parallel-safe`.
- Execution Graph fans out after Task-1.
- Human is told they may open 3 windows.
- Each Task only runs its Simple Test.
- fan-in runs one Slice Capability Test.

### Shared schema conflict

Two Tasks both redesign the same schema / migration chain.

Expected:
Keep sequential, or first create one prerequisite Task that freezes the shared schema boundary.

### Not worth parallelizing

Three tiny Tasks touch nearby code and coordination cost exceeds likely savings.

Expected:
`Parallel Work Recommendation: Stay sequential`.

### Step naming

Agent proposes `Step-7` as a tracked construction unit.

Expected:
Reject it. Use `Task-7`, or plain numbered actions inside Task-7.

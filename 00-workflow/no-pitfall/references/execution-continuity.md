# Execution Continuity

本文件是持续执行机制的唯一详细 owner，解决“局部完成被误判成整个施工结束”。

核心模型：

`Active User Directive + Autonomy Mode + Execution Horizon + Standing Authorization + Ready Work + Autonomous Continuation Judgment + Global Blocker`

## Active User Directive

每次开始 / 恢复先恢复：

```text
Authorized Objective:
Autonomy Mode: NORMAL | FULL
Stop / Pause Boundary:
```

用户命令决定目标与自动化力度；Execution Horizon 只帮助解释目标，不能覆盖明确命令。

### FULL AUTO

目标未完成时默认寻找合法推进路径。可以选择下一 Ready Work、在 Local Blocker 时切换分支、做已冻结边界内的低成本机械实现选择，并调用 Product / Architect / Blueprint / Stage Verifier / Repair Planning 等已有能力。直接施工受阻但这些能力可在现有授权内解除时，自动路由，不重复征求同一授权。

只有 Human 主观决定、Agent 无法执行的外部动作、真正 Global Blocker、无法调用所需上游能力，或用户明确停止，才合法 PAUSE / STOP。

## Execution Horizon

- `TASK`：只完成明确 Task。
- `SLICE`：完成 Current Slice + Slice Gate。
- `STAGE`：完成 Current Stage + Stage Gate。
- `CONTINUOUS`：连续推进所有已冻结、合法、可执行的工作；下一 Stage 已冻结且 Blueprint READY 时继续，需要可调用上游能力时路由继续。

Horizon 不授权未冻结 Scope，也不得把用户更高层目标保守缩成 `TASK`。

## Standing Authorization

“继续执行 / 一直做下去 / 不要每个 Task 停 / 把 Stage 做完 / 按蓝图全部继续 / 除非真正阻塞”等表达通常形成 Standing Authorization，其生命周期由 Authorized Objective / Horizon 决定。

Task、Slice、Stage、commit、CI、局部修复或 checkpoint 完成不会自动消费仍有效的上层授权。

## Execution Loop

```text
Resolve Directive / Horizon
→ Compute Ready Work
→ Execute one Task
→ Local Proof / Exit
→ Recompute Ready Work
→ Continue
```

Task blocked 时：记录 Local Blocker → 重算 Ready Work；有其他合法 Ready Work 就继续。只有当前 Horizon 内无任何合法 Ready Work，且剩余工作都依赖 blocker 或必须外部 Authority 解除，才是 Global Blocker。

## Ready Work

Ready Work 必须同时满足：

- 属于当前 Authorized Objective / Horizon。
- 已有冻结 Stage / Blueprint 授权（若该模式要求）。
- prerequisites 满足。
- 没有未决 Product / Architecture choice。
- Repository Reality 允许施工。

选择时优先当前 Slice 的 Ready Task，其次 Slice Gate、后续已解锁 Slice、Stage Gate、Horizon 允许的下一已冻结 Stage；没有直接 Ready Work 时再检查可授权路由或当前 authority 内 replan。

## Autonomous Continuation Judgment

每个 checkpoint（Task Exit、Slice/Stage Gate、repair/commit/CI complete、Local Blocker）按顺序判断：

```text
Authorized Objective complete?
├─ YES → STOP
└─ NO
   ↓
Valid autonomous progress exists?
├─ YES → CONTINUE
└─ NO
   ↓
Authorized Skill / planning layer can resolve?
├─ YES → ROUTE + CONTINUE
└─ NO
   ↓
Human / External Authority required?
├─ YES → PAUSE
└─ NO → REPLAN within current authority, then continue
```

FULL AUTO 下存在 `CONTINUE` 或 `ROUTE + CONTINUE` 时，不得选择 `PAUSE / STOP`。

## 合法 STOP / PAUSE

`STOP` 只有：Authorized Objective 真正完成；或用户明确 STOP / 改变命令。

`PAUSE` 只有：Global Blocker 且无其他路径；必须 Human / External Authority 做不可代理动作；必须用户做产品/商业/审美等主观裁决；或继续需要上游能力但当前 Agent / orchestrator 确实无法调用。

FULL AUTO 的 PAUSE 应说明：

```text
Authorized Objective still incomplete because:
Why no autonomous path remains:
Required external / human action:
Resume condition:
```

## Checkpoint

长任务可汇报：

```text
Active Directive:
Authorized Objective:
Autonomy Mode:
Completed:
Current:
Blocked:
Next Ready:
Horizon:
```

Checkpoint 默认下一动作是继续，不应以“如需继续请告诉我”消费 Standing Authorization。

# Execution Continuity

## 目的

解决：

> Agent 每完成一个 Task 就把局部完成误判成整个施工结束。

核心模型：

`Active User Directive + Autonomy Mode + Execution Horizon + Standing Authorization + Ready Work + Autonomous Continuation Judgment + Global Blocker`

## Active User Directive

每次开始 / 恢复时先恢复：

```text
Authorized Objective:
Autonomy Mode: NORMAL | FULL
Stop / Pause Boundary:
```

用户命令决定目标与自动化力度。

Execution Horizon 只是帮助理解目标，不得覆盖用户明确命令。

### FULL

FULL AUTO 下：

- 目标未完成时默认继续寻找合法推进路径。
- 停止必须对应合法 Stop / Pause Reason。
- 如果当前施工路径走不通，但 Product / Architect / Blueprint / Repair Planning 能在现有授权内解除，自动路由，不重复征求同一份授权。
- 只有人类主观决定、外部不可访问动作、真正全局 blocker、或用户明确停止时暂停 / 停止。

## Execution Horizon

### TASK

只授权当前 Task。

### SLICE

授权到 Current Slice 完成并通过 Slice Gate。

### STAGE

授权到 Current Stage 完成并通过 Stage Gate。

### CONTINUOUS

授权连续推进所有已经冻结、合法、可执行的工作。

Stage 完成后：

- 下一 Stage 已冻结且 Blueprint READY → 继续。
- 下一步需要 Architect / Blueprint 重新冻结，而且当前 orchestrator 有能力调用它们 → 路由并继续，不重复问用户。
- 需要用户产品决定 / 人工设备 / 外部权限 → Global Blocker，暂停。

## Standing Authorization

以下表达通常形成 Standing Authorization：

- 继续执行。
- 一直做下去。
- 不要每个 Task 停。
- 把当前 Stage 做完。
- 按蓝图全部继续。
- 把现有计划做完，除非真正阻塞。

Standing Authorization 的生命周期由 Horizon 决定。

单个 Task 完成不会消费 Stage / Continuous 授权。

## Execution Loop

```text
Resolve Horizon
→ Compute Ready Work
→ Execute one Task
→ Local Proof
→ Local Exit
→ Recompute Ready Work
→ Continue
```

如果 Task blocked：

```text
Mark Local Blocker
→ Recompute Ready Work
→ Other Ready Work?
   YES → Continue
   NO  → Is all remaining work blocked?
         YES → Global Blocker → Pause
```

## Ready Work

Ready Work 必须：

- 属于当前 Horizon。
- 已有冻结的 Stage / Blueprint 授权。
- prerequisites 满足。
- 没有未决 Product / Architecture choice。
- 当前仓库状态允许施工。

## Autonomous Continuation Judgment

每个 checkpoint 依次判断：

1. Authorized Objective 是否完成？
2. 若未完成，是否有 Ready Work？
3. 若没有 Ready Work，是否有已授权 Skill / planning layer 可以解除？
4. 若仍没有，是否必须 Human / External Authority 介入？
5. 若都不是，重新规划当前 authority 内的合法路径。

结果只有：

- `CONTINUE`
- `ROUTE + CONTINUE`
- `PAUSE`
- `STOP`

FULL AUTO 下如果存在 `CONTINUE` 或 `ROUTE + CONTINUE`，不得选择 `PAUSE / STOP`。

## 合法 STOP / PAUSE

### STOP

只有：

1. Authorized Objective 真正完成。
2. 用户明确 STOP / 改变命令。

### PAUSE

只有：

1. Global Blocker 且没有其他合法推进路径。
2. 必须由 Human / External Authority 完成 Agent 无法执行的动作。
3. 必须由用户做产品 / 商业 / 审美等主观裁决。
4. 继续需要上游决策，但当前 Agent / orchestrator 确实无法调用相应能力。

Task / Slice / Stage / commit / CI 完成本身都不是 STOP 条件。

FULL AUTO 下，每次 PAUSE 都必须说明：

```text
Authorized Objective still incomplete because:
Why no autonomous path remains:
Required external / human action:
Resume condition:
```

## Checkpoint

长任务可汇报 checkpoint，但 checkpoint 的默认下一动作是继续：

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

不要把进度汇报写成“我已经完成 X，如需继续请告诉我”。

Standing Authorization 存在时，应直接继续。

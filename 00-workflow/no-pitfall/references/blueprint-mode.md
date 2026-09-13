# Blueprint Mode

当存在有效 Execution Contract 时，本 Skill 与 Construction Blueprint 配套使用。

## Authority

`Stage-n Contract → Execution Contract → Repository Reality`

Product Definition 与 Architecture 仍是更高层语义权威，但施工 Agent 不应绕过 Execution Contract 自行重新规划。

## Active Directive

进入 Blueprint Mode 时先恢复：

```text
Authorized Objective:
Autonomy Mode:
Standing Authorization:
```

用户命令是运行时持续授权；Task / Slice / Stage Gate 只是 checkpoint。

## Execution Horizon

根据 Active Directive 解释：

`TASK | SLICE | STAGE | CONTINUOUS`

用户明确要求“继续执行 / 不要每个 Task 停 / 把当前 Stage 或现有计划做完”时，形成 Standing Authorization。

Standing Authorization 在 Horizon 完成前持续有效。

## Continue / Route / Pause / Stop

每次局部完成后：

- Objective 未完成 + 有 Ready Work → `CONTINUE`
- Objective 未完成 + 无 Ready Work，但可由 Product / Architect / Blueprint / Repair 等授权能力解除 → `ROUTE + CONTINUE`
- Objective 未完成 + 必须人类 / 外部动作 → `PAUSE`
- Objective 已完成 / 用户 STOP → `STOP`

FULL AUTO 时，`CONTINUE` 与 `ROUTE + CONTINUE` 优先于 `PAUSE`。

## Task Loop

每个 Task：

1. 读取 Task 与前置条件。
2. 检查真实仓库。
3. 只做 Task 授权变化。
4. 只有存在当前 Live Uncertainty 时，执行最低成本的局部验证。
5. 保存真实证据。
6. 满足 Task Exit 后先更新依赖图与 Ready Work；Standing Authorization 仍有效时，自动进入下一 Ready Task，不返回用户等待新授权。

## Local vs Global Blocker

当前 Task 阻塞时：

- 有其他 Ready Work → 当前 blocker 只是 Local Blocker，继续别的 Ready Work。
- 当前 Horizon 内无任何 Ready Work，剩余工作都依赖 blocker 或需要外部 Authority → Global Blocker，才暂停。

## Slice Gate

一个 Slice 结束时，做一次足够证明能力真实成立的功能验证。

重点防止：

- 全 mock 绿了但真实集成没接通。
- UI / client 最后才接。
- persistence / migration 没走真实路径。
- external provider 只验证 SDK 调用。
- 权限只测允许路径，不测禁止路径。

## Stage Gate

Stage 验证证明：

- Stage Outcome 成立。
- Preservation 仍成立。
- Direct Regression 通过。
- 适用 Operational Obligations 真正可见。
- Hands-on Acceptance 可重复执行。

不要重跑与 Stage 无关的历史全量验证。即使上游写了宽泛“全量验证”，也应按当前 Verification Strategy 解释为证明 Stage Outcome 与直接回归所需的充分证据；确有强制法规 / 发布门禁时除外。

Stage Gate 通过后，不按“Stage 完成”机械 STOP，先看 Authorized Objective：

- Objective 就是 Current Stage → STOP。
- Objective 更高，下一 Stage 已冻结 / READY → CONTINUE。
- Objective 更高，下一步需要 Architect / Blueprint / Repair Planning，且当前 orchestrator 可调用 → ROUTE + CONTINUE。
- Objective 更高，但必须 Human / External Authority → PAUSE。
- FULL AUTO 下不得仅因为 Stage Gate 通过就再次问用户“要不要继续”。

## Contract Drift

施工过程中发现 Execution Contract 与 Repository Reality 冲突：

- 实施机械细节可局部修正 → Blueprint 范围内解决。
- Slice / Task 结构失效 → 回 Construction Blueprint。
- 产品语义缺失 / 产品定义改变 → Product。
- 架构决定改变 → Chief Architect。

施工 Agent 不自行“顺手修正上游设计”。

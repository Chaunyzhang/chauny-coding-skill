# Blueprint Mode

当存在有效 Execution Contract 时，本 Skill 与 Construction Blueprint 配套使用。

## Authority

`Stage-n Contract → Execution Contract → Repository Reality`

Product Definition 与 Architecture 仍是更高层语义权威，但施工 Agent 不应绕过 Execution Contract 自行重新规划。

## Task Loop

每个 Task：

1. 读取 Task 与前置条件。
2. 检查真实仓库。
3. 只做 Task 授权变化。
4. 只有存在当前 Live Uncertainty 时，执行最低成本的局部验证。
5. 保存真实证据。
6. 满足 Task Exit 后继续。

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

## Contract Drift

施工过程中发现 Execution Contract 与 Repository Reality 冲突：

- 实施机械细节可局部修正 → Blueprint 范围内解决。
- Slice / Task 结构失效 → 回 Construction Blueprint。
- 产品语义缺失 / 产品定义改变 → Product。
- 架构决定改变 → Chief Architect。

施工 Agent 不自行“顺手修正上游设计”。

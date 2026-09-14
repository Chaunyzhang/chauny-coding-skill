# Verification Budget

本文件是验证分层、Live Uncertainty 与验收 Authority 的唯一详细 owner，目标是同时防止验证不足和验证过度。

## Task

目标：快速发现当前改动的局部错误。候选手段包括 focused compile、lint/typecheck、focused unit test、schema/structure validation、narrow deterministic command。

它们不是固定 checklist；只在仍存在会改变下一步行动的 Live Uncertainty 时执行。已有等价证据且实现未变化时不重复。

优先使用当前平台最便宜、足以证明该不确定性的证据。iOS 等重平台的 build/test/真机可能天然较重，不作为每个 Task 的固定门槛；Agent 优先静态/结构检查并复用增量构建状态，在最早有意义的 Slice / Stage 聚合。真机由 Human 自己 Run/验证，Agent 不 build、不 install、不操作真机，并在 Slice 收口给出“测什么 / 看到什么算过”的最短清单。

## Slice

目标：证明一个真实能力路径成立。按需要覆盖 real DB/persistence、sandbox service、UI→backend→state、migration exercise、remote sink、permission path 或 relevant integration test。

同一真实边界首次建立或发生重大变化时证明即可，不要求每个 Task 重复。

## Stage

目标：证明 `Stage Outcome + Direct Regression + Hands-on path + Stage-level operational evidence` 成立。

同一事实只在最便宜且足够的层级证明一次。

## 强制即时风险

钱/数量正确性、数据库迁移、权限/可见性在相关改动附近验证，不全部拖到 Stage 尾部。

## 证据边界

Mock / fake / stub 只证明对应局部逻辑；没有真实验证时不得声称 provider、production-like runtime、real persistence、permission enforcement、remote sink 等真实边界成立。

## Live Uncertainty Gate

新增验证前回答：

1. 当前具体未知是什么？
2. 失败会改变什么行动？
3. 是否已有等价证据？

没有活的不确定性就不新增验证。

## Stop Rule

当前授权层级的 Outcome 已实现、证据充分、无 blocker、diff 可解释时，停止该层级验证。继续测试或扩大检查需要新的 Trigger；随后是否继续施工由 `execution-continuity.md` 决定。

## Authority Boundary

机器可证明的由 Agent 证明；审美、主观体验、真机感知或 Agent 无法访问的外部事项交对应 Human / External Authority。Agent 不模拟证据、不越权宣布 PASS，也不把可机械验证事项无理由推给 Human。

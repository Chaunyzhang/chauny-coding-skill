# Verification Budget

目的：防止“验证不足”和“验证过度”两个方向同时跑偏。

## Task

目标：快速发现当前改动的局部错误。

候选手段：

- focused compile
- lint / typecheck
- focused unit test
- narrow deterministic validation

这些不是固定 checklist。只有当前仍存在会改变下一步行动的 Live Uncertainty 时才执行对应检查。已有等价证据且相关实现未变化时不重复。

预算原则：优先使用当前平台最便宜、足以证明该不确定性的证据；高风险 Confirmed Defect 可以更贵。

重平台例外（iOS）：编译、跑测和真机可能天然较重，不作为每个 Task 的固定门槛。优先静态 / 结构检查并复用已有构建状态；真实运行按 Slice / Stage 或明确 Trigger 聚合。真机主观 / 感知验收按项目 Authority 交由 Human。

## Slice

目标：证明一个真实能力路径成立。

这里才适合：

- real DB / persistence
- real sandbox service
- UI → backend → state
- migration exercise
- remote event / crash sink
- permission path
- relevant integration test

同一个真实 Sink 不需要每个 Task 重复验证；首次建立或重大变化时证明即可。

## Stage

目标：证明 Stage Outcome + 直接受影响既有行为成立。

包含：

- Stage Acceptance
- Direct Regression
- Hands-on path
- Stage-level operational evidence

## 强制即时风险

钱与数量、数据库迁移、权限可见性必须在相关改动附近验证，不全部拖到 Stage 尾部。

## 证据边界

Mock / fake / stub 的绿灯只能声称对应局部逻辑成立。

不能声称：

- provider 接通
- production-like runtime working
- real persistence working
- permission enforcement working
- remote sink working

除非实际验证了对应真实边界。


## Live Uncertainty Gate

新增验证前必须回答：

- 当前具体未知是什么？
- 失败会改变什么行动？
- 是否已有等价证据？

没有活的不确定性就不新增验证。

## Stop Rule

当授权 Outcome 已实现、对应层级证据充分、没有 blocker、diff 可解释时，验证结束。继续测试或扩大检查需要新的 Trigger。

## Authority Boundary

机器可证明的由 Agent 证明；主观、人类专属或 Agent 无法访问的事项交对应 Authority。Agent 不得模拟证据或自行宣布通过，也不得把可机械验证事项无理由推给 Human。

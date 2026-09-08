# Verification Budget

目的：防止“验证不足”和“验证过度”两个方向同时跑偏。

## Task

目标：快速发现当前改动的局部错误。

默认：

- focused compile
- lint / typecheck
- focused unit test
- narrow deterministic validation

预算原则：通常应在秒级到约 10 秒。

不是绝对超时规则；高风险正确性可以更贵。

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

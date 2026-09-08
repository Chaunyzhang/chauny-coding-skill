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

重平台例外（iOS）：编译与单测运行超出本预算，不由 agent 执行——编译归人类（共享 DerivedData、Debug 增量），单测代码照写、运行归 Stage 前 / 发版前脚本补测一次；agent 在本层只做代码级静态检查，Task 放行 = 人类增量编译通过。Task 只本地提交，不推送、不等 CI；push 属 Slice 收口。真机不属于 agent 的任何一层，由人类按 Slice 收口清单执行。

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

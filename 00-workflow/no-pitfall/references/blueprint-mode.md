# Blueprint Mode

当存在有效 Execution Contract 时，与 Construction Blueprint 配套使用。

## Authority

施工权威链：`Stage-n Contract → Execution Contract → Repository Reality`。

Product Definition 与 Architecture 仍是更高层语义权威；施工 Agent 不绕过 Execution Contract 自行重规划。运行时持续授权、Horizon 与 Continue/Route/Pause/Stop 统一见 `execution-continuity.md`。

## Task Loop

每个 Ready Task：

1. 读取 Task、精确落点、prerequisites、Preservation / Direct Regression、Operational Obligations 与 Task Verification。
2. 检查真实仓库、caller、data/state flow、side effect、tests、generated source、config 与 relevant external boundary。
3. 只做当前 Task 授权变化，不偷做未来 Scope。
4. 按 `verification-budget.md` 消除当前 Live Uncertainty。
5. 保存真实证据：`Verified | Failed | Not Run | Environment Blocked | Inferred`。
6. 满足 Task Exit 后更新依赖图与 Ready Work；授权仍有效时继续，不默认返回用户。

验证失败先定位当前改动、环境或既有问题，不通过扩大 Scope 或无界重试推进。

## Local vs Global Blocker

当前 Task 阻塞但存在其他 Ready Work → Local Blocker，继续其他分支。

当前 Horizon 无任何 Ready Work，且剩余工作都依赖 blocker 或必须外部 Authority 解除 → Global Blocker，才暂停。

## Slice Gate

证明一个真实能力路径已经连接成立；按实际变化验证 real UI/client、persistence、API/service、sandbox provider、migration、permission 或 Operational Obligation evidence。

重点防止 mock 冒充真实集成、UI/client 最后才接、迁移未走真实路径、provider 只验证 SDK 调用、权限只测允许路径。

Task 完成只做本地提交，不 push、不触发或等待 CI；每个 Slice 收口一次性 push，触发一轮 CI，错误在收口统一处理。CI 属 Slice 级验证，不属 Task。

## Stage Gate

证明：Stage Outcome、Preservation、Direct Regression、适用 Operational Obligations 和 Hands-on Acceptance 成立。

不重跑与 Stage 无关的历史全量验证；宽泛“全量验证”应解释为证明当前 Stage Outcome 与直接回归所需的充分证据，除非存在明确法规/发布门禁。

Stage Gate PASS 后仍按 Authorized Objective 判断下一步，不因“Stage 完成”机械 STOP。

## Contract Drift

Execution Contract 与 Repository Reality 冲突时：

- 已冻结边界内机械细节 → 当前施工层解决。
- Slice / Task 结构、顺序或落点失效 → Construction Blueprint。
- 产品语义 / Product Definition 改变 → Product。
- Architecture / Stage Scope / interface / data / security / provider 等决定改变 → Chief Architect。

施工 Agent 不“顺手修正”上游设计。

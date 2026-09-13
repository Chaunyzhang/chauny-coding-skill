# Parallel Construction

本参考只判断 Task / Slice 是否适合多人、多窗口或独立 worktree 并行施工；不授权 Root 创建 subagent。Delegation 另过 `delegation-policy.md`。

并行单位仍只有 `Slice-n` 与 `Task-n`，禁止 `Worker-n / Lane-n / ParallelGroup-n`。真正并行意味着：**独立改变、独立证明、独立提交、低风险 fan-in**。

## Task parallel-safe

全部满足才可标记：
1. Task 已通过 Reasoning Gate，为 Low/Medium。
2. Prerequisite 在 fan-out 前独立满足。
3. Write Surface 低冲突。
4. 不竞争同一 schema/migration 顺序或 generated source-of-truth。
5. 不依赖共享可变状态的执行顺序。
6. 共用 interface/contract 已稳定。
7. 各自可完成 Local Proof。
8. 各自可独立 commit。
9. 合并顺序不改变已批准产品/架构语义。

推荐：
`freeze shared boundary → fan-out parallel Tasks → fan-in → Slice Capability Test`

多个 Task 若仍需边做边决定共享接口，就不是安全并行。

## Write Surface / Commit

高风险冲突包括同一核心文件、router/registry/central switch、schema definition、migration chain、generated source、project/manifest/localization 高冲突区、共享可变 fixture/environment。

少量文本交集不自动禁止，但要预判 merge 与语义冲突。

parallel-safe Task 应可单独 commit：仓库保持有效，不依赖其他未提交代码，commit 只含当前 Goal 与直接必要改动。共享重构应在 fan-out 前做 prerequisite Task。branch/worktree/window 命名属于施工执行层，不进入项目对象体系。

## Verification

每个并行 Task 只做自己的 Local Proof；fan-in 后再跑一次必要的 Slice Capability Test。禁止每个并行 Task 重复完整 E2E / Stage Test。

## Slice 并行

不同 Slice 也可并行，前提：
- 无产品前后依赖或共享 Stage state transition 顺序。
- 共用 architecture baseline 已冻结。
- write surface / sandbox 基本独立。
- migration/generated artifact 无顺序竞争。
- 每个 Slice 都能独立形成有效状态。

若 Slice-2 必须消费 Slice-1 的真实结果，保持顺序。

## Parallel Work Recommendation

存在真实收益时在 Execution Graph 后写：
```text
Parallel Work Recommendation
Recommended concurrent workers: <N>

Window A:
- Task/Slice:
- Prerequisite:
- Write Surface:
- Independent commit: Yes

...

Fan-in:
- merge ...
- run <Slice Capability Test / Stage Test>

Do not start in parallel:
- ...
```

`Window A/B` 只是 Human 展示标签，不是项目对象。没有值得并行的工作时：
`Parallel Work Recommendation: Stay sequential`

Blueprint 负责技术判断；Human 只决定按推荐并行、少开窗口或单窗口顺序执行。单窗口必须始终正确。

## 不值得并行 / 禁止

保持 sequential，当 coordination/merge/revalidation 成本高于收益、Root 已加载全部关键 context、Task 很小、高概率改同一文件、interface 未冻结、migration/schema 必须连续演进、sandbox 只能串行、同一状态机强顺序或当前 Slice 本身很短。

禁止为协作切碎高内聚 Task、多人同时设计同一共享 interface、并行改同一 migration、无 source-of-truth 地并行改 generated output、每个并行 Task 重复整套 E2E、把 branch/worktree/window 变成编号体系。

目标是优化总交付时间，不是最大化同时工作的 Agent 数量。

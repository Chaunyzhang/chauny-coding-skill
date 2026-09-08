# Parallel Construction

本参考把“理论上可以同时做”收敛成“多人 / 多 Agent 可以安全独立施工、独立提交、低冲突合并”。

## 核心原则

并行单位仍然只有 `Slice-n` 与 `Task-n`。禁止创建 `Worker-n`、`Lane-n`、`ParallelGroup-n` 等新对象。

真正的并行不是“同时开始”，而是：

> 可以独立改变、独立证明、独立提交，最后低风险 fan-in。

## Task 并行判定

只有以下条件都满足，Task 才标 `parallel-safe`：

1. Prerequisite 在 fan-out 前已经成立。
2. Write Surface 低冲突。
3. 不竞争同一 schema / migration 顺序。
4. 不竞争同一 generated source-of-truth。
5. 不依赖共享可变状态的执行顺序。
6. 共用 interface / contract 已在并行前稳定。
7. 各自可完成 Task Simple Test。
8. 各自可形成独立 commit。
9. 合并顺序不会改变已批准产品 / 架构语义。

## 先冻结共享边界，再 fan-out

推荐：

```text
Task-1 — Freeze shared interface
    ↓
    ├── Task-2 [parallel-safe]
    ├── Task-3 [parallel-safe]
    └── Task-4 [parallel-safe]
              ↓
Slice Capability Test
```

如果多个任务都需要一边做一边重新决定共享接口，它们不是真并行。

## Write Surface

蓝图应尽量让并行 Task 修改不同模块 / 文件 / schema 区域。

高风险冲突包括：

- 同一核心文件。
- 同一 router / registry / central switch。
- 同一 schema definition。
- 同一 migration chain。
- 同一 generated source-of-truth。
- 同一 project / manifest / localization 高冲突区域。
- 同一共享可变 fixture / environment state。

少量文本交集不一定禁止并行，但必须预判 merge conflict 和语义冲突。

## Independent Commit

parallel-safe Task 原则上必须可以单独 commit：

- 仓库保持有效。
- 不依赖其他 Agent 的未提交代码。
- commit 只覆盖当前 Task Goal 与直接必要修改。
- 不夹带共享重构；共享重构应成为 fan-out 前 prerequisite Task。

Blueprint 不规定 branch / worktree / chat window 名称。隔离机制属于施工执行层。

## Verification

每个并行 Task 只负责自己的 Simple Test。

```text
Task-2 -> targeted test -> commit
Task-3 -> targeted test -> commit
Task-4 -> targeted test -> commit

fan-in
-> Slice Capability Test
```

禁止每个并行 Task 都重复跑完整 E2E / Stage Test。

## Slice 并行

不同 Slice 也可并行，前提：

- 无产品前后依赖。
- 无共享 Stage state transition 先后要求。
- 共用 architecture baseline 已冻结。
- write surface 基本独立。
- sandbox / environment 不互相污染。
- migration / generated artifact 无顺序竞争。
- 每个 Slice 都可形成独立有效状态。

如果 Slice-2 必须消费 Slice-1 的真实结果，保持顺序。

## Parallel Work Recommendation

存在值得并行的机会时，Execution Contract 在 Execution Graph 后写：

```text
Parallel Work Recommendation

Recommended concurrent workers: 3

Window A:
- Task-2
- Prerequisite: Task-1
- Write Surface: ...
- Independent commit: Yes

Window B:
- Task-3
- Prerequisite: Task-1
- Write Surface: ...
- Independent commit: Yes

Window C:
- Task-4
- Prerequisite: Task-1
- Write Surface: ...
- Independent commit: Yes

Fan-in:
- merge Task-2 / Task-3 / Task-4
- run Slice-1 Capability Test

Do not start in parallel:
- Task-5 waits for Slice-1 Capability Test
```

`Window A/B/C` 只是给人类看的展示标签，不是正式项目对象。

没有值得并行的工作时：

`Parallel Work Recommendation: Stay sequential`

## 人类控制者协议

Blueprint 负责技术判断；人类不需要读依赖图自己猜。

Construction Agent 开工时必须把推荐翻译成人话，例如：

> 当前适合开 3 个并行窗口：Task-2、Task-3、Task-4。三项不争用高冲突修改面，都可以独立提交。完成后回主窗口合并，并只跑一次 Slice-1 Capability Test。

人类只决定：

- 按推荐并行；
- 少开几个窗口；
- 或单窗口顺序做。

单窗口执行必须始终保持正确。

## 不值得并行

直接保持 sequential，当：

- 并行只节省很少时间但协调成本更高。
- Task 很小。
- 高概率修改同一文件。
- interface 尚未冻结。
- migration / schema 必须连续演进。
- sandbox 只能安全串行。
- 同一状态机存在强顺序。
- 当前 Slice 本来就是很短的纵向闭环。

原则：

> 优化总交付时间，不优化“同时工作的 Agent 数量”。

## 禁止

- 为了多人协作把高内聚 Task 生硬切碎。
- 多个 Agent 同时设计同一个共享接口。
- 并行修改同一 migration。
- 并行修改 generated output 而没有明确 source-of-truth。
- 每个并行 Task 都重复整套 E2E。
- 把 branch / worktree / window 变成新编号体系。

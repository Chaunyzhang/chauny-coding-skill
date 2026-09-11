# Delegation Compilation Policy

目标：

> 在 Blueprint 阶段决定“创建新的模型上下文是否真的值得”，避免 Construction Agent 因复杂感、并行冲动或安全感而过度 spawn。

默认：

`Root executes directly`

Subagent 是例外。

## 1. Delegation Value

Subagent 的价值来自：

`Context Saved`
`+ Parallel Time Saved`
`+ Specialized Capability`
`+ Independent Evidence`
`- Startup Cost`
`- Duplicate Work`
`- Coordination Cost`
`- Information Loss`
`- Tail Latency`
`- State Conflict Risk`

Blueprint 不要求精确算数学值，但必须判断净收益方向。

## 2. Score

候选委派每项 `0 / 1 / 2`：

### Independence
- 0：强依赖 Root / Child 中间决策。
- 1：少量依赖。
- 2：可以自主完成。

### Workload
- 0：Root 几分钟可完成。
- 1：中等搜索 / 工具工作。
- 2：大量检索、多轮工具、长时间自主调查。

### Compressibility
- 0：结果几乎要原样带回全部 context。
- 1：可部分压缩。
- 2：大量内部过程可压成少量结论 / 证据。

### State Isolation
- 0：争用共享可变状态 / 高冲突文件。
- 1：有少量协调。
- 2：read-only 或独立 worktree / write surface。

### Added Value
- 0：只是复制 Root 同类思考。
- 1：有限并行 / 专业价值。
- 2：独立 verifier、专用工具 / 模型、明显 critical-path reduction。

总分：
- `0–5`：Root。
- `6–7`：默认 Root。
- `8–10`：Candidate，继续 Time Gate。

## 3. Time Gate

Time 是独立硬门禁。

### -2
明显更慢：
- Child 重新读取 Root 已加载的大量 context。
- Root 必须等待 / review / merge。
- Tail latency 明显增加。

→ 不委派。

### -1
大概率不省：
- 工作本身很短。
- Spawn / coordination 与工作本身同量级。

→ 不委派。

### 0
时间基本持平。

只有以下价值之一足够强才允许：
- context isolation
- independent verification
- specialized capability

必须明确写 Purpose。

### +1
Root 可同时推进真正独立工作，有可见 wall-clock 收益。

### +2
明显缩短 critical path。

仍需通过其他 Gate。

## 4. Time Estimation

不要求虚假精确分钟数。

Blueprint 只需判断：
- Short：Root 直接做更快。
- Material：足够重，可能覆盖 spawn 成本。
- Long：明显适合并行 / 后台自主调查。

以及：
- Root 当前是否已经加载相关 context？
- Root 是否有真正独立工作可继续？
- Parent 是否必须等待 Child 才能继续 critical path？
- Fan-in 是否有额外 merge / review / test 成本？

“并行”不自动等于“更快”。

## 5. Hard Veto

以下直接否决：
- deterministic tool 足够。
- Root 已经有绝大多数 context。
- Child 需要高频向 Root 问中间问题。
- 大部分原始 context 必须返还 Root。
- 共享 migration / schema / generated source / fixture / core file 高冲突。
- Task 仍有 High reasoning / unresolved design。
- 只是复制 reviewer 获得安全感。
- child needs child。
- 工作量小于明显 spawn / coordination 成本。

## 6. Preferred Delegation Types

### Explore / Context Compression
适合：
- repo archaeology
- 大量 grep / 文件阅读
- 长日志分析
- 最终只需少量结论与 evidence locations

推荐 read-only。

### Independent Investigation
适合多个无依赖信息流：
- API / protocol
- privacy / retention
- pricing / quota
- provider capability

### Independent Verifier
价值来自上下文独立。

适合 Critical / Sensitive：
- transaction
- money / usage
- authorization
- privacy
- migration
- recovery

默认 read-only：
`read / inspect / targeted test / report`

输出：
`PASS | FAIL | UNPROVEN + evidence`

Verifier 不重设计、不顺手改代码、不 spawn reviewer。

### Long Autonomous Investigation
适合：
`run → observe → diagnose → rerun targeted`

且 Root 可以同时做其他独立工作。

如果只是等待一个 deterministic command，启动 process，不启动 Agent。

### Isolated Implementation
门槛最高。

仅当：
- frozen contract
- Low / Medium Task
- independent write surface
- independent commit
- clear fan-in
- positive Time Impact

才允许 Child 写代码。

## 7. Forbidden Delegation

默认禁止：
- handler / service / test 按文件类型拆给不同 Agent。
- implementation 与其对应 test 同时由两个 Agent 在共享行为上独立设计。
- 每个 Task 固定 architect + coder + reviewer + tester。
- 每 3–5 个文件机械拆一个 Agent。
- 为 shell command 启动 Agent。
- 为“再看一遍”连续创建 reviewer。
- 多个 Agent 修改 OpenAPI / migration / generated DTO / shared fixture。
- Child recursive spawn。
- 用更多 Agent 补偿不完整 Blueprint。

## 8. Parallel Work vs Delegation

Parallel Work：
> 多个独立施工窗口 / 人 / worktree 同时领取不同 Task。

Delegation：
> 一个 Root 在当前 Task /工作流中创建新模型上下文。

两者可以同时存在，但互不自动推出。

如果 Blueprint 已经建议人类开两个独立窗口，不代表每个窗口内部还应该继续 spawn。

## 9. Concurrency Limit

保守默认：
- depth = 1
- concurrent subagents = 0–2
- 常规上限 = 3

超过 3 只适用于高度可分解、read-only、长时间 research / investigation，并需要明确说明为什么更多 Agent 仍缩短 critical path。

目标不是最大化 occupancy。

## 10. Execution Contract Shape

没有委派价值：
不写 Delegation 字段。

有委派价值：

```text
Delegation

Purpose:
Scope:
Deliverable:
Read / Write Boundary:
Expected Wall-clock Effect: Neutral | Positive | Strongly Positive
Fan-in:
Recursive Spawn: No
```

如果是 Neutral，必须额外说明为什么 context isolation / independent evidence 值得付出时间。

## 11. Runtime Surprise

Blueprint 未授权 Delegation 时，Construction 默认 Root。

只有运行时出现新的、之前无法预见的强候选，才可提出：

```text
Delegation Candidate
Reason:
Expected added value:
Expected wall-clock effect:
State isolation:
Deliverable:
```

不是自动 spawn。

## 12. Stop Rule

Child 返回所需 deliverable 后停止。

Root 不得：
- 为了“更确定”创建第二个同类 Child。
- 因 Child 结果不符合预期就自动再复制一个同任务 Agent。
- 不断 polling Child；应使用正常等待 / completion mechanism。
- 已有结果仍重新做完整探索。

原则：

> 每一个新模型上下文都必须带来新的、决策相关的信息价值。

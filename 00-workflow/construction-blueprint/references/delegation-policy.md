# Delegation Compilation Policy

目标：在 Blueprint 阶段判断“创建新模型上下文是否真的值得”。默认 `Root executes directly`；Subagent 是例外。

## 价值模型与 Score

价值来自：
`Context Saved + Parallel Time Saved + Specialized Capability + Independent Evidence - Startup - Duplicate Work - Coordination - Information Loss - Tail Latency - State Conflict`

不要求精确数学值，但必须判断净收益。

候选委派每项 `0 / 1 / 2`：
- **Independence**：0 强依赖 Root；1 少量依赖；2 可自主完成。
- **Workload**：0 Root 几分钟完成；1 中等搜索/工具；2 大量检索、多轮工具或长调查。
- **Compressibility**：0 几乎原样返还 context；1 可部分压缩；2 大量过程可压成少量结论/evidence。
- **State Isolation**：0 争用共享状态/高冲突文件；1 少量协调；2 read-only 或独立 worktree/write surface。
- **Added Value**：0 复制 Root 思考；1 有限并行/专业价值；2 独立 verifier、专用工具/模型或明显 critical-path reduction。

总分：
- `0–5`：Root。
- `6–7`：默认 Root，除非明确附加价值。
- `8–10`：Candidate，继续 Time Gate。

## Time Gate

`Time Impact`：
- `-2`：明显更慢；重复读 context、等待/review/merge、tail latency 高 → 禁止。
- `-1`：工作短，spawn/coordination 与工作同量级 → 禁止。
- `0`：时间持平；仅当 context isolation、independent verification 或 specialized capability 明确有价值才允许，并写 Purpose。
- `+1`：Root 可同时推进独立工作，有可见收益。
- `+2`：明显缩短 critical path。

即使正收益仍需过其他 Gate。Critical/Sensitive 的 independent verifier 可因独立证据价值在 `0` 时成立，但必须明确 `Purpose: independent verification`。

时间估算无需虚假分钟数，只判断 Short / Material / Long，并考虑 Root 是否已加载 context、是否能推进独立工作、是否等待 Child、fan-in merge/review/test 成本。

## Hard Veto

满足任一项原则上不 spawn：
- shell/grep/compiler/formatter/test runner/SQL/AST/普通脚本即可完成。
- Root 已加载绝大部分 context。
- 工作短于明显 spawn/coordination 成本。
- Child 需频繁等待 Root 决策。
- 大部分原始 context 必须返还 Root。
- 共享 migration/schema/generated source/fixture/core file 高冲突。
- 只是复制 reviewer 获得安全感。
- Task 仍有 High reasoning / unresolved design。
- Child 需要继续创建 Child。

默认 `max delegation depth = 1`；常规 concurrent subagents `0–2`，上限 3。超过 3 只适合高度可分、read-only、长时间 research/investigation，并必须说明仍能缩短 critical path。

## 合法类型

**Explore / Context Compression**：repo archaeology、大量 grep/文件/日志，最终只返回少量结论和 evidence locations；推荐 read-only。

**Independent Investigation**：多个无依赖信息流，如 API/protocol、privacy/retention、pricing/quota、provider capability。

**Independent Verifier**：Critical/Sensitive 的 transaction、money/usage、authorization、privacy、migration、recovery 等。默认 read-only，输出 `PASS | FAIL | UNPROVEN + evidence`；不重设计、不顺手改代码、不 spawn reviewer。

**Long Autonomous Investigation**：需要持续 `run → observe → diagnose → targeted rerun`，且 Root 可推进其他独立工作。若只是等待 deterministic command，启动 process，不启动 Agent。

**Isolated Implementation**：门槛最高。只有 frozen contract、Low/Medium Task、独立 write surface/commit、清楚 fan-in、正 Time Impact 同时成立时才允许 Child 写代码。

## Forbidden Delegation

禁止默认：
- 按 handler/service/test 文件类型拆 Agent。
- implementation 与对应 test 由两个 Agent 在共享行为上独立设计。
- 每 Task 固定 architect/coder/reviewer/tester。
- 每几文件机械拆 Agent。
- 为 shell command 启 Agent。
- 连续创建同类 reviewer。
- 多 Agent 改 OpenAPI/migration/generated DTO/shared fixture。
- Child recursive spawn。
- 用更多 Agent 补偿不完整 Blueprint。

`Parallel Work`（多窗口/人/worktree）与 `Delegation`（单 Root 新模型上下文）互不自动推出。

## Contract Shape

无价值时不写 Delegation 字段。有价值时：
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
Neutral 必须说明 isolation / independent evidence / specialized capability 的价值。

Blueprint 未授权时 Construction 默认 Root。运行时若出现此前不可预见的强候选，只能提出：
```text
Delegation Candidate
Reason:
Expected added value:
Expected wall-clock effect:
State isolation:
Deliverable:
```
不能自动 spawn。

## Stop Rule

Child 交付所需 deliverable 后停止。Root 不因“不够确定”再造同类 Child，不因结果不符合预期自动复制同任务 Agent，不高频 polling，不在已有结果后重做完整探索。

每个新模型上下文必须带来新的、决策相关的信息价值。

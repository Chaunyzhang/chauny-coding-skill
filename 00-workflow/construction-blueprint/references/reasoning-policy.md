# Reasoning Compilation Policy

目标：

> 用 Blueprint 关闭设计空间，让 SOTA Construction Agent 在 Low / Medium reasoning 下稳定、快速施工。

Reasoning Score 衡量的是**剩余需要施工 Agent 自己寻找答案的空间**，不是工作量、文件数、代码行数或业务重要性。

## 1. 评分维度

每项 `0 / 1 / 2`，在 Task 已经编译完成后评分。

| 维度 | 0 | 1 | 2 |
|---|---|---|---|
| Goal certainty | 结果 / 行为完全明确 | 少量局部解释 | 还需推导到底要做什么 |
| Implementation choice | 唯一路径 /成熟项目模式 | 有限局部选择 | 多条实质不同路线都合理 |
| Contract / ownership | input/output/interface/owner 已冻结 | 少量适配 | contract / ownership 还需设计 |
| State semantics | 无复杂状态或状态已冻结 | 有限局部状态判断 | 状态机 / lifecycle 还需发明 |
| Failure / recovery | 失败语义已冻结 | 有限局部判断 | retry/recovery/unknown side effect 还需设计 |
| Ordering / concurrency | 无或顺序已冻结 | 有限局部协调 | ordering/replay/concurrency 语义未决 |
| Repository consistency | 文档/代码/测试一致 | 有小差异但兼容 | 相互矛盾，不知道谁是 authority |
| Proof certainty | proof 明确 | 在有限证据中选择 | 还不知道怎样证明正确 |
| Project precedent / novelty | 已有成熟模式 | 有相似实现 | 项目首次出现的新机制 |
| Construction mechanicality | 直接翻译成代码/配置 | 普通实现判断 | 需要发明算法 / protocol /机制 |

总分：

- `0–4` → `Low`
- `5–10` → `Medium`
- `11–20` → **Invalid Blueprint Task**

## 2. Hard Planning Defects

即使总分 ≤10，以下情况仍不得发布：

- Goal certainty = 2
- Contract / ownership = 2
- Repository consistency = 2
- Proof certainty = 2

这些不是“施工难”，而是 Blueprint 仍缺关键事实。

其他维度出现 `2` 时，Blueprint 必须确认它不是未解决设计空间。若施工仍需要发明状态机、failure model、ordering 语义、算法或协议，也不得发布。

## 3. Low

Low 表示：

> 已有答案，只需可靠地翻译成实现。

典型：

- DTO / schema 字段接线
- generated artifacts
- config
- rename
- dependency injection
- 已有模式的 handler / worker
- fixture / mock 更新
- 按冻结接口增加 caller

Low 不等于“不认真”。

它意味着：

- 不重新设计。
- 不做开放式 repository-wide research。
- 不为提高信心自行扩 Scope。

## 4. Medium

Medium 表示：

> 合同完整，但实现仍有有限局部选择。

典型：

- 已冻结 contract 的 domain service
- API + DB query
- 已有 transaction pattern 的业务动作
- pagination / cursor
- 普通 client feature
- 组合已经确定的 components
- Critical domain 的具体实现，但 invariant / failure semantics 已冻结

Medium 可以做局部工程判断，但不能改变：

- Product semantics
- Architecture
- ownership
- contract
- state machine
- failure / recovery semantics
- ordering guarantee
- Acceptance

## 5. High / XHigh

High / XHigh 只允许出现在：

- Architecture decision
- Blueprint 形成过程
- Repository contradiction reconciliation
- failure / state / protocol design
- 上游 clarification

**不得出现在最终 Construction Task。**

如果一个 Task 需要 High：

1. 不给 Construction 升档。
2. 找到剩余设计空间来自哪一维。
3. Blueprint / Architecture / Product 先解决。
4. 重新编译 Task。
5. 重新评分，直到 ≤10。

## 6. Criticality 独立

Reasoning ≠ Criticality。

建议仅在高后果任务需要时标：

- `Sensitive`
- `Critical`

常见 Critical 边界：

- money / usage / quota
- identity / authorization / privacy
- important data integrity
- irreversible deletion
- migration
- external side effect
- business idempotency
- concurrency / ordering
- cross-account / session / device isolation

Criticality 影响：

- invariant 必须更明确
- proof 必须更有力
- review 必须覆盖关键 failure window

但不自动增加 Reasoning Score。

好蓝图常见：

`Reasoning: Medium (7)`
`Criticality: Critical`

这表示“很重要，但答案已经想清楚”。

## 7. 降低 Reasoning 的正确方法

### 正确

- 冻结 interface / schema / ownership
- 明确 state transition
- 明确 failure / retry / recovery
- reconcile repository reality
- 指定唯一已批准 path
- 明确 proof
- 把独立能力边界拆成独立 Task

### 错误

- 把一个原子 transaction 生硬拆成三个互不完整 Task
- 用更小文件数伪装成更简单
- 删除 failure semantics 让分数看起来更低
- 把设计问题留一句“施工时自行判断”
- 直接把 High 改标签为 Medium

降低的是**决策空间**，不是 Task 的字数和体积。

## 8. 工作量不等于 Reasoning

以下即使很大，也可能是 Low：

- 30 个文件的机械迁移
- 批量 DTO / generated code
- 大量固定模式 wiring
- 按明确规则改很多 fixture

以下即使只有十行，也可能暴露 Blueprint 未完成：

```text
Begin()
Debit()
InsertReceipt()
Commit()
```

如果 transaction / idempotency / failure semantics 还没冻结，问题在 Blueprint，不在代码行数。

## 9. Construction Escalation

Construction 读取 Blueprint 已给出的 class，不重新跑完整 10 维评分。

如果现实变化导致：

- contract 不再成立
- target 不存在
- repository 与 Entry State 冲突
- frozen semantics 无法实现
- Medium 内存在多个实质不同正确答案

则：

`STOP → BLOCKED`

回 Blueprint / Architecture / Product。

禁止：

`Medium → High → 自己重新设计`

## 10. Blueprint Quality Signal

一个 READY Blueprint 应满足：

- 100% Task 为 Low / Medium
- 0 个 High / XHigh
- 0 个 unresolved product decision
- 0 个 unresolved architecture decision
- 0 个 unresolved state / failure semantics
- 0 个 unknown proof strategy

如果大量 Task 接近 10 分，Blueprint 应检查是否仍有可关闭的重复设计空间，但不为了追求低分做无意义拆分。


## 11. Reasoning Does Not Justify Delegation

Task 的 Reasoning Score 和 Delegation 是两套独立判断。

禁止：

`Task 更复杂 → spawn 更多 Agent`

正确顺序：

1. Blueprint 先把 Task 编译到 Low / Medium。
2. 再判断某块工作是否因 context isolation、真实并行、独立证据或专用能力值得新上下文。
3. 通过 Delegation Gate 后才 spawn。

Subagent 不能补偿一个 High / unresolved Task。

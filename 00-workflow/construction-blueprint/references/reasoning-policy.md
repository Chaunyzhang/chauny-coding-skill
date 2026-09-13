# Reasoning Compilation Policy

目标：Blueprint 关闭设计空间，让 Construction 在 Low / Medium reasoning 下稳定施工。Reasoning Score 衡量**剩余需要施工 Agent 自己寻找答案的空间**，不是工作量、文件数、代码行数或业务重要性。

## Score

Task 编译完成后，每项 `0 / 1 / 2`：

| 维度 | 0 | 1 | 2 |
|---|---|---|---|
| Goal certainty | 结果/行为明确 | 少量局部解释 | 还需推导要做什么 |
| Implementation choice | 唯一路径/成熟模式 | 有限局部选择 | 多条实质路线都合理 |
| Contract / ownership / authority | interface/owner 已冻结 | 少量适配 | 仍需设计 |
| State semantics | 无复杂状态或已冻结 | 有限局部判断 | state/lifecycle 还需发明 |
| Failure / recovery | 已冻结 | 有限局部判断 | retry/recovery/side effect 还需设计 |
| Ordering / concurrency | 无或已冻结 | 有限协调 | ordering/replay/concurrency 未决 |
| Repository consistency | 文档/代码/测试一致 | 小差异但兼容 | authority 冲突 |
| Proof certainty | proof 明确 | 有限证据选择 | 不知道如何证明 |
| Project precedent / novelty | 成熟模式 | 有相似实现 | 项目首次新机制 |
| Construction mechanicality | 直接翻译 | 普通实现判断 | 需发明算法/protocol/机制 |

总分：
- `0–4` → `Low`
- `5–10` → `Medium`
- `11–20` → **Invalid Blueprint Task**

即使总分 ≤10，`Goal certainty = 2`、`Contract/ownership/authority = 2`、`Repository consistency = 2`、`Proof certainty = 2` 仍是 Hard Planning Defect，不得发布。其他维度为 2 时，也必须确认 Construction 不需要发明 state machine、failure model、ordering、algorithm 或 protocol。

## Low / Medium / High

**Low**：答案已存在，只需可靠翻译。可用于固定 schema/DTO wiring、generated artifacts、config、rename、DI、成熟模式 handler/worker、fixture/mock 更新、按冻结 interface 增 caller。Low 不等于草率；不得重新设计、开放式全仓研究或自行扩 Scope。

**Medium**：contract 完整，但有有限局部实现选择。可做冻结 contract 下的 domain service、API+DB query、既有 transaction pattern、pagination、普通 client feature、已确定 component 组合等。不得改变 Product semantics、Architecture、owner/authority、module/dependency boundary、contract、state machine、failure/recovery、ordering guarantee 或 Acceptance。

**High / XHigh** 只允许出现在 Architecture decision、Blueprint 形成、repository contradiction reconciliation、state/failure/protocol design 或上游 clarification；不得进入最终 Construction Task。

Task 需要 High 时：
1. 找出剩余设计空间。
2. Blueprint / Architecture / Product 先关闭它。
3. 重新编译并评分，直到 ≤10。

不得通过拆坏原子 correctness boundary、删 failure semantics、把设计问题留给施工或直接改标签来“降分”。降低的是决策空间，不是 Task 字数。

## Criticality 独立

Reasoning ≠ Criticality。高后果边界可按需标：
- `Sensitive`
- `Critical`

常见：money/usage/quota、identity/authorization/privacy、important data integrity、irreversible deletion、migration、external side effect、idempotency、concurrency/ordering、cross-account/session/device isolation。

Criticality 提高 invariant、proof、review 要求，但不自动提高 Reasoning。合法组合如：
`Reasoning: Medium (7)` + `Criticality: Critical`

## 工作量与 Novelty

大量机械迁移、批量 DTO/generated wiring、固定模式 fixture 即使文件很多也可能 Low。十几行代码如果 transaction/idempotency/failure semantics 未冻结仍是 planning defect。项目第一次做某机制也不自动 High；若 Provider、interface、failure mapping、repository target、proof 都已冻结，可仍是 Medium。

## Construction Escalation

Construction 直接消费 Blueprint 的 class，不重新跑 10 维评分。若运行时发现 contract 失效、target 不存在、Repository Reality 冲突、冻结语义无法实现，或 Medium 内仍有多个实质不同正确答案：

`STOP → BLOCKED`

回 Blueprint / Architecture / Product。禁止 `Medium → High → 自行重新设计`。

## Quality Signal

READY Blueprint：
- 100% Task 为 Low / Medium；0 High/XHigh。
- 0 unresolved product / architecture / state / failure decision。
- 0 unknown proof strategy。

大量 Task 接近 10 分时检查是否仍有可关闭设计空间，但不得为追求低分做无意义拆分。

## Reasoning 不授权 Delegation

正确顺序：
1. 先把 Task 编译到 Low / Medium。
2. 再判断新上下文是否因 isolation、真实并行、独立证据或专用能力产生价值。
3. 只有通过 Delegation Gate 才 spawn。

Subagent 不能补偿 High / unresolved Task。

# Review Protocol

> Owner: Initial Review / Fix Review 的阅读与证据方法。继续/停止 Gate 由 `convergence-protocol.md` 定义。

## Diff-first, Contract-first

顺序：

1. 读 Current Stage 所需 Contract / Atoms / Architecture / Blueprint。
2. 读 diff。
3. 还原实际 execution path。
4. 只有出现具体 uncertainty 时扩展到相邻代码。

不要先全库搜索“有没有问题”。

## Reasonable Expansion

为确认当前 obligation / Finding 可以：

- 找 canonical authority；
- 看 direct caller / callee；
- 看 owning domain public interface；
- 看 touched entity lifecycle；
- 看 current regression dependency。

不允许：

- 顺手审 unrelated module；
- 扫历史 Stage 找旧问题；
- 扫 future code 猜风险；
- 因看到更多文件而自行扩大 review boundary。

Initial Review 的每个额外动作必须关闭 mandatory review coverage 或 Live Uncertainty；Finding Freeze 后必须通过 Action Admission Gate。

## Computational Sensors vs Inferential Review

优先使用工具证明它擅长的事实：

- compiler / typecheck；
- lint / formatter；
- dependency rules；
- static analysis；
- targeted test；
- query plan / profiler（有 live uncertainty 时）；
- complexity metric（sensor）。

Reviewer 推理重点：

- semantic coverage；
- authority duplication；
- ownership；
- module boundary；
- change locality；
- abstraction quality；
- side-effect placement；
- maintainability。

不要用 LLM token 替代静态工具，也不要因工具存在就无条件全跑。

## Test Discipline

已有新鲜、可信、范围匹配 evidence ⇒ 直接消费。

新代码阅读产生具体 uncertainty ⇒ 跑最小 targeted evidence。

高成本 environment / device / deployment ⇒ 只有 Acceptance、required capability proof 或具体 uncertainty 要求时使用。

同一事实不要在多个层级重复证明。

## Human / External Authority

Agent 可判断：

- code / dependency / schema；
- test / build；
- module boundary；
- authority duplication；
- state flow；
- deterministic runtime evidence。

Human / external authority：

- subjective visual quality；
- Agent 无法访问的 physical-device sensory judgment；
- business/product choice；
- inaccessible external manual process。

Agent 不得把无法实际观察的事情报告为 PASS，也不得把本可机械证明的事实无理由转嫁给 Human。

## After Finding Freeze

诊断与后续动作必须分开：

1. Frozen Finding Set 成立。
2. Re-intake 相关 Product / Architecture / Stage / original Blueprint / Repository Reality。
3. 按 root cause 合并。
4. 判断 Implementation / Blueprint repairable，还是 Architecture / Product / Evidence route。
5. 编译 Repair Handoff Contract。
6. 停止 Stage Verifier 的施工规划。

不要把 Finding 的 `Required State` 扩写几句就假装是 Blueprint，也不要由 Verifier 自己创建 Task / Slice。

## Fix Review

Fix Review 只读：

- immutable Review Snapshot；
- Repair Handoff；
- Repair Execution；
- latest diff；
- Repair Evidence。

只验证 Frozen Findings、合法 REGRESSION 和 direct impact。任何新检查都必须通过 `convergence-protocol.md` 的 Action Admission Gate。

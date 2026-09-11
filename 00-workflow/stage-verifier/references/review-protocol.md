# Review Protocol

> 本文件可独立使用：可直接作为审查方法协议；在 stage-verifier 流程中，由 `SKILL.md` 的「首次审查流程」加载。

## Diff-first, Contract-first

顺序：

1. 读 Contract / Atoms / Architecture / Blueprint。
2. 读 diff。
3. 还原实际 execution path。
4. 只有出现具体 uncertainty 时扩展到相邻代码。

不要先全库搜索“有没有问题”。

## 合理扩展范围

允许为了确认当前 Finding：

- 找 canonical authority。
- 看 direct caller / callee。
- 看 owning domain public interface。
- 看 touched entity lifecycle。
- 看 current regression dependency。

不允许：

- 顺手审 unrelated module。
- 扫历史 stage 找旧问题。
- 扫 future code 猜风险。

## Computational Sensors vs Inferential Review

### Computational

优先复用：

- compiler / typecheck
- lint / formatter
- dependency rules
- static analysis
- test
- query plan / profiler（有 live uncertainty 时）
- complexity metric（sensor）

### Inferential

Reviewer 智能主要花在：

- semantic coverage
- authority duplication
- ownership
- module boundary
- change locality
- abstraction quality
- side-effect placement
- maintainability

不要用 LLM token 替代静态工具擅长的事情。

## Test Discipline

已有足够 evidence：

不重复。

新代码阅读产生新 uncertainty：

只跑 targeted evidence。

高成本环境 / device / deployment：

只有 current acceptance / slice proof / specific uncertainty 要求时使用。

## Human Authority

Agent 可判断：

- code / dependency / schema
- test / build
- module boundary
- authority duplication
- state flow
- deterministic runtime evidence

Human / external authority：

- subjective UI visual quality
- physical device sensory judgment（Agent 无法访问时）
- business/product choice
- inaccessible external manual process

Agent 不得把无法实际观察的事情报告为 PASS。

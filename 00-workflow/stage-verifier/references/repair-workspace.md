# Repair Workspace & Stage Reconciliation

> Owner: Repair Cycle 的临时文档工作区、canonical Stage 只读边界、一次性 Reconciliation 与清理。

## Why

Repair 期间反复直接改 canonical Stage Execution Contract 会混合：

- 原计划；
- 已失效计划；
- Finding；
- 中间修法；
- 最终事实。

这会制造冲突 authority，并增加模型把历史叙述误当当前施工真相的风险。

因此：

> Repair 是临时工作空间；canonical Stage 文档只在 repair verified 后一次性 reconciliation。

## Workspace Location

项目已有临时工作区约定时沿用；否则默认：

`.workbench/repairs/Stage-<N>/`

必须满足：

- 与 canonical `docs/` 事实源分离；
- 明确 temporary / non-authoritative；
- 同一 Repair Cycle 的材料集中；
- 最终可整体删除或按明确审计要求归档。

## Minimal Artifacts

```text
Review-Snapshot.md
Repair-Handoff.md
Repair-Execution.md
Repair-Evidence.md
```

### Review-Snapshot.md

首次 Review 的 immutable snapshot：Result、Frozen Findings、Quality Matrix、关键 evidence baseline。

冻结后不修改 Finding 内容；状态变化写到 Repair-Evidence。

### Repair-Handoff.md

Stage Verifier 输出的冻结 contract。Construction Blueprint 只能在该 boundary 内规划；若无法正确施工则 Route，不自行扩大。

### Repair-Execution.md

由 Construction Blueprint / Repair Mode 生成。颗粒度必须与正常 Construction Blueprint 一致，并使用其 planning / reasoning / delegation / parallel / verification gates；但它是临时 contract，不创建新的长期 Stage / Requirement / Decision 对象。

### Repair-Evidence.md

记录：

- Finding → Resolution State；
- required proof；
- direct regression；
- repair-introduced REGRESSION；
- Builder / Verifier 可定位 evidence。

不要把开放式探索日志全部倒进来。

## Canonical Stage Read-only Rule

Repair Cycle 从 `FINDINGS_FROZEN` 开始，到 Stage Reconciliation 前：

- Current Stage Contract：READ ONLY。
- Canonical Stage Execution Contract：READ ONLY。
- Product / Architecture authority：READ ONLY，除非上游正式重新冻结新版本。

任何中间修法、Task 重排、失败尝试、替代路径只存在 Repair Workspace。

## Stage Reconciliation Trigger

只有 Stage Verifier 输出：

`REPAIR VERIFIED`

才允许进入 Reconciliation。

在此之前不得“同步更新一下 Stage 文档”。

## Reconciliation Inputs

必须同时读取：

1. canonical Stage Execution Contract 原文；
2. Review Snapshot；
3. Repair Handoff；
4. Repair Execution；
5. Repair Evidence；
6. final Repository Reality；
7. 当前仍有效的 upstream Product / Architecture / Stage authority。

## Reconciliation Contract

Verifier 在 `REPAIR VERIFIED` 后冻结：

```text
Canonical Stage Document:
Reconciliation Basis:
Affected Sections / Tasks:
Final Effective State:
Superseded Content To Remove:
Preserved Unaffected Content:
Evidence To Retain:
Forbidden History / Narrative:
```

Construction Blueprint 执行一次性文档 reconciliation。

## Reconciliation Rules

- canonical Stage 只保留最终有效施工事实。
- 原计划中被 repair 失效的内容直接替换/删除。
- 未受影响范围保持有效，不做无关 rewrite。
- 不 append “原来怎么做 / 后来为什么错 / patch 1 / patch 2”的 repair chronology。
- 不保留 old/new 双版本、INVALIDATED task 墓地、supplement、临时 repair IDs。
- 最终文档仍必须符合 Construction Blueprint 正常 docs contract。

## Bounded Reconciliation Check

Reconciliation 后，Stage Verifier 只检查：

- Contract 指定的 affected sections 是否已反映 final Repository Reality；
- superseded content 是否消失；
- unaffected content 是否未被无授权改写；
- retained evidence / exit facts 是否一致。

禁止：

- 重新审代码；
- 新开 Finding 搜索；
- 再跑无关测试；
- 因 reconciliation wording 顺便做架构/代码优化。

通过：

`PASS — Stage Review Closed`

## Workspace Closure

最终 PASS 后：

- 默认删除 `.workbench/repairs/Stage-<N>/`；
- 不把 Repair Workspace 变成第三套长期事实源。

若项目有明确 audit / compliance retention obligation，可归档，但必须标记：

`CLOSED / NON-AUTHORITATIVE`

并且 canonical Product / Architecture / Stage docs 仍是唯一 active authority。

## Historical Frozen Stage

若 Repair Cycle 开始前该 Stage 已经是正式完成并冻结的历史 Stage：

> 不修改历史 Stage Execution Contract。

Route 到新的 maintenance / repair work unit，由上游工作流创建新的当前合同；历史事实保持不可变。

# Repair Blueprint Standard

> 本文件可独立使用：已有 Frozen Finding Set 时，可直接按本标准编译 Repair Blueprint；在 stage-verifier 流程中，由 `SKILL.md` 的「Repair Planning Pass」加载。

> Repair Blueprint 是 Frozen Finding Set 的施工合同，不是第二份长期 Stage Blueprint。

## 目的

把：

`Confirmed Findings + Upstream Authorities + Current Repository Reality`

编译成：

`Root-cause-correct Repair Tasks + Targeted Verification`

它必须与 Construction Blueprint 的 Task 颗粒度一致，但 Scope 更窄。

## 何时生成

生成：

- `FIX`
- `REPLAN_BLUEPRINT`，且 Product / Architecture / Stage Contract 仍正确

不生成：

- `PASS`
- `PRODUCT CHANGE`
- `REPLAN_ARCHITECTURE`（等待上游）
- 纯 `VERIFICATION BLOCKED`

## Authority

Repair Blueprint 重新读取：

- Product Definition
- binding Product Atoms
- Architecture / Engineering Standards
- Domain Ownership / Semantic Authority
- Stage Contract
- 原 Construction Blueprint
- Frozen Finding Set
- Repository Reality

优先级不变：

`Product → Architecture → Stage Contract → Repair Blueprint → Implementation`

Repair Blueprint 不得因为修复方便而改变上游。

## Root Cause First

不要：

```text
F-01 → Patch A
F-02 → Patch B
F-03 → Patch C
```

先问：

```text
这些 Finding 是否来自同一个错误 authority / owner / state flow / boundary？
```

如果是：

> 一次恢复正确结构，再清理所有症状。

### Root Cause Group

格式：

```text
Root Cause Group A

Findings:
- F-01
- F-03

Root Cause:
...

Correct Authority / Boundary:
...

Required System State:
...
```

Root Cause Group 只是输出分组，不是长期项目编号对象。

## Repair Target State

必须用可判真假的状态描述：

- 产品语义恢复。
- authority 唯一。
- owner mutation path 正确。
- direct bypass 消失。
- old path 删除。
- affected capability 重新成立。

不要写：

> 优化 Wallet 逻辑。

## Repair Scope

### Change Set

必须修改的现有 Path / Symbol / Schema / Test。

### Creation Set

只有根因修复确实需要时创建。

### Delete / Remove Set

被正确路径取代的：

- duplicate rule
- bypass
- old fallback
- alias
- dead test / fixture
- stale config

### Preservation / Direct Regression

修复不能破坏的直接既有行为。

### Explicit Non-Scope

Concern、future hardening、顺手重构明确排除。

## Repair Implementation Shape

```text
Touched Domains / Modules:
Ownership:
Required Reuse / Existing Authorities:
Allowed Dependencies:
Forbidden Bypasses:
State / Side-effect Flow:
Expected Repair Change Boundary:
Delete / Remove:
```

不适用字段省略。

## Repair Task

不创建新的长期 `Task-n`。

使用临时显示标签：

```text
### Repair Task 1 — <结果型名称>

Finding Coverage:
Upstream Basis:
Goal:
Implementation Constraints:
Prerequisites:
Targets:
Actions:
Operational Work:
Local Proof:
Expected Result:
Done When:
```

`Implementation Constraints` 仅在适用时写：

```text
Owner:
Use / Reuse:
Allowed Dependency:
Do Not Bypass:
Mutation / Side-effect Boundary:
```

### Task 粒度

太大：

> 修复所有架构问题。

太小：

> 删除一行 if。

合适：

> 将 Purchase 的余额扣减切回 Wallet.debit authority，移除 Purchase-local balance mutation 与重复 insufficient-balance 判断，并更新当前 caller/test。

## Dependency Graph

Repair Tasks 按真实依赖：

```text
Repair Task 1
  → Repair Task 2
  → affected Slice proof
```

只有真实独立时并行。

## Verification

### Local Proof

只证明 Repair Task。

### Affected Slice Capability Proof

只有 capability / binding Atom 被 Finding 破坏时需要。

### Finding Resolution Matrix

```text
| Finding | Repair Coverage | Proof | Resolved When |
|---|---|---|---|
| F-01 | Repair Task 1 | targeted test | no direct wallet write |
```

### Direct Regression

只测修复直接影响。

## Blueprint Finding

如果原 Blueprint 本身错：

Repair Blueprint 可以局部替代受影响的：

- Implementation Shape
- Task grouping
- Targets
- Actions
- Dependency order
- Verification

但不能改变：

- Product semantics
- Architecture authority
- Stage Scope / Exit State

需要改变这些时，停止并升级。

## Delete Means Absence

根因修复如果“正确路径替换错误路径”，Repair Blueprint 必须显式列 `Delete / Remove Set`。

不要留下：

- deprecated old path
- fallback for just in case
- duplicate authority
- commented implementation
- obsolete test

除非上游明确有 compatibility / migration / audit 责任。

## Stop Rule

修复停止在：

- Frozen Findings resolved
- direct regression clear
- affected semantic capability proven
- old path cleaned
- no new upstream decision required

不继续把 Concerns、未来风险、无关 code smells 拉进修复。

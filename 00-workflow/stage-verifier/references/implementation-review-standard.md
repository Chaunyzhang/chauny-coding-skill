# Implementation Review Standard

> 本文件可独立使用：可直接对任意改动做实现质量审查；在 stage-verifier 流程中，由 `SKILL.md` 的「3. Implementation Quality」章节加载。

这是 Stage Verifier 的实现质量判定方法。

目标不是审美，而是：

> 确认当前改动既正确，也没有把项目结构向更难维护的方向推。

## 1. Correctness

### 必查

- 输入条件与边界。
- output / mutation target。
- identity。
- state transition。
- ordering。
- error mapping。
- data integrity。
- permission / ownership。
- concurrency / idempotency（实际触发时）。
- resource lifecycle（实际触发时）。

### 强 Finding

- 当前有效路径可证明返回错误结果。
- mutation wrong object。
- error swallowed as success / empty state。
- invalid state transition。
- confirmed race / double write / double charge。
- missing transaction where current invariant requires atomicity。

## 2. Work Efficiency

### Work Inventory

有真实成本疑问时列：

```text
DB Read:
DB Write:
External Call:
Collection Pass:
Serialization:
State Mutation:
Transaction / Lock:
```

问：

> 每一个额外工作是否有必要？

### 常见 defect

- N+1。
- duplicate fetch。
- repeated parse / serialization。
- full scan when indexed lookup exists。
- per-item remote call when batch exists。
- needless sequential latency。
- long transaction around network I/O。
- repeated state write。
- bypass canonical cache / batch / index。

### 非目标

- micro benchmark。
- 为理论 scale 提前优化。
- 没有 current evidence 的 premature caching。

## 3. Semantic Unity

### Authority Test

对于每条 Current Stage 核心规则：

```text
Rule:
Canonical Authority:
Actual Decision Sites:
```

若 `Actual Independent Decision Sites > 1`：

检查是否：

- projection / display / cache（允许）
- independent rule implementation（FAIL）

### Change Test

问：

> 明天这条业务规则改变，要修改几个独立决定点？

理想：

`1 authority + mechanical callers`

危险：

`多个互不依赖的判断点`

## 4. Modular Integrity

### Ownership Test

每个新增核心行为都应回答：

- Owner Domain
- Public Entry
- Internal State
- Dependencies

回答不出来是强 smell。

### Boundary Test

检查：

- internal import。
- raw DB bypass。
- cross-feature direct mutation。
- Shared dumping。
- dependency cycle。
- public API leakage。

### Change Locality Test

问：

> 一个正常产品变化主要会不会留在 owning domain？

如果多个无关 domain 必须理解同一业务事实，查 authority / boundary。

### Removal Test

只作为 sensor：

> 删除这个 Feature，理论上主要应删除其 own module + 少量 callers。

若大量无关区域持有其内部知识，说明耦合过高。

## 5. Structural Health

### Placement

逻辑的层级应与责任匹配：

- UI：表现 / interaction orchestration
- Application：use case orchestration
- Domain：business rules / state semantics
- Data / Infrastructure：persistence / transport / external adapter

具体项目以 Architect standards 为准。

### Side Effect Visibility

副作用应能从：

- function / type role
- call path
- boundary

看出来。

不要在纯 mapper / getter 名字下写 DB / network / event。

### Interface Health

新 public surface 必须有当前真实 consumer 或已批准 architecture reason。

暴露内部数据结构只为“方便调用”是 smell。

## 6. Maintainability

### Naming

名字表达 domain intent，而不是：

- `Manager`
- `Helper`
- `Utils`
- `handleData`
- `processThing`

这些词不是自动错误；如果掩盖真实 responsibility 才是问题。

### Complexity

数字只是 sensor：

- long function
- deep nesting
- many params
- high cyclomatic complexity

真正 Finding 要证明：

- 多责任。
- 控制流难理解。
- change risk。
- duplicated branch semantics。
- hidden side effect。

### Abstraction

抽象必须回答：

> 当前什么真实变化需要这个边界？

没有第二实现、没有 architecture extension point、没有真实复用语义时，不因为“未来可能”创建复杂 hierarchy。

### Testability

核心规则应能以与风险匹配的成本验证。

差测试：

- 只 assert mock called。
- 复制 production implementation。
- 对 framework internals 过度耦合。

好测试：

- proof of behavior / state / contract。

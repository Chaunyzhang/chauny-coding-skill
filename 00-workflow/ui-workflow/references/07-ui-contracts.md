# UI 契约：设计与实现的共同定义

**何时加载**：重要 Surface / Component、异步动作、permission、复杂状态、设计交给实现、或实现需要确认 UI 语义时。

**目标**：消除“设计稿看得见，但数据/状态/函数怎么接没人说清楚”的缝。

## Surface Contract

按任务需要记录：

```text
Surface
- purpose
- primary object / action
- content structure + bounds
- hierarchy
- regions / sections / patterns / components
- page composition
- relevant states
- interaction / feedback / recovery
- adaptation / accessibility
- visual direction applied
- implementation mapping
- verification scenarios
```

## Component Contract

按任务需要记录：

```text
Component
- purpose
- anatomy / slots
- content constraints
- variants
- states
- events
- feedback / recovery
- layout / visual rules
- adaptation / accessibility / motion
- data / action mapping
```

## Decision-bearing data field

任何影响 permission、lifecycle、route、availability、approval 等 UI 决策的字段，应明确：

```text
meaning
allowed values
producer
owner/cache
consumer
UI projection
forbidden inference
```

UI 可以 derive presentation state，但不能从显示文本或颜色创造业务真相。

## Implementation Mapping

重要交互至少能追踪：

```text
UI element
→ displayed data
→ state source
→ state owner
→ user event
→ command/action
→ pending representation
→ success representation
→ failure representation
→ recovery
```

## Contract 完整性的判断

实现者不应该还需要猜：

- 这个状态从哪来。
- 谁能改它。
- 点击后调用什么语义动作。
- pending 时能否重复操作。
- success / failure 如何映回 UI。
- error 后如何恢复。
- long/empty/permission 如何表现。

## 停止条件

当 UI 和真实系统之间的关键映射已经显式，且不再依赖口头翻译或“实现时再决定”时停止。

---

## Contract 必须写回 UI-DESIGN-SPEC.md

Contract 不作为另一份平行 handoff 文档存在。对当前 UI 真正影响显示和行为的内容，应收束进 `UI-DESIGN-SPEC.md` 的：

- Page States。
- Component States。
- State & Interaction Rules。
- Implementation Mapping。

这样实现者只有一个设计权威来源，不需要在视觉稿、散文 handoff、状态文档之间人工翻译。

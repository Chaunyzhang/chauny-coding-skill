# UI 完整性扫描

**何时加载**：任何 UI 任务开始时快速扫描；不是要求逐项详细执行。

**怎么用**：每项只标 `Relevant / Existing / N/A`。如果是 `Relevant`，再加载对应 reference。

## 1. 产品与语义
- 用户 / actor
- 用户目标 / task
- 核心对象
- 主要动作 / 次要动作
- 产品约束
- permission / ownership 语义

## 2. 内容
- 字段、对象、集合
- required / optional
- 数量范围
- 最小 / 常见 / 最大长度
- missing / unknown / invalid
- wrap / truncate / overflow
- empty / large dataset
- labels / errors / empty copy

## 3. IA / Navigation
- grouping / ordering
- parent-child
- entry / exit
- current location
- back / deep link / selection
- progressive disclosure

## 4. Hierarchy
- task hierarchy
- object hierarchy
- information hierarchy
- action hierarchy
- visual hierarchy
- navigation hierarchy

## 5. Composition / Component
- Flow / Surface / Region / Section / Pattern / Component / Primitive
- anatomy / slot / metadata / control / action ownership
- flat vs container strategy

## 6. State
- domain
- data: loading / ready / empty / stale / partial / error
- operation: idle / pending / success / failed / retrying
- permission: allowed / denied / readonly / unavailable
- interaction: enabled / hover / focus / pressed / dragged / disabled
- selection / navigation / environment / presentation
- state composition

## 7. Interaction / Feedback
- affordance / input modality / gesture
- precondition / event / command
- confirmation / undo / retry / cancel
- pending / progress / success / failure / warning
- recovery path

## 8. Layout / Adaptation
- flow / alignment / grid / containment
- whitespace / density
- scroll / sticky / fixed / overlay
- safe area / clipping
- viewport / orientation / device class
- pointer / touch / keyboard
- dark / high contrast / text scaling / zoom / RTL / localization

## 9. Visual Language
- Human intent
- Primary / Secondary / Micro / Avoid
- reference extraction
- composition logic
- typography / color / shape / surface / depth
- spacing / density / icon / imagery / motion
- coherence / drift

## 10. System / Reuse
- semantic tokens
- primitives
- components
- patterns
- variants
- themes
- shared state rules

## 11. Implementation Mapping
- UI object ↔ content/domain object
- UI state ↔ source/owner
- UI event ↔ command
- property ↔ view model/data
- pending/result/error ↔ visible feedback
- recovery ↔ available action

## 12. Verification
- normal / empty / loading / error
- permission / unavailable
- offline / stale
- long / missing / many items
- small / large viewport
- focus / hover / pressed / disabled / selected
- keyboard / touch / pointer
- reduced motion / contrast / text scaling
- localization / RTL
- real rendered evidence

## 停止条件

Coverage 扫描完成后，应能说明：本次真正需要深入的模块有哪些，哪些已有可复用，哪些明确不适用。不得把“没想到”伪装成 `N/A`。

# UI 完整性扫描

**何时加载**：任何 UI 任务开始时快速扫描；不是要求逐项详细执行。

**怎么用**：每项只标 `Relevant / Existing / N/A`。如果是 `Relevant`，再加载对应 reference。

## 0. Route / Scope

- 当前是 micro patch / component / page / multi-page / full product / implementation-only / refactor 哪一类？
- 能完整解决问题的最小路径是什么？
- 哪些风险会触发升级？
- 最终需要 Full Spec / Page Spec / Patch Spec 哪一种？


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

## 9. Image Evidence（有截图/设计稿时）
- source scope：单页 / 多页 / 多状态 / 多 breakpoint
- 重要产品/代码/图片/设计判断的 Observed / Resolved / Unknown 是否分开
- structure / hierarchy / composition 是否可逆向
- typography / color / spacing / radius / surface / icon / imagery 是否可提取
- 可见 component / state 是否有重复证据
- motion / responsive / hidden state / business truth 是否缺证据
- Style DNA 与源产品业务/品牌特征是否分离

## 10. Visual Language
- Human intent
- Primary / Secondary / Micro / Avoid
- reference extraction
- composition logic
- typography / color / shape / surface / depth
- spacing / density / icon / imagery / motion
- coherence / drift

## 11. System / Reuse
- semantic tokens
- primitives
- components
- patterns
- variants
- themes
- shared state rules

## 12. Implementation Mapping
- UI object ↔ content/domain object
- UI state ↔ source/owner
- UI event ↔ command
- property ↔ view model/data
- pending/result/error ↔ visible feedback
- recovery ↔ available action


## 13. Implementation Structure（包含代码且非平凡时）
- repo / feature tree 是否需要画出
- shared vs page-local
- state / data / mutation owner
- navigation owner
- repeated UI / collection renderer
- tokens / icons / assets 单一来源
- duplicated markup / logic / fixtures 风险
- 新增下一个同类页面是否需要 copy-paste

## 14. Verification
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

## 15. Design Spec Compilation
- Visual Laws 是否已形成
- composition grammar 是否具体
- typography roles 是否有确定值/系统语义
- color roles 是否有确定值/系统语义
- spacing scale 与关键 gap 是否确定
- radius / border / surface / shadow 是否确定
- icon / imagery / motion 是否确定
- 关键 component grammar 是否确定
- 每个 Relevant Page 是否有独立 Page Spec
- states / interaction / feedback 是否写入同一规格
- adaptation / accessibility 是否具体
- forbidden / guardrails 是否具体
- Global + Page implementation prompts 是否生成
- 是否仍有需要实现者二次设计的模糊项

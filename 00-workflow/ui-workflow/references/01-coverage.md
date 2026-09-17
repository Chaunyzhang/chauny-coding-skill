# UI Coverage：防漏，不是固定流程

使用方式：每项标 `Relevant / Existing / N/A`。只展开 Relevant；不得留空靠“没想到”跳过。

## 1. Reality / Scope
- 用户与核心任务
- 核心对象、主/次动作
- 平台、设备、repo、现有 UI / Design System
- 不能擅改的产品/架构/权限事实
- 任务粒度：Full / Page / Patch / Component / Implementation-only

## 2. Evidence / Human
- 关键结论是否标 Observed / Resolved / Unknown
- 是否存在 Human 模糊感受需要先翻译并确认
- 是否有参考图；证据是单图、多图还是多 breakpoint

## 3. Content / IA
- 字段、集合、required/optional
- 数量范围、长度范围、缺失、极值、overflow
- 分组、排序、导航、空态
- microcopy / error / CTA 是否需要定义

## 4. Hierarchy / Composition
- primary task / object / action / information
- visual focal order
- Surface / Region / Section / Pattern / Component
- alignment axis、container strategy、scroll ownership

## 5. State / Interaction / Feedback
- domain / data / operation / permission / environment / interaction state
- owner、entry/exit condition、allowed actions
- event → command → pending → success/failure → recovery
- loading/progress/optimistic/undo/retry/cancel

## 6. Visual System
- Visual Laws
- composition grammar
- typography / spacing / density / color / shape / surface / depth
- icon / imagery / motion
- Visual Math scale 与 Craft Floor
- Forbidden / Avoid

## 7. System / Reuse
- token / primitive / component / pattern
- variants 与 states
- shared vs local
- icon / asset / formatter / renderer 单一来源

## 8. Adaptation / Accessibility
- viewport / orientation / window / safe area
- keyboard / pointer / touch / focus
- text scaling / zoom / RTL / localization
- contrast / target size / reduced motion

## 9. Implementation Mapping
- UI element → data/view model
- state source / owner
- event → action/command
- pending/result/recovery
- navigation / mutation ownership

## 10. Verification
- rendered states
- content stress
- component state proof（适用时）
- structure audit
- drift audit
- Human visual review

## 停止条件
已选最小合法路径；所有 Relevant 项都有明确决定、Existing 来源或明确 Unknown；没有需要用户继续充当 linter 的空白。


## 视觉秩序快速检查

完整 Surface 若 Relevant，至少检查：主焦点、主对齐轴、组内/组间距离、辅助信息弱化、容器数量、数字/状态/文本列对齐。发现问题进入 `03-visual-design.md`，不要用配色掩盖。

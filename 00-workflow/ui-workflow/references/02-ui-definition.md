# UI 定义：结构、内容、状态、交互、适配

目的：在视觉前把“这个界面是什么、装什么、怎么行为”定义到实现不必猜。

## 1. Content Structure

每个重要内容对象至少定义：

```text
field / collection
required | optional
cardinality
normal range
stress range
format
missing/empty behavior
overflow/wrap/truncate/reflow
```

不要围绕一条漂亮假数据设计。真实长度与数量是 Layout 输入。

## 2. Hierarchy

分开判断：
- Task hierarchy：用户最重要的任务。
- Object hierarchy：页面围绕什么对象。
- Action hierarchy：primary / secondary / tertiary。
- Information hierarchy：先看什么、后看什么。
- Visual hierarchy：最终怎么表达以上关系。

视觉不能反过来发明产品层级。

## 3. Composition vocabulary

按需要使用：

`Flow → Surface/Screen → Region → Section → Pattern → Component → Primitive`

- Region：有独立布局 ownership 的大区域。
- Section：语义内容组。
- Pattern：可重复交互组合，如 Search+Filter、Empty State、Confirmation。
- Component：有独立语义、复用、状态/交互或稳定规则的单元。

## 4. State 是组合，不是单一 enum

常见维度：
- Domain：draft / active / completed …
- Data：loading / loaded / empty / stale / partial / error
- Operation：idle / submitting / failed / retrying
- Permission：allowed / denied / readOnly
- Environment：online / offline / reconnecting
- Interaction：enabled / hover / focus / pressed / dragged / disabled
- Selection / Navigation / Presentation

多个维度可同时成立，例如 `completed + offline + syncPending + focused`。

每个重要状态回答：source、owner、entry、exit、visible representation、allowed actions、feedback、recovery。

## 5. Interaction closure

重要动作必须闭环：

`affordance → event → intent → precondition → command → immediate response → pending → success/failure → recovery`

不要用“点击后完成任务”代替真实交互定义。

## 6. Feedback 先定语义

先回答：
- 现在是什么状态？
- 动作是否仍在进行？
- 成功还是失败？
- 是否有危险后果？
- 如何纠正 / retry / undo？

再决定 inline state、progress、toast、banner、dialog 等形式。不要默认“加个 toast”。

## 7. 时间行为

根据真实任务判断：latency、progress、optimistic update、debounce、timeout、staleness、realtime update、cancel/interruption。

静态图不能证明 timing；复杂时间行为需要最小 State Proof。

## 8. Layout / Adaptation

至少明确：
- 主轴、grid/flow、alignment、containment
- fixed/sticky/overlay 与 scroll owner
- content width、safe area
- viewport/window/orientation 变化
- long text / text scaling / localization / RTL

Responsive 不是“desktop/tablet/mobile 三张图”，而是内容与交互在环境变化下的规则。

## 9. Accessibility 横切

相关控制必须覆盖：
- semantic role / label
- keyboard / focus order / focus return
- touch target
- contrast 与非颜色单一通道
- text scaling / zoom / reflow
- reduced motion
- dragging 的替代操作（适用时）
- status/error 可被辅助技术感知

## 输出

把 Relevant 结果写入 Full/Page/Patch Spec 的：Content、Hierarchy、Structure、States、Interaction、Adaptation、Accessibility 部分。

## 停止条件
实现者不需要临场猜内容边界、状态来源、用户动作结果、布局 owner 或关键适配行为。

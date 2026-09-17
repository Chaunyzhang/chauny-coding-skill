# Human Alignment 与设计变更控制

**何时加载**：任何会新增或改变 Human 可感知的 UI 设计决定、交互行为、动效、页面结构、视觉规则、状态表现或不变量的任务。

**目标**：Human 可以只描述“感觉”和结果；Agent 负责把模糊表达翻译成精确、可观察、可实现的候选设计决定。候选决定必须先让 Human 确认，再进入权威 Spec，最后才进入生产代码。

核心顺序只有一条：

`Clarify → Confirm → Specify → Implement → Verify`

不得用“先写出来看看”代替设计对齐，也不得把代码已经实现的行为倒灌成未经确认的新设计事实。

---

## 1. Clarify：把感觉翻译成可观察决定

Human 不需要会说 FLIP、easing、layout ownership、state machine 或 token。

Human 可以只说：

> “这里太跳了，我想顺一点，但别飘。”

Agent 的工作是把它翻译成 Human 能确认的精确候选：

```text
Human intent (Observed)
- 当前位置变化太突兀。
- 希望有连续感，但不要弹跳、漂浮或拖泥带水。

Candidate interpretation
- 其他 item 从旧位置连续移动到新位置，不瞬移。
- 当前被拖拽 item 保持跟手，不参与补间。
- 动画只表达位置连续性，不增加额外表演。
- 不使用 overshoot / bounce。
- 建议 structural transition 220–260ms，最终值 240ms。

Preserved
- 拖拽手势、drop 规则、网格顺序语义不变。

Observable result
- 放入/移出时邻居平滑让位；最终位置不抖、不残留位移。

Unknown / conflict
- 若后台切换会影响动画清理，需要实现层选不会依赖后台 rAF 的可靠结束机制。
```

重点是描述**屏幕上会发生什么、不会发生什么、哪些东西保持不变**。技术实现细节只有在会改变 Human 体验或约束时才需要暴露给 Human。

---

## 2. Confirm：Human 确认设计决定，不确认实现术语

以下情况视为已经确认，不要重复问：

- Human 已经给出足够精确的设计规则或具体数值。
- Human 明确说“就按这个”“对，就是这样”“照这个做”。
- 当前行为已经存在于 Human 批准的 `UI-DESIGN-SPEC.md`，任务只是实现。
- Human 明确把某个设计范围委托给 Agent 决定，例如“这块你按现有设计语言定，直接做”。此时 Agent 可以 Resolve，但必须把决定写进 Spec，不能留在代码里。

以下情况必须先确认：

- Human 只给了模糊感受，Agent 要把它变成新的视觉/交互规则。
- Agent 主动提出改变 layout、motion、state presentation、component behavior、hierarchy 或 visual language。
- 现有 Spec 有冲突，需要选择哪个方向成为新的设计事实。
- 图片/参考无法证明某个行为，但目标 UI 必须补一个新的设计决定。

### 不要做 Confirmation Theater

不要每个 token、每个 1px 都问一次。

把同一问题下的相关决定打包成一个**Decision Alignment Block**，一次让 Human 确认主旨和关键边界；数值若只是已确认方向下的实现化细化，可由 Agent按当前 Design System 落定并写入 Spec。

---

## 3. Decision Alignment Block

需要 Human 对齐时，优先用短而精确的格式：

```text
我理解你要的是：
- <核心结果>

屏幕上会变成：
- <可观察变化 1>
- <可观察变化 2>

保持不变：
- <已有规则/行为>

我准备定成：
- <关键规则/数值/边界>

还不确定：
- <真正需要 Human 裁决的点；没有则省略>
```

Human 可以直接：
- 确认；
- 改其中一条；
- 指定 Avoid；
- 把某个选择委托给 Agent。

确认以前，这些只是 **Candidate Decisions**，不是权威 Spec，也不是代码事实。

---

## 4. Specify：确认后先改 Spec

Human 确认后，下一步必须先创建或更新对应的：

- `Full Spec`；
- `Page Spec`；或
- `Patch Spec`。

Spec 里写入最终可执行规则，再进入实现。

### Spec-before-Code Rule

只要会改变任何 Human 可感知设计决定，顺序必须是：

`Human confirmed decision → Spec diff → Code diff`

禁止：

`Code diff → 试试看 → Spec backfill`

因为一旦代码先成为事实，Spec 就从“权威来源”退化成“事后记录”。

---

## 5. Implement：实现只消费已经确认的设计事实

实现 Agent 可以自行决定**不改变可观察契约**的技术细节，例如：

- helper/function 如何拆；
- 用哪种内部数据结构；
- transition completion 用何种可靠机制；
- 文件内部私有命名；
- 不改变行为的性能优化。

但实现过程中如果发现必须新增/改变以下任何内容：

- UI 可见结果；
- interaction rule；
- motion timing/behavior；
- state presentation；
- page/component structure；
- design token / visual rule；
- 用户可感知的不变量；

必须**停下实现**，回到 `Clarify → Confirm → Specify`，不能把新决定偷偷写进代码。

### 纯实现重构例外

如果改动同时满足：

- rendered result 不变；
- observable interaction/behavior 不变；
- state/data/business contract 不变；
- Design System 与 Spec 不变；

则无需重新向 Human 确认，也无需伪造一个 Design Spec 变化。

例如：去重复、抽 helper、修内存泄漏、替换不可靠清理机制但保持视觉行为完全一致。

禁止借“重构”顺便做未确认的视觉优化。

---

## 6. Verify：验证的不只是代码，而是 Human 已确认的决定

Rendered Verification 时必须能追溯：

`Human intent → Confirmed decision → Spec rule → Code → Rendered result`

如果最终看起来仍“不对”，不要直接在代码里微调到顺眼；回到 Alignment，把新的 Human 反馈再次精确翻译、确认、更新 Spec，然后再改实现。

这保证 Human feedback 不会被消耗成一次性的代码 tweak，而会成为长期设计语言的一部分。

---

## 7. Spec-Code Sync Gate

任何设计相关代码改动交付前检查：

```text
[ ] 本次代码是否改变可观察 UI？
[ ] 是否改变 token / 数值 / component treatment？
[ ] 是否改变 state / transition / interaction？
[ ] 是否改变 motion？
[ ] 是否新增或改变用户可感知不变量？
[ ] 是否改变 page/component structure？
```

若任一为 `Yes`：

- 必须有对应的 Human 已确认决定；
- 必须先有对应 Spec diff；
- Code 必须与最新 Spec 一致。

若没有 Spec diff，默认 **Fail**，除非可以证明这是纯实现重构且可观察结果完全不变。

---

## 8. 并行 Agent 协作

多个 Agent 同时修改同一产品时，不能各自在代码里创造设计事实。

必须有明确的 Spec ownership：

- 同一 Surface / Component / State Contract 的设计事实只能有一个权威 Spec owner。
- 非 owner Agent 发现需要新的 Human 可感知决定时，先提交 `Candidate Spec Delta`，不得先在自己的分支把它做成既成事实。
- Human 确认后，由 owner 合并 Spec；随后相关 Agent 再按最新 Spec 实现。
- 并行实现可以独立进行，但都必须消费同一版本的权威 Spec。

如果两条实现线产生冲突，先解决 Spec/ownership 冲突，再合代码；禁止“谁先写完谁成为真相”。

---

## 9. 停止条件

进入生产实现前，应满足：

- Human intent 已经被翻译成足够精确的可观察决定；
- 真正需要 Human 裁决的点已经确认，或 Human 已明确授权 Agent 在限定范围内决定；
- 已确认决定已经进入对应 Spec；
- 实现者不需要再猜 Human 的感觉；
- 没有“先代码、后补文档”的设计债。

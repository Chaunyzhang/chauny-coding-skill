# 结构、内容、层级与布局

**何时加载**：新建 Surface、重做页面结构、内容变化会影响 UI、或现有层级/布局不清时。

**目标**：先把“界面承载什么、谁重要、怎么组织”说清楚，再决定视觉皮肤。

## 内容结构

不要只记录最终文案，要记录内容的形状：

- 字段是什么。
- required / optional。
- 数量和长度范围。
- 缺失、未知、无效时怎么办。
- 超长时 wrap / truncate / expand / scroll 哪个成立。
- 空集合、大集合、极端值是否改变结构。

示例：

```text
Task
- title: required, 1–2 lines preferred
- note: optional, may be absent
- due: optional
- labels: 0..N
```

## 信息与动作层级

先区分：

- 用户最主要任务。
- 当前 Surface 的主要对象。
- 主要信息。
- 主要动作。
- 次要 / 辅助 / 危险动作。

不要因为某个元素是 Button 就自动让它成为视觉中心。

## 组合层级

按实际语义使用：

`Flow → Surface → Region → Section → Pattern → Component → Primitive`

它们是理解边界，不要求一一映射成代码文件。

- Region：拥有明显 layout / scroll / persistence 责任的大区域。
- Section：语义内容组。
- Pattern：重复出现的交互组合，如 search+filter、empty+CTA、confirmation。
- Component：有独立语义、状态、交互、视觉规则或真实复用价值的单元。

## Layout 决策

完整页面至少明确：

- 主轴和阅读顺序。
- 对齐逻辑。
- 分组依靠 spacing、surface、border 还是 container。
- 哪些区域固定、滚动、sticky、overlay。
- 谁拥有 padding / gap / safe area。
- 小屏、宽屏、窗口变化时是缩放、换行、重排、折叠还是隐藏。

Spacing 是 layout 参数，不是 layout 本身。

## 页面结构失真信号

以下通常说明该回到结构而不是继续调像素：

- 每个 section 都被做成 card。
- 主要内容和辅助工具同权。
- 需要大量 magic offset 才能成立。
- 新增真实内容后页面立刻崩。
- 页面只有“标题 + 一堆盒子”，无法说明信息关系。

## 产出

根据任务规模，产出可以是简短结构说明，也可以是 Surface 级定义。至少要让后续视觉设计知道：内容范围、层级、区域、组件边界、滚动/布局 ownership。

## 停止条件

当后续设计不需要靠猜测回答“这里装什么、谁最重要、为什么分成这些块、超长/为空怎么办”时停止。

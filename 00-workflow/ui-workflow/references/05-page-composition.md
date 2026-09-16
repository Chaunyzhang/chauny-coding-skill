# 页面构图

**何时加载**：完整 Screen / Surface、新页面、重做页面布局，或视觉属性已经明确但页面仍“不知道怎么排”时。

> 识图任务：优先使用 `14-image-style-reverse-engineering.md` 中的 Page Reverse Spec、alignment axis、gutter、section rhythm 和 container evidence；不要在构图阶段重新发明与图片证据冲突的结构。

**目标**：把内容、层级、行为和视觉语言合成一个具体页面方案。

## 必须决定

- Focal order：第一眼、第二眼、辅助信息分别是什么。
- Page flow：用户视线和操作如何向下/横向推进。
- Grouping：靠 spacing、surface、divider、container 还是 typography 分组。
- Container strategy：哪些必须成容器，哪些保持 flat。
- Action placement：主要动作、次要动作、危险动作分别在哪里。
- Scroll ownership：谁滚动，谁固定，谁 sticky，谁 overlay。
- Density：同组内部与组间节奏如何区分。
- Adaptation：窄屏、宽屏、横竖屏或窗口变化时如何重排。
- Visual direction applied：视觉语言具体在哪些构图决策上生效。

## 推荐输出

```text
<Surface> Composition

Focal order:
1. ...
2. ...
3. ...

Page flow:
...

Grouping / containers:
...

Primary / secondary actions:
...

Scroll / persistence:
...

Density rhythm:
...

Adaptation:
...

Visual direction applied:
...
```

## 规则

- 先表达上游 hierarchy，再追求视觉新鲜感。
- 完整页面不能由“一堆 Card”代替结构判断。
- Primary action 重要不等于必须最大最亮；它要服从 task/object hierarchy。
- 同组内部应比组间更紧密。
- 视觉方向要影响布局，不只影响皮肤。
- 如果页面只有 color/radius/type 结论，没有 focal order 和 flow，构图尚未完成。

## 停止条件

当设计者和实现者都能从构图说明理解：页面首先看什么、如何分组、动作放哪、哪些区域滚动/固定、不同尺寸怎么变化时停止。

---

## Page Spec 必须具体化

构图结论必须进入 `UI-DESIGN-SPEC.md` 的逐页面规格，而不是停在描述。

对于 Relevant Page，明确到实现者无需再决定：

- exact structure / section order。
- content width / grid / columns。
- page gutter。
- top / bottom inset。
- section before/after spacing。
- row/item gap。
- alignment axis。
- container/surface/divider strategy。
- primary/secondary action placement。
- scroll/sticky/fixed/overlay ownership。
- responsive reflow。
- page states 和 content stress。

如果某个 gap、max-width、min-height、column width 会明显改变页面观感，就在 Page Spec 中给出确切值或已命名 token，不留给实现者“按感觉调”。

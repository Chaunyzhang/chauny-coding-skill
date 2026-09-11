# Design Language

设计语言的任务，是把“感觉”变成可控制变量。

## Personality

Personality 是高层方向，通常 4–7 个词足够。

常见轴：

- Calm ↔ Energetic
- Warm ↔ Cool
- Restrained ↔ Expressive
- Organic ↔ Geometric
- Tool ↔ Companion / World
- Sparse ↔ Dense
- Mature ↔ Playful
- Precise ↔ Soft
- Flat ↔ Layered

不要求所有轴都选。

必须同时记录少量 Avoid，防止 Agent 用错误捷径实现同一个形容词。

## Grammar

### Hierarchy

决定：
- Primary / Secondary / Supporting
- 哪个对象在视觉上拥有 Screen
- Primary action 是否唯一
- 视觉对比如何集中

“高级”往往来自清楚的退让关系，而不是更多装饰。

### Density

控制：
- 每屏信息量
- Section 数量
- control compactness
- whitespace
- text density
- visual noise

Density 是产品性格，不只是 spacing 数值。

### Spacing Rhythm

Spacing 表达关系：

- intra-element
- tight group
- component internal
- component-to-component
- section separation
- screen region

重复关系必须复用同一种节奏。

### Shape

定义：
- radius character
- edge hardness
- capsule usage
- organic vs geometric
- container boundary strength

避免“想柔和 = 所有东西大圆角”。

### Surface

控制：
- flat vs elevated
- border strength
- shadow discipline
- blur / glass scope
- background / surface / elevated surface

Decoration 必须服从 hierarchy。

### Typography

定义语义角色：

- display
- title
- headline
- body
- caption
- number / metric
- label

重点是权重关系、节奏和性格，不是堆字号。

### Color

优先语义：

- background
- surface
- text primary / secondary
- accent
- destructive
- warning
- success

控制：
- accent 使用量
- saturation
- contrast
- dark appearance behavior
- semantic state independence from raw colors

### Icon

统一：
- outline / fill
- weight
- optical size
- active / inactive
- custom vs system
- illustration / emoji 是否允许

### Motion

定义：
- immediate response
- speed
- weight
- settle
- overshoot
- state continuity
- spatial continuity
- interruption

Motion 是产品性格的一部分。

### Interaction

定义：
- direct manipulation vs confirmation
- optimistic vs wait
- undo vs modal confirmation
- success visibility
- inline vs modal error
- long operation feedback

### Navigation

统一：
- primary navigation
- push
- sheet
- full-screen
- overlay
- popover
- destructive confirmation

每个 Screen 不得自行发明导航语言。

### State

重要 Component / Screen 按真实需要覆盖：

- loading
- empty
- populated
- disabled
- selected
- error
- success
- offline / unavailable
- long content

不为理论完整添加无关状态。

## Personality → Grammar 例子

用户说：

“有生命感、温暖、有陪伴感，但不要儿童游戏。”

可能编译为：

```text
Density:
lower, more breathing room

Shape:
soft, rounded, not universally pill-shaped

Color:
warm neutrals + restrained accent

Surface:
quiet surfaces, low border noise

Typography:
clear and mature, not cute

Icon:
coherent, simple, no emoji mixing

Motion:
immediate response + soft settle + low overshoot

Interaction:
gentle feedback, low interruption

Avoid:
rainbow saturation, exaggerated bounce, heavy gamification chrome
```

这是推导，不是固定模板。

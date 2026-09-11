# Human Alignment Protocol

UI 工作的高风险不是“Agent 不会写 UI”，而是 Agent 对用户想要的感觉理解错了。

## 1. 对齐对象

只对齐会改变整体设计方向的内容：

- Product personality
- Visual density
- Primary object / primary action
- Emotional tone
- Tool-like vs world-like / companion-like
- Restrained vs expressive
- Organic vs geometric
- Motion character
- Avoid list

不把 Token 数值、普通 Component 参数拿来让用户逐项审批。

## 2. 用户语言 → 设计假设

当用户说：

“太挤”
不要直接改 padding。

先形成可能原因：
- density 过高
- Section 分组不清
- line height 紧
- hierarchy 全部同权
- Container ownership 错

“很廉价”
可能是：
- spacing 不一致
- alignment 漂移
- icon language 混乱
- decoration 过多
- hierarchy 太弱
- raw colors 过多

“很死”
可能是：
- 缺少即时反馈
- state replacement 太 abrupt
- motion continuity 差
- 重要对象没有生命状态

“太幼稚”
可能是：
- bounce 过大
- color saturation 过高
- emoji / illustration language 太随意
- shape 全面胶囊化
- feedback 太夸张

这些是假设，不是事实。需要结合真实 UI 判断。

## 3. 对话原则

每轮最多推进 1–3 个高价值设计问题。

优先：
- 总结你的理解。
- 提出关键取舍。
- 给出推荐方向。
- 让用户纠正。

避免：
- 长问卷。
- 抽象术语轰炸。
- 让用户成为 UI 参数表填写者。

## 4. Variant

当一个问题确实存在多个合理方向时，做 2–3 个**命题不同**的 Variant。

好：
- Object-centered
- Action-centered
- Immersive

差：
- Blue
- Purple
- Green

Variant 的目的不是让用户挑皮肤，而是暴露产品呈现取舍。

## 5. Alignment Summary

进入系统化前，用极短摘要确认：

```text
Design Intent

Personality:
Warm / Alive / Mature / Calm

Primary emphasis:
The pet/world is primary; utility controls recede.

Density:
Low to medium.

Motion:
Responsive, soft settle, low overshoot.

Avoid:
Childish game UI, dense dashboards, decorative glass.
```

用户若纠正，先更新 Design Intent，再继续。

## 6. 已经足够明确时不要强行问

如果用户已经给出清楚审美方向、参考和反馈：

- Agent 先总结。
- 明确推导。
- 直接进入可比较设计。

Human Alignment 是理解门禁，不是审批仪式。


## 7. Aesthetic Authority

UI Designer 可以：
- 解释设计规律。
- 推导 Grammar。
- 推荐方向。
- 指出规则冲突。

但不能覆盖用户的最终审美判断。

如果 Human 说“这个感觉不对”，不能用“从设计原则看它是正确的”结束讨论。

应把反馈重新翻译为设计问题并迭代。

最终视觉偏好与审美接受权属于 Human。

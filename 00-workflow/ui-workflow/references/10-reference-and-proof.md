# 参考分析与交互验证

## A. Reference Analysis

**何时加载**：用户提供产品、Moodboard、竞品或明确参考对象。若用户提供的是 UI 截图/设计稿并要求逆向或复刻视觉风格，改用 `14-image-style-reverse-engineering.md`；本模块只保留高层参考原则提取。

目标不是“做得像”，而是提取可迁移原则。

分析顺序：

1. 参考里真正吸引用户的是什么：结构、密度、层级、Typography、色彩、shape、motion、interaction，还是品牌表层。
2. 哪些是参考产品自身业务/品牌造成的，不应搬运。
3. 哪些原则与当前产品兼容。
4. 哪些会和当前 Human intent / platform / accessibility 冲突。
5. 把留下的原则翻译成当前项目自己的规则。

示例：

```text
喜欢 A 的“克制”
→ 提取：低容器噪声 + typography-led hierarchy

喜欢 B 的“生活感”
→ 提取：更自然的 spacing + 更有人味的微交互

最终不是 A+B 外观拼贴，而是：
克制结构 + 生活化微表达
```

禁止照搬品牌色、icon、独特 layout signature 作为“参考分析”。

## B. Prototype / State Proof

**何时加载**：静态说明不足以验证关键交互风险，例如：

- drag / direct manipulation
- 多层 overlay
- editor / canvas
- 多步 flow
- optimistic rollback
- interruptible long action
- 复杂 motion continuity

先回答最小问题：

- 用户如何进入状态？
- 当前可操作对象是谁？
- 状态改变时对象连续性是否清楚？
- 中断 / 失败 / cancel 后去哪？
- focus / selection / scroll 是否保持正确？

选择最低成本 proof：state storyboard、关键状态快照、最小 clickable prototype、targeted running surface。

简单 checkbox、普通导航等已明确模式，不强制 prototype。

## 停止条件

Reference 已被翻译成项目规则，或交互的不确定性已经被最低成本证据消除时停止。

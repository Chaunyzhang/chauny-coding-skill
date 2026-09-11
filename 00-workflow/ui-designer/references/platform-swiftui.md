# SwiftUI Platform Rules

本文件不教 SwiftUI 基础语法，只记录容易破坏 UI System 的实现约束。

## Layout

优先 relationship-based layout：

- VStack / HStack / Grid
- alignment
- Spacer
- padding
- frame constraints
- safe-area APIs

过度依赖 `.offset()` / `.position()` 通常表示设计 ownership 或 layout model 有问题。

## Ownership

SwiftUI View hierarchy 应尽量反映设计 ownership：

- badge belongs to avatar
- loading overlay belongs to component
- fixed bottom action 不应误放进滚动内容

## Safe Area

- interaction content 默认尊重 Safe Area
- background 可按设计延伸
- 不把 `ignoresSafeArea()` 当通用修复工具

## Preview

Preview 的价值是低成本比较设计，而不是形式覆盖率。

复杂 UI 应优先为这些提供快速观察路径：

- important variants
- loading / empty / error
- selected / disabled
- long content
- dark appearance
- Dynamic Type
- motion states

不要为了 Preview 数量本身增加维护成本。

## Design Lab / Gallery

只有当以下一项成立时建立：
- reusable Component 数量已经明显增加
- Motion 调试频繁
- 需要比较多个设计方向
- full app navigation 明显拖慢 UI 迭代

否则 Preview 就足够。

## Abstraction

设计语言未稳定前：
- 优先具体语义 Component
- 不构建复杂通用容器框架
- 不为未来假想复用过度抽象

真实重复出现后再上移到 Design System。

## Visual Patch Smell

持续出现以下行为时，暂停局部修补并回 UI Designer：

- 多个 magic spacing
- 大量 `.offset()`
- 同义 Component 多份实现
- raw color 漂移
- 每个 Screen 各自定义 motion
- caller 传入大量 height/radius/padding/color 参数


## Cost Discipline

SwiftUI UI 验证默认选择最低成本路径。

优先：

`Existing Preview → Targeted Preview → Minimal running surface`

不默认：

- 每个改动启动完整 App。
- 每个改动跑真机。
- 遍历全部 simulator size。
- 生成完整 screenshot matrix。
- 为主观视觉判断自动反复刷新 Preview。

Preview 是工具，不是验收仪式。

如果 Human 已经可以从一个关键 Preview / Screenshot 判断设计方向，就停止增加视觉证据。

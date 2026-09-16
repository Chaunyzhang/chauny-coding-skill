# SwiftUI 平台适配

**何时加载**：项目实际使用 SwiftUI。

**目标**：只记录 SwiftUI 中会影响 UI 结构、状态和验证的高影响约束；不重复通用 SwiftUI 教程。

## Layout

优先 relationship-based layout：

- Stack / Grid / alignment
- Spacer
- padding
- frame constraints
- safe-area APIs

持续依赖 `.offset()` / `.position()` 修补布局，通常表示 ownership 或 layout model 有问题，应先检查结构。

## View hierarchy 与 ownership

View hierarchy 尽量反映设计 ownership：

- badge 属于 avatar，而不是页面随机 overlay。
- loading overlay 属于被阻塞的 component/surface。
- fixed bottom action 不应误放进可滚动内容。

## Safe Area

- 可交互内容默认尊重 safe area。
- background 可按设计延伸。
- 不把 `ignoresSafeArea()` 当通用修复工具。

## State

- 持久业务状态不因 View 重建而丢失。
- View-local presentation state 保持局部。
- Derived presentation 尽量由权威状态推导。
- 避免同一事实同时存在于多个 `@State` / model owner 中。

## Preview

Preview 用于低成本比较真实重要状态，不追求数量：

- normal
- loading / empty / error（相关时）
- selected / disabled / pending（相关时）
- long content
- dark appearance
- Dynamic Type

只有 reusable components 明显增加、motion 调试频繁或 full app navigation 严重拖慢迭代时，才考虑更重的 Design Lab / Gallery。

## 视觉修补异味

出现这些信号时暂停 patch：

- 多个 magic spacing。
- 大量 `.offset()`。
- 同义 View 多份实现。
- raw color 漂移。
- 每个 Screen 各自定义 motion。
- caller 传大量 height/radius/padding/color 参数。

优先回到 Design System / Composition / Ownership 修正。

## 验证成本

默认：

`Existing Preview → Targeted Preview → Minimal running surface → Full app / device when needed`

不要求每个小改动启动完整 App 或遍历所有 Simulator。

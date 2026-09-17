# SwiftUI 平台适配

只在 SwiftUI 项目加载。核心 UI 规则仍以通用 Spec 为准。

## Layout
- 优先使用 SwiftUI layout system 表达关系，避免靠大量 magic offsets 修图。
- Safe area、keyboard、Dynamic Type 必须是布局输入。
- GeometryReader 只在确实需要父级尺寸时使用，避免扩散为默认布局工具。

## Ownership
- Durable shared state 放在明确 owner；leaf View 通过 Binding/action/event 消费。
- `@State` 只拥有本 View 的本地状态；不要把服务端/跨页 truth 藏进叶子 View。
- Navigation path / sheet presentation 有明确 owner。

## Component / Design System
- token、font role、color role、spacing/radius family 有单一来源。
- 同义组件优先复用 Style/ViewModifier/Component contract，不靠复制 modifiers。

## Preview / State Proof
- 关键 components/Surface 为 Relevant states 建 Preview/fixture，尤其 empty/error/long text/large Dynamic Type。

## Visual repair smell
以下通常意味着结构/Spec 有问题：大量 `.offset`、负 padding、同义 magic number、overlay 堆叠修 alignment、每页自建 Color/Font literals。

## Verification
真机/Simulator 验证 safe area、keyboard、Dynamic Type、Dark Mode（适用）、Reduce Motion、VoiceOver/Focus（适用）。

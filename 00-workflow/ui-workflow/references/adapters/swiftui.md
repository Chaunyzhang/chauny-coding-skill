# SwiftUI 与原生生态适配

只在 SwiftUI 或原生桌面/移动苹果生态项目加载。核心 UI/UX 规则以通用 Spec 与 `references/craft/` 为准，本文件只约束原生布局、状态归属、材质几何与真机验证。

## 1. Layout 与连续几何（必须）

- 优先使用原生布局容器（Stack / Grid / Layout）表达结构关系，不能靠大量 `.offset`、负 padding 或 overlay 堆叠硬修对齐（这些通常是结构或 Spec 有问题的信号）。
- Safe area、键盘高度与 Dynamic Type 必须是布局一等输入；`GeometryReader` 只在确实需要父级尺寸时使用，避免扩散为默认布局工具。
- 圆角容器优先使用连续曲率圆角（Continuous Corner / Squircle）并遵守嵌套同心圆角关系，避免生硬几何圆弧割裂边缘高光与阴影。

## 2. 状态归属（Ownership）

- 跨页持久化真相放在明确 owner（Model / Store）；叶子 View 通过 `Binding` 或事件回调消费。
- `@State` 只拥有本 View 的本地瞬时状态，不能把服务端或跨页真相藏进叶子 View。
- `NavigationPath`、Inspector、Popover 与 Sheet 的展示状态必须有明确单一 owner，避免多处同时触发叠窗。

## 3. 材质、语义动态色与组件复用

- 优先消费系统语义动态色（主/次/三级/四级 Label、Standard 与 Grouped Background）与系统材质（Vibrancy / Material），不手写死白/死黑或硬编码不透明度冒充失焦态与暗色态；半透明材质只用于导航与控制层，不铺在内容层。
- token、font role、color role、spacing/radius family 保持单一来源；同义组件通过 `ButtonStyle` / `ViewModifier` / 共享组件契约复用，不靠复制粘贴 modifier 链。

## 4. Preview 与真机验证（必须）

- 关键组件与 Surface 为 Relevant 状态建 Preview/fixture，重点覆盖 empty、error、长文本、极值数据与超大 Dynamic Type。
- 真机或 Simulator 必验：safe area、软键盘、Dynamic Type、Dark Mode、窗口/分栏失焦态、VoiceOver/键盘焦点，以及系统三项偏好降级（Reduce Motion、Reduce Transparency、Increase Contrast）。

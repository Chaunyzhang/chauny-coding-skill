# UI 设计工作流 Evals

这些场景测试 Agent 行为，不测试是否逐字复述 Skill。

## Eval 1 — 从零 Todo 首页

**输入**：用户说“做一个 Todo App 首页，安静、温暖、成熟，不要幼稚。”

**期望行为**：
- 先做轻量 Coverage，而不是启动全套企业流程。
- 主动明确任务列表内容边界、empty/loading/error、完成动作、层级、组件和 layout。
- 将 `安静/温暖/成熟/不要幼稚` 编译成统一视觉规则。
- 页面构图先于高保真属性细节。
- 最终生成 `UI-DESIGN-SPEC.md`：给出确切 typography roles、color roles/values、spacing scale、radius、surface/shadow、icon、motion、关键组件 geometry，以及 Todo Home 的逐页面结构/间距/状态。
- 生成可复制的 Global UI prompt 和 Todo Home page prompt。
- 不需要用户逐条提醒长标题、空状态、pending 等。

**失败行为**：
- 直接输出漂亮 loaded screenshot。
- 只写 “warm/minimal/mature” 三个词。
- 每条任务都做成大 Card 并统一大圆角。
- 最后只留下“温暖中性色 / 中等圆角 / 舒适间距”等模糊描述，让实现者自己选数值。
- 没有 `UI-DESIGN-SPEC.md` 或逐页面 Page Spec。
- 强制运行全部能力模块。

## Eval 2 — 极简 + 一点活跃

**输入**：用户要求“整体极简，但 icon 和互动可以活跃一点，最好跟 OS 的动态感结合。”

**期望行为**：
- 极简控制结构层。
- 活跃主要进入 icon / accent / micro-motion。
- 最终仍是一套明确的统一视觉方向。
- 把方向解析成 Visual Laws，并进一步固化到具体 color/type/shape/motion/component 规则，而不是停在风格词。

**失败行为**：
- 把极简与活跃平均，得到多彩卡片 + 大阴影 + 大量动效。
- 直接判定两者不能共存。

## Eval 3 — 已有稳定 Design System 的局部按钮修改

**输入**：已有成熟组件库，只要把一个 destructive action 表达清楚。

**期望行为**：
- 复用现有视觉系统，不重新进行整套 Visual Direction 编译。
- 只展开 action hierarchy、destructive semantics、states、feedback、accessibility 和 rendered verification。

**失败行为**：
- 重新设计整页。
- 要用户重新选择产品风格。

## Eval 4 — 权限不能从视觉推断

**输入**：旧 UI 用按钮文案是否包含“Admin”来判断是否可删除；用户要求重构。

**期望行为**：
- 把 permission 视为显式 decision-bearing fact。
- 要求真实 source/owner/allowed values。
- 删除字符串推断作为正常路径。
- 加 negative/source gate 防回归。

**失败行为**：
- 把字符串判断封装进 helper 就宣布重构完成。

## Eval 5 — SwiftUI 项目

**输入**：iOS SwiftUI App，需要实现一个复杂列表页面。

**期望行为**：
- 核心实现规则保持平台无关。
- 加载 SwiftUI adapter 处理 layout、safe area、View ownership、Preview 和 state。
- 不出现 React/TSX 文件结构或 hooks 约定。

**失败行为**：
- 把 `components/hooks/api` 当成固定目录结构。
- 用 Web/React 术语约束 SwiftUI。

## Eval 6 — 用户给 Linear 和 Things 作为参考

**输入**：用户说“我喜欢 Linear 的克制，但希望有 Things 那种生活感。”

**期望行为**：
- 分析喜欢的可迁移原则，不复制品牌外壳。
- 形成类似“克制结构 + 更生活化的微表达”的项目化规则。
- 继续受当前产品内容、平台和 Human Avoid 约束。

**失败行为**：
- 直接做 Linear + Things 的外观拼贴。

## Eval 7 — 复杂拖拽

**输入**：卡片支持长按拿起、跨区域拖拽、非法目标、取消和失败回滚。

**期望行为**：
- 识别静态设计不足，触发最低成本 state proof / prototype。
- 明确 pickup / dragging / valid target / invalid target / drop / cancel / rollback。
- 不为了 prototype 本身搭完整 Demo App。

**失败行为**：
- 只画 idle 和 dragging 两张图。
- 或反过来对普通按钮也强制做 prototype。

## Eval 8 — Human 否定视觉结果

**输入**：Agent 的机械检查都通过，但用户说“还是太幼稚。”

**期望行为**：
- Human 判断优先。
- 回看 saturation、shape、icon、motion、density 等可能来源。
- 更新视觉规则并重新给最低成本判断材料。

**失败行为**：
- 以“符合设计原则/一致性检查已通过”反驳用户。

## Eval 9 — 只做实现

**输入**：已有经过确认的 Surface Contract 和视觉稿，让 Agent 完成代码。

**期望行为**：
- 直接读取现有 `UI-DESIGN-SPEC.md`（若已提供）、repo、state/data owner、component contract 和平台规则并实现。
- 不重新询问审美方向，不自行替换 spacing/radius/color/type/motion 等已确定规则。
- 可见结果最终对照 Spec 做 rendered verification。

**失败行为**：
- 重做 Human Alignment。
- 自行改变已确认视觉方向。


## Eval 10 — 完整设计必须编译为权威规格

**输入**：用户要求从零设计一个三页面习惯追踪 App，并在确认方向后交给另一个 Agent 实现。

**期望行为**：
- 前面的 Coverage / Visual / Composition / System / State 判断最终只收束到一个 `UI-DESIGN-SPEC.md`。
- 全局部分给出明确 Visual Laws、Typography、Color、Spacing、Radius、Surface/Border/Depth、Icon、Motion 和组件 Grammar。
- 三个页面分别有 Page Spec，包含结构树、视觉优先级、关键间距/尺寸、组件、状态、适配和页面禁令。
- 文档包含 Global implementation prompt 和三个可复制 page prompts。
- 实现 Agent 可以只看该文档完成 UI，不需要重新设计。

**失败行为**：
- 只输出 moodboard、风格形容词或 token 草稿。
- 全局有 token，但页面布局/间距仍留给实现 Agent 自己决定。
- Page Spec 只写“遵循设计系统”。
- Prompt 再次要求实现 Agent“根据极简、温暖、高级感自由发挥”。


## Eval 11 — 从单张 UI 截图逆向视觉语言

**输入**：用户上传一张高质量 Todo App 首页截图，说“提取这张图的设计语言，我要用这个风格做自己的 App。”

**期望行为**：
- 触发识图模式，而不是只给几个风格形容词。
- 区分 `Observed / Resolved / Unknown`。
- 逆向页面树、视觉层级、alignment、gutter、section/item gap、Typography hierarchy、palette roles、radius/surface/border/depth、icon/imagery 和重复组件。
- 从近似间距/尺寸中归纳 token scale，而不是逐像素创建 token。
- 形成 3–5 条 Visual Laws 和可迁移 Style DNA。
- 明确单张静态图无法证明 motion、完整 states、responsive、state owner、backend behavior。
- 把可证明结果编译进 `UI-DESIGN-SPEC.md`，并用于目标 App，而不是复制源产品业务结构。

**失败行为**：
- 只说“极简、现代、圆润”。
- 直接照抄截图坐标。
- 从静态截图编造动画时长和 breakpoint。
- 从按钮颜色/文案推断权限或业务状态。
- 把源产品 logo、品牌资产、业务 IA 一起复制。

## Eval 12 — 多张同产品截图归纳 Design System

**输入**：用户上传同一个 App 的首页、详情页、设置页三张截图，要求尽量复刻 UI 风格。

**期望行为**：
- 跨图片寻找重复 typography、spacing、radius、surface、icon、component 规律。
- 合并同一 token 的近似观测值，形成统一 Design System。
- 每页生成独立 Page Reverse Spec，但共享同一个全局 Visual Laws / tokens / Component Grammar。
- 如果三张图之间存在视觉异常或一次性值，不把它误升格为全局规则。

**失败行为**：
- 每张图各建一套 token。
- 页面间视觉语言互相矛盾。
- 用截图偶然差异制造大量 radius/spacing/color。

## Eval 13 — 单截图不能证明响应式和动效

**输入**：用户上传一张桌面 Web 截图，要求“完全反推它的所有设计规则”。

**期望行为**：
- 尽可能提取可见结构和视觉规则。
- 明确 mobile breakpoint、reflow、hover transition、loading/error 等无法由该图证明。
- 将这些标为 Unknown；若用户的目标产品需要它们，则按目标产品约束补设计并明确是新决定。

**失败行为**：
- 编造 768/1024 breakpoint。
- 编造 180ms ease-out。
- 编造 unseen loading/error states，并声称来自原图。

## Eval 14 — 图片证据冲突时不强行统一

**输入**：用户上传同一产品两张截图，其中按钮圆角、标题字号明显不同，无法判断是不同版本、不同 breakpoint 还是不同 component variant。

**期望行为**：
- 把冲突本身记录为证据。
- 先尝试通过页面/组件语义、多图上下文判断是否属于 variant 或 breakpoint。
- 证据不足时标记 `Unknown / conflict`，不要为了生成“统一系统”擅自平均成一个值。
- 如果目标是新产品风格复刻，可以基于 Human 目标做一个新的 Resolved 决策，但明确它是目标设计决定，而非源图事实。

**失败行为**：
- 把两个冲突值直接平均。
- 隐藏冲突并声称源产品就是统一的。

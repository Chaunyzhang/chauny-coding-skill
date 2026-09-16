# UI 设计工作流 Evals

这些场景测试 Agent 行为，不测试是否逐字复述 Skill。

## Eval 1 — 从零 Todo 首页

**输入**：用户说“做一个 Todo App 首页，安静、温暖、成熟，不要幼稚。”

**期望行为**：
- 先做轻量 Coverage，而不是启动全套企业流程。
- 主动明确任务列表内容边界、empty/loading/error、完成动作、层级、组件和 layout。
- 将 `安静/温暖/成熟/不要幼稚` 编译成统一视觉规则。
- 页面构图先于高保真属性细节。
- 不需要用户逐条提醒长标题、空状态、pending 等。

**失败行为**：
- 直接输出漂亮 loaded screenshot。
- 只写 “warm/minimal/mature” 三个词。
- 每条任务都做成大 Card 并统一大圆角。
- 强制运行全部 12 个能力模块。

## Eval 2 — 极简 + 一点活跃

**输入**：用户要求“整体极简，但 icon 和互动可以活跃一点，最好跟 OS 的动态感结合。”

**期望行为**：
- 极简控制结构层。
- 活跃主要进入 icon / accent / micro-motion。
- 最终仍是一套明确的统一视觉方向。

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
- 直接读 repo、state/data owner、component contract、平台规则并实现。
- 不重新询问审美方向。
- 可见结果最终做 rendered verification。

**失败行为**：
- 重做 Human Alignment。
- 自行改变已确认视觉方向。

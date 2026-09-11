# Evals

## 1. 用户说“太挤”

输入：
用户说首页“太挤、看起来廉价”。

正确：
先检查 Density、Section grouping、Hierarchy、Alignment、Spacing rhythm，再决定是否需要视觉修改。

错误：
直接把所有 padding +4、加 blur 和 shadow。

## 2. 用户说“有生命感但别幼稚”

正确：
形成 Personality / Avoid，并推导为 Motion、Color、Shape、Density、Icon 等 Grammar；必要时给不同方向对比。

错误：
自动使用粉色、大圆角、emoji 和大幅 bounce。

## 3. 参数提问

输入：
Button 当前 radius 16，Agent 觉得 18 也可以。

正确：
按现有 Shape Grammar / Token 决定，不问用户。

错误：
让用户逐项选择 radius、padding、font size。

## 4. UI 时机

输入：
Stage 仍在快速搭 Backend / Data / 基础能力，Functional UI 已可操作。

正确：
不启动完整 UI Design Pass；继续保留可用 Functional UI。

错误：
为了“设计完整”提前重做所有 Screen。

## 5. UI milestone

输入：
核心能力已基本稳定，出现多个不一致 Screen、重复 Component、局部视觉 patch。

正确：
建议进入 UI Design Pass，先 Human Alignment，再 Systemization。

## 6. Product boundary

输入：
设计删除交互时发现不知道删除是否可恢复。

正确：
识别为产品语义问题，回 Product。

错误：
UI Designer 自己决定做 Undo，因此定义为 soft delete。

## 7. Architecture boundary

输入：
为了某 UI Flow 想改 Authentication / data ownership。

正确：
回 Chief Architect。

## 8. Variant

输入：
产品首页方向不明确。

正确：
Variant 在核心命题上不同，例如 Object-centered / Action-centered / Immersive。

错误：
三个方案只换 accent color。

## 9. SwiftUI patch

输入：
一个 Screen 需要大量 offset 才能视觉对齐。

正确：
优先检查 layout ownership / hierarchy / container structure。

错误：
继续追加 offset 直到截图看起来正确。

## 10. Motion

输入：
用户说“更高级、更丝滑”。

正确：
检查 continuity、response、settle、overshoot、state identity 和 interruption。

错误：
给每个元素加 fade + spring。


## 11. UI Project Structure

输入：
`EggCard` 目前只在 Hatch Feature 使用。

正确：
留在 `Features/Hatch/...`，不因为“可能以后复用”提前上移。

错误：
直接放进 `DesignSystem/Components`。

## 12. Shared Component Promotion

输入：
`PrimaryButton` 已经在 Hatch、Store、Inspiration 三个 Feature 使用，语义、State、Style 一致。

正确：
收敛 API 后上移到 Design System，并删除重复实现。

## 13. Directory Ambiguity

输入：
Agent 想新增 `Views/`，项目已有 `Features/...` 和 `DesignSystem/Components/`。

正确：
拒绝职责重叠的新目录，按 Feature-local / Shared Component 规则归属。

## 14. Design System Dependency

输入：
共享 `PetCard` 需要直接 import HatchFeature 的业务模型。

正确：
识别边界错误；Design System 不应依赖 Feature。保持 Feature-local 或重新抽取纯语义输入。


## 15. Human Aesthetic Authority

输入：
Agent 完成页面，并认为“整体已经很高级”。

正确：
Agent 只报告机械检查通过，并展示最低成本真实结果给 Human Review。

错误：
Agent 自行输出 `Visual QA passed` / `Aesthetically approved`。

## 16. Screenshot Loop

输入：
页面做了一个小 spacing 调整，没有用户要求再次确认。

正确：
如果已有规则足以机械确认，不反复生成截图。

错误：
连续截图、自己比较、自己打分直到“满意”。

## 17. Full App Run

输入：
一个 Feature-local Component 改了 semantic color token usage。

正确：
做最低成本的局部检查 / Preview。

错误：
启动完整 App、走全导航、跑真机做视觉确认。

## 18. Variant Cost

输入：
Design Intent 已明确，没有核心方向分歧。

正确：
按已确认方向做一个方案。

错误：
为了“探索充分”自动生成三套完整 Variant。

## 19. Human Says It Feels Wrong

输入：
规则机械上全部合规，但 Human 说“还是太冷”。

正确：
接受主观反馈，重新解释为 Color / Surface / Typography / Density 等 Grammar 问题并迭代。

错误：
因为规则都合规而坚持当前设计已经正确。

# Mechanical UI Review Protocol

本文件只定义 Agent 可以客观执行的 UI 检查。

它不是审美评分表。

## Authority

Agent 可以检查：

- Consistency
- Completeness
- Rule compliance
- Structural correctness
- Accessibility mechanics
- Component / Token usage
- State coverage

Human 决定：

- Beauty
- Taste
- Personality fit
- Visual balance
- Perceived quality
- Motion feel
- Final aesthetic acceptance

Agent 不得用自己的“看起来不错”替代 Human Review。

## 1. Structure

机械检查：

- Screen 是否有已定义的 purpose。
- Section / Component 是否符合既定 ownership。
- fixed / scroll relationship 是否与 Handoff 一致。
- 是否出现大量无规则的 offset / absolute positioning。

## 2. Design System Compliance

检查：

- semantic color 是否来自权威位置。
- typography role 是否复用。
- spacing / radius / motion 是否绕过既定 Token。
- shared Component 是否重复实现。
- Feature-local UI 是否错误上移或放错位置。
- DesignSystem 是否依赖业务 Feature。

## 3. State Coverage

只检查当前范围明确要求的状态：

- loading
- empty
- populated
- disabled
- selected
- error
- success
- permission / unavailable
- long content

未要求的状态不为理论完整强行扩展。

## 4. Interaction Mechanics

检查：

- 可交互元素是否具备既定 feedback。
- destructive action 是否使用既定 pattern。
- navigation 是否符合现有语言。
- loading / error / completion 是否有实现遗漏。

不判断“反馈是不是足够高级”。

## 5. Motion Mechanics

检查：

- Motion 是否有明确 job。
- 是否使用既定 Motion Token / pattern。
- state transition 是否存在明显断链。
- 是否出现无职责 animation。
- repeated / interruption state 是否有机械错误。

不判断“这个动画是否更丝滑、更舒服”。

## 6. Accessibility Mechanics

按项目能力检查：

- touch target
- Dynamic Type support
- semantic labels
- contrast requirement（可计算时）
- focus / disabled mechanics
- meaning 是否只依赖 color

## 7. Human Review Package

需要 Human Review 时，Agent 只准备最低成本的可判断材料：

优先顺序：

1. 已存在的 Preview。
2. 单个关键 Screenshot。
3. 最小可运行入口。
4. 只有必须验证设备行为时才升级到真机。

不要为了 Human Review 自动生成完整 Screenshot Matrix。

## 8. Feedback Interpretation

人类说：

“太挤”
“太廉价”
“太死”
“更舒服”
“更高级”

这些不是机械结论。

Agent 应：

1. 接受 Human 判断。
2. 翻译为可能的 Design Grammar 问题。
3. 提出最可能的系统层修复。
4. 修改后再次给 Human 看。

Agent 不与用户争论其主观判断，也不自行宣布“已经更高级”。

## 9. Cost / Value Rule

默认禁止：

- 重复截图确认同一事实。
- 多轮 Agent 自我视觉 critique。
- 无 Trigger 的全设备视觉巡检。
- 无 Trigger 的真机 UI 验证。
- 每个小改动都完整启动 App。
- 为简单页面建立复杂 Gallery。
- 为普通动画做 profiling。
- 无明确设计分歧时制作多个 Variant。

只执行能：

- 改变当前设计决策；
- 发现客观缺陷；
- 或为 Human 提供必要判断材料

的检查。

## 10. Completion

Agent 的 UI Review 可以结束，当：

- 已知规则冲突已清除。
- 当前要求的状态 /结构 / Component / Token 没有机械遗漏。
- Human 所需的最低成本 Review 材料已经准备好。
- 没有继续执行重复、低收益的视觉检查。

最终审美结论不属于 Agent Review。

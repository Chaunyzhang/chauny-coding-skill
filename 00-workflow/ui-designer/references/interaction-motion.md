# Interaction & Motion

## Feedback

每个有意义动作都应有及时反馈。

反馈可以是：
- pressed state
- progress
- state transition
- visible result
- error
- haptic
- motion

不要让用户猜“系统有没有收到”。

## Destructive

危险动作的 UI 必须符合上游已经确定的产品语义。

UI Designer 决定：
- 如何强调危险性
- 是否采用现有 confirmation pattern
- 如何表达 recovery / undo

但“是否可恢复”属于产品语义，不由 UI 决定。

## Motion Jobs

Motion 至少承担一个职责：

- continuity
- hierarchy
- state change
- origin / destination
- feedback
- relationship
- physical response

没有职责的动画应删除。

## Continuity

优先让同一个对象演化，而不是无意义 replacement。

例如：
- card → expanded detail
- idle control → active → processing → result

不是每个状态都换一套完全无关的 UI。

## Personality

示例：

Restrained productivity:
- fast response
- short settle
- low overshoot

Alive companion:
- immediate response
- soft organic transition
- subtle idle behavior
- controlled breathing
- low-to-medium overshoot

Playful:
- stronger scale
- more bounce
- expressive feedback

不要把“Alive”实现成所有元素持续动。

## Motion Tokens

只有重复的 motion relationship 才建立 Token，例如：
- fast response
- standard settle
- soft spring
- snappy spring
- press scale

不要每个 Component 自创 duration / spring。

## Interruption

重要交互动画必须考虑：
- repeated tap
- state changes mid-animation
- cancel
- reverse
- fast navigation

顺滑不仅是 easing，也是状态机稳定。

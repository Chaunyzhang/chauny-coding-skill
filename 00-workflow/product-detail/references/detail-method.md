# Product Detail Method

## Requirement Walkthrough

对一个 `Requirement-n` 做局部产品语义编译时，按需检查：

1. Intent：为什么 Current Stage 需要它。
2. Actor：谁执行、谁受影响。
3. Trigger：什么时候发生。
4. Preconditions：什么状态下允许发生。
5. Inputs：真正影响产品结果的用户输入。
6. Behavior：产品对用户承诺的主要行为。
7. State / Lifecycle：发生前后状态怎么变。
8. Ownership / Permission / Visibility：谁拥有、谁能看、谁能改。
9. Success：用户如何知道成功。
10. Failure / Recovery：失败、超时、中断、重复、冲突怎么表现。
11. Related Behavior：与当前 Stage 其他 Requirement 的产品关系。
12. Acceptance：怎样才算这个 Requirement 成立。
13. Explicit Exclusions：容易误做、但 Current Stage 明确不做什么。

不是每项都必须写。

## 深度规则

简单 Requirement 可能只需要：

- Intent
- Behavior
- Success
- Acceptance

复杂 Requirement 才需要完整生命周期、权限、失败与冲突语义。

禁止为了格式完整制造假细节。

## 场景模拟

内部快速走：

`Entry → Action → State Change → Visible Result`

再按风险选择：

- cancel
- retry
- duplicate
- permission denied
- stale state
- provider failure
- partial completion
- concurrent action

只有发现会改变产品含义的缺口才升级为用户问题。

# Product Refinement Boundary

Blueprint 只处理实施机械细节，不补产品语义。

## 什么时候回 Product Refinement

Product Refinement 是例外路径。先过四道门：

1. **Current Stage**：问题直接属于当前正在建设的 Requirement。
2. **Need Now**：现在不决定，就无法正确确定能力边界或验收。
3. **Cannot Defer**：不能安全交给运营后台、配置项、seed / fixture、后续 Stage 或低成本可逆默认值。
4. **Product Impact**：不同答案会改变 User Outcome、Actor / Relationship、Ownership、Permission / Visibility、State / Lifecycle、Irreversible Action、Business Rule Shape、Commercial Boundary、User-visible Failure / Recovery、External Promise、Acceptance Outcome 或 Privacy / Sensitive Product Semantics。

四项必须全部成立。

先确认 Product Definition / Product Atoms / Stage Contract 是否已有答案；已有答案则继承，不回问。

Foundation / technical-only / infrastructure / migration Stage 默认不进入 Product Refinement，除非该语义会改变当前底座抽象、状态模型、权限 / 所有权或 Acceptance。

未来由运营后台 / 配置系统控制的价格、奖励数值、概率、解锁阈值、文案等，默认不问具体值，只要求当前底座支持正确的配置结构。

四道门全部通过且 Blueprint 无法安全机械选择时：

```text
Owner: Product
Stage:
Requirement:
Missing Product Semantics:
Why Different Answers Change Product Behavior:
Downstream Impact:
```

回 `product`（Focused Refinement）。

## 不回 Product Refinement 的内容

Blueprint 自己按既有约定处理：

- UI layout / button placement / ordinary copy
- existing design-system component choice
- file / symbol / function organization
- test placement
- SDK wiring within frozen provider choice
- endpoint naming within frozen interface semantics
- low-cost reversible local behavior
- repository convention

## 回 Architecture 的内容

以下属于 Chief Architect：

- interface contract
- data ownership architecture
- consistency / transaction boundary
- security architecture
- technology / provider choice
- module boundary
- compatibility / migration strategy
- Stage scope / architecture acceptance

## 路由

`Implementation detail → Blueprint`

`Product semantics → product`

`Product Definition change → product`

`Architecture decision → chief-architect`

# Product Detail Boundary

Blueprint 只处理实施机械细节，不补产品语义。

## 什么时候回 Product Detail

当不同答案会改变：

- User Outcome
- Actor / Relationship
- Ownership
- Permission / Visibility
- Product State / Lifecycle
- Irreversible Action
- Business Rule
- Commercial Behavior
- User-visible Failure / Recovery
- External Promise
- Acceptance Outcome
- Privacy / Sensitive Product Semantics

先确认 Product Definition / Stage Contract 是否已有答案。

已有答案则继承，不回问。

没有答案且 Blueprint 无法安全机械选择时：

```text
Owner: Product
Stage:
Requirement:
Missing Product Semantics:
Why Different Answers Change Product Behavior:
Downstream Impact:
```

回 `product-detail`。

## 不回 Product Detail 的内容

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

`Product semantics → product-detail`

`Product Definition change → product-designer`

`Architecture decision → chief-architect`

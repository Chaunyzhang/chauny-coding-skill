# Question Filter

用于判断一个问题是否值得在 Product Detail 阶段询问用户。

## 必问候选

只有答案会改变以下内容时，才进入用户问题候选：

- User Outcome
- Actor / Relationship
- Ownership
- Permission / Visibility
- State / Lifecycle
- Irreversible Action
- Business Rule
- Commercial Behavior
- User-visible Failure / Recovery
- External Promise
- Acceptance Outcome
- Privacy / Sensitive Product Semantics

即使进入候选，也先检查 Product Definition、已有用户决定和 Architecture Constraint 是否已经给出答案。

已有答案则不问。

## 默认自行处理

以下通常不是用户问题：

- UI layout
- button placement
- ordinary copy
- icon
- spacing
- component choice
- common confirmation pattern
- loading presentation
- file / symbol naming
- endpoint naming
- library usage
- test placement
- standard retry implementation
- code organization
- formatting / lint

若这些细节确实会改变产品结果，再升级；否则保持实现自由。

## 根问题优先

优先问一个能够决定多个下游行为的问题。

示例：

“删除是永久删除还是进入可恢复状态？”

这个答案同时决定：

- lifecycle
- recovery
- visibility
- data retention expectation
- acceptance

优于分别问五个细节问题。

## 推荐默认

当存在明显稳健默认且不改变产品核心语义：

1. 给出默认。
2. 简述影响。
3. 不要求用户确认每一个普通选择。

只有高影响或不可逆选择必须等待用户裁决。

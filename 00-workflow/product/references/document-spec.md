# Product Documents

## Canonical Sources

只有：

```text
docs/product/Product-Definition.md
docs/product/Product-Atoms.md
```

两份都属于产品当前权威事实。

不得创建平行的：

- Product Detail
- Feature Spec
- Capability Card
- Interview Notes
- Product Thoughts
- Decision Log
- Stage Product Detail
- 其他重复产品事实文件

## Product Definition Structure

```text
# Product Definition

## 1. Product Core
## 2. Users & Outcomes
## 3. Core Product Loop
## 4. Product Rules
## 5. Business Model
## 6. Market & Competitive Reality
## 7. Capability Map
## 8. Ideal Product State
## 9. Current Minimum Complete Outcome
## 10. Candidate Requirements
## 11. Product Evolution & Architecture-Shaping Considerations
## 12. Product Acceptance Intent
## 13. Open Product Questions
## 14. Handoff to Architecture
```

### 9. Current Minimum Complete Outcome

必须包括：

- Outcome
- Primary Actors
- Core Journey
- Must-Have Capabilities
- Current Requirements
- Required Product Rules / Failure Semantics
- Visible Result
- Completion Boundary
- Explicitly Not Current
- Product Priority / Relationships（需要时）

### 10. Candidate Requirements

```text
Requirement-n

Requirement:
Product Rationale:
Related Outcome / Rule:
Horizon: Current | Near | Future
Product Priority:
Architecture-Shaping: Yes | No
```

### 14. Handoff to Architecture

只做 consumer-aware index：

```text
Current Minimum Complete Outcome:
...

Current Requirements:
- Requirement-n

Product Priority / Relationships:
- ...

Relevant Product Atoms:
- Requirement-n → Atom-n, Atom-n

Explicitly Not Current:
- ...

Architecture-Shaping Future:
- ...

Open Product Questions:
- ...
```

不要复制 Atom Statement。

## Product Atoms Structure

推荐：

```text
# Product Atoms

## Product-wide Rules

### Atom-1

Statement:
Kind:
Belongs To:
Status:

## Requirement-7 — <name>

### Atom-42
...

### Atom-43
...

Representative Example:
...
```

按产品语义归类，不按聊天时间顺序归类。

## Single Source Rule

同一个事实如果是 Definition-level conclusion，Definition 是权威表达；Atoms 只保存其更具体、不可丢失的子事实。

不要在 Definition 和 Atoms 复制完全相同的一句话。

## Write Routing

### Route to Definition

内容改变：

- Product Core
- Users & Outcomes
- Product Loop
- Product Rule
- Business Model
- Capability Map
- Ideal State
- Current MCO
- Requirement
- Product Evolution
- Acceptance Intent
- Architecture Handoff

### Route to Atoms

内容：

- 太具体不适合 Definition；
- 但丢失会让后续语义、实施或验收出现歧义。

### Discard

- 思考过程。
- 被否定路线。
- 研究流水账。
- 临时脑暴。
- 普通实现 / UI 参数。
- 可由现有规则稳定重建的信息。

## Deletion

被推翻的事实：

- 直接删除旧 Statement / Example。
- 更新关系引用。
- 不追加 superseded / old version / revision history。

产品历史依赖版本库，不依赖当前事实文档。

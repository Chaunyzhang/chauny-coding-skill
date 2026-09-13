# Product Documents

## Canonical Sources

产品域只有两份长期权威事实：

```text
docs/product/Product-Definition.md
docs/product/Product-Atoms.md
```

不得创建 Product Detail、Feature Spec、Capability Card、Interview Notes、Product Thoughts、Decision Log、Stage Product Detail 或其他平行产品事实源。

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

包括：Outcome、Primary Actors、Core Journey、Must-Have Capabilities、Current Requirements、Required Product Rules / Failure Semantics、Visible Result、Completion Boundary、Explicitly Not Current，以及需要时的 Product Priority / Relationships。

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

只做 consumer-aware index，不复制 Atom Statement：

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

## Product Atoms Structure

推荐：

```text
# Product Atoms

## Product-wide Rules

### Atom-1
...

## Requirement-7 — <name>

### Atom-42
...

Representative Example:
...
```

按稳定产品语义归类，不按聊天时间顺序。

## Ownership & Write Routing

同一事实只有一个权威表达：Definition-level conclusion 由 Definition 拥有；Atoms 只保存更具体、不可丢失且不能从 Definition 稳定重建的子事实。不要在两处复制同一句话。

- **Definition**：Product Core、Users & Outcomes、Product Loop、Product Rule、Business Model、Capability Map、Ideal State、Current MCO、Requirement、Product Evolution、Acceptance Intent、Architecture Handoff。
- **Atoms**：过于具体而不适合 Definition，但丢失会让后续语义、实施或验收出现歧义的信息。
- **Discard**：思考过程、被否定路线、研究流水账、临时脑暴、普通实现 / UI 参数、可由现有规则稳定重建的信息。

## Deletion

事实被推翻时，直接删除 / 改写旧 Statement、Example 和关系引用；不追加 superseded、old version 或 revision history。历史由版本库承担，不由当前事实文档承担。

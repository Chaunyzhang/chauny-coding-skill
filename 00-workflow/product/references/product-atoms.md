# Product Atoms

## Purpose

Product Atoms 是产品长期细节记忆。

它解决的问题不是“把所有产品信息写得更详细”，而是：

> 防止高带宽产品对话里的关键事实因为 Product Definition 的概念压缩而永久消失。

## Capture Test

出现新信息时，依次判断：

1. 丢失后，下游是否可能实现出技术上合理但产品语义错误的结果？
2. 丢失后，未来是否很可能重新问用户已经回答过的问题？
3. 丢失后，是否无法区分真完成与空壳完成？
4. 丢失后，某个重要产品巧思是否无法从 Definition 稳定重建？
5. 是否会改变角色、对象关系、状态、权限、商业、配置边界、失败语义或 Acceptance？

任一 YES：捕获。

全部 NO：通常不进入 Atom Store。

## Atomicity

Atom 应是“最小可独立理解和引用的产品陈述”。

例如：

差：

```text
AI 引用灵感后能看到内容、可以修改，修改前要确认并跨设备保存。
```

更好：

```text
Atom-42
AI context 必须包含被引用 Inspiration 的实际内容。

Atom-43
引用保持原 Inspiration identity，不创建副本。

Atom-44
AI 对被引用 Inspiration 的修改必须经过用户确认。

Atom-45
确认后修改原 Inspiration。

Atom-46
引用关系必须跨会话恢复。
```

但不要机械按逗号 / 动词切分。两个无法独立理解的半句应保持一起。

## Schema

默认：

```text
### Atom-n

Statement:
Kind: Behavior | Rule | State | Relationship | Acceptance
Belongs To:
Status: Confirmed | Assumption | Open | Blocking
```

仅在有价值时追加：

```text
Horizon: Current | Near | Future
Depends On: Atom-n
Constrains: Atom-n
Related: Atom-n
Rationale:
```

## Kinds

### Behavior

真实产品行为：

- 用户做什么。
- 产品响应什么。
- AI / automation 能做什么。
- 外部参与方得到什么。

### Rule

长期必须成立 / 禁止的产品语义：

- 操作必须确认。
- 奖励规则可配置。
- 某对象不能被某角色修改。

### State

状态与生命周期：

- Pending → Active。
- 删除后进入可恢复状态。
- 完成后不可再次编辑。

### Relationship

角色 / 对象之间的关系：

- 引用指向原对象。
- Team owns shared project。
- Payer 与 user 是不同角色。

### Acceptance

可观察的成立事实：

- 引用「买牛奶」后 AI 能正确复述其内容。
- 确认修改后重新进入仍看到更新结果。

## Status

### Confirmed

用户明确决定或可靠产品事实。

### Assumption

Agent 准备作为产品判断使用，但用户尚未确认。

必须说明依据和猜错影响。

### Open

值得长期保留，但当前不需要决定。

### Blocking

不解决会使当前 Product Definition / Current MCO / 高影响架构塑形判断错误。

最终交给 Architecture 前不得保留 Blocking。

### Rejected

没有 Rejected 状态。

被否定内容从当前 Atom Store 删除；如果用户给出替代结论，直接更新事实。

## Belongs To

Atom 不得散装存在。

优先归属：

- Requirement-n
- Product Rule
- Current MCO
- Capability 名称
- Business Model
- Ideal Product State

一个 Atom 可以与其他部分有关，但应有一个主要 Belongs To。

## Relations

默认只用三种：

### Depends On

本 Atom 的产品语义依赖另一 Atom 成立。

### Constrains

本 Atom 限制另一 Atom 的允许空间。

### Related

有重要产品关系，但无明显单向依赖 / 约束。

不要为了构建知识图谱而给每条 Atom 连接一切。

## Grouping

`Product-Atoms.md` 优先按稳定归属分组，例如：

```text
# Product Atoms

## Product-wide Rules

### Atom-1
...

## Requirement-7 — AI 引用灵感

### Atom-42
...

### Atom-43
...

Representative Example:
...

## Requirement-8 — ...
```

不要按时间顺序保存。

时间顺序不能表达产品语义。

## Representative Example

Example 不编号。

保留条件：

- 能同时锁住多条 Atom。
- 能快速区分“看起来完成”和“真正完成”。
- 是用户真实表达的典型行为，或用户明确认可的等价例子。

一个 Requirement 通常 0–2 个足够。

不要把所有测试 case 搬进产品文档。

## Rationale

只保存“生成正确未来决策”所必需的 Why。

保留：

> 引用必须保持原对象 identity，因为后续 AI 修改目标必须是用户正在引用的那个对象。

不保留：

> 我们当时讨论了 A、B、C，最后觉得这个更好。

Rationale 是决策生成信息，不是历史记录。

## Continuous Reconciliation

每次有实质新产品信息后：

1. New → 新 Atom。
2. Same → 不新增。
3. More precise → 更新原 Atom。
4. Conflict → 标记 Blocking / 让用户裁决。
5. Rejected → 删除旧 Atom。
6. New relation → 加最少必要 relation。
7. Definition-level change → 同步更新 Product Definition。

禁止：

- 同义 Atom 重复增长。
- 为同一产品事实维护两份权威措辞。
- 旧事实被替换后继续作为“历史参考”留在当前文档。

## Current vs Future

Atom 可以保存 Future 巧思，只要它确实有产品价值。

例如：

```text
Atom-71
Statement: Reward amount is controlled by configurable product rule.
Kind: Rule
Belongs To: Reward Capability
Status: Confirmed
Horizon: Current
```

```text
Atom-72
Statement: Operations UI can change reward amount without app release.
Kind: Behavior
Belongs To: Operations Capability
Status: Confirmed
Horizon: Near
```

这样 Current 可以正确建立“可配置结构”，但不会提前建设 Near 的运营后台。

## Conversation Memory Rule

任何已经通过 Capture Test 的内容：

> 不得仅存在于聊天历史。

在进入下一轮重要产品讨论前，先写入 / reconcile canonical docs。

如果当前环境不能实际写文件，应明确产出待写入的 Atom 更新，而不是假装“我记住了”。

## Atom Store 不是 Question Generator

不得因为 Atom schema 有字段就追问用户。

Product Atoms 记录自然产生的高价值产品信息。

只有 Focused Refinement 的进入门禁成立时，才为缺失产品语义主动提问。

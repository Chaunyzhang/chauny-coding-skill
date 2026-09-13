# Product Atoms

## Purpose

Product Atoms 是产品长期细节记忆，用来防止高带宽产品对话中的关键事实因 Product Definition 的概念压缩而永久消失。它不是“把所有产品信息写得更详细”。

## Capture Test

出现新信息时判断：丢失后是否可能导致以下任一结果？

1. 下游实现技术上合理但产品语义错误。
2. 未来重复询问用户已回答的问题。
3. 无法区分真实完成与空壳完成。
4. 重要产品巧思无法从 Definition 稳定重建。
5. 角色、对象关系、状态、权限、商业、配置边界、失败语义或 Acceptance 被改变。

任一 YES：捕获；全部 NO：通常不进入 Atom Store。

## Atomicity

Atom 是最小可独立理解、引用和变化的产品陈述。不要把多个可独立变化的事实压成一句，也不要机械按逗号 / 动词切分。

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

- **Behavior**：用户、产品、AI / automation 或外部参与方发生的真实产品行为。
- **Rule**：长期必须成立或禁止的产品语义。
- **State**：状态、转换与生命周期。
- **Relationship**：角色 / 对象间关系，如 identity、ownership、payer/user。
- **Acceptance**：可观察、可区分真完成与空壳完成的成立事实。

## Status

- **Confirmed**：用户明确决定或可靠产品事实。
- **Assumption**：Agent 准备据此继续建模但用户未确认；应说明依据和猜错影响。
- **Open**：值得长期保留，但当前无需决定。
- **Blocking**：不解决会使 Product Definition、Current MCO 或高影响 Architecture-Shaping 判断错误；交 Architecture 前不得保留。

没有 `Rejected` 状态。被否定内容从当前 Atom Store 删除；如有替代结论，直接更新当前事实。

## Belongs To & Relations

Atom 必须有一个主要稳定归属，优先使用：Requirement-n、Product Rule、Current MCO、Capability、Business Model、Ideal Product State。

关系只在有生成价值时使用：

- **Depends On**：本 Atom 的产品语义依赖另一 Atom。
- **Constrains**：本 Atom 限制另一 Atom 的允许空间。
- **Related**：存在重要关系，但无明显单向依赖 / 约束。

不要为了构建知识图谱连接所有 Atom。

## Grouping

`Product-Atoms.md` 按稳定产品语义归组，不按聊天时间顺序，例如：

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
```

## Representative Example

Example 不编号。只在它能同时锁住多条 Atom、快速区分真完成与空壳完成，且来自用户真实表达或明确认可的等价行为时保留。一个 Requirement 通常 0–2 个足够；不要把测试用例库搬进产品文档。

## Rationale

只保存生成正确未来决策所需的 Why，不保存讨论历史。

保留：

> 引用必须保持原对象 identity，因为后续 AI 修改目标必须是用户正在引用的那个对象。

不保留：

> 我们当时讨论了 A、B、C，最后觉得这个更好。

## Continuous Reconciliation

每次出现实质新产品信息后：

1. **New** → 新 Atom。
2. **Same** → 不新增。
3. **More precise** → 更新原 Atom。
4. **Conflict** → 标记 Blocking / 让用户裁决。
5. **Rejected** → 删除旧 Atom。
6. **New relation** → 加最少必要 relation。
7. **Definition-level change** → 同步更新 Product Definition。

禁止同义 Atom 重复增长、为同一事实维护两份权威措辞、旧事实被替换后仍作为历史参考留在当前文档。

## Current vs Future

Future 巧思只要有长期产品价值也可以形成 Atom，并用 Horizon 表达时间层；这不代表现在建设。

例如 Current 可以确认“reward amount 可配置”，Near 可以确认“运营 UI 可在不发版时修改 reward amount”。这样当前建立正确的可配置结构，又不提前建设运营后台。

## Conversation Memory Rule

通过 Capture Test 的信息不得只存在于聊天历史。进入下一轮重要产品讨论前，先写入 / reconcile canonical docs；若环境不能实际写文件，应明确产出待写入更新，而不是假装“已记住”。

## Atom Store 不是 Question Generator

不得因为 schema 缺字段就追问用户。Atoms 记录自然产生的高价值信息；只有 Focused Refinement 门槛成立时，才为缺失产品语义主动提问。

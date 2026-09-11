---
name: domain-skill-authoring
display_name: 领域技能编写
description: 通过与用户共同建模，把模糊目标、现有 Skill、权威资料、真实踩坑和项目约束，提炼成高密度、可验证、可复用、能稳定改变 Agent 行为的专业 Skill。适用于新建、升级、审查和重构 Skill。
---

# 领域技能编写

## Purpose

不是“把资料整理成 Markdown”。

本 Skill 的任务是：

> **先理解用户希望 Agent 发生什么行为变化，再从概念和第一性原理出发，把这种目标编译成一套稳定、精确、可维护的 Skill。**

核心链：

`User Intent → Shared Concept Model → Agent Behavior Model → Evidence / Research → Rules → References → Evals → Stable Skill`

## Authoring Invariants

以下是写 Skill 的上层不变量。

### 1. Behavior Before Content

先回答：

> 使用这个 Skill 以后，Agent 的思考、判断、沟通、行动、停止或交接应该发生什么变化？

不要先回答：

> 这个文件应该有哪些章节？

章节服务于行为，不反过来塑造 Skill。

### 2. Intent Before Specification

用户通常不会一开始就准确描述 Skill。

用户可能提供：

- 一个目标。
- 一些不满意。
- 若干例子。
- 旧 Skill。
- 新材料。
- 真实事故。
- 对 Agent 行为的直觉。

Authoring Agent 必须从这些内容中理解真正意图，而不是把用户原话逐条变成规则。

### 3. Concept Before Rules

先寻找能解释多个例子和反馈的稳定概念，再写具体规则。

例如：

`“不要把多个功能硬串成完整产品剧情”`

不应只变成一条孤立禁令。

应继续抽象出：

`Slice = single capability cross-layer closure`

稳定概念一旦成立，具体规则应从概念自然推导。

### 4. First Principles Before Inheritance

现有 Skill、bundle、行业文章、代码、规范都只是输入，不自动拥有结构权。

先问：

- 这个领域最根本的问题是什么？
- 什么必须长期成立？
- Agent 真正需要做对什么判断？
- 哪些规则只是历史实现或旧流程留下来的？

再判断现有内容应该保留、重写、下沉还是删除。

资料是 evidence，不是 ontology。

### 5. Dialogue Is Model Building

和用户沟通不是填写需求表。

目标是共同发现正确模型。

优先使用：

- 复述你理解到的真正问题。
- 提出一个候选概念。
- 用用户自己的例子验证概念。
- 指出两种解释之间的差异。
- 让用户纠正模型。

避免：

- 长问卷。
- 按模板逐项确认。
- 把本可推导的问题重新抛给用户。
- 用户每说一句就新增一条规则。

### 6. Examples Are Evidence, Not Rules

例子、事故、抱怨首先是证据。

Authoring Agent 必须判断：

- 这是一次性的局部情况？
- 是某个更稳定原则的表现？
- 是旧规则执行过度？
- 是概念模型本身错了？
- 是边界 / authority 错了？

只有提炼成可复用规律后才进入 Skill。

### 7. Plain Language Before Artifact

正式写 Skill 前，先能用人话解释：

> 这个 Skill 使用后，Agent 会怎么工作？

至少用一个真实场景预演。

如果用户听完说“不是这个意思”，说明概念模型仍然错误，不应继续正式写文件。

### 8. Source Roles Must Be Explicit

不同输入承担不同角色，禁止无差别融合。

常见角色：

- **Semantic Baseline**：已有 Skill 的当前正确能力。
- **Material Warehouse**：新版 bundle、长文、笔记、外部建议，只作为可选内容来源。
- **Authority / Evidence**：官方规范、RFC、平台文档、标准。
- **Project Reality**：真实仓库、现有系统、已有规则。
- **User Correction**：用户对目标与行为模型的最新修正。

升级已有 Skill 时，除非用户明确要求重做：

> 旧 Skill 默认是 semantic baseline；新材料默认是 warehouse。

用户最新明确修正拥有最高的意图解释优先级。

详细见 `references/source-role-assignment.md`。

### 9. Behavioral Density, Not Shortness

高密度不等于少字。

一段内容值得留在主 Skill，当它会改变 Agent 的：

- 判断。
- 行动。
- 沟通。
- 权限边界。
- 触发条件。
- 验证方式。
- 停止条件。
- 上下游交接。

不会改变行为的背景、教程、历史、百科知识通常不应进入主体。

### 10. Think Broadly, Publish Narrowly

Authoring Reasoning 可以：

- 看大量材料。
- 比较多个模型。
- 模拟失败路径。
- 研究行业实践。
- 推演边界。
- 分析用户修正。

Final Skill 只保存稳定结论。

不要把写 Skill 的思考过程写进 Skill。

### 11. Structure Follows the Domain

不要强迫所有 Skill 具有相同目录和章节。

主 Skill 应保存该领域必须常驻 Agent 心智的内容。

References 保存：

- 按需展开的专业方法。
- 平台 / Domain 细节。
- 较长判定表。
- 可按 Trigger 加载的知识。

Evals 保存行为测试。

如果一个 Skill 不需要 reference，不为了模板创建 reference。

---

# Rule Quality Principles

以下原则控制“已经确定要写什么以后，规则应该怎么写”。

1. Skill 只记录长期稳定、必须正确、可复用的增量知识。
2. 一个 Skill 只负责一个可清楚描述的问题域；无法解释职责时重新建模或拆分。
3. 固定正确性、风险边界和结果，不无必要固定具体操作流程。
4. 规则按 `MUST / SHOULD / MAY` 分级；无法确定等级时不得写成 MUST。
5. 每条硬规则只表达一个约束。
6. Trigger 必须基于客观状态、行为或风险，不依赖模糊关键词。
7. 记录领域 Invariants。
8. 记录 Forbidden Patterns：已知错误路线、危险 shortcut、AI 高频误区。
9. 记录 Boundaries：何时成立、何时不成立、谁拥有裁决权。
10. 不复制 Agent 本来就知道的基础百科知识。
11. 区分事实规则、领域共识、项目选择和用户偏好。
12. 原则与工具分离；工具只有在本身是硬约束时才写死。
13. 可客观验证的重要正确性要求必须说明如何验证。
14. 主观判断不得伪装成机器可证明事实；明确 Human / Agent 的裁决边界。
15. 无证据时区分 `Confirmed / Suspected / Unknown`。
16. Skill 是 guardrail，不是逐行脚本；保留合理推理空间。
17. 高风险技术结论优先依据官方规范、RFC、平台文档或权威标准。
18. 踩坑必须提炼成可复用规律，不记录事故流水账。
19. 新踩坑优先补已有 Skill；只有形成新的独立问题域才新增 Skill。
20. Skill 之间的 MUST 不得冲突。
21. 通用 Skill 尽量跨项目规模成立；规模差异进入 Boundary / Decision Rule。
22. 不为不存在的问题提前堆规则。
23. 每个重要 Skill 必须可测试。
24. Eval 必须测试行为，而不是逐字复述规则。
25. 废弃即消失：被推翻的旧规则、阈值、例子、引用和历史痕迹从当前 Skill 级联删除。
26. Skill 的目标是不让 Agent 在已有成熟答案处重复发明规则，也不阻止 Agent 在未固定空间里推理。

---

# Trigger

当需要：

- 新建专业 Skill。
- 从模糊需求设计 Skill。
- 升级已有 Skill。
- 合并 / 重构多个版本。
- 从资料、事故或项目经验中提炼 Skill。
- 审查 Skill 是否真正满足用户目标。
- 修复 Skill 造成的错误 Agent 行为。

时触发。

---

# Authoring Workflow

## Phase 1 — Understand Intent

不要先写文件。

先建立用户真正想要的 Agent Behavior Model。

至少回答：

- 用户为什么需要这个 Skill？
- 没有这个 Skill 时，Agent 现在最常做错什么？
- 使用 Skill 后，用户希望 Agent 做什么不同的判断？
- 哪些事 Agent 应该主动做？
- 哪些事 Agent 不应该做？
- 哪些决定必须回用户 / 上游？
- 什么情况下这个 Skill 根本不应该出现？

### 沟通方式

优先形成候选理解，例如：

> “我理解你真正要的不是 X，而是 Y；如果这样定义，Agent 会……，对吗？”

比：

> “请填写 In Scope / Out of Scope / Trigger / Output。”

更有效。

如果用户已经明确，不为形式继续追问。

详细见 `references/intent-modeling.md`。

## Phase 2 — Build Shared Concept Model

从用户目标、例子、抱怨和材料中提炼少量核心概念。

检查每个概念：

- 能否解释多个真实例子？
- 是否比原始描述更稳定？
- 是否把不同问题错误合并？
- 用户听人话解释后是否认可？
- 这个概念是否真的需要命名？

不要过早创造术语。

概念存在的目的，是减少后续规则数量和歧义。

## Phase 3 — Preview Agent Behavior in Plain Language

在正式写 Skill 前，用人话描述：

- Skill 什么时候进入。
- Agent 首先做什么。
- 中间如何判断。
- 遇到模糊情况如何处理。
- 什么不做。
- 最终交给谁 / 输出什么。

至少用：

1. 一个正常场景。
2. 一个用户最担心的失败场景。

进行预演。

如果这个预演与用户脑中的 Agent 行为不一致，返回 Phase 1 / 2。

不要用正式 Skill 术语掩盖模型错误。

## Phase 4 — Assign Source Roles

在读大量资料前先标角色。

对每份输入回答：

- Baseline？
- Warehouse？
- Authority？
- Evidence？
- Project Reality？
- User Correction？

升级已有 Skill 时先建立能力基线，不因新材料更长、更专业就自动覆盖旧能力。

详细见 `references/source-role-assignment.md`。

## Phase 5 — Research Only What Needs Research

概念模型稳定后再研究。

按风险和变化速度选择来源：

1. 官方规范 / RFC / 平台文档。
2. 权威行业标准。
3. 官方框架 / 工具文档。
4. 成熟生产实践。
5. 高质量事故报告 / postmortem。
6. 真实项目踩坑。

研究只解决：

- 不确定事实。
- 高风险边界。
- 当前知识可能过时的内容。
- 用户材料无法支持的关键判断。

不要为了显得专业而做无目标研究。

高风险 MUST 不得仅凭模型记忆形成。

## Phase 6 — Derive From First Principles

不要直接从资料复制规则。

先定义：

- Domain purpose。
- Invariants。
- Failure modes。
- Authority boundaries。
- Correctness conditions。
- 必须固定与可以自由选择的部分。

再从这些内容推导规则。

如果某条规则无法回答：

> “它保护哪个不变量 / 避免哪个真实失败？”

应重新评估是否值得存在。

## Phase 7 — Compile Behavioral Rules

只提取会改变 Agent 行为的内容：

- Trigger
- Invariants
- MUST
- SHOULD
- MAY
- Forbidden
- Decision Rules
- Verification
- Boundaries
- Handoff / Authority（需要时）

删除：

- 教程。
- 百科知识。
- 背景历史。
- 空泛建议。
- 重复解释。
- Agent 本来就会的基础操作。
- 不影响判断和行动的说明。

### Truth vs Choice

先固定共同必须成立的正确性条件，再保留实现自由。

不得把常见方案、作者偏好或项目选择伪装成唯一正确方案。

## Phase 8 — Separate Core vs References

主 `SKILL.md` 只放必须长期常驻的行为架构。

优先放：

- Role / purpose。
- Trigger。
- Invariants。
- 高影响 MUST / Forbidden。
- Decision logic。
- Authority / Handoff。
- Completion / Stop conditions。

下沉到 references：

- 长专业展开。
- 平台细节。
- Domain-specific checklists。
- 复杂方法。
- 条件触发知识。

判断：

> Agent 在大多数使用场景中都需要随时知道这条内容吗？

不是，就考虑 reference。

详细见 `references/artifact-architecture.md`。

## Phase 9 — Build Evals From Real Misunderstandings

Eval 不只验证规则存在。

优先来自：

- 用户曾经纠正过的误解。
- Agent 最容易做出的合理但错误解释。
- 严格执行旧规则后产生的问题。
- 诱导 Agent 越权的场景。
- 缺少 Skill 时最常出现的 shortcut。

至少包含：

1. Normal case。
2. Edge / boundary case。
3. Tempting wrong solution。
4. Intent misunderstanding case。
5. Upgrade regression case（升级已有 Skill 时）。

Eval 测：

- 是否理解用户真正意图。
- 是否应用正确概念。
- 是否遵守边界。
- 是否拒绝诱导错误。
- 是否保留合理自由度。
- 是否产出用户需要的 Agent 行为。

## Phase 10 — Explain the Draft in Plain Language

正式发布前，再用人话解释一次：

> “用了这个 Skill 后，Agent 会怎么工作。”

不要只给目录树和规则摘要。

重点解释：

- 行为变化。
- 触发时机。
- 用户会少做 / 多做什么。
- Agent 会主动避免什么。
- 上下游如何协作。

如果人话解释听起来不符合用户目标，修改 Skill，而不是修改解释。

## Phase 11 — Compress by Decision Value

最终删除：

- Agent 已知基础知识。
- 无行为影响解释。
- 重复规则。
- 模板性填充。
- 历史痕迹。
- 无真实风险的限制。
- 只为“显得完整”存在的章节。

压缩目标：

> **减少无价值文字，同时保留足以稳定行为的概念、边界和决策规则。**

不要为了短而删专业能力。

## Phase 12 — Publish & Regression

发布前：

- 跑 eval。
- 检查与相关 Skill 的 MUST 是否冲突。
- 检查 baseline 能力是否被静默丢失。
- 检查用户最新修正是否真正进入当前模型。
- 检查 references 是否仍引用旧概念。
- 删除被推翻规则的所有残留。

---

# Upgrading Existing Skills

升级不是“把旧版和新版合并”。

默认流程：

1. 读取旧版，理解当前 semantic baseline。
2. 列出它实际能让 Agent 做什么。
3. 把新版本 / bundle /资料标为 warehouse。
4. 读取用户新的目标和纠正。
5. 建立新的 shared concept model。
6. 对旧能力逐项判断：
   - Keep
   - Clarify
   - Generalize
   - Conditionalize
   - Move to reference
   - Explicitly remove
7. 只有明确理由才删除能力。
8. 新规则必须与新的行为模型一致，而不是因为 warehouse 中存在就加入。
9. 发布前做 regression eval。

内部可维护能力映射，但正式 Skill 不需要保存迁移历史。

---

# Conversation Protocol

## Prefer Reflective Hypotheses

好：

> “你说的这些例子似乎都在表达一个更高层要求：X。按这个定义，Agent 会 Y，而不会 Z。我理解对吗？”

差：

> “请依次告诉我 Trigger、Input、Output、Boundary、Verification。”

## Ask High-Information Questions

只有当答案会改变：

- Skill role。
- core concept。
- authority。
- trigger。
- high-impact behavior。
- final artifact shape。

时优先询问。

能从已有上下文推导的，不重复问。

## Treat Corrections as Model Updates

用户说“不是这个意思”时：

不要只给旧规则加一个例外。

先检查：

> 是不是底层概念模型错了？

如果是，重建概念，再级联修改规则。

---

# Rule Classification

## MUST

违反会导致：

- Skill 明确目标无法成立。
- 正确性 / 安全 / 数据 /兼容严重问题。
- 权限边界错误。
- 长期系统性漂移。
- 用户明确不可接受的 Agent 行为。

## SHOULD

默认正确，但存在合理例外。

偏离时 Agent 应能说明理由。

## MAY

实现选择或可选增强。

不得把 MAY 写成流程税。

---

# Verification

Verification 必须与 claim 类型一致。

### 客观工程 claim

优先机器证据：

- build
- unit / integration / contract / migration / UI / E2E tests
- schema validation
- static analysis
- runtime evidence
- logs

### 主观或人类裁决 claim

不得伪装成机器可验证。

例如：

- 审美。
- 产品方向。
- 商业偏好。
- 主观可接受性。

应明确 Human Authority。

### Authoring-level Verification

正式 Skill 必须能回答：

- 用户是否认可 Agent Behavior Model？
- 核心概念是否能解释关键例子？
- 规则是否由概念和不变量推导，而不是堆补丁？
- 人话预演是否与最终 Skill 一致？
- Eval 是否覆盖用户最担心的误解？

---

# Output Architecture

不是固定模板。

常见结构：

```text
skill-name/
├── SKILL.md
├── references/
│   └── <only when needed>
└── evals/
    └── EVALS.md
```

主 Skill 的常见内容：

```text
Purpose / Role
Trigger
Invariants
MUST / SHOULD / MAY
Forbidden
Decision Rules
Authority / Handoff
Verification
Boundaries
Completion
References
```

没有内容的章节删除。

如果领域更适合其他结构，可以调整。

结构必须服务于 Agent 行为，不服务于模板完整。

---

# Eval Requirements

至少建立：

1. Normal case。
2. Edge / boundary case。
3. Tempting wrong solution。
4. Intent misunderstanding case。
5. Adversarial case。

升级已有 Skill 时增加 regression case。

Eval 检查 Agent 是否：

- 正确理解 Skill 的真正职责。
- 正确触发 / skip。
- 使用核心概念，而不是只背规则。
- 识别关键风险与边界。
- 拒绝 Forbidden。
- 保留合理推理空间。
- 在需要时升级给正确 Authority。
- 产出用户真正想要的行为。

---

# Update Rules

新踩坑出现时：

1. 先判断它暴露的是：
   - 局部实现问题；
   - 缺少一条规则；
   - Boundary 不清；
   - Authority 错误；
   - Trigger 错误；
   - 还是 Concept Model 错误。
2. 如果是 Concept Model 错误，先修概念，再级联规则。
3. 优先补已有 Skill。
4. 只有形成新的独立问题域才新建 Skill。
5. 增加对应 regression eval。

规则被改写或撤销时：

1. 直接删除旧规则、旧阈值、旧示例和旧反例。
2. 级联清除 references、Decision Rules、Verification、Boundaries 中的旧引用。
3. 不在当前 Skill 内保留 superseded / revision history。
4. 重新跑 eval。

---

# Final Quality Gate

发布前必须确认：

## Intent & Model

- 能一句话说明“这个 Skill 会让 Agent 发生什么行为变化”。
- 用户真正目标已被理解，而不是只复述原始措辞。
- 核心概念能解释主要例子和纠正。
- 正式写文件前已做人话行为预演。
- 用户修正已更新概念模型，而不是堆成例外。

## Source Discipline

- 已明确 baseline / warehouse / authority / reality / user correction。
- 新材料没有因更长或更专业而自动覆盖 baseline。
- 高风险事实有合适依据。
- 用户提供的例子没有被机械复制成通用规则。

## Rule Quality

- Invariants 稳定。
- MUST 有足够理由。
- SHOULD 保留合理例外。
- MAY 未被错误强制。
- Forbidden 对准真实 shortcut。
- Trigger 客观。
- Boundaries 清楚。
- 主观 claim 没有伪装成机器可验证事实。
- 项目选择没有伪装成通用真理。

## Information Density

- 主 Skill 中每个重要段落都会改变 Agent 行为。
- 没有百科知识、教程和背景废话。
- References 只承载按需专业展开。
- 没有为了模板完整创建无价值章节或文件。
- 没有为了短而删除专业能力。

## System Fit

- 与上下游 Skill 权责不冲突。
- 没有静默丢失 baseline 的有效能力。
- 新命名 / 新对象只有在确实降低歧义时才存在。
- 废弃内容已级联删除。

## Evals

- 有 normal。
- 有 boundary。
- 有 tempting wrong solution。
- 有 intent misunderstanding。
- 有 adversarial。
- 升级时有 regression。
- Eval 测行为，不测逐字复述。

任何一项失败，继续修改，不发布。

---

# Final Principle

> 先理解用户想让 Agent 变成什么，再写 Agent 应该遵守什么。

> 先形成概念，再形成规则。

> 从第一性原理推导，不让材料结构替你思考。

> 对话的目标是共同建模，不是填写模板。

> 例子用来发现规律，不用来堆规则。

> 正式文件之前先用人话验证 Agent 行为。

> 作者可以广泛思考，最终 Skill 只保留稳定、能改变行为的高密度信息。

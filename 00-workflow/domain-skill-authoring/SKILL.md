---
name: domain-skill-authoring
display_name: 领域技能编写
description: 把一个专业领域的需求、权威资料、行业经验和真实踩坑，提炼成短、准、可验证、可复用的专业 Skill。
---

# 领域技能编写

## Purpose
把一个专业领域的需求、权威资料、行业经验和真实踩坑，提炼成短、准、可验证、可复用的专业 Skill。

## Core Principles

1. Skill 只记录长期稳定、必须正确、可验证的工程规则。
2. 一个 Skill 只负责一个独立问题域；无法一句话说明职责时继续拆分。
3. 固定正确性、风险边界和验证要求，不无必要固定具体实现流程。
4. 所有规则按 `MUST / SHOULD / MAY` 分级。
5. 每条硬规则只表达一个约束。
6. Trigger 必须基于客观变化或行为，不用模糊关键词。
7. 每个 Skill 必须记录领域 Invariants。
8. 必须记录 Forbidden Patterns：已知错误路线、危险 shortcut、AI 高频误区。
9. 必须写 Boundaries：适用范围、例外、需要额外判断的条件。
10. 不复制 AI 本来就知道的百科知识，只保留增量知识。
11. 区分事实规则与项目选择；项目架构、框架、工具偏好不得伪装成通用真理。
12. 原则与工具分离；除非工具本身是项目硬约束，否则只规定目标，不写死工具。
13. 每个重要规则必须有 Verification。
14. Agent 不得仅凭判断宣布完成；优先依赖 build、tests、logs、schema validation、E2E 等证据。
15. 必须区分 `Confirmed / Suspected / Unknown`，无证据不得把假设写成事实。
16. Skill 是 guardrail，不是脚本机器人；允许合理 trade-off，但不得违反 MUST 和 Invariants。
17. 高风险领域的关键规则必须优先依据官方规范、RFC、平台文档或权威标准。
18. 详细背景资料不进入主体；主体保持短、硬、高信息密度。
19. 踩坑必须提炼成可复用规则，不记录流水账。
20. 新踩坑优先补已有 Skill；只有形成新的独立问题域才新建 Skill。
21. Skill 之间的 MUST 不得冲突；优先级默认：`Security invariant > Data integrity > Project convention > Preferred implementation style`。
22. Skill 名称必须具体表达问题域，禁止 `best-practices`、`expert`、`full-stack` 这类宽泛命名。
23. 通用 Skill 应尽量跨项目规模成立；规模差异放在 SHOULD、MAY 或 Decision Rules。
24. 不为不存在的问题提前堆规则；宁缺毋滥。
25. 每个重要 Skill 必须可测试。
26. Eval 必须包含诱导 Agent 犯错的 adversarial case。
27. Skill 修改后必须跑 regression eval。
28. 一条规则只有在违反后会造成真实 bug、数据风险、安全风险、兼容问题、长期一致性问题，或属于成熟行业共识时，才值得进入 Skill。
29. Skill 的目标是不让 Agent 在已有成熟答案的地方重新发明规则。
30. 最终标准：窄、硬、稳、准、活、可触发、可验证、可维护、可测试、无废话。

## Trigger
当需要新建、补全、审查或重构一个专业领域 Skill 时触发。

## Authoring Workflow

### 1. Define Scope
先明确：
- Skill 名称
- 一句话职责
- Trigger
- In Scope
- Out of Scope
- 常见失败
- 失败后果

无法一句话说明职责时，拆分。

### 2. Research
按优先级调研：
1. 官方规范 / RFC / 平台文档
2. 权威行业标准
3. 官方框架 / 工具文档
4. 成熟生产实践
5. 高质量事故报告 / postmortem
6. 真实项目踩坑

关键规则交叉验证。
不得仅凭模型记忆形成高风险 MUST。

### 3. Extract
只提取：
- Invariants
- MUST
- SHOULD
- MAY
- Forbidden Patterns
- Failure Modes
- Decision Conditions
- Verification
- Boundaries

删除：
- 教程
- 百科知识
- 背景介绍
- 空泛建议
- 个人偏好
- 重复内容

### 4. Separate Truth From Choice
先找共同必须满足的正确性条件，再列可选方案。

例如数据库 schema change：

必须保证：
- 历史数据有确定处理方式
- 新旧版本兼容
- migration 可追踪
- 数据完整性可验证

常用方案可以包括：
- expand-contract
- backfill
- dual read/write

具体选择根据：
- 数据量
- 数据库能力
- 部署方式
- 停机要求
- 新旧版本共存情况
- 风险成本

不得把常用方案误写成唯一正确方案。

### 5. Classify Rules

#### MUST
违反即产生正确性、安全、数据、兼容或长期一致性问题。

#### SHOULD
默认正确，但存在合理例外；偏离时应说明技术理由。

#### MAY
可选实现，不属于强制约束。

无法确定等级时，不得写成 MUST。

### 6. Atomicize
每条规则只表达一个约束。

禁止：
> 修改数据库时注意 migration、性能、兼容和测试。

改成独立规则。

### 7. Add Invariants
记录该领域长期稳定、不会轻易改变的事实。

例如：
- Webhook delivery 不得假设 exactly-once。
- 客户端版本无法原子升级。
- 用户可见错误文案不是根因证据。

### 8. Add Forbidden Patterns
主动寻找并记录：
- AI 高频 shortcut
- 看似能工作但生产危险的方案
- 绕过验证的方法
- 掩盖问题而非解决根因的方法
- 与项目既有 canonical pattern 冲突的方法

### 9. Define Verification
每个重要正确性要求都必须回答：
> 怎么证明它成立？

优先机器证据：
- build
- unit / integration / contract / migration / UI / E2E tests
- schema validation
- runtime evidence
- logs
- static analysis

禁止使用 `review carefully` 这类不可验证表述。

### 10. Define Boundaries
检查每条规则：
- 什么时候成立？
- 什么时候不成立？
- 是否受项目规模影响？
- 是否受平台版本影响？
- 是否受部署模型影响？
- 是否只是项目选择？

有边界就写明。

### 11. Compress
最终删除：
- AI 已知基础知识
- 解释性废话
- 重复句
- 无约束价值内容
- 不必要的固定流程
- 无法验证的观点

要求：
- 短
- 准
- 硬
- 高信息密度

## Output Structure

```text
# Skill Name

## Trigger

## Invariants

## MUST

## SHOULD

## MAY

## Forbidden

## Decision Rules

## Verification

## Boundaries

## References
```

没有内容的章节可以删除。
不得为了模板完整而填充废话。

## Eval Requirements

至少建立：
1. Normal case
2. Edge case
3. Tempting wrong solution

Eval 检查：
- 是否正确触发 Skill
- 是否识别关键风险
- 是否遵守 MUST
- 是否拒绝 Forbidden
- 是否保留合理决策空间
- 是否执行 Verification

测试 Agent 的行为，不测试它是否逐字复述规则。

## Update Rules

新踩坑出现时：
1. 判断是否可复用。
2. 优先补已有 Skill。
3. 只有形成独立问题域才新建 Skill。
4. 把事故提炼成规则。
5. 增加对应 regression eval。

## Final Quality Gate

输出正式 Skill 前必须确认：

- 单一职责成立
- Trigger 客观明确
- Invariants 稳定
- MUST 有可靠依据
- SHOULD 保留合理例外
- MAY 未被错误强制
- 硬规则原子化
- Forbidden 完整
- Boundaries 明确
- Verification 可执行
- 项目选择未伪装成通用事实
- 工具未被无必要绑定
- 高风险结论有权威来源
- 踩坑已提炼为规则
- 与现有 Skill 无 MUST 冲突
- 可跨项目规模使用
- 没有为不存在的问题过度设计
- 有 adversarial eval
- 修改后可做 regression eval
- 没有百科知识和废话

任何一项失败，继续修改，不输出正式 Skill。

## Final Principle

固定不变量，不固定所有实现。  
固定正确性，不固定个人偏好。  
固定必须验证的结果，不固定所有操作步骤。  
记录成熟规则，不让 Agent 临场重新发明工程常识。

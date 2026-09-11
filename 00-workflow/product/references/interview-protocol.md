# 产品对话协议

## 1. 先恢复产品记忆

开始 / 恢复时先读：

1. Product Definition
2. Product Atoms
3. 用户本轮新输入

不要先根据聊天记忆重新解释整个产品。

## 2. 每轮同时做两件事

对外：

- 和用户继续产品思考。

对内：

- 捕获本轮新产生的 durable product information。

不要让“继续聊天”和“维护产品记忆”变成先后两个阶段。

## 3. 问题合法性

一个问题值得占用用户注意力，通常因为不同答案会改变：

- 产品身份 / 核心用户。
- 用户结果 /核心闭环。
- 角色、ownership、permission、lifecycle、不可逆规则。
- 商业关系。
- Current MCO。
- Current Requirements 之间的产品关系。
- 重要市场假说。
- Architecture-Shaping 产品方向。

普通 UI / 实现 / 可配置运营参数不属于产品核心提问。

## 4. 每轮问题纪律

- 通常 1–3 问。
- 优先高信息量根问题。
- 不重复询问 Product Definition / Atoms 已经回答的问题。
- 用户已经深入思考时允许持续多轮。
- 边际价值低时停止追问，给出候选 Assumption 让用户纠正。

## 5. 自然细节必须捕获

用户在回答大问题时经常顺便说出非常重要的小事实。

例如：

> “引用的是原来那张卡，不是复制一份；AI 修改之前要让我确认。”

不要只提取“大方向”。

这类信息必须在当轮转成 Atom。

## 6. 不把 Atom Store 变成问卷

用户没自然讨论到的细节，不因为 Atom schema 没填就追问。

只有：

- Current MCO /当前 Requirement 真的需要；
- 现在不决定会搭错产品语义；
- 不能安全延后 / 配置；
- 答案高影响；

才进入 Focused Refinement。

## 7. 深挖链

用户答案只是功能名 /愿望 /形容词时，可按需要沿：

`谁 → 真实处境 /触发 → 做什么 → 产品响应 → 状态变化 → 可见价值 → 完成 → 回访 → 失败语义`

逐步深挖。

不是每次全问。

## 8. Current Outcome Questions

接近交架构时，应明确：

- “现在你最想先让哪个完整产品结果真正成立？”
- “少掉什么能力后，这个结果会变成空壳？”
- “哪些 Requirement 必须共同存在？”
- “哪些虽然都是 Current，但本身可以独立成立？”
- “什么明确不需要现在做？”
- “哪些 Future 虽然不建设，但会改变今天的产品模型？”

这些是产品问题，不应交给 Architect 猜。

## 9. Assumption / Open / Blocking

### Assumption

Agent 准备用某个判断继续产品建模，但用户未确认。

### Open

值得保留但当前可以后决策。

### Blocking

不解决会改变 Product Core、MCO、关键 Product Rule、商业关系或架构塑形产品模型。

用户确认后转稳定事实；否定后删除旧内容。

## 10. 冲突

发现 Product Definition / Atom /用户新输入冲突时：

1. 明确冲突事实。
2. 说明会改变什么。
3. 让用户裁决真正的产品问题。
4. 裁决后更新 canonical source。
5. 删除被替代旧事实。

不要保留两个互相矛盾的“都可能”。

## 11. 阶段性复述

当一个核心问题稳定时，用人话复述：

- 当前结论。
- 对产品意味着什么。
- 哪些相关 Atom / Rule 被确定。

不要频繁要求“整份总结是否正确”。

## 12. Focused Refinement

Architect / Blueprint 回来问产品语义时：

1. 先查相关 Atom。
2. 若已有答案，直接返回源事实。
3. 若没有，做 Need-Now 判断。
4. 只有必须现在决定才问用户。
5. 新答案写回同一 Definition / Atom Store。

不生成 Product Detail 副本。

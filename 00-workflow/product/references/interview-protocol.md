# 产品对话协议

## 1. 恢复与持续捕获

开始、恢复或上下文压缩后，先读：

1. Product Definition
2. Product Atoms
3. 用户本轮新输入

不要靠聊天记忆重新解释产品。

每轮同时进行两件事：对外继续产品思考；对内捕获本轮新增的 durable product information。用户回答大问题时自然带出的具体高价值事实也必须当轮形成 Atom，不要只提取“大方向”。

## 2. 问题门槛

问题值得占用用户注意力，通常因为不同答案会改变以下至少一项：

- 产品身份、核心用户、用户结果或核心闭环。
- 角色、ownership、permission、lifecycle、不可逆规则。
- 商业关系、Current MCO、Current Requirements 的产品关系。
- 重要市场假说或 Architecture-Shaping 产品方向。

普通 UI、实现细节和可配置运营参数不属于产品核心提问。

每轮通常 1–3 问，优先高信息量根问题；Definition / Atoms 已有答案时不重复问。用户已深入思考可继续多轮；边际价值低时停止追问，可给出候选 Assumption 让用户纠正。

## 3. Atom Store 不是问卷

不要因为 schema 有字段就补问未自然出现的细节。只有同时满足以下条件才进入 Focused Refinement：

- Current MCO / 当前 Requirement 真的需要；
- 现在不决定会搭错产品语义；
- 不能安全延后、配置化或使用低成本可逆默认；
- 不同答案会产生高影响差异。

## 4. 深挖链

当用户答案仍只是功能名、愿望或形容词时，可按需沿：

`谁 → 真实处境 / 触发 → 做什么 → 产品响应 → 状态变化 → 可见价值 → 完成 → 回访 → 失败语义`

逐步深挖，不必每次全问。

## 5. Current Outcome Questions

接近交架构时，必须能回答：

- 现在最想先让哪个完整产品结果成立？
- 少掉什么能力后会变成空壳？
- 哪些 Requirement 必须共同存在？哪些虽是 Current 但可独立成立？
- 什么明确不需要现在做？
- 哪些 Future 虽不建设，却会改变今天的产品模型？

这些是产品问题，不交给 Architect 猜。

## 6. Status 与冲突

Status 的定义以 `product-atoms.md` 为准。对话中按以下方式使用：

- **Assumption**：准备继续建模但尚未确认。
- **Open**：值得保留但可后决策。
- **Blocking**：不解决会改变 Product Core、MCO、关键 Product Rule、商业关系或架构塑形模型。

发现 Definition / Atom / 用户新输入冲突时：明确冲突及影响，让用户裁决，随后更新 canonical source 并删除被替代事实。不要保留两个互相矛盾的 Confirmed 版本。

## 7. 阶段性复述

一个核心问题稳定后，可用人话复述：当前结论、它对产品意味着什么、哪些相关 Atom / Rule 被确定。不要频繁要求用户确认整份总结。

## 8. Focused Refinement

Architect / Blueprint 回来询问产品语义时：

1. 先查 Product Definition 与相关 Atoms。
2. 已有答案则直接返回源事实。
3. 没有答案则做 Need-Now 判断。
4. 只有必须现在决定才问用户。
5. 新答案写回同一 Definition / Atom Store。

不生成 Product Detail 副本。

# 产品 Skill Evals

评测目标：验证 Agent 能同时保持产品思考深度、原子信息保真、Current Product Intent 清晰和职责边界克制。

## 1. 模糊产品想法

用户：
“我想做一个让独立咖啡店记住顾客偏好、节日前提醒店主联系顾客的工具。”

正确：
- 先帮助理解真实用户结果和持续价值。
- 每轮只问少量高价值问题。
- 用户自然说出的归属、提醒、顾客数据等高价值细节同步形成 Atom。
- 不只是改写成 PRD。

## 2. Atomic Capture

用户：
“AI 引用灵感的时候要真的能看到那条灵感内容，而且改之前要我确认，改的是原来的那条，不是复制。”

正确：
当轮至少拆出：
- AI context 获得实际内容。
- 引用保持原对象 identity。
- 修改需确认。
- 修改目标是原对象。

错误：
- 只在聊天里说“明白”。
- 等产品讨论结束后再凭记忆总结。
- 把四个事实压成一句含糊 Requirement。

## 3. 代表性 Example 作为 semantic checksum

用户确认：
“引用『买牛奶』，说『改成买牛奶和面包』，确认后原卡片更新。”

正确：
- 作为 Requirement 的 Representative Example 保留。
- 不把它变成 `Scenario-n` 或大量测试 case。

## 4. 不制造细节

Product Atoms 已存在，某 Requirement 没有定义按钮位置、普通错误文案和运营价格。

正确：
- 不因为 Atom Store 想“完整”而提问。
- 只记录自然出现或 Current MCO 真正需要的产品事实。

错误：
- 按 Atom schema 逐字段盘问用户。

## 5. Current MCO 由产品明确

用户说：
“现在最想先让孵化、记录灵感获得货币、用货币买蛋这三个能力成立。”

正确：
- 在 Current MCO 中记录当前完整产品结果。
- 明确相关 Current Requirements。
- 记录哪些必须共同成立、哪些能力可独立成立。
- 不创建 `Product Stage-1`。
- 不自行决定架构 Stage 顺序。

## 6. 禁止 MVP / V1

用户：
“那就叫 MVP 或 V1 吧。”

正确：
- 保持 Current Minimum Complete Outcome / Current / Near / Future 体系。
- 不建立“缩水版本”对象或 Product Stage。

## 7. 产品关系不是业务施工剧情

前提：
孵化、记录灵感+奖励、货币购买蛋都属于 Current MCO。

正确：
- 可记录三者共同构成产品价值。
- 如果产品语义不要求连续发生，不写成必须“孵猫→灵感→赚钱→买狗蛋”的顺序约束。
- 施工拆分交 Architect / Blueprint。

## 8. Architecture Handoff 不再摘要 Atom

Requirement-7 有 Atom-42–46。

正确：
`Handoff to Architecture` 列 `Requirement-7 → Atom-42–46`，让 Architect 读取原文。

错误：
重新写一段“简化版 Requirement-7 细节”，造成第三层摘要。

## 9. Focused Refinement 先查记忆

Architect 问：
“分享到底是访问同一个对象还是复制？”

Product Atoms 已有 Confirmed Atom：
“Recipient accesses the same project; ownership remains with owner.”

正确：
直接返回并引用该 Atom，不再问用户。

## 10. Foundation / 运营参数

Current MCO 需要“记录灵感获得奖励”，未来运营可配置数值。

正确：
- Atom 保存“reward amount is configurable”。
- 不追问现在是 5 还是 10。
- Current 产品要求只固定配置结构语义。

## 11. 真正必须补的产品语义

当前要实现共享，但从未决定访问同一对象还是副本，且这会改变 ownership / revoke / lifecycle。

正确：
- 通过 Focused Refinement 问根问题。
- 结论写入 Atoms /必要时 Product Definition。
- 不创建独立 Product Detail 文档。

## 12. Product Definition 仍然克制

用户和 Agent 聊了几十条具体巧思。

正确：
- Product Definition 只保留整体产品模型和稳定高层结论。
- 具体但不可丢失信息进入 Atoms。
- 思考过程两边都不进。

错误：
因为担心丢失，把 Product Definition 变成长篇聊天摘要。

## 13. Atom 必须归类

出现 30 条新 Atom。

正确：
按 Requirement / Product Rule / Capability / MCO 等稳定归属整理，并建立最少必要关系。

错误：
按时间顺序追加 `2026-09-11 讨论记录`。

## 14. Atom 冲突

已有：
`Atom-21: Project belongs to individual owner.`

用户新决定：
“团队项目应该归团队，创建者离开也保留。”

正确：
- 判断是否是范围变化还是直接冲突。
- 若替代旧规则，更新 / 删除旧 Atom并修关系。
- 不同时保留两个互相冲突的 Confirmed Atom。

## 15. 被否定事实彻底消失

用户否定旧分享模型。

正确：
- 删除旧 Atom /旧 Example /旧关系引用。
- 不增加 `Rejected` / `Superseded` 状态。

## 16. 长期方向不能因不在 Current 丢失

用户：
“多端和团队现在不做，但成功以后一定会需要。”

正确：
- 判断是否 Architecture-Shaping。
- 相关高价值行为可形成 Near/Future Atom。
- 不提前写施工级规格。

## 17. Candidate Requirement 与 Atom 不混淆

Requirement：
“用户可以让 AI 修改已引用的灵感。”

Atoms：
- AI 获得实际内容。
- 修改需确认。
- 修改原对象。

正确：
Requirement 仍是一项建设候选；Atoms 保存其产品语义。

错误：
用几十个 Atom 取代 Requirement，导致 Architect 无法做范围裁决。

## 18. 市场事实

用户：
“这个市场肯定很大。”

正确：
- 视为需要外部验证的假说。
- 未查证不写成 Confirmed 产品事实。
- 若研究结论改变产品模型，写入 Definition；具体长期约束需要时可形成 Atom。

## 19. UI / 技术越权

用户问：
“引用卡片要用 sheet 还是页面？API 是 REST 还是 RPC？”

正确：
- UI 呈现交 UI 设计域。
- API 交 Architecture。
- 只处理背后真正的产品语义。

## 20. Conversation compaction

长产品讨论后即将恢复新会话。

正确：
- Product Definition + Product Atoms 已在过程中持续更新。
- 恢复时先读两份 canonical sources。
- 不依赖“模型应该还记得之前聊过什么”。

## 21. 空壳功能防丢信息

产品已经确认：
“AI 必须理解被引用灵感实际内容并能修改原对象。”

Architect / downstream 若只留下 `referenceId`：

正确产品 Skill 输出应能从 Atom Store 明确指出：
- 只传 ID 不能覆盖相关 Behavior / Identity / Acceptance Atoms。
- 这不是新功能，而是已有产品语义未完整实现。

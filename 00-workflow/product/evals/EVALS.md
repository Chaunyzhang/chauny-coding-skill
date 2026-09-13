# 产品 Skill Evals

评测目标：验证 Agent 同时保持产品思考深度、原子信息保真、Current Product Intent 清晰和职责边界克制。

## 1. 模糊产品想法

用户：“我想做一个让独立咖啡店记住顾客偏好、节日前提醒店主联系顾客的工具。”

正确：先理解真实用户结果和持续价值；每轮只问少量高价值问题；自然出现的归属、提醒、顾客数据等 durable detail 同步形成 Atom；不只是改写 PRD。

## 2. Atomic Capture

用户：“AI 引用灵感的时候要真的能看到那条灵感内容，而且改之前要我确认，改的是原来的那条，不是复制。”

正确：当轮至少拆出实际内容进入 AI context、引用保持原对象 identity、修改需确认、修改目标是原对象。

错误：只口头确认；等讨论结束再凭记忆总结；把四个事实压成模糊 Requirement。

## 3. Representative Example

用户确认：“引用『买牛奶』，说『改成买牛奶和面包』，确认后原卡片更新。”

正确：作为 Requirement 的 Representative Example 保留；不编号为 `Scenario-n`，不扩成测试用例库。

## 4. 不制造细节

某 Requirement 没有按钮位置、普通错误文案、运营价格。

正确：不因 Atom Store 想“完整”而追问；只记录自然出现或 Current MCO 真正需要的产品事实。

## 5. Current MCO 由 Product 明确

用户：“现在最想先让孵化、记录灵感获得货币、用货币买蛋这三个能力成立。”

正确：形成 Current MCO；列出 Current Requirements 及 Must Together / Independent 等真实产品关系；不创建 Product Stage，不安排架构 Stage 顺序。

## 6. 禁止 MVP / V1

用户：“那就叫 MVP 或 V1 吧。”

正确：继续使用 Current MCO 与 Current / Near / Future，不建立缩水版本对象或 Product Stage。

## 7. 产品关系不是施工剧情

前提：孵化、记录灵感+奖励、货币购买蛋都属于 Current MCO。

正确：可表达它们共同构成产品价值；若产品语义不要求连续发生，不制造“孵猫→灵感→赚钱→买狗蛋”的顺序。施工拆分交 Architect / Blueprint。

## 8. Handoff 不再摘要 Atom

Requirement-7 有 Atom-42–46。

正确：Handoff 写 `Requirement-7 → Atom-42–46`，让 Architect 读原文。

错误：再写一层简化版 Requirement 细节。

## 9. Focused Refinement 先查记忆

Architect 问：“分享到底是访问同一个对象还是复制？” Atoms 已有 Confirmed：`Recipient accesses the same project; ownership remains with owner.`

正确：直接返回并引用源事实，不再问用户。

## 10. Foundation / 运营参数

Current MCO 需要“记录灵感获得奖励”，未来运营可配置数值。

正确：保存“reward amount is configurable”；不追问现在是 5 还是 10；当前只固定配置结构语义。

## 11. 真正必须补的产品语义

当前要实现共享，但从未决定访问同一对象还是副本，且会改变 ownership / revoke / lifecycle。

正确：Focused Refinement 问根问题；答案写回 Definition / Atoms；不创建 Product Detail。

## 12. Product Definition 保持克制

经过几十条具体巧思。

正确：Definition 只保留整体模型和稳定高层结论；具体但不可丢的信息进入 Atoms；思考过程两边都不进。

错误：把 Definition 写成长篇聊天摘要。

## 13. Atom 必须归类

出现 30 条新 Atom。

正确：按 Requirement / Product Rule / Capability / MCO 等稳定归属整理，并建立最少必要关系。

错误：按时间顺序追加讨论记录。

## 14. Atom 冲突

已有 `Atom-21: Project belongs to individual owner.` 用户新决定：“团队项目应该归团队，创建者离开也保留。”

正确：先判断范围变化还是直接冲突；若替代旧规则，更新 / 删除旧 Atom 并修关系；不保留两个互相冲突的 Confirmed Atom。

## 15. 被否定事实彻底消失

用户否定旧分享模型。

正确：删除旧 Atom / Example / 关系引用；不增加 `Rejected` / `Superseded` 状态。

## 16. 长期方向不能因不在 Current 丢失

用户：“多端和团队现在不做，但成功以后一定会需要。”

正确：判断是否 Architecture-Shaping；高价值行为可形成 Near / Future Atom；不提前写施工级规格。

## 17. Requirement 与 Atom 不混淆

Requirement：“用户可以让 AI 修改已引用的灵感。” Atoms：AI 获得实际内容、修改需确认、修改原对象。

正确：Requirement 保持建设候选；Atoms 保存不可丢失产品语义。

错误：用几十个 Atom 取代 Requirement，导致 Architect 无法做范围裁决。

## 18. 市场事实

用户：“这个市场肯定很大。”

正确：视为待外部验证假说；未查证不写成 Confirmed；研究若改变产品模型写入 Definition，长期具体约束需要时形成 Atom。

## 19. UI / 技术越权

用户：“引用卡片要用 sheet 还是页面？API 是 REST 还是 RPC？”

正确：UI 呈现交 UI 设计域，API 交 Architecture；Product 只处理背后的产品语义。

## 20. Conversation Compaction

长产品讨论后恢复新会话。

正确：Definition + Atoms 已持续更新；恢复时优先读两份 canonical sources，不依赖模型聊天记忆。

## 21. 空壳功能防丢信息

已确认：“AI 必须理解被引用灵感实际内容并能修改原对象。” downstream 只留下 `referenceId`。

正确：能从 Atom Store 指出仅传 ID 未覆盖 Behavior / Identity / Acceptance 等既有语义；这不是新功能，而是已有产品语义未完整实现。

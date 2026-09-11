# Escalation Routing

施工遇到问题时按“谁拥有决定权”路由，不按谁最方便回答路由。

## Blueprint

施工拆分、Task 顺序、文件 / symbol 落点、已冻结边界内的机械实施问题。

## Product

当前 Stage 某 Requirement 的局部产品语义不足，或细化结果需要改变 Product Definition 时，统一回 `product`。

典型：

- ownership
- permission
- lifecycle
- irreversible behavior
- visible failure / recovery
- acceptance semantics
- Product Definition 本身需要更新

## Chief Architect

技术与架构决定：

- Stage Scope
- Decision
- module / interface
- data ownership architecture
- transaction / consistency
- security
- provider / stack
- migration / compatibility

## 不升级

普通 UI、代码组织、现有 convention、低成本可逆实现选择，施工 / Blueprint 自己解决。


## Verification / Acceptance Authority

Agent 只能对自己拥有证据能力的事项宣布通过。

- 机械可验证 → Agent。
- UI 审美、主观体验、真机感知 → Human（若项目规则如此定义）。
- Agent 无法访问的外部系统 → 对应 External Authority / Human。

不要为了获取自己没有的确定性而进入模拟、重复截图、反复测试或推断式验收。

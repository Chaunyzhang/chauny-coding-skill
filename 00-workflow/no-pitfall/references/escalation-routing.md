# Escalation Routing

施工遇到问题时按“谁拥有决定权”路由，不按谁最方便回答路由。

## Blueprint

施工拆分、Task 顺序、文件 / symbol 落点、已冻结边界内的机械实施问题。

## Product Detail

当前 Stage 某 Requirement 的局部产品语义不足，但不一定改变整个 Product Definition。

典型：

- ownership
- permission
- lifecycle
- irreversible behavior
- visible failure / recovery
- acceptance semantics

## Product Designer

只有细化结果需要改变 Product Definition 时。

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

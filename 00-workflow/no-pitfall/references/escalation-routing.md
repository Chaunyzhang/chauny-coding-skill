# Escalation Routing

施工遇到问题按“谁拥有决定权”路由，不按谁最方便回答路由。

## Construction Blueprint

施工拆分、Task/Slice 顺序、文件/symbol 落点、Execution Contract 与 Repository Reality 的施工级冲突。

## Product

产品语义或 Product Definition：actor、ownership、permission/visibility、state/lifecycle、irreversible behavior、business rule、visible failure/recovery、acceptance outcome、external product promise 等。若 Product Definition 本身改变，由 Product 更新 Definition / Atoms 后再交 Chief Architect 重新裁决。

## Chief Architect

Stage Scope / Exit / Acceptance、Decision、module/interface semantics、data ownership/consistency、transaction、security boundary、provider/stack、migration/compatibility 等架构决定。

## 当前施工层

普通 UI/代码组织、现有 convention、测试放置，以及不改变产品/架构语义的低成本可逆实现选择。

## Verification / Acceptance Authority

机械可验证 → Agent；审美/主观体验/真机感知 → Human（若项目如此定义）；Agent 无法访问的外部系统 → 对应 External Authority / Human。

不要为了获取自己没有的确定性而模拟、反复截图、重复测试或推断式验收。FULL AUTO 下，可由已有授权 Skill 解除的决定应自动路由；只有真正需要用户裁决或不可代理动作时暂停。

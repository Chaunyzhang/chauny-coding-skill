# Evals

## 1. 29 条完整性

要求：重构 no-pitfall。

通过：
1–29 条全部存在，正文语义不丢；导航可重排。

失败：
因为“重复”合并删除任意一条。

## 2. Task 小改动

Task：纯函数 bug fix。

通过：
检查 caller / tests，做局部修复和 focused test；不跑真机、远程 analytics、全量 Stage 验证。

失败：
为了“完整验证”执行全部真实环境链路。

## 3. Payment

Task：支付 webhook 新增重试。

通过：
触发副作用 / 幂等规则，验证 duplicate / retry / partial failure；必要时真实 sandbox。

失败：
只测 happy path 或用 mock 证明 provider 行为。

## 4. Migration

Task：schema migration。

通过：
确认旧状态 → 新状态、读写兼容、回填 / 恢复 / 顺序，并在相关步骤当场验证。

失败：
只看新 schema compile 通过。

## 5. Product ambiguity

施工共享功能发现“共享是副本还是同一对象”未定义。

通过：
回 Product Detail。

失败：
施工 Agent按最省代码的方案自行决定。

## 6. Architecture ambiguity

Execution Contract 要求某数据所有权，但真实架构无法满足且需要改变 owner boundary。

通过：
回 Chief Architect。

失败：
局部加兼容层绕过架构。

## 7. Failed verification

focused test 失败。

通过：
先定位当前改动 / 环境 / 既有问题；不扩大修改范围；每次重试必须有新信息。

失败：
反复 rerun 直到偶尔绿色，或顺手重构周边代码。

## 8. Superseded solution

方案 A 被正式改成方案 B。

通过：
主工作区删除 A 的旧实现、旧正文、旧配置、旧引用；进度事实仍保留。

失败：
留下 SUPERSEDED、注释掉旧代码或“原方案”正文。

## 9. General work

用户只要求修一个独立 bug，没有 Blueprint。

通过：
进入 General Work Mode，仍遵守全部 29 条。

失败：
因为没有 Execution Contract 就认为 no-pitfall 不适用。

# Stage Verifier v2 Evals

## 1. Product Atom 丢失

Product Atom：
AI 必须看到引用内容。

实现：
只把 `referenceId` 传给 AI。

期望：
FAIL。
Dimension: Semantic。
不得因为 ID traceability 完整就 PASS。

## 2. 双 Authority

Architecture：
Wallet owns balance mutation。

实现：
Purchase 直接 update balance table；
Wallet 也有 debit API。

期望：
FAIL。
Dimension: Semantic Unity / Modular Integrity。

## 3. 合法 Projection

Server 是 permission authority。
Client 根据 server 返回 `canEdit` 控制按钮。

期望：
不能因为 Client “也有 canEdit”误判双 authority。

## 4. Shared 垃圾场

Reward calculation 被三个 Feature 用。
Builder 搬到 `Shared/RewardUtils`。

Architecture：
Reward owns reward calculation。

期望：
FAIL。
原因是 ownership 被破坏，不是因为目录名字本身。

## 5. 语法重复但语义不同

两个 Domain 都有 `isExpired()`，规则完全不同。

期望：
不为了 DRY 强行抽象。
Semantic Unity PASS。

## 6. Work Efficiency — N+1

一次显示 100 项：
loop 内每项独立 DB query；
Repository 已有 batch API。

期望：
FAIL，说明当前真实工作量。
不要只说“性能可以优化”。

## 7. Micro optimization

纯内存 20 项数组，单次多扫一遍。
没有性能预算 / profiling / live issue。

期望：
不构成 Finding。

## 8. Complexity Sensor

函数 70 行，但单一职责、线性控制流、无重复语义。

期望：
触发 sensor，可 PASS / CONCERN。
不能仅凭 70 行 FAIL。

## 9. 真复杂

函数 validation + remote fetch + permission + state mutation + DB write + event emission，
嵌套 5 层。

期望：
Structural Health / Maintainability FAIL 或明确 MAJOR，
必须指出责任混合的实际影响。

## 10. Error Swallowing

catch 后返回空数组，产品把 backend failure 显示成“没有数据”。

期望：
FAIL Correctness。

## 11. Speculative abstraction

只有一个 provider。
Builder 创建 protocol + factory + registry + adapter hierarchy，
无 Architect extension point。

期望：
若只增加不必要复杂度但仍正确，可 CONCERN；
若违反 Engineering Standard “no speculative abstraction”，则 FAIL。

## 12. Change Locality

改 reward 规则需要同时改 UI、API handler、job、DB trigger 四套判断。

期望：
确认四处为 independent decision sites 后 FAIL Semantic Unity。
不能只因为“改了四个文件”判错。

## 13. 多模块但合理

一次支付能力真实触及 Checkout、Wallet、Inventory 三个 owner，
通过各自 public interface。

期望：
Modular Integrity PASS。
不能机械使用“>3 modules”判 FAIL。

## 14. New Shared Helper Sensor

新增 `Shared/DateUtils`，实际是纯技术日期 parser，无业务 owner。

期望：
检查后 PASS。

## 15. Boundary bypass

Feature A import Feature B internal repository。

Architecture 禁止 feature-internal cross import。

期望：
FAIL。

## 16. Product / Architecture 正确，Blueprint 错

Binding Atom 要求修改原对象。
Blueprint Task 却规划创建 copy。

期望：
REPLAN_BLUEPRINT。
Verifier 不自己写新 Blueprint。

## 17. Architecture 缺 Authority

Current requirement 需要共享 ownership，
Architecture 没定义谁可 mutation。

期望：
REPLAN_ARCHITECTURE。
不让 Builder 猜。

## 18. Product 变化

用户现在决定“分享必须复制副本”，
而 Product Atom / Stage 都是 same-object collaboration。

期望：
PRODUCT CHANGE。

## 19. Evidence 缺失

代码看起来正确，
但 Acceptance 需要真实 migration result，未运行。

期望：
VERIFICATION BLOCKED，而不是代码 FAIL。

## 20. Findings Freeze

首次发现 F-01/F-02。
修复后 reviewer 顺手看到无关旧模块命名差。

期望：
不新增普通 Finding。

## 21. 修复直接回归

修 F-01 后直接破坏 current Stage public API。

期望：
允许新增 REGRESSION-01。

## 22. PASS Stop

全部 Finding resolved、evidence complete。

期望：
PASS 并立即停止。
不得继续“再找一轮”。

## 23. 删除残留

旧 API 已明确被替换，
active repo 仍保留 alias + fallback + old test。

没有 compatibility requirement。

期望：
Finding。

## 24. Human visual authority

UI 机械约束满足。
Reviewer 没有真实视觉 evidence。

期望：
不能宣称“视觉很好 / premium / Visual QA PASS”。

## 25. Existing evidence reuse

Builder 已运行 targeted integration test，结果新鲜、范围匹配、日志完整。

Reviewer 无新 uncertainty。

期望：
直接消费 evidence，不重跑。

## 26. Hypothetical risk

Reviewer 想到“未来 10M 用户可能慢”。

当前无 scale requirement / profiling / expensive path evidence。

期望：
不是 Finding。

## 27. Public API expansion

Task 为一个内部 use case 新增 8 个 public setters 暴露内部 state。

期望：
Structural Health FAIL，说明 encapsulation / owner bypass 风险。

## 28. Representative Example

Product example：
引用“买牛奶”→ AI 改“买牛奶和面包”→确认→原卡片更新。

实现实际新建了一张卡。

期望：
Semantic FAIL。

## 29. Mechanical scope

Blueprint Expected Change Boundary 是 Reward + Wallet。
实现还重构了 unrelated Search 模块，没有 requirement / dependency 原因。

期望：
Scope Finding。

## 30. Concern 不触发修复循环

某函数参数 6 个，当前 responsibility 仍清楚。

期望：
最多 CONCERN；Stage 可 PASS。

# Stage Verifier v3 Evals

## 1. Product Atom 丢失
Scenario: Atom 要求 AI 看到引用实际内容；实现只传 `referenceId`。
Pass: Semantic FAIL；ID traceability 不算语义覆盖。

## 2. 双 Authority
Scenario: Wallet owns balance mutation；Purchase 直接 update balance，Wallet 也有 debit API。
Pass: FAIL — Semantic Unity / Modular Integrity。

## 3. 合法 Projection
Scenario: Server 是 permission authority；Client 只消费 `canEdit` 控制按钮。
Pass: 不误判为双 authority。

## 4. Shared 垃圾场
Scenario: Reward 规则有明确 Reward owner，却搬到 `Shared/RewardUtils`。
Pass: FAIL；理由是 ownership 被破坏，不是目录名本身。

## 5. 语法重复但语义不同
Scenario: 两个 Domain 都有 `isExpired()`，规则不同。
Pass: 不为 DRY 强行抽象。

## 6. Work Efficiency — N+1
Scenario: 100 项 loop 内逐项 DB query，已有 batch API。
Pass: FAIL，并说明真实多余工作。

## 7. Micro optimization
Scenario: 20 项内存数组多扫一次，无 budget / profiling / live issue。
Pass: 不是 Finding。

## 8. Complexity Sensor
Scenario: 70 行线性单职责函数。
Pass: Sensor / Concern 可成立，不能仅凭行数 FAIL。

## 9. 真复杂
Scenario: validation + fetch + permission + mutation + DB + event，嵌套 5 层。
Pass: Structural Health / Maintainability FAIL 或明确 MAJOR，并指出责任混合影响。

## 10. Error Swallowing
Scenario: backend error 被 catch 成空数组，产品显示“没有数据”。
Pass: Correctness FAIL。

## 11. Speculative abstraction
Scenario: 单 provider 却创建 protocol + factory + registry + adapters，无 architecture extension point。
Pass: 仅复杂度可 Concern；若违反已批准 no-speculative-abstraction 标准则 FAIL。

## 12. Change Locality
Scenario: 改 reward rule 必须改 UI/API/job/DB trigger 四套独立判断。
Pass: 确认是 independent decision sites 后 FAIL；不能仅因“改四个文件”判错。

## 13. 多模块但合理
Scenario: Checkout/Wallet/Inventory 三 owner 通过 public interface 协作。
Pass: Modular Integrity PASS。

## 14. New Shared Helper Sensor
Scenario: `Shared/DateUtils` 是纯技术 parser，无业务语义 owner。
Pass: 检查后可 PASS。

## 15. Boundary bypass
Scenario: Feature A import Feature B internal repository，Architecture 明确禁止。
Pass: FAIL。

## 16. Product / Architecture 正确，Blueprint 错
Scenario: Atom 要求修改原对象；Blueprint 规划创建 copy。
Pass: `REPLAN_BLUEPRINT`；Verifier 不自己重写 Tasks。

## 17. Architecture 缺 Authority
Scenario: requirement 需要共享 mutation，但 Architecture 未定义 owner。
Pass: `REPLAN_ARCHITECTURE`；不让 Builder / Verifier 猜。

## 18. Product 变化
Scenario: 用户改为“分享必须复制副本”，现有 Product/Stage 是 same-object collaboration。
Pass: `PRODUCT CHANGE`。

## 19. Evidence 缺失
Scenario: code 看似正确，但 Acceptance 需要真实 migration evidence，未运行。
Pass: `VERIFICATION BLOCKED`，不是代码 FAIL。

## 20. Findings Freeze
Scenario: 初审冻结 F-01/F-02；修复后看到无关旧模块命名差。
Pass: 不新增普通 Finding，不修它。

## 21. 修复直接回归
Scenario: 修 F-01 直接破坏 Current Stage public API。
Pass: 可新增 `REGRESSION-01`。

## 22. PASS Stop
Scenario: Reconciliation 完成，全部条件满足。
Pass: `PASS — Stage Review Closed` 并立即停止；不得“再找一轮”。

## 23. 删除残留
Scenario: 旧 API 已被替代，无 compatibility requirement，却保留 alias + fallback + old test。
Pass: Finding；Required Delete / Remove 必须覆盖。

## 24. Human visual authority
Scenario: 机械 UI constraint 满足，但没有真实视觉 evidence。
Pass: 不宣称 Visual QA / premium PASS。

## 25. Existing evidence reuse
Scenario: Builder 已有新鲜、范围匹配 targeted integration evidence，Reviewer 无新 uncertainty。
Pass: 直接消费，不重跑。

## 26. Hypothetical risk
Scenario: “未来 10M 用户可能慢”，无 scale requirement / profiling / expensive-path evidence。
Pass: 不是 Finding，也不授权继续测试。

## 27. Public API expansion
Scenario: 内部 use case 新增 8 个 public setters 暴露内部 state。
Pass: Structural Health FAIL，并指出 encapsulation / owner bypass 风险。

## 28. Representative Example
Scenario: 产品例子要求确认后更新原卡；实现新建另一张卡。
Pass: Semantic FAIL。

## 29. Mechanical scope
Scenario: Expected Change Boundary 是 Reward + Wallet；实现还重构 unrelated Search。
Pass: Scope Finding。

## 30. Concern 不触发 Repair
Scenario: 函数参数 6 个但责任仍清楚。
Pass: 最多 Concern；不进入 Repair Handoff。

## 31. 多 Finding 单根因
Scenario: Purchase 直接写 balance、UI 独立判断 insufficient、Wallet.debit 未使用；Wallet 是 authority。
Pass: Repair Handoff 形成一个 Root Cause Group：恢复 Wallet authority + 清除 duplicate path；不机械形成三个 patch。

## 32. Repair Handoff 粒度
Scenario: Finding 为 Reward eligibility 重复 authority。
Pass: Handoff 必须有 Frozen Findings、Root Cause、Upstream Basis、Target State、Allowed Boundary、Delete/Remove、Required Proof、Stop Gate；不得只有“统一 Reward 逻辑”。

## 33. Architecture Finding 不得硬修
Scenario: ownership 本身未定义。
Pass: `REPLAN_ARCHITECTURE`；不生成猜测性 Repair Handoff 施工细节。

## 34. Blueprint Finding 回流 Construction Blueprint
Scenario: Product / Architecture / Stage 正确；原 Blueprint 规划 direct DB write，违反 Wallet authority。
Pass: `REPLAN_BLUEPRINT` + Repair Handoff；Next Action 明确 Route to Construction Blueprint / Repair Mode；Verifier 不自己生成 Repair Tasks。

## 35. Evidence Block 不是 Repair
Scenario: 实现可能正确，只缺真实 migration evidence。
Pass: Evidence Acquisition Plan；不生成 Repair Handoff / code Tasks。

## 36. Repair 删除旧路径
Scenario: 正确 authority 恢复后旧 helper / alias / fallback 无兼容责任。
Pass: Handoff 的 Required Delete / Remove 明确列出；Construction plan 必须消费。

## 37. Repair 只要求受影响 proof
Scenario: F-01 只影响 Purchase capability。
Pass: Handoff 只要求必要 local / affected capability / direct regression proof，不要求全 Stage 重跑。

## 38. Concern 不进入 Repair Boundary
Scenario: Quality Matrix 有非阻断 Concern。
Pass: Explicit Non-Scope；不能偷偷修。

## 39. Verifier 不创建 Repair Task ID
Scenario: repair 需要多步施工。
Pass: Verifier 只输出 Handoff；不得创建 `Repair Task 1`、`Patch-n` 或长期 Task ID。

## 40. Repair Planning 发现新 Architecture Decision
Scenario: 正确修复需要新增长期 Billing authority。
Pass: 立即 `REPLAN_ARCHITECTURE`；不继续 blueprinting。

## 41. 无 Action Basis 必须停
Scenario: Frozen Findings 已有足够 proof，Reviewer 想再搜相邻模块“保险一下”。
Pass: Action Ticket 无合法 basis ⇒ MUST STOP。

## 42. Action Ticket 不完整
Scenario: Reviewer 写 `Action Basis: REQUIRED_PROOF`，但说不出具体 Unknown、Decision Impact 或 Stop After。
Pass: 动作 inadmissible，不执行。

## 43. 新测试必须改变判断
Scenario: 已有 targeted evidence；Reviewer 想跑 full suite，但即使失败也不能说明 F-01 是否 resolved。
Pass: 不运行；缺乏 Decision Impact。

## 44. 无关 confirmed defect 在 Freeze 后出现
Scenario: Fix Review 阅读 direct caller 时看到另一个无关模块的真实 bug。
Pass: 记录 `Deferred Observation`；不加入 Frozen Findings、不修、不扩搜。

## 45. Late Critical Evidence 不追加 Finding
Scenario: 冻结后外部系统提供新证据，证明一个原已存在的 Current Stage BLOCKER。
Pass: `REVIEW CYCLE INVALIDATED — NEW REVIEW REQUIRED`；关闭旧 cycle，不追加 F-N+1。

## 46. Repair Boundary 不是最小 diff
Scenario: 根因修复必须删除 duplicate authority、改两个 caller、更新直接 test。
Pass: 全部允许；不能为了“小 diff”留下错误现实。

## 47. REPAIR VERIFIED 后不得继续改代码
Scenario: Findings 清零且 required proof 足够；Reviewer 又想到 cleanup。
Pass: 输出 `REPAIR VERIFIED`，唯一 Next Action 是 Stage Reconciliation。

## 48. Repair 期间 canonical Stage 文档只读
Scenario: Builder 修完一半，想同步改 `docs/blueprint/stages/Stage-3.md`。
Pass: 禁止；中间状态只写 Repair Workspace。

## 49. Repair Workspace 独立
Scenario: 项目无其他约定。
Pass: repair docs 进入 `.workbench/repairs/Stage-<N>/`，不创建第二份 canonical Stage doc。

## 50. Repair Execution 必须由 Construction Blueprint 编译
Scenario: Verifier 已有完整 Handoff，觉得修法明显。
Pass: 仍然 Route；Verifier 不复制 Task/Reasoning/Delegation/Parallel/Verification schema。

## 51. Repair Execution 与正常 Blueprint 同颗粒度
Scenario: Construction Blueprint Repair Mode 只输出“改 Wallet、跑测试”。
Pass: FAIL receiver contract；必须使用正常 Task granularity / planning gates，只是范围更窄、文档临时。

## 52. Stage Reconciliation 只在 Repair Verified 后
Scenario: Findings 尚未全部 resolved，想先把 Stage doc 更新成“预计最终状态”。
Pass: 禁止。

## 53. Reconciliation 不保留修复历史
Scenario: canonical Stage doc 追加“原 Task → F-01 → patch 1 → patch 2 → final”。
Pass: FAIL；应删除 superseded content，只保留最终有效施工事实。

## 54. Reconciliation 不重写无关部分
Scenario: Repair 只影响 Wallet Task，Reconciliation 顺便整理 Search/Analytics Stage 章节。
Pass: 禁止；只改 Reconciliation Contract 指定范围。

## 55. Bounded Reconciliation Check
Scenario: Stage doc 已更新。Verifier 在 closure check 时想重新打开代码全审。
Pass: 禁止；只核对 reconciliation targets、superseded removal、final reality 一致性。

## 56. PASS Seal
Scenario: 最终 PASS 后同一实现无变化，Reviewer 又重新打开 repo。
Pass: violation；旧 cycle 已封闭。

## 57. PASS 后新代码变化
Scenario: PASS 后又有 implementation change。
Pass: 可以开启新的 Review Cycle；不能续接旧 Finding Set。

## 58. Historical Stage 不回写
Scenario: Repair 开始前 Stage 已正式 frozen / historical。
Pass: 不修改历史 Stage doc；Route 到新的 maintenance / repair work unit。

## 59. Workspace Closure
Scenario: Reconciliation check PASS，无 audit retention requirement。
Pass: 删除 Repair Workspace，不把它留成第三套长期 SoT。

## 60. Audit retention
Scenario: 项目有明确 compliance retention requirement。
Pass: Workspace 可归档，但必须 `CLOSED / NON-AUTHORITATIVE`，不能参与后续 active authority resolution。

# Repository Intake

目标：只扫描 Current Stage 真正需要的仓库范围，同时取得足够真实信息做确定性计划。

## 递进扫描

从 Authorized Scope、Project Structure、Included Requirement、Entry State 和 direct dependencies 定位第一批文件，再按真实依赖扩大：
1. 直接目标 file/module。
2. callers / callees。
3. shared interface / schema / state。
4. tests / fixtures / migrations / config。
5. external provider integration。
6. generated artifact source。
7. 只有发现真实依赖才继续扩大。

不要一开始全仓库 grep 或建立“全项目知识图谱”。

## 必须确认的现实

**实现**：Path、Symbol/type/function/route/view/handler、ownership/module boundary、Domain Owner/Semantic Authority、public/internal boundary、必须复用的 policy/repository/service/helper。

**数据**：schema/model、migration history、source of truth、read/write path、上游已冻结的 consistency/transaction boundary。

**接口**：public/internal contract、version/compatibility、generated client/schema source。

**运行**：config/environment、provider init、queue/job/scheduler/realtime、feature flag/rollout（适用时）。

**测试**：现有 target、最小 selector、integration environment、known flaky/slow suite。

**工具**：只记录真实可执行的 build、lint/typecheck、targeted test、migration check、schema generation 等；不猜脚本名。

## Authority / Reuse Intake

只针对 Current Stage 触及的事实确认：
- 谁拥有规则与 canonical authority。
- 外部正确 public path。
- 哪些直接访问会 bypass owner。
- 是否已有同语义实现。
- 正常变化应落在哪个 owning domain。

若两个独立位置已在决定同一核心业务事实，这是 Repository Reality 冲突；不要规划第三套。

## 旧实现默认继承

已有模式默认继承，除非与 Stage Contract、Architecture/Standards 冲突，已证明无法支持本 Stage，或上游 Decision 明确替换。不要因“有更漂亮写法”顺手重构。

## 仓库现实冲突

Blueprint 可吸收：
- 文件名/symbol 与文档略有差异但语义兼容。
- 已批准边界内存在多种低成本机械路径。
- 现有 helper/component 可替代原计划新建。

回 Architecture：
- data/interface/module boundary 不同。
- Domain Ownership / Semantic Authority 不明确或冲突。
- 需要新增长期 module/owner/authority/dependency direction。
- Provider/platform 或 migration/compatibility 前提不同。
- Stage Scope 在现结构中无法成立。

回 Product：
- 真实实现暴露未定义的用户状态、失败含义、权限、不可逆行为等产品语义。

## Entry State

只写后续 Task 依赖的事实，具体到真实 path/symbol/caller/state；禁止“模块基本完成，后续需完善”式泛述。

扫描结束应能回答：从哪里改、谁调用、触达什么、最小验证命令、哪些真边界需 Slice 验证、哪些 authority/public path 必须复用、哪些 bypass 禁止、Expected Change Boundary 在哪里、是否存在上游冲突。

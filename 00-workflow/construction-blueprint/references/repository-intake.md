# Repository Intake

目标：让蓝图只扫描 Current Stage 真正需要的仓库范围，同时获得足够真实信息做确定性计划。

## 起点

先从上游给出的：

- Authorized Scope
- Architecture / Project Structure
- Included Requirement-n
- Entry State
- direct dependencies

定位第一批文件。

不要一开始全仓库 grep 所有东西。

## 递进扫描

按以下顺序扩大：

1. Current Stage 直接目标文件 / module。
2. callers / callees。
3. shared interface / schema / state。
4. tests / fixtures / migrations / config。
5. external provider integration。
6. generated artifact source。
7. 只有发现真实依赖时再扩大。

## 必须确认的现实

### 实现位置
- 实际 Path。
- Symbol / type / function / route / view / handler。
- ownership / module boundary。
- 现有 Domain Owner / Semantic Authority。
- public entry / internal boundary。
- 是否已有必须复用的 policy / repository / service / helper。

### 数据
- schema / model。
- migration history。
- source of truth。
- write / read path。
- consistency / transaction boundary（只读上游结论）。

### 接口
- public / internal interface。
- version / compatibility。
- generated client / schema source。

### 运行
- config / environment。
- provider SDK 初始化。
- queue / job / scheduler / realtime path。
- feature flag / rollout（适用时）。

### 测试
- 现有 test target。
- 最小可运行 selector。
- integration environment。
- known flaky / slow suite。

### 工具命令
只写真实可执行命令，例如：

- build
- lint / typecheck
- targeted test
- migration check
- schema generation

不猜不存在的脚本名。

## Authority / Reuse Intake

只针对 Current Stage 触及的业务事实，确认：

- 当前规则由谁拥有。
- 当前 canonical authority 在哪。
- 哪个 public path 是外部正确入口。
- 哪些直接访问会绕过 owner。
- 是否已经存在相同语义的实现。
- 正常变化应主要落在哪个 owning domain。

不要为了建立“全项目知识图谱”扫描全仓。

若发现两个独立位置已经在决定同一核心业务事实，这属于 Repository Reality，应报告给 Blueprint / Architecture；不要在计划中默认继续复制第三套。

## 旧实现默认继承

已有项目的实现模式默认继承，除非：

- 与 Stage Contract 冲突。
- 违反当前 Architecture / Engineering Standards。
- 已经证明无法支持本 Stage。
- 上游 Decision 明确要求替换。

Blueprint 不因为“有更漂亮写法”顺手重构。

## 仓库现实冲突

如果仓库与上游冲突：

### Blueprint 可吸收
- 文件名 / symbol 与文档略有差异但语义兼容。
- 已批准边界内有多种低成本机械路径。
- 现有 helper / component 可替代原计划新建。

### 回 Architecture
- data / interface / module boundary 不同。
- Domain Ownership / Semantic Authority 不明确或互相冲突。
- Current Stage 需要新增长期 module / owner / authority / dependency direction。
- Provider / platform 不同。
- migration / compatibility 前提不同。
- Stage Scope 无法在当前结构中成立。

### 回 Product
- 真实实现暴露产品语义缺口，例如用户状态、失败含义、权限或不可逆行为未定义。

## Entry State 写法

只记录后续 Task 依赖的事实。

好的：

> `UserRepository.save()` 当前直接写 `users` 表；`UserService.create()` 是唯一 caller；没有现成 soft-delete 状态。

差的：

> 用户模块目前基本完成，但后续需要完善。

## 目标

扫描结束后，Blueprint 应能回答：

- 从哪里改。
- 谁调用它。
- 改动会触达什么。
- 最小验证命令是什么。
- 哪些真实边界需要 Slice 层验证。
- 哪些现有 authority / public path 必须复用。
- 哪些 bypass 必须禁止。
- Expected Change Boundary 在哪里。
- 是否存在需要上游重审的冲突。

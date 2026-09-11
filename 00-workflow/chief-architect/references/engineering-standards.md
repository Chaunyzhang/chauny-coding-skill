# Engineering Standards

用于制定 `docs/architecture/ENGINEERING_STANDARDS.md`。

目标：冻结真正需要跨 Stage、跨模块、跨开发者统一的规则；不要把项目规范写成语言教程或代码风格百科。

## 写入原则

一条规则只有满足至少一个条件才进入全项目标准：

- 不统一会造成数据或接口语义不一致。
- 不统一会造成安全 / 隐私风险。
- 不统一会造成跨模块维护困难。
- 不统一会造成兼容 / 迁移事故。
- 不统一会让 Observability / Testing 失真。
- 同类问题会在多个 Stage 重复出现。

否则优先交给：

- 语言官方惯例
- formatter / linter
- framework conventions
- 局部模块 README
- Blueprint / implementation choice

不使用 `ES-n`。需要引用时使用：

`ENGINEERING_STANDARDS.md § <Section>`

## 建议章节

### 1. Naming

只规定跨边界命名：

- module / package
- API field / endpoint
- database table / column
- event name
- public type / contract

局部变量和私有 helper 优先服从语言惯例和 lint。

事件名与错误码各自钉死一个全项目模式，写进本文件并作为唯一权威；注册表 / 契约必须与本文件一致，偏离只能在注册表显式标注为由架构裁决的例外，不得两套模式并存。

### 2. Repository & Module Boundaries

明确：

- Domain / Feature / Module responsibility
- dependency direction
- public / internal boundary
- cross-module import rules
- owned state / rules / lifecycle
- generated artifacts ownership
- migrations / schema / config / test 归属

模块不是目录名。必须能说明：

> 它拥有什么业务知识？外部通过什么公开入口与它合作？哪些内部事实不允许被外部直接依赖？

禁止：

- 通过相对路径、global singleton、raw database access 或 shared util 绕开模块边界。
- Feature A 直接 import / 调用 Feature B 的内部实现。
- 外部直接修改另一个 Domain 拥有的 state。
- Blueprint / Construction 在未经过 Architecture 裁决时创建新的长期模块边界。

### 3. Domain Ownership & Semantic Authority

对跨 Stage 稳定的核心业务规则，明确：

- Domain Owner
- Owned State / Entity / Lifecycle
- Mutation Authority
- Decision Authority
- Public Capability

核心原则：

> 同一产品 / Domain 事实只允许一个 Semantic Authority 决定。

典型 authority：

- balance mutation
- reward calculation
- permission
- state transition
- public error code
- canonical schema
- identity mapping

允许缓存、投影、展示和机械转换；不允许第二套独立规则实现。

判断双权威的强信号：

- 改一条业务规则必须在多个互不依赖的位置修改决定逻辑。
- 两个模块都能独立 mutation 同一核心 state。
- Client 与 Server 各自决定同一最终 permission / balance / eligibility。
- 新代码绕过已有 policy / repository / domain service 重新写 `if` 判断。

### 4. Reuse Before Create

默认顺序：

1. 找现有 owner。
2. 找现有 public interface / policy / repository / service。
3. 判断现有抽象是否真正承载相同语义。
4. 只有出现真实新责任 / 新变化轴时才创建新长期抽象。

禁止：

- 因“不想动旧代码”复制一套等价规则。
- 因“两处会用”就自动抽到 Shared。
- 为假想未来创建 factory / provider / registry / strategy 层级。

### 5. Shared / Common Policy

`Shared / Common / Utils / Helpers` 只承载没有业务 owner 的真正通用技术能力。

有明确 Domain 归属的业务逻辑，即使多个调用方使用，也仍属于该 Domain，通过 public API 复用。

Shared 不得成为：

- 不知道放哪的临时区。
- 跨 Feature 私有逻辑的混合区。
- 绕过 dependency direction 的跳板。

### 6. Change Locality / Modular Health

架构目标不是“所有变更只改一个文件”，而是：

> 一项正常产品变化应主要局限在 owning domain；无关模块不应因为不了解该业务却被迫同步修改规则。

Review sensor：

- 修改一个业务规则是否需要改多个独立 authority。
- 新 Requirement 是否触碰大量无关模块。
- 理解一个业务是否必须全仓搜索并拼装逻辑。
- 删除一个 Feature 是否会让大量无关区域报错。
- 模块 public API 是否不断扩大以暴露内部细节。

这些是 smell，不是单独的自动 FAIL；只有能指出真实责任泄漏 / 双权威 / 依赖腐化时才升级为 Finding。

### 7. State Mutation & Side-effect Ownership

核心 state 必须有明确 mutation owner。

其他模块通过 owner 暴露的 capability 请求变化，不直接：

- 写 owner 数据表。
- 改内部缓存 / state container。
- 触发 owner 私有生命周期转换。

Side effect（DB write、network call、event emission、payment、notification）应在可追踪边界发生，不隐藏在名字像 pure getter / mapper 的函数里。

### 8. Work Efficiency

全局只规定会反复造成真实成本的规则：

- 避免 N+1。
- 避免同一 request / action 内无理由重复 DB / network / parse / serialization。
- 可批量且语义等价时避免逐项远程调用。
- expensive operation 在已有 canonical cache / batch / index 时不得绕开。
- transaction / lock 不包裹无关网络调用或长耗时工作。

不要为普通局部代码做 micro-optimization。

### 9. Complexity & Abstraction

数字阈值只能当 sensor，例如：

- function length
- nesting depth
- parameter count
- cyclomatic complexity

除非项目明确冻结阈值，否则数字本身不能成为 FAIL。

真正要审的是：

- 是否承担多个独立责任。
- 是否让控制流难以理解。
- 是否制造 speculative abstraction。
- 是否让一个简单产品变化需要理解不相关框架层。

### 3. Dependency Policy

第三方依赖引入至少检查：

- 维护活跃度
- license
- 安全历史
- 传递依赖
- 替换成本
- 是否已有平台原生能力

规则应包含：

- lockfile 入库
- 安全补丁处理纪律
- 重大版本升级策略
- 高风险依赖的额外审查条件

### 4. API / Interface

至少统一：

- public contract SoT
- path / method / naming
- error envelope / error code
- pagination / filtering / sorting
- idempotency
- version / deprecation
- time / money / enum serialization

禁止 ORM entity 直接成为长期公共契约。

### 5. Data

按项目实际冻结：

- ID 策略
- time / timezone 语义
- money / currency 精度与舍入
- enum evolution
- nullability
- soft / hard delete
- audit fields
- transaction boundary
- System of Record / derived data
- schema migration discipline

典型全局规则：

- 时间存储使用统一标准；需要原时区语义的字段显式保存时区。
- 金额使用整数最小货币单位或 Decimal，不用浮点。
- 业务唯一性由 DB constraint 兜底，而不是只靠先查后写。

### 6. Error Handling

统一：

- validation / auth / permission / business / system 分类
- stable error code
- internal exception 与 user-facing message 分离
- retryable / non-retryable 语义
- correlation context
- sensitive detail redaction

禁止把原始内部异常直接返回用户。

**错误码与用户文案所有权**：错误码是对外契约，由服务端唯一所有，命名与语义稳定，客户端逻辑只依赖错误码、不依赖文案。面向用户的错误文案是表现层，由各客户端唯一所有，集中为一张「错误码 → 文案」对照表（single source），禁止在业务代码内联硬编码提示串；服务端返回的 message 只作兜底（未知码、非 App 渠道、调试）。改文案只改说法，不得改变错误码语义。新增错误路径必须同时登记错误码与各端文案条目；客户端遇到表中没有的错误码应显式上报，不得静默兜一句。

### 7. Security

至少覆盖：

- authentication / authorization boundary
- server-side permission enforcement
- input validation
- secret storage
- sensitive data handling
- least privilege
- admin / support access
- dangerous operation confirmation / audit

客户端缓存的权限信息只能用于 UI，不作为最终授权依据。

### 8. Observability

只冻结可复用规则：

- structured logging level / fields
- event naming / version
- error / crash context
- correlation IDs
- PII / secret redaction
- environment tagging
- sink initialization responsibility

具体 Stage 观测内容放 Stage Contract，不写进全局标准。

### 9. Testing

统一三层边界：

- Task 简单测
- Slice 能力功能测
- Stage 模块测

并定义：

- unit / integration / E2E 的适用边界
- real sandbox vs mock 原则
- flaky test 处理
- test data isolation
- CI 中不同测试的运行时机

不要规定“所有测试每次都跑”。

### 10. Compatibility & Migration

统一 breaking-change 定义和弃用流程，覆盖：

- API
- database schema
- events
- client compatibility
- config

数据库破坏性变更通常遵循：

`expand → migrate / backfill → switch reads/writes → contract`

### 11. Third-party Boundary

跨 Provider 统一：

- timeout
- retry
- idempotency
- circuit / fallback when applicable
- credential boundary
- error normalization
- provider-specific code isolation

### 12. Documentation

规定何时必须同步：

- ARCHITECTURE
- TECH_STACK
- PROJECT_STRUCTURE
- ENGINEERING_STANDARDS
- EXTERNAL_SERVICES
- OBSERVABILITY
- DECISIONS
- ROADMAP / Stage Contract

不要要求每个代码改动都更新架构文档；只有架构事实变化才更新。

## 审查原则

架构师制定标准后不持续扫描全仓库执法。

Blueprint 只引用本 Stage 适用章节；Construction 遵守；Verifier 只检查本次变更触达范围和明确的直接回归。

全仓规范审计只有在：

- 用户明确要求
- 安全 / 数据事故
- 大规模迁移
- 架构重组
- lint / static analysis 发现系统性问题

时单独执行。

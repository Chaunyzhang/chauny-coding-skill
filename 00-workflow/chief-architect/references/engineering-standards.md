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

- dependency direction
- public / internal boundary
- cross-module import rules
- generated artifacts ownership
- migrations / schema / config / test 归属

禁止通过相对路径、global singleton 或 shared util 绕开模块边界。

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

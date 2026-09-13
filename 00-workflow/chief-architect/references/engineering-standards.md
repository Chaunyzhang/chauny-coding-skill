# Engineering Standards

用于制定 `docs/architecture/ENGINEERING_STANDARDS.md`。只冻结跨 Stage / 模块 / 开发者必须统一的规则，不写成语言教程或代码风格百科。

## 写入原则

一条规则只有在不统一会造成数据 / 接口语义不一致、安全 / 隐私风险、跨模块维护困难、兼容 / 迁移事故、Observability / Testing 失真，或会在多个 Stage 反复出现时，才进入全项目标准。

否则优先交给语言惯例、formatter / linter、framework convention、局部模块 README、Blueprint / implementation choice。

不使用 `ES-n`；引用方式：`ENGINEERING_STANDARDS.md § <Section>`。

## 1. Naming

只规定跨边界命名：module / package、API field / endpoint、DB table / column、event、public type / contract。局部变量 / private helper 服从语言惯例和 lint。

事件名与错误码各有一个全项目模式并作为唯一权威；注册表 / 契约必须一致。例外必须显式由 Architecture 裁决，不能两套模式并存。

## 2. Repository & Module Boundaries

必须明确 Domain / Feature / Module responsibility、dependency direction、public/internal boundary、cross-module import、owned state / rules / lifecycle，以及 generated / migration / schema / config / test 归属。

模块不是目录名。必须能回答：它拥有什么业务知识？外部通过什么 public capability 合作？哪些内部事实不能被外部直接依赖？

禁止：

- 通过 relative path、global singleton、raw DB access 或 shared util 绕过边界。
- Feature A 直接依赖 Feature B internal implementation。
- 外部直接 mutation 另一个 Domain 的 state。
- Blueprint / Construction 未经 Architecture 裁决创建新的长期模块边界。

## 3. Domain Ownership & Semantic Authority

对跨 Stage 稳定核心业务规则明确 Domain Owner、Owned State / Entity / Lifecycle、Mutation Authority、Decision Authority、Public Capability。

核心原则：**同一产品 / Domain 事实只允许一个 Semantic Authority 决定。**

典型 authority：balance mutation、reward calculation、permission、state transition、public error code、canonical schema、identity mapping。

允许 cache / projection / display / mechanical transform；禁止第二套独立决定逻辑。

双权威强信号：一条业务规则要改多个互不依赖位置；两个模块都能 mutation 同一核心 state；Client / Server 各自决定同一最终 permission / balance / eligibility；新代码绕过已有 policy / repository / domain service 重写判断。

## 4. Reuse Before Create

默认顺序：

1. 找现有 owner。
2. 找现有 public interface / policy / repository / service。
3. 判断现有抽象是否承载相同语义。
4. 只有出现真实新责任 / 新变化轴才创建新长期抽象。

禁止因“不想改旧代码”复制等价规则；禁止因“两处会用”自动抽 Shared；禁止为假想未来创建 factory / provider / registry / strategy 层级。

## 5. Shared / Common Policy

`Shared / Common / Utils / Helpers` 只承载无业务 owner 的真正通用技术能力。有明确 Domain 归属的业务逻辑即使多处使用，也留在 Domain，通过 public API 复用。

Shared 不能成为“不知道放哪”的临时区、跨 Feature 私有逻辑混合区或绕过 dependency direction 的跳板。

## 6. Change Locality / Modular Health

目标不是“任何变更只改一个文件”，而是：正常产品变化主要局限于 owning domain，无关模块不因不了解该业务而被迫同步修改规则。

Review sensor：修改一条业务规则是否触及多个独立 authority；新 Requirement 是否触碰大量无关模块；理解一个业务是否必须全仓拼装逻辑；删除 Feature 是否破坏大量无关区域；public API 是否持续扩大暴露内部细节。

这些是 smell，不单独自动 FAIL；只有能指出责任泄漏、双权威或依赖腐化时升级为 Finding。

## 7. State Mutation & Side-effect Ownership

核心 state 有明确 mutation owner；其他模块通过 owner public capability 请求变化，不直接写其数据表、内部 cache/state container 或触发私有 lifecycle transition。

DB write、network call、event emission、payment、notification 等 side effect 必须发生在可追踪边界，不隐藏在名字像 pure getter / mapper 的函数中。

## 8. Work Efficiency

只冻结会反复造成真实成本的规则：避免 N+1；同一 request/action 不无理由重复 DB/network/parse/serialization；语义等价时批量优于逐项 remote call；已有 canonical cache/batch/index 时不绕开；transaction/lock 不包裹无关网络或长耗时工作。

不为普通局部代码做 micro-optimization。

## 9. Complexity & Abstraction

function length、nesting depth、parameter count、cyclomatic complexity 等数字默认只是 sensor；除非项目明确冻结阈值，否则数字本身不能成为 FAIL。

真正审查多责任、难理解控制流、speculative abstraction，以及简单产品变化是否被迫理解不相关框架层。

## 10. Dependency Policy

第三方依赖至少检查 maintenance、license、security history、transitive dependencies、replacement cost、是否已有平台原生能力。

全局规则应明确 lockfile、security patch、major-version upgrade 和高风险依赖额外审查条件。

## 11. API / Interface

统一 public contract SoT、path/method/naming、error envelope/code、pagination/filter/sort、idempotency、version/deprecation、time/money/enum serialization。ORM entity 不直接成为长期公共契约。

## 12. Data

按项目实际冻结 ID、time/timezone、money/currency precision/rounding、enum evolution、nullability、soft/hard delete、audit fields、transaction boundary、System of Record / derived data、schema migration。

典型规则：时间存储统一标准且需要原时区语义时显式保存；金额用 integer minor unit 或 Decimal，不用 float；业务唯一性由 DB constraint 兜底而非只靠先查后写。

## 13. Error Handling

统一 validation / auth / permission / business / system 分类、stable error code、internal exception 与 user-facing message 分离、retryable semantics、correlation、sensitive redaction。原始内部异常不得直接返回用户。

**错误码与用户文案所有权**：错误码是服务端唯一拥有的对外契约，客户端逻辑只依赖错误码；用户文案由各客户端表现层拥有，并集中成唯一“错误码 → 文案”映射，不在业务代码散落硬编码。服务端 message 只作未知码 / 非 App 渠道 / 调试兜底。改文案不改变 code 语义；新增错误路径同步登记 code 与各端文案；客户端遇到未知 code 应显式上报。

## 14. Security

至少覆盖 authentication / authorization boundary、server-side permission enforcement、input validation、secret storage、sensitive data、least privilege、admin/support access、dangerous-operation confirmation / audit。客户端缓存 permission 仅供 UI，不作为最终授权依据。

## 15. Observability

只冻结可复用规则：structured logging levels/fields、event naming/version、error/crash context、correlation IDs、PII/secret redaction、environment tags、sink initialization responsibility。具体 Stage 运行义务进入 Stage Contract。

## 16. Testing

统一 Task / Slice / Stage 三层边界，以及 unit/integration/E2E 适用范围、real sandbox vs mock、flaky handling、test-data isolation、CI 运行时机。不要规定“所有测试每次都跑”。

## 17. Compatibility & Migration

统一 API / DB schema / events / client / config 的 breaking-change 与 deprecation 流程。数据库破坏性变化通常遵循：

`expand → migrate/backfill → switch reads/writes → contract`

## 18. Third-party Boundary

跨 Provider 统一 timeout、retry、idempotency、适用的 circuit/fallback、credential boundary、error normalization、provider-specific code isolation。

## 19. Documentation

架构事实变化时同步受影响的 ARCHITECTURE、TECH_STACK、PROJECT_STRUCTURE、ENGINEERING_STANDARDS、EXTERNAL_SERVICES、OBSERVABILITY、DECISIONS、ROADMAP / Stage Contract。普通代码改动不要求更新架构文档。

## 审查原则

Architecture 定义标准后不持续全仓执法。Blueprint 只引用本 Stage 适用章节；Construction 遵守；Reviewer / Verifier 只检查本次变更触达范围与直接回归。

全仓规范审计只在用户明确要求、安全 / 数据事故、大规模 migration、architecture restructuring，或 lint / static analysis 显示系统性问题时单独执行。

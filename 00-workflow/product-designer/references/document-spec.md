# Product Definition 文档规范

用途：规定正式产品事实怎样命名、怎样写入以及哪些内容禁止进入文档。

## 1. 正式文档只有一份

文件：

`docs/product/Product-Definition.md`

它是本 skill 的唯一正式产品输出和当前权威来源。

不得为了整理方便自行创建：

- Interview Notes
- Product Thoughts
- Persona 文件
- Capability Card
- Feature Spec
- Vision 文件
- Constraint 文件
- Research Notes
- Product Decision Log

如果用户明确需要新的文档体系，先由用户决定再改变。

## 2. 命名白名单

### 可长期引用的对象

| 名称 | 写法 | 含义 |
|---|---|---|
| Product Definition | 固定名称 | 产品当前权威定义 |
| Candidate Requirement | `Requirement-n` | 值得提出、但尚未由后续架构角色裁决是否建设的产品提议 |
| Stage | `Stage-n`（仅引用既有） | 架构侧已有建设阶段；本 skill 不创建或修改 |

禁止另造编号前缀和同义对象名。

### 工作标签

`Confirmed / Assumption / Open / Blocking` 是 Agent 工作标签，不是正式产品对象。

最终 Product Definition：

- 不给每条正文加 `Confirmed`。
- 不保存 Assumption 历史。
- 可以保留真正有长期价值的 Open Product Questions。
- 不得带 Blocking 定稿。

## 3. 写入测试

一条内容进入 Product Definition 前，至少满足以下一项：

- 会改变产品是什么或服务谁。
- 会改变用户结果或核心产品闭环。
- 会改变角色、归属、权限、状态、可见性或稳定产品规则。
- 会改变商业关系、价值捕获或持续付费逻辑。
- 会改变 Current Minimum Complete Outcome。
- 会决定某项能力是否属于产品形态或处于什么 Horizon。
- 会约束产品未来演进。
- 会影响后续架构必须考虑的产品模型。
- 是一个必须由后续角色裁决的 Candidate Requirement。
- 是一个尚未解决、但未来必须回来的重要产品问题。
- 是经过可靠外部证据验证、并会实质改变产品决策的市场 / 竞争事实或约束。

反向检查：

> 如果删除这句话，后续产品、架构和建设人员仍然能完全正确理解并建设产品吗？

如果可以，通常不写。

## 4. 明确禁止写入的内容

- 思考过程、Agent 推理链、聊天流水账。
- 用户金句和“某某说过”。
- 被讨论后否定的路线和历史版本，除非它形成明确长期 Non-goal。
- 为了显得完整而虚构的 Persona 年龄、城市、爱好、性格标签。
- 无结论的脑暴清单。
- 市场研究资料堆砌、竞品功能长表、无产品影响的统计数字。
- 页面布局、按钮位置、控件、颜色、普通微文案。
- 具体数据库、接口、模块、协议、技术栈或系统设计。
- 详细施工级异常分支和交互状态，除非某个失败语义本身是稳定产品规则。
- “体验流畅”“简单易用”“行业领先”这类不可判定且没有产品约束的信息。

## 5. 外部事实如何写

市场、竞争、行业和用户行为事实若进入 Product Definition：

- 必须来自可识别来源或用户提供的可靠一手信息。
- 尽量记录来源名称与时间，足以让后续人员知道事实依据。
- 写“产品含义”，不复制研究过程。
- 推断必须与事实分开。

示例：

不写：
`我们查了 8 个竞品，其中 A 有 X，B 有 Y……`

更好：
`同类产品已验证小团队愿意为集中协作与权限控制持续付费；因此团队管理员作为付款者是可行候选，但本产品的具体付费意愿仍需验证。（Evidence: …, date）`

## 6. Product Definition 结构

# Product Definition

## 1. Product Core

写清：

- 产品类别。
- 核心服务对象。
- 核心价值。
- 产品最终改变的用户状态。
- 与主要替代方案相比的本质差异。

要求能形成一句稳定核心定义，但正文不必追求营销文案。

## 2. Users & Outcomes

对主要角色写清：

- Role：角色是什么。
- Real Context：在什么真实处境遇到问题。
- Current Alternative：现在怎样解决。
- Intended Outcome：真正想完成什么。
- Adoption Friction：为什么可能不采用本产品。
- Ownership / Responsibility：若适用，拥有或负责什么。
- Commercial Role：使用者、付款者、管理员是否不同。

这里只记录对产品有影响的行为型用户事实，不写装饰性 Persona。

## 3. Core Product Loop

固定用以下链条说明主闭环：

`Need → Trigger → Entry → Action → Product Response → State Change → Visible Value → Return Reason`

如存在两个本质不同的核心闭环，可分别写；不要把每个功能流程都变成一个“Loop”。

## 4. Product Rules

记录跨功能稳定成立的产品语义，例如：

- 对象与角色的归属关系。
- 关键状态和状态变化。
- 权限与可见性原则。
- 允许 / 禁止的行为。
- 删除、撤回、取消、过期、完成等动作的真实含义。
- 不可逆操作。
- 会影响信任、商业或协作关系的规则。

规则写产品语义，不写技术实现。

## 5. Business Model

如适用，写清：

- Payer：谁付费。
- Value Exchanged：付费对应什么价值。
- Charging Logic：大致按什么对象 / 关系收费；不要求早期给出精确价格。
- Free / Paid Boundary：免费与付费的价值边界。
- Continued Value：价值为什么持续存在。
- Retention / Renewal Logic：为什么持续付费。
- Cost / Scale Constraint：若交付成本或规模形态会明显约束产品，写明产品层面的约束。

如果商业模式尚未确定，但不影响当前产品定义，可以明确 Open；如果不同模式会改变账号、权限、对象或闭环，则为 Blocking，不得假装已经确定。

## 6. Market & Competitive Reality

只记录会改变产品判断的现实信息：

- 目标用户和问题存在的关键证据。
- 用户主要现有替代方案。
- 直接竞品或相邻案例已经验证的行为 / 付费机制。
- 重要切换成本、渠道、市场结构或监管约束。
- Critical Unverified Assumptions：仍需要现实验证、且可能改变模式的重要假说。

不要写完整市场报告或功能对比表。

## 7. Capability Map

每项能力使用统一字段：

```text
Capability:
Classification: Core | Supporting | Expansion
Horizon: Current | Near | Future
Intended Outcome:
Core Behavior:
Key Rule / State Effect: （如有）
Architecture-Shaping: Yes | No
Related Requirement: Requirement-n（如有）
```

规则：

- Classification 和 Horizon 必须分别填写，不能把 Future 当分类。
- 当前能力说明到产品结果和关键产品行为，不展开页面级细节。
- Future 只有 Architecture-Shaping = Yes 时才要求达到行为级。

## 8. Ideal Product State

只记录已经形成意义的长期产品方向：

- 理想角色 / 用户关系。
- 理想核心旅程。
- 主要能力族。
- AI / 自动化边界。
- 协作 / 多端 / 生态方向。
- 长期商业形态。
- 数据 / 所有权 / 权限扩展。
- Explicit Long-Term Non-goals。
- 必须长期保持的产品原则。

不要把宏大愿景口号、所有脑洞和未来功能清单写进来。

## 9. Current Minimum Complete Outcome

定义当前最小但完整的产品成果：

- Outcome：当前真正要形成的用户 / 系统结果。
- Primary Actors：主要参与者。
- Core Journey：从入口到结果的完整旅程概述。
- Must-Have Capabilities：没有它就无法正确形成该成果的能力。
- Required Failure Semantics：缺失会让成果错误、不可信或不安全的重要失败语义。
- Visible Result：怎样观察到成果已经成立。
- Completion Boundary：做到哪里算当前成果完整，什么明确留到后面。

MCO 不是“功能越少越好”。移除任一 Must-Have 后，成果应会变得不成立、错误、不可信或不安全。

## 10. Candidate Requirements

每项统一为：

```text
Requirement-n
Requirement:
Product Rationale:
Related Outcome / Rule:
Horizon: Current | Near | Future
Product Priority:
Architecture-Shaping: Yes | No
```

禁止写后续架构裁决结果。

## 11. Product Evolution & Architecture-Shaping Considerations

写产品逻辑上的成长方向：

- 当前成果之后自然增加什么能力。
- 哪些用户、角色或场景后续进入。
- 哪些能力存在明确前后依赖。
- 当前成果距离 Ideal Product State 还缺什么主要能力族。
- 哪些 Future 方向 Architecture-Shaping = Yes，以及为什么它们可能影响今天的底座。

不写技术 Roadmap，不决定 Stage 顺序。

## 12. Product Acceptance Intent

只写产品层面的可观察完成事实：

- 用户能够完成什么。
- 系统形成什么可见结果。
- 用户如何知道成功。
- 关键失败情况下必须表现为什么。
- 哪些 Product Rules 必须体现。

不写测试脚本和页面级验收用例。

## 13. Open Product Questions

只保留未来必须回来、且对产品有实质影响的问题。

每项写：

- Question。
- Why It Matters。
- What It Could Change。
- Current Best Direction（如有）。

不要把普通待办、UI 细节和研究清单塞进本节。

定稿时 Blocking 必须为 0；Open 可以存在，但剩余未知不得让后续人员误解当前产品。

## 14. Handoff to Architecture

简短列出：

- Product Core。
- Current Minimum Complete Outcome。
- 关键 Product Rules。
- Capability Map。
- Candidate Requirements。
- Product Evolution & Architecture-Shaping Considerations。
- 仍需架构知道的 Open Product Questions。

明确声明：Candidate Requirements 是产品提议；后续架构角色拥有最终范围、拆分、延期、Stage 安排和实现边界裁决权，但保留的产品结果与规则不能被静默改变。

## 7. 更新纪律

- 用户新决定与旧文档冲突：以用户最新明确决定为准，更新受影响章节并检查连锁影响。
- 新想法只影响局部：局部更新，不趁机重写无关产品语义。
- 发现现有产品现实与文档不一致：明确指出，不静默美化。
- 新想法改变 Product Core、关键 Product Rules、Business Model 或 Current MCO：视为重要变更，重新检查相关闭环、能力和候选需求。
- 不保留已经被替代的历史措辞，除非用户明确要求版本记录。

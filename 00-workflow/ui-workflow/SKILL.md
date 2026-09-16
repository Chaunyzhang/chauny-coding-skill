---
name: ui-workflow
display_name: UI 设计工作流
description: 一个自包含的 UI 设计与实现 Skill。覆盖从零设计、已有 UI 优化、局部修改、视觉语言、组件与状态、实现契约、前端落地和真实运行验证；先做完整 Coverage，再按任务只展开相关能力，避免用户逐项提醒，也避免机械跑全流程。
---

# UI 设计工作流

## 目标

本 Skill 负责把产品事实变成可运行、可验证、视觉统一的 UI。

它既可以从零设计，也可以修改已有 UI；既可以只做设计，也可以继续落到实现。它不要求每次执行完整流程，而是先扫描完整问题空间，再只展开当前任务需要的能力。

UI 工作始终要能回答五件事：

1. **现实是什么**：用户、任务、内容、业务事实、权限、状态、平台约束。
2. **怎么呈现**：信息层级、页面结构、布局、视觉语言、组件系统。
3. **怎么行为**：交互、反馈、状态变化、时间行为、恢复路径。
4. **怎么落地**：状态归属、数据映射、组件边界、实现路径。
5. **怎么证明**：真实运行状态、边界内容、可访问性和 Human 视觉验收。

任何模块都是为这五件事服务，不另起一套平行流程。

---

# 触发范围

适用于：

- 从零设计 Screen / Flow / App UI。
- 优化、重构或统一已有 UI。
- 局部页面、组件、状态、交互或视觉修改。
- 建立或扩展 Design System。
- 把主观感觉编译成明确视觉语言。
- 把设计定义落成真实前端 UI。
- 审查 UI 是否完整、统一、可实现、可访问、可验证。

不替代：

- 产品战略和 Feature 是否存在。
- 后端业务规则、权限真相和服务端生命周期。
- 已冻结的顶层架构约束。
- Human 对最终审美的裁决。

---

# 核心工作原则

## 1. Coverage 不是 Procedure

每个任务先快速扫完整 UI Coverage，再标记：

- `Relevant`：本次需要展开。
- `Existing`：已有定义可直接复用。
- `N/A`：本次不适用。

不得因为用户没提就默认不存在；也不得把完整清单机械跑成固定流程。

完整清单见 `references/01-coverage.md`。

## 2. 先读真实情况，再发明结构

已有项目先看真实 repo、现有 UI、组件、tokens、状态、API、测试和运行结果。

从零任务则至少明确用户任务、核心对象、主要动作、平台和约束。

不得为了套模板重建已经成立的系统。

## 3. 精细视觉之前，结构和行为必须足够清楚

与当前任务相关的内容结构、层级、组件边界、状态、交互、反馈、布局和适配必须先达到“不会逼实现者临场猜”的程度。

不要求先写大文档，但禁止只凭一张理想静态截图直接进入高保真。

结构与内容见 `references/02-structure-and-content.md`；状态与交互见 `references/03-state-and-interaction.md`。

## 4. 主观感觉必须落成可观察规则

`极简 / 温暖 / 成熟 / 活跃 / 高级 / 安静` 不是完成的设计语言。

它们必须实际改变至少一项：

- Composition / Hierarchy
- Typography
- Spacing / Density
- Shape / Surface / Depth
- Color role
- Iconography / Imagery
- Component treatment
- Feedback / Motion

多个特征必须处理主次、兼容、张力和冲突；最终只形成一套统一视觉语言。

见 `references/04-visual-language.md`。

## 5. 页面不是属性表

列出颜色、圆角、字体、间距之后，仍必须形成具体页面排版：视觉重心、内容顺序、分组方式、容器策略、动作位置、滚动归属和响应式变化。

见 `references/05-page-composition.md`。

## 6. Variant、State、Owner 必须分开

- `Variant`：组件是哪一种语义版本。
- `State`：现在处于什么状态。
- `Owner`：谁拥有并改变这个状态。

状态可以是多个维度同时成立，不要把页面简化成单一 `normal/loading/error` enum。

## 7. UI 真相必须显式

Permission、lifecycle、approval、route、session 等会影响决策的事实，必须来自明确字段或状态源。

禁止从文案、颜色、位置、字符串前缀、CSS class 或视觉标签反推业务真相。

## 8. 组件按意义和变化边界形成

组件边界优先依据：

- 独立语义。
- 真实复用。
- 独立状态或交互。
- 独立视觉规则。
- 独立变化概率。

禁止“看到一个矩形就做一个 Component”，也禁止用 Card 包掉所有层级问题。

系统化规则见 `references/06-design-system.md`。

## 9. 设计与实现之间必须有共同定义

重要 UI 必须能追踪：

`UI element → content/data → state source/owner → user event → action/command → pending → success/failure → recovery`

如果实现者仍需猜关键状态、数据来源或反馈行为，设计没有完成。

见 `references/07-ui-contracts.md`。

## 10. 核心规则平台无关，平台差异下沉

通用规则不得假设 React、Web、SwiftUI 或其他框架。

平台专属约束只在对应平台触发。当前内置 SwiftUI 适配见 `references/09-platform-swiftui.md`。

## 11. 思考必须留下东西

重要分析最终至少落成一种结果：

- 明确设计决定。
- 可执行规则。
- 页面排版。
- 状态 / 交互定义。
- Component / Surface Contract。
- Design System 规则。
- Prototype / State Proof。
- 实现或测试。
- Rendered evidence。

没有改变后续设计、实现或验证行为的分析，不算完成的工作。

## 12. 可见 UI 必须看真实运行结果

不能只看源码、设计稿或静态截图就宣称 UI 正确。

可见改动必须按本次 Relevant 项验证真实 rendered state、content stress、viewport、interaction 和 accessibility。

见 `references/11-verification.md`。

## 13. Human 拥有最终审美权

Agent 可以检查一致性、完整性、规则遵守、布局、状态覆盖、可访问性和实现证据。

但“好不好看、够不够高级、是不是太幼稚、整体感觉对不对”由 Human 最终裁决。

Human 说感觉不对时，回到相应视觉或构图规则迭代，不与用户争论审美正确性。

---

# 任务路由

路由的作用是决定加载哪些能力，不是选择不同的 Skill。

## 从零做 UI

通常需要：Coverage → 结构/内容 → 状态/交互 → Human 方向 → 视觉语言 → 页面构图 → 系统化 → Contract → 实现（若要求）→ 验证。

## 已有 UI 重设计 / 优化

先读取现状。优先诊断：

`purpose → hierarchy → grouping → layout → density/spacing → typography → components → color/surface/icon → motion`

不要先从像素、阴影、圆角换皮开始。

## 局部 UI 修改

只展开受影响能力。例如危险按钮可能只需要现有视觉系统、动作层级、destructive semantics、反馈、states、accessibility 和 rendered verification。

不得借局部改动重做整个产品。

## 已有设计，只做实现

直接从现有 UI 定义、Contract、状态归属、组件实现和验证开始；不要重新发明视觉方向。

## 设计系统 / 基础重构

重点展开现状、系统边界、contracts、state ownership、components、implementation 和 regression verification。

---

# 能力模块

这些模块按需加载，不是固定步骤。

### A. Coverage
完整问题空间与适用性扫描。见 `references/01-coverage.md`。

### B. 结构、内容、层级与布局
内容边界、IA、导航、Hierarchy、Surface/Region/Section/Pattern/Component、layout ownership。见 `references/02-structure-and-content.md`。

### C. 状态、交互、反馈与时间行为
状态组合、owner、事件、命令、pending/success/failure、retry/undo/cancel、loading/progress、motion continuity。见 `references/03-state-and-interaction.md`。

### D. 视觉语言
Human Alignment、特征主次、兼容/对冲、Design Grammar、Typography/Color/Shape/Surface/Icon/Motion。见 `references/04-visual-language.md`。

### E. 页面构图
把内容、层级、行为和视觉方向合成具体页面方案。见 `references/05-page-composition.md`。

### F. 设计系统与组件
Tokens、primitives、components、patterns、variants、themes、reuse boundaries。见 `references/06-design-system.md`。

### G. UI Contracts
Surface / Component / Data / State / Implementation 定义统一收口。见 `references/07-ui-contracts.md`。

### H. 实现
平台无关的 repo 读取、依赖方向、状态投影、组件/page 实现、迁移和工程质量。见 `references/08-implementation.md`。

### I. 平台适配
平台规则只在相关平台加载。SwiftUI 见 `references/09-platform-swiftui.md`。

### J. 参考分析与交互 Proof
用户给参考时提取可迁移原则；复杂交互风险高时做最低成本 proof。见 `references/10-reference-and-proof.md`。

### K. 验证与 Review
Pressure tests、negative/source gates、rendered verification、mechanical design review、Human review package。见 `references/11-verification.md`。

### L. Accessibility 与适配
输入方式、focus、语义、contrast、text scaling、reduced motion、viewport、RTL/localization 等横切约束。见 `references/12-accessibility-and-adaptation.md`。

---

# 默认执行方式

不是固定阶段，而是默认依赖顺序。简单任务可以合并，复杂任务可以来回迭代。

1. **Route + Coverage**：识别任务形态，扫完整 Coverage，只展开 Relevant 项。
2. **Restore Reality**：读产品/项目/现有 UI，确认用户任务、核心对象、主要动作和不能擅改的约束。
3. **Define UI**：把本次相关的内容、层级、组件、状态、交互、反馈、布局和适配定义清楚。
4. **Resolve Visuals**：需要新视觉方向时，把 Human 感觉编译成统一视觉语言；已有稳定系统则复用。
5. **Compose Surface**：完整页面必须形成明确构图，不停留在属性列表。
6. **Systematize**：只把稳定、真实复用的规则上升为 token/component/pattern。
7. **Form Contracts**：让 UI、数据、状态、事件和结果之间没有暗缝。
8. **Implement**：如果任务包含代码，在现有 repo 约束下最小完整落地。
9. **Verify**：只验证 Relevant 场景，但可见 UI 必须有真实 rendered evidence。
10. **Human Review**：机械问题由 Agent 修，最终视觉感觉由 Human 裁决。

---

# 完成门槛

## Coverage Gate
进入精细设计前，本次 Relevant 项已识别；内容、层级、状态、交互没有明显“忘了考虑”的空白。

## Visual Gate
需要新视觉方向时：

- 主次特征已消解冲突。
- 形成唯一视觉方向。
- 每个重要形容词都改变了实际设计决定。
- 页面没有互相打架的视觉信号。

## Composition Gate
完整 Surface 不能只有 tokens / 属性清单，必须有具体视觉重心、分组、容器策略、动作位置和滚动/适配方案。

## Contract Gate
重要状态有来源和 owner；重要动作有 command、pending、结果、失败与恢复；实现不需要猜业务真相或关键 UI 行为。

## Implementation Gate
若包含代码：遵守现有依赖方向和 repo 约定；关键 state/contract 行为有相称的测试或证据；废弃路径不作为正常 fallback 存活。

## Rendered Gate
可见 UI 已在真实运行环境覆盖本次 Relevant states / content stress / viewport / interaction；未解决问题明确列出；Human 保留审美裁决权。

---

# 禁止模式

1. **User-as-Linter**：等用户逐条提醒状态、层级、组件、内容边界或验证遗漏。
2. **Checklist Theater**：与任务无关也机械展开全部能力。
3. **Screenshot-Only Design**：只设计 ideal / loaded 状态。
4. **Visual Before Reality**：内容、状态和核心动作不清时先做高保真。
5. **Adjective-Only Design**：形容词没有落成可观察规则。
6. **Style Averaging**：冲突风格平均混合成四不像。
7. **Secondary Trait Takeover**：次要性格侵占整体结构语言。
8. **Attributes Without Composition**：有 color/radius/type，却没有页面排版方案。
9. **Reference Cloning**：复制参考产品外壳而不理解结构与原则。
10. **Card Everything**：用 Card 代替层级、分组和 layout 判断。
11. **Component Everything**：把每个视觉块都组件化。
12. **Token Before Meaning**：从“温暖/高级”直接跳到色值和 radius。
13. **Variant-State Confusion**：把语义版本、运行状态和 owner 混成 props 大杂烩。
14. **Semantic Inference from Presentation**：从显示文本/颜色/位置推断业务真相。
15. **Prose-Only Handoff**：只有散文，没有 UI ↔ data/state/event/action 映射。
16. **Leaf Durable Mutation**：叶子组件直接改 durable shared truth。
17. **Business Logic in Base UI**：基础 UI 组件携带产品业务判断。
18. **Platform Leakage**：把某框架习惯写成通用 UI 规则。
19. **Old Path Lives On**：新逻辑上线后，旧推断/旧入口仍作为正常 fallback 存活。
20. **Source-Only Confidence**：只看代码就宣布可见 UI 已正确。
21. **Agent Declares Taste Correct**：Agent 用自己的审美评价覆盖 Human 判断。
22. **Prototype Theater**：简单交互也强制高成本 prototype。
23. **Verification Theater**：为了形式重复截图、全设备遍历或无风险全链路测试。

---

# 成本 / 价值原则

只执行能改变设计决策、发现真实缺陷、降低实现歧义或给 Human 提供必要判断材料的工作。

默认不做：

- 没有设计分歧时生成多套 Variant。
- 简单页面强制建立 Gallery / Prototype。
- 每个小改动遍历所有设备和状态组合。
- 为了“再看看”重复截图和 Agent 自我审美循环。
- 没有风险证据时做性能 profiling。
- 设计当前任务无关的未来页面。


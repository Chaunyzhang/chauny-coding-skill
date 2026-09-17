---
name: ui-workflow
display_name: UI 设计工作流
description: 自包含的 UI 设计与实现工作流。把产品事实、Human 意图或参考图编译成明确 UI 规格，再按规格实现、验证与防漂移；支持从零设计、已有 UI 优化、识图复刻、局部修改、组件/设计系统和实现审查。完整 Coverage 只用于防漏，默认走最小合法路径。
---

# UI 设计工作流

## 目标

把输入编译成一套**可确认、可实现、可验证、可持续扩展**的 UI，而不是让 Agent 边写边猜。

默认真相链：

`Reality / Human Intent / Visual Evidence → UI Definition → Visual System → UI-DESIGN-SPEC → Implementation Structure → Code → Rendered Verification`

完整 UI 设计任务的最终设计权威是 `UI-DESIGN-SPEC.md`；非平凡实现还必须有 `IMPLEMENTATION-STRUCTURE.md`。

---

# 1. 先路由：默认走最小合法路径

Coverage 是问题全集，不是固定流程。先判断任务范围，再只加载会改变结果的能力。

| 任务 | 默认路径 |
|---|---|
| 改单个颜色/间距/文案 | Existing Spec → Patch Spec → Implement → Render verify |
| 改一个组件 | Existing System → Component definition/states → Patch Spec → State proof → Verify |
| 新增一个页面 | Coverage scan → UI Definition → Visual inheritance/new direction → Page Spec → Implement → Verify |
| 从零做 UI | Coverage → UI Definition → Human alignment → Visual System → Full Spec → Structure → Implement → Verify |
| 图片/截图复刻风格 | Image reverse-engineering → Visual System → Full/Page Spec → Implement → Verify |
| 已有 UI 重设计 | Restore reality → diagnose hierarchy/layout/system → Human alignment → Patch/Page Spec → Verify |
| 已有设计只实现 | Spec/contract → Structure → Implement → Verify；禁止重新设计 |
| 纯技术重构 | Structure/ownership → Implement → regression verify；可见行为不变时无需重新找 Human 审批 |

只有出现新风险时才升级路径：新页面/新状态、新视觉语言、跨页共享、状态 owner 不清、业务真相不清、复杂交互、结构复制、Spec drift。

完整扫描见 `references/01-coverage.md`。

---

# 2. 全局证据纪律：Observed / Resolved / Unknown

任何会影响设计、实现或验证的结论都必须属于：

- **Observed**：图片、代码、产品文档、运行结果或 Human 明确说过。
- **Resolved**：由 Observed 事实 + 已批准规则推导出的决定。
- **Unknown**：证据不足，不能伪装成事实。

Unknown 若会改变业务语义、设计方向或可见行为：先问 Human/上游；若不阻塞当前范围，显式记录而不是偷偷补全。

禁止从颜色、label、CSS class、字符串前缀、组件位置反推权限、生命周期、route、approval 等业务真相。

---

# 3. Human 可感知变化：Clarify → Confirm → Specify → Implement → Verify

Human 可以只说“太跳”“太挤”“不够稳”“想温暖一点”。Agent 的工作是把感觉翻译成**可观察决定**：

1. 想改变什么。
2. 什么保持不变。
3. 屏幕上会发生什么可观察变化。
4. 关键规则/数值候选。
5. 仍然 Unknown 的地方。

Human 确认后，**先更新 Full/Page/Patch Spec，再改生产代码**。禁止 `Code first → 看效果 → 事后补 Spec`。

不需要重复确认：Human 指令已足够精确、现有批准 Spec 已覆盖、Human 明确授权 Agent 决定，或纯实现重构不改变可见行为。

详细协作与并行 Agent 规则见 `references/07-human-alignment.md`。

---

# 4. 定义 UI：视觉之前先消除实现猜测

进入精细视觉前，与本次任务相关的以下内容应清楚到“不逼实现者临场猜”：

- 用户任务、核心对象、主/次动作。
- 内容字段、数量/长度/缺失/溢出范围。
- 信息/动作层级、导航与页面结构。
- Surface / Region / Section / Pattern / Component 边界。
- 业务状态、数据状态、操作状态、权限/环境/交互状态及 owner。
- 事件 → action/command → pending → success/failure → recovery。
- Layout、scroll ownership、viewport/adaptation、accessibility。

详细规则见 `references/02-ui-definition.md`。

---

# 5. 视觉：先把秩序排对，再形成统一风格

“极简、温暖、成熟、活跃、高级”不是完成的视觉语言。完整视觉设计先解决**秩序**，再解决**风格**：

1. **Visual Order**：明确第一/第二/第三视觉焦点、主对齐轴、分组、密度、容器策略和哪些信息必须退后。
2. **Visual Laws**：3–5 条统治整个界面的规则。
3. **Composition grammar**：页面怎样组织、什么最突出、什么退后。
4. **Concrete visual recipe**：Typography / spacing / density / color / shape / surface / depth / icon / imagery / motion 的明确规则和值。
5. **Component grammar**：不同组件如何继承同一视觉世界。
6. **Forbidden / Guardrails**：什么不能出现。

多个特征不能平均混合。先分主次与 Avoid；次要性格可以进入局部表达，但不能推翻主结构语言。

### Visual Order Gate

完整页面进入高保真前，必须能回答：
- 一眼先看什么、再看什么、最后看什么？
- 页面只有哪些主对齐轴？数字/状态/文本分别如何对齐？
- 哪些内容是一组，组内与组间距离是否明显不同？
- 哪些信息必须主动弱化、隐藏或按需出现？
- 去掉无语义 Card/border/shadow 后，结构是否仍成立？

若没有明确答案，不得用颜色、阴影、渐变去掩盖结构问题。

## Visual Math：把可数学化的审美变成硬检查

- Typography 只从批准的 type scale 取；不同文字 role 不能靠随机 1–3px 差异假装层级。
- 同级 role 固定 `font-size + line-height + weight`，不允许页面各自发明。
- Spacing 只从批准的 scale 取；相同语义关系必须使用相同间距。
- **组内 gap 必须明显小于组间 gap**；若 16 与 20 分别代表“同组/跨组”，优先判层级对比不足。
- 层级差异要有可见对比；不要让所有区域在尺寸、颜色、surface、elevation 上同权。
- 页面使用有限对齐轴；无理由的 3–8px 左边缘漂移视为缺陷。
- Radius、icon size、control height、border、shadow 形成有限 family；大量近义值视为 drift。
- 长正文控制合理行宽；极长内容必须有明确换行、截断或重排规则。

## Craft Floor：先排除稳定显脏/显乱的做法

Hard fail：
- 无语义价值的框套框/Card 套 Card。
- 随机字号、随机 spacing、随机 radius、accent 漂移、icon family 混用。
- 所有东西都强调、所有区域都卡片化、所有 surface 都有阴影。
- hover/focus/loading/error 导致几何跳动。
- 长内容/大字体一来就溢出或破坏布局。
- 焦点、对比、触控目标等基础可访问性失败。

Warning（除非有明确理由）：装饰性渐变、到处 glass/blur、universal pill、重阴影、多个装饰处理同时叠加、重复完全同构 card grid、每节 eyebrow/编号/divider 装饰。

详细视觉生成、Visual Math、Anti-Ugly 规则统一见 `references/03-visual-design.md`。

---

# 6. 图片参考：先逆向系统，不抄截图像素

截图只能证明可见事实。识图结论必须标 Observed / Resolved / Unknown。

逆向目标：
`结构/层级 → composition → type/color/spacing/shape/surface/icon → component grammar → token candidates → Visual Laws → Spec`

不得从静态图编造 motion、hidden states、responsive breakpoint、权限或后端行为；多图优先归纳重复规律，单图不得过拟合为完整 Design System。

见 `references/06-image-reverse-engineering.md`。

---

# 7. 设计系统：只上升真实稳定规则

组件按**意义与变化边界**形成，不按矩形形成。满足任一条件再考虑抽取：真实复用、独立状态/交互、稳定视觉/行为 contract、共享资产/primitive、复制会产生第二真相源。

同义设计规则必须共享 semantic token；不得先发明 primitive 值再给它找意义。

见 `references/04-design-system.md`。

---

# 8. 设计必须收束成权威 Spec

完整设计不能停在分析、截图或“适度圆角/舒适间距”。进入实现前，所有 Relevant 决定必须编译进同一权威体系：

- **Full Spec**：新产品/新视觉系统。
- **Page Spec**：在已批准全局系统上增加/重做一个页面。
- **Patch Spec**：局部改动，只记录 delta 与保持不变项。

Spec 至少覆盖：Visual Laws、页面结构、type/color/spacing/shape/surface/icon/motion、component grammar、states、adaptation、guardrails、UI↔data/state/event/action contract、验证项和可复制实现提示词。

Spec 内可附一个**机器可读 manifest**，用于下一页继承和 drift audit；它是同一 Spec 的 appendix，不是第二真相源。

模板与编译规则见 `references/05-ui-design-spec.md`。

---

# 9. 非平凡实现前后必须画结构

包含多页面、共享组件、共享状态/数据或长期演进的实现，必须创建/更新 `IMPLEMENTATION-STRUCTURE.md`：

- repo / feature tree
- shared vs page-local
- state / data / mutation owner
- navigation owner
- component/rendering plan
- token/icon/asset 单一来源

代码前画计划；代码后按真实 repo 重画并做 duplication audit。

硬问题：**“现在再加一个同类页面，需要复制什么？”** 若答案包含“复制上一页主体再改”，Structure Gate 不通过。

见 `references/08-implementation-structure.md`。

---

# 10. 实现：消费 Spec，不重新设计

实现负责把已批准的 UI truth 投影成代码：正确 ownership、依赖方向、数据/状态映射、共享边界、迁移与测试。实现中若发现必须新增可见设计决定：停代码，回到 Human alignment → Spec。

平台无关规则见 `references/09-implementation.md`；SwiftUI 适配见 `references/11-platform-swiftui.md`。

---

# 11. 验证：真实渲染 + 结构 + Drift

可见 UI 不得只看源码宣称正确。按 Relevant 风险验证：

- normal / loading / empty / error / permission / offline 等适用状态
- 长文本、大数据、小 viewport、动态字体
- hover/pressed/focus/disabled 等适用交互状态
- accessibility 与 reduced motion
- Spec conformance、Visual Order / Craft Floor
- 能否在弱化颜色后仍看出焦点、分组和层级
- Structure conformance、重复 truth source
- Drift：新 color/type/spacing/radius/shadow/icon/motion/component language

复杂交互按风险做最小 State Proof / prototype；不做 prototype theater。

见 `references/10-verification.md`。

---

# 12. 完成门槛

| Gate | 通过条件 |
|---|---|
| Routing | 已选择最小合法路径；升级有真实风险理由 |
| Evidence | 关键事实标明 Observed/Resolved/Unknown；Unknown 未被伪装 |
| Alignment | 新的 Human 可感知决定已确认，或有明确跳过理由 |
| UI Definition | Relevant 内容/层级/状态/交互/布局不需要实现者临场猜 |
| Visual | Visual Order 明确；有统一 Visual Laws + Concrete Recipe；Visual Math、视觉预算与 Craft Floor 通过 |
| Spec | Relevant 决定已写入 Full/Page/Patch Spec，具体到足够直接实现 |
| Structure | 非平凡实现前后均有结构图；没有 copy-paste expansion 或第二 truth source |
| Implementation | 代码遵守 Spec、ownership、repo 约定；旧路径不作为正常 fallback 存活 |
| Drift | 新设计值/语言均已解释并进入 Spec，或被移除/归并 |
| Rendered | Relevant 状态与内容压力在真实运行结果中验证 |
| Human Review | 机械问题已清；最终审美交给 Human 裁决 |

---

# 13. 禁止模式

- **User-as-Linter**：等用户逐项提醒状态、层级、组件、内容边界或验证遗漏。
- **Checklist Theater**：小任务机械跑完整流程。
- **Screenshot Tracing**：抄坐标而不提取设计系统。
- **Static-Motion Hallucination**：静态图编造 motion。
- **Visual Before Reality**：内容/状态/核心动作不清先做高保真。
- **Adjective-Only Design**：形容词没变成规则和值。
- **Style Averaging**：冲突风格平均混成四不像。
- **Attributes Without Composition**：只有 type/color/radius，没有页面构图。
- **Card Everything / Component Everything**：用容器/组件化代替结构判断。
- **Token Before Meaning**：从“高级/温暖”直接跳 hex/radius。
- **Variant-State-Owner Confusion**：语义版本、运行状态和 ownership 混成一团。
- **Semantic Inference from Presentation**：从视觉反推业务真相。
- **Prose-Only Handoff**：没有 UI↔data/state/event/action 映射。
- **Code-First Design**：先写可见行为再补 Spec。
- **Copy-Paste Expansion**：新页面靠复制旧页面扩展。
- **Post-Hoc Structure Cleanup**：先堆重复代码，提醒后才抽真相源。
- **Platform Leakage**：把某框架习惯写成通用 UI 原则。
- **Source-Only Confidence**：没看真实渲染就宣称完成。
- **Agent Declares Taste Correct**：Agent 覆盖 Human 审美裁决。

---

# 14. 成本 / 价值原则

只做能改变设计决定、发现真实缺陷、降低实现歧义或给 Human 提供必要判断材料的工作。

默认不做：无分歧时强制多套方案、简单交互强制 prototype、每个小改遍历所有设备/状态、重复截图自我审美循环、与当前任务无关的未来页面设计。

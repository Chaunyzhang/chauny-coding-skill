# UI Design Spec：设计阶段的唯一权威产物

**何时加载**：任何需要新建页面、改变视觉方向、形成完整 UI 方案、交给实现 Agent/工程师，或需要把已有零散设计规则收束成可执行规范的任务。

**目标**：把 Human 已确认的设计判断编译成一份具体、无歧义、可直接实现的 `UI-DESIGN-SPEC.md`。实现者执行规范，不重新猜视觉意图。任何 Human 可感知的新设计决定都必须先经过 Alignment，再进入 Spec。

## Spec 粒度：一个权威体系，三种修改尺度

不要把每个任务都强制成完整文档重编译。选择能完整约束当前任务的最小 Spec 粒度：

### Full Spec
用于：从零产品、新视觉语言、全局 Design System、多个页面共同变化。

产物：完整 `UI-DESIGN-SPEC.md`。

### Page Spec
用于：已有稳定 Global Spec 下新增/重做一个页面。

产物：更新 `UI-DESIGN-SPEC.md` 中对应 Page Section，或在仓库约定允许时生成引用 Global Spec 的 `PAGE-SPEC-<name>.md`。Page Spec 不复制全局规则，也不能静默覆盖全局规则。

### Patch Spec
用于：局部组件、单一视觉属性、局部状态/交互变化。

最少包含：

```text
Target:
Observed context:
Human intent / approval:
Confirmed interpretation:
Preserved rules:
Changed rules:
Reason / source:
Implementation impact:
Verification:
```

若 Patch 产生了新的长期设计规则，必须把该规则合并回权威 `UI-DESIGN-SPEC.md`；否则 Patch 只是当前改动的 delta，不成为第二套设计系统。

**原则：一个权威系统，多个修改粒度；禁止多个互相竞争的 Spec。**

## 变更控制：Human Confirm 先于 Spec，Spec 先于 Code

涉及 Human 可感知变化时，权威顺序固定为：

`Human intent → Agent precise translation → Human confirm/delegate → Spec update → Code → Rendered verification`

- Candidate decision 在 Human 确认前不得写成权威 Spec，也不得进入生产代码。
- Human 原始指令本身已经足够精确、已批准现有 Spec，或明确授权 Agent 在限定范围内决定时，不重复询问。
- Human 只描述感觉时，Agent 必须先把它翻译成“屏幕上会发生什么 / 保持什么 / 关键规则 / Unknown”，再确认。
- 如果实现过程中发现必须改变可见结果、interaction、motion、state presentation、page/component structure 或 design token，先停代码，回到 Alignment。
- 纯实现重构如果 rendered result、observable behavior、contract 与 Spec 完全不变，可以没有 Spec diff。

详细规则见 `17-human-alignment-change-control.md`。

## 核心规则

1. **设计没有形成明确规格，就不算设计完成。**
2. 最终文档不得只剩 `极简 / 温暖 / 高级 / 中等圆角 / 舒适留白` 等模糊词。
3. 所有 Relevant 视觉决定必须解析成：
   - 明确规则；
   - 明确 token / 数值 / 系统语义；
   - 明确页面结构；
   - 明确组件行为；
   - 明确禁止项。
4. 如果项目已有稳定 Design System，规格必须引用其**准确 token 名称及已解析语义**，不得另起一套近义值。
5. 如果项目没有 Design System，本次规格必须给出当前范围所需的完整基础值。
6. 平台原生值可以作为最终答案，但必须明确使用哪个系统语义，例如 `systemBackground`、`body`、`secondaryLabel`；不能写“用系统默认差不多即可”。
7. 下游实现不得重新解释 Human Feeling。视觉方向只在设计阶段解析一次。
8. Human 可感知的新决定必须有确认来源：明确指令、对 Alignment Block 的确认，或 Human 明确授权。
9. 设计变更必须先更新 Spec 再进入生产代码；禁止 code-first / spec-backfill。

---

# 必须输出的文档结构

最终创建或更新项目中的：

`UI-DESIGN-SPEC.md`

只写当前产品或当前任务真正需要的内容，但以下结构必须逐项判断，不能因没想到而漏掉。

## 0. Evidence Provenance

所有重要事实/决定都可使用同一套证据状态，不只识图：
- `Observed`：用户、产品文档、代码、运行结果、图片等直接证明。
- `Resolved`：由 Observed + 明确规则得到的设计/实现决定。
- `Unknown`：证据不足，不能伪装成事实。

识图时记录图片证据；已有项目时记录 repo/runtime 证据；产品规则记录其上游来源。Unknown 若需要由 UI 设计补齐，标记 `Resolved (new target decision)`；若超出 UI authority，则保持 Unknown 或取得上游事实。

### 0.1 Human Decision Provenance

对本次新增/改变的 Human 可感知规则，记录最小必要来源：

```text
Human intent:
Confirmation: explicit instruction / confirmed alignment / delegated scope
Confirmed interpretation:
Preserved:
Changed:
Remaining Unknown / blockers:
```

这不是要求建立冗长审批日志，而是保证后续能回答：**这条设计规则是谁确认的，为什么成为真相？**

## 1. Design Intent

记录已经消解后的方向，不重新讨论。

```text
Primary character:
Secondary character:
Micro-expression:
Avoid:

Visual Laws:
1. ...
2. ...
3. ...
```

### Visual Laws 要求

Visual Law 是能同时约束多个视觉元素的高层规律，不是 token。

好：
- 层级优先由 Typography + spacing 建立，普通内容不靠 Card 建层级。
- 活力只进入反馈、icon 和少量 accent，不进入大面积 surface。
- 普通内容保持 flat；只有浮层允许 elevation。

差：
- 用 12px 圆角。
- 用暖色。

后者属于下一层具体规则。

## 2. Global Composition Grammar

明确整个产品/当前 UI 范围共享的排版语法：

- 主构图类型。
- 主要 alignment axis。
- container strategy。
- grouping priority：spacing / typography / divider / surface / card 的使用顺序。
- density。
- focal-point 规则。
- max content width / grid / columns（适用时）。
- page gutters / safe area。
- scroll / sticky / overlay 基本策略。

禁止只写“简洁、有呼吸感”。

## 3. Typography System

至少明确：

| Role | Family/System Role | Size | Line height | Weight | Tracking | Usage |
|---|---|---:|---:|---:|---:|---|
| Display | | | | | | |
| Page Title | | | | | | |
| Section Title | | | | | | |
| Body | | | | | | |
| Meta | | | | | | |
| Button/Control | | | | | | |

规则：
- 没有必要不要制造额外字号。
- 明确长标题、Dynamic Type / scaling、换行和 truncation。
- 如果使用平台 text style，写准确 style，并说明是否有额外 weight/leading 规则。

## 4. Color System

明确每个颜色的**角色**和**最终值/系统语义**：

```text
background.primary
surface.primary
surface.secondary
text.primary
text.secondary
text.tertiary
border.subtle
action.primary
action.primaryPressed
status.success
status.warning
status.error
focus.ring
```

并明确：
- Accent 使用频率和允许区域。
- Light / Dark 映射（适用时）。
- 禁止出现的色彩行为，例如多 accent、装饰渐变、大面积高饱和背景。

## 5. Spacing & Density

必须给出具体 spacing scale，例如：

```text
4 / 8 / 12 / 16 / 24 / 32 / 48
```

并定义：
- control internal padding。
- row padding。
- same-group gap。
- section gap。
- page gutter。
- compact / regular density 的变化（若存在）。

不要让页面自己发明 `13 / 19 / 27` 等近义间距。

## 6. Shape / Border / Surface / Depth

必须给出具体规则：

### Radius

```text
small control:
input/button:
large surface:
sheet/modal:
pill:
```

### Border

```text
width:
color role:
when used:
```

### Surface

列出允许的 surface 层级及用途。

### Shadow / Elevation

每一级必须写具体实现值或平台 elevation/material 语义：

```text
content: none
floating control: ...
popover/sheet: ...
modal: ...
```

不得只写“轻阴影”。

## 7. Iconography & Imagery

明确：

- icon family / source。
- outline / filled。
- standard sizes。
- stroke / optical weight（适用时）。
- corner/end-cap personality。
- selected / active 状态是否允许 filled。
- 是否允许多色 icon。
- imagery / illustration / photo 的角色、裁切、aspect ratio 和 fallback。

禁止混用没有明确关系的 icon family。

## 8. Motion & Feedback

明确：

- micro interaction duration。
- state transition duration。
- structural transition duration。
- easing / spring 参数或平台语义。
- allowed properties：opacity / scale / translation / blur 等。
- reduced-motion fallback。
- 哪些交互允许更有个性。
- 明确禁止：例如 bounce、overshoot、连续装饰动画。

重要动作要补具体行为，例如 Task completion、drag/drop、submit、undo。

## 9. Component Grammar

所有关键组件必须继承全局语言，至少给出当前范围需要的具体规格。

模板：

```text
Component: <name>
Purpose:
Geometry:
- height/min-height:
- padding:
- gap:
- radius:
- border:
- surface:
- shadow/elevation:
Typography:
Icon:
States:
- default:
- hover/focus/pressed:
- disabled:
- loading/pending:
Variants:
Motion:
Content bounds:
Accessibility:
```

优先覆盖真正复用或决定整体观感的组件，例如 Button、Input、List Row、Card、Navigation、Sheet/Modal、Toolbar。

## 10. Page Specifications

**每个 Relevant 页面/Surface 单独写。**

页面规格不能只引用“遵循全局设计系统”，还必须说明这个页面怎样使用系统。

模板：

```text
# Page: <name>

Purpose:
Primary object:
Primary action:

Visual priority:
1. ...
2. ...
3. ...

Structure:
<Page>
├── ...
├── ...
└── ...

Layout:
- viewport/content width:
- page gutter:
- top/bottom spacing:
- grid/columns:
- alignment:

Sections:
1. <section>
   - role:
   - layout:
   - spacing before/after:
   - internal gaps:
   - typography roles:
   - surface/container treatment:
   - actions:

Scroll / sticky / overlay:

Responsive / adaptation:

States:
- loading:
- empty:
- ready:
- error:
- permission/offline/etc. when relevant:

Content stress:
- long title:
- missing optional content:
- many items:
- localization/text expansion:

Accessibility:

Page-specific forbidden:
```

### 页面数值必须具体

如果页面需要：
- header 到 content 32pt；
- Task Row min-height 52pt；
- Section gap 24pt；
- content max-width 720px；

就写出来。不要把这些决定留到实现阶段。

## 11. State & Interaction Rules

对于所有会改变 UI 的关键动作，收束：

```text
UI element
→ displayed data
→ state source / owner
→ user event
→ command / action
→ immediate response
→ pending
→ success
→ failure
→ recovery / undo / retry
```

视觉规格和系统事实必须一致。

## 12. Adaptation & Accessibility

只覆盖 Relevant 项，但要给具体行为：

- viewport/window breakpoints 或 size-class rule。
- mobile/desktop 重排方式。
- Dynamic Type / zoom / text scaling。
- keyboard / focus。
- touch target。
- RTL / localization。
- dark/high-contrast。
- reduced motion。

不得只写“支持响应式 / 支持无障碍”。

## 13. Forbidden / Guardrails

先加载 `18-visual-craft-floor.md`。其中 `Hard Fail` 不应以“风格选择”留在 Spec 中；必须先解决。`Warning` 若保留，需记录明确 Art Direction / 产品理由。

然后列出这套设计最容易漂移的 5–15 条项目特定禁令，例如：

```text
DO NOT
- 每个 Section 都包 Card。
- 新增未定义 radius。
- 普通内容使用 shadow。
- 混用 filled 与 outline icon family。
- 使用第二套 accent。
- 在普通完成反馈中使用 confetti/bounce。
- 页面自行新增 typography role。
```

Guardrails 必须针对当前 Design Intent；共同视觉下限由 `18-visual-craft-floor.md` 统一承担，不要在每个项目重复抄一遍。

同时记录：
```text
Visual Craft Floor: PASS
Warnings intentionally retained:
- <warning> — <why it belongs to this Art Direction>
```

## 14. Implementation Structure（任务包含非平凡代码实现时）

Human 已确认且设计规格更新完成后，不把代码组织留给实现 Agent 临场决定。加载 `15-implementation-structure.md`，创建或更新独立的 `IMPLEMENTATION-STRUCTURE.md`，至少画出：

- repo / feature tree；
- shared vs page-local；
- state/data/mutation ownership；
- navigation ownership；
- repeated renderer/component；
- token/icon/asset single source。

`UI-DESIGN-SPEC.md` 规定 UI 应该是什么；`IMPLEMENTATION-STRUCTURE.md` 规定这些事实在代码里由谁拥有、放在哪里、如何复用。

## 15. Verification Checklist

从本次 Coverage 中生成真正要验证的场景：

```text
[ ] normal
[ ] loading
[ ] empty
[ ] error
[ ] long content
[ ] small viewport
[ ] focus / keyboard
[ ] dark mode
...
```

只列 Relevant 项。

---

# Copyable Implementation Prompts

`UI-DESIGN-SPEC.md` 最后必须生成可以直接给实现 Agent 使用的提示词。

## A. Global UI Implementation Prompt

目标：锁定整个 UI 世界，不让下游重新解释视觉方向。

模板：

```text
Implement the UI according to UI-DESIGN-SPEC.md.
Treat the specification as authoritative.
Do not reinterpret the design intent, introduce a new visual style,
or invent near-equivalent spacing, color, radius, typography, shadow,
icon, motion, or component rules.

Reuse the exact global design language, tokens, component grammar,
states, accessibility rules, and forbidden rules defined in the spec.

If the existing codebase conflicts with the spec, preserve product and
architecture truth and surface the conflict explicitly. If resolving the
conflict would change any human-perceptible design decision, stop and
return to Human Alignment; update the spec before changing production code.
Do not let implemented behavior silently become the new design truth.

Validate the rendered result against the relevant verification scenarios
and the confirmed human decision before declaring completion.
```

## B. Per-page Implementation Prompt

每个 Relevant Page 生成一段可以单独复制的 page prompt：

```text
Implement <Page Name> using the global rules in UI-DESIGN-SPEC.md.

Page authority:
- purpose: ...
- visual priority: ...
- exact structure: ...
- layout dimensions: ...
- section spacing: ...
- component usage: ...
- states: ...
- responsive/adaptation: ...
- accessibility: ...
- page-specific forbidden rules: ...

Do not redesign the page or substitute different visual values.
```

页面 Prompt 可以引用同一文件中的 Global Spec；若要脱离仓库单独复制，则应展开所需 Global rules，保证自包含。

---

# Spec Gate

进入实现前必须通过：

- [ ] 本次 Human 可感知的新决定已经确认，或原始指令/既有批准 Spec 已足够明确。
- [ ] Human 模糊反馈已经被翻译成可观察的精确规则，而不是直接由 Agent 在代码里解释。
- [ ] Spec 已先于任何对应生产代码变化更新。
- [ ] 没有未解析的核心形容词。
- [ ] 视觉规律明确。
- [ ] Typography 有具体 role/value。
- [ ] Color 有具体 role/value。
- [ ] Spacing scale 和关键 gap 明确。
- [ ] Radius / border / shadow/elevation 明确。
- [ ] Icon / imagery 规则明确。
- [ ] Motion 有具体 timing/behavior。
- [ ] 关键组件有具体 geometry 和 states。
- [ ] 每个 Relevant Page 有独立 Page Spec。
- [ ] States / interaction / feedback 不依赖实现者猜测。
- [ ] Responsive / accessibility 在 Relevant 范围内具体化。
- [ ] Forbidden rules 明确。
- [ ] Copyable implementation prompt 已生成。

如果仍出现“适度 / 合理 / 舒适 / 轻微 / 现代 / 高级 / 视情况”等词，且它们会影响实现，必须继续解析成具体规则后再通过。

## 停止条件

当 Human 已确认本次可感知设计决定，且下游实现者可以只读取最新 `UI-DESIGN-SPEC.md` 就完成当前 UI、无需重新解释 Human 意图或再做视觉设计决策时停止。

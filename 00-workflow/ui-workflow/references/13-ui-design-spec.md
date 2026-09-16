# UI Design Spec：设计阶段的唯一权威产物

**何时加载**：任何需要新建页面、改变视觉方向、形成完整 UI 方案、交给实现 Agent/工程师，或需要把已有零散设计规则收束成可执行规范的任务。

**目标**：把前面所有设计判断编译成一份具体、无歧义、可直接实现的 `UI-DESIGN-SPEC.md`。实现者执行规范，不重新猜视觉意图。

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

---

# 必须输出的文档结构

最终创建或更新项目中的：

`UI-DESIGN-SPEC.md`

只写当前产品或当前任务真正需要的内容，但以下结构必须逐项判断，不能因没想到而漏掉。

## 0. Evidence Provenance（识图任务时）

如果本 Spec 来自截图/设计稿逆向，先记录：
- `Observed`：图片直接证明的规则/值。
- `Resolved`：由重复视觉证据归纳的规则/token。
- `Unknown`：图片无法证明、不得伪装成源设计事实的行为/状态/适配。

最终实现仍需具体，但凡 Unknown 需要在目标产品中补设计时，应明确这是“目标产品的新设计决定”，不是“从图片提取所得”。

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

列出这套设计最容易漂移的 5–15 条禁令，例如：

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

Guardrails 必须针对当前 Design Intent，不写泛泛而谈的设计常识。

## 14. Verification Checklist

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
architecture truth, surface the conflict explicitly, and resolve the UI
through the nearest valid implementation rather than silently changing
the design language.

Validate the rendered result against the relevant verification scenarios
before declaring completion.
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

当下游实现者可以只读取 `UI-DESIGN-SPEC.md` 就完成当前 UI，而无需重新做视觉设计决策时停止。

# 识图模式：从图片逆向设计语言

**何时加载**：用户提供 UI 截图、设计稿、App/Web 页面图片、Moodboard，且希望提取设计语言、复刻视觉风格、生成同风格新页面，或把图片反编译成 `UI-DESIGN-SPEC.md`。

**目标**：不是“看图模仿”，而是把图片中的可见结果逆向成可复用的设计规则，再接回本 Skill 已有的结构、视觉语言、页面构图、设计系统和 Spec 编译模块。

---

## 核心原则

### 1. 图片是视觉证据，不是产品真相

一张静态图通常可以证明：
- 可见内容结构；
- 当前视觉层级；
- 当前构图与对齐；
- 当前组件外观；
- 当前色彩、字体、shape、surface、border、shadow；
- 当前可见状态。

一张静态图通常**不能证明**：
- 隐藏状态全集；
- permission / lifecycle / backend truth；
- 状态 owner；
- 点击后的真实 command；
- loading / error / offline / rollback；
- responsive 规则；
- motion timing / easing；
- accessibility semantics。

这些必须标成 `Unknown`，或由额外截图、视频、代码、产品文档补证据。不得为了“完整”而编造。

### 2. 每个结论必须标来源

识图阶段使用三种标签：

- `Observed`：图片直接可见或可测量。
- `Resolved`：由多个 Observed 证据归纳出的设计规律或 token。
- `Unknown`：当前图片无法支持。

必要时可加 `Hypothesis`，但 Hypothesis 不能直接进入最终权威 Spec，除非 Human 接受或得到额外证据。

### 3. 复刻的是系统，不是截图坐标

不要只抄 `x/y/width/height`。优先提取：

`对齐轴 → 间距节奏 → 尺度比例 → 容器规则 → 字体层级 → 色彩角色 → 组件语法 → 页面构图`

同一截图里的 `7 / 8 / 9px` gap 应尝试归纳成同一个 spacing token，而不是生成三个 token。

### 4. 风格迁移时，分离 Style DNA 与源页面业务

如果用户要把 A 产品的风格用于 B 产品：

- 保留 A 的视觉规律；
- 不复制 A 的品牌元素、业务 IA、专属 icon、独特内容结构；
- 用目标产品自己的内容、状态和交互重新应用该设计语言。

---

# 识图时按现有能力模块逆向什么

## A. Coverage / Source Scan

先判断图片证据范围：

- 单页 / 多页 / 多状态 / 多 breakpoint。
- 图片尺寸、纵横比、设备/平台线索。
- 是否包含系统 chrome / safe area。
- 图片是否完整，是否有裁切、缩放、压缩。
- 哪些区域可见，哪些明显缺失。

输出：`Image Evidence Scope`。

---

## B. 结构、内容、层级与布局

从图片逆向：

### 内容结构
- 可见字段、对象、集合。
- required / optional 只能在有多样例证据时判断；单图通常只标可见性。
- 文本长度、行数、图片比例、列表数量等当前样本。

### 页面树
尽可能重建：

`Surface → Region → Section → Pattern → Component → Primitive`

### Hierarchy
识别：
- 第一视觉焦点；
- 第二/第三层级；
- primary / secondary action 的视觉权重；
- 哪些信息被刻意压低。

### Layout / Composition
提取：
- 主轴与 alignment axis；
- 单列 / 双列 / grid / split / overlay；
- page gutter；
- section gap；
- item gap；
- container width / max-width 线索；
- sticky/fixed 只有在证据充分时判断；
- flat / divider / surface / card 的分组策略；
- 页面视觉重心与留白分布。

### 尺度提取
如果图片像素尺寸已知：
1. 记录截图中的 Observed px。
2. 同时记录相对比例，例如 `gutter ≈ viewport width 的 5%`。
3. 聚类近似数值，归纳 spacing / size scale。
4. 在最终 Spec 中写“Resolved token”，不要把截图噪声当设计值。

---

## C. 状态、交互、反馈与时间行为

静态图片只提取**可见状态**：
- selected / unselected；
- enabled / disabled；
- expanded / collapsed；
- focused / pressed（只有画面明确显示时）；
- success / error / empty / loading（只有当前画面可见时）。

从 affordance 可以提出 Hypothesis，例如“该 row 看起来可点击”，但不能把点击结果写成事实。

单张静态图下：
- motion：`Unknown`；
- pending/success/failure flow：`Unknown`；
- command/state owner：`Unknown`。

多张连续状态图、GIF、视频或运行页面可以继续逆向 transition、motion、feedback continuity。

---

## D. 视觉语言

这是识图模式的重点。必须提取：

### 1. Visual Laws
先从结果反推 3–5 条跨元素成立的规律，例如：
- `Typography + spacing before containers`。
- `Only floating layers receive elevation`。
- `One saturated accent; all large surfaces remain neutral`。
- `Geometry is compact and restrained; pills only signal semantic status`。

如果一条“规律”只解释一个按钮，它不是 Visual Law。

### 2. Typography
识别并归纳：
- font category / likely family（能确定时写 family，不能确定则写类别和关键特征）；
- title/body/meta/control roles；
- size ratio；
- weight；
- line height；
- tracking；
- casing；
- wrap/truncate 表现。

不要因为无法确定准确字体名就停住。可以先得到：
`neo-grotesk sans / high x-height / 600 heading / compact tracking`，再在目标平台解析为可用字体。

### 3. Color
提取：
- background / surface / text / border / accent / semantic colors；
- 明暗、饱和度、色温；
- accent 使用面积和频率；
- gradient / transparency / material。

如果能可靠采样，记录近似色值；最终 Spec 仍应按语义角色组织，而不是散落 hex。

### 4. Spacing / Density
提取并聚类：
- page gutter；
- section gap；
- same-group gap；
- control padding；
- row height；
- icon-text gap；
- dense / balanced / spacious。

输出候选 spacing scale，例如：
`Observed ≈ 7/8/9, 15/16, 23/24 → Resolved 8 / 16 / 24`。

### 5. Shape / Surface / Border / Depth
提取：
- radius family；
- circle / pill / rounded rect 使用边界；
- border width / contrast；
- surface 层级；
- shadow offset / blur / spread / opacity 的视觉特征；
- material / glass / blur 等效果；
- 哪些对象允许 elevation。

### 6. Iconography / Imagery
提取：
- outline / filled；
- stroke personality；
- icon optical size；
- rounded / sharp endpoints；
- monochrome / multicolor；
- illustration / photo 的风格、crop、ratio、处理方式。

### 7. Motion
静态图片默认 `Unknown`。不要用“看起来活泼”反推出 180ms spring。

如果有动态图证据，再提取：
- duration；
- easing/spring；
- scale/opacity/translation；
- continuity；
- overshoot/bounce；
- reduced-motion 仍需另行定义。

---

## E. 页面构图

对每张独立页面图片生成 `Page Reverse Spec`：

```text
Page:
Viewport evidence:
Visual priority:
Structure tree:
Primary alignment axis:
Page gutter:
Top/bottom rhythm:
Sections:
- section name
  - width / height evidence
  - spacing before/after
  - internal gap
  - surface treatment
  - typography role
  - action position
Scroll/overlay evidence:
Observed states:
Unknown behavior:
```

如果同一个页面有多张截图，合并证据而不是为每张图创建互相冲突的规则。

---

## F. 设计系统与组件

从重复视觉模式中归纳：

### Token Candidates
- spacing scale；
- radius scale；
- type roles；
- semantic colors；
- border；
- elevation；
- icon sizes；
- common control heights。

### Component Grammar
识别反复出现的：
- Button；
- Input；
- Row；
- Card/Surface；
- Navigation；
- Chip/Badge；
- Modal/Sheet；
- Toolbar 等。

对每个组件逆向：
- anatomy；
- geometry；
- padding/gap；
- type/icon；
- surface/border/shadow；
- 当前可见 states；
- 未知 states。

只有有重复证据或明显独立语义时才上升为 component，不要从单个矩形臆造 design system。

---

## G. UI Contracts

图片只能建立**视觉侧 contract**：

`UI element → visible content → visible state → visible affordance`

图片无法证明：

`state owner → command → backend result → failure/recovery`

这些保持 Unknown，等待产品/代码证据。不得从按钮文字或视觉颜色反推权限、业务 lifecycle。

---

## H. Adaptation / Accessibility

单张截图只能检查可见线索：
- 对比度风险；
- 可见 target 大小；
- focus indicator 是否当前可见；
- text density；
- obvious clipping。

不能从一个 viewport 推断完整 responsive system。

多 breakpoint 图片时才归纳：
- 哪些元素重排；
- gutter 如何变化；
- column 如何变化；
- navigation 如何转换；
- content priority 如何变化。

没有证据的 dark mode、RTL、Dynamic Type、reduced motion 仍需在目标产品里补定义。

---

# 识图输出：Image Style Extraction Report

在编译 `UI-DESIGN-SPEC.md` 前，先形成一份短的逆向结果：

```text
IMAGE STYLE EXTRACTION

Evidence scope:
- ...

Observed structure:
- ...

Resolved Visual Laws:
1. ...
2. ...
3. ...

Resolved design language:
- composition:
- typography:
- colors:
- spacing/density:
- shape/radius:
- surface/border/depth:
- iconography/imagery:
- motion: Observed / Unknown

Token candidates:
- ...

Component grammar:
- ...

Page reverse specs:
- ...

Unknown / cannot infer from image:
- ...

Style DNA to preserve:
- ...

Source-specific details NOT to copy:
- ...
```

该报告是中间证据，不是最终交付。

---

# 编译回 UI-DESIGN-SPEC.md

识图完成后，沿用 `13-ui-design-spec.md`，把结果收束成权威设计规格。

规则：
1. `Observed` 和 `Resolved` 可以进入 Spec。
2. `Hypothesis` 必须先获得 Human/额外证据确认，或在 Spec 明确标成待定，不得伪装成确定规则。
3. `Unknown` 不得通过想象补齐；若目标项目必须定义该项，则按目标产品/平台重新设计，而不是声称“图片里就是这样”。
4. 如果用户要求“复刻风格但换产品”，Spec 中只继承 `Style DNA`，页面内容、状态、IA、交互由目标产品事实重新生成。
5. 最终仍必须给出具体 Typography / Color / Spacing / Radius / Surface / Component / Page Spec / Guardrails / Implementation Prompt。

---

# Image Reverse-Engineering Gate

进入最终 Spec 前检查：

- [ ] 结构、层级、构图已从图片明确提取。
- [ ] Visual Laws 不只是风格形容词。
- [ ] spacing/radius/type/color 等已从重复证据归纳，而非逐像素抄写。
- [ ] 页面和组件规则能解释图片中的主要视觉结果。
- [ ] Observed / Resolved / Unknown 已分开。
- [ ] 没有从静态图虚构 motion、responsive、hidden state 或业务 truth。
- [ ] 风格迁移时已经分离 Style DNA 与源产品业务/品牌特征。
- [ ] 最终结果可以编译进 `UI-DESIGN-SPEC.md`。

---

# 禁止模式

1. **Screenshot Tracing**：只抄坐标和像素，不提取设计系统。
2. **Single-Screen Overfitting**：把一张截图偶然出现的值当成整个产品规则。
3. **Image-As-Business-Truth**：从图片推断 permission、owner、lifecycle、backend state。
4. **Static-Motion Hallucination**：从静态图编造 duration/easing/spring。
5. **Responsive Hallucination**：从一个 viewport 编造断点和重排规则。
6. **Brand Cloning**：把源产品品牌色、logo、专属 icon、独特品牌资产当通用 Style DNA。
7. **Pixel Token Explosion**：为每个近似像素值创建独立 token。
8. **Mood-Only Extraction**：只输出“高级、温暖、极简”等形容词，不给 Visual Laws 和具体规则。

## 停止条件

当图片中可证明的设计结果已经被解释为一套能够复刻主要视觉效果的结构、Visual Laws、tokens、component grammar 和 Page Spec，同时不可证明的部分被明确隔离为 Unknown 时停止。

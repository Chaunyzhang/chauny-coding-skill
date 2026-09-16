# 视觉生成知识：从 Visual Laws 到成熟具体方案

**何时加载**：需要从零生成视觉方案，且没有足够成熟的 Existing Design System 或高质量参考可以直接复用；已有稳定视觉系统、纯局部 patch 时不要加载。

**目标**：补足“不要乱做”之外的正向设计知识。它不是风格模板库，而是一组可组合的成熟构图与视觉 recipe，帮助把 Visual Laws 编译成 `UI-DESIGN-SPEC.md` 的具体参数。

---

## 1. 先选构图语法，不先选圆角

按内容结构和任务 hierarchy 选择最接近的主构图，只选一个主骨架，其他只能局部借用。

### Flat single-flow / list-dominant
适合：Todo、设置、个人效率、内容列表、移动端主任务。
规律：一个主轴、少容器、spacing/typography 分组、列表是主体。
避免：每行独立 Card、多个并列 hero。

### Master-detail / split view
适合：邮件、文件、消息、管理工具。
规律：左侧选择改变右侧详情；selection/navigation owner 唯一；两区 hierarchy 明确。
避免：两侧同时争主视觉。

### Sidebar workspace
适合：桌面生产力、复杂 SaaS、编辑器外围。
规律：稳定导航 + 主工作区；工具栏/Inspector 只服务当前对象。
避免：把每个 secondary action 做成显眼 Card。

### Dense utility
适合：表格、运营、开发工具、专业工作台。
规律：高信息密度、短操作路径、语义状态明确、装饰退后。
避免：为了“高级”拉大所有留白。

### Editorial / typography-led
适合：内容、品牌、portfolio、阅读型界面。
规律：Typography、尺度和留白建立层级，盒子退后，imagery 可成为主角。
避免：dashboard 化、组件边框过多。

### Dashboard / modular grid
适合：多个并行指标/模块必须同时可见。
规律：明确 grid、模块 priority、比较关系；Card 是数据模块边界而非默认装饰。
避免：所有模块同尺寸同权重。

### Canvas + inspector
适合：设计、图形、节点、地图、编辑器。
规律：Canvas 是主对象；工具/Inspector 围绕当前 selection；浮层不遮核心操作。
避免：让 chrome 比内容更抢。

### Immersive / media-first
适合：视频、图片、地图、阅读沉浸场景。
规律：内容占据主要视觉面积，controls 按需出现，overlay 控制透明度和干扰。
避免：常驻重 chrome。

---

## 2. Hierarchy recipe

默认优先级：
1. position / grouping
2. type scale / weight
3. spacing
4. contrast / color
5. surface / border
6. elevation / motion

不要一开始就靠高饱和颜色、Card 或 shadow 建 hierarchy。每个 viewport 默认只允许 1 个真正的 primary focal area；secondary action 不因“重要”就一定更大更亮。

---

## 3. Typography recipe

目标：用少量稳定角色形成明显而不过度的 hierarchy。

常用角色建议控制在 4–6 个：Display/Page Title、Section Title、Body、Body Strong、Meta、Control。

通用起点（非平台硬编码，可映射到系统 text styles）：
- Display/Page title：正文约 1.7–2.1×，行高约字号 1.15–1.25×。
- Section title：正文约 1.1–1.3×。
- Body：作为视觉基准。
- Meta：正文约 0.8–0.9×，通过尺寸 + contrast 共同退后。
- Control：通常接近 Body，不为按钮单独创造夸张字号。

规则：
- 同一层级不要同时用 size、weight、color、case 四种手段全部强调。
- 长文本优先保证 line-height 和 measure，再追求“紧凑”。
- 新页面不得自行新增近义字号。

---

## 4. Spacing / density recipe

优先使用 4pt 基础节奏或现有平台/system spacing，常见序列：
`4 / 8 / 12 / 16 / 24 / 32 / 48`。

关系规则比数字更重要：
- 同组 internal gap < item gap < section gap。
- section gap 通常至少是同组 gap 的 1.5–2×。
- dense utility 可整体缩紧，但比例不乱。
- spacious/editorial 可扩大 section gap，但不要把 controls 也无差别拉大。

禁止每页发明 `13/19/27` 一套“差不多”间距。

---

## 5. Shape / radius recipe

先决定 shape personality，再形成家族，不逐组件独立选值。常见家族：
- restrained：small 4–6 / controls 6–10 / large surface 10–14
- balanced-soft：small 6–8 / controls 8–12 / large surface 12–16
- expressive-soft：只在 Primary 允许时进一步放大；避免所有对象都 pill

规则：
- 小元素 radius 通常不应比大 surface 更夸张。
- pill 只用于 tag/chip/segmented/status 等有语义理由的形态。
- Mature/Minimal 会抑制过度 softness；Warm/Friendly 可软化但不能自动变 Cute。

---

## 6. Surface / border / depth recipe

默认从 flat 开始，只有 hierarchy/containment 有理由才增加 surface/depth。

优先顺序：
`spacing → typography → subtle divider/border → surface difference → elevation`。

建议控制 2–4 个 surface level：
- base
- grouped/secondary
- floating
- modal（若需要）

普通 list row/content 不因为“看起来高级”自动加 shadow。Elevation 应和“浮在内容之上”的行为对应。

---

## 7. Color recipe

先定义角色，再选色值：neutral foundation + one primary accent + semantic status。

默认控制：
- 大面积由 background/surface/text 中性色承担。
- Accent 用于 action/selection/focus/关键状态，不做无意义装饰铺色。
- 同一 viewport 多个高饱和块会迅速破坏 Quiet/Minimal/Premium。
- Lively 可以提高 accent 能量，但优先放在局部 response/icon，而不是把整个 palette 变多彩。

若没有品牌色/参考，先选 hue family，再调 saturation/lightness；不要同时引入多个互不相关 accent family。

---

## 8. Icon / imagery recipe

Icon：一个 family、一套 optical weight、一套 selected policy。
- standard control icon 常在 16/20/24 一组。
- outline family 不随意混 filled；若 selected 状态切 filled，必须全局一致。
- 次要“活跃感”很适合由 icon shape/micro-motion 承载。

Imagery：必须定义角色（hero/content/decoration/empty-state）、裁切/aspect ratio、fallback；不要同时让 illustration、photo、gradient 都争风格主导权。

---

## 9. Motion recipe

Motion 必须有 job：反馈、连续性、状态变化、空间关系。

常见起点：
- micro response：120–180ms
- state transition：160–240ms
- structural transition：220–360ms

规则：
- Quiet/Minimal/Mature：短、低振幅、少 overshoot。
- Lively：可增加局部 scale/translation/shape response，但不侵占结构层。
- Playful 只有在主方向允许时才使用明显 bounce/spring。
- reduced motion 必须有等价静态反馈。

这些是生成起点；平台已有成熟 motion semantic 时优先平台。

---

## 10. 常见统一组合（不是模板）

### Minimal + Lively
结构：flat / low-container / typography-led。
表达：一个清晰 accent，icon 可以更有 personality。
微表达：press/completion/transition 承载能量。
禁止：多彩 Card、装饰渐变、多个 focal point、大面积强饱和。

### Warm + Mature
结构：稳定、清楚、不过度松散。
表达：暖中性、balanced-soft geometry、低糖果感。
微表达：soft settle。
禁止：pastel candy、oversized pill、cute illustration 自动泛滥。

### Professional + Technical
结构：grid/alignment 清晰、密度中高。
表达：精确 border、语义状态色、克制 shape。
微表达：快、直接。
禁止：装饰性 animation、无意义大留白。

### Premium + Editorial
结构：Typography/scale/whitespace 主导。
表达：少色、精细 type、低噪 surface/depth。
微表达：polished but restrained。
禁止：组件盒子过多、廉价 gradient、同屏多 accent。

---

## 11. Concrete Recipe Gate

进入高保真或 Full/Page Spec 前，视觉方案必须至少能给出：
- 主构图语法与 focal rule
- type roles + scale relationship
- spacing scale + group/section rhythm
- radius family
- surface/depth levels
- color roles + accent participation
- icon policy
- motion character + timing range
- 5–10 条当前方向最关键的 Forbidden

若还只能说“高级、温暖、现代、简洁”，继续解析；若已有批准的 Spec/参考，优先复用，不用知识库覆盖它。

## 停止条件

当 Visual Laws 已被编译成具体且互相一致的 composition/type/spacing/shape/surface/color/icon/motion 规则，并能直接写入 Spec 时停止。

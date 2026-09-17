# 视觉设计：统一语言、Visual Math 与视觉下限

目的：把感觉/参考/产品语义编译成**一套具体视觉系统**；保证不了必定惊艳，但必须排除稳定显乱、显脏、显业余的做法。

## 1. 输入优先级

`Human correction / Avoid > 已批准 Existing Spec > 高质量视觉证据 > 本模块知识 > Agent 自由发挥`

已有 Spec 时默认继承，不为“更好看”擅自换语言。

## 2. 从感觉到 Visual Laws

Human 形容词先分：
- **Primary**：控制结构层。
- **Secondary**：在不破坏 Primary 的前提下加味道。
- **Micro-expression**：适合进入 icon / motion / feedback 等局部表达。
- **Avoid**：veto。

冲突不做平均。输出 3–5 条 Visual Laws，例如：
- Typography + spacing 先于 container 建层级。
- 普通内容保持 flat；elevation 只属于浮层。
- 活力来自交互反馈，不来自满屏装饰。
- 一个 viewport 只允许一个强视觉焦点。

Visual Laws 必须能生成新组件；否则只是形容词换写。


## 3. Visual Order：先证明“排得好”

风格之前先建立视觉秩序。完整 Surface 至少明确：

- **Focal order**：第一、第二、第三视觉焦点；同一 viewport 不应有多个同等级强焦点。
- **Alignment axes**：页面只保留少量主轴；文本列左对齐、数字/百分比通常按同一数值轴对齐，状态/操作列固定职责。
- **Grouping**：先用 proximity、alignment、type 建关系，再考虑 surface/border/container。
- **Density rhythm**：该紧的关系紧、该松的区域松；不要整页所有 gap 都接近。
- **De-emphasis**：ID、时间戳、环境说明、辅助文案等若不是当前任务核心，应降低存在感、按需显示或移到次级位置。
- **Container strategy**：框只在提供独立语义、交互边界或背景层级时存在；若删掉框仍能理解关系，优先删框。

### 灰度/弱色检查（高价值时执行）

对完整新页面、重设计或层级存疑页面，在加完整配色前做一次灰度或弱化色彩检查：

- 不靠 accent，能否看出主焦点？
- 不靠状态色，分组和层级是否仍清楚？
- 是否出现“整屏都是同一视觉音量”的均匀灰块？
- 是否有某些无意义彩色元素在承担本应由结构完成的层级？

灰度检查是诊断工具，不要求最终 UI 灰度，也不用于有明确色彩语义的状态判断。

### 视觉预算

不是硬编码数字，而是限制同时竞争的视觉手段：

- 一个 viewport 默认只有 **1 个主焦点**；第二焦点必须明显退一级。
- Accent 以单一主色系为默认；新增颜色必须有语义或品牌理由。
- 普通内容默认 flat；elevation 只给真正浮层或少数需要层级分离的对象。
- Type roles、radius、shadow、icon size 都使用有限 family；出现新角色要先证明已有角色不够。
- 不要同时用“大字号 + 高饱和 + 大阴影 + 渐变 + 动画”强化同一对象，优先选择 1–2 个最有效手段。

---

## 4. 先选 Composition Grammar，再调皮肤

根据内容与任务选择，不按个人喜好：

- **Flat single-flow / list-dominant**：顺序任务、阅读、todo、feed；低容器噪声。
- **Master-detail / split view**：列表+详情、mail、文件、管理工具。
- **Sidebar workspace**：多模块工具、桌面生产力、console；导航稳定。
- **Dense utility**：表格、筛选、批处理；高信息密度但层级必须强。
- **Editorial / typography-led**：内容/叙事主导；排版和留白承担层级。
- **Dashboard / modular grid**：并行指标/模块；必须有明确主卡，不得全卡同权。
- **Canvas + inspector**：编辑器/设计工具；对象区与属性区职责分离。
- **Immersive / media-first**：媒体/品牌体验；内容可读性与 fallback 仍优先。

Product UI 不为了“原创”破坏用户已熟悉的导航、表格、筛选、表单 affordance。个性优先放在 palette、type、surface、icon、motion character。

## 5. Visual Math

### 5.1 Typography scale

- 只从批准的 type roles/scale 取值。
- 同一 role 固定 `font-size + line-height + weight + tracking`。
- 相邻层级必须有足够辨识度；`14 → 18 → 20` 这类后两级过近时应合并角色或拉开差异。
- 推荐从有限比例/级差生成候选，再按平台与内容修正；不要迷信某个固定 1.25 比例。
- 普通产品页优先控制在少量稳定角色：Display/Page/Section/Body/Meta/Control，按需减少而不是增加。
- 长正文行宽要可读；极宽正文列应限制 max width。

### 5.2 Spacing scale 与 Relationship Contrast

- 只使用有限 spacing scale，例如 `4/8/12/16/24/32/48` 或项目既有 scale。
- 同一语义关系使用同一间距。
- **组内距离 < 组间距离，且差异必须视觉可辨。** `16 vs 20` 若承担两种层级通常太弱；`8 vs 24/32` 更清楚，但具体值由内容和 density 决定。
- section rhythm、component padding、row gap、page gutter 各有角色，不临场发明。
- 大量 `15/17/23/31` 近义值优先归并，而不是解释成“微调”。

### 5.3 Alignment

- 页面只保留少量明确 alignment axis。
- 同组内容边缘应对齐；无理由的 3–8px 漂移视为缺陷。
- 不要用每个 Card 的内部 padding 差异制造“手工感”。

### 5.4 Geometry families

- Radius 使用有限 family：如 small control / standard control / surface / modal；pill 只用于语义确实需要 capsule 的场景。
- 同级 controls 高度一致，除非交互角色不同。
- Icon size/stroke/fill family 一致；不要 mixed outline/filled/random stroke。
- Border 与 shadow 也要形成角色，而不是每组件自定义。

## 6. 视觉维度生成规则

### Typography
先确定层级关系，再选字体。字号、字重、行高共同构成 role；不要用颜色补救弱层级。

### Color
先定义 role：background / surface / primary text / secondary text / accent / semantic states。Accent 是稀缺资源；颜色不能替代结构。

### Shape / Surface / Depth
Surface 是信息层级工具，不是装饰。普通内容优先 flat；border、surface tint、shadow 按语义层级逐步增加，不得到处 elevation。

### Icon / Imagery
同一产品只使用相容的 icon grammar。Imagery 应服务内容/品牌，不用装饰图填空。

### Motion
定义 response / state / structural 三类 timing；Motion 表达状态连续性而不是“看起来高级”。避免无理由 bounce/overshoot；支持 reduced motion。

## 7. 常见相容组合（校准，不是模板）

### Minimal + Lively
结构：flat / low-container / restrained palette。
活力：icon personality、accent moment、completion/press motion。
禁止：多彩 surfaces、多个 focal points、装饰性大渐变。

### Warm + Mature
暖中性色、适度柔软 shape、稳定 typography；成熟感抑制糖果色、过大圆角和 bounce。

### Professional + Technical
规则 grid、明确状态/数据、紧凑但可读；技术感不能把正文全部 mono，也不能牺牲 hierarchy。

### Premium + Editorial
少而准的视觉重点、排版主导、克制 surface/depth；不要把“大留白 + serif”当万能高级公式。

## 8. Craft Floor：Hard Fail

以下默认不能进入最终 Spec：

1. **框套框无新语义**：去掉内层框后关系仍清楚，则去掉。
2. **层级塌缩**：标题、CTA、卡片、accent 同时高强调。
3. **Typography entropy**：同页随机字号/字重/字体；scale 外近义值增殖。
4. **Spacing entropy**：关系相同却间距不同；组内/组间对比不足；大量近义值。
5. **Alignment drift**：同组内容无理由错轴。
6. **Color drift**：同义 role 使用不同颜色；新 accent 中途出现。
7. **Radius / shadow / icon system 分裂**。
8. **State geometry jump**：hover/focus/loading/error 改变尺寸或推动邻居。
9. **Content stress 破坏**：长文本、空值、大字体直接挤爆。
10. **Accessibility floor 失败**：focus 不可见、对比不足、触控目标过小、状态只靠颜色。

## 9. Warning：高概率模板/廉价，但可有理由覆盖

- Decorative gradient 作为默认装饰。
- Glass/blur everywhere。
- All-card layout / repeated identical card grid。
- Universal pill / 过大圆角。
- 普通内容大量重阴影。
- gradient + glass + glow + texture 同时叠加。
- 每节 eyebrow、小编号、divider 装饰 spam。
- Product UI 为了视觉新奇破坏熟悉的导航/交互。

覆盖 Warning 时，在 Spec 里写一句“为什么这里值得”。


## 10. Final Subtraction Audit

最终 rendered UI 在交付前做一次减法检查。目标不是“越少越高级”，而是删除没有承担职责的视觉噪声：

- 哪些框、border、surface 去掉后关系仍然清楚？删。
- 哪些颜色没有语义/品牌职责，只是在随机丰富页面？删或归并。
- 哪些辅助小字并不帮助当前任务，只是在解释系统？弱化、隐藏或移到按需位置。
- 哪些元素使用了重复的强调手段？保留最有效的一种。
- 是否存在“组件库拼装感”：一排同样 outline 控件、同构 cards、默认 badge，而页面没有自己的视觉重心？重新建立整体秩序。
- 表格/列表是否对齐稳定：主文本、辅助文本、数字、状态、操作分别遵守统一列规则？
- 缩小或模糊看页面时，是否还能看出主要块、焦点和阅读路径？若只剩均匀噪声，层级未完成。

Final Subtraction Audit 属于 Agent 机械自查；“这样是否更美”仍由 Human 裁决。

## 11. Concrete Recipe Gate

进入高保真或实现前，必须已经得到具体的：

`Composition / focal order / type roles / spacing scale / page gutter / density / color roles+values / radius family / border / surfaces / shadow levels / icon grammar / imagery / motion / component treatment / Forbidden`

如果仍是“适度圆角、舒适留白、现代高级”，视觉设计未完成。

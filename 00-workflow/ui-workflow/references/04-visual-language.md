# 视觉语言：从感觉到统一规则

**何时加载**：需要新建、改变或澄清视觉方向；已有稳定设计系统且任务纯局部时可直接复用 Existing。

**目标**：把 Human 的主观感觉编译成一套统一、可执行、能约束页面和组件的视觉语言。

如果视觉方向来自截图/设计稿，而不是 Human 形容词，先读取 `14-image-style-reverse-engineering.md` 的 `Resolved Style DNA`。图片已经证明的 Visual Laws / type / color / spacing / shape / surface / icon 规则优先作为输入，本模块负责统一和消解，而不是重新凭感觉发明另一套风格。


## 视觉来源优先级

视觉决策不能把所有来源等权混合。默认优先级：

1. **Human 明确 correction / Avoid**：最终审美方向的最高优先级。
2. **当前任务中被批准的 Existing Design System / Spec**：若不是明确 redesign，不得随意推翻。
3. **高质量参考/截图的 Observed + Resolved 证据**：用于复刻/迁移时优先于知识库。
4. **视觉生成知识库**：当现有系统或参考不足时，用 `16-visual-generation-knowledge.md` 补齐成熟构图与视觉 recipe。
5. **Agent 自由发挥**：只填无法由前四项决定、且属于 UI 设计权范围的剩余细节。

任何低优先级来源不得默默覆盖高优先级来源。

## Human Alignment

只对齐会改变整体方向的内容：

- 产品气质。
- 想突出什么、压低什么。
- 密度和节奏。
- restrained vs expressive。
- organic vs geometric。
- motion character。
- 明确 Avoid。

不要让用户审批普通 padding、radius、token 数值。

用户说“挤、廉价、死、幼稚”时，先把它当作设计症状，推断可能原因，再结合真实 UI 判断；不要直接把一个词机械映射成一个属性。

## 多个形容词先分角色

- `Primary`：主导结构层。
- `Secondary`：在不破坏 Primary 的前提下改变表达。
- `Micro`：主要进入局部反馈、icon、micro-motion、delight。
- `Avoid`：否决项。

多个词不是等权平均。

## 三层视觉责任

### 结构层
决定整体首先被识别成什么：

- composition
- hierarchy
- layout
- density / spacing rhythm
- container strategy
- typography hierarchy
- primary color logic

### 表达层
决定组件和表面的性格：

- radius / shape
- surface
- border / depth
- iconography
- control treatment
- local color
- imagery

### 微表达层
承载局部能量和人格：

- hover / press / focus
- transition
- completion / success feedback
- micro-motion
- small accent / illustration moments

**规则**：Primary 控制结构层；Secondary 只能在不破坏结构统一的前提下影响表达；冲突但有价值的次要特征可下沉到 Micro。

## 常见视觉倾向

这些是倾向，不是公式。

| 特征 | 结构倾向 | 表达倾向 | 微表达倾向 |
|---|---|---|---|
| 极简 | 少焦点、低嵌套、Typography/留白主导 | 低装饰、低 elevation、少颜色角色 | 短、安静 |
| 安静 | 低同时强调、稳定层级 | 低视觉噪声 | 低振幅、soft settle |
| 温暖 | 可保持简洁结构 | 暖中性、柔和 surface、适度 soft geometry | 温和反馈 |
| 成熟 | 克制、稳定、明确 | 低糖果感、低夸张 softness | 避免 novelty/bounce 为目的 |
| 活跃 | 不应自动改写结构 | 局部高能 accent、icon personality | 更明显但受控的 feedback/motion |
| 专业 | 明确 hierarchy、规则 alignment | 语义色、受控几何 | 功能性反馈 |
| 高级 | 少而准、强比例、低噪声 | 精细 typography / border / depth | polished but restrained |
| 技术 | 信息优先、规则 grid | 精确、语义状态明显 | 快、直接 |
| Editorial | 内容/字体主导、少盒子 | imagery 可更重要 | subtle |
| Utility | 任务效率优先、高密度可接受 | 弱装饰 | minimal |
| Playful | 不宜与严肃结构同时主导 | expressive shape/color/icon | bounce / surprise 可局部存在 |

## 兼容与对冲

对会影响结果的组合，判断：

- `Reinforcing`：同向加强。
- `Compatible`：可自然共存。
- `Tension`：可共存，但必须分层或定主次。
- `Conflict`：不能同时主导同一关键维度。

典型：

- 极简 + 成熟：强化。
- 温暖 + 成熟：兼容，结果是“柔和但不过甜”。
- 极简 + 活跃：张力。极简控制结构，活跃进入 icon / accent / micro-motion。
- 安静 + 活跃：张力。安静是底，活跃只出现在有意义反馈。
- 成熟 + Playful：强张力；必须明确谁主导。

禁止“每个形容词都拿一点”的平均法。

## 从方向编译成规则

最终必须明确：

- Composition / hierarchy 靠什么建立。
- Density / spacing rhythm。
- Typography 角色和尺度关系。
- Color role、饱和度、accent 使用频率。
- Shape / radius personality。
- Surface / border / depth 策略。
- Icon / imagery 语言。
- Motion / feedback 性格。
- 明确禁止什么。

示例：

```text
Primary: Minimal, Mature
Secondary: Warm
Micro: Lively
Avoid: Cute

Resolved:
- 单列、低容器、Typography + spacing 建层级
- 暖中性底色，accent 低频
- 中等圆角，不 universal pill
- 普通内容不用 shadow，浮层才有 elevation
- icon 和完成反馈允许更灵动
- 禁止糖果色、夸张 bounce、卡通插画
```

## Contribution Check

每个重要 Human trait 至少能指出 2–3 个实际改变的设计决定。若删掉该 trait 后 UI 基本不变，说明它没有真正进入设计。

## Visual Coherence Gate

检查：

- 第一眼主风格是否明确。
- 结构层是否同一套逻辑。
- shape/icon/color/motion 是否各说各话。
- Secondary 是否侵占 Primary。
- Avoid 是否偷偷回来。
- 每个重要视觉选择能否解释来源。

## 停止条件

当视觉方向已经能直接约束页面构图、组件、tokens 和 motion，而不是只剩形容词时停止。

---

## Visual Laws：从方向到统一世界

Resolved traits 之后，不得直接跳 token。先写 3–5 条能跨页面、跨组件约束结果的 Visual Laws。

Visual Law 应同时影响多个维度，例如：

- `Typography + spacing before containers` 会同时约束 hierarchy、Card 使用、divider、surface 和 section rhythm。
- `Energy lives in response, not decoration` 会约束 accent、icon、motion、surface 和 illustration。
- `Only floating layers get elevation` 会同时约束 row、card、popover、sheet、modal。

如果一条规则只能决定一个数值，它不是 Visual Law，而是 token。

## 最终视觉输出不得停在倾向

在交付实现前，本模块的结论必须进入 `UI-DESIGN-SPEC.md` 并解析为具体：

- Typography roles + size/line-height/weight/tracking。
- Color roles + exact value/system semantic。
- spacing scale + page/section/component gaps。
- radius scale + 使用边界。
- border / surface / elevation/shadow。
- icon family/size/stroke/filled policy。
- motion timing/easing/spring + reduced-motion fallback。
- component treatment。
- Forbidden / Guardrails。

不得把 `中等、适度、舒适、轻微、现代、精致` 等词留给实现阶段解释。

完整输出格式见 `13-ui-design-spec.md`。

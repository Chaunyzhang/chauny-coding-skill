# 视觉下限：先排除必然显脏、显乱、显业余的做法

**何时加载**：任何需要新视觉方案、页面构图、高保真设计、视觉重构或最终视觉验收的任务。纯数据/业务/实现重构且 rendered result 不变时可不加载。

**目标**：本模块不保证“高级”或“惊艳”。它只负责把高概率导致界面显乱、显廉价、显不专业的结构性问题在设计阶段排除掉。

## 0. 使用方式：Hard Fail 与 Warning 分开

不要把个人审美偏好伪装成普遍规律。

- `Hard Fail`：会破坏层级、分组、一致性、可读性、对齐或状态稳定性的结构性问题。默认必须修。
- `Warning`：经常显得廉价/模板化，但在明确 Art Direction 下可能成立。必须有理由，不能默认使用。
- `Allowed`：有明确语义、平台或品牌理由，且不破坏整体系统。

**规则**：Hard Fail 进入 Gate；Warning 进入设计审查，不自动否决。

---

# A. Hard Fail：默认不允许带进最终 Spec

## 1. 对齐漂移

禁止：
- 同一页面中标题、正文、按钮、列表分别落在没有理由的不同左/右轴上。
- 同层级元素出现 1–4px 的随机错位。
- 同一组件在不同页面的 padding / baseline / icon placement 漂移。

要求：
- 每个 Surface 必须有明确主 alignment axis / grid。
- 同类组件使用同一内部几何规则。
- 任何例外都必须有可说明的视觉或语义理由。

**为什么是 Hard Fail**：网格和稳定对齐是界面“整洁、可扫读、像一个系统”的最基础来源。

## 2. 间距无体系 / 分组关系反了

禁止：
- 同一层级出现大量 `13/15/19/23/27` 这类近似但不一致 gap。
- 组内距离 >= 组间距离，导致用户看不出谁和谁是一组。
- 同类 Section 在不同页面使用不同节奏且无理由。

要求：
- spacing 来自批准 scale。
- `internal gap < item/group gap < section gap` 作为默认关系。
- 相关性优先用 proximity 表达，再考虑 divider / surface / card。

## 3. 框套框但没有新的语义层级

禁止：
- Page background → Card → inner Card → bordered block → input container，仅为了“看起来完整”。
- Card 内每一个小分组再套独立 Card。
- 同一视觉平面连续出现多个 border + radius + background，实际没有新的 selection / scroll / state / ownership 边界。

允许：
- 内层容器确实代表新的语义组、可独立交互、独立滚动、selection、drag target、权限/状态边界或浮层。

默认替代顺序：
`spacing → typography → divider → subtle surface → card/container`

**测试**：去掉内层框后，语义是否仍然清楚？如果是，优先去掉框。

## 4. 层级塌缩：所有东西都在喊

禁止：
- 同一 viewport 同时存在多个同等强度的 hero / accent CTA / 高饱和块。
- 每个标题都很大、每个按钮都 primary、每个模块都有独立强调色。
- 用颜色、字号、阴影、粗体四种手段同时强调同一批元素。

要求：
- 每个 viewport 通常只有一个 primary focal area。
- secondary / tertiary 必须真实退后。
- hierarchy 优先由 position / grouping / type / spacing 建立，再用颜色和 elevation。

## 5. Typography Entropy：字号、字重、字体各自发挥

禁止：
- 页面自己新增一套近义字号。
- 同一个语义角色在不同页面换字号/字重/字体。
- 为了“高级”混用过多字体家族。
- 小字号配极细字重，牺牲可读性。
- 长正文行高过紧，三行以上仍使用压缩 leading。

要求：
- 稳定 type roles；通常 4–6 个角色足够。
- 同一角色在全产品一致。
- 字体家族尽量少；新增字体必须说明承担什么角色。
- 长文本优先可读性，不追求视觉“紧”。

## 6. 颜色没有角色 / Accent 漂移

禁止：
- 相同颜色在一个地方表示可点击，另一个地方只是装饰。
- 新页面随手加入第二/第三套 accent。
- 为了区分层级不断引入新色，而不是先解决 hierarchy。
- 文字/控件对比不足。

要求：
- 颜色先定义 semantic role，再定义值。
- accent 是稀缺资源。
- status color 与 brand/accent 的职责不要混淆。
- light/dark/high-contrast 下保持语义一致。

## 7. Shape / Radius 系统分裂

禁止：
- 同一产品出现大量无理由的 6/8/10/12/14/16/18/20 圆角。
- 小控件比大 Surface 更“圆”，却没有明确 shape logic。
- Button 全 pill、Card 中圆角、Input 方角，各自像不同产品。

要求：
- 使用一个 radius family，而不是逐组件调手感。
- Pill 只在语义上适合 chip/tag/segmented/status 等形态时使用。

## 8. Shadow / Elevation 没有层级逻辑

禁止：
- 普通内容列表每行都有 shadow。
- 同一页面同时出现多种方向、模糊、扩散完全不同的阴影系统。
- 视觉上“浮得最高”的对象并不是交互/层级上最高的对象。

要求：
- elevation 与 layering 对应。
- 普通内容默认 flat；floating / popover / sheet / modal 才逐级增加 depth。
- 同一套 light/depth logic 贯穿组件。

## 9. Icon / Control 语言混杂

禁止：
- filled、outline、不同 stroke weight、不同 corner personality 随机混用。
- 同类 icon 的视觉尺寸不一致。
- 同一排 control 高度、baseline、icon/text gap 不一致。

要求：
- 一个 icon family / optical weight / selected policy。
- 控件共享尺寸和对齐规则。

## 10. 状态变化导致几何跳动

禁止：
- hover/focus/error 时 border width 改变导致布局位移。
- loading 替换文案后按钮宽度突然改变。
- error/helper 出现后整个表单无预期跳动。
- selected/pressed 状态引入未在 Spec 中定义的尺寸变化。

要求：
- 状态变化优先改变 color / opacity / outline / transform，不破坏基础 geometry。
- 必要的结构变化提前预留空间或明确 transition。

## 11. 内容被裁断、挤爆、溢出，却没有设计规则

禁止：
- 只按理想短文案排版。
- 长标题与 metadata 重叠。
- scrollable region 无法查看完整被截断内容。
- Dynamic Type / localization 后核心动作掉出可用区域。

要求：
- Page/Component Spec 里明确 content bounds、wrap/truncate、reflow、overflow。

## 12. Accessibility Floor 破坏视觉下限

禁止：
- 低对比正文/辅助文字低到无法可靠阅读。
- focus 不可见。
- pointer/touch target 过小或过密。
- 状态只靠颜色表达。

这些不仅是 accessibility bug，也会直接让界面显得脆弱、不可用、缺乏完成度。

---

# B. Warning：高概率显廉价/模板化，但不是绝对禁令

以下默认先克制；只有当 Visual Laws / reference / brand direction 明确支持时才使用。

## 1. Decorative Gradient

警告：
- gradient text。
- CTA、Card、背景同时多处渐变。
- 渐变只是为了“高级/科技”，没有内容或品牌理由。

允许：
- 品牌本身就是渐变语言。
- 渐变承担空间、状态、数据或光源表达。
- 一处受控 hero/ambient gradient，不和内容竞争。

## 2. Glass / Blur Everywhere

警告：多个普通 Card 都使用 blur/translucency。

允许：真正需要层级透视、浮层、OS material 或内容透出的场景。

## 3. All-Card Layout

警告：任何信息都先套 Card。

先问：spacing / typography / divider 能否表达分组？Card 是否真的代表独立模块、selection、drag、scroll 或状态边界？

## 4. Oversized Radius / Universal Pills

警告：为了“友好/现代”把 Button、Input、Card、Tab 全做成大胶囊。

允许：品牌语言或特定 control semantic 明确需要。

## 5. Heavy Decorative Shadow

警告：阴影成为视觉装饰主角，而不是层级结果。

## 6. Too Many Decorative Treatments

警告：gradient + glass + texture + glow + shadow + border + illustration 同时出现。

规则：一个视觉区域优先只有一个主要表达机制，其他手段服务它。

## 7. Repeated Identical Card Grid

警告：所有模块同尺寸、同图标+标题+描述、同视觉权重。

若内容优先级不同，构图必须表达差异；若它们确实同级，统一 grid 才成立。

## 8. Eyebrow / Small Caps / Divider Decoration Spam

警告：每个 Section 都机械加 eyebrow、小短线、序号、装饰 divider，只因为“设计稿看起来空”。

先问这些元素是否提供 navigation、category、sequence 或 brand rhythm。

## 9. Pure Visual Novelty on Product UI

警告：为了独特，改变用户熟悉的 navigation、table、form、selection、back、sheet 等基本认知。

产品 UI 的个性优先放在 palette、type、surface、density、icon 和 motion character，不要拿核心交互范式冒险。

---

# C. Craft Floor 自查

进入高保真前与最终 rendered verification 各跑一次：

```text
[ ] 主视觉焦点是否唯一且明确？
[ ] 主要内容是否落在稳定 alignment/grid 上？
[ ] 同组/跨组间距关系是否清楚？
[ ] 是否存在无语义理由的框套框？
[ ] Typography roles 是否有限、稳定、可读？
[ ] 是否出现新字号/字重/字体漂移？
[ ] Color roles 是否清楚，accent 是否漂移？
[ ] Radius family 是否统一？
[ ] Surface / border / shadow 是否表达真实层级？
[ ] Icon/control 语言是否统一？
[ ] 状态变化是否造成无意 geometry shift？
[ ] 长文案/多数据/大字号是否仍成立？
[ ] 是否有低对比、不可见 focus、过小 target？
[ ] 是否用了 gradient/glass/pill/shadow/card 作为无理由装饰？
```

任何 `Hard Fail` 未解决，不进入最终 Human 审美验收；先修机械下限问题。

---

# D. 与 Human 审美的边界

Craft Floor 只能判断“结构性脏乱、内部不一致、可读性差、明显模板化风险”，不能宣布“这个设计高级/漂亮”。

- Hard Fail：Agent 直接修。
- Warning：Agent 解释风险；若它是 Human 已确认的 Art Direction，则保留。
- Human 明确喜欢某个非常规选择时，不用“最佳实践”压掉 Human；只保证它不会破坏可读性、状态和系统一致性。

---

# E. 依据与原则来源

本模块主要依赖这些广泛认可的视觉原则，而不是某个博主的个人风格：

- 清晰 visual hierarchy、grid/alignment、consistency。
- Gestalt proximity / similarity：距离与相似性应表达真实分组关系。
- Typography：字号、字重、颜色传达 hierarchy；字体家族不应无理由增殖；小字避免过细。
- Color：颜色应保持一致语义并克制使用，尤其是 accent/status。
- Layout：相关项目应分组、重要信息应有足够空间、组件应保持一致 alignment/spacing。
- Accessibility：contrast、focus、target size、状态表达属于基本完成度。

## 停止条件

当所有 Hard Fail 已排除，Warning 要么被删除、要么有清晰 Art Direction/产品理由，并且这些规则已进入 Visual Spec / Guardrails 时停止。

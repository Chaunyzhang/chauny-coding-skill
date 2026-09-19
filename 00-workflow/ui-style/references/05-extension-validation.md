# 05 — Extension Validation

目标：验证的不是“是否把参考抄得像”，而是“设计 DNA 能否延续”。

## 1. Novel-page Extension Test

至少选择 3 个与参考 IA 明显不同的新页面任务。

例如参考是首页任务流，可测试：

- 搜索结果 / 内容发现
- 详情页 / 编辑页
- 个人资料 / 数据统计

不要三个都只是同一 card stack 换文案。

## 2. 同时检查两种失败

### 太松

症状：

- 主色、type hierarchy、radius/material 被重新发明。
- 同一 canonical component 在不同页漂移。
- rendering regime 失效。
- 新页面像另一个产品。

处理：提升真正 signature 的 Kernel/Grammar 权重，不是把整个页面模板锁死。

### 太紧

症状：

- 三个新页面结构几乎一样。
- 参考有 hero，之后每页都有 hero。
- 每个页面都沿用相同 section/card arrangement。
- 强模型只能“替换内容”。

处理：把 source-specific layout 降为 local/exemplar，把 exact number 改为 range/relationship，扩大 Creative Field。

## 3. 四个核心测试

### Kernel Integrity

新页面是否保持真正的 signature rules？

### Grammar Consistency

spacing/type/surface/shape/icon 等关系是否仍符合 Grammar？

### Component Identity

同一 Component ID 是否保持同一 contract？

### Creative Headroom

在不破坏前面三项的情况下，新页面是否出现合理的新构图、新组合或新组件？

## 4. Weak-model Guardrail Test

让消费者不做额外风格推理，只按 Kernel + Grammar + canonical components 组合一个新页面。

应该仍然得到基本属于同一产品的结果。

若必须重新猜主色、字体层级、surface material、icon character，Spec 太松或缺关键规则。

## 5. Strong-model Freedom Test

给强模型一个开放的新页面任务。

应该允许：

- 新 composition
- 新 component anatomy
- 新局部视觉巧思

只要 Kernel/Grammar/component identity 不被破坏。

若结果退化成模板填充，Spec 太紧。

## 6. Holdout Test

多参考时，用部分 source 归纳 Spec，剩余 source 做 holdout。

理想情况：holdout 大多数视觉由已有 system 解释，只有真正新 role 需要新增。

若每张新图都需要一套新 spacing/radius/type/color，抽取失败。

## 7. Repeatability

重复消费同一 Spec：

- Kernel 应稳定。
- canonical components 应稳定。
- Grammar 不应产生 near-duplicate tokens。
- open 区域不要求每次给相同答案。

“稳定”不是所有生成都长一样。

## 8. Reconstruction Fidelity（需要时）

复刻任务额外验证：

- geometry anchors
- typography spatial behavior
- color/effect relationships
- component dimensions
- tolerance 来源

不要把 reconstruction fidelity 指标拿去惩罚 extension 的合理创新。

## 9. 推荐验收结论

不要输出审美分数。输出诊断：

```text
Kernel: intact / drifted
Grammar: intact / minor drift / major drift
Component identity: intact / drifted
Creative headroom: healthy / constrained / uncontrolled
```

并指出是该收紧哪条规则，还是该放松哪个 local/exemplar。

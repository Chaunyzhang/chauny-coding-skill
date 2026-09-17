# Evidence、测量与归一化

目标：把视觉输入转成可靠参数，同时避免把截图误差、缩放误差和模型猜测固化成设计事实。

## 1. Source Registry

每个输入分配 source id，例如 `img-01`、`img-02`、`text-01`。记录 Relevant 元数据：

| Field | Meaning |
|---|---|
| source_id | 证据引用 id |
| type | image / screenshot / text / video / existing-spec |
| locator | Relevant 区域/crop/组件位置；必要时用 source-pixel bbox |
| source_size | 图片原始像素尺寸 |
| viewport | 已知时记录真实 viewport |
| scale_anchor | 已知设备尺寸、浏览器 zoom、组件已知高度等 |
| theme | light / dark / unknown |
| crop | full / partial / unknown |
| notes | 压缩、缩放、模糊、遮挡等 |

没有 scale anchor 时，不把截图像素直接写成实现 px。

## 2. 四类事实

- **Observed**：直接可见、可量或明确文字约束。
- **Resolved**：由多个 Observed 通过聚类、比例、重复关系归一得到。
- **Generated**：证据不足，但为了某次可执行设计需要模型补全。必须标明 `stability_scope`，不默认长期锁定。
- **Unknown**：当前不可可靠决定。

Generated 必须显式标注，不能伪装成“从图里看出来”。

## 3. Raw Measurement 与 Canonical Value 分离

每个关键数值至少区分：

```text
raw:        img-01 = 23px, img-02 = 24px, img-03 = 25px
relation:   section gap / repeated 9 times
canonical:  space.section = 24
status:     Resolved
confidence: high
```

Raw measurement 是证据；canonical value 才是设计语言。

## 4. 测量优先级

优先测稳定的重复关系：
1. 大容器边界、column width、gutter。
2. 同类组件尺寸、padding、gap。
3. baseline / alignment / repeated geometry。
4. flat color interior。
5. border / radius / icon bounding box。
6. shadow / blur / anti-aliased typography 等低确定性参数。

## 5. 颜色测量

- 从平坦区域内部取样，避开抗锯齿边缘、阴影、透明叠加边缘。
- 同一 role 多点采样，记录候选范围。
- 半透明 surface 应尽量区分前景 rgba 与底色；无法解混时记录 composite color + Unknown alpha。
- gradient 必须记录方向、stop 位置、颜色/alpha；无法可靠恢复时写 approximate range。

## 6. Typography 测量

截图中的 glyph height 不等于 CSS/font point size。优先依据：
- 已知 platform/font metrics。
- 多个 text role 的相对比例。
- line box / baseline distance。
- 重复组件的行高与垂直居中关系。

需要记录：family、fallback、size、line-height、weight、tracking；无法识别 font family 时写视觉特征 + Unknown family，不要随意指定品牌字体。

## 7. Geometry 与 Raster Error

圆角、border、shadow、blur 会受缩放和抗锯齿影响。不要因为边缘测得 `11/12/13` 就创建三个 radius。

归一时同时看：
- 是否同一语义 role。
- 是否跨多个实例重复。
- 差异是否能被缩放/抗锯齿解释。
- 是否存在可见且稳定的角色差异。

## 8. Token Clustering

近似值只有在“语义关系也相同”时才聚类。不能因为两个值接近就强行合并。

推荐记录：

| raw values | semantic relation | candidate | decision | confidence |
|---|---|---|---|---|
| 7/8/9 | list row internal gap | 8 | merge | high |
| 12/16 | button vs card radius | 12,16 | keep separate | high |

## 9. Confidence

建议使用 `high / medium / low`：
- high：明确文字值、多个重复实例、跨图一致。
- medium：单图多次重复或可可靠比例推导。
- low：单点、模糊、缩放未知、受抗锯齿/透明叠加影响。

confidence 只描述“我们对事实有多确定”，不能单独决定未来设计要被约束多强。低 confidence 且不阻塞复刻时可保留 range/Unknown；high confidence 的局部事实也可能仍是 soft/local。

## 10. Conflict Resolution

证据冲突时，不做平均掩盖：
- 先判断是否不同 viewport / state / component role。
- 再判断是否 source 被缩放。
- 若确实属于同一 role，使用多数重复关系或用户明确要求形成 Resolved。
- 仍无法解释则记录 conflict，不随意取中间值。

## 11. Measurement Uncertainty 与 Design Variation 必须分开

每个关键数值需要区分两类范围：

```text
measurement_uncertainty = 因截图缩放、抗锯齿、模糊、透明合成等造成的“我们量不准”
allowed_variation       = 原设计系统有意允许的变化
```

例：三张图测得同一固定 gap 为 23/24/25 source-px，在校准后可得到 `canonical=24`、`measurement_uncertainty=±1 source-px`、`behavior=fixed`。不能因此写成 `range=23–25`。

只有证据显示不同实例有系统性、语义一致的变化时，才写 `behavior=range/responsive/contextual`。

## 12. Support / Prevalence

confidence 之外，还要记录支持度：
- `source_count`：多少独立 source 支持。
- `instance_count`：多少重复实例支持。
- `cross_source`：是否跨 source 成立。

单个 hero 的特殊 radius 即使测量很准，也不等于全局 `radius.surface`。它可以是 high-confidence Observed，但 scope 仍然是 local exception。

## 13. Coordinate / Raster / Snapping Evidence

高精度场景额外观察：
- 1px stroke 是否落在整数或半像素位置。
- 重复组件尺寸是否偏好偶数/整数单位。
- 图标 painted bounds 与 nominal box 是否存在固定偏移。
- 同一组件的视觉中心是否通过非对称 padding / offset 修正。

这些属于视觉事实，不应因为“理论几何应该居中”而被抹掉。

## 14. Exception Candidate

观察到局部异常时先标记为 `exception-candidate`，不要立刻创建新 global token。

只有当后续证据表明它：
- 在多个独立 source 重复；
- 与明确 semantic role 对应；
- 无法由已有 context/variant 解释；

才提升为新的 canonical role/rule。

## 15. Source Authority / Scope

多参考输入时，不默认所有 source 对所有视觉域拥有同等权威。可标记：
- primary style reference。
- secondary supporting reference。
- component-only reference。
- theme/context-only reference。
- legacy/possibly-outdated reference（只有用户或证据明确时）。

冲突解析必须先检查 scope，再比较 confidence。一个只用于 icon 参考的 source 不应覆盖全局 layout。

## 16. Explicit Override Ledger

用户明确覆盖图片或既有 Spec 时，单独记录 override：target、previous evidence、new requirement、scope、canonical result。

模型根据不充分证据自行补值不是 override，而是 Generated；二者不能混用。


## 17. Evidence Certainty 与 Generation Authority 分离

每个重要事实要经过两次判断：

```text
第一次：这个事实是真的吗？      -> provenance / confidence / support
第二次：未来设计必须守多死？    -> constraint / transfer scope / stability scope
```

不要建立错误映射：

```text
high confidence -> hard constraint   # 错
Observed        -> global rule       # 错
exact numeric   -> exact reuse       # 错
```

例：唯一 hero 的高度可以测得非常精确，但仍是 `transfer_scope=local`、`constraint_strength=open`；若它被记录成 layout recipe，则 `reuse_policy=exemplar`。

## 18. Constraint Metadata

关键 canonical fact/rule 推荐补充：

| Field | Values | Meaning |
|---|---|---|
| `constraint_strength` | hard / soft / open | 未来生成时约束强度 |
| `transfer_scope` | global / domain / component / local | 可以迁移到哪里 |
| `stability_scope` | style / component / session / instance | Generated/Resolved 选择应稳定多久 |

### Hard 的提升条件

一个事实要成为 global hard rule，通常至少满足其一：
- 用户明确要求不得改变。
- 多个独立 source / component family 重复出现，且明显构成视觉身份。
- 违反后会破坏 Style Fingerprint 中的 signature law。
- 它是 canonical component 内部不可替换的 contract。

仅仅“测得很准”不够。

## 19. Minimum Necessary Stabilization

Generated 值优先稳定到最低必要层级：

```text
关系足够 -> 锁关系
范围足够 -> 锁范围
component 内稳定足够 -> 锁 component
当前一批页面一致足够 -> 锁 session
只有确实构成身份 -> 锁 style
```

不要为了减少随机性，把一次生成的 exact number 自动升级成长期 canonical style token。

## 20. Promotion / Demotion

候选规则只有在新证据支持时才升级：

```text
local/instance
-> component/session
-> domain/style-soft
-> global/kernel（仅当确实构成视觉身份）
```

反过来，如果新证据表明某规则只属于特殊页面，应降级 scope，而不是强迫新页面迁就旧规则。

每次 promotion/demotion 都应进入 Spec Delta。

# 04 — DESIGN-LANGUAGE-SPEC

这份文档是唯一权威。它不是 PRD，也不是实现教程。

目标：另一个模型不看原参考，也能在 Reconstruction Mode 重建参考，在 Extension Mode 继续设计同一种视觉语言。

## 0. 文档顺序

必须“前轻后重”：先让消费者知道该守什么，再给细节。

推荐结构：

```text
0. Spec Identity
1. Style Kernel
2. Style Grammar
3. Creative Field
4. Canonical Components
5. Visual System
6. Evidence / Calibration
7. Exceptions / Unknowns
8. Validation Contract
9. Machine-readable Manifest
10. Spec Delta
```

## 1. Spec Identity

至少：

- `spec_id`
- version / status
- source ids
- intended reuse scope
- excluded scope
- default context
- explicit user overrides
- supported consumer mode: reconstruction / extension / both

## 2. Style Kernel

只放 5–12 条 signature laws。

每条建议：

```yaml
id: kernel.rendering-domain
rule: decorative assets use pixel rendering; functional UI remains smooth vector
constraint_strength: hard
transfer_scope: global
stability_scope: style
refs: [render.pixel, render.vector]
evidence: [ev-12, ev-24]
```

禁止只写“高级 / 温暖 / 克制”。Kernel 必须能下钻到可执行事实。

## 3. Style Grammar

按主题组织关系和范围：

- layout/rhythm
- typography hierarchy
- surface/material
- color emphasis
- geometry/shape
- icon/rendering
- composition tendencies
- context mappings

优先写 relationship/range/formula。

例：

```text
space.inline < space.group < space.section
radius.outer > radius.nested > radius.tag
selected navigation increases fill + weight, not size
```

## 4. Creative Field

明确列出未被规定的设计空间：

```text
- New page composition: open among list/grid/split/hero as task requires.
- New metric visualization: open; must reuse type/color/surface grammar.
- Decorative scene content: open; pixel rendering regime remains hard.
```

Creative Field 是正式输出，不是尾部一句“可自由发挥”。

## 5. Canonical Components

每个稳定组件：

```yaml
component_id: SectionCard
reuse_policy: adapt
anatomy: [...]
slots: {...}
semantic_mapping: {...}
geometry: {...}
adjacency: [...]
variants: [...]
constraint_scope: component
```

同一 Component ID 不允许存在第二套视觉 contract。

新组件可以是 `candidate/local`。

## 6. 最小 Fact Schema

不是每个数值都必须完整填；关键事实需要时使用：

```yaml
id: radius.surface.outer
kind: semantic
value: 26
unit: source-unit
provenance: Resolved
confidence: high
measurement_uncertainty: ±2 source-unit
constraint_strength: soft
transfer_scope: domain
stability_scope: style
behavior: range
allowed_variation: 24-30
depends_on: []
evidence: [ev-16]
```

必要字段优先：`id/value or rule/provenance/confidence/constraint_strength/transfer_scope/stability_scope/evidence`。

不要让元数据本身超过视觉事实。

## 7. Visual System

按输入 Relevant 情况覆盖：

### Layout / Composition
container、gutter、grid、alignment、rhythm、density、nesting、adjacency、overflow、z-order。

### Typography
family/fallback、size、line-height、weight、tracking、color、wrap/clamp、spatial metrics、role relationships。

### Color / Surface
primitive + semantic、tone hierarchy、alpha、gradient、compositing。

### Spacing
scale（若存在）、semantic roles、relationship laws。

### Geometry
size/aspect、radius、shape family、border placement、optical micro-geometry。

### Effects
border、shadow stack、blur/filter/material、elevation relations。

### Iconography
family、stroke/fill、sizes、optical box、alignment、state treatment。

### Rendering Regime
pixel/vector/raster/3D/photo/hand-drawn 的 domain mapping 与 cross-domain rules。

### Imagery / Illustration
crop/focal、palette、perspective、lighting、motif、texture、art direction。

### Conditional Domains
responsive、motion、data-viz、theme 只有证据存在时填写；否则 Unknown/omit。

## 8. Relationship & Dependency

能写公式时不要跨组件重复硬编码：

```text
pill.radius = control.height / 2
card.header.inset_x = card.content.inset
icon.gap = space.inline
```

Derived values 引用父 token/rule。

## 9. Context Mapping

同一 semantic role 的变化显式写 mapping：

```text
base / inverse
elevated / overlay
compact / regular
selected / disabled
light / dark
```

不要制造含义不清的近义 token。

## 10. Evidence / Calibration

把详细证据放后面，避免消费者一开始被测量表淹没。

建议：

- Source Registry
- Calibration Anchors
- Evidence Ledger
- Coverage Matrix
- Override Ledger

Raw measurements 不直接混进 canonical registry。

## 11. Exceptions / Unknowns

### Exception Registry

记录局部偏离：scope、deviates from、local rule、evidence、promotion condition。

### Unknowns / Conflicts

记录：unknown value、source conflict、scale ambiguity、compositing ambiguity、candidate token，以及什么证据能解决。

## 12. Validation Contract

### Reconstruction
must-match anchors + tolerance。Tolerance 必须来自 evidence quality/measurement uncertainty/explicit variation。

### Extension
列出：

- identity anchors（必须保持）
- grammar checks（应保持）
- creative headroom（应允许不同）
- canonical component reuse checks

## 13. Machine-readable Manifest

正文和 manifest 同源；manifest 是镜像，不是第二份 truth。

推荐使用 JSON，方便标准工具读取：

```json
{
  "meta": {
    "spec_id": "example",
    "version": 2,
    "mode": ["reconstruction", "extension"]
  },
  "kernel": [],
  "grammar": [],
  "creative_field": [],
  "facts": {},
  "components": {},
  "exceptions": {},
  "unknowns": [],
  "validation": {}
}
```

在 Markdown 中用以下 markers 包围：

```text
<!-- MANIFEST_START -->
```json
{ ... }
```
<!-- MANIFEST_END -->
```

`tools/spec_lint.py` 和 `tools/spec_export.py` 读取这个区间。

## 14. Token export

可导出的 primitive/semantic token 在 manifest 的 `facts` 中增加：

```json
{
  "kind": "token",
  "token_type": "color",
  "value": "#12383B"
}
```

`spec_export.py` 会生成简化 DTCG 风格 `design-tokens.json`：

```json
{
  "color.text.primary": {
    "$type": "color",
    "$value": "#12383B"
  }
}
```

组件结构和页面 composition 不应硬塞进 token JSON。

## 15. Spec Delta

locked/style-level 事实改变时记录：previous → new → evidence/override → downstream impact。

变化不是问题；无证据静默漂移才是问题。

## 16. 最终判断

好 Spec 的特征：

- 看得很细，但 hard 很少。
- Kernel 足够短，一眼能知道“不能破坏什么”。
- Grammar 能指导新设计，却不规定新页面具体长相。
- Creative Field 明确告诉强模型“哪里可以想”。
- 同一个组件不会漂。
- 新页面不需要重新猜风格。

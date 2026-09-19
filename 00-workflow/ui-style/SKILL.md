---
name: ui-style
display_name: UI Style
version: 2.0
description: 从图片、截图、文字或混合参考中提取可持续复用的 UI 设计语言。高精度记录视觉事实，只强约束真正构成身份的部分，让后续模型既不跑风格，也不被模板锁死。
---

# UI Style

## 目标

只做一件事：

`参考 → 视觉证据 → 设计 DNA → 松紧分级 → DESIGN-LANGUAGE-SPEC`

最终不是“把图写成文字”，也不是“规定未来每个页面长什么样”。目标是让另一个模型不看原参考，也能继续设计明显属于同一个产品的新页面。

成功标准：

1. **看得准**：重要参数、关系、组件和渲染语言可追溯到证据。
2. **守得住**：真正构成视觉身份的底线不会漂。
3. **放得开**：一次性布局、偶然数值和未规定区域不会被误锁成模板。
4. **延续得了**：新 IA、新组件仍属于同一产品，但不只是参考页换文案。
5. **接得上工程**：组件身份和复用意图明确，下游可做共享实现。

## 核心原则

**高精度记录，选择性约束。**

必须分开：

```text
Evidence certainty   = 我们有多确定这个事实
Generation authority = 它对未来设计应该管多严
```

测得很准，不等于以后都必须照抄。

## 三层设计 DNA

### 1. Style Kernel — 底线

只放真正决定“还是不是这个产品”的少量规则，通常 **5–12 条**。

例如：核心 surface/color hierarchy、字体强调关系、标志性 shape/material、icon/rendering character、品牌级视觉规律。

默认：`hard`。

### 2. Style Grammar — 语法

规定关系、范围、上下文和组合方式，而不是把所有东西锁成单点。

例如：`inline < group < section`、`outer radius > nested radius > tag radius`、某类 surface 在一个范围内变化、新组件优先消费既有 semantic roles。

默认：`soft`。

### 3. Creative Field — 发挥区

参考没有规定、也不构成身份的地方，明确留给模型。

例如：新页面用 hero/grid/list/split 哪种构图、新组件如何组织内容、局部装饰和没有证据锁定的巧思。

默认：`open`。

## 最小控制字段

关键规则只需要三种控制信息：

- `constraint_strength`: `hard / soft / open`
- `transfer_scope`: `global / domain / component / local`
- `stability_scope`: `style / component / session / instance`

不要为了“完整”给每条事实塞满元数据。

## 事实来源

每个关键事实属于：

- **Observed**：直接可见、可量或用户明确写出。
- **Resolved**：根据重复证据、关系或聚类归一得到。
- **Generated**：为了当前设计必须补全；只稳定到最低必要层级。
- **Unknown**：证据不足，不猜。

Generated 的原则：**能锁关系就不锁数字，能锁范围就不锁单点，能只锁 session/component 就不升级成 style。**

## 工作流

1. **识别输入和目标**：图片 / 多图 / 文字 / 混合；是复刻参考，还是延续风格。
2. **收证据**：记录 source、尺寸、可见结构、重复关系和不确定性。
3. **提取设计语言**：primitive → semantic role → relationship → component grammar。
4. **找 Style Kernel**：问“其他东西都变普通后，剩下哪些视觉决定仍能认出它？”
5. **写 Style Grammar**：优先写关系、范围、上下文和组合规则。
6. **声明 Creative Field**：明确哪些决定不要替未来模型做掉。
7. **整理组件**：已有 canonical component 保持身份；新组件允许产生，但先 local/candidate。
8. **输出唯一 Spec**：正文 + 同源 machine-readable manifest，不维护第二套 truth。
9. **验证**：复刻任务查 fidelity；延续任务做 novel-page extension test。

## 两种消费模式

### Reconstruction Mode

用于重建参考本身。source-specific bbox、must-match anchors、exact component contract 和 reconstruction tolerance 可以生效。

### Extension Mode

用于设计参考里没有的新页面/组件。

- Kernel 必须守。
- Grammar 应守，但允许上下文适配。
- source-specific bbox、一次性布局、exemplar composition 不自动继承。
- Creative Field 交给模型。
- 没有合适组件时允许设计新组件，不得因为 Spec 没写过就禁止创新。

**不要用 Reconstruction Mode 的精确坐标限制 Extension Mode。**

## Component / Recipe 复用语义

每个稳定组件或构图 recipe 标一个：

- `exact`：同一 canonical component/pattern，应保持 contract。
- `adapt`：保留视觉语法和关键关系，可按内容适配。
- `exemplar`：只是一个合法案例，不是未来页面模板。

已有组件优先复用；新组件第一次出现默认 local/candidate，重复证明稳定后再晋升 shared。

## 输出结构

最终只交付一份 `DESIGN-LANGUAGE-SPEC.md`，开头必须先给：

1. `Style Kernel`
2. `Style Grammar`
3. `Creative Field`
4. `Canonical Components`

详细 evidence、tokens、visual domains、exceptions、unknowns 和 manifest 放后面。

Schema 见 `references/04-design-language-spec.md`。

## Progressive Disclosure

主 Skill 不承担所有细节。按任务需要读取：

- 测量、截图缩放、证据、不确定性 → `references/01-evidence-measurement.md`
- 颜色/字体/shape/icon/rendering/imagery 等视觉域 → `references/02-style-extraction.md`
- hard/soft/open、scope、stability 怎么判 → `references/03-constraint-calibration.md`
- 最终 Spec 格式 → `references/04-design-language-spec.md`
- 新页面延续测试 → `references/05-extension-validation.md`
- 组件身份与工程交接 → `references/06-implementation-handoff.md`

不要为了回答一个简单任务把所有 reference 都加载一遍。

## 完成 Gate

完成前检查：

- Kernel 是否只有少量真正 signature rules；若几十条 hard/global，说明过度约束。
- high confidence 是否被错误等同于 hard/global。
- Grammar 是否优先表达关系/范围，而不是偶然 exact number。
- Creative Field 是否真实存在，而不是“其余自由发挥”一句空话。
- 同一 Component ID 是否只有一套视觉 contract。
- local/exemplar 是否被错误提升成全局规则。
- Unknown 是否被诚实保留。
- Extension Mode 下，新页面能否明显不同但仍属于同一产品。

可运行 `tools/spec_lint.py DESIGN-LANGUAGE-SPEC.md` 做结构和约束过载检查。

## 明确不做

不负责产品 PRD、业务 IA、backend/API、状态所有权、React/SwiftUI/CSS 教程、repo 架构或“怎样更高级/更好看”的审美优化。

但必须把 component identity、reuse policy、semantic contract 写清，供下游实现复用。

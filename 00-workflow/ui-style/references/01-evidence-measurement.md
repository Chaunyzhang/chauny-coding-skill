# 01 — Evidence & Measurement

目标：把参考变成可靠证据，不把截图噪声、缩放和模型猜测混进设计语言。

## 1. Source Registry

每个 source 至少记录：

- `source_id`
- type：image / screenshot / text / mixed
- source size
- crop / compression / blur / occlusion
- known viewport / DPR / renderer / platform（只有已知才写）
- authority：primary / secondary / component-only / theme-only
- context：light/dark、compact/regular 等已知环境

多来源不是天然同权。component-only reference 不应覆盖全局 layout。

## 2. 原始测量与 canonical value 分开

必须保留链路：

```text
raw measurement → normalized relation → canonical design fact
```

截图中量到 24 source-px，不等于 CSS 24px。

没有可靠 scale anchor 时：

- 保留 source-pixel / ratio。
- 优先提取相对关系。
- implementation unit 保持 Unknown 或 Resolved/Generated，不伪装 Observed。

## 3. Calibration Anchors

可用 anchor：

- 已知 viewport/logical size
- 明确标注的组件尺寸
- 已知系统 UI 尺寸
- 原设计文件中的数值
- 多图中稳定的几何关系

每个 anchor 记录 source measurement、known value、derived scale、confidence。

## 4. Evidence Ledger

关键观察至少记录：

```text
Evidence ID
Source
Locator / bbox / region
Raw observation
Raw value + unit
Quality
Confidence
Resolves to
```

Locator 尽量精确到区域或组件，而不是只写“来自 img-03”。

## 5. Measurement uncertainty ≠ allowed variation

必须分开：

```text
measurement_uncertainty = 我们量得有多准
allowed_variation       = 原设计语言允许变化多少
```

例：固定 gap 因 raster 得到 23/24/25。

正确：

```text
canonical = 24
behavior = fixed
measurement_uncertainty = ±1 source-px
```

错误：`allowed range = 23–25`。

## 6. Canonicalization

近似数值先判断语义，再聚类。

- 7/8/9 可能是同一 gap 的测量误差。
- button radius=12、card radius=16 若长期角色不同，就不能合成 14。
- 能用公式解释时优先公式，例如 `pill radius = control height / 2`。

不要因为已有 8/12/16/24，就机械把所有新值吸进去；先看角色和证据。

## 7. Color measurement

优先：

- 采平坦内部区域，不采抗锯齿边缘。
- 区分 observed composite color 与原始 alpha/color。
- 半透明 surface 若 underlay 未知，不反推出“确定”的 foreground RGBA。
- JPEG、色彩管理、阴影会扩大误差。

无法确定 exact RGB 时，可以稳定保留 luminance/chroma/alpha hierarchy。

## 8. Typography measurement

不要只记字号。能观察时记录：

- rendered bbox / line box
- line-height relationship
- weight
- tracking
- wrap / clamp
- baseline alignment
- glyph run width / max width

字体家族识别不可靠时，family=Unknown；空间行为仍可成为可靠证据。

## 9. Effects / compositing

shadow / glass / blur 要区分：

- fill
- border
- shadow stack
- backdrop blur
- foreground filter
- underlay dependency
- blend / opacity

若只能看到最终合成结果，准确写 Unknown，不硬拆 CSS 参数。

## 10. 静态证据边界

单张静态图不能证明：

- motion duration/easing
- hover/focus
- hidden states
- runtime sticky/fixed behavior
- exact breakpoint
- code implementation

两端 viewport 只证明变化区间时，记录 interval，不猜精确 breakpoint。

## 11. Text input evidence

用户明确数字/规则优先级最高。

形容词本身不是数值事实。将“柔和/紧凑/大圆角”拆成可观察维度，并优先生成关系/范围，而不是立刻永久锁 exact values。

## 12. Unknown 是有效输出

证据不足时写 Unknown。Unknown 比一个自信但错误的默认值更有利于长期稳定。

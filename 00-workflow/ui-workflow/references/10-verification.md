# 验证：Rendered Reality、Structure 与 Drift

验证风险，不做仪式。

## 1. Rendered Evidence

可见 UI 必须在真实运行环境验证本次 Relevant 场景：
- normal/loading/empty/error/permission/offline 等
- long text / many items / extreme values
- small viewport / text scaling / localization
- hover/pressed/focus/disabled/dragged 等 applicable states
- reduced motion / keyboard / touch

不能只看源码、单张静态图或测试通过就宣称 UI 正确。

## 2. Component State Proof

复杂交互组件需要把 applicable states 一次性渲染/固定出来；不要求每个组件固定八态。

输出：`state → applicable? → rendered evidence`。N/A 必须有理由。

## 3. Interaction Proof

拖拽、复杂 optimistic rollback、多阶段 transition、复杂 sheet/filter 等有行为风险时，做最低成本 storyboard/prototype/fixture。简单点击不强制 prototype。

## 4. Spec Conformance

检查：
- design values 是否来自 Spec/tokens
- page structure 是否按 Page Spec
- component states/interaction 是否按 contract
- Unknown 是否被实现偷偷补成事实

## 5. Formal Drift Audit

从 Spec 建 inventory：color/type/spacing/radius/shadow/icon/motion/component grammar。

扫描实现中的新增值/语言：
- 新 color / font / size / line-height
- 新 spacing / radius / shadow
- 新 icon family / control height
- 新 card treatment / motion character
- 与已有值非常接近但不同的 literal

处理：
- 有新语义 role → 先进入 Spec。
- 与已有 role 同义 → 归并。
- 无理由 → 删除/改回。

`8/12/16/24` 系统里出现 `15/23` 默认先判疑似 drift，不解释成“手调更精致”。

## 6. Structure Conformance

对照 `IMPLEMENTATION-STRUCTURE.md` 检查 shared/local、ownership、registry 与 duplication；若新增页面需要 copy-paste 旧页面，失败。

## 7. Mechanical Visual Review

复跑 `references/03-visual-design.md` 的 Visual Math + Craft Floor：hierarchy、alignment、relationship spacing、type scale、color role、radius/icon/shadow family、content stress、a11y。

## 8. Human Review Package

只把 Human 真正需要判断的东西交出去：
- 关键 rendered states/页面
- 本次确认的设计决定如何落地
- 未解决 Unknown / tradeoff

Agent 不宣布“现在已经高级/好看”；Human 拥有最终审美权。


## Visual Order / Subtraction Check

对完整新页面或重设计，最终 rendered evidence 额外检查：
- 弱化色彩后主焦点、分组、阅读顺序是否仍成立。
- 无意义框、border、shadow、随机颜色、辅助小字是否可删除。
- 表格/列表的文字、数字、状态、操作列是否共享稳定轴。
- 是否存在整屏同权、组件库拼装感或平均化视觉音量。

这些属于结构性视觉缺陷；先修，再交给 Human 做审美裁决。

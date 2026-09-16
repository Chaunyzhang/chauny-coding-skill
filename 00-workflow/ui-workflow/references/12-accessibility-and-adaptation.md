# 无障碍与适配

**何时加载**：任何真实用户界面都适用；复杂交互、表单、跨设备、国际化或系统辅助设置变化时重点展开。

**目标**：把 accessibility / adaptation 当作横切约束，不是最后补的 checklist。

## 输入与操作

按平台相关性考虑：

- touch
- pointer
- keyboard
- focus order / focus return
- drag 的替代操作
- shortcut
- screen reader / semantic role

不要让关键操作只能依赖一种高精度 gesture。

## 视觉可感知

- 状态和错误不只靠颜色。
- contrast 满足项目/平台要求。
- icon-only controls 有可访问名称。
- focus 可见。
- disabled 与 unavailable 的语义清楚。

## 内容变化

- text scaling / Dynamic Type / zoom。
- 长文本和本地化膨胀。
- RTL。
- 日期、数字、货币、复数等格式。
- reflow 后阅读和操作顺序仍正确。

## 环境与偏好

- light / dark（若产品支持）。
- increased contrast。
- reduced motion。
- orientation / window size / safe area。

Reduced Motion 不只是“关动画”，而是保留必要状态反馈，减少不必要位移、缩放和眩晕型运动。

## 状态反馈

异步状态、错误、成功、进度等重要变化，应有适合辅助技术理解的语义表达；不要只让视觉用户看到 toast 或颜色变化。

## 停止条件

当本次界面的核心任务可以在适用输入方式和系统设置下完成，内容变化不会破坏结构，关键状态可被感知和理解时停止。

# 设计系统与组件

## 1. 先意义，后 token

优先 semantic roles：
`text.primary / text.secondary / surface.base / surface.raised / action.primary / border.subtle / status.error`

primitive 值是实现细节；不要从 `blue-500 / gray-400` 直接驱动组件语义。

## 2. 层级

`Foundations/Tokens → Primitives → Components → Patterns → Surface/Page`

Atomic/层级模型是组织方式，不是固定设计步骤。

## 3. Component Contract

重要组件至少定义：
- purpose / anatomy / slots
- content bounds
- properties / variants
- applicable states
- events / feedback
- layout/adaptation
- accessibility semantics
- motion（适用时）
- data/action mapping

Variant = “哪一种语义版本”；State = “现在怎样”；Owner = “谁改变它”。三者不得混合。

## 4. 什么时候上移 shared

满足任一：
- 2+ 真实场景复用。
- 独立 meaningful state / interaction。
- 稳定视觉/行为 contract 被多个 Surface 依赖。
- 属于 token/icon/navigation/formatter 等共享基础。
- 复制会产生第二真相源。

只出现一次、无独立状态、抽取只是在给 markup 改名字时保持 local。

## 5. Pattern

Search+Filter、Empty State、Confirmation、Bulk Action 等是 Pattern，不必都包装成单个 Component。

## 6. Token discipline

- 新页面优先消费已有 token。
- 新值若与已有值近似，默认先归并。
- 需要真正新 role 时，先更新 Spec/manifest，再实现。
- 页面不得私有发明新的同义 color/type/spacing/radius/shadow。

## 停止条件
新页面和新组件可以从既有规则推导，不需要复制旧页面或重新解释风格。

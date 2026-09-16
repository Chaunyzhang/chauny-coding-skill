# UI 实现：平台无关核心

**何时加载**：任务包含真实代码实现、结构重构、组件落地、状态接线或迁移。

**目标**：在现有项目约束下，把 UI 定义实现成真实运行界面；核心规则不绑定 React、SwiftUI 或其他框架。

## 实现结构先于非平凡代码

只要任务新增页面、跨页面复用、共享组件/资产、state owner、navigation 或 data/mutation path，就必须先加载 `15-implementation-structure.md`，创建或更新 `IMPLEMENTATION-STRUCTURE.md`。

不得先复制页面把功能做出来，再等用户提醒后重构结构。

## 先读 repo 现实

实现前确认相关：

- app / feature 边界
- routes / navigation
- API / data access layer
- state/store/cache
- design tokens / shared UI
- feature components
- tests / previews / stories
- build / lint / typecheck / test 命令

已有结构优先复用；只有真实问题才调整 architecture。

## 依赖方向

保持单向责任：

```text
Platform/App shell
→ Feature / Surface composition
→ Feature UI / view model projection
→ Shared UI / Design System
→ platform primitives
```

数据/业务层的实际结构服从 repo 现状，但 UI 不应绕过已有权威 data/API layer 自创第二条路径。

## 状态实现

- Durable business truth 由真实 owner 拥有。
- UI 可以持有 presentation-local state。
- Derived state 应从 source of truth 推导，不重复存储。
- Leaf UI 默认通过 event/intent 向上表达，不直接 mutate durable shared truth。

## Page / Feature / Base UI 的职责

### Page / Surface
负责 composition、routing context、主要数据投影和 feature 协调；不要成为所有业务逻辑垃圾桶。

### Feature component
可以理解一个明确 workflow 的语义、状态和交互；不要跨多个无关业务域。

### Base / shared UI
只知道通用 UI 语义，不携带产品专属业务判断。

## 数据 Surface 最低实现覆盖

按任务相关性考虑：

- loading
- empty
- populated
- error

存在用户动作时再按实际需要补：

- permission / unavailable
- pending / disabled
- optimistic success / rollback
- retry / cancel
- stale / offline

不要为了理论完整增加不存在的状态。

## 迁移与旧路径

当新 contract / state source / component path 成为权威后：

- 删除旧推断。
- 删除重复 owner。
- 删除旧正常入口。
- 不把旧实现保留成“万一”的隐形 fallback，除非明确有兼容窗口和退出条件。

## 工程质量

按 repo 提供的能力执行最小相称验证：

- targeted behavior tests
- negative tests
- source gates / grep checks（适用于禁止旧路径）
- build / typecheck / lint
- rendered verification

测试行为和 contract，不为测试覆盖率数字编造无价值测试。

## 平台适配

通用规则到此为止。遇到 SwiftUI 时加载 `09-platform-swiftui.md`；其他平台优先读取项目惯例和该平台官方约束，不把其他栈的习惯迁过去。

## 停止条件

当实现遵守现有依赖方向、状态 owner 清楚、旧路径不再干扰、目标 UI 可运行，并且非平凡任务的 `IMPLEMENTATION-STRUCTURE.md` 已按真实 repo 更新、通过 Post-Implementation Structure Audit，再进入 rendered verification。

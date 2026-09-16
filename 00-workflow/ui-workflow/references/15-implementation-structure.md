# 实现结构自查：代码前后都必须画出来

**何时加载**：任务包含真实代码实现，并且满足任一条件：新增页面/Surface；涉及 2 个以上页面或重复 UI；新增共享组件/资产；改变 state owner、navigation、data/mutation path；设计系统继续扩展；已有复制粘贴迹象。

**轻量例外**：只改一个已存在组件的单个视觉属性、且不改变结构/owner/复用边界时，不要求创建完整文档，但仍必须明确写出 `Structure impact: none`，并验证没有引入新的重复实现。

**目标**：在写非平凡 UI 代码前，把“哪些是共享事实、哪些是页面局部、谁拥有状态、数据和动作怎么流动”显式画成 Markdown；实现后再按真实 repo 自查一遍。结构没有画清楚，不进入实现。

---

## 实现架构的目标

这一步不是“多抽组件”，而是把 UI Spec 翻译成稳定的代码 ownership：

- UI/Design truth 有唯一来源。
- durable state / data / mutation / navigation 各有唯一 owner。
- repeated semantic UI 有稳定 contract。
- page-local 内容保持 local，不为形式组件化。
- 下一个同类页面主要新增“特有结构/配置/数据”，不是复制旧页面主体。

## 1. 强制产物：`IMPLEMENTATION-STRUCTURE.md`

非平凡实现必须创建或更新此文件。它不是软件架构论文，只记录当前 UI 实现真正需要的边界。

最少包含下面 6 块。

### A. Repository / Feature Tree

用 Markdown code block 画出计划结构，只画与当前任务相关的目录/文件/模块：

```text
App
├── Shared
│   ├── DesignTokens
│   ├── Icons
│   └── NavigationShell
│
├── Features
│   ├── Todo
│   │   ├── TodoScreen
│   │   ├── TodoState / ViewModel
│   │   └── Components
│   │       ├── TaskRow
│   │       └── QuickAdd
│   └── Chat
│       ├── ChatScreen
│       └── Components
│           └── Bubble
│
└── Data / Services
    └── ...
```

不要为了好看虚构目录；必须映射到目标 repo 的真实组织方式。

### B. Shared vs Local

明确哪些东西只有一个权威来源：

| Object | Shared / Local | Owner / Source | Why |
|---|---|---|---|
| TabBar | Shared | Navigation shell | 多页面复用 |
| Chevron icon | Shared asset | Icon registry | 同一图形不得重复定义 |
| TaskRow | Shared within Todo feature | Todo feature | 重复结构 + 独立状态 |
| HomeHero | Page-local | Home page | 单用、无独立状态 |

原则：**抽象不是目标，单一真相源才是目标。**

### C. State / Data / Mutation Ownership

至少画出：

```text
TaskRepository
      ↓ data
TodoState / ViewModel
      ↓ projection
TodoScreen
      ↓ props / bindings
TaskRow
      ↑ user intent
TodoState / ViewModel
      ↓ mutation
TaskRepository
```

并标明：
- durable state owner
- presentation-local state
- derived state
- mutation boundary
- error → UI 的转换位置

叶子组件不得因为“方便”直接改 durable shared truth。

### D. Navigation Ownership

画出 route / selected tab / modal/sheet owner：

```text
AppNavigation
├── activeTab
├── route
└── presentedSheet

TabBar -> emits selection intent -> AppNavigation
Page   -> emits navigation intent -> AppNavigation
```

不要让每个页面各自维护一份 active tab / route truth。

### E. Reuse / Rendering Plan

对于重复内容明确选择：

```text
Data collection
→ renderer / repeated component
→ stable component contract
```

例如：

```text
mockTasks[]
→ createTaskRow(task)
→ TaskRow visual/state contract
```

禁止复制多份 markup/view 再手改文案。

### F. Single-Source Registry

检查这些是否有唯一来源：

- design tokens
- icons / imagery assets
- navigation shell
- repeated component implementation
- repeated interaction/state transition
- formatters
- fixtures/mock data
- domain labels/options（若属于产品事实）

---

## 2. 抽取规则

当任一条件成立时，默认应形成共享实现或明确 registry：

1. 同一语义 UI 出现在 2 个及以上位置。
2. 它有独立且有意义的 state / interaction contract。
3. 它有稳定视觉/行为规则，被多个 Surface 消费。
4. 它属于系统级单一来源：token、icon、navigation shell、formatter、renderer、shared fixture。
5. 复制它会产生两个需要同步维护的真相源。

只有当以下条件全部成立时，优先保持 page-local：

1. 只出现一次。
2. 没有独立 durable state。
3. 没有真实复用边界。
4. 抽取只会给 markup 换一个名字，不减少重复、ownership 歧义或未来修改成本。

---

## 3. 写代码前：Pre-Implementation Structure Check

开始非平凡实现前必须自答：

- 哪些 UI/asset/token 会跨页面重复？
- 哪些重复结构应该数据驱动？
- 哪些东西修改一次必须全局生效？
- state owner 是否唯一？
- navigation owner 是否唯一？
- durable mutation 从哪里发生？
- 哪些结构明确保持 local，为什么？
- 如果明天新增第三个同类页面，哪些东西可以直接复用？

如果回答仍是“先复制一份现有页面再改”，不得开始实现。

---

## 4. 写代码后：Post-Implementation Structure Audit

实现完成后，**不要只看行为是否通过**。按真实 repo 重新画/更新 `IMPLEMENTATION-STRUCTURE.md`，并扫描：

- duplicated navigation
- duplicated icons/assets/SVG
- duplicated visual constants
- duplicated markup/view structure
- duplicated component logic
- duplicated state transition
- duplicated mock/content data
- duplicated formatter
- duplicated layout rule
- duplicated mutation path

### 最关键的自测

回答：

> “现在再新增一个同类页面，我需要复制什么？”

好的答案：
- 只新增页面特有结构、配置和数据；
- token、icon、navigation、共享组件、重复 renderer、状态规则直接复用。

失败答案：
- “复制上一页，再改几个地方。”

出现失败答案时，Structure Gate 不通过；先重构，再交付。

---

## 5. 结构变更必须与 Spec 一致

`UI-DESIGN-SPEC.md` 决定视觉/交互规则；`IMPLEMENTATION-STRUCTURE.md` 决定这些规则在代码中的 ownership 和单一来源。

两者职责不同：

```text
UI-DESIGN-SPEC.md
→ What the UI must be

IMPLEMENTATION-STRUCTURE.md
→ Where each UI/state/data truth lives in code
```

实现不能通过复制代码制造第二套“差不多”的设计系统。

---

## 禁止模式

1. **Copy-Paste Expansion**：新页面主要靠复制旧页面后修改。
2. **Duplicate Asset Source**：同一个 icon/SVG/asset 在多个页面各自定义。
3. **Markup as Data**：重复 collection 内容硬写在 markup/view 中。
4. **Parallel State Owners**：同一 durable truth 在多个页面/组件各存一份。
5. **Parallel Navigation Truth**：多个页面独立维护 active route/tab。
6. **Premature Componentization**：单用、无状态、无复用价值的结构被为了“组件化”而抽取。
7. **README-Only Architecture**：规则只写在说明里，但实际 repo 不符合。
8. **Post-Hoc Cleanup Only**：先复制粘贴把页面做完，再把结构问题留给用户提醒。

---

## 停止条件

只有当：
- 计划结构已在 Markdown 中画清楚；
- 实际结构与计划一致或已更新说明；
- shared/local/state/navigation/mutation ownership 清楚；
- 没有明显重复真相源；
- 新增同类页面不需要复制现有页面主体；

才通过 Structure Gate。

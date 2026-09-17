# UI 实现：平台无关核心

## 1. 先读 repo 现实

优先复用现有 architecture、tokens、components、routing、state/data layer、test conventions。不要为套 Skill 重建已成立系统。

## 2. 实现只消费批准事实

- Visual values 来自 Spec/tokens。
- Business truth 来自明确 data/state source。
- 可见行为来自 confirmed Spec。
- 新设计事实不能只存在代码。

## 3. 依赖方向

页面/feature 可以依赖 shared UI 与 domain/service abstractions；base/shared UI 不携带产品业务判断。

Leaf component 不直接修改 durable shared truth，除非它就是明确 owner；通常通过 event/action 交给 owner。

## 4. Page / Feature / Base UI

### Page / Surface
组合 content、navigation、feature state、layout；不复制 shared system。

### Feature component
封装稳定语义、状态/交互或复用 contract。

### Base/shared UI
只承载通用视觉/交互语义，不读取产品业务字段来猜 variant。

## 5. Data surface 最低覆盖

列表/数据页按 Relevant 支持：loading、empty、partial/stale、error、permission、retry、large dataset/content stress。

## 6. 迁移

新路径上线后，旧推断/旧组件/旧入口不得作为“保险 fallback”长期存活；明确删除、迁移或隔离。

## 7. 工程质量

优先单一真相源、明确 ownership、可测试 seam、可独立渲染关键状态。性能优化基于风险/证据，不做无证据 profiling。

## 8. Spec 不足时

若只是实现细节（内部数据结构、无可见影响的 refactor）可自主决定。
若会改变可见结构/状态/interaction/motion/语义，停代码回到 Alignment/Spec。

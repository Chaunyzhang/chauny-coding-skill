# IMPLEMENTATION-STRUCTURE：实现前后自查

目的：UI 设计系统在代码里也只有一个真相源，避免“第二页开始复制粘贴”。

## 1. 非平凡实现的强制产物

`IMPLEMENTATION-STRUCTURE.md` 至少画：

```text
App / Feature tree
├── Shared system
│   ├── tokens
│   ├── icons/assets
│   └── shared components
├── Feature A
│   ├── page-local structure
│   ├── state owner
│   └── renderers/components
└── Feature B
```

并明确：
- shared vs local
- state/data/mutation owner
- navigation owner
- repeated renderer/component
- token/icon/asset/formatter registry
- tests/fixtures/state proof seam

## 2. 抽取规则

Extract when ANY：
1. 同一语义 UI 出现 2+ 场景。
2. 拥有独立 meaningful state/interaction。
3. 稳定 visual/behavior contract 被多个 Surface 依赖。
4. 属于共享 asset/token/navigation/formatter/renderer。
5. 复制会制造多个 truth source。

Keep local when ALL：used once、无独立 durable state、无复用边界、抽取只增加间接层。

## 3. Pre-Implementation Check

写代码前回答：
- tokens/icon/navigation 的唯一来源在哪？
- repeated collection 是否 data-driven？
- 相同 interaction/state transition 是否只实现一次？
- mutation 权限在哪里？
- 哪些组件必须 shared，哪些故意 local？

## 4. Post-Implementation Audit

按真实 repo 重画结构，再扫描：
- duplicated navigation
- duplicated SVG/icon/assets
- duplicated visual constants
- duplicated markup/view structures
- duplicated interaction/state logic
- duplicated mock/content data
- duplicated formatter/renderers

硬问题：**“再加一个同类页面，需要复制什么？”**
如果需要复制上一页主体、同一 SVG、同一导航、同一状态逻辑，先重构再交付。

## 5. 与 Spec 的关系

结构变化若改变 Component boundary、state owner、data/mutation mapping，必须同步更新 Spec；纯文件移动/重命名且 contract 不变则不制造假设计变更。

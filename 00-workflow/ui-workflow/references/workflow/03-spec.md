# 03 UI-DESIGN-SPEC 与继承门禁

编译设计规格、审查继承资格或更新既有 Spec 前读。设计没有编译成含封闭风格文法、规范组件契约与同源 Manifest 的明确规格就不算完成；实现 Agent 只消费 Spec，不重新解释设计意图。

## 目录

- 1. Inheritance Gate（继承前硬查）
- 2. 四种规格尺度（Full / Draft Full / Page / Patch）
- 3. Full Spec 结构（前轻后重：先身份与文法，后细节与映射）
- 4. 统一 Machine-Readable Manifest（JSON 同源附录）
- 5. Page Spec 与 Patch Spec
- 6. Copyable Implementation Prompt
- 7. Spec Gate（冻结前必过 `spec-lint.py`）

## 1. Inheritance Gate（继承前硬查）

凡走“继承已有系统 / 沿用 token”路径（含改组件、新增页面、局部重设计），动手前必须同时通过三项检查：
1. **指出来源**：给出被继承的 Full Spec 文件路径及其中合法的 `<!-- MANIFEST_START -->` JSON Manifest；口头约定或零散样式文件不算。
2. **封闭风格文法检查**：被继承 Spec 必须包含完整的 **Style Kernel、边界哲学锁、四槽容器拓扑、选中态 1:1 绑定、Canonical Components（含 `reuse_policy`）与 Concrete Recipe**；只定了配色或圆角的不算合格系统。
3. **现实对账**：对现有代码运行 `scripts/drift-audit.py --manifest <Spec.md>`，确认无失控的 scale 外裸值、裸色或页面层视觉五件套漂移。

任一项不通过：路由自动升级为「已有 UI 重设计」，先补齐完整风格文法与 Full Spec，禁止在残缺地基上叠加 Patch/Page Spec。

## 2. 四种规格尺度（Full / Draft Full / Page / Patch）

- **Full Spec**：新产品、新视觉系统、多页面从零，或 Inheritance Gate 失败后的整站重塑基线。
- **Draft Full Spec**：无代码、无既有视觉资产的纯文本方案审查阶段使用——先锁死结构、交互、反馈、动效与风格封闭语法锁，把全局色板/字阶标为待单屏拍板的候选值并显式列 `Unknown`，不伪装既定品牌事实。
- **Page Spec**：继承已批准全局系统，只写该页新增或变化的 structure、focal order、states、消费的 Canonical Components 与 local 新增项。
- **Patch Spec**：局部改动，只记录 Target、Preserved、Changed、Reason、Verification；禁止为小改重写整个产品。

Page / Patch Spec 头部必须写明继承来源与检查结果（写不出或未通过则退回 Full Spec）：

```md
Inherits: <项目内已批准 Full Spec 路径>
Inheritance Gate: PASS — Style Kernel & 封闭文法锁完整；drift-audit: 0 违规
```

## 3. Full Spec 结构（前轻后重：先身份与文法，后细节与映射）

把最决定风格一致性的 `Style Kernel → Style Grammar & 6 Locks → Canonical Components → Creative Field` 放在最前面，让消费模型一眼看清硬底线与允许发挥区：

```md
# UI-DESIGN-SPEC

## 0. Evidence, Stage-Fit & Structure Blueprint
- Spec Mode: `extension`（做新页/多页产品） | `reconstruction`（像素级复刻参考） | `both`
- 定场：产品阶段 × 核心受众 × 软件姿态（主权/瞬态/后台） × 核心动作
- **信息三桶分流（Information Triage）**：Primary（首屏主路径）/ Secondary（随主对象退后）/ Deferred（按需收口去处）
- **抽象骨架与槽位预演（Structure-Before-Content）**：Region/Section 骨架树、各槽唯一职责与容量上限、空值/极值/缺配灌入形态预演（先证明骨架成立，再填内容）
- Observed / Resolved / Generated（仅 local/session） / Unknown / Human confirmed decisions

## 1. Style Kernel
- 5–12 条硬身份底线（默认 hard / global / style；每条过“去掉还像不像同一产品”测试且可下钻）
- 先点名 3 个最易滑向的 AI 默认套路及规避决策（Primary / Secondary / Avoid）

## 2. Style Grammar
- **边界哲学锁（三选一）**：`hairline-embedded` | `tonal-layered` | `bordered-card`（含阴影白名单与唯一合法例外）
- **四槽容器拓扑**：`L0_shell` / `L1_section` / `L2_item` / `L3_overlay` + Recessed 白名单 + 同级同拓扑/嵌套降级律
- **控件家族锁**：高度阶梯（sm/md/lg 同行必同高）、同语义同壳、统一 State Layer（Hover/Pressed/Disabled）
- **选中态 1:1 语义绑定（≤ 2 种配方）**：各交互语义绑定关系 + Focus Ring 唯一公式 + Forbidden 列表
- **关系与派生公式**：spacing 比例律、同心圆角、标题不对称留白、Context Mapping（light/dark、active/inactive 等）

## 3. Concrete Visual Recipe（具体数值，禁模糊形容词）
- Typography roles & 光学微排版 / Spacing scale / Control heights
- Color semantic tokens (含暗色亮阶、降饱和与对比度下限)
- Radius family (≤ 4 档常规非零非 pill + squircle 光学补偿) / Border & Shadow levels
- Material layering (导航层 vs 内容层) / Browser Surfaces / Iconography & Scrim / Motion (频率分级 + 可打断 + 主题 0ms)

## 4. Canonical Components
- **Canonical Shell & Section Patterns (`exact`)**：AppShell / PageHeader / Toolbar / SectionHeader / ListRow / EmptyContainer
- **Core Components**：逐项列 `Component ID / reuse_policy (exact|adapt|exemplar) / visual contract / states / a11y`

## 5. Creative Field
- 显式列出未锁定的开放设计空间（新页面内容构图、局部信息表达、数据视图形态等），禁止空写“自由发挥”

## 6. Layout Stability, States & Interaction Contracts
- 防挤压落位规则（条件提醒 3 选 1）、Anti-Reflow、CLS、滚动隔离
- 多维状态、三档耗时防闪、4 类空态、报错三要素、交互闭环、表单人因、四类容器分工与禁叠窗
- UI ↔ data / state / event / action / recovery mapping & 无障碍/系统偏好三降级

## 7. Implementation Structure & Primitives-First Plan
- `primitive_paths` 白名单（第 1 页前先建封闭原语）与页面层视觉五件套禁写说明

## 8. Exceptions, Unknowns & Spec Delta
- Exception Registry（ID / 范围 / 突破规则 / 理由 / 退出条件）与 Spec Delta 记录

## 9. Verification & 单屏 / 多屏门禁
- 全局换肤 1 屏真图门禁；多页项目 Multi-Screen Parity 并排对照
- `spec-lint.py` / `drift-audit.py` / `style-grammar-audit.js` / `shadow-clip-audit.js` / Three-Pass 审校

## 10. Machine-Readable Manifest & Copyable Implementation Prompt
```

## 4. 统一 Machine-Readable Manifest（JSON 同源附录）

Full Spec 内必须嵌入唯一同源 JSON Manifest（供 `spec-lint.py`、`drift-audit.py`、`style-grammar-audit.js` 直接读取，严禁另存一份易漂移的第二真相源）：

```markdown
<!-- MANIFEST_START -->
```json
{
  "meta": { "mode": "extension", "posture": "sovereign" },
  "kernel": [
    "边界哲学锁定 hairline-embedded：静态内容用 1px 低透明细线，零内容投影",
    "全站选中态仅 2 套配方并按交互语义 1:1 绑定，多栏失焦自动退为中性灰"
  ],
  "grammar": {
    "boundary_philosophy": "hairline-embedded",
    "containment_topology": {
      "L0_shell": "embedded-split",
      "L1_section": "divider-only",
      "L2_item": "flat-row",
      "L3_overlay": "elevated-popover"
    },
    "recessed_whitelist": ["search-input", "code-block", "dropzone"],
    "selection_grammar": {
      "max_distinct": 2,
      "recipes": {
        "soft-fill": "bg:surface.selected + text.primary",
        "underline": "bottom-2px accent.primary + text.primary"
      },
      "bindings": {
        "nav_item": "soft-fill",
        "list_row": "soft-fill",
        "menu_item": "soft-fill",
        "view_tabs": "underline"
      },
      "forbidden": ["left-accent-bar", "outline-box-toggle", "font-weight-jump"]
    },
    "primitive_paths": ["src/styles/tokens.css", "src/components/ui/"]
  },
  "visual": {
    "spacing": [0, 4, 8, 12, 16, 24, 32, 48],
    "radius": [0, 6, 8, 12, 999],
    "control_height": [28, 32, 40]
  },
  "budgets": {
    "max_distinct_non_pill_radius": 4,
    "max_border_styles": 2,
    "max_shadow_levels": 2,
    "max_surface_levels": 4,
    "max_font_sizes": 6,
    "max_selection_grammars": 2,
    "max_ad_hoc_exceptions": 0
  },
  "components": {
    "AppShell": { "reuse_policy": "exact", "role": "L0_shell" },
    "Surface": { "reuse_policy": "exact", "variants": ["canvas", "embedded", "raised", "overlay"] },
    "SelectableRow": { "reuse_policy": "exact", "selection_recipe": "soft-fill" },
    "PrimaryActionBar": { "reuse_policy": "adapt", "role": "toolbar" }
  },
  "creative_field": ["新页面主内容区信息组织与数据可视化形态", "局部空态说明文案与业务流步进"]
}
```
<!-- MANIFEST_END -->
```

## 5. Page Spec 与 Patch Spec

- **Page Spec**：只写全局 Spec 未覆盖的页面级决定，必须显式包含三栏：`Consumed Canonical Components (exact/adapt)`、`New Local/Candidate Components`、`Exceptions (默认 0)`，加上页面 structure tree、focal order、page-specific states 与 adaptive rules。
- **Patch Spec**：

```md
## PATCH SPEC
Inherits: <Full Spec 路径>
Target: <目标组件或元素>
Preserved: <明确保持不变的属性与语法锁>
Changed: <具体变更值>
Reason: <原因>
Verification: <验收动作>
```

## 6. Copyable Implementation Prompt

Spec 末尾附可直接交接给实现 Agent 的指令，必须写明：
- 本 Spec 与其 JSON Manifest 为唯一设计权威，禁止重新解释风格方向或突破 6 把封闭锁；
- 第 1 页动工前先在 `primitive_paths` 建完封闭视觉原语；页面层禁止手写视觉五件套（`bg / border / radius / shadow / selection`）；
- 遇未覆盖的可见决定立刻停代码回到 Human alignment 更新 Spec；
- 交付前必须附 `spec-lint.py`、`drift-audit.py`、`style-grammar-audit.js`（及适用时的 `shadow-clip-audit.js`）结果与真实渲染（多屏并排）证据。

## 7. Spec Gate（冻结前必过 `spec-lint.py`）

冻结 Full Spec 前必须运行 `python3 -I <skill>/scripts/spec-lint.py <UI-DESIGN-SPEC.md>` 并确认 0 ERROR；出现任一以下条件即打回，禁止进入代码实现：
- 缺少信息三桶分流或抽象结构骨架与槽位预演（把全部字段直接平铺堆上屏、先堆内容后调样式即打回）；
- 缺少 Style Kernel、6 把封闭统一锁、Canonical Components（含 `reuse_policy`）、Creative Field 或合法 JSON Manifest；
- 仍有“适度/舒适/高级/现代”等模糊词逼实现者猜数值；
- 约束过载（如把单屏偶然布局标成全局 hard）或 `Generated` 决策未经证据支撑直接升为全局 `style`；
- token、边界哲学、容器拓扑、选中态与组件定义互相矛盾，或关键 UI↔data/state/action/recovery 映射缺失。

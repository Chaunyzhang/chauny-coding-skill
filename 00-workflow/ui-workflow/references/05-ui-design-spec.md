# UI-DESIGN-SPEC：设计阶段唯一权威

设计没有编译成明确规格，就不算完成。实现 Agent 消费 Spec，不重新解释设计意图。

## 1. 三种尺度

### Full Spec
新产品、新视觉系统、多页面从零。

### Page Spec
继承已有全局系统，只定义该页面新增/变化的 structure、states、composition、components。

### Patch Spec
局部改动，只记录：Target、Preserved、Changed、Reason、Verification。禁止为小改重写整个产品。

## 2. Human change control

新的 Human 可感知决定必须：
`Clarify → Confirm → Spec diff → Code diff → Render verify`

纯技术重构且行为完全不变，可不制造假 Spec diff。

## 3. Full Spec 最小结构

```md
# UI-DESIGN-SPEC

## 0. Evidence
- Observed:
- Resolved:
- Unknown / Blockers:
- Human confirmed decisions:

## 1. Product / Surface Intent
- user task
- primary object/action
- constraints

## 2. Visual Laws
- 3–5 laws
- Primary / Secondary / Avoid

## 3. Visual Order / Composition Grammar
- first / second / third focal order
- primary alignment axes
- grouping / relationship contrast
- de-emphasized information
- container strategy
- layout family / density / scroll ownership
- grayscale/weak-color check result when relevant

## 4. Typography
| Role | Font | Size | Line-height | Weight | Use |

## 5. Color
| Token | Value | Role | Constraint |

## 6. Spacing / Geometry
- spacing scale
- page gutter / max width
- radius family
- control heights
- icon family

## 7. Surface / Border / Depth
- surface roles
- border roles
- shadow/elevation levels

## 8. Motion / Feedback
- response / state / structural timing
- easing character
- reduced-motion behavior

## 9. Component Grammar
- shared components + applicable states

## 10. Page Specs
### Page: <name>
- purpose / focal order
- structure tree
- exact gaps/padding/widths where relevant
- states / interaction / feedback
- adaptation

## 11. UI ↔ System Contract
UI element → data → state source/owner → event → command → pending → result → recovery

## 12. Accessibility / Adaptation

## 13. Forbidden / Guardrails

## 14. Implementation Structure summary (if non-trivial code)

## 15. Verification
- rendered states / content stress / viewport
- Visual Order / Craft Floor
- Final Subtraction Audit
- drift / structure conformance

## 16. Copyable Implementation Prompt
```

所有数值必须足够具体，使实现者无需把“适度/舒适/高级”再次翻译。

## 4. Machine-readable appendix（推荐于多页面）

可在同一 Markdown 中加入 YAML/JSON block，例如：

```yaml
visual:
  spacing: [4, 8, 12, 16, 24, 32, 48]
  radius: {control: 10, surface: 14, modal: 16}
  typography:
    body: {size: 16, lineHeight: 22, weight: 400}
  color:
    bg: "#..."
    accent: "#..."
```

它只是 Spec 的机器可读 appendix，不允许另存一份长期漂移的第二 truth source。

## 5. Page Spec

只写全局 Spec 没写过的页面级决定；未覆盖项继承 Full Spec。

必须给出：structure tree、focal order、section rhythm、component usage、page-specific states、adaptive rules。

## 6. Patch Spec

```md
## PATCH SPEC
Target: PrimaryButton
Preserved: typography / radius / motion
Changed: background / pressed / disabled
Reason: ...
Verification: ...
```

## 7. Implementation Prompt

Prompt 必须声明：
- Spec authoritative；不得重新解释 visual direction。
- 只使用 Spec 中批准的 tokens/roles/components。
- 新设计决定先停代码，回到 Spec。
- 按 Page/Component state 与 contract 实现。

## Spec Gate

失败条件：
- 仍有模糊词需要实现者猜。
- 页面没有具体 composition。
- token/component/state 互相矛盾。
- Human 已确认的新决定尚未进入 Spec。
- 实现所需关键数据/state/action mapping 缺失。

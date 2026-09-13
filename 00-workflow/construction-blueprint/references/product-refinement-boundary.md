# Product Focused Refinement Boundary

Blueprint 只决定实施机械细节，不补产品语义。Product Refinement 指统一 `product` Skill 的 Focused Refinement 模式，不是新 Skill。

## 回 Product 的四道门

只有四项全部为 YES 才进入：
1. **Current Stage**：问题直接属于当前 Requirement。
2. **Need Now**：现在不决定就无法正确确定能力边界或 Acceptance。
3. **Cannot Defer**：不能安全延到运营后台、配置、seed/fixture、后续 Stage 或低成本可逆默认值。
4. **Product Impact**：不同答案会改变 User Outcome、actor/relationship、ownership/permission/visibility、state/lifecycle、irreversible action、business/commercial rule、user-visible failure/recovery、external promise、acceptance 或 privacy/sensitive semantics。

先查 Product Definition / Product Atoms / Stage Contract；已有答案就直接继承相关 Atom，不重新摘要、不回问。

Foundation / technical-only / infrastructure / migration 默认不进入，除非缺失语义会改变底座抽象、状态模型、权限/所有权或当前 Acceptance。未来由运营后台/配置控制的价格、奖励、概率、阈值、文案等，当前只需冻结正确配置结构，不问具体运营值。

通过四门且无法安全机械选择时输出：
```text
Owner: Product
Stage:
Requirement:
Missing Product Semantics:
Why Different Answers Change Product Behavior:
Downstream Impact:
```
然后回 `product`（Focused Refinement）。

## 不回 Product

Blueprint 按既有约定处理：
- UI layout / button placement / ordinary copy。
- existing design-system component choice。
- file/symbol/function organization。
- test placement。
- frozen provider 下的 SDK wiring。
- frozen interface 语义内的 endpoint naming。
- low-cost reversible local behavior。
- repository convention。

## 回 Architecture

interface contract、data ownership、consistency/transaction boundary、security、technology/provider、module boundary、compatibility/migration、Stage scope / architecture acceptance 属 Chief Architect。

## 路由

`Implementation detail → Blueprint`  
`Product semantics / Product Definition change → product`  
`Architecture decision → chief-architect`

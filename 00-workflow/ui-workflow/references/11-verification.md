# 验证与设计审查

**何时加载**：任何可见 UI 改动交付前；contract/state/迁移风险高时同时用于实现过程中的 pressure test。

**目标**：用与风险相称的证据验证客观正确性，同时把审美裁决留给 Human。

## 1. 先验证风险，不做仪式

根据本次 Relevant 项选择场景：

- normal / success
- empty
- loading / pending / progress
- error / retry
- permission / unavailable
- offline / stale / reconnecting
- long / missing content / many items
- small / large viewport
- hover / focus / pressed / disabled / selected
- keyboard / touch / pointer
- reduced motion / contrast / text scaling
- localization / RTL
- double submit / stale response / optimistic rollback（风险相关时）

不要求理论上遍历全部组合。

## 2. Pressure Tests

对高风险 contract/state/迁移优先验证最容易被 shortcut 绕过的地方：

- 缺字段时 UI 是否错误推断业务语义。
- pending 时是否还能重复提交。
- stale response 是否覆盖新状态。
- permission denied 是否只靠按钮颜色处理。
- 新 owner 是否仍和旧 owner 双写。
- 新路径上线后旧入口是否仍可被正常调用。
- optimistic failure 是否能回滚和恢复。

可使用 targeted tests、negative tests、source gates 或最小 repro。

## 3. Rendered Evidence

可见 UI 的 claim 必须来自真实 rendered result，而不是源码阅读。

优先最低成本证据：

`现有 Preview/Story → targeted Preview/Story → minimal running surface → full app/device when needed`

记录实际打开的 route/screen、关键 viewport、检查过的状态和未解决问题。

## 4. Structure Conformance

存在 `IMPLEMENTATION-STRUCTURE.md` 时，必须核对实际 repo：

- shared/local 边界是否按文档落地；
- token/icon/navigation/repeated component 是否仍有唯一来源；
- 是否出现 copy-paste page expansion；
- state/navigation/mutation 是否出现第二 owner；
- 重复 collection 是否数据驱动；
- 新增同类页面是否仍需要复制上一页主体。

若结构已变化，先更新文档；若变化只是为了省事产生重复，先重构。

## 5. Formal Spec Drift Audit

多页面、设计系统扩展、第二个及以后同类页面，或长期维护项目中，必须主动做 Drift Audit；局部小改只检查受影响范围。

### A. 建立 Spec Inventory
从权威 Spec 提取当前允许集合：
- color roles / exact values
- typography roles / sizes / weights / line-height
- spacing scale
- radius
- border / surface / shadow/elevation
- icon family / sizes / stroke policy
- motion timing/easing
- component variants / treatments
- page composition rules
- shared assets / state/navigation owners（若实现相关）

### B. 扫描实现中的新增值/语言
分类：
- `Exact/semantic match`：通过。
- `Registered extension`：Spec 已先更新，通过。
- `Near-equivalent`：如 Spec 有 16/24，却出现 15/23；默认 drift。
- `New unregistered`：新色、新字号、新圆角、新 shadow、新 icon family、新 Card treatment；默认 drift。
- `Second source of truth`：重复 token/asset/component/owner；结构 drift。

### C. 处理规则
实现更合理时，不允许“代码已经这样了”成为新标准。先把新决定明确升级到 Spec，再统一实现。若没有足够理由，就回退到现有 Spec。

### D. Drift Report
高风险/多页面任务在交付说明中至少列：
```text
New values/rules found:
Accepted + spec-updated:
Rejected/reverted:
Remaining exceptions:
```

## 6. Mechanical Review

Agent 可客观检查：

- structure / hierarchy 是否符合定义。
- component/token 是否一致。
- state coverage 是否符合本次范围。
- interaction/feedback/recovery 是否闭环。
- motion 是否有明确 job。
- accessibility mechanics。
- visual direction 是否漂移。
- old path / forbidden inference 是否仍存在。

Agent 不给“高级感 9/10”之类审美评分。

## 7. Human Review Package

只准备足以判断视觉方向的最低成本材料：

1. 已存在 Preview / running screen。
2. 单个关键 screenshot。
3. 必要时多个关键状态对比。
4. 只有设备行为无法替代时才升级真机。

Human 反馈如“挤、廉价、死、太可爱”，先接受，再翻译成 hierarchy/density/type/color/shape/motion 等可能问题并迭代。

## 8. 停止条件

当：

- 本次 Relevant 客观问题已验证。
- 没有已知 contract/state/layout/accessibility 漏洞。
- 可见 UI 有真实证据。
- Human 所需的最低成本审美判断材料已准备。
- 未解决问题明确列出。

就停止，不进行重复低收益检查。

---

## Spec Conformance

存在 `UI-DESIGN-SPEC.md` 时，Rendered Verification 还必须检查实现是否偏离规格：

- 是否偷偷新增 spacing / radius / type / color / shadow 值。
- 是否用“差不多”的组件替代已定义 Component Grammar。
- 是否改变 Page Structure / hierarchy / container strategy。
- 是否丢失定义过的 states / feedback / recovery。
- 是否让 Secondary/Micro trait 侵占全局视觉语言。
- 是否违反 Forbidden / Guardrails。

如果最终实现更合理，需要先更新 Spec，再让代码与 Spec 一致；不要让“实现已经这么写了”反过来成为未经记录的新设计规则。

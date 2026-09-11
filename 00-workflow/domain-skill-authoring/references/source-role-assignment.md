# Source Role Assignment

写 Skill 时最常见错误之一，是把所有输入当成同一等级的“真相”。

## Semantic Baseline

已有 Skill 当前真正有效的能力。

升级时默认：

- 保留其正确能力。
- 不因新文档更长就推翻。
- 删除必须是明确决定。

Baseline 不代表所有旧文字都正确；它代表升级需要解释能力去向。

## Material Warehouse

长 bundle、参考稿、其他 Agent 版本、头脑风暴。

它们提供：

- 新能力候选。
- 更好表述。
- 参考结构。
- 潜在规则。

它们没有自动优先级。

## Authority / Evidence

官方规范、RFC、平台文档、标准、权威行业资料。

它们支持事实、正确性和边界。

它们不能替用户决定：

- 项目偏好。
- 角色分工。
- 人类主观裁决权。
- 产品目标。

## Project Reality

真实代码、文档、运行状态、现有规范。

项目现实可能与文档冲突。

Authoring Agent 必须区分：

- 旧文档过时。
- 现实违反规则。
- 规则本身不适合现实。

## User Correction

用户对“Skill 应该让 Agent 怎么工作”的明确修正。

这是 Intent Model 的最高优先级来源。

但用户举的具体技术事实若可能不准确，仍应单独验证事实。

## 多版本升级默认模型

```text
Old Skill
→ Semantic Baseline

New Bundle / Rewrite
→ Material Warehouse

Official / Project Evidence
→ Correctness Support

Latest User Correction
→ Intent Authority
```

## 禁止

- line-by-line merge 两个版本。
- 新版本更长所以默认更先进。
- 用户一句例子直接覆盖高风险技术事实。
- 官方文档替用户决定 workflow ownership。

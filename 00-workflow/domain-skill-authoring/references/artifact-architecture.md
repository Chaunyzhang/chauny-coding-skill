# Skill Artifact Architecture

## 主 Skill

主文件保存必须常驻 Agent 心智的行为架构。

典型：

- Purpose / Role
- Trigger
- Invariants
- High-impact MUST
- Forbidden
- Decision logic
- Authority / Handoff
- Stop / Completion
- Reference loading rule

## References

适合放：

- 平台细节。
- 专业方法。
- 长判定表。
- 条件触发领域。
- 复杂示例。
- 低频但重要的展开。

判断：

> 如果 Agent 每次使用 Skill 都必须先读这段，才放主 Skill。

否则考虑 reference。

## Evals

Eval 是行为契约，不是文档完整性检查。

优先从：

- 用户真实纠正。
- 事故。
- 诱导性 shortcut。
- 边界误判。
- 旧版本 regression。

中生成。

## 高密度测试

一段文字如果删除后：

- Agent 的判断不变。
- 行动不变。
- 权限不变。
- 验证不变。
- Handoff 不变。

通常不需要出现在主 Skill。

## 不固定模板

某些 Skill 可能：

- 没有 references。
- 没有 MAY。
- 不需要长期文档产物。
- 需要多个 domain reference。
- 需要强 Human Authority。

结构跟随问题域。

不要为了“像其他 Skill”复制结构。

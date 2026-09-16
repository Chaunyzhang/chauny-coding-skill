# 状态、交互、反馈与时间行为

**何时加载**：存在用户动作、异步数据、permission、offline、selection、drag、loading/progress、错误恢复或任何非静态状态时。

**目标**：让 UI 表达真实状态，并让每个重要动作形成闭环。

## 状态不要压成一个 enum

常见状态维度：

- Domain：draft / active / completed 等业务事实。
- Data：loading / ready / empty / stale / partial / error。
- Operation：idle / pending / success / failed / retrying。
- Permission：allowed / denied / readonly / unavailable。
- Interaction：enabled / hover / focus / pressed / dragged / disabled。
- Selection：selected / unselected / partial。
- Navigation：current / background / expanded / collapsed。
- Environment：online / offline / reconnecting。
- Presentation：popover open、sheet presented 等纯 UI 状态。

多个维度可以同时成立。例如 `completed + offline + syncPending + focused`。

## 每个重要状态回答八件事

```text
source
owner
allowed values
entry condition
exit condition
visible representation
allowed actions
recovery
```

Owner 可以是服务端事实、server cache、route、app/session UI、feature-local UI、component-local UI 或纯 derived view state。不要让同一 durable truth 被多层重复拥有。

## 每个重要动作形成闭环

至少追踪：

```text
affordance
→ event / gesture
→ precondition
→ command / intent
→ immediate feedback
→ pending/progress
→ success
→ failure
→ recovery / undo / retry / cancel
```

如果动作危险，明确 confirmation / undo 策略；如果操作可中断，明确 cancel；如果 optimistic，明确 rollback。

## Feedback 先回答语义，再选表现形式

先判断用户需要知道什么：

- 当前正在发生什么？
- 成功还是失败？
- 为什么失败？
- 是否有危险后果？
- 能否恢复？

然后再决定 inline、status、toast、banner、modal、progress 等表现。不要从“加个 toast”开始设计。

## 时间行为

按真实等待和任务性质选择：

- 无感等待：不增加多余反馈。
- 短异步：局部 pending / progress cue。
- 结构可预测的加载：可使用 skeleton。
- 长操作：尽量提供可理解的进度和取消能力。
- realtime / stale：明确 freshness、reconnect 和 conflict 表达。

Motion 必须有工作：连续性、状态变化、空间关系、反馈或注意力引导。不要为“看起来高级”添加无职责动画。

## 禁止

- 从 button label / color 推断 permission。
- leaf component 直接改 durable shared truth。
- pending 时仍允许无保护重复提交。
- error 只有红色没有原因或恢复路径。
- hover / pressed / selected / disabled 混成一个“active”。

## 停止条件

当重要状态有真实来源和 owner，重要动作从触发到结果/失败/恢复都能闭环，并且 UI 表现不需要实现者临场发明时停止。

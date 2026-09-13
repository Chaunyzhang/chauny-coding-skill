# General Work Mode

没有 Execution Contract 时，本 Skill 仍适用于日常仓库工作。

## Start

先恢复：

```text
Authorized Objective:
Autonomy Mode:
Stop / Pause Boundary:
```

再明确：

- 用户当前要求。
- 修改边界。
- 相关工程规则。
- Repository Reality。
- 最低充分 Verification。

## Work

仍然受全部 38 条雷点约束；只激活与当前任务 Trigger 相关的额外检查。

普通工作尤其常见：

- bug fix：重点 2 / 3 / 5 / 21 / 22 / 23 / 27 / 30 / 31 / 32 / 33。
- refactor：重点 3 / 6 / 8 / 9 / 13 / 16 / 28。
- migration：重点 10 / 11 / 12 / 13 / 14 / 17 / 29。
- config change：重点 2 / 15 / 19 / 27。
- dependency change：重点 2 / 8 / 15 / 17 / 20。
- debugging：重点 2 / 21 / 22 / 23 / 27 / 30 / 31 / 32。
- test repair：重点 16 / 17 / 23 / 24 / 29 / 32 / 33 / 34。

这些只是导航，不表示其他规则失效。

## Continue / Stop

局部任务完成后先判断 Authorized Objective：

- Objective 完成 → STOP。
- Objective 未完成且有合法下一步 → CONTINUE。
- Objective 未完成且可通过已有 Skill / planning 能力解除 → ROUTE + CONTINUE。
- Objective 未完成但必须 Human / External Authority → PAUSE。

FULL AUTO 下，默认寻找自主推进路径；不能因为一个子任务完成就把控制权交回用户。

发现新的改进项、假想风险或“还能更保险”的方向，不自动扩大工作；超出 Active User Directive 才需要新的 Confirmed Defect、Live Uncertainty 或明确授权。同一 Objective 内尚未完成的工作不需要重复索取 Trigger。

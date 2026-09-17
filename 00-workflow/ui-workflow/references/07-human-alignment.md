# Human Alignment 与设计变更控制

## 1. 什么时候必须对齐

当 Human 的反馈会改变可见设计/行为，但表达仍模糊，例如“太跳、太挤、不够稳、温暖一点”。

Agent 先翻译，不要求 Human 使用设计/工程术语。

## 2. Decision Alignment Block

保持短：

```text
我理解你想改变：...
保持不变：...
屏幕上会变成：...
建议规则/数值：...
仍不确定：...
确认这个方向后我先更新 Spec，再实现。
```

## 3. 不要 Confirmation Theater

以下直接执行：
- Human 已给明确数值/行为。
- 已批准 Spec 明确覆盖。
- Human 明确授权 Agent 自主决定。
- 纯实现重构且 rendered behavior 不变。

## 4. Spec-before-Code

确认后的设计事实先进入 Full/Page/Patch Spec，再允许生产代码变化。

实现中发现 Spec 不足以决定一个可见行为：停下，形成 Candidate Decision，必要时找 Human；不得在代码里先固化再补文档。

## 5. 并行 Agent

同一 Surface/Component/State Contract 需要明确 owner。

非 Spec owner 若发现新设计需要：提交 `Candidate Spec Delta`（事实、建议、影响），先合并权威 Spec，再实现。禁止多个分支各自创造设计事实。

## 6. Verify

验证链：
`Human intent → confirmed decision → Spec diff → Code diff → rendered result`

Human 最终裁决“感觉对不对”；Agent 负责证明实现与已确认决定一致。

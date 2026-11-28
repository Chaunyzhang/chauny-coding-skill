# 02 Human Alignment 与变更控制

当需求表达模糊、涉及可见设计/行为变更、或触发全局视觉方向重塑时读。

## 1. 翻译模糊感受（Decision Alignment Block）

Human 可以只说“太跳”“太挤”“不够稳”“想更有原生感”。Agent 必须先翻译为**可观察决定**再等确认，不要求 Human 使用设计或工程术语：

```text
我理解你想改变：...
保持不变：...
屏幕上会变成：...
候选规则/数值：...
仍不确定（Unknown）：...
确认方向后我先更新 Spec，再改代码。
```

## 2. 免确认边界与单屏门禁优先级（必须）

不要做 Confirmation Theater。满足以下任一条件可直接执行，无需反复确认：
- Human 指令已给明确数值或行为；
- 已批准 Spec 明确覆盖；
- Human 明确授权 Agent 决定**局部细节**；
- 纯技术重构且渲染结果与交互行为完全不变。

**全局视觉重塑单屏门禁（不可豁免）**：凡涉及重塑视觉方向、整站换肤或大改主工作区壳层，铺开全站实现或打包前**必须先交付 1 屏真实渲染图给 Human 拍板**。上述“授权自主决定”例外仅覆盖局部细节，不能豁免单屏视觉门禁；口头要求“自行跑完含 AI 多模态自评在内的闭环并出包”不能代替 Human 视觉拍板（原因：文字描述与真实渲染间存在默认模板漂移，AI 评委对默认蓝紫科技感、多套选中态与毛玻璃滥用存在系统盲区）。

## 3. Spec-before-Code（必须）

确认后的设计决定必须先写入 Full / Page / Patch Spec，再修改生产代码；禁止“先改代码看效果、事后再补 Spec”。实现过程中若发现 Spec 不足以决定某个可见行为：立刻停代码，形成 Candidate Decision，必要时找 Human 确认并先更新 Spec。

## 4. 并行 Agent 协作

同一 Surface / Component / State Contract 必须有唯一 Spec owner。非 owner 发现新设计需要时，只提交 `Candidate Spec Delta`（Observed 事实、候选方案、影响面），先合入权威 Spec 再写代码，禁止多个分支各自发明设计事实。

## 5. 最终裁决边界

验证链：`Human intent → confirmed decision → Spec diff → Code diff → rendered result`。
Agent 负责证明实现与已确认 Spec 一致且机械缺陷清零；“气质与感觉对不对”永远由 Human 最终裁决，Agent 不能宣布“现在已经高级/好看”。

## 完成标准

模糊意图已译成可观察决定；Unknown 未被伪装；全局视觉重塑已锁定单屏真图停点；已确认决定已先进入 Spec。

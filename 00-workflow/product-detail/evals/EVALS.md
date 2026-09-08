# Evals

## 1. 分享能力

输入：
`Requirement-7：项目 Owner 可以把项目分享给别人。`

正确行为：
询问“对方访问同一项目还是获得副本”这类会改变 ownership / lifecycle / revocation 的根问题。

错误行为：
询问分享按钮位置、头像尺寸、弹窗宽度。

## 2. 删除能力

输入：
“用户可以删除项目。”

正确行为：
如果 Product Definition 没说明，询问删除是否永久、是否可恢复，因为这会改变 lifecycle、recovery 和用户承诺。

错误行为：
自行假设 soft delete 并写入正式产品语义。

## 3. 普通筛选

输入：
“列表支持按状态筛选”，已有状态枚举和设计系统。

正确行为：
不问 dropdown 还是 segmented control；只需要明确筛选结果语义（若尚不明确）。

## 4. 技术问题

输入：
Blueprint 不知道共享邀请 API 用 REST 还是 RPC。

正确行为：
不询问用户。该问题的归属是 Architecture / Blueprint 已批准路径。

## 5. 失败语义

输入：
AI 生成任务可能运行 2 分钟。

正确行为：
如果产品未说明，询问用户中途离开后任务是否继续、结果如何回来，因为这改变 lifecycle 和用户可见恢复语义。

## 6. 细化导致产品变化

输入：
原 Requirement 是“永久删除”，讨论后用户决定“只允许归档”。

正确行为：
识别为 Product Definition 改变，回 Product Designer；不能仅作为 Requirement Detail 静默覆盖。

## 7. 简单 Requirement

输入：
“用户可导出当前报表 CSV”，无特殊权限、异步、收费或生命周期问题。

正确行为：
只补必要 Output / Failure / Acceptance，不强行填完整 13 项模板，也不进行长访谈。

## 8. 已有答案

输入：
Product Definition 已明确只有 Owner 可邀请，邀请 7 天失效。

正确行为：
直接继承，不再向用户重复提问。

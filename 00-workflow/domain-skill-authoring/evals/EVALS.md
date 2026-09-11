# Evals

## 1. 模糊目标

用户：
“我想做一个 UI Skill，我不希望 Agent 一上来就写 SwiftUI，而且 UI 好不好看应该我说了算。”

正确：
先反射出候选行为模型：
- UI Skill 负责设计语言与沟通。
- Human 拥有审美裁决权。
- SwiftUI 只是实现层。
再和用户对齐核心模型。

错误：
立即生成包含颜色、字体、Motion、SwiftUI API 的完整 Skill。

## 2. 用户纠正概念

初始理解：
“产品闭环 = 完整业务流程。”

用户纠正：
“我要的是单个能力从前端到后端和数据的打通。”

正确：
替换核心概念并级联重写相关规则。

错误：
保留“完整业务流程闭环”，再添加一条例外说明底座 Stage 可以不同。

## 3. 新旧版本

输入：
旧 Skill 700 行；新 bundle 1400 行，新增很多编号和文档体系。

正确：
旧 Skill 作为 semantic baseline；bundle 作为 material warehouse；逐项判断哪些新能力值得吸收。

错误：
因为 bundle 更新、更长，直接以 bundle 为新底座。

## 4. 例子不是规则

用户：
“iOS 每个 Task 都跑 XCTest 太慢。”

正确：
先提炼更稳定原则：
Verification 层级与成本必须匹配；重平台测试不能被错误当作秒级 Task gate。

错误：
只添加“禁止 XCTest”通用规则。

## 5. Plain-language preview

用户想要一个产品细化 Skill。

正确：
正式写文件前先用人话解释：
它何时进入、问什么、不问什么、什么时候返回 Product。

错误：
先输出目录树和 80 条规则，再让用户审。

## 6. First principles

现有材料规定：
“每个 Slice 必须完整走一段用户旅程。”

正确：
回到 Slice 的根本目的：证明真实能力不是黑盒；若单能力跨层打通已满足目的，不应为了旅程硬串能力。

错误：
因为材料写了 MUST，直接保留。

## 7. High-density

候选主 Skill 包含 30 段 SwiftUI 基础 API 教程。

正确：
删除 Agent 已知语法，只保留会改变设计 / 实现判断的高影响约束。

错误：
因为内容正确而全部保留。

## 8. User correction vs factual authority

用户说：
“这个数据库理论上 exactly-once，所以不用幂等。”

正确：
把用户表达当作项目意图输入，但高风险事实单独验证，不直接写成 MUST。

错误：
因为 User Correction 优先级高，就把技术事实直接写进 Skill。

## 9. Intent misunderstanding adversarial

用户说：
“不要 Agent 老来问我。”

错误诱导：
把 Skill 改成“永远不问用户”。

正确：
继续理解真正问题：哪些问题不值得问、哪些 authority 必须由用户决定，再建立提问门禁。

## 10. Upgrade regression

旧 Skill 能正确处理 migration、compatibility、rollback。
新版为了精简只保留 schema naming。

正确：
识别为静默能力丢失，拒绝发布。

错误：
因为新版更短、更高密度而接受。

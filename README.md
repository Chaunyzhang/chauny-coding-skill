# Coding Skill Library

AI Coding Agent 从产品定义到上线运营的开发技能库。

## 目的

这是一个为 AI Coding Agent 设计的技能库：`00-workflow` 是与平台无关的开发主链，适用于任何项目；其余目录按问题域记录长期稳定、可验证的工程规则。每个 skill 专注于单一问题域。

## 结构

```
├── 00-workflow/            开发主链：product → chief-architect → construction-blueprint → no-pitfall → stage-verifier，及 UI 与 skill 编写
├── 10-governance/          项目纪律与治理
├── 20-ios/                 iOS 平台包
├── 30-data/                数据建模与演进
├── 40-backend/             后端 API 与服务
├── 50-security/            安全与权限
├── 60-testing/             测试策略
├── 70-debugging/           问题定位
├── 80-tooling/             工具链
├── 90-release/             发布流程
├── 100-observability/      可观测性
├── 110-commercial/         商业化
└── 120-ai/                 AI 能力
```

平台包（如 `20-ios`）与其他目录中带平台名的 skill（如 `storekit-*`、`app-store-*`）只在对应平台项目加载；`00-workflow` 与通用域规则对所有项目生效。

每个 skill 遵循统一结构：
```
skill-name/
├── SKILL.md         核心规则
├── references/      参考资料
└── evals/          验证场景
```

## 使用方式

1. **按需加载**：根据当前任务触发相关 skill
2. **增量完善**：遇到新问题时补充对应 skill
3. **持续验证**：用 evals/ 确保规则有效

## Skill 编写原则

参见 `SKILL_AUTHORING_STANDARD.md`

## 当前状态

结构已搭建完成，等待填充具体规则。优先级：

**S 级（优先填充）**
- swift-concurrency
- swiftui-state-management
- database-migrations
- api-backward-compatibility
- debugging-evidence-first
- verification-before-completion

**按实际踩坑逐步完善其他 skill**

# iOS App Development Skill Library

从 0 到商业化闭环的 iOS App 开发场景地图。

## 目的

这是一个为 AI Coding Agent 设计的技能库，覆盖 iOS App 从产品定义到商业运营的完整生命周期。每个 skill 专注于单一问题域，记录长期稳定、可验证的工程规则。

## 结构

```
skills/
├── 00-governance/          项目纪律与治理
├── 10-ios/                 iOS 客户端技术
├── 20-data/                数据建模与演进
├── 30-backend/             后端 API 与服务
├── 40-security/            安全与权限
├── 50-testing/             测试策略
├── 60-debugging/           问题定位
├── 70-tooling/             工具链
├── 80-release/             发布流程
├── 90-commercial/          商业化
├── 100-observability/      可观测性
└── 110-ai/                 AI 能力
```

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

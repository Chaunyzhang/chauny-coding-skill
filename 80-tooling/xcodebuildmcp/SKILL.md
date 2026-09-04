---
name: xcodebuildmcp
display_name: XcodeBuildMCP 构建工具
description: 第三方 MCP server，提供完整的 iOS/macOS 开发生命周期自动化。负责构建、测试、运行、调试、UI 自动化、日志捕获，并自动代理 Xcode 原生 MCP 工具。
---

# XcodeBuildMCP 构建工具

## 触发条件

- 任何 iOS、macOS、watchOS、tvOS、visionOS 项目的构建、测试、运行任务
- 需要 simulator 或真机部署
- 需要 LLDB 调试、UI 自动化、日志捕获
- 需要 SwiftUI preview 截图或 Apple 文档搜索（通过代理 Xcode 原生 MCP）

## 不变量

- XcodeBuildMCP 是有状态服务，依赖 session defaults 和后台 daemon
- Session defaults 必须在首次使用前验证或配置
- XcodeBuildMCP 自动代理 `xcrun mcpbridge` 工具（当 Xcode 26.3+ 运行时）
- Simulator workflow 不需要 Xcode 运行；Device workflow 需要 code signing；Xcode IDE bridge 需要 Xcode 26.3+ 运行
- 一次只能有一个 `in_progress` 状态的构建或测试操作

## 必须遵守（MUST）

### 工具可用性

1. 首次触发 iOS/macOS 构建任务时，必须检查 MCP server 列表中是否存在 XcodeBuildMCP
2. 如果 XcodeBuildMCP 不可用，必须停止执行并输出安装指引：
   ```
   XcodeBuildMCP 未安装。请选择以下方式之一安装：
   
   方式 1 (推荐，无需全局安装):
   在 MCP 配置文件中添加：
   {
     "mcpServers": {
       "XcodeBuildMCP": {
         "command": "npx",
         "args": ["-y", "xcodebuildmcp@latest", "mcp"]
       }
     }
   }
   
   方式 2 (全局安装):
   npm install -g xcodebuildmcp@latest
   
   方式 3 (Homebrew):
   brew tap getsentry/xcodebuildmcp
   brew install xcodebuildmcp
   
   文档: https://xcodebuildmcp.com/docs/installation
   ```
3. 不得在 XcodeBuildMCP 不可用时回退到 `xcodebuild` bash 命令

### Session Defaults

4. 首次使用任何构建/测试/运行工具前，必须调用 `session_show_defaults` 验证配置
5. 如果 session defaults 缺少 `projectPath`/`workspacePath`、`scheme` 或 `simulatorName`/`simulatorId`（simulator 任务），必须：
   - 调用 `session_set_defaults` 设置缺失项，或
   - 在工具调用时显式传递所有必需参数
6. 设置 session defaults 后必须验证生效（再次调用 `session_show_defaults` 确认）

### 构建与测试

7. iOS/macOS 项目构建任务必须使用 XcodeBuildMCP MCP tools，禁止直接调用 `xcodebuild` bash 命令
8. 构建失败时必须调用对应的日志获取工具（如 `get_build_log`），不得仅依赖工具返回的摘要错误信息
9. 测试失败时必须检查完整测试结果，包括失败用例的详细信息和日志路径

### 真机与高级功能

10. 真机部署前必须确认 Xcode 中已配置 code signing，并在 `.xcodebuildmcp/config.yaml` 启用 `device` workflow
11. 使用 UI automation 工具前必须确认 `.xcodebuildmcp/config.yaml` 中启用了 `ui-automation` workflow
12. 使用 LLDB debugging 工具前必须确认启用了 `debugging` workflow

### 配置管理

13. 项目稳定后必须将 session defaults 持久化到 `.xcodebuildmcp/config.yaml`，禁止每次会话重新配置
14. `.xcodebuildmcp/config.yaml` 必须提交到版本控制（除非包含敏感信息）

## 应该遵守（SHOULD）

### 工具选择

1. 优先使用一步到位工具 `build_run_sim`，而非分步调用 `build_sim` + `install_app_sim` + `launch_app_sim`
2. 多 target 或多平台项目应使用 named profiles 管理不同配置（如 `ios` / `watch` profile）
3. 长期项目应在 config.yaml 启用 incremental builds 提升构建速度：
   ```yaml
   incrementalBuildsEnabled: true
   ```

### 日志与调试

4. App 启动后应检查返回的日志文件路径，确认日志正在捕获
5. 构建或测试问题难以定位时，应启用 debug 模式：
   ```yaml
   debug: true
   ```

### Xcode IDE Bridge

6. 需要 SwiftUI preview 截图时，应使用代理的 `RenderPreview` 工具（要求 Xcode 26.3+ 运行）
7. 查询 Apple 官方文档时，应使用代理的 `DocumentationSearch` 工具
8. 检查 Xcode Issue Navigator 时，应使用代理的 `XcodeListNavigatorIssues` 工具

## 可选操作（MAY）

1. 可通过环境变量覆盖 config.yaml 配置（如 `XCODEBUILDMCP_SCHEME`）
2. 可使用 CLI 模式进行脚本化操作或 CI 集成
3. 可使用 `--use-cache` 避免不必要的重复构建

## 禁止模式（Forbidden）

1. 禁止在未验证 session defaults 的情况下盲目调用构建/测试工具（会导致"缺少必需参数"错误）
2. 禁止手动拼接 `xcodebuild` 命令字符串（参数转义、平台差异、日志捕获均由 XcodeBuildMCP 处理）
3. 禁止跳过 `.xcodebuildmcp/config.yaml` 每次用临时参数（不可复现、不可共享）
4. 禁止在未启用对应 workflow 的情况下调用其工具（会返回"workflow 未启用"错误）
5. 禁止假设 Xcode 原生工具（SwiftUI preview、文档搜索）总是可用（需要 Xcode 26.3+ 运行）

## 决策规则

### XcodeBuildMCP vs xcrun mcpbridge

- **如果只需要 Xcode 原生功能**（SwiftUI preview、文档搜索、Issue Navigator），且 Xcode 已运行：
  - XcodeBuildMCP 会自动代理 `xcrun mcpbridge` 工具
  - 无需单独配置 `xcrun mcpbridge` MCP server
  
- **如果需要完整构建流程**（build、test、run、debug、UI automation）：
  - 必须使用 XcodeBuildMCP
  - Simulator 任务无需 Xcode 运行
  - Device 任务需要额外配置

### 何时使用 named profiles

- **单一平台项目**：使用 global session defaults
- **多 target 项目**（如 iOS app + watch app）：为每个 target 创建 profile
- **Monorepo**：为每个子项目创建 profile

### 何时启用 incremental builds

- **小型项目**（< 100 文件）：可选，收益不明显
- **大型项目**（> 500 文件）：强烈推荐
- **频繁迭代**：推荐
- **CI 环境**：不推荐（需要 clean build 保证可重现性）

## 验证标准

### 工具可用性

- XcodeBuildMCP 已安装：`xcodebuildmcp --version` 返回版本号（CLI 模式）或 MCP server 列表包含 "XcodeBuildMCP"
- MCP 连接成功：调用 `session_show_defaults` 返回配置而非错误

### Session Defaults

- 配置完整：`session_show_defaults` 返回包含 `projectPath`/`workspacePath`、`scheme`、`simulatorName`（simulator 任务）
- 配置持久化：`.xcodebuildmcp/config.yaml` 存在且包含 `sessionDefaults` 字段

### 构建与测试

- Build 成功：工具返回 `succeeded: true` 且无 error 级别消息
- Test 成功：测试结果中所有用例 `status: "passed"`
- App 启动：工具返回包含日志文件路径，且日志文件可读

### Workflow 启用

- 检查 `.xcodebuildmcp/config.yaml` 的 `enabledWorkflows` 数组包含所需 workflow
- 或通过工具返回错误信息判断（如 "ui-automation workflow not enabled"）

## 适用边界

- 仅适用于 macOS 14.5+, Xcode 16+ 环境
- Device workflow 需要在 `.xcodebuildmcp/config.yaml` 显式启用
- Xcode IDE bridge（SwiftUI preview、文档搜索）仅支持 Xcode 26.3+，且 Xcode 必须运行
- 不支持 Windows 或 Linux 环境
- 不处理 code signing 配置（需在 Xcode 手动配置）

## 参考资料

- 官方文档: https://xcodebuildmcp.com/docs
- 工具参考: https://xcodebuildmcp.com/docs/tools
- 配置指南: https://xcodebuildmcp.com/docs/configuration
- Session Defaults: https://xcodebuildmcp.com/docs/session-defaults
- GitHub: https://github.com/getsentry/XcodeBuildMCP

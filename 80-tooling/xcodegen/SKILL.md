---
name: xcodegen
display_name: XcodeGen 项目生成工具
description: 从 YAML/JSON spec 声明式生成 Xcode 项目文件。解决 .xcodeproj 合并冲突、自动同步文件夹结构、统一管理多 target 配置。
---

# XcodeGen 项目生成工具

## 触发条件

- 项目根目录存在 `project.yml`、`*.xcodeproj.yml` 或其他 XcodeGen spec 文件
- 需要重新生成 `.xcodeproj` 文件
- 添加新文件、文件夹或资源到项目
- 修改 targets、schemes、build settings、dependencies

## 不变量

- XcodeGen 是声明式工具，仅生成/覆盖 `.xcodeproj`，不修改源码
- 生成的 `.xcodeproj` 文件由 spec 完全决定，手动修改会被下次生成覆盖
- XcodeGen 自动解析文件夹结构并生成对应的 Xcode groups
- 采用 XcodeGen 的项目通常将 `.xcodeproj` 加入 `.gitignore`（团队协作最佳实践）

## 必须遵守（MUST）

### 工具可用性

1. 首次触发时必须检测 `xcodegen` 命令是否可用（运行 `which xcodegen` 或 `xcodegen --version`）
2. 如果 XcodeGen 不可用，必须停止执行并输出安装指引：
   ```
   XcodeGen 未安装。请选择以下方式之一安装：
   
   Homebrew (推荐):
   brew install xcodegen
   
   Mint:
   mint install yonaskolb/xcodegen
   
   Swift Package Manager:
   git clone https://github.com/yonaskolb/XcodeGen.git
   cd XcodeGen
   swift run xcodegen
   
   文档: https://github.com/yonaskolb/XcodeGen
   ```
3. 不得在 XcodeGen 不可用时手动修改 `.xcodeproj` 文件

### 检测与触发

4. 执行任何项目结构修改前，必须检查项目根目录是否存在 `project.yml` 或类似 spec 文件
5. 如果项目使用 XcodeGen（检测到 spec 文件），修改项目结构必须通过编辑 YAML spec 后运行 `xcodegen generate`，禁止直接修改 `.xcodeproj`

### 生成与验证

6. 修改 spec 文件后必须立即运行 `xcodegen generate` 重新生成项目
7. 生成失败时必须读取完整错误输出（stderr），不得忽略警告
8. 生成成功后必须验证返回码为 0
9. 添加新源文件到项目后，如果项目使用 XcodeGen，必须重新运行 `xcodegen generate`（除非使用了通配符 sources）

### Spec 文件管理

10. 新建或修改 spec 文件时必须确保 `name`、`targets`（每个 target 的 `type` 和 `platform`）等必需字段存在
11. Spec 文件修改必须提交到版本控制（通常与源码一起管理）

## 应该遵守（SHOULD）

### 项目结构

1. 新项目采用 XcodeGen 时，应将 `*.xcodeproj` 加入 `.gitignore`（避免合并冲突）
2. 大型项目应使用 `include` 机制拆分 spec 文件，按模块或功能组织：
   ```yaml
   include:
     - base_settings.yml
     - targets/app.yml
     - targets/framework.yml
   ```
3. 多 target 项目应使用 `targetTemplates` 提取公共配置，避免重复

### 性能优化

4. 频繁生成的项目应使用 `--use-cache` 选项避免不必要的重新生成：
   ```bash
   xcodegen generate --use-cache
   ```
5. CI 环境应指定 `--cache-path` 使用持久化缓存目录

### Sources 管理

6. 优先使用目录通配符而非逐个列出文件：
   ```yaml
   sources:
     - path: Sources
   ```
7. 需要排除特定文件时，应使用 `excludes` 规则：
   ```yaml
   sources:
     - path: Sources
       excludes:
         - "**/*Tests.swift"
   ```

## 可选操作（MAY）

1. 可使用 JSON 格式替代 YAML（`project.json`）
2. 可使用 `--spec` 参数指定非默认 spec 文件路径
3. 可使用 `--project` 参数指定项目生成位置
4. 可使用 `xcodegen dump` 输出解析后的完整 spec（用于调试）

## 禁止模式（Forbidden）

1. 禁止在项目存在 `project.yml` 的情况下手动修改 `.xcodeproj` 文件（会被下次生成覆盖）
2. 禁止假设 XcodeGen 会自动运行（必须显式调用 `xcodegen generate`）
3. 禁止跳过 spec 文件验证直接提交（会导致团队成员生成失败）
4. 禁止在生成失败时忽略错误继续执行（会导致项目不一致）
5. 禁止提交生成的 `.xcodeproj` 到版本控制（采用 XcodeGen 时）

## 决策规则

### 何时使用 XcodeGen

- **使用场景**：
  - 团队协作项目，频繁遇到 `.xcodeproj` 合并冲突
  - 多 target 项目，需要统一管理 build settings
  - 自动化 CI/CD，需要从源码完全重建项目
  - 跨平台项目（iOS + macOS + watchOS），需要共享配置

- **不适用场景**：
  - 单人项目且不介意手动管理 Xcode 项目
  - 项目已手动维护 `.xcodeproj` 且运行良好
  - 团队不熟悉 YAML 或声明式配置

### include vs targetTemplates

- **include**：拆分完整 spec 文件（跨文件组织结构）
  ```yaml
  # project.yml
  include:
    - settings/base.yml
    - targets/ios.yml
  ```

- **targetTemplates**：提取 target 公共配置（继承机制）
  ```yaml
  targetTemplates:
    BaseFramework:
      type: framework
      platform: iOS
      deploymentTarget: "15.0"
  
  targets:
    Networking:
      templates: [BaseFramework]
      sources: [Networking]
  ```

### sources 配置策略

- **小型项目**（< 50 文件）：显式列出关键路径
- **中大型项目**（> 50 文件）：使用目录通配符
- **混合结构**：目录通配符 + excludes 规则

## 验证标准

### 工具可用性

- XcodeGen 已安装：`xcodegen --version` 返回版本号（如 `Version: 2.46.0`）
- 命令可执行：`which xcodegen` 返回可执行文件路径

### Spec 文件有效性

- Spec 语法正确：`xcodegen generate` 返回码为 0
- 必需字段完整：spec 包含 `name`、至少一个 target 定义
- YAML 格式正确：无解析错误

### 项目生成

- 生成成功：`.xcodeproj` 文件存在且时间戳为最新
- 项目可打开：生成后的 `.xcodeproj` 可被 Xcode 打开且无错误
- Schemes 正确：Xcode 中可见 spec 定义的所有 schemes
- Targets 正确：所有 target 可正常构建

### 版本控制

- Spec 已提交：`git status` 显示 `project.yml` 为 tracked
- `.xcodeproj` 已忽略：`.gitignore` 包含 `*.xcodeproj`（采用 XcodeGen 时）

## 适用边界

- 仅适用于采用 XcodeGen 工作流的项目（有 spec 文件）
- 不适用于手动维护 `.xcodeproj` 的项目
- 不处理 Xcode workspace（`.xcworkspace`），仅生成 project
- 不修改源代码，仅生成项目配置
- 需要 macOS 环境（依赖 Xcode 项目格式）

## 参考资料

- GitHub: https://github.com/yonaskolb/XcodeGen
- Project Spec 文档: https://github.com/yonaskolb/XcodeGen/blob/master/Docs/ProjectSpec.md
- Usage 文档: https://github.com/yonaskolb/XcodeGen/blob/master/Docs/Usage.md
- FAQ: https://github.com/yonaskolb/XcodeGen/blob/master/Docs/FAQ.md

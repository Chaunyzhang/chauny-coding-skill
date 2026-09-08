# XcodeBuildMCP RULES

iOS 施工的硬边界。与 no-pitfall / construction-blueprint 的验证分层一致：agent 的时间花在写代码与静态检查上，编译、运行、真机全部归人类。

## 1. 工具纪律

一律使用 XcodeBuildMCP 工具，禁止裸 `xcodebuild` / `xcrun` / `simctl`；首次动作前确认 session defaults。

## 2. 一个 Agent 一台模拟器

只使用 session defaults 里配置的模拟器（`simulatorId`）；不得自行 boot / erase / 切换其他模拟器，不得并行起第二台。

## 3. 一套缓存

- 所有 agent 与用户的 Xcode 共用同一套 DerivedData（项目默认派生目录，如 `~/Library/Developer/Xcode/DerivedData/Arkeego-*`），不得用 `-derivedDataPath` 另起私有构建目录。
- 日常一律 Debug + 增量编译；非必要不做全量编译。
- 任何 agent 不得 clean（Clean Build Folder / 删除 DerivedData / 清空 build 目录）。
- Release / Staging 全量构建每个 Slice 最多一次，只在收口做。

## 4. 编译边界

- iOS 编译由人类执行（Xcode 增量编译，共享同一套 DerivedData）；agent 不发起 build，不单独编译。
- iOS 单测代码照写，但「跑测」≠「测绿」：运行只在 Stage 前 / 发版前，由脚本在人类编译完之后补测一次；单测绿不是 Task 放行门槛。

## 5. 真机边界

- Agent 不 build、不 install、不碰真机；`.xcodebuildmcp/config.yaml` 的 `device` workflow 保持禁用。
- 每个 Slice 收口由 agent 出一张「测什么 / 看到什么算过」清单，用户自己 Run 自己测。
- 清单注意事项必须包含：免费开发者签名 7 天过期，过期需在 Xcode 重新签名安装后再测。

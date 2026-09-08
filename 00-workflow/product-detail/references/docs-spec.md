# Document Spec

正式 Product Detail 必须严肃、短、可施工。

推荐：

```text
# Stage-n Product Detail

## Requirement-n — <name>

Intent:
Actor:
Trigger:
Behavior:
State / Lifecycle:
Permission / Visibility:
Failure / Recovery:
Acceptance:
Explicit Exclusions:
```

只保留适用字段。

## 写入标准

一句内容值得落袋，当它会约束至少一个：

- Stage Contract
- Blueprint
- Construction
- Verification

否则不写。

## 禁止内容

- 访谈过程
- Agent 推理过程
- 被否定方案全集
- 用户金句
- 产品愿景散文
- UI 微细节
- 技术实现方案
- 代码结构
- 无关未来功能

## 单一事实来源

项目若选择 Product Definition 内嵌 Detail，就不要再维护 Stage Detail 副本。

项目若选择 `docs/product/details/Stage-n.md`，Product Definition 只引用，不复制全文。

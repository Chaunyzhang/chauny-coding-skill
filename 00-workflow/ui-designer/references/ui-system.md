# UI System Rules

## Systemization Target

UI System 只收重复且值得统一控制的决定。

### Tokens

适合 Tokenize：
- semantic color
- typography role
- spacing scale
- radius / shape role
- control size
- surface role
- motion timing / spring family

不适合：
- 只出现一次、没有系统意义的独特布局值
- 为了“没有 raw number”强行给每个数字命名

## Hierarchy

UI 结构：

`Screen → Section → Component → Primitive`

这是设计层级，不要求一一对应文件层级。

## Screen

每个 Screen 先明确：

- purpose
- primary content
- secondary/supporting
- primary action
- fixed vs scroll
- relevant states

结构不稳时禁止过度 polish。

## Section

Section 是语义组。

Section 间 separation 通常应强于组内 spacing。

## Component

当至少两项成立时优先考虑独立 Component：

- reused
- stateful
- independently interactive
- independently styled
- independently evolving
- semantically nameable

Component boundary 表达意义，不表达“代码有几行”。

## Component API

输入应该是语义变化：

```text
style: primary | secondary | destructive
size: compact | regular | large
state: loading | disabled | selected
```

避免开放任意 styling 参数让 caller 绕过系统。

## Variant vs State

Variant = 它是哪一类。
State = 它当前怎样。

二者组合，不为每种组合造新 Component。

## Layout Ownership

每个元素必须有合理 parent ownership。

若需要大量 offset / absolute positioning 才能成立，先怀疑 ownership / structure。

## Fixed vs Flexible

通常固定：
- control size
- icon size
- avatar size
- toolbar chrome

通常自适应：
- text
- content height
- lists
- card content
- available width

不要为了截图像素一致冻结真实内容。

## Responsive

检查：
- viewport
- orientation / size class
- long text
- localization
- Dynamic Type
- device class

设计规则必须描述“关系如何变化”，而不是只描述一个尺寸。

# 识图与风格逆向

目标：从图片提取**可生成的设计系统**，不是抄坐标。

## 1. 证据等级

- **Observed**：图里直接可见/可量。
- **Resolved**：多处重复或多图一致支持的规律。
- **Unknown**：图片无法证明。

单图证据弱于多图；同一产品多页面、多状态、多 breakpoint 越多，越能推导 Design System。

## 2. 必须提取

### Structure / Hierarchy
- 页面树、Region/Section、内容顺序
- focal order、alignment axes、container strategy
- grid/column/content width、scroll clues

### Visual Math
- type roles 与近似 scale
- spacing clusters：组内/组间/page gutter
- radius family、control heights、icon sizes
- 对齐与重复几何

### Visual language
- Visual Laws
- palette roles（不是只采样 hex）
- surface/border/depth
- typography character
- icon/imagery grammar
- component grammar

### Token candidates
多处近似值优先归并为候选 token，不机械保留 7/8/9 三个值；若有证据表明不同 role，保留差异并说明。

## 3. 不得从静态图声称知道

- animation duration/easing
- hidden states
- breakpoint
- backend behavior
- state owner
- permission/lifecycle truth

这些保持 Unknown，除非有视频、代码、交互记录或 Human 说明。

## 4. Style transfer

把源图拆成：
- **Style DNA**：可迁移的 Visual Laws、type/color/shape/surface/icon/motion character。
- **Source semantics**：源产品业务结构、品牌资产、专有文案。

只迁移前者；后者由目标产品定义。

## 5. 输出

先形成简短 `Image Style Extraction Report`：Observed / Resolved / Unknown + Visual Laws + token candidates + component grammar；随后编译进 Full/Page Spec。

## Gate

如果最终只是“极简、高级、温暖”或一组截图坐标，逆向失败。

# UI Workflow Evals

目标：测试行为，而不是检查是否“提到某个词”。

## E1 — 小改不能过杀
**Input:** “把现有 primary button 背景从 A 改成 B，其他不动。”

Expected:
- 读取 Existing Spec。
- 走 Patch Spec；Preserved/Changed 清楚。
- 不重新做 Coverage/视觉方向/整页构图。
- rendered verify。

Fail:
- 重跑完整设计流程。
- 擅自改 radius/type/motion。

## E2 — Human 模糊反馈先对齐
**Input:** “这个拖进去太跳了，我想顺一点，但别飘。”

Expected:
- Agent 翻译为可观察变化、保持不变项、motion 候选、Unknown。
- Human confirm 后先改 Spec，再改代码。

Fail:
- 直接改动画试试看。
- 代码先跑，事后补 Spec。

## E3 — UI 从零，视觉必须具体
**Input:** “做一个安静、温暖、成熟，但有一点生命力的 Todo 首页。”

Expected:
- 定义 content/state/hierarchy 后再视觉。
- 输出 Visual Laws。
- 明确 Composition、type roles、spacing scale、relationship gaps、radius、surface/depth、color roles+values、icon、motion、Forbidden。
- 编译 Full/Page Spec。

Fail:
- 只输出“温暖极简”与大概方向。
- 实现 Agent 仍需自己选字号/间距/圆角。

## E4 — Visual Math 抓弱层级
**Input:** 页面使用字号 `14/18/20`；同组 gap=16，跨组 gap=20；多个同级标题左边缘差 4px。

Expected:
- 指出 type hierarchy 后两级辨识度弱，而不是机械说“必须 1.25”。
- 指出 16/20 relationship contrast 弱，建议从现有 spacing scale 拉开。
- alignment drift 作为 hard fail。

Fail:
- 因为数值都不同就判合格。
- 强制所有项目使用固定 1.25 或 1:4。

## E5 — 框套框
**Input:** section card 内再套三个无独立语义的小 card，仅为制造层次。

Expected:
- 应用“去掉内层框后关系是否仍清楚”测试。
- 优先用 spacing/type/surface 关系分组。

Fail:
- 继续加 border/shadow 修层次。

## E6 — 图片逆向不幻觉
**Input:** 单张静态 App 截图。

Expected:
- Observed/Resolved/Unknown 分离。
- 提取 structure、type/color/spacing/radius/surface/icon、Visual Laws、token candidates。
- motion/breakpoint/state owner 保持 Unknown。

Fail:
- 给出 180ms ease-out 等无证据参数。
- 抄坐标而不归纳系统。

## E7 — 多图归一 token
**Input:** 三张同产品截图里类似 gap 测得 7/8/9px。

Expected:
- 识别重复关系，优先归并为一个 token 候选（如 8），除非有证据证明 role 不同。

Fail:
- 建 7/8/9 三个 token。

## E8 — 状态组合
**Input:** Task 已完成、离线、待同步且获得 focus。

Expected:
- 支持多维状态同时成立；分别说明 owner/表现/允许动作。

Fail:
- 强行塞进单一 enum `completedOfflineFocused` 或只保留一个状态。

## E9 — 第二页不能复制扩展
**Input:** 已有 Todo Home，新做 Chat 页；两页共享 TabBar、icons，列表行/气泡可数据驱动。

Expected:
- 写代码前有 IMPLEMENTATION-STRUCTURE.md。
- TabBar/icons 共享单一来源；重复 rows/bubbles 数据驱动。
- 单用 Hero/Composer 在无独立复用/状态需求时可 local。
- 写完后结构再审计。

Fail:
- 复制 TabBar/SVG/markup，等用户提醒再抽。
- 一切皆组件。

## E10 — Drift
**Input:** Spec spacing=`8/12/16/24`，第三页出现 `15/23`；新蓝色 CTA 未在 Spec 中。

Expected:
- 15/23 判疑似 drift 并归并/解释新 role。
- 新 CTA color 必须先进入 Spec，否则阻塞交付。

Fail:
- 把近似值解释为“细致手调”。

## E11 — 实现发现新设计决定
**Input:** 实现拖拽时发现需要“失败弹回动画”，Spec 未定义。

Expected:
- 停代码；形成 Candidate Decision；必要时 Human confirm；先改 Spec 再实现。

Fail:
- 在代码里先加 spring，最后补文档。

## E12 — 纯重构不制造审批
**Input:** 抽取重复 renderer，不改变 DOM/视觉/行为。

Expected:
- 更新 IMPLEMENTATION-STRUCTURE.md；无需 Human 重新确认设计，也无需虚假 Patch Spec。

Fail:
- 把技术重构包装成视觉变更审批。

## E13 — Product UI 不为原创破坏习惯
**Input:** Dashboard 想“更有个性”。

Expected:
- 个性放在 palette/type/surface/icon/motion/density；保留熟悉的导航、表格、筛选与 form affordance。

Fail:
- 为差异化把 sidebar 放到反常位置或改掉基本表格交互。

## E14 — Rendered evidence
**Input:** 代码 lint/test 全过，但未打开 UI。

Expected:
- 不宣称完成；渲染 Relevant states/content stress/viewport 后再交付。

Fail:
- Source-only confidence。


## E15 — 规范正确但视觉秩序普通
**Input:** 一个后台用户表格：标题弱、辅助小字很多、筛选器一排 outline、头像随机多色、表格列对齐松散、所有元素视觉音量接近。

Expected:
- 不把问题简化成“换配色/加阴影”。
- 先指出 focal order、alignment、grouping、de-emphasis、container strategy、table numeric/text/status alignment。
- 能提出灰度/弱色检查和 Final Subtraction Audit。
- 随机头像色若无语义，应归并或证明其职责。
- 具体修改进入 Spec 后再实现。

Fail:
- 只调圆角、颜色、阴影。
- 用更多 Card/border 提升“设计感”。
- 保留全部辅助小字与随机颜色，理由只是“丰富”。

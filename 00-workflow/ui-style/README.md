# UI Style v2

核心：**高精度记录，选择性约束。**

- `SKILL.md`：短主流程与调度规则。
- `references/01–06`：按需读取的细节。
- `templates/`：最终 Spec 起始模板。
- `tools/spec_lint.py`：检查结构、Kernel 过载、明显的约束升级问题。
- `tools/spec_export.py`：从同源 JSON manifest 导出 token JSON。
- `tools/token_cluster.py`：辅助聚类 raw numeric measurements，不替代语义判断。
- `evals/EVALS.md`：守风格 + 留创作空间的测试集。

设计目标不是让模型变成参数执行器，而是：

> 底线锁身份，语法控方向，剩下交给模型设计。

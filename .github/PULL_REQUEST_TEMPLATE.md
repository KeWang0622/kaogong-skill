## 改动内容 What changed

<!-- 一句话说明这个 PR 做了什么 -->

## 类型 Type

- [ ] `feat` 新功能
- [ ] `fix` 修正错误的考试内容
- [ ] `docs` 文档
- [ ] `chore` / `ci` / `refactor`

## 📌 内容出处 Sources（修改考试内容时必填）

> 本项目服务真实考生，**涉及考试内容的修改必须附出处**，否则不予合并。

| 改了什么 | 依据 | 可信度 | 链接 |
|---|---|---|---|
|  |  | 🟢 官方 / 🟡 权威媒体 / 🟠 行业整理 |  |

- [ ] 🟠 行业整理来源已在正文中标注「非官方口径」
- [ ] 没有把模拟题标称为「真题」
- [ ] 涉及逐年变化的信息已提示「以当年官方公告为准」

## 自检 Checklist

- [ ] 本地跑过 `python3 scripts/validate.py`，全部通过
- [ ] 若改动了 `skills/`，已运行 `python3 scripts/build-bundle.py` 并提交 `dist/`
- [ ] 若新增了 `references/` 内容，已在 `SOURCES.md` 补充来源

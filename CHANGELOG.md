# 更新日志 Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与 [语义化版本](https://semver.org/lang/zh-CN/)。

## [2.0.0] - 2026-09-08

首个符合 [Agent Skills 开放标准](https://agentskills.io/specification) 的版本。**同一份技能现在可在 Claude Code、ChatGPT/Codex、Cursor、Gemini CLI 等 40+ 客户端使用。**

### 修复 Fixed

- **技能此前在 Linux 上无法被识别**：文件名 `skill.md` 改为规范要求的 `SKILL.md`，并移入 `skills/kaogong/` 目录（macOS 文件系统大小写不敏感，掩盖了这个问题）。
- **移除无效的 `triggers:` 字段**：Agent Skills 规范中不存在该字段，此前它完全不起作用。触发词已改写进 `description`，这才是各客户端实际用于匹配的字段。
- **README 安装命令无法执行**：`git clone .../YOUR_USERNAME/kaogong-skill.git` 中的占位符从未替换。
- **README 承诺的 6 个斜杠命令并不存在**：现已在 `commands/` 中真实实现（共 7 个）。
- **行测考试概况遗漏「行政执法类」试卷**：国考自 2022 年起为三套卷（副省级 135 题、地市级 130 题、行政执法类 130 题），此前只写了两套。
- **申论考试概况同样遗漏行政执法类卷**。
- **报考年龄已过时**：2026 年度国考起放宽至 38 周岁（应届硕博 43 周岁），此前内容仍为 35 周岁。

### 新增 Added

- `skills/kaogong/references/baokao.md` — 报考全流程：国考/省考/事业编/选调生对比、报考条件、时间线、职位选择、体检、考察、公示。
- `skills/kaogong/references/SOURCES.md` — 三级可信度标注的权威来源索引（🟢 官方 / 🟡 权威媒体 / 🟠 行业整理）与时效性声明。
- `/kaogong-baokao` 报考咨询与选岗命令。
- `dist/kaogong-compact.md` 与 `dist/kaogong-full.md` — 供 ChatGPT 自定义 GPT、豆包、Kimi 等无文件系统平台使用的单文件版本，由脚本自动生成。
- `scripts/validate.py` — Agent Skills 规范校验（frontmatter 字段、命名规则、字符上限、相对链接可达性）。
- `scripts/build-bundle.py` — 从源文件生成单文件版本，杜绝版本漂移。
- `scripts/install.sh` — 检测本机客户端并一键安装。
- `.claude-plugin/` — Claude Code 插件与市场清单，支持 `/plugin marketplace add KeWang0622/kaogong-skill`。
- GitHub Actions CI：规范校验、`dist/` 同步性检查、外链检查。
- Issue / PR 模板，其中内容类改动**强制要求填写出处与可信度等级**。
- `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`docs/INSTALL.md`、本更新日志。

### 变更 Changed

- 将 712 行的单文件 `skill.md` 拆分为精简的 `SKILL.md`（行为与路由）+ 6 个按需加载的 `references/`。**每轮对话的上下文占用大幅下降**——规范建议 `SKILL.md` 保持在 500 行以内。
- `SKILL.md` 新增「引用与可信度」一节：涉及 🟠 行业整理来源的数据（如逐模块题量、分值权重）必须声明为非官方口径。
- 强化边界声明：不得将模拟题称为真题、不得预测分数线、明确拒绝协助作弊。

### 兼容性 Compatibility

旧的根目录 `skill.md` 已移除。此前通过克隆整个仓库到 `.claude/skills/` 使用的用户，请改用 [docs/INSTALL.md](docs/INSTALL.md) 中的安装方式。

## [1.0.0] - 2026-04-06

- 首次发布：行测、申论、面试、时政、学习计划五大模块的单文件 Claude Code skill。

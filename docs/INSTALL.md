# 安装指南 Installation

本项目是一个符合 [Agent Skills 开放标准](https://agentskills.io/specification) 的技能包。**同一份 `skills/kaogong/` 目录可以在 40+ 种 AI 客户端里直接使用**，无需为每个平台维护不同版本。

---

## 一分钟安装（推荐）

```bash
git clone https://github.com/KeWang0622/kaogong-skill.git
cd kaogong-skill
./scripts/install.sh
```

脚本会检测你已安装的客户端并询问安装位置。想手动安装，见下表。

---

## 各客户端安装路径

`~/.agents/skills/` 是多家客户端共用的约定路径，**装一次，Codex / Cursor / Gemini CLI 同时可用**。

| 客户端 | 全局路径 | 项目级路径 | 官方文档 |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills/kaogong/` | `.claude/skills/kaogong/` | [docs](https://code.claude.com/docs/en/skills) |
| **ChatGPT / Codex** | `~/.agents/skills/kaogong/` | `.agents/skills/kaogong/` | [docs](https://learn.chatgpt.com/docs/build-skills) |
| **Cursor** | `~/.agents/skills/` 或 `~/.cursor/skills/` | `.agents/skills/` 或 `.cursor/skills/` | [docs](https://cursor.com/docs/context/skills) |
| **Gemini CLI** | `~/.agents/skills/` 或 `~/.gemini/skills/` | `.agents/skills/` 或 `.gemini/skills/` | [docs](https://geminicli.com/docs/cli/skills/) |
| **GitHub Copilot / VS Code** | 见官方文档 | 见官方文档 | [docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| **其他 40+ 客户端** | — | — | [agentskills.io/clients](https://agentskills.io/clients) |

手动安装示例：

```bash
mkdir -p ~/.agents/skills
cp -r skills/kaogong ~/.agents/skills/
```

装好后，直接说「我想练一道资料分析」或输入 `/kaogong` 即可激活。

---

## Claude Code 插件安装（含 7 个斜杠命令）

作为插件安装可以额外获得 `/kaogong-xingce`、`/kaogong-shenlun` 等命令：

```
/plugin marketplace add KeWang0622/kaogong-skill
/plugin install kaogong-skill@kaogong
```

---

## 没有文件系统的平台

ChatGPT 自定义 GPT、豆包、Kimi、通义等只提供「粘贴指令」输入框的平台，使用预生成的单文件版本：

| 文件 | 用途 |
|---|---|
| [`dist/kaogong-compact.md`](../dist/kaogong-compact.md) | 精简版，约 3,000 字符，适合自定义 GPT 的 8,000 字符指令框 |
| [`dist/kaogong-full.md`](../dist/kaogong-full.md) | 完整版，含全部知识库，适合长上下文对话或知识库上传 |

**自定义 GPT 用法**：把 `kaogong-compact.md` 粘进 Instructions，把 `kaogong-full.md` 作为 Knowledge 文件上传。

> 这两个文件由 `scripts/build-bundle.py` 从 `skills/kaogong/` 自动生成，CI 会校验其与源文件同步，不会出现版本漂移。

---

## 验证安装

```bash
python3 scripts/validate.py      # 校验是否符合 Agent Skills 规范
```

在客户端里问一句「行测三套卷有什么区别？」——如果答得出副省级 135 题、地市级和行政执法类 130 题，说明技能已生效。

---

## 卸载

删除对应目录即可：

```bash
rm -rf ~/.agents/skills/kaogong ~/.claude/skills/kaogong
```

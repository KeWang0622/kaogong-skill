# 安装与更新

按你实际使用的入口选择。项目免费，AI 平台本身可能收费。核对日期：2026-10-11。

## 手机或网页聊天

打开 [精简版](../dist/kaogong-compact.md)，复制正文并告诉 AI“请按这些规则辅导我”；若支持上传文件，再提供 [完整版](../dist/kaogong-full.md)。这是一种提示词体验方式，不代表已在客户端安装技能。

精简版低于本项目设置的 8,000 字符预算，只有行为规则；完整版包含参考资料。实际粘贴、文件大小和上下文限制以平台为准。不要只发 GitHub 链接并假定 AI 已读完仓库。

如果使用的环境仍提供自定义 GPT 的 Instructions / Knowledge 入口，可分别放入精简版和完整版；入口、权限与迁移安排依账户而异，见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/migrate-custom-gpts)。普通手机或网页对话不会因本地复制目录而自动安装本仓库。

## 本地技能客户端

```bash
git clone https://github.com/KeWang0622/kaogong-skill.git
cd kaogong-skill
./scripts/install.sh
```

脚本检测本地目录并询问位置；目录存在不代表已验证该客户端支持技能。也可显式指定目标，例如：

```bash
./scripts/install.sh ~/.agents/skills
```

| 客户端 | 用户技能目录 | 官方说明 |
|---|---|---|
| Codex | `~/.agents/skills/kaogong/` | [Skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `~/.claude/skills/kaogong/` | [Skills](https://code.claude.com/docs/en/skills) |
| Cursor | 依版本选择 `~/.agents/skills/` 或 `~/.cursor/skills/` | [Skills](https://cursor.com/docs/context/skills) |
| Gemini CLI | 依版本选择 `~/.agents/skills/` 或 `~/.gemini/skills/` | [Skills](https://geminicli.com/docs/cli/skills/) |
| 其他兼容客户端 | 按宿主文档安装整个 `skills/kaogong/` 目录 | [Agent Skills](https://agentskills.io/) |

Codex 可用 `$kaogong` 显式触发，也可以自然提问。其他客户端以其技能菜单与文档为准。`commands/` 是插件快捷入口，复制技能目录不保证出现这些命令。

## Claude Code 插件

```text
/plugin marketplace add KeWang0622/kaogong-skill
/plugin install kaogong-skill@kaogong
```

共 12 个命令，包括职测、综应、公基、公文与错题复盘。命令可能以插件命名空间显示，以客户端菜单为准。

## 检查是否生效

1. 在客户端技能列表确认出现 `kaogong`；必要时刷新或重启。
2. 提问：“用 kaogong 帮我练一道综应 B 类题，等我回答再批改。”
3. 观察是否按 B 类任务给材料和要求，而非重新询问国考省考、直接给出答案或声称使用内部官方评分表。

能回答一般考试常识不足以证明加载了技能。`python3 scripts/validate.py` 只检查仓库结构，也不验证客户端是否已加载。

## 更新与自定义

```bash
git pull --ff-only
./scripts/install.sh ~/.agents/skills
```

安装器更新前会保存已有 `kaogong` 目录的备份（位于技能扫描目录之外），并打印路径。更新后检查技能列表；如需恢复，将新版目录移开，再把备份内的 `kaogong` 移回目标技能目录。自定义内容应单独保存，升级不会自动合并本地修改。

网页版或自定义指令用户需要重新复制/上传新版文件，不会自动同步 GitHub。客户端联网能力不会因安装该技能而自动开启。

## 常见问题

- **GitHub 打不开**：仓库当前没有维护的镜像地址。可通过能访问仓库的设备下载再传到自己的设备；不要把未知镜像当作官方发布。
- **没有斜杠命令**：检查是否安装 Claude Code 插件；只安装技能目录请用自然语言或宿主的技能选择入口。
- **一直给答案、不等作答**：明确说明“进入练习模式，先出题”，并检查是否加载主技能。若重复发生，可按 [质量检查](QUALITY.md) 提交匿名案例。
- **缺少参考文件**：应安装整个 `skills/kaogong/`，而非只复制 `SKILL.md`；网页版使用完整版知识文件。

## 卸载

仅删除实际安装位置下的 `kaogong` 目录即可；有自定义内容或学习记录时先保留。插件通过客户端插件管理器卸载，上传的知识文件在相应平台单独移除。

<div align="center">

# 考公 AI 导师

**一道题讲明白，一份答案改具体。**

公务员 · 事业单位 · 免费开源

[![License: MIT](https://img.shields.io/badge/license-MIT-2f6f62?style=flat-square)](LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/KeWang0622/kaogong-skill/validate.yml?branch=main&style=flat-square&label=checks)](https://github.com/KeWang0622/kaogong-skill/actions/workflows/validate.yml)
[![GitHub stars](https://img.shields.io/github/stars/KeWang0622/kaogong-skill?style=flat-square&label=stars)](https://github.com/KeWang0622/kaogong-skill/stargazers)

[开始使用](#start) · [能练什么](#subjects) · [更多例子](docs/EXAMPLES.md) · [安装指南](docs/INSTALL.md) · [English](README_EN.md)

</div>

做题之后，最费劲的往往是弄清楚：为什么选错了？申论漏了哪层意思？下次遇到类似的题，应该先看哪里？

这个项目把出题、讲解、批改和复盘的流程整理成一个 **AI 技能包**。把它交给你正在用的 AI，就可以从一道题开始，接着追问、修改答案、再练一次。考国考、省考或事业编，都可以先说明自己的目标。

项目按 [Agent Skills](https://agentskills.io/) 标准组织；手机和网页用户也可以用单文件版。技能本身免费，所用 AI 平台可能收费。

## 先看一次讲题 ✍️

下面是一个根据仓库原创题编写的**交互示例**，用来说明辅导方式；不同模型的实际回答会有差异。

> **你**：给我一道职测数量题，先别告诉我答案。
>
> **导师**：某服务中心本月办理业务 660 件，比上月增长 10%。上月办理多少件？
>
> A. 594　B. 600　C. 650　D. 726
>
> **你**：A。我用 660 减去它的 10%。
>
> **导师**：应该选 B，600 件。关键在于，这个 10% 是按**上月**计算的。
>
> 设上月为 x，本月就是 x × 1.1 = 660，所以 x = 600。你减去的是 660 的 10%，把计算增长率的基数换了。
>
> 下次先找“比谁增长”，那个量才是基期。用同一组数据再试一下：本月比上月多办了多少件？

你也可以把自己的题目和思路发过来。批改申论、综应时，请一并提供题干、材料和答案，这样反馈才能对应到具体内容。

<a id="start"></a>

## 开始使用 🚀

### 手机 / 网页聊天

1. 打开 [精简版](dist/kaogong-compact.md)，复制正文发给 AI，加一句“请按这些规则辅导我”。
2. 如果支持上传文件，再上传 [完整版](dist/kaogong-full.md)，里面包含各科参考资料。
3. 说出你今天想练的内容，例如：

```text
我准备考事业单位 A 类，每天能学一小时。
今天先练一道职测判断题，等我回答后再解析。
```

只用精简版也能体验教学流程。文件上传、自定义指令等具体用法见 [安装指南](docs/INSTALL.md)。

<details>
<summary><b>Codex、Claude Code 等本地客户端</b></summary>

在终端运行：

```bash
git clone https://github.com/KeWang0622/kaogong-skill.git
cd kaogong-skill
./scripts/install.sh
```

按提示选择安装位置。Codex 也可以直接指定：

```bash
./scripts/install.sh ~/.agents/skills
```

安装后用自然语言提问，或在 Codex 中输入 `$kaogong`。更多客户端路径、更新与卸载方式见 [安装指南](docs/INSTALL.md)。

</details>

<details>
<summary><b>Claude Code 插件安装</b></summary>

在 Claude Code 中运行：

```text
/plugin marketplace add KeWang0622/kaogong-skill
/plugin install kaogong-skill@kaogong
```

插件带有 12 个快捷命令，见 [命令速查](docs/COMMANDS.md)。命令可能带插件命名空间，以客户端菜单为准。

</details>

<a id="subjects"></a>

## 能练什么

| 你的目标 | 可以一起练 |
|---|---|
| **公务员笔试** | 行测六个部分；申论概括、分析、对策、应用文与议论文 |
| **事业单位笔试** | 职测、综应 A—E 分类训练；按当地大纲练公共基础知识 |
| **公文专项** | 请示与报告等文种辨析、行文规则、格式改错、材料写作 |
| **面试** | 结构化题目、作答点评、参考框架，再练一遍 |
| **报考与时政** | 一起读目标公告、核对条件，把政策和新闻放回考试情境 |
| **日常复习** | 按可用时间排计划，整理错题，导出下次继续用的学习卡 |

事业单位各地考法不同，最好带上**地区、年份、科目和岗位类别**。暂时不知道也没关系，可以先问：“我想考事业编，职测、综应、公基有什么区别？”

新加入的职测、综应、公基和公文模块，来自读者的建议。完整改动见 [更新日志](CHANGELOG.md)。

## 除了刷题，还可以这样用

**一份答案，改到具体的句子。**

```text
这是申论题干、材料和我的答案。
请指出哪些要点有材料依据，哪些遗漏了，最后让我重写最需要改的一段。
```

**一道错题，练到换个问法也会做。**

```text
刚才这题我把同比和环比弄混了。
帮我对比一下，再出一道换了数据的题，不要直接给答案。
```

**一天一小时，也要留出复盘时间。**

```text
我在职备考，距离考试 45 天，每天只有 60 分钟。
考公基和写作，请先安排第一周，把练习和复盘都算进去。
```

[查看公文改错、综应训练和学习卡示例 →](docs/EXAMPLES.md)

## 关于答案和分数

考试信息值得认真对待。项目把考纲、制度文件和教学建议分开整理，方便你核对。

- **看出处。** 涉及科目、资格和政策，尽量回到目标考试的官方文件；[来源索引](skills/kaogong/references/SOURCES.md)记录版本和适用范围。最新信息需要联网核验，离线时应明确说明。
- **看材料。** 批改要说明答案对应了哪些材料要点。自拟量表会标为“训练评分”，不能当作正式考试得分。
- **看得出问题，就提出来。** 模拟题会要求 AI 自检，但它仍可能算错或出歧义题。[提交纠错](https://github.com/KeWang0622/kaogong-skill/issues/new?template=content-error.yml)时，附上题目和疑点就很有帮助。

<details>
<summary>其他使用说明</summary>

本项目与考试主管部门无关，不保证提分或录用。报名、考试与录用要求以官方公告为准。D/E 类综应提供分类入口和训练方法，专业内容还需结合相应教材核验。

学习卡可以复制保存；跨对话继续时请带回记录。当前没有云端学习账户、自动提醒或进度同步。各 AI 客户端的加载、联网和文件能力有所不同，实际效果需要在自己的环境中确认。

</details>

## 一起把它改好 🤝

职测、综应、公基、公文，就是从“能不能再加上这些”开始的。欢迎继续告诉我们，哪道题没讲清楚，哪份答案改得不对，哪个地方的考纲还缺着。

**不用会写代码。** 你可以 [报一个错](https://github.com/KeWang0622/kaogong-skill/issues/new?template=content-error.yml)、[提一个需求](https://github.com/KeWang0622/kaogong-skill/issues/new?template=feature.yml)，也可以直接修改文档。提交时记得去掉姓名、电话和准考证号等个人信息。

想贡献题目或代码，先看 [贡献指南](CONTRIBUTING.md)。近期优先补充经过审校的原创题、地方考纲，以及 D/E 类专业内容审校。

<details>
<summary>项目结构与本地检查</summary>

| 路径 | 内容 |
|---|---|
| [`skills/kaogong/SKILL.md`](skills/kaogong/SKILL.md) | 主技能：教学流程与知识路由 |
| [`skills/kaogong/references/`](skills/kaogong/references/) | 各科参考资料与来源 |
| [`commands/`](commands/) | Claude Code 插件命令 |
| [`dist/`](dist/) | 自动生成的精简版和完整版 |
| [`scripts/`](scripts/) · [`tests/`](tests/) | 安装、构建与检查 |

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/build-bundle.py
bash -n scripts/install.sh
```

自动检查验证文件与打包；实际教学行为的验收场景见 [质量检查](docs/QUALITY.md)。

</details>

如果它帮你弄懂了一道题，欢迎把这个仓库分享给一起备考的人。也欢迎点个 ⭐，回来时更容易找到。

---

[MIT License](LICENSE) · [更新日志](CHANGELOG.md) · [English](README_EN.md)

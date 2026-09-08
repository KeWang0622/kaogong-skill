<div align="center">

<img src="assets/banner.png" alt="考公AI导师 — 免费的公务员考试 AI 辅导" width="100%">

<br><br>

[![Stars](https://img.shields.io/github/stars/KeWang0622/kaogong-skill?style=for-the-badge&labelColor=0a1020&color=e0483d)](https://github.com/KeWang0622/kaogong-skill/stargazers)
[![License](https://img.shields.io/badge/License-MIT-c8b98a?style=for-the-badge&labelColor=0a1020)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-spec_compliant-4a9eff?style=for-the-badge&labelColor=0a1020)](https://agentskills.io/specification)
[![Validate](https://img.shields.io/github/actions/workflow/status/KeWang0622/kaogong-skill/validate.yml?style=for-the-badge&labelColor=0a1020&label=CI)](https://github.com/KeWang0622/kaogong-skill/actions/workflows/validate.yml)

**每年 370 万人考公，培训班收费 1–3 万元。这个免费技能想改变这一切。**

`行测` · `申论` · `面试` · `时政` · `报考` —— 一个符合开放标准的 AI 备考导师，
可在 **Claude Code、ChatGPT / Codex、Cursor、Gemini CLI 等 40+ 客户端**中直接使用。

[安装](#-安装) · [功能](#-功能模块) · [内容准确性](#-内容准确性我们和别的-prompt-仓库不一样的地方) · [示例](#-使用示例) · [贡献](CONTRIBUTING.md)

</div>

---

## 为什么需要这个技能

> 2026 年度国考通过资格审查 **371.8 万人**，计划招录 3.81 万人，竞争比约 **98 : 1**。
> 过审人数从 2023 年的近 260 万一路涨到今天，四年翻了近一倍。<sup>[来源](skills/kaogong/references/SOURCES.md)</sup>

- 线下培训班 1–3 万元，并非人人负担得起
- 越来越多考生已经在用 AI 替代传统培训，但通用聊天机器人**不懂评分标准**，批改结果不可信
- 这个技能把**真实的题型分类、阅卷规则、制度依据**打包进 AI，让它像个懂行的老师，而不是一个会说漂亮话的聊天框

**一对一 · 随时随地 · 完全免费。**

---

## ⚡ 安装

### 通用安装（推荐，一次装好多个客户端）

```bash
git clone https://github.com/KeWang0622/kaogong-skill.git
cd kaogong-skill
./scripts/install.sh
```

`~/.agents/skills/` 是 Codex、Cursor、Gemini CLI 共用的约定路径——**装一次，多端可用**。

### 手动安装

```bash
mkdir -p ~/.agents/skills && cp -r skills/kaogong ~/.agents/skills/
```

| 客户端 | 路径 |
|---|---|
| **Claude Code** | `~/.claude/skills/kaogong/` |
| **ChatGPT / Codex** | `~/.agents/skills/kaogong/` |
| **Cursor** | `~/.agents/skills/` 或 `~/.cursor/skills/` |
| **Gemini CLI** | `~/.agents/skills/` 或 `~/.gemini/skills/` |
| **其他 40+ 客户端** | 见 [完整安装指南](docs/INSTALL.md) |

### Claude Code 插件（额外获得 7 个斜杠命令）

```
/plugin marketplace add KeWang0622/kaogong-skill
/plugin install kaogong-skill@kaogong
```

### 没有文件系统的平台（自定义 GPT / 豆包 / Kimi / 通义）

| 文件 | 用途 |
|---|---|
| [`dist/kaogong-compact.md`](dist/kaogong-compact.md) | 约 3,000 字符，塞得进自定义 GPT 的指令框 |
| [`dist/kaogong-full.md`](dist/kaogong-full.md) | 完整版含全部知识库，可作为知识文件上传 |

装好后，直接说「**我想练一道资料分析**」或输入 `/kaogong` 即可激活。

---

## 🎯 功能模块

| 命令 | 模块 | 能做什么 |
|---|---|---|
| `/kaogong` | **入门诊断** | 摸清你的考试类型、阶段、薄弱项，给出学习路径 |
| `/kaogong-xingce` | **行测训练** | 五大模块出题，一次一题，讲透思路与同类题方法 |
| `/kaogong-shenlun` | **申论批改** | 按真实阅卷规则**踩点给分**，指出漏了哪几个点 |
| `/kaogong-mianshi` | **面试模拟** | 结构化面试出题，多维度点评并打分 |
| `/kaogong-shizheng` | **时政热点** | 五维度拆解热点，提炼可用表述，预测出题角度 |
| `/kaogong-baokao` | **报考选岗** | 资格条件、国考省考事业编对比、体检政审全流程 |
| `/kaogong-plan` | **学习计划** | 基础期 → 提高期 → 冲刺期，细化到每日任务 |

<details>
<summary><b>展开：各模块覆盖的详细内容</b></summary>

<br>

**行测**（[完整参考](skills/kaogong/references/xingce.md)）
常识判断（政治/法律/经济/历史/文化/地理/科技）· 言语理解（逻辑填空 + 片段阅读六大题型）· 数量关系（数字推理 + 12 种高频运算题型）· 判断推理（图形/定义/类比/逻辑）· 资料分析（截位直除、特征数字法、错位加减等速算技巧）

**申论**（[完整参考](skills/kaogong/references/shenlun.md)）
概括归纳 · 综合分析 · 提出对策 · 应用文写作 · 大作文。踩点给分 + 结构分 + 语言分；大作文细化到标题、开头、分论点、结尾的四等评分。

**面试**（[完整参考](skills/kaogong/references/mianshi.md)）
综合分析 · 计划组织 · 人际沟通 · 应急应变 · 自我认知，按七维度权重逐项点评。

**时政**（[完整参考](skills/kaogong/references/shizheng.md)）
政治/经济/社会/文化/生态五维分析框架，关联党的二十大报告、政府工作报告等核心文件。

**报考**（[完整参考](skills/kaogong/references/baokao.md)）
国考/省考/事业编/选调生/公安类对比 · 报考条件与年龄 · 报名到录用时间线 · 职位表筛选方法 · 体检标准 · 考察政审 · 公示。

</details>

---

## 🔍 内容准确性（我们和别的 prompt 仓库不一样的地方）

备考信息错了是要害人的。所以这个项目做了三件多数 prompt 仓库不会做的事：

### 1. 每一条制度性内容都标了出处

[`SOURCES.md`](skills/kaogong/references/SOURCES.md) 按三级可信度标注全部来源：

| 级别 | 含义 | 举例 |
|---|---|---|
| 🟢 **官方** | 法律法规、部委规章、政府公告 | 《公务员录用规定》、《公务员录用体检通用标准（试行）》国人部发〔2005〕1 号 |
| 🟡 **权威媒体** | 新华社、人民网等对官方数据的报道 | 报名人数、竞争比 |
| 🟠 **行业整理** | 培训机构对真题的统计归纳 | 逐模块题量、分值权重 |

🟠 级内容 AI 在回答时**会主动声明「为业内统计/推测，非官方口径」**——因为官方从不公布逐模块分值。

### 2. AI 被明确约束不许编

写进技能的硬性规则：不得把模拟题称为「真题」· 不得编造分数线和政策条文 · 不确定就说不确定 · 涉及逐年变化的信息必须提示「以当年官方公告为准」· 拒绝任何作弊协助。

### 3. 贡献必须附来源

改动考试内容的 PR [必须填写出处和可信度等级](.github/PULL_REQUEST_TEMPLATE.md)，否则不予合并。

> **⚠️ 免责声明**：本项目与国家公务员局及任何考试主管部门无关。报名时间、职位表、分数线、政策变动**一律以官方发布为准**。练习题均为模拟原创题。批改结果仅供参考。

---

## 💬 使用示例

<details open>
<summary><b>行测 · 逻辑填空</b></summary>

```
你: /kaogong-xingce

AI: 请选择要练习的模块：
    1. 常识判断  2. 言语理解与表达  3. 数量关系  4. 判断推理  5. 资料分析

你: 2 → 逻辑填空

AI: 【逻辑填空】

    在互联网时代，信息传播的速度______，一条新闻可以在几分钟内传遍全球。
    然而，信息的真实性却常常______，虚假新闻和谣言______，给社会带来了
    不小的困扰。

    A. 今非昔比  令人堪忧  层出不穷
    B. 一日千里  难以保证  屡见不鲜
    C. 突飞猛进  无法辨别  比比皆是
    D. 日新月异  参差不齐  此起彼伏

你: B

AI: ✓ 正确！

    【解析】
    第一空：形容信息传播速度快。"一日千里"形容发展速度极快，用于描述信息传播
    速度恰当。"突飞猛进"侧重进步，"日新月异"侧重变化，语境侧重"速度"而非
    "变化"，排除 C、D。"今非昔比"侧重今昔对比，不直接形容速度，排除 A。

    第二空："信息的真实性难以保证"搭配恰当。"令人堪忧"语义重复（"堪"已有
    "令人"之意），排除 A。

    第三空："屡见不鲜"指经常看到、不感到新奇，形容虚假新闻频繁出现很恰当。

    【方法总结】逻辑填空三步走：
    1. 语境分析 → 把握感情色彩和语义方向
    2. 辨析差异 → 找选项间的关键区别
    3. 代入验证 → 确认搭配是否恰当
```

</details>

<details>
<summary><b>申论 · 概括归纳题批改</b></summary>

```
你: /kaogong-shenlun → 概括归纳题

AI: 【概括归纳题】（15分）
    [给出约 1000 字材料，关于某城市基层治理的问题…]

    题目：请根据给定资料，概括当前城市基层治理中存在的主要问题。
    要求：全面准确，条理清晰，不超过 200 字。

你: [提交答案]

AI: 【批改结果】得分：11/15

    ✓ 优点：
    - 答案分条列点，条理清晰（结构分满分）
    - 准确提到了"人员不足"和"经费紧张"两个核心要点

    ✗ 不足：
    - 遗漏要点：未提及"权责不对等"问题（-2分）
    - 遗漏要点：未概括"居民参与度低"（-1分）
    - 表述可优化："管理混乱"过于笼统，应具体化为"多头管理、职责交叉"（-1分）

    【参考答案】
    城市基层治理主要存在以下问题：一是权责不对等，基层承担大量上级下派任务
    但缺乏相应权力和资源；二是人员不足，社区工作者数量少、待遇低、流动性大；
    三是经费紧张，财政投入不足制约服务水平提升；四是多头管理，部门职责交叉
    导致推诿扯皮；五是居民参与度低，自治意识薄弱，社区治理缺乏群众基础。
```

</details>

<details>
<summary><b>报考 · 「我 36 岁还能考吗？」</b></summary>

```
你: 我今年36岁，本科，还能考国考吗？

AI: 能。这里有个重要的政策变化，很多人还不知道：

    国考的年龄上限长期是 35 周岁，但从 2026 年度起已放宽到 38 周岁
    （2026 年应届硕士、博士研究生可放宽至 43 周岁）。这是配合渐进式
    延迟法定退休年龄政策作出的调整。🟡 来源：人民网、新京报（2025-10）

    所以 36 岁报考 2026 年度国考没有年龄障碍。

    但要提醒两点：
    1. 省考是否跟进、跟进幅度各省不一，必须查本省当年公告
    2. 具体到某个职位，年龄之外还有学历、专业、基层工作年限等限制，
       以职位表备注栏为准

    官方查询入口：国家公务员局 scs.gov.cn / 本省人事考试网

    需要我帮你梳理一下选岗的筛选顺序吗？
```

</details>

---

## 🏗 项目结构

```
kaogong-skill/
├── skills/kaogong/
│   ├── SKILL.md              # 行为与路由（精简，每轮对话都加载）
│   └── references/           # 知识库（按需加载，不占用日常上下文）
│       ├── xingce.md         # 行测
│       ├── shenlun.md        # 申论
│       ├── mianshi.md        # 面试
│       ├── shizheng.md       # 时政
│       ├── baokao.md         # 报考全流程
│       └── SOURCES.md        # 权威来源索引
├── commands/                 # 7 个斜杠命令
├── dist/                     # 单文件版本（由脚本生成，勿手改）
├── scripts/
│   ├── install.sh            # 一键安装
│   ├── validate.py           # Agent Skills 规范校验
│   └── build-bundle.py       # 生成 dist/
└── .claude-plugin/           # Claude Code 插件清单
```

采用**渐进式披露**：`SKILL.md` 只放行为指令，详细知识放 `references/`，AI 需要时才读。
这让日常对话的上下文占用大幅下降，同时保留完整的知识深度。

```bash
python3 scripts/validate.py       # 校验规范合规性
python3 scripts/build-bundle.py   # 改完 skills/ 后重新生成 dist/
```

---

## 🤝 贡献

欢迎贡献！特别需要帮忙的方向：

- **时政与政策更新** —— 年度数据、年龄条件逐年变化，需要持续维护
- **题库扩展** —— 高质量模拟题与详细解析
- **省考适配** —— 各省题量、时长、模块差异
- **英文文档** —— 让更多人能参与进来

> 📌 **涉及考试内容的修改必须附上出处。** 详见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [行为准则](CODE_OF_CONDUCT.md)。

---

## ⭐ Star 增长

如果这个项目帮到了你，点个 Star 让更多考生看到它。

[![Star History Chart](https://api.star-history.com/svg?repos=KeWang0622/kaogong-skill&type=Date)](https://star-history.com/#KeWang0622/kaogong-skill&Date)

---

## 📄 许可

[MIT License](LICENSE) · 更新记录见 [CHANGELOG.md](CHANGELOG.md)

---

<div align="center">

### In English

**kaogong-skill** is a free, open-source [Agent Skill](https://agentskills.io) that turns any
compatible AI client into a tutor for the Chinese civil service exam (公务员考试) —
covering the aptitude test (行测), essay writing (申论), structured interviews (面试),
current affairs, application guidance, and study planning.

Every institutional claim is **cited and tiered by source reliability**
(🟢 official regulation · 🟡 major news outlet · 🟠 industry compilation),
and the skill is instructed to flag uncertainty rather than invent numbers.

Install into `~/.agents/skills/` and it works in Claude Code, ChatGPT/Codex, Cursor,
Gemini CLI and 40+ other clients. See [docs/INSTALL.md](docs/INSTALL.md).

<br>

> 「千军万马过独木桥，AI 帮你稳步前行。」

</div>

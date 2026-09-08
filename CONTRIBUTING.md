# 贡献指南 Contributing

感谢你愿意让这个项目变得更好。本项目服务的是**正在备考的真实考生**，因此对内容准确性的要求高于一般开源项目。

---

## 🔴 最重要的一条规则

> **涉及考试内容的修改，必须附上出处。没有出处的内容不予合并。**

出处按可信度分三级（与 [`skills/kaogong/references/SOURCES.md`](skills/kaogong/references/SOURCES.md) 一致）：

| 级别 | 含义 | 举例 |
|---|---|---|
| 🟢 **官方** | 法律法规、部委规章、政府网站公告 | 《公务员录用规定》、国家公务员局公告 |
| 🟡 **权威媒体** | 新华社、人民网、中国青年报等对官方数据的报道 | 报名人数、竞争比 |
| 🟠 **行业整理** | 培训机构对历年真题的统计归纳 | 逐模块题量、分值权重推测 |

提交 PR 时请在描述里写清楚：**改了什么 → 依据是什么 → 链接**。🟠 级来源必须在正文中标注「为业内统计/推测，非官方口径」。

**绝对不要提交：**

- 声称是「真题」的题目（本项目只收录**模拟原创题**）
- 无法给出出处的分数线、职位表、政策条文
- 任何协助考试作弊的内容

---

## 可以帮忙的方向

| 方向 | 说明 |
|---|---|
| **时政更新** | `references/shizheng.md` 与 `SOURCES.md` 中的年度数据需要逐年维护 |
| **政策校验** | 年龄、学历、报考条件逐年变化，欢迎核对并更新 |
| **题库扩展** | 补充高质量模拟题与详细解析 |
| **省考适配** | 各省题量、时长、模块差异的差异化补充 |
| **翻译与国际化** | README / 文档的英文版维护 |
| **交互优化** | 改进 `SKILL.md` 的流程与提示词 |

---

## 开发流程

```bash
# 1. Fork 并克隆
git clone https://github.com/<你的用户名>/kaogong-skill.git
cd kaogong-skill

# 2. 创建分支
git checkout -b feat/your-feature

# 3. 修改后本地校验（无需安装依赖，只要 Python 3.9+）
python3 scripts/validate.py

# 4. 若改动了 skills/ 下的内容，重新生成单文件版本
python3 scripts/build-bundle.py

# 5. 提交并推送
git commit -m "docs: 更新 2027 国考报名数据"
git push -u origin feat/your-feature
```

然后在 GitHub 上创建 Pull Request。

### 提交信息规范

采用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>: <描述>
```

类型：`feat`（新功能）、`fix`（修正错误内容）、`docs`（文档）、`refactor`、`chore`、`ci`。

---

## 项目结构约定

```
skills/kaogong/
├── SKILL.md            # 行为与路由，保持精简（< 500 行，规范建议）
└── references/         # 详细知识库，按需加载
```

- **`SKILL.md` 只写"怎么做"**：角色、原则、流程、路由。
- **`references/` 只写"是什么"**：题型、评分标准、制度规定。
- 新增知识请优先放进 `references/`，而不是让 `SKILL.md` 变长——它每轮对话都会占用上下文。
- 修改 `references/` 后，记得在 `SOURCES.md` 补充对应来源。

CI 会自动校验 Agent Skills 规范合规性（frontmatter 字段、命名规则、相对链接是否有效）。

---

## 行为准则

参与本项目即表示你同意遵守 [行为准则](CODE_OF_CONDUCT.md)。

## 许可

提交的贡献将以 [MIT License](LICENSE) 授权。

<div align="center">

# Kaogong AI Tutor

**Work through a question. Understand the mistake. Try again.**

An open-source study skill for Chinese civil service and public institution exams.

[![License: MIT](https://img.shields.io/badge/license-MIT-2f6f62?style=flat-square)](LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/KeWang0622/kaogong-skill/validate.yml?branch=main&style=flat-square&label=checks)](https://github.com/KeWang0622/kaogong-skill/actions/workflows/validate.yml)

[简体中文](README.md) · [Get started](#get-started) · [Examples](docs/EXAMPLES.md) · [Star History](#star-history) · [Contribute](CONTRIBUTING.md)

</div>

Knowing the right answer is only part of exam preparation. The useful follow-up is often more specific: which condition did you miss, which point did your essay leave out, and what should you try next?

**kaogong-skill** gives an AI assistant a study workflow: ask a question, wait for your answer, explain the reasoning, and follow up on mistakes. It includes subject references, original practice examples, and guidance for checking official sources. Tutoring defaults to Chinese; the skill can respond in English while preserving Chinese exam terminology.

The project follows the [Agent Skills](https://agentskills.io/) standard. Portable Markdown files are available for chat interfaces. The project is free; your AI provider may charge for usage.

## A small example ✍️

*An illustrative exchange based on an original practice question in this repository. It is not a recorded model evaluation.*

> **You:** Give me a quantitative reasoning question. Wait for my answer.
>
> **Tutor:** A service center handled 660 requests this month, 10% more than last month. How many did it handle last month?
>
> **You:** 594. I subtracted 10% of 660.
>
> **Tutor:** The answer is 600. The 10% increase is measured against last month's total. So x × 1.1 = 660, giving x = 600. Multiplying 660 by 0.9 changes the base of the percentage.
>
> Try a follow-up: how many more requests did the center handle this month?

See [more examples in Chinese](docs/EXAMPLES.md), including official-document correction, applied writing, and a study card you can bring to your next conversation.

## Get started

### In a chat interface

Copy the [compact instructions](dist/kaogong-compact.md) into your AI conversation and ask it to follow them. If the interface supports file uploads, also provide the [full reference bundle](dist/kaogong-full.md).

Then describe your goal:

```text
我准备考事业单位 A 类，每天能学一小时。
今天先练一道职测判断题，等我回答后再解析。
```

The compact file contains the workflow; the full file adds subject references. File handling and context limits depend on your client.

### In a local skill client

```bash
git clone https://github.com/KeWang0622/kaogong-skill.git
cd kaogong-skill
./scripts/install.sh
```

For Codex, you can specify the destination:

```bash
./scripts/install.sh ~/.agents/skills
```

Ask naturally or invoke `$kaogong` in Codex. See the [installation guide in Chinese](docs/INSTALL.md) for other clients, updates, and troubleshooting.

<details>
<summary>Claude Code plugin</summary>

```text
/plugin marketplace add KeWang0622/kaogong-skill
/plugin install kaogong-skill@kaogong
```

The plugin provides 12 shortcut commands. See the [command reference](docs/COMMANDS.md); your client may display them with a plugin namespace.

</details>

## Subjects

| Area | Coverage |
|---|---|
| Civil service written exams | 行测 aptitude tests and 申论 material-based writing |
| Public institution written exams | 职测 aptitude tests, 综应 applied tasks by A–E category, and local 公基 public knowledge syllabuses |
| Official-document exam tasks | Document types, correspondence rules, error correction, and writing |
| Interviews | Structured questions, feedback, and a second attempt |
| Planning and review | Study schedules, mistake analysis, follow-up exercises, and portable study cards |
| Applications and current affairs | Reading official notices and connecting verified policy material to exam tasks |

Specify the region, year, subject, and position category when you know them. Local recruitment exams differ; the skill should check the target notice before choosing a syllabus.

## Sources and scores

Official facts, teaching advice, and original practice are labeled separately. The [source index](skills/kaogong/references/SOURCES.md) records document versions and scope. Current policies require verification; an offline assistant should state what it has not checked.

Writing feedback uses the supplied material and an identified rubric. Project-designed rubrics are **training estimates**, not official marking schemes or score predictions. AI-generated questions can still contain errors. Please [report a content issue](https://github.com/KeWang0622/kaogong-skill/issues/new?template=content-error.yml) with the relevant question and your concern.

The project is not affiliated with examination authorities. It does not guarantee results or replace specialist textbooks for teaching and medical posts. Study records can be copied into a future conversation; cloud accounts, progress sync, and automatic reminders are not provided.

## Contribute 🤝

The aptitude, applied writing, public knowledge, and official-document modules grew out of reader suggestions. Useful contributions include a confusing explanation, a changed local syllabus, or a carefully checked original question.

You do not need to write code. Open an [issue](https://github.com/KeWang0622/kaogong-skill/issues) or follow the [contribution guide](CONTRIBUTING.md). Remove personal information before sharing examples. Source citations are required for institutional claims; original exercises and training rubrics should be labeled as project work.

The skill lives in [`skills/kaogong/`](skills/kaogong/); [`dist/`](dist/) is generated from it. Maintainer checks and pending behavioral acceptance cases are documented in [QUALITY.md](docs/QUALITY.md).

<a id="star-history"></a>

## Star History ⭐

Thanks to everyone who has starred, shared, or improved the project. Click the chart to explore its growth.

<div align="center">
  <a href="https://www.star-history.com/?repos=KeWang0622%2Fkaogong-skill&amp;type=date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=KeWang0622/kaogong-skill&amp;type=Date&amp;theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=KeWang0622/kaogong-skill&amp;type=Date" />
      <img alt="GitHub star history for Kaogong AI Tutor" src="https://api.star-history.com/svg?repos=KeWang0622/kaogong-skill&amp;type=Date" width="800" />
    </picture>
  </a>
</div>

---

[MIT License](LICENSE) · [Changelog](CHANGELOG.md) · [简体中文](README.md)

#!/usr/bin/env python3
"""Generate single-file portable builds from the canonical skill.

Some platforms (ChatGPT Custom GPTs, 豆包/Kimi/通义 web, any "paste a system
prompt" box) cannot read a skill directory. This script flattens
skills/kaogong/ into standalone Markdown so those platforms stay in sync with
the source of truth instead of drifting from a hand-maintained copy.

Outputs:
  dist/kaogong-full.md     — SKILL.md + every reference inlined (long context)
  dist/kaogong-compact.md  — instructions only, fits an 8,000-character box

Run after editing anything under skills/. CI verifies dist/ is up to date.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "kaogong"
DIST = ROOT / "dist"
REPO = "https://github.com/KeWang0622/kaogong-skill"

# Order matters: routing first, then knowledge, sources last.
REFERENCE_ORDER = ["xingce", "shenlun", "mianshi", "shizheng", "baokao", "SOURCES"]
SECTION_NAMES = {
    "xingce": "行测",
    "shenlun": "申论",
    "mianshi": "面试",
    "shizheng": "时政热点",
    "baokao": "报考全流程",
    "SOURCES": "参考来源",
}
CUSTOM_GPT_LIMIT = 8000

# [`references/xingce.md`](references/xingce.md) -> capture the stem once
REF_LINK = re.compile(r"\[`references/(\w+)\.md`\]\(references/\1\.md\)")
# The whole "先读 <link>，然后：" lead-in, which only makes sense with real files
READ_FIRST = re.compile(r"先读 " + REF_LINK.pattern + r"，然后[：:]?\s*")


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 3)
    return text if end == -1 else text[end + 5 :].lstrip()


def absolutize(text: str, base: Path) -> str:
    """Rewrite surviving relative links to absolute repo URLs.

    Once references are inlined into one file, a path like ../../../CONTRIBUTING.md
    no longer resolves, so point it back at the repository instead.
    """

    def repl(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        path, _, anchor = target.partition("#")
        resolved = (base / path).resolve()
        try:
            rel = resolved.relative_to(ROOT)
        except ValueError:
            return label  # outside the repo: drop the link, keep the text
        url = f"{REPO}/blob/main/{rel.as_posix()}"
        return f"[{match.group(1)[1:-1]}]({url}{'#' + anchor if anchor else ''})"

    return re.sub(r"(\[[^\]]*\])\(([^)]+)\)", repl, text)


def header(title: str) -> str:
    return (
        f"<!-- 自动生成，请勿直接编辑。源文件：skills/kaogong/ -->\n"
        f"<!-- Generated file — edit skills/kaogong/ instead. -->\n"
        f"<!-- Source: {REPO} -->\n\n"
        f"# {title}\n\n"
    )


def build_full() -> str:
    body = strip_frontmatter((SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))
    # Once inlined there are no separate files, so point at the sections below.
    body = READ_FIRST.sub(lambda m: f"参考下方《{SECTION_NAMES[m.group(1)]}》章节，然后：\n\n", body)
    body = REF_LINK.sub(lambda m: f"《{SECTION_NAMES[m.group(1)]}》章节", body)
    body = absolutize(body, SKILL_DIR)
    parts = [header("考公AI导师 — 完整单文件版"), body, "\n\n"]
    for stem in REFERENCE_ORDER:
        path = SKILL_DIR / "references" / f"{stem}.md"
        if not path.exists():
            print(f"warning: missing reference {path.name}", file=sys.stderr)
            continue
        content = path.read_text(encoding="utf-8")
        content = content.split("\n> 返回 [SKILL.md]")[0].rstrip()
        # Cross-references between inlined files become section pointers.
        content = re.sub(
            r"\[([^\]]*)\]\((\w+)\.md\)",
            lambda m: f"《{SECTION_NAMES.get(m.group(2), m.group(1))}》章节",
            content,
        )
        content = absolutize(content, path.parent)
        parts.append(f"\n---\n\n{content}\n")
    return "".join(parts).rstrip() + "\n"



def build_compact() -> str:
    body = strip_frontmatter((SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))
    # Drop the routing table: there are no separate files to route to here.
    if "## 知识库路由" in body and "## 六种工作模式" in body:
        head, _, rest = body.partition("## 知识库路由")
        body = head + "## 六种工作模式" + rest.partition("## 六种工作模式")[2]
    # No knowledge base ships with the compact build, so drop the "read X first"
    # lead-ins entirely rather than pointing at files that are not there.
    body = READ_FIRST.sub("执行以下流程：\n\n", body)
    body = REF_LINK.sub(lambda m: f"《{SECTION_NAMES[m.group(1)]}》", body)
    body = absolutize(body, SKILL_DIR)
    note = (
        "> **精简版说明**：本文件只包含行为指令，不含详细知识库（题型详解、评分标准、"
        "制度依据）。需要完整版请使用 [`kaogong-full.md`](kaogong-full.md)。\n\n"
    )
    return header("考公AI导师 — 精简版（可粘贴进 Custom GPT 指令框）") + note + body


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}  {len(content):,} chars, {len(content.splitlines()):,} lines")


def main() -> int:
    print("Building portable bundles…")
    write(DIST / "kaogong-full.md", build_full())

    compact = build_compact()
    write(DIST / "kaogong-compact.md", compact)
    if len(compact) > CUSTOM_GPT_LIMIT:
        print(
            f"\n✗ kaogong-compact.md is {len(compact):,} chars, over the "
            f"{CUSTOM_GPT_LIMIT:,}-character Custom GPT instruction limit. "
            f"Trim SKILL.md or move detail into references/.",
            file=sys.stderr,
        )
        return 1
    print(f"\n✓ compact build fits Custom GPT ({len(compact):,} / {CUSTOM_GPT_LIMIT:,} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

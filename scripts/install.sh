#!/usr/bin/env bash
# Install the kaogong skill into a local AI client.
# Usage: ./scripts/install.sh [target-directory]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$REPO_ROOT/skills/kaogong"

if [[ ! -f "$SOURCE/SKILL.md" ]]; then
  echo "error: $SOURCE/SKILL.md not found — run this from a full clone of the repo." >&2
  exit 1
fi

# ~/.agents/skills is the shared convention for Codex, Cursor and Gemini CLI.
declare -a CANDIDATES=(
  "$HOME/.agents/skills:Codex / Cursor / Gemini CLI (shared convention)"
  "$HOME/.claude/skills:Claude Code"
  "$HOME/.cursor/skills:Cursor (legacy path)"
  "$HOME/.gemini/skills:Gemini CLI (legacy path)"
)

install_to() {
  local dest="$1"
  mkdir -p "$dest"
  rm -rf "${dest:?}/kaogong"
  cp -R "$SOURCE" "$dest/kaogong"
  echo "  ✓ installed to $dest/kaogong"
}

if [[ $# -ge 1 ]]; then
  install_to "$1"
  echo "Done. Say 「我想练一道资料分析」 or type /kaogong to activate."
  exit 0
fi

echo "考公AI导师 — installer"
echo

selected=0
for entry in "${CANDIDATES[@]}"; do
  dir="${entry%%:*}"
  label="${entry#*:}"
  parent="$(dirname "$dir")"
  # Only offer clients that are actually present on this machine.
  [[ -d "$parent" ]] || continue
  read -r -p "Install for $label? [y/N] " reply < /dev/tty
  if [[ "$reply" =~ ^[Yy]$ ]]; then
    install_to "$dir"
    selected=1
  fi
done

if [[ $selected -eq 0 ]]; then
  echo
  echo "No client directory detected or selected."
  echo "Install manually with:  ./scripts/install.sh ~/.agents/skills"
  exit 0
fi

echo
echo "Done. Say 「我想练一道资料分析」 or type /kaogong to activate."

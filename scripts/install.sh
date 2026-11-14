#!/usr/bin/env bash
# Copia skills e agentes da esteira para um projeto, no formato da plataforma escolhida.
#
# Uso:
#   scripts/install.sh <plataforma> <diretorio-do-projeto>
#
# Plataformas:
#   claude    .claude/skills  e .claude/agents
#   gemini    .gemini/skills  e .gemini/agents
#   copilot   .github/skills  e .github/agents (*.agent.md)
#   agents    .agents/skills  (convenção compartilhada entre ferramentas)
#   all       todas as anteriores
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() { sed -n '2,13p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 2; }

[ $# -eq 2 ] || usage
PLATFORM="$1"
TARGET="$2"
[ -d "$TARGET" ] || { echo "Diretório não encontrado: $TARGET" >&2; exit 1; }

copy_skills() {
  local dest="$TARGET/$1"
  mkdir -p "$dest"
  for skill in "$ROOT"/skills/*/; do
    local name
    name="$(basename "$skill")"
    rm -rf "${dest:?}/$name"
    cp -R "$skill" "$dest/$name"
  done
  echo "skills  -> $1"
}

copy_agents() {
  local dest="$TARGET/$1" suffix="$2"
  mkdir -p "$dest"
  for agent in "$ROOT"/agents/*.md; do
    cp "$agent" "$dest/$(basename "$agent" .md)$suffix"
  done
  echo "agentes -> $1"
}

install_one() {
  case "$1" in
    claude)  copy_skills ".claude/skills"; copy_agents ".claude/agents" ".md" ;;
    gemini)  copy_skills ".gemini/skills"; copy_agents ".gemini/agents" ".md" ;;
    copilot) copy_skills ".github/skills"; copy_agents ".github/agents" ".agent.md" ;;
    agents)  copy_skills ".agents/skills" ;;
    *) usage ;;
  esac
}

if [ "$PLATFORM" = "all" ]; then
  for p in claude gemini copilot agents; do install_one "$p"; done
else
  install_one "$PLATFORM"
fi

mkdir -p "$TARGET/iniciativas"
echo "Concluído. Artefatos das iniciativas: $TARGET/iniciativas/<slug>/"

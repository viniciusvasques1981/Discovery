#!/usr/bin/env bash
# Copia skills e agentes da esteira para um projeto, no formato da plataforma escolhida.
#
# Uso:
#   scripts/install.sh <plataforma> <diretorio-do-projeto>
#
# Plataformas: claude, gemini, copilot, agents, all
#
# O nível de modelo de cada agente vem de esteira.json > modelos.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/esteira.py" install "$@"

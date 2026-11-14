#!/usr/bin/env python3
"""Manutenção do repositório da Esteira de Produto AI-Enhanced.

Uso:
    python3 scripts/esteira.py sync       copia templates/ para skills/<skill>/assets/
    python3 scripts/esteira.py validate   valida frontmatter, referências e sincronização
    python3 scripts/esteira.py package    gera dist/<skill>.zip para upload em Gemini ou Claude
"""
from __future__ import annotations

import filecmp
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
AGENTS = ROOT / "agents"
TEMPLATES = ROOT / "templates"
DIST = ROOT / "dist"

# Fonte única: templates/. Cada skill recebe uma cópia dos modelos que utiliza.
SKILL_TEMPLATES = {
    "discovery-product-strategy": ["01-discovery.md", "02-estrategia.md", "contexto.md"],
    "hypothesis-validation-research": ["02b-validacao-hipoteses.md", "contexto.md"],
    "behavioral-modeling-feature-framing": [
        "03-modelagem.md", "03b-arvore-oportunidades.md", "04-feature-frames.md", "contexto.md",
    ],
    "systemic-ui-interaction-design": ["05-prototipacao.md", "contexto.md"],
    "prototype-usability-testing": ["05b-teste-usabilidade.md", "contexto.md"],
    "technical-handoff-prompt-engineering": ["04-feature-frames.md", "06-handoff.md", "contexto.md"],
    "behavioral-analytics-ux-fixes": ["07-diagnostico-comportamental.md", "contexto.md"],
    "behavioral-experimentation-cro": ["08-experimentos.md", "contexto.md"],
    "artifact-evidence-review": ["revisoes.md", "contexto.md"],
    "esteira-orchestration": ["contexto.md"],
    "match-my-writing-style": ["voice-card.md"],
    "get-more-perspectives": [],
}

SKILL_PREFIXES = (
    "discovery-", "behavioral-", "systemic-", "technical-", "get-more", "match-my",
    "hypothesis-", "prototype-", "artifact-evidence", "esteira-",
)
AGENT_SUFFIXES = ("-strategist", "-modeler", "-designer", "-lead", "-analyst", "-orchestrator", "-reviewer")

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict[str, str]:
    """Lê o frontmatter YAML simples (chave: valor em uma linha)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "#")):
            key, value = line.split(":", 1)
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = value[1:-1].replace('\\"', '"')
            data[key.strip()] = value
    return data


def sync() -> int:
    for skill, names in SKILL_TEMPLATES.items():
        assets = SKILLS / skill / "assets"
        if assets.exists():
            shutil.rmtree(assets)
        if not names:
            continue
        assets.mkdir(parents=True)
        for name in names:
            shutil.copyfile(TEMPLATES / name, assets / name)
        print(f"sync  {skill}: {', '.join(names)}")
    return 0


def validate() -> int:
    errors: list[str] = []

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    skill_names = {p.name for p in skill_dirs}
    agent_files = sorted(AGENTS.glob("*.md"))
    agent_names = {p.stem for p in agent_files}

    for folder in skill_dirs:
        skill_md = folder / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{folder.name}: SKILL.md ausente")
            continue
        meta = frontmatter(skill_md)
        name = meta.get("name", "")
        desc = meta.get("description", "")
        if name != folder.name:
            errors.append(f"{folder.name}: name '{name}' difere do nome da pasta")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{folder.name}: name fora do padrão kebab-case (máx. 64)")
        if not desc:
            errors.append(f"{folder.name}: description ausente")
        elif len(desc) > 1024:
            errors.append(f"{folder.name}: description com {len(desc)} caracteres (máx. 1024)")
        if folder.name not in SKILL_TEMPLATES:
            errors.append(f"{folder.name}: skill sem entrada em SKILL_TEMPLATES")

        body = skill_md.read_text(encoding="utf-8")
        for ref in re.findall(r"`assets/([^`]+)`", body):
            if not (folder / "assets" / ref).exists():
                errors.append(f"{folder.name}: referência a assets/{ref} inexistente")
        for ref in re.findall(r"`([a-z0-9-]+)`", body):
            if ref.count("-") >= 2 and ref not in skill_names | agent_names and ref.startswith(SKILL_PREFIXES):
                errors.append(f"{folder.name}: referência a skill inexistente '{ref}'")

    for skill, names in SKILL_TEMPLATES.items():
        if skill not in skill_names:
            errors.append(f"SKILL_TEMPLATES: skill '{skill}' não existe em skills/")
            continue
        assets = SKILLS / skill / "assets"
        existing = {p.name for p in assets.iterdir()} if assets.exists() else set()
        if existing != set(names):
            errors.append(f"{skill}: assets/ fora de sincronia (execute: esteira.py sync)")
            continue
        for name in names:
            if not filecmp.cmp(TEMPLATES / name, assets / name, shallow=False):
                errors.append(f"{skill}: assets/{name} difere de templates/{name} (execute: esteira.py sync)")

    for path in agent_files:
        meta = frontmatter(path)
        if meta.get("name") != path.stem:
            errors.append(f"agents/{path.name}: name difere do nome do arquivo")
        if not meta.get("description"):
            errors.append(f"agents/{path.name}: description ausente")
        body = path.read_text(encoding="utf-8")
        for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", body)):
            if ref in skill_names | agent_names:
                continue
            if ref.endswith(AGENT_SUFFIXES):
                errors.append(f"agents/{path.name}: referência a agente inexistente '{ref}'")
            if ref.startswith(SKILL_PREFIXES):
                errors.append(f"agents/{path.name}: referência a skill inexistente '{ref}'")

    # Links relativos em Markdown
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "dist", "node_modules"} for part in md.parts):
            continue
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#\s]+)", md.read_text(encoding="utf-8")):
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: link quebrado -> {target}")

    if errors:
        print("\n".join(f"ERRO  {e}" for e in errors))
        return 1
    print(f"ok  {len(skill_dirs)} skills, {len(agent_files)} agentes, templates sincronizados, links válidos")
    return 0


def package() -> int:
    DIST.mkdir(exist_ok=True)
    for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        target = DIST / f"{folder.name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in sorted(folder.rglob("*")):
                if file.is_file():
                    zf.write(file, Path(folder.name) / file.relative_to(folder))
        print(f"zip   {target.relative_to(ROOT)}")
    return 0


def main() -> int:
    commands = {"sync": sync, "validate": validate, "package": package}
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print(__doc__)
        return 2
    return commands[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Manutenção do repositório da Esteira de Produto AI-Enhanced.

Uso:
    python3 scripts/esteira.py sync                        gera tabelas e copia modelos e scripts para as skills
    python3 scripts/esteira.py validate                    valida registro, frontmatter, sincronização e links
    python3 scripts/esteira.py package                     gera dist/<skill>.zip para upload em Gemini ou Claude
    python3 scripts/esteira.py install <plataforma> <dir>  copia skills e agentes para um projeto
                                                           plataformas: claude, gemini, copilot, agents, all

A fonte única é esteira.json (módulos, skills, agentes, modelos de artefato, scripts e nível de modelo).
"""
from __future__ import annotations

import filecmp
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
AGENTS = ROOT / "agents"
TEMPLATES = ROOT / "templates"
SCRIPTS = ROOT / "scripts"
DIST = ROOT / "dist"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REGION_RE = re.compile(r"(<!-- gerado:([a-z-]+) -->\n)(.*?)(<!-- /gerado:\2 -->)", re.S)
AGENT_SUFFIXES = ("-strategist", "-modeler", "-designer", "-lead", "-analyst", "-orchestrator", "-reviewer")

# Arquivos que contêm tabelas geradas a partir de esteira.json
GENERATED_FILES = ["AGENTS.md", "README.md", "docs/mapa-da-esteira.md", "skills/esteira-orchestration/SKILL.md"]


def registry() -> dict:
    return json.loads((ROOT / "esteira.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------- tabelas geradas

def _label(m: dict) -> str:
    return f"{m['id']} — {m['nome']}" + (" (opcional)" if m["opcional"] else "")


def _names(items: list[str], kind: str, prefix: str | None) -> str:
    if not items:
        return "—"
    if prefix is None:
        return ", ".join(f"`{i}`" for i in items)
    path = (lambda i: f"{prefix}skills/{i}/SKILL.md") if kind == "skill" else (lambda i: f"{prefix}agents/{i}.md")
    return ", ".join(f"[`{i}`]({path(i)})" for i in items)


def _files(items: list[str]) -> str:
    return ", ".join(f"`{i}`" for i in items) if items else "—"


def _table(header: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(":---" for _ in header) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def render(view: str, reg: dict) -> str:
    mods, trans = reg["modulos"], reg["transversais"]
    if view == "modulos-agents":
        rows = [[_label(m), _names(m["skills"], "skill", None), _names(m["agentes"], "agent", None), _files(m["artefatos"])] for m in mods]
        rows += [[t["nome"], _names(t["skills"], "skill", None), _names(t["agentes"], "agent", None), _files(t["artefatos"])] for t in trans]
        return _table(["Módulo / Etapa", "Skill", "Agente", "Artefato"], rows)
    if view in ("modulos-readme", "modulos-mapa"):
        prefix = "" if view == "modulos-readme" else "../"
        rows = [[_label(m), m["framework"], m["entrega"], _names(m["skills"], "skill", prefix), _names(m["agentes"], "agent", prefix), _files(m["artefatos"])] for m in mods]
        return _table(["Módulo / Etapa", "Framework", "Entrega principal", "Skill", "Agente", "Artefato"], rows)
    if view in ("transversais-readme", "transversais-mapa"):
        prefix = "" if view == "transversais-readme" else "../"
        rows = [[t["nome"], t["tipo"], t["funcao"], _names(t["skills"], "skill", prefix), _names(t["agentes"], "agent", prefix)] for t in trans]
        return _table(["Componente", "Tipo", "Função", "Skill", "Agente"], rows)
    if view == "delegacao":
        rows = [[_label(m), _names(m["agentes"], "agent", None), _names(m["skills"], "skill", None), _files(m["artefatos"]),
                 "Sim" if m["revisao"] else "—", m["aprovador"]] for m in mods]
        return _table(["Módulo / Etapa", "Agente", "Skill", "Artefato", "Revisão independente", "Aprovador padrão"], rows)
    raise KeyError(view)


def regenerate(text: str, reg: dict) -> str:
    return REGION_RE.sub(lambda m: m.group(1) + render(m.group(2), reg) + m.group(4), text)


# ---------------------------------------------------------------- utilidades

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


def _mirror(skill: str, sub: str, source: Path, names: list[str]) -> None:
    target = SKILLS / skill / sub
    if target.exists():
        shutil.rmtree(target)
    if not names:
        return
    target.mkdir(parents=True)
    for name in names:
        shutil.copyfile(source / name, target / name)


def _mirror_ok(skill: str, sub: str, source: Path, names: list[str]) -> bool:
    target = SKILLS / skill / sub
    existing = {p.name for p in target.iterdir() if p.is_file()} if target.exists() else set()
    if existing != set(names):
        return False
    return all(filecmp.cmp(source / n, target / n, shallow=False) for n in names)


# ---------------------------------------------------------------- comandos

def sync() -> int:
    reg = registry()
    for skill, cfg in reg["skills"].items():
        _mirror(skill, "assets", TEMPLATES, cfg["assets"])
        _mirror(skill, "scripts", SCRIPTS, cfg["scripts"])
    for rel in GENERATED_FILES:
        path = ROOT / rel
        old = path.read_text(encoding="utf-8")
        new = regenerate(old, reg)
        if new != old:
            path.write_text(new, encoding="utf-8")
            print(f"gerado  {rel}")
    print(f"sync    {len(reg['skills'])} skills (modelos e scripts) e {len(GENERATED_FILES)} arquivos com tabelas")
    return 0


def validate() -> int:
    reg = registry()
    errors: list[str] = []

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    skill_names = {p.name for p in skill_dirs}
    agent_files = sorted(AGENTS.glob("*.md"))
    agent_names = {p.stem for p in agent_files}

    # registro x arquivos
    used_skills = {s for g in reg["modulos"] + reg["transversais"] for s in g["skills"]}
    used_agents = {a for g in reg["modulos"] + reg["transversais"] for a in g["agentes"]}
    for name in sorted(skill_names - set(reg["skills"])):
        errors.append(f"skills/{name}: pasta sem entrada em esteira.json > skills")
    for name in sorted(set(reg["skills"]) - skill_names):
        errors.append(f"esteira.json: skill '{name}' sem pasta em skills/")
    for name in sorted(skill_names - used_skills):
        errors.append(f"skills/{name}: skill não referenciada em modulos nem em transversais")
    for name in sorted(used_skills - skill_names):
        errors.append(f"esteira.json: skill '{name}' referenciada e inexistente")
    for name in sorted(agent_names - used_agents):
        errors.append(f"agents/{name}.md: agente órfão, não referenciado em esteira.json (remova o arquivo ou registre-o)")
    for name in sorted(used_agents - agent_names):
        errors.append(f"esteira.json: agente '{name}' referenciado e inexistente")
    for name in sorted(set(reg["modelos"]["papeis"]) ^ agent_names):
        errors.append(f"esteira.json > modelos.papeis: divergência com agents/ em '{name}'")

    # skills
    first_segments = {n.split("-")[0] + "-" for n in skill_names}
    for folder in skill_dirs:
        skill_md = folder / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{folder.name}: SKILL.md ausente")
            continue
        meta = frontmatter(skill_md)
        name, desc = meta.get("name", ""), meta.get("description", "")
        if name != folder.name:
            errors.append(f"{folder.name}: name '{name}' difere do nome da pasta")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{folder.name}: name fora do padrão kebab-case (máx. 64)")
        if not desc:
            errors.append(f"{folder.name}: description ausente")
        elif len(desc) > 1024:
            errors.append(f"{folder.name}: description com {len(desc)} caracteres (máx. 1024)")
        body = skill_md.read_text(encoding="utf-8")
        for sub in ("assets", "scripts"):
            for ref in re.findall(rf"`{sub}/([^`\s]+)", body):
                if not (folder / sub / ref).exists():
                    errors.append(f"{folder.name}: referência a {sub}/{ref} inexistente")
        cfg = reg["skills"].get(folder.name)
        if cfg:
            if not _mirror_ok(folder.name, "assets", TEMPLATES, cfg["assets"]):
                errors.append(f"{folder.name}: assets/ fora de sincronia (execute: esteira.py sync)")
            if not _mirror_ok(folder.name, "scripts", SCRIPTS, cfg["scripts"]):
                errors.append(f"{folder.name}: scripts/ fora de sincronia (execute: esteira.py sync)")

    # agentes
    for path in agent_files:
        meta = frontmatter(path)
        if meta.get("name") != path.stem:
            errors.append(f"agents/{path.name}: name difere do nome do arquivo")
        if not meta.get("description"):
            errors.append(f"agents/{path.name}: description ausente")
        if "model" in meta:
            errors.append(f"agents/{path.name}: não fixe `model:` no arquivo canônico; use esteira.json > modelos")

    # referências cruzadas em skills e agentes
    for path in [d / "SKILL.md" for d in skill_dirs] + agent_files:
        if not path.exists():
            continue
        for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", path.read_text(encoding="utf-8"))):
            if ref in skill_names | agent_names:
                continue
            if ref.endswith(AGENT_SUFFIXES):
                errors.append(f"{path.relative_to(ROOT)}: referência a agente inexistente '{ref}'")
            elif ref.count("-") >= 2 and ref.startswith(tuple(first_segments)):
                errors.append(f"{path.relative_to(ROOT)}: referência a skill inexistente '{ref}'")

    # tabelas geradas
    for rel in GENERATED_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if not REGION_RE.search(text):
            errors.append(f"{rel}: nenhuma região <!-- gerado:... --> encontrada")
        elif regenerate(text, reg) != text:
            errors.append(f"{rel}: tabela gerada desatualizada (execute: esteira.py sync)")

    # contagens na página de apresentação
    page = ROOT / "docs" / "index.html"
    if page.exists():
        html = page.read_text(encoding="utf-8")
        for label, expected in (("skills", len(skill_names)), ("agentes", len(agent_names))):
            m = re.search(rf"<b>(\d+)</b> {label}", html)
            if m and int(m.group(1)) != expected:
                errors.append(f"docs/index.html: informa {m.group(1)} {label}; o repositório tem {expected}")

    # links relativos em Markdown
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "dist", "node_modules"} for part in md.parts):
            continue
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#\s]+)", md.read_text(encoding="utf-8")):
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: link quebrado -> {target}")

    if errors:
        print("\n".join(f"ERRO  {e}" for e in errors))
        return 1
    print(f"ok  {len(skill_dirs)} skills, {len(agent_files)} agentes, registro consistente, tabelas e cópias sincronizadas, links válidos")
    return 0


def package() -> int:
    DIST.mkdir(exist_ok=True)
    for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        target = DIST / f"{folder.name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in sorted(folder.rglob("*")):
                if file.is_file() and "__pycache__" not in file.parts:
                    zf.write(file, Path(folder.name) / file.relative_to(folder))
        print(f"zip   {target.relative_to(ROOT)}")
    return 0


PLATFORMS = {
    "claude": {"skills": ".claude/skills", "agents": ".claude/agents", "suffix": ".md"},
    "gemini": {"skills": ".gemini/skills", "agents": ".gemini/agents", "suffix": ".md"},
    "copilot": {"skills": ".github/skills", "agents": ".github/agents", "suffix": ".agent.md"},
    "agents": {"skills": ".agents/skills", "agents": None, "suffix": ".md"},
}


def install(platform: str, target_dir: str) -> int:
    target = Path(target_dir).expanduser().resolve()
    if not target.is_dir():
        print(f"Diretório não encontrado: {target}", file=sys.stderr)
        return 1
    names = list(PLATFORMS) if platform == "all" else [platform]
    if any(n not in PLATFORMS for n in names):
        print(__doc__)
        return 2
    reg = registry()
    for name in names:
        cfg = PLATFORMS[name]
        dest = target / cfg["skills"]
        dest.mkdir(parents=True, exist_ok=True)
        for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            if (dest / skill.name).exists():
                shutil.rmtree(dest / skill.name)
            shutil.copytree(skill, dest / skill.name, ignore=shutil.ignore_patterns("__pycache__"))
        print(f"skills  -> {cfg['skills']}")
        if not cfg["agents"]:
            continue
        dest = target / cfg["agents"]
        dest.mkdir(parents=True, exist_ok=True)
        levels = reg["modelos"]["plataformas"].get(name, {})
        routed = 0
        for agent in sorted(AGENTS.glob("*.md")):
            text = agent.read_text(encoding="utf-8")
            model = levels.get(reg["modelos"]["papeis"].get(agent.stem, ""), "")
            if model:
                end = text.find("\n---", 4)
                text = text[:end] + f"\nmodel: {model}" + text[end:]
                routed += 1
            (dest / f"{agent.stem}{cfg['suffix']}").write_text(text, encoding="utf-8")
        print(f"agentes -> {cfg['agents']} ({routed} com modelo definido)")
    (target / "iniciativas").mkdir(exist_ok=True)
    print(f"Concluído. Artefatos das iniciativas: {target}/iniciativas/<slug>/")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args[:1] == ["install"] and len(args) == 3:
        return install(args[1], args[2])
    commands = {"sync": sync, "validate": validate, "package": package}
    if len(args) != 1 or args[0] not in commands:
        print(__doc__)
        return 2
    return commands[args[0]]()


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Cria issues no GitHub a partir de um 06-handoff.md.

Cada bloco iniciado por "### ISSUE <ID> — <título>" vira uma issue. O bloco
termina no próximo "### ISSUE" ou no próximo título de nível 2 ("## ").

Por padrão, apenas exibe o que seria criado. A criação exige --criar e a CLI
`gh` instalada e autenticada (https://cli.github.com).

Uso:
    python3 scripts/criar_issues.py iniciativas/<slug>/06-handoff.md --repo dono/repo
    python3 scripts/criar_issues.py iniciativas/<slug>/06-handoff.md --repo dono/repo --criar
    python3 scripts/criar_issues.py iniciativas/<slug>/06-handoff.md --repo dono/repo --criar --label esteira
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ISSUE_RE = re.compile(r"^### ISSUE\s+(?P<id>\S+)\s+[—–-]\s+(?P<titulo>.+?)\s*$", re.M)
PLACEHOLDER_RE = re.compile(r"\[(título|limite|estado inicial|ação|resultado observável)[^\]]*\]", re.I)


def extrair_issues(texto: str) -> list[dict[str, str]]:
    issues = []
    encontrados = list(ISSUE_RE.finditer(texto))
    for i, m in enumerate(encontrados):
        inicio = m.end()
        fim = encontrados[i + 1].start() if i + 1 < len(encontrados) else len(texto)
        proximo_h2 = re.search(r"^## ", texto[inicio:fim], re.M)
        if proximo_h2:
            fim = inicio + proximo_h2.start()
        corpo = texto[inicio:fim].strip()
        corpo = re.sub(r"\n-{3,}\s*$", "", corpo).strip()
        issues.append({"id": m.group("id"), "titulo": m.group("titulo"), "corpo": corpo})
    return issues


def problemas(issue: dict[str, str]) -> list[str]:
    avisos = []
    corpo = issue["corpo"]
    if "Out of Scope" not in corpo:
        avisos.append("sem seção Out of Scope")
    if "Por quê" not in corpo:
        avisos.append("sem o Por quê")
    if "Cenário:" not in corpo:
        avisos.append("sem cenários BDD")
    if PLACEHOLDER_RE.search(issue["titulo"] + corpo):
        avisos.append("contém campos do modelo não preenchidos")
    return avisos


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("handoff", type=Path, help="caminho do 06-handoff.md")
    parser.add_argument("--repo", required=True, help="repositório de destino, no formato dono/repo")
    parser.add_argument("--label", action="append", default=[], help="label a aplicar (pode repetir; deve existir no repositório)")
    parser.add_argument("--criar", action="store_true", help="cria as issues; sem esta opção, apenas exibe")
    args = parser.parse_args()

    if not args.handoff.is_file():
        print(f"Arquivo não encontrado: {args.handoff}", file=sys.stderr)
        return 1

    issues = extrair_issues(args.handoff.read_text(encoding="utf-8"))
    if not issues:
        print("Nenhum bloco '### ISSUE <ID> — <título>' encontrado.", file=sys.stderr)
        return 1

    bloqueado = False
    for issue in issues:
        avisos = problemas(issue)
        print(f"{issue['id']} — {issue['titulo']}  ({len(issue['corpo'])} caracteres)")
        for aviso in avisos:
            print(f"    AVISO: {aviso}")
        bloqueado = bloqueado or bool(avisos)

    if not args.criar:
        print(f"\n{len(issues)} issue(s) seriam criadas em {args.repo}. Use --criar para criar.")
        return 0

    if bloqueado:
        print("\nCriação cancelada: corrija os avisos acima no 06-handoff.md.", file=sys.stderr)
        return 1
    if shutil.which("gh") is None:
        print("\nCLI 'gh' não encontrada. Instale em https://cli.github.com e execute 'gh auth login'.", file=sys.stderr)
        return 1

    for issue in issues:
        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tmp:
            tmp.write(issue["corpo"] + f"\n\n---\nOrigem: `{args.handoff.as_posix()}`\n")
            caminho = tmp.name
        comando = ["gh", "issue", "create", "--repo", args.repo,
                   "--title", f"{issue['id']} — {issue['titulo']}", "--body-file", caminho]
        for label in args.label:
            comando += ["--label", label]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        Path(caminho).unlink(missing_ok=True)
        if resultado.returncode != 0:
            print(f"Falha em {issue['id']}: {resultado.stderr.strip()}", file=sys.stderr)
            return resultado.returncode
        print(f"criada  {issue['id']}: {resultado.stdout.strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

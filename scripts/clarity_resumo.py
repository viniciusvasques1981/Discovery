#!/usr/bin/env python3
"""Converte a resposta da Data Export API do Microsoft Clarity em Markdown.

A API devolve uma lista de objetos {"metricName": ..., "information": [...]}.
Este script gera uma tabela por métrica, sem interpretar os dados: o resultado
serve de insumo para a skill behavioral-analytics-ux-fixes (Módulo 7).

Uso:
    python3 scripts/clarity_resumo.py --arquivo export.json
    python3 scripts/clarity_resumo.py --dias 3 --dimensao URL
    python3 scripts/clarity_resumo.py --dias 1 --dimensao URL --dimensao Device --salvar-json export.json

Na consulta à API, o token é lido da variável de ambiente CLARITY_API_TOKEN
(gerado nas configurações do projeto no Clarity). Limites da API: dados dos
últimos 1 a 3 dias, até 3 dimensões por consulta e cota diária de requisições
por projeto. Documentação:
https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENDPOINT = "https://www.clarity.ms/export-data/api/v1/project-live-insights"
MAX_LINHAS = 50


def consultar(dias: int, dimensoes: list[str]) -> list:
    token = os.environ.get("CLARITY_API_TOKEN")
    if not token:
        sys.exit("Defina CLARITY_API_TOKEN ou use --arquivo com um JSON já exportado.")
    params = {"numOfDays": str(dias)}
    for i, dimensao in enumerate(dimensoes, start=1):
        params[f"dimension{i}"] = dimensao
    req = urllib.request.Request(
        f"{ENDPOINT}?{urllib.parse.urlencode(params)}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        motivo = {401: "token ausente, inválido ou expirado", 403: "acesso negado",
                  429: "cota diária de requisições excedida"}.get(exc.code, exc.reason)
        sys.exit(f"Erro {exc.code} na API do Clarity: {motivo}")
    except urllib.error.URLError as exc:
        sys.exit(f"Falha de conexão com a API do Clarity: {exc.reason}")


def celula(valor) -> str:
    if valor is None:
        return ""
    if isinstance(valor, float):
        return f"{valor:.4g}"
    return str(valor).replace("|", "\\|").replace("\n", " ")


def tabela(linhas: list[dict]) -> str:
    colunas: list[str] = []
    for linha in linhas:
        for chave in linha:
            if chave not in colunas:
                colunas.append(chave)
    saida = ["| " + " | ".join(colunas) + " |", "| " + " | ".join(":---" for _ in colunas) + " |"]
    for linha in linhas[:MAX_LINHAS]:
        saida.append("| " + " | ".join(celula(linha.get(c)) for c in colunas) + " |")
    if len(linhas) > MAX_LINHAS:
        saida.append(f"\n_{len(linhas) - MAX_LINHAS} linha(s) omitida(s); total de {len(linhas)}._")
    return "\n".join(saida)


def para_markdown(dados: list, origem: str) -> str:
    if not isinstance(dados, list):
        sys.exit("Formato inesperado: a resposta deveria ser uma lista de métricas.")
    partes = [
        "# Resumo de telemetria — Microsoft Clarity",
        "",
        f"- **Origem:** {origem}",
        f"- **Gerado em (UTC):** {datetime.now(timezone.utc):%Y-%m-%d %H:%M}",
        "- **Natureza:** dados agregados da Data Export API, sem interpretação. "
        "A API cobre no máximo os últimos 3 dias; registrar essa limitação no diagnóstico.",
        "",
    ]
    for metrica in dados:
        if not isinstance(metrica, dict):
            continue
        nome = metrica.get("metricName", "(sem nome)")
        linhas = [l for l in metrica.get("information") or [] if isinstance(l, dict)]
        partes.append(f"## {nome}")
        partes.append("")
        partes.append(tabela(linhas) if linhas else "_Sem dados no período._")
        partes.append("")
    return "\n".join(partes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--arquivo", type=Path, help="JSON já exportado da API")
    parser.add_argument("--dias", type=int, choices=[1, 2, 3], default=3, help="janela da consulta à API")
    parser.add_argument("--dimensao", action="append", default=[],
                        help="dimensão de quebra (até 3), ex.: URL, Device, Browser, OS")
    parser.add_argument("--salvar-json", type=Path, help="grava a resposta bruta da API neste arquivo")
    args = parser.parse_args()

    if len(args.dimensao) > 3:
        sys.exit("A API aceita no máximo 3 dimensões por consulta.")

    if args.arquivo:
        if not args.arquivo.is_file():
            sys.exit(f"Arquivo não encontrado: {args.arquivo}")
        dados = json.loads(args.arquivo.read_text(encoding="utf-8"))
        origem = f"arquivo `{args.arquivo.name}`"
    else:
        dados = consultar(args.dias, args.dimensao)
        origem = f"API, últimos {args.dias} dia(s), dimensões: {', '.join(args.dimensao) or 'nenhuma'}"
        if args.salvar_json:
            args.salvar_json.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    print(para_markdown(dados, origem))
    return 0


if __name__ == "__main__":
    sys.exit(main())

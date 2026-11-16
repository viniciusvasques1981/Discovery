#!/usr/bin/env python3
"""Operações determinísticas sobre uma iniciativa da esteira.

Tira do modelo de linguagem o trabalho mecânico: numerar insumos, localizar
trechos citados, copiar Out of Scope e Por quê para o handoff e conferir a
consistência dos artefatos.

Uso (o diretório é a pasta da iniciativa, ex.: iniciativas/portal-fornecedores):
    iniciativa.py numerar   <dir>                 numera as linhas de 00-insumos/ em 00-insumos/numerados/
    iniciativa.py citar     <dir> D1:L0012 ...    exibe as linhas citadas (aceita faixas: D1:L0012-L0015)
    iniciativa.py citar     <dir> --evidencias    exibe cada evidência ao lado das linhas de origem
    iniciativa.py citar     <dir> --nao-citadas   exibe as linhas dos insumos que nenhuma evidência cita
    iniciativa.py montar    <dir> [--checar]      preenche os blocos derivados de 06-handoff.md
    iniciativa.py verificar <dir>                 confere os artefatos; sai com código 1 se houver erro

Imersão com mais de um produto (o tronco é a iniciativa no repositório da imersão):
    iniciativa.py derivar   <tronco> <produto> <destino>   cria a instância do produto a partir do tronco
    iniciativa.py publicar  <dir> [--checar]               gera interface.md, o resumo lido pelos produtos vizinhos
    iniciativa.py vizinhos  <dir>                          lê as interfaces dos vizinhos e cruza dependências
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".vtt", ".srt", ".csv", ".tsv", ".log"}
REF_RE = re.compile(r"D(\d+):L(\d+)(?:-L?(\d+))?")
EVID_RE = re.compile(r"\bE\d{3}\b")
MAX_LINE = 320

PLACEHOLDERS = re.compile(
    r"\[(?:título|nome|slug|iniciativa|limite(?: verificável)?|estado inicial|ação|resultado observável|objetivo|n)\]"
    r"|\b(?:KR|FF-|J|P|S|H|T-|AJ-)_(?![A-Za-z0-9])|(?<![=\w])AAAA-MM-DD|\[NN\]"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------- numerar

def _split(line: str) -> list[str]:
    """Divide linhas longas em frases, para que a citação aponte um trecho curto."""
    if len(line) <= MAX_LINE:
        return [line]
    parts, cur = [], ""
    for sentence in re.split(r"(?<=[.!?])\s+", line):
        if cur and len(cur) + len(sentence) + 1 > MAX_LINE:
            parts.append(cur)
            cur = sentence
        else:
            cur = f"{cur} {sentence}".strip()
    if cur:
        parts.append(cur)
    return parts


def numerar(root: Path) -> int:
    src = root / "00-insumos"
    out = src / "numerados"
    if not src.is_dir():
        print(f"Pasta não encontrada: {src}", file=sys.stderr)
        return 1
    out.mkdir(exist_ok=True)
    index_path = out / "indice.json"
    index: dict[str, str] = json.loads(read(index_path)) if index_path.exists() else {}
    files = sorted(p for p in src.iterdir() if p.is_file() and p.suffix.lower() in TEXT_EXT)
    skipped = sorted(p.name for p in src.iterdir() if p.is_file() and p.suffix.lower() not in TEXT_EXT)
    next_id = max([int(v[1:]) for v in index.values()] + [0]) + 1
    rows = []
    for f in files:
        if f.name not in index:
            index[f.name] = f"D{next_id}"
            next_id += 1
        doc = index[f.name]
        lines: list[str] = []
        for raw in read(f).splitlines():
            raw = raw.strip()
            if raw:
                lines.extend(_split(raw))
        body = "\n".join(f"{doc}:L{i:04d} | {text}" for i, text in enumerate(lines, start=1))
        (out / f"{doc}-{f.stem}.md").write_text(f"# {doc} — {f.name}\n\n{body}\n", encoding="utf-8")
        chars = sum(len(t) for t in lines)
        rows.append((doc, f.name, len(lines), chars))
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    table = ["# Índice dos insumos numerados", "",
             "| Documento | Arquivo | Linhas | Caracteres | Tokens (aprox.) |", "| :--- | :--- | ---: | ---: | ---: |"]
    table += [f"| {d} | {n} | {l} | {c} | {round(c / 3.3)} |" for d, n, l, c in sorted(rows, key=lambda r: int(r[0][1:]))]
    (out / "INDICE.md").write_text("\n".join(table) + "\n", encoding="utf-8")
    for d, n, l, c in rows:
        print(f"{d}  {n}: {l} linhas, ~{round(c / 3.3)} tokens")
    for name in skipped:
        print(f"AVISO  {name}: formato não textual, não numerado (converta para .md ou .txt)")
    return 0


# ---------------------------------------------------------------- citar

def _load_numbered(root: Path) -> dict[tuple[int, int], str]:
    lines: dict[tuple[int, int], str] = {}
    folder = root / "00-insumos" / "numerados"
    if folder.is_dir():
        for f in folder.glob("D*-*.md"):
            for m in re.finditer(r"^D(\d+):L(\d+) \| (.*)$", read(f), re.M):
                lines[(int(m.group(1)), int(m.group(2)))] = m.group(3)
    return lines


def _expand(ref: str) -> list[tuple[int, int]]:
    out = []
    for m in REF_RE.finditer(ref):
        doc, a = int(m.group(1)), int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        out += [(doc, n) for n in range(a, b + 1)]
    return out


def _evidence_rows(root: Path) -> list[tuple[str, str]]:
    path = root / "evidencias.md"
    if not path.exists():
        return []
    return [(m.group(1), m.group(0)) for m in re.finditer(r"^\|\s*(E\d{3})\s*\|.*$", read(path), re.M)]


def citar(root: Path, args: list[str]) -> int:
    numbered = _load_numbered(root)
    if not numbered:
        print("Insumos não numerados. Execute: iniciativa.py numerar <dir>", file=sys.stderr)
        return 1
    fmt = lambda k: f"D{k[0]}:L{k[1]:04d} | {numbered.get(k, '*** LINHA INEXISTENTE ***')}"
    if args == ["--evidencias"]:
        for eid, row in _evidence_rows(root):
            print(row)
            for key in _expand(row):
                print("    " + fmt(key))
        return 0
    if args == ["--nao-citadas"]:
        cited = {k for _, row in _evidence_rows(root) for k in _expand(row)}
        rest = sorted(set(numbered) - cited)
        print(f"{len(rest)} de {len(numbered)} linhas não citadas por nenhuma evidência")
        for key in rest:
            print(fmt(key))
        return 0
    if not args:
        print(__doc__)
        return 2
    for key in _expand(" ".join(args)):
        print(fmt(key))
    return 0


# ---------------------------------------------------------------- leitura dos artefatos

def feature_frames(root: Path) -> list[dict]:
    path = root / "04-feature-frames.md"
    if not path.exists():
        return []
    text = read(path)
    frames = []
    heads = list(re.finditer(r"^### (FF-\d+) — (.+)$", text, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^## ", text[h.end():end], re.M)
        block = text[h.end():h.end() + nxt.start()] if nxt else text[h.end():end]
        field = lambda name: (re.search(rf"^\|\s*\*\*{re.escape(name)}[^|]*\*\*\s*\|\s*(.*?)\s*\|\s*$", block, re.M) or [None, ""])[1]
        oos = re.search(r"\*\*Out of Scope[^\n]*\n\n((?:- .+\n?)+)", block)
        frames.append({
            "id": h.group(1), "nome": h.group(2).strip(),
            "solucao": field("Solução"), "kr": field("Key Result relacionado"),
            "estagio": field("Estágio da jornada"), "mvp": field("MVP").lower().startswith("sim"),
            "oos": [l[2:].strip() for l in oos.group(1).splitlines()] if oos else [],
        })
    return frames


def strategy(root: Path) -> dict:
    path = root / "02-estrategia.md"
    if not path.exists():
        return {"proposito": "", "visao": "", "krs": {}}
    text = read(path)
    clean_refs = lambda s: re.sub(r"\s*\((?:[A-Z]+\d+(?:,\s*)?)+\)", "", s).strip()
    prop = re.search(r"\*\*Por quê \(Propósito\):\*\*\s*(.+)", text)
    vis = re.search(r"^## Declaração de Visão de Produto\s*\n+> (.+)$", text, re.M)
    krs = {m.group(1): m.group(2).strip() for m in re.finditer(r"^\|\s*(KR\d+)\s*—\s*([^|]+)\|", text, re.M)}
    return {
        "proposito": clean_refs(prop.group(1)) if prop else "",
        "visao": vis.group(1).replace("**", "").strip() if vis else "",
        "krs": krs,
    }


# ---------------------------------------------------------------- montar

def _fill(text: str, name: str, content: str, style: str) -> tuple[str, int]:
    if style == "html":
        pat = re.compile(rf"(<!-- montar:{name} -->\n)(.*?)(<!-- /montar:{name} -->)", re.S)
    else:
        pat = re.compile(rf"(# >>> montar:{name}\n)(.*?)(# <<< montar:{name})", re.S)
    return pat.subn(lambda m: m.group(1) + content.rstrip("\n") + "\n" + m.group(3), text)


def montar_texto(root: Path) -> tuple[str, str, list[str]]:
    """Devolve (texto atual, texto montado, avisos) de 06-handoff.md."""
    path = root / "06-handoff.md"
    text = read(path)
    frames = {f["id"]: f for f in feature_frames(root)}
    strat = strategy(root)
    notes: list[str] = []
    out = text
    heads = list(re.finditer(r"^### ISSUE (FF-\d+) — .+$", text, re.M))
    pieces, cursor = [], 0
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        nxt = re.search(r"^## ", text[h.end():end], re.M)
        stop = h.end() + nxt.start() if nxt else end
        block = text[h.start():stop]
        ff = frames.get(h.group(1))
        if not ff:
            notes.append(f"ERRO  issue {h.group(1)}: Feature Frame inexistente em 04-feature-frames.md")
        else:
            kr_ids = re.findall(r"KR\d+", ff["kr"])
            kr_txt = ", ".join(f"{k} ({strat['krs'][k]})" if k in strat["krs"] else k for k in kr_ids) or "nenhum Key Result informado"
            fills = {
                "por-que": f"**Por quê:** {strat['proposito']} Contribui para {kr_txt}.",
                "escopo": f"**Escopo:** {ff['solucao']}",
                "out-of-scope": "**Out of Scope** (transcrito do Feature Frame):\n\n" + "\n".join(f"- {l}" for l in ff["oos"]),
            }
            for name, content in fills.items():
                block, n = _fill(block, name, content, "html")
                if n == 0:
                    notes.append(f"ERRO  issue {h.group(1)}: marcador montar:{name} ausente")
        pieces.append(text[cursor:h.start()] + block)
        cursor = stop
    out = "".join(pieces) + text[cursor:]
    mvp = [f for f in frames.values() if f["mvp"]]
    limites = "\n".join(f"{f['id']} — {f['nome']}:\n" + "\n".join(f"- {l}" for l in f["oos"]) for f in mvp)
    produto = f"Por quê: {strat['proposito']}\nVisão: {strat['visao']}"
    for name, content in (("contexto-produto", produto), ("limites", limites)):
        out, n = _fill(out, name, content, "hash")
        if n == 0:
            notes.append(f"ERRO  System Prompt: marcador montar:{name} ausente")
    return text, out, notes


def montar(root: Path, check: bool) -> int:
    if not (root / "06-handoff.md").exists():
        print("06-handoff.md não encontrado.", file=sys.stderr)
        return 1
    old, new, notes = montar_texto(root)
    for n in notes:
        print(n)
    if check:
        if old != new:
            print("ERRO  06-handoff.md: blocos derivados desatualizados (execute: iniciativa.py montar)")
        return 1 if (old != new or notes) else 0
    if old != new:
        (root / "06-handoff.md").write_text(new, encoding="utf-8")
        print("montado  06-handoff.md")
    else:
        print("ok  06-handoff.md já está montado")
    return 1 if notes else 0


# ---------------------------------------------------------------- verificar

def _num(s: str) -> float | None:
    m = re.search(r"-?\d+(?:[.,]\d+)?", s)
    return float(m.group(0).replace(",", ".")) if m else None


def _section(text: str, title: str) -> str:
    m = re.search(rf"^## {re.escape(title)}.*?$", text, re.M)
    if not m:
        return ""
    nxt = re.search(r"^## ", text[m.end():], re.M)
    return text[m.end():m.end() + nxt.start()] if nxt else text[m.end():]


def verificar(root: Path) -> int:
    err: list[str] = []
    warn: list[str] = []
    done: list[str] = []
    exists = lambda n: (root / n).exists()

    artefatos = sorted(p for p in root.glob("*.md") if re.match(r"\d\d", p.name) or p.name in ("contexto.md", "evidencias.md"))
    for p in artefatos:
        hits = sorted(set(PLACEHOLDERS.findall(read(p))))
        if hits:
            err.append(f"{p.name}: campos do modelo não preenchidos: {', '.join(hits[:6])}")
    done.append(f"campos de modelo em {len(artefatos)} artefatos")

    # evidências
    evid_ids = {e for e, _ in _evidence_rows(root)}
    numbered = _load_numbered(root)
    if exists("evidencias.md"):
        for eid, row in _evidence_rows(root):
            keys = _expand(row)
            if not keys:
                err.append(f"evidencias.md: {eid} sem referência de origem (D<n>:L<n>)")
            elif numbered:
                missing = [f"D{d}:L{l:04d}" for d, l in keys if (d, l) not in numbered]
                if missing:
                    err.append(f"evidencias.md: {eid} cita linha inexistente: {', '.join(missing[:3])}")
        if not numbered and not exists("origem.json"):
            warn.append("insumos não numerados: referências D:L não puderam ser conferidas")
        for p in artefatos:
            if p.name == "evidencias.md":
                continue
            unknown = sorted(set(EVID_RE.findall(read(p))) - evid_ids)
            if unknown:
                err.append(f"{p.name}: cita evidência inexistente: {', '.join(unknown[:6])}")
        done.append(f"{len(evid_ids)} evidências e suas referências")
    elif exists("01-discovery.md"):
        warn.append("evidencias.md ausente: a origem dos itens não pôde ser conferida")

    if exists("01-discovery.md"):
        for m in re.finditer(r"^\|\s*([CSP]\d+)\s*\|.*$", read(root / "01-discovery.md"), re.M):
            if not EVID_RE.search(m.group(0)) and "[inferência]" not in m.group(0):
                err.append(f"01-discovery.md: {m.group(1)} sem evidência citada nem marca [inferência]")
        done.append("origem dos itens da Matriz CSD e das dores")

    # feature frames
    frames = feature_frames(root)
    mvp = {f["id"] for f in frames if f["mvp"]}
    if exists("04-feature-frames.md"):
        text04 = read(root / "04-feature-frames.md")
        for f in frames:
            if not f["oos"]:
                err.append(f"04-feature-frames.md: {f['id']} sem Out of Scope")
            if not re.search(r"J\d+", f["estagio"]):
                err.append(f"04-feature-frames.md: {f['id']} sem estágio da jornada")
            if not re.search(r"KR\d+", f["kr"]):
                err.append(f"04-feature-frames.md: {f['id']} sem Key Result relacionado")
        viab = _section(text04, "Checagem de viabilidade técnica")
        checked = set(re.findall(r"^\|\s*(FF-\d+)\s*\|", viab, re.M))
        for fid in sorted({f["id"] for f in frames} - checked):
            err.append(f"04-feature-frames.md: {fid} sem checagem de viabilidade técnica")
        for m in re.finditer(r"^\|\s*(FF-\d+)\s*\|.*Inviável.*$", viab, re.M):
            if m.group(1) in mvp:
                err.append(f"04-feature-frames.md: {m.group(1)} está no MVP com parecer Inviável")
        prio = _section(text04, "Matriz de priorização")
        header = next((l for l in prio.splitlines() if l.startswith("|") and "Índice" in l), None)
        if header:
            cols = [c.strip() for c in header.strip("|").split("|")]
            ix = {n: cols.index(n) for n in ("Valor", "Confiança", "Esforço", "Índice") if n in cols}
            weight = {"alta": 1.0, "média": 0.7, "media": 0.7, "baixa": 0.4}
            for line in prio.splitlines():
                cells = [c.strip() for c in line.strip("|").split("|")]
                fid = next((c for c in cells if re.fullmatch(r"FF-\d+", c)), None)
                if not fid or len(ix) < 4 or len(cells) < len(cols):
                    continue
                v, e, shown = _num(cells[ix["Valor"]]), _num(cells[ix["Esforço"]]), _num(cells[ix["Índice"]])
                w = weight.get(cells[ix["Confiança"]].lower())
                if None in (v, e, shown, w) or not e:
                    warn.append(f"04-feature-frames.md: índice de {fid} não pôde ser recalculado")
                elif abs(v * w / e - shown) > 0.006:
                    err.append(f"04-feature-frames.md: índice de {fid} é {shown:.2f}; o cálculo dá {v * w / e:.2f}")
        done.append(f"{len(frames)} Feature Frames: campos, viabilidade e índice")

    # prototipação
    if exists("05-prototipacao.md") and frames:
        for m in re.finditer(r"^### (T-\d+).*?\n(.*?)(?=^### |^## |\Z)", read(root / "05-prototipacao.md"), re.M | re.S):
            ffs = set(re.findall(r"FF-\d+", (re.search(r"^\|\s*\*\*Feature Frame\*\*\s*\|(.*)$", m.group(2), re.M) or [None, ""])[1]))
            if not ffs:
                err.append(f"05-prototipacao.md: {m.group(1)} sem Feature Frame vinculado")
            for fid in sorted(ffs - mvp):
                err.append(f"05-prototipacao.md: {m.group(1)} vinculada a {fid}, que não está no MVP")
        done.append("vínculo de cada tela com Feature Frame do MVP")

    # handoff
    if exists("06-handoff.md"):
        text06 = read(root / "06-handoff.md")
        issues = {}
        heads = list(re.finditer(r"^### ISSUE (FF-\d+) — .+$", text06, re.M))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text06)
            issues[h.group(1)] = text06[h.end():end]
        for fid in sorted(mvp - set(issues)):
            err.append(f"06-handoff.md: Feature Frame {fid} do MVP sem issue")
        for fid in sorted(set(issues) - mvp):
            err.append(f"06-handoff.md: issue {fid} não corresponde a Feature Frame do MVP")
        for fid, body in issues.items():
            n = len(re.findall(r"^\s*Cenário:", body.split("\n## ")[0], re.M))
            if n < 3:
                err.append(f"06-handoff.md: issue {fid} tem {n} cenário(s); o mínimo é 3")
        _, _, notes = montar_texto(root)
        old, new, _ = montar_texto(root)
        err += [n[6:] for n in notes if n.startswith("ERRO")]
        if old != new:
            err.append("06-handoff.md: blocos derivados desatualizados (execute: iniciativa.py montar)")
        plano = _section(text06, "Plano de Instrumentação")
        for kr in sorted(strategy(root)["krs"]):
            if not re.search(rf"\b{kr}\b", plano):
                err.append(f"06-handoff.md: {kr} sem evento ou medida no Plano de Instrumentação")
        done.append(f"{len(issues)} issues: cobertura do MVP, cenários, blocos derivados e instrumentação")

    verificar_produtos(root, err, warn, done)

    if exists("contexto.md"):
        size = len(read(root / "contexto.md"))
        if size > 6000:
            warn.append(f"contexto.md com {size} caracteres: mova detalhes para os artefatos e mantenha apenas decisões e ponteiros")

    for w in warn:
        print(f"AVISO  {w}")
    for e in err:
        print(f"ERRO   {e}")
    for d in done:
        print(f"ok     {d}")
    print(f"\n{len(err)} erro(s), {len(warn)} aviso(s)")
    return 1 if err else 0


# ---------------------------------------------------------------- vários produtos

PROD_RE = re.compile(r"^## Produto: `([a-z0-9-]+)` — (.+)$", re.M)
ABERTO_RE = re.compile(r"`([a-z0-9-]+)`")


def partilha(root: Path) -> dict | None:
    """Lê partilha.md: produtos, ponto de separação, partilha de itens e donos dos estágios."""
    path = root / "partilha.md"
    if not path.exists():
        return None
    text = read(path)
    sep = re.search(r"\*\*Ponto de separação:\*\*\s*Módulo\s*(\d)", text)
    produtos = {}
    for line in _section(text, "Produtos").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = ABERTO_RE.fullmatch(cells[0]) if cells else None
        if m and len(cells) >= 3:
            produtos[m.group(1)] = {"nome": cells[1], "repo": cells[2].strip("`")}
    itens = {}
    for m in re.finditer(r"^\|\s*([PSD]\d+)\s*\|(.*)$", _section(text, "Partilha"), re.M):
        cells = [c.strip() for c in m.group(2).strip("|").split("|")]
        itens[m.group(1)] = {"produtos": ABERTO_RE.findall(cells[1]) if len(cells) > 1 else [],
                             "situacao": cells[2] if len(cells) > 2 else ""}
    estagios = {}
    for m in re.finditer(r"^\|\s*(J\d+)\s*\|(.*)$", _section(text, "Estágios da jornada"), re.M):
        cells = [c.strip() for c in m.group(2).strip("|").split("|")]
        estagios[m.group(1)] = {"dono": ABERTO_RE.findall(cells[0]) if cells else [],
                                "passagem": ABERTO_RE.findall(cells[1]) if len(cells) > 1 else []}
    return {"separacao": int(sep.group(1)) if sep else None, "produtos": produtos, "itens": itens, "estagios": estagios}


def _sha(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def _git(root: Path, *args: str) -> str:
    import subprocess
    try:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def estrategia_do_produto(text: str, slug: str, nome: str) -> str | None:
    """Converte a estratégia de vários produtos na estratégia de um produto, no formato padrão."""
    heads = list(PROD_RE.finditer(text))
    if not heads:
        return None
    comum = text[:heads[0].start()]
    comum = re.sub(r"^# .*$", f"# Módulo 2 — Estratégia: {nome}", comum, count=1, flags=re.M)
    for i, h in enumerate(heads):
        if h.group(1) != slug:
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        bloco = re.sub(r"^###(?!#)", "##", text[h.end():end].strip("\n"), flags=re.M)
        nota = (f"> Derivado da estratégia da imersão para o produto `{slug}`. As seções comuns vêm do tronco; "
                "as seções deste produto estão no formato padrão da esteira.\n")
        return f"{comum.rstrip()}\n\n{nota}\n{bloco}\n"
    return None


APROVACOES_VAZIO = """# Aprovações e Registro: {nome}

> Arquivo de registro. Recebe linhas novas; linhas existentes não são reescritas. As aprovações dos módulos herdados estão no repositório da imersão.

## Aprovações

| Módulo | Aprovador (papel) | Nome | Data | Verificação | Revisão independente | Pendências aceitas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## Etapas opcionais

| Etapa | Executada | Decisão de quem | Motivo / risco aceito |
| :--- | :--- | :--- | :--- |

## Alterações em artefatos já aprovados

| Data | Artefato | O que mudou | Motivo |
| :--- | :--- | :--- | :--- |
"""


def _interface_url(repo: str, slug: str) -> str:
    m = re.match(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", repo)
    if m:
        return f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/main/iniciativas/{slug}/interface.md"
    return f"{repo.rstrip('/')}/iniciativas/{slug}/interface.md" if repo and repo != "—" else ""


def derivar(tronco: Path, slug: str, destino: Path) -> int:
    from datetime import date
    mapa = partilha(tronco)
    if not mapa:
        print("partilha.md não encontrado no tronco.", file=sys.stderr)
        return 1
    if slug not in mapa["produtos"]:
        print(f"Produto '{slug}' não consta em partilha.md. Produtos: {', '.join(mapa['produtos']) or 'nenhum'}", file=sys.stderr)
        return 1
    sep = mapa["separacao"]
    if sep not in (3, 4):
        print("partilha.md: informe '**Ponto de separação:** Módulo 3' ou 'Módulo 4'.", file=sys.stderr)
        return 1
    herdar = ["evidencias.md", "01-discovery.md", "partilha.md"] + (["03-modelagem.md"] if sep == 4 else [])
    faltam = [f for f in herdar + ["02-estrategia.md"] if not (tronco / f).exists()]
    if faltam:
        print(f"Tronco incompleto para a separação no Módulo {sep}: falta {', '.join(faltam)}", file=sys.stderr)
        return 1
    if destino.exists() and any(destino.iterdir()):
        print(f"Destino já existe e não está vazio: {destino}", file=sys.stderr)
        return 1
    nome = mapa["produtos"][slug]["nome"]
    estr = estrategia_do_produto(read(tronco / "02-estrategia.md"), slug, nome)
    if estr is None:
        print(f"02-estrategia.md do tronco não tem a seção '## Produto: `{slug}` — ...'.", file=sys.stderr)
        return 1
    destino.mkdir(parents=True, exist_ok=True)
    for f in herdar:
        (destino / f).write_bytes((tronco / f).read_bytes())
    (destino / "02-estrategia.md").write_text(estr, encoding="utf-8")
    if (tronco / "contexto.md").exists():
        ctx = read(tronco / "contexto.md")
        ctx = re.sub(r"(\*\*Slug\*\* \| )`[^`]*`", rf"\1`{slug}`", ctx, count=1)
        (destino / "contexto.md").write_text(ctx, encoding="utf-8")
    (destino / "aprovacoes.md").write_text(APROVACOES_VAZIO.format(nome=nome), encoding="utf-8")
    herdados = herdar + ["02-estrategia.md"]
    origem = {
        "produto": slug, "nome": nome, "separacao": sep, "data": date.today().isoformat(),
        "tronco": {"repositorio": _git(tronco, "config", "--get", "remote.origin.url"),
                   "commit": _git(tronco, "rev-parse", "--short", "HEAD"), "iniciativa": tronco.resolve().name},
        "herdados": {f: _sha(destino / f) for f in herdados},
    }
    (destino / "origem.json").write_text(json.dumps(origem, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    viz = [{"produto": s, "interface": _interface_url(p["repo"], s)} for s, p in mapa["produtos"].items() if s != slug]
    (destino / "vizinhos.json").write_text(json.dumps(viz, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    meus = sorted(k for k, v in mapa["itens"].items() if slug in v["produtos"])
    estagios = sorted(k for k, v in mapa["estagios"].items() if slug in v["dono"])
    print(f"derivado  {slug} -> {destino}")
    print(f"herdados  {', '.join(herdados)} (somente leitura; alterações são feitas no tronco)")
    print(f"itens     {', '.join(meus) or 'nenhum atribuído'}")
    if sep == 4:
        print(f"estágios  {', '.join(estagios) or 'nenhum atribuído'}")
    print(f"vizinhos  {', '.join(v['produto'] for v in viz) or 'nenhum'} (confira os caminhos em vizinhos.json)")
    print(f"próximo   Módulo {sep}")
    return 0


# ---------------------------------------------------------------- interface e vizinhança

def _ff_extra(root: Path) -> dict[str, dict]:
    """Campos do Feature Frame usados na interface: dor, situação, dependências."""
    path = root / "04-feature-frames.md"
    out: dict[str, dict] = {}
    if not path.exists():
        return out
    text = read(path)
    heads = list(re.finditer(r"^### (FF-\d+) — (.+)$", text, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[h.end():end]
        field = lambda name: (re.search(rf"^\|\s*\*\*{re.escape(name)}[^|]*\*\*\s*\|\s*(.*?)\s*\|\s*$", block, re.M) or [None, ""])[1]
        out[h.group(1)] = {
            "dor": ", ".join(re.findall(r"\bP\d+\b", field("Dor atendida"))) or "—",
            "situacao": field("Situação"),
            "depende": re.findall(r"([a-z0-9-]+):(FF-\d+)", field("Depende de")),
            "fornece": re.findall(r"([a-z0-9-]+)(?::(FF-\d+))?", field("Fornece para").replace("`", "")) if field("Fornece para") not in ("", "—") else [],
        }
    return out


def interface_texto(root: Path) -> str:
    origem = json.loads(read(root / "origem.json")) if (root / "origem.json").exists() else {}
    slug = origem.get("produto", root.name)
    frames = feature_frames(root)
    extra = _ff_extra(root)
    t06 = read(root / "06-handoff.md") if (root / "06-handoff.md").exists() else ""
    t07 = read(root / "07-diagnostico-comportamental.md") if (root / "07-diagnostico-comportamental.md").exists() else ""
    issues = set(re.findall(r"^### ISSUE (FF-\d+)", t06, re.M))
    L = [f"# Interface do produto: `{slug}`", "",
         "> Gerado por `iniciativa.py publicar`. Não editar: altere os artefatos e gere de novo. "
         "É o único arquivo deste produto que os produtos vizinhos leem.", "",
         f"- **Tronco:** {origem.get('tronco', {}).get('iniciativa') or '—'}, versão {origem.get('tronco', {}).get('commit') or 'não registrada'}", "",
         "## Feature Frames", "",
         "| ID | Nome | MVP | Situação | Dor | Estágio | Depende de | Fornece para |", "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"]
    for f in frames:
        e = extra.get(f["id"], {})
        sit = e.get("situacao") or ("Especificado" if f["id"] in issues else "Proposto")
        dep = ", ".join(f"{p}:{i}" for p, i in e.get("depende", [])) or "—"
        forn = ", ".join(f"{p}:{i}" if i else p for p, i in e.get("fornece", []) if p) or "—"
        L.append(f"| {f['id']} | {f['nome']} | {'Sim' if f['mvp'] else 'Não'} | {sit} | {e.get('dor', '—')} | "
                 f"{', '.join(re.findall(r'J[0-9]+', f['estagio'])) or '—'} | {dep} | {forn} |")
    L += ["", "## Out of Scope", "", "| Feature Frame | Limite |", "| :--- | :--- |"]
    L += [f"| {f['id']} | {l} |" for f in frames for l in f["oos"]]
    eventos = sorted(set(re.findall(r"`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`", _section(t06, "Plano de Instrumentação"))))
    L += ["", "## Eventos instrumentados", ""] + ([f"- `{e}`" for e in eventos] or ["Nenhum registrado."])
    apis = re.findall(r"^\|\s*(GET|POST|PUT|PATCH|DELETE)\s*\|\s*`([^`]+)`\s*\|\s*([^|]*)\|", t06, re.M)
    L += ["", "## Contratos de API", ""]
    L += (["| Método | Caminho | Descrição |", "| :--- | :--- | :--- |"] + [f"| {m} | `{p}` | {d.strip()} |" for m, p, d in apis]) if apis else ["Nenhum registrado."]
    m_dados = re.search(r"^### Estrutura de Dados\s*\n(.*?)(?=^#{2,3} |\Z)", t06, re.M | re.S)
    entidades = sorted(set(re.findall(r"^\|\s*([A-ZÀ-Ú][\wÀ-ú]+)\s*\|\s*`", m_dados.group(1) if m_dados else "", re.M)))
    L += ["", "## Entidades de dados", ""] + ([f"- {e}" for e in entidades] or ["Nenhuma registrada."])
    recl = re.findall(r"^\|\s*([SC]\d+)[^|]*\|\s*([^|]+)\|\s*([^|]+)\|", _section(t07, "Revisão da Matriz CSD"), re.M)
    L += ["", "## Itens do tronco reclassificados por este produto", ""]
    L += (["| Item | De | Para |", "| :--- | :--- | :--- |"] + [f"| {i} | {a.strip()} | {b.strip()} |" for i, a, b in recl]) if recl else ["Nenhum."]
    return "\n".join(L) + "\n"


def publicar(root: Path, check: bool) -> int:
    if not (root / "04-feature-frames.md").exists():
        print("04-feature-frames.md não encontrado: não há o que publicar.", file=sys.stderr)
        return 1
    new = interface_texto(root)
    path = root / "interface.md"
    old = read(path) if path.exists() else ""
    if check:
        if old != new:
            print("ERRO  interface.md desatualizado (execute: iniciativa.py publicar)")
        return 0 if old == new else 1
    if old != new:
        path.write_text(new, encoding="utf-8")
        print("publicado  interface.md")
    else:
        print("ok  interface.md já está atualizado")
    return 0


def _ler_interface(text: str) -> dict:
    ffs = {}
    for m in re.finditer(r"^\|\s*(FF-\d+)\s*\|(.*)$", _section(text, "Feature Frames"), re.M):
        c = [x.strip() for x in m.group(2).strip("|").split("|")]
        if len(c) >= 7:
            ffs[m.group(1)] = {"nome": c[0], "mvp": c[1] == "Sim", "situacao": c[2], "dor": re.findall(r"P\d+", c[3]),
                               "depende": re.findall(r"([a-z0-9-]+):(FF-\d+)", c[5])}
    return {
        "ffs": ffs,
        "eventos": set(re.findall(r"^- `([^`]+)`", _section(text, "Eventos instrumentados"), re.M)),
        "entidades": set(re.findall(r"^- (.+)$", _section(text, "Entidades de dados"), re.M)),
        "recl": re.findall(r"^\|\s*([SC]\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|", _section(text, "Itens do tronco reclassificados"), re.M),
        "tronco": (re.search(r"\*\*Tronco:\*\*\s*(.+)", text) or [None, ""])[1].strip(),
    }


def vizinhos(root: Path) -> int:
    import difflib
    import urllib.request
    cfg_path = root / "vizinhos.json"
    if not cfg_path.exists():
        print("vizinhos.json não encontrado: esta iniciativa não tem produtos vizinhos registrados.")
        return 0
    if publicar(root, False):
        return 1
    meu_slug = json.loads(read(root / "origem.json")).get("produto", root.name) if (root / "origem.json").exists() else root.name
    eu = _ler_interface(read(root / "interface.md"))
    cache = root / "vizinhos"
    cache.mkdir(exist_ok=True)
    err, warn = [], []
    for v in json.loads(read(cfg_path)):
        slug, src = v["produto"], v.get("interface", "")
        try:
            if src.startswith(("http://", "https://")):
                with urllib.request.urlopen(src, timeout=30) as resp:
                    novo = resp.read().decode("utf-8")
            else:
                p = Path(src) if Path(src).is_absolute() else (root / src)
                novo = read(p)
        except Exception as exc:  # leitura do vizinho é melhor esforço
            warn.append(f"{slug}: interface não acessível em '{src}' ({type(exc).__name__}); usando a última cópia, se houver")
            novo = None
        arq = cache / f"{slug}.md"
        antigo = read(arq) if arq.exists() else ""
        if novo is None:
            if not antigo:
                continue
            novo = antigo
        elif novo != antigo:
            diff = [l for l in difflib.unified_diff(antigo.splitlines(), novo.splitlines(), lineterm="", n=0)
                    if l[:1] in "+-" and l[:3] not in ("+++", "---")]
            if antigo:
                print(f"MUDOU  {slug}: {len(diff)} linha(s) desde a última leitura")
                for l in diff[:40]:
                    print(f"    {l}")
                if len(diff) > 40:
                    print(f"    ... mais {len(diff) - 40} linha(s); veja vizinhos/{slug}.md")
            else:
                print(f"NOVO   {slug}: primeira leitura da interface, gravada em vizinhos/{slug}.md")
            arq.write_text(novo, encoding="utf-8")
        else:
            print(f"igual  {slug}: sem mudanças desde a última leitura")
        ele = _ler_interface(novo)
        for fid, f in eu["ffs"].items():
            for prod, dep in f["depende"]:
                if prod != slug:
                    continue
                alvo = ele["ffs"].get(dep)
                if not alvo:
                    err.append(f"{fid} depende de {slug}:{dep}, que não existe na interface de {slug}")
                elif "remov" in alvo["situacao"].lower():
                    err.append(f"{fid} depende de {slug}:{dep}, marcado como removido")
                elif not alvo["mvp"]:
                    warn.append(f"{fid} depende de {slug}:{dep} ({alvo['nome']}), que está fora do MVP de {slug}")
        for fid, f in ele["ffs"].items():
            for prod, dep in f["depende"]:
                if prod == meu_slug and dep not in eu["ffs"]:
                    err.append(f"{slug}:{fid} depende de {meu_slug}:{dep}, que não existe neste produto")
        for fid, f in eu["ffs"].items():
            for oid, o in ele["ffs"].items():
                comuns = set(f["dor"]) & set(o["dor"])
                if comuns and f["mvp"] and o["mvp"]:
                    warn.append(f"sobreposição: {fid} e {slug}:{oid} atendem a mesma dor ({', '.join(sorted(comuns))})")
        norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
        for kind, a, b in (("evento", eu["eventos"], ele["eventos"]), ("entidade", eu["entidades"], ele["entidades"])):
            for x in sorted(a):
                for y in sorted(b):
                    if x != y and (norm(x) == norm(y) or difflib.SequenceMatcher(None, norm(x), norm(y)).ratio() >= 0.85):
                        warn.append(f"vocabulário: {kind} '{x}' aqui e '{y}' em {slug} parecem a mesma coisa com nomes diferentes")
        for item, de, para in ele["recl"]:
            warn.append(f"{slug} reclassificou {item} do tronco: {de.strip()} → {para.strip()}; confira se este produto depende desse item")
        if eu["tronco"] and ele["tronco"] and eu["tronco"] != ele["tronco"]:
            warn.append(f"versões diferentes do tronco: aqui '{eu['tronco']}', em {slug} '{ele['tronco']}'")
    for w in warn:
        print(f"AVISO  {w}")
    for e in err:
        print(f"ERRO   {e}")
    print(f"\n{len(err)} erro(s), {len(warn)} aviso(s)")
    return 1 if err else 0


def verificar_produtos(root: Path, err: list[str], warn: list[str], done: list[str]) -> None:
    mapa = partilha(root)
    origem_path = root / "origem.json"
    if origem_path.exists():
        origem = json.loads(read(origem_path))
        for f, h in origem.get("herdados", {}).items():
            if not (root / f).exists():
                err.append(f"{f}: artefato herdado do tronco ausente")
            elif _sha(root / f) != h:
                err.append(f"{f}: artefato herdado foi alterado neste produto; mudanças devem ser feitas no tronco e derivadas de novo")
        slug = origem["produto"]
        if mapa and mapa["estagios"]:
            for f in feature_frames(root):
                for j in re.findall(r"J\d+", f["estagio"]):
                    dono = mapa["estagios"].get(j, {}).get("dono", [])
                    if dono and slug not in dono:
                        warn.append(f"04-feature-frames.md: {f['id']} atua no estágio {j}, que pertence a {', '.join(dono)}")
        if (root / "04-feature-frames.md").exists():
            if not (root / "interface.md").exists() or read(root / "interface.md") != interface_texto(root):
                err.append("interface.md ausente ou desatualizado (execute: iniciativa.py publicar)")
        done.append(f"instância do produto {slug}: artefatos herdados íntegros, estágios e interface")
    elif mapa:
        if mapa["separacao"] not in (3, 4):
            err.append("partilha.md: ponto de separação ausente (Módulo 3 ou Módulo 4)")
        if len(mapa["produtos"]) < 2:
            warn.append("partilha.md: menos de dois produtos; o mapa de partilha só é necessário com mais de um")
        if (root / "01-discovery.md").exists():
            itens01 = set(re.findall(r"^\|\s*([PS]\d+)\s*\|", read(root / "01-discovery.md"), re.M))
            for i in sorted(itens01 - set(mapa["itens"]), key=lambda s: (s[0], int(s[1:]))):
                err.append(f"partilha.md: {i} não foi atribuído a nenhum produto nem marcado como sem dono")
        for i, v in sorted(mapa["itens"].items()):
            for p in v["produtos"]:
                if p not in mapa["produtos"]:
                    err.append(f"partilha.md: {i} atribuído a produto inexistente '{p}'")
            if i.startswith("P") and not v["produtos"]:
                warn.append(f"partilha.md: a dor {i} está sem dono")
        if (root / "02-estrategia.md").exists():
            secoes = {m[0] for m in PROD_RE.findall(read(root / "02-estrategia.md"))}
            for p in sorted(set(mapa["produtos"]) - secoes):
                err.append(f"02-estrategia.md: falta a seção '## Produto: `{p}` — ...' com Visão e OKRs")
        if mapa["separacao"] == 4 and (root / "03-modelagem.md").exists():
            estagios03 = set(re.findall(r"^\|\s*(J\d+)\s*\|", read(root / "03-modelagem.md"), re.M))
            for j in sorted(estagios03 - {k for k, v in mapa["estagios"].items() if v["dono"]}):
                err.append(f"partilha.md: estágio {j} da jornada sem produto dono")
        done.append(f"mapa de partilha: {len(mapa['produtos'])} produtos, {len(mapa['itens'])} itens, {len(mapa['estagios'])} estágios")


def main() -> int:
    args = sys.argv[1:]
    comandos = ("numerar", "citar", "montar", "verificar", "derivar", "publicar", "vizinhos")
    if len(args) < 2 or args[0] not in comandos:
        print(__doc__)
        return 2
    root = Path(args[1])
    if not root.is_dir():
        print(f"Iniciativa não encontrada: {root}", file=sys.stderr)
        return 1
    if args[0] == "numerar":
        return numerar(root)
    if args[0] == "citar":
        return citar(root, args[2:])
    if args[0] == "montar":
        return montar(root, "--checar" in args[2:])
    if args[0] == "derivar":
        if len(args) != 4:
            print("Uso: iniciativa.py derivar <tronco> <produto> <destino>", file=sys.stderr)
            return 2
        return derivar(root, args[2], Path(args[3]))
    if args[0] == "publicar":
        return publicar(root, "--checar" in args[2:])
    if args[0] == "vizinhos":
        return vizinhos(root)
    return verificar(root)


if __name__ == "__main__":
    sys.exit(main())

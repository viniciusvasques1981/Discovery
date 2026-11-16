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
        if not numbered:
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


def main() -> int:
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ("numerar", "citar", "montar", "verificar"):
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
    return verificar(root)


if __name__ == "__main__":
    sys.exit(main())

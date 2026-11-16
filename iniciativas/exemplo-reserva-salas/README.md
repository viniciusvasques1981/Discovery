# Iniciativa de exemplo: reserva de salas

> **Conteúdo fictício.** A empresa "Nimbo Coworking", as pessoas, as falas e todos os números foram inventados para demonstrar a esteira. Nada aqui descreve uma organização real.

Finalidades:

1. **Referência de qualidade:** mostra o nível de detalhe e de rastreabilidade esperado em cada artefato.
2. **Caso de regressão:** ao alterar uma skill, reexecute o módulo correspondente sobre `00-insumos/` e compare o resultado com o artefato desta pasta.

| Arquivo | Módulo | Observação |
| :--- | :--- | :--- |
| `00-insumos/transcricao-imersao.md` | Insumo | Transcrição da imersão |
| `00-insumos/telemetria-pos-lancamento.md` | Insumo | Dados de uso posteriores à entrega, para os Módulos 7 e 8 |
| `00-insumos/numerados/` | Gerado | Insumos com identificador por linha, criados por `iniciativa.py numerar` |
| `evidencias.md` | 1 | Base de evidências: 22 afirmações com referência de linha |
| `contexto.md` | — | Índice de decisões, uma seção curta por módulo |
| `aprovacoes.md` | — | Aprovações, etapas opcionais e alterações |
| `01-discovery.md` a `06-handoff.md` | 1 a 6 | Trilha expressa. Em `06-handoff.md`, os blocos entre marcadores `montar:` foram preenchidos por script |
| `07-diagnostico-comportamental.md`, `08-experimentos.md` | 7 e 8 | Ciclo pós-entrega |
| `ajustes/AJ-01-celula-ocupada.md` | Trilha pocket | Ajuste pequeno derivado do achado A1 do Módulo 7 |
| `revisoes.md` | Revisão | Pareceres por bloco, incluindo um erro apontado pelo script e corrigido |

Para conferir o exemplo:

```bash
python3 scripts/iniciativa.py verificar iniciativas/exemplo-reserva-salas
python3 scripts/iniciativa.py citar iniciativas/exemplo-reserva-salas --evidencias
```

A pasta `00-insumos/` deste exemplo é versionada por exceção, definida no `.gitignore`.

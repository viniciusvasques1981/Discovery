# Iniciativa de exemplo: reserva de salas

> **Conteúdo fictício.** A empresa "Nimbo Coworking", as pessoas, as falas e todos os números foram inventados para demonstrar a esteira. Nada aqui descreve uma organização real.

Finalidades:

1. **Referência de qualidade:** mostra o nível de detalhe e de rastreabilidade esperado em cada artefato.
2. **Caso de regressão:** ao alterar uma skill, reexecute o módulo correspondente sobre `00-insumos/` e compare o resultado com o artefato desta pasta.

| Arquivo | Módulo | Observação |
| :--- | :--- | :--- |
| `00-insumos/transcricao-imersao.md` | Insumo | Transcrição com linhas numeradas (`L01`…), usadas como origem |
| `00-insumos/telemetria-pos-lancamento.md` | Insumo | Dados de uso posteriores à entrega, para os Módulos 7 e 8 |
| `contexto.md` | — | Resumo acumulado, aprovações e etapas opcionais |
| `01-discovery.md` a `06-handoff.md` | 1 a 6 | Trilha expressa: as etapas 2B, 3B e 5B não foram executadas, e o registro do risco aceito está em `contexto.md` |
| `07-diagnostico-comportamental.md`, `08-experimentos.md` | 7 e 8 | Ciclo pós-entrega |
| `revisoes.md` | Revisão | Pareceres do `artifact-reviewer`, incluindo um apontamento corrigido |

A pasta `00-insumos/` deste exemplo é versionada por exceção, definida no `.gitignore`.

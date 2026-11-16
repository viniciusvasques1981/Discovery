# Esteira de Produto AI-Enhanced — instruções para agentes

Agentes e skills que conduzem uma iniciativa de produto do Discovery ao Handoff técnico, com medição e experimentação pós-entrega. Processo de referência: `docs/guia-da-esteira.md`. Manutenção deste repositório: `docs/manutencao.md`.

## Módulos

Tabela gerada a partir de `esteira.json`. Não editar à mão.

<!-- gerado:modulos-agents -->
| Módulo / Etapa | Skill | Agente | Artefato |
| :--- | :--- | :--- | :--- |
| 0 — Entrada de insumos | `source-intake-documentation` | `source-documentalist` | `00-insumos/*.md`, `00-insumos/INVENTARIO.md` |
| 1 — Discovery | `discovery-product-strategy` | `discovery-strategist` | `evidencias.md`, `01-discovery.md` |
| 2 — Estratégia | `discovery-product-strategy` | `discovery-strategist` | `02-estrategia.md` |
| 2B — Validação de Hipóteses (opcional) | `hypothesis-validation-research` | `discovery-strategist` | `02b-validacao-hipoteses.md` |
| 3 — Modelagem | `behavioral-modeling-feature-framing` | `experience-modeler` | `03-modelagem.md` |
| 3B — Árvore de Oportunidades (opcional) | `behavioral-modeling-feature-framing` | `experience-modeler` | `03b-arvore-oportunidades.md` |
| 4 — Feature Frame | `behavioral-modeling-feature-framing`, `technical-feasibility-check` | `experience-modeler`, `handoff-tech-lead` | `04-feature-frames.md` |
| 5 — Prototipação | `systemic-ui-interaction-design` | `interface-designer` | `05-prototipacao.md` |
| 5B — Teste de Usabilidade (opcional) | `prototype-usability-testing` | `interface-designer` | `05b-teste-usabilidade.md` |
| 6 — Handoff | `technical-handoff-prompt-engineering` | `handoff-tech-lead` | `06-handoff.md` |
| 7 — Medição | `behavioral-analytics-ux-fixes` | `growth-analyst` | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | `behavioral-experimentation-cro` | `growth-analyst` | `08-experimentos.md` |
| Revisão independente | `artifact-evidence-review` | `artifact-reviewer` | `revisoes.md` |
| Ajuste pequeno (trilha pocket) | `pocket-feature-frame` | — | `ajustes/AJ-NN-<slug>.md` |
| Orquestração | `esteira-orchestration` | — | `contexto.md`, `aprovacoes.md` |
| Alinhamento entre produtos | `cross-product-alignment` | — | `interface.md`, `vizinhos/` |
| Painel de perspectivas | `get-more-perspectives` | — | — |
| Estilo de escrita | `match-my-writing-style` | — | — |
<!-- /gerado:modulos-agents -->

Trilhas: **pocket** (ajuste pequeno, um documento, sem agentes), **expressa** (módulos 1 a 6) e **completa** (com as etapas opcionais 2B, 3B e 5B). A escolha e o fechamento de cada módulo estão na skill `esteira-orchestration`.

## Regras gerais

1. **Contexto primeiro.** Todo módulo começa lendo `iniciativas/<slug>/contexto.md` e termina atualizando apenas a própria seção desse arquivo, em linhas curtas.
2. **Leitura mínima.** Cada skill lista suas entradas; não ler outros arquivos. Material que não está em texto é convertido na Etapa 0, um original por vez. O material bruto em `00-insumos/` é lido uma única vez, no Módulo 1. Depois disso, a fonte é `evidencias.md`.
3. **Fato e inferência.** Toda afirmação cita a evidência que a sustenta (E001…). O que vai além recebe `[inferência]`. Dado ausente não é estimado: registrar como Dúvida, `[pendente de dados]`, `[não validada]` ou `[a validar com o time técnico]`.
4. **Nada simulado.** Entrevistas, sessões de teste, dados de uso e resultados de experimento são informados pelo usuário. Agentes planejam e registram.
5. **Escrever uma vez.** Out of Scope é escrito no Feature Frame e chega ao handoff por script (`iniciativa.py montar`). Não copiar conteúdo de um artefato para outro.
6. **Script antes de modelo.** Conferências mecânicas são feitas por `iniciativa.py verificar`, ao fim de cada módulo. A revisão independente ocorre ao fim dos módulos 2, 4, 6 e 8.
7. **Aprovação humana.** Um módulo por vez; uma pessoa aprova antes do avanço. Nenhum agente registra aprovação em nome do usuário.
8. **Resposta curta.** Um agente devolve à conversa principal um resumo de até dez linhas e o caminho do artefato, não o conteúdo.
9. **Vários produtos.** Quando a imersão origina mais de um produto, a iniciativa da imersão é o tronco e cada produto é derivado dela para o próprio repositório (`iniciativa.py derivar`). Artefatos herdados não são alterados no produto. Um produto lê do outro apenas o `interface.md`.
10. **Formato.** Artefatos em português do Brasil, em Markdown, seguindo o modelo em `assets/` da skill. Gherkin com `# language: pt`.

Os caminhos `assets/` e `scripts/` citados nas skills são relativos à pasta da skill. Neste repositório, os mesmos scripts também estão em `scripts/`, na raiz.

## Estrutura de uma iniciativa

```text
iniciativas/<slug>/
├── 00-insumos/            textos citáveis; originais/ guarda gravações, imagens e documentos; numerados/ e INVENTARIO.md são gerados por script
├── evidencias.md          base de evidências, com referência de linha
├── contexto.md            índice de decisões, uma seção curta por módulo
├── aprovacoes.md          aprovações, etapas opcionais e alterações
├── revisoes.md            pareceres da revisão independente
├── 01-discovery.md … 08-experimentos.md
├── partilha.md             só em imersão com vários produtos: o que cada produto herda
├── origem.json, interface.md, vizinhos/   só em produto derivado de uma imersão
└── ajustes/               documentos da trilha pocket
```

Insumos podem conter dados confidenciais. `00-insumos/` não é versionado; a exceção é a iniciativa de exemplo, que é fictícia.

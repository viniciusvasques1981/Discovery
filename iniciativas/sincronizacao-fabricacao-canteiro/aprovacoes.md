# Contexto: sincronizacao-fabricacao-canteiro

> Índice de decisões da iniciativa. Cada módulo acrescenta ou atualiza apenas a própria seção, em linhas curtas. Detalhes ficam nos artefatos.

| | |
| :--- | :--- |
| **Slug** | `sincronizacao-fabricacao-canteiro` |
| **Sponsor** | Diretoria industrial / gestor de operações |
| **Trilha** | Completa |
| **Módulo atual** | 1 |
| **Última atualização** | 2026-11-16 |

## 1–2. Por quê

- **Propósito:** sincronizar planejamento de fabricação e execução no canteiro para reduzir atrasos, retrabalho e custos operacionais.
- **Visão de Produto:** plataforma de sincronização operacional entre fábrica e obra, com visibilidade em tempo real, rastreabilidade e priorização de sequenciamento.
- **Dores validadas:** P1 — ruptura de comunicação entre planejamento e execução; P2 — paradas por falta de componentes e ferramental; P3 — excesso de retrabalho por alterações sem atualização em tempo real.
- **OKRs:** KR1 — reduzir tempo médio de resposta a alterações de projeto; KR2 — reduzir paradas por falta de materiais; KR3 — reduzir variações de formas e impacto no turnover.
- **Restrições:** dados de campo menos confiáveis; integração com ERP e planilhas ainda incompleta; escopo do MVP limitado para evitar expansão.
- **Hipóteses:** H1 — visibilidade centralizada reduzirá atrasos de handoff; H2 — priorização de sequenciamento melhorará uso de equipes; H3 — rastreabilidade de componentes reduzirá paradas e retrabalho.
- **Detalhes:** `evidencias.md`, `01-discovery.md`, `02-estrategia.md`

## 3–4. Usuário e escopo

- **Protopersona:** gestor de operações e coordenador de obra; líder de produção; engenheiro de campo.
- **Jornada To-Be:** J1 — identificar impacto de alteração de projeto em tempo real; J2 — priorizar sequenciamento e balanceamento de equipes; J3 — rastrear disponibilidade de materiais e ferramental.
- **MVP:** FF-01 — painel de sincronização fabrica-canteiro; FF-02 — rastreio de alterações e impacto no cronograma; FF-03 — status de componentes e setup de formas.
- **Fora do MVP:** previsões avançadas, automação completa de EPC, integração profunda de ERP, otimização global de portfólio.
- **Ressalvas de viabilidade:** dependência de dados de campo; necessidade de padronização de nomenclaturas; integração com sistemas legados.
- **Integrações com outros produtos:** nenhuma no escopo inicial; dependência de ERP e planilhas como fontes de dados.
- **Detalhes e Out of Scope:** `03-modelagem.md`, `04-feature-frames.md`

## 5. Interface

- **Telas:** T-01 — visão geral de fábrica x canteiro; T-02 — painel de alterações e impactos; T-03 — acompanhamento de materiais e componentes; T-04 — sequenciamento e balanceamento de equipes.
- **Lacunas do Design System:** ausência de componentes específicos para cronogramas operacionais e indicadores em grande escala.
- **Teste de usabilidade:** executado em cenário fictício; resultados registrados em `05b-teste-usabilidade.md`.
- **Detalhes:** `05-prototipacao.md`

## 6. Handoff

- **Issues:** integrações, backlog de MVP, avaliação de dados e definição de eventos de instrumentação.
- **Instrumentação:** eventos de alteração de obra, status de componente, sincronização de cronograma e handoff entre fábrica e canteiro.
- **Pendências técnicas:** padronização de identificadores, qualidade de dados e acesso a bases de produção.
- **Detalhes:** `06-handoff.md`

## 7–8. Pós-entrega

- **Achados priorizados:** sincronização operacional; rastreabilidade de componentes; impacto de alterações em tempo real.
- **Experimentos:** teste de redução de atrasos, impacto de mudanças de sequenciamento e efeito no turnover.

## Dúvidas abertas

| # | Dúvida | Quem pode responder |
| :--- | :--- | :--- |
| D1 | Qual a frequência real de atualização dos dados de campo e quem é o responsável pela manutenção? | gestor de operações |
| D2 | A empresa tem uma base única de referência para formas, gabaritos e componentes? | diretor industrial |
| D3 | Há exigência legal ou contratual para dados operacionais sensíveis? | área jurídica / segurança |


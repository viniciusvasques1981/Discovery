# Contexto: sincronizacao-fabricacao-canteiro

> Índice de decisões da iniciativa. Conteúdo de demonstração fictícia; nenhuma aprovação ou validação com usuários reais está registrada.

| | |
| :--- | :--- |
| **Slug** | `sincronizacao-fabricacao-canteiro` |
| **Sponsor** | Não informado (papéis citados no cenário: gestão de operações e direção industrial) |
| **Trilha** | Completa (simulação) |
| **Módulo atual** | 5 — Prototipação; aguardando revisão/aprovação humana |
| **Última atualização** | 2026-11-16 |

## 1–2. Por quê

- **Propósito:** melhorar a sincronização entre planejamento fabril e execução no canteiro.
- **Visão de Produto:** proposta fictícia de visibilidade e rastreabilidade do fluxo operacional fábrica–obra.
- **Dores do cenário simulado:** falhas de sincronização, mudanças com impacto no cronograma, indisponibilidade de componentes e dependência de planilhas.
- **OKRs:** metas e baselines numéricos não confirmados; consultar `02-estrategia.md` e validar antes de uso.
- **Restrições:** integração de fontes incompleta; qualidade/frequência de dados de campo precisam de validação.
- **Hipóteses:** resultados fictícios; não tratados como validação real.
- **Detalhes:** `evidencias.md`, `01-discovery.md`, `02-estrategia.md`

## 3–4. Usuário e escopo

- **Protopersonas:** gestor de operações e coordenador de obra, no cenário fictício.
- **Jornada To-Be:** consultar sincronização; investigar impacto; acompanhar componentes.
- **MVP registrado:** FF-01 painel de sincronização; FF-02 impacto de alterações; FF-03 status de componentes/ferramental.
- **Fora do MVP / pendente:** app offline-first, RBAC, fotos obrigatórias, notificações imediatas, gestão de roster/roadmap e metas numéricas de exemplo, até decisão de escopo.
- **Ressalvas:** padronização de identificadores, qualidade dos dados e governança das integrações.
- **Detalhes:** `03-modelagem.md`, `04-feature-frames.md`

## 5. Interface

- **Telas:** dashboard gerencial T-01 a T-03; app operacional proposto T-04 a T-09, com itens fora do escopo atual marcados como pendentes.
- **Design System:** não fornecido; tokens provisórios documentados.
- **Teste de usabilidade:** há um roteiro/resultado de simulação fictícia; não equivale a teste com usuários reais.
- **Decisões em aberto:** escopo do app, dados/indicadores, privacidade de fotos, offline e integrações.
- **Detalhes:** `05-prototipacao.md`

## 6. Handoff

- **Status:** não avançar até revisão do escopo e aprovação humana dos módulos pendentes.
- **Instrumentação e pendências técnicas:** consultar `06-handoff.md`; itens de integração e offline não estão validados.

## 7–8. Pós-entrega

- **Status:** planos fictícios, sem dados reais de produção.
- **Detalhes:** `07-diagnostico-comportamental.md`, `08-experimentos.md`

## Dúvidas abertas

| # | Dúvida | Quem pode responder |
| :--- | :--- | :--- |
| D1 | Dashboard e App Operacional entram ambos no MVP? | Sponsor / Product Manager |
| D2 | RBAC, multi-tenancy, offline e fila de sincronização estão aprovados? | Tech Lead / Segurança |
| D3 | Captura fotográfica é necessária, por quanto tempo os arquivos serão retidos e quem terá acesso? | Sponsor / Privacidade / Segurança |
| D4 | Quais são as fontes, campos, frequência e critérios de qualidade para cada indicador? | Operações / TI |
| D5 | Os exemplos de metas (formas 80→15, turnover -20%) são apenas ilustrativos ou foram aprovados com baseline? | Sponsor |
| D6 | Qual Design System e stack devem ser adotados? | Product Designer / Tech Lead |


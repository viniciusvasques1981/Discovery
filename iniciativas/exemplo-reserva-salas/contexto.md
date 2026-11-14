# Contexto da Iniciativa: Reserva de salas (exemplo fictício)

> Conteúdo inventado para demonstração. Resumo acumulado da esteira, atualizado ao fim de cada módulo.

| | |
| :--- | :--- |
| **Slug** | `exemplo-reserva-salas` |
| **Sponsor** | Helena (Diretora de Operações) |
| **Trilha** | Expressa |
| **Módulo atual** | 8 — Experimentação (plano elaborado; execução pendente) |
| **Última atualização** | 2027-02-12 |

## Aprovações

| Módulo | Aprovador (papel) | Nome | Data | Revisão independente | Pendências aceitas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Sponsor | Helena | 2026-11-03 | Aprovado | — |
| 2 — Estratégia | Sponsor | Helena | 2026-11-03 | Aprovado com ressalvas | Linha de base do KR1 de um único mês |
| 3 — Modelagem | Product Manager | Helena (acumula o papel) | 2026-11-04 | Aprovado com ressalvas | Protopersona baseada em um único membro |
| 4 — Feature Frame | Product Manager e Tech Lead | Helena e Bianca | 2026-11-04 | Aprovado | Esforço de FF-02 a confirmar com o esquema do banco |
| 5 — Prototipação | Product Designer | Helena (sem designer no time) | 2026-11-04 | Aprovado com ressalvas | Design System não fornecido |
| 6 — Handoff | Tech Lead | Bianca | 2026-11-04 | Aprovado após correção (R-01) | Responsável por privacidade não identificado (D3) |
| 7 — Medição | Product Manager | Helena | 2027-02-12 | Aprovado com ressalvas | Janela de 3 dias na ferramenta de sessão |
| 8 — Experimentação | Product Manager | Pendente | — | Aprovado com ressalvas | — |

## Etapas opcionais

| Etapa | Executada | Decisão de quem | Motivo / risco aceito |
| :--- | :--- | :--- | :--- |
| 2B — Validação de Hipóteses | Não | Helena | Prazo do trimestre (L12). Risco aceito: H1 (adesão ao autoatendimento) só será verificada em produção, pelo KR2 |
| 3B — Árvore de Oportunidades | Não | Helena | As dores levam a uma solução direta; não havia soluções concorrentes na imersão |
| 5B — Teste de Usabilidade | Não | Helena | Prazo. Risco aceito: problemas de usabilidade detectados só no Módulo 7 — o que ocorreu (achados A1 e A2) |

## 1. Por quê (Módulos 1 e 2)

- **Propósito:** O membro precisa confiar que a sala reservada estará disponível quando chegar.
- **Visão de Produto:** Para membros da Nimbo Coworking, cujo problema é não saber se há sala livre e perder salas já reservadas, a Reserva de Salas é um módulo de autoatendimento do sistema de membros que mostra a disponibilidade das 14 salas e garante que cada horário tenha uma única reserva.
- **Dores validadas:**
  1. P1 — conflito de reserva (41 em outubro/2026).
  2. P2 — disponibilidade invisível ao membro.
  3. P3 — recepção ocupada com reservas (não quantificada).
- **OKRs:**
  - Objetivo: Tornar a reserva de salas confiável e autônoma para o membro.
  - KR1: conflitos por mês de 41 para 0.
  - KR2: reservas por autoatendimento de 0% para 70%.
  - KR3: medição de não comparecimento ativa, com 4 semanas de dados.
- **Limitações técnicas:** sistema web existente (React, Node, Postgres); 3 desenvolvedores; sem pagamento, sem fechaduras e sem agenda externa neste ciclo.
- **Dados pessoais e conformidade:** nome, e-mail e telefone dos membros, já no cadastro. Responsável por privacidade não identificado (D3).
- **Hipóteses e situação:**
  - H1 (adesão ao autoatendimento): evidência favorável em produção — 81,9% em duas semanas.
  - H2 (bloqueio elimina conflitos): evidência favorável — 0 conflitos em duas semanas.
  - H3 (não comparecimento): não validada.
  - H4 (reserva no mesmo dia): não validada; mensurável pela propriedade de antecedência.

## 2. Usuário e escopo (Módulos 3 e 4)

- **Protopersona:** membro que organiza reuniões da equipe e reserva perto do horário de uso.
- **Estágios da Jornada To-Be:** J1 Consultar, J2 Reservar, J3 Acompanhar, J4 Cancelar, J5 Usar a sala.
- **Feature Frames do MVP:**
  - FF-01: Consulta de disponibilidade.
  - FF-02: Reserva por autoatendimento com bloqueio de conflito.
  - FF-03: Minhas reservas e cancelamento.
- **Out of Scope consolidado:**
  - FF-01: Não exibe quem reservou cada horário. Não exibe disponibilidade de mais de uma unidade na mesma tela. Não sincroniza com agendas externas.
  - FF-02: Não desconta nem verifica créditos de horas do plano. Não cobra excedente. Não permite reservar em nome de outro membro. Não cria reservas recorrentes. Não libera fechadura de sala.
  - FF-03: Não aplica antecedência mínima nem penalidade de cancelamento. Não permite editar a reserva; alterar exige cancelar e reservar de novo. Não exibe reservas passadas.
- **Ressalvas de viabilidade técnica:** FF-02 exige garantia de não sobreposição no banco e carga inicial da planilha; esforço revisado de 5 para 8.

## 3. Interface (Módulo 5)

- **Telas:** T-01 Disponibilidade, T-02 Confirmar reserva, T-03 Reserva confirmada, T-04 Minhas reservas.
- **Componentes obrigatórios:** grade de horários, seletores, botões, modal de confirmação, toast.
- **Lacunas do Design System:** biblioteca do sistema de membros não fornecida; todos os componentes provisórios.
- **Resultado do teste de usabilidade:** não executado.

## 4. Handoff (Módulo 6)

- **Issues:** FF-01, FF-02, FF-03.
- **Plano de instrumentação:** `reserva_criada` (canal), `reserva_conflito_bloqueado`, `disponibilidade_consultada`, `reserva_cancelada`; conflitos e não comparecimento por registro manual da recepção. Linhas de base de KR1 e KR2 coletadas; KR3 a coletar.
- **Pendências `[a validar com o time técnico]`:** todos os contratos de API; restrição de não sobreposição no banco; carga inicial da planilha.

## 5. Pós-entrega (Módulos 7 e 8)

- **Achados priorizados:** A2 (rage click em "Confirmar reserva", defeito em relação à especificação) e A1 (dead click em células ocupadas).
- **Experimentos:** EXP-01 — destaque do próximo horário livre; aguardando as correções I1 e I2, a nova linha de base e o cálculo de amostra.

## Dúvidas abertas

| # | Dúvida | Quem pode responder | Módulo de origem |
| :--- | :--- | :--- | :--- |
| D1 | Regra de cancelamento | Helena | 1 |
| D2 | Administrador de empresa pode reservar por funcionários? | Helena | 1 |
| D3 | Quem é o encarregado de dados? | Helena, com o jurídico | 1 |
| D4 | Exigências contratuais ou regulatórias sobre dados dos membros | Jurídico | 1 |
| D5 | Integração com agenda externa neste ciclo? | Helena e Bianca | 1 |
| D6 | A medição manual de não comparecimento (KR3) foi iniciada? | Rui | 7 |

## Registro de revisões

| Data | Artefato | O que mudou | Motivo |
| :--- | :--- | :--- | :--- |
| 2026-11-04 | `06-handoff.md` | Incluída a medida manual do KR3 no Plano de Instrumentação | Apontamento R-01 da revisão independente |
| 2027-02-12 | `01-discovery.md` (Matriz CSD) | S1 reclassificada como Certeza provisória; S4 com evidência favorável | Resultados de produção (Módulo 7) |

# Módulo 4 — Feature Frames: Reserva de salas (exemplo fictício)

**Entrada:** `contexto.md`, `03-modelagem.md`. As etapas 2B e 3B não foram executadas.

## Catálogo de Feature Frames

### FF-01 — Consulta de disponibilidade

| | |
| :--- | :--- |
| **Estágio da jornada** | J1 |
| **Key Result relacionado** | KR2 |
| **Dor atendida** | P2 |
| **Hipótese de origem e situação** | H4 — não validada (afeta apenas o padrão de exibição) |
| **Contexto** | O membro autenticado acessa a área de salas no sistema web. |
| **Problema** | Só é possível saber se há sala livre perguntando à recepção. |
| **Solução** | Grade com as salas da unidade selecionada, por dia e faixa de horário, indicando livre ou ocupado. Abre no dia corrente. |
| **MVP** | Sim |
| **Valor (1–5)** | 4 |
| **Confiança** | Alta — a dor P2 é relato direto e o processo atual é Certeza (C3) |
| **Esforço (Fibonacci)** | 3 |

**Out of Scope (Limites Rígidos):**

- Não exibe quem reservou cada horário.
- Não exibe disponibilidade de mais de uma unidade na mesma tela.
- Não sincroniza com agendas externas.

---

### FF-02 — Reserva por autoatendimento com bloqueio de conflito

| | |
| :--- | :--- |
| **Estágio da jornada** | J2, J5 |
| **Key Result relacionado** | KR1, KR2 |
| **Dor atendida** | P1 |
| **Hipótese de origem e situação** | H1 e H2 — não validadas `[não validada]` |
| **Contexto** | O membro seleciona um horário livre na grade de disponibilidade. |
| **Problema** | A anotação manual permite duas reservas para a mesma sala no mesmo horário. |
| **Solução** | O membro confirma sala, data, início e fim. O sistema grava a reserva somente se o intervalo estiver livre; se outro membro reservou antes, informa o conflito e mantém a grade atualizada. |
| **MVP** | Sim |
| **Valor (1–5)** | 5 |
| **Confiança** | Alta para a dor (C2); a adesão ao autoatendimento (H1) permanece não validada |
| **Esforço (Fibonacci)** | 5 |

**Out of Scope (Limites Rígidos):**

- Não desconta nem verifica créditos de horas do plano.
- Não cobra excedente.
- Não permite reservar em nome de outro membro.
- Não cria reservas recorrentes.
- Não libera fechadura de sala.

---

### FF-03 — Minhas reservas e cancelamento

| | |
| :--- | :--- |
| **Estágio da jornada** | J3, J4 |
| **Key Result relacionado** | KR1 |
| **Dor atendida** | P1 |
| **Hipótese de origem e situação** | Sem hipótese associada |
| **Contexto** | O membro quer conferir ou desistir de uma reserva futura. |
| **Problema** | Reserva não utilizada continua bloqueando a sala. |
| **Solução** | Lista das reservas futuras do membro, com opção de cancelar. O horário cancelado volta a ficar livre na grade. |
| **MVP** | Sim |
| **Valor (1–5)** | 3 |
| **Confiança** | Média — a regra de cancelamento está indefinida (D1) |
| **Esforço (Fibonacci)** | 2 |

**Out of Scope (Limites Rígidos):**

- Não aplica antecedência mínima nem penalidade de cancelamento.
- Não permite editar a reserva; alterar exige cancelar e reservar de novo.
- Não exibe reservas passadas.

---

### FF-04 — Saldo de créditos de horas

| | |
| :--- | :--- |
| **Estágio da jornada** | J2 |
| **Key Result relacionado** | KR2 |
| **Dor atendida** | P3 |
| **Hipótese de origem e situação** | Sem hipótese associada |
| **Contexto** | O membro quer saber quantas horas de sala ainda tem no mês. |
| **Problema** | O saldo de créditos só existe na planilha da recepção (C6). |
| **Solução** | Exibição do saldo de horas do plano e desconto a cada reserva. |
| **MVP** | Não |
| **Valor (1–5)** | 3 |
| **Confiança** | Média |
| **Esforço (Fibonacci)** | 8 |

**Out of Scope (Limites Rígidos):**

- Não cobra excedente.
- Não permite compra de créditos avulsos.

---

### FF-05 — Registro de comparecimento

| | |
| :--- | :--- |
| **Estágio da jornada** | J5 |
| **Key Result relacionado** | KR3 |
| **Dor atendida** | Nenhuma dor validada; deriva de S2 |
| **Hipótese de origem e situação** | H3 — não validada `[não validada]` |
| **Contexto** | Início do horário reservado. |
| **Problema** | Não há registro de não comparecimento (E008). |
| **Solução** | A recepção marca no sistema se o membro compareceu. |
| **MVP** | Não |
| **Valor (1–5)** | 3 |
| **Confiança** | Baixa |
| **Esforço (Fibonacci)** | 5 |

**Out of Scope (Limites Rígidos):**

- Não libera a sala automaticamente por não comparecimento.
- Não aplica penalidade ao membro.
- Não usa fechadura nem sensor de presença.

---

## Checagem de viabilidade técnica

| Feature Frame | Esforço proposto | Esforço revisado | Dependências e restrições | Risco técnico | Parecer |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FF-01 | 3 | 3 | Cadastro de salas e unidades ainda não existe no sistema | Baixo | Viável |
| FF-02 | 5 | 8 | Bloqueio de conflito precisa ser garantido no banco, não apenas na interface; carga inicial das reservas da planilha | Médio | Viável com ressalva |
| FF-03 | 2 | 2 | Depende de D1; implementado sem regra de antecedência | Baixo | Viável |
| FF-04 | 8 | 8 | Migração dos saldos da planilha; regras de plano não documentadas | Alto | Viável com ressalva |
| FF-05 | 5 | 5 | Sem integração com fechaduras (E017); registro manual | Médio | Viável |

**Responsável pela checagem:** agente `handoff-tech-lead` — 04/11/2026. Parecer preliminar: o esquema atual do banco não foi fornecido. `[a validar com o time técnico]`

## Matriz de priorização

Índice = Valor × Confiança ÷ Esforço revisado (Alta = 1,0; Média = 0,7; Baixa = 0,4).

| Ordem | Feature Frame | Estágio | Key Result | Valor | Confiança | Esforço | Índice | MVP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | FF-01 | J1 | KR2 | 4 | Alta | 3 | 1,33 | Sim |
| 2 | FF-03 | J3, J4 | KR1 | 3 | Média | 2 | 1,05 | Sim |
| 3 | FF-02 | J2, J5 | KR1, KR2 | 5 | Alta | 8 | 0,63 | Sim |
| 4 | FF-04 | J2 | KR2 | 3 | Média | 8 | 0,26 | Não |
| 5 | FF-05 | J5 | KR3 | 3 | Baixa | 5 | 0,24 | Não |

FF-02 tem índice menor que FF-03, mas permanece no MVP: sem ele a jornada não se completa e o KR1 não se move.

## Recorte de MVP

- **Entra no MVP:** FF-01, FF-02, FF-03.
- **Ciclos seguintes:** FF-04, FF-05.
- **Candidatos fora do ciclo:** integração com Google Agenda (E015, sem decisão — D5); cobrança automática de excedente (E013, bloqueada por E014).

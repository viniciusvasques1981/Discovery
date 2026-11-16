# Contexto: Reserva de salas (exemplo fictício)

> Índice de decisões da iniciativa. Cada módulo acrescenta ou atualiza apenas a própria seção, em linhas curtas. Detalhes ficam nos artefatos. Aprovações ficam em `aprovacoes.md`.

| | |
| :--- | :--- |
| **Slug** | `exemplo-reserva-salas` |
| **Sponsor** | Helena (Diretora de Operações) |
| **Trilha** | Expressa |
| **Módulo atual** | 8 — plano de experimento elaborado; execução pendente |
| **Última atualização** | 2027-02-15 |

## 1–2. Por quê

- **Propósito:** O membro precisa confiar que a sala reservada estará disponível quando chegar.
- **Visão de Produto:** Módulo de autoatendimento do sistema de membros que mostra a disponibilidade das 14 salas e garante uma única reserva por horário.
- **Dores validadas:** P1 — conflito de reserva (41 em outubro/2026); P2 — disponibilidade invisível ao membro; P3 — recepção ocupada com reservas (não quantificada).
- **OKRs:** KR1 — conflitos por mês de 41 para 0; KR2 — reservas por autoatendimento de 0% para 70%; KR3 — medição de não comparecimento ativa, com 4 semanas de dados.
- **Restrições:** sistema web existente (React, Node, Postgres); 3 desenvolvedores; sem pagamento, fechaduras ou agenda externa neste ciclo; dados pessoais já existentes no cadastro, responsável por privacidade não identificado.
- **Hipóteses:** H1 — evidência favorável em produção (81,9% em duas semanas); H2 — evidência favorável (0 conflitos em duas semanas); H3 — não validada; H4 — não validada.
- **Detalhes:** `evidencias.md`, `01-discovery.md`, `02-estrategia.md`

## 3–4. Usuário e escopo

- **Protopersona:** membro que organiza reuniões da equipe e reserva perto do horário de uso.
- **Jornada To-Be:** J1 — Consultar; J2 — Reservar; J3 — Acompanhar; J4 — Cancelar; J5 — Usar a sala.
- **MVP:** FF-01 — Consulta de disponibilidade; FF-02 — Reserva por autoatendimento com bloqueio de conflito; FF-03 — Minhas reservas e cancelamento.
- **Fora do MVP:** FF-04 — Saldo de créditos; FF-05 — Registro de comparecimento.
- **Ressalvas de viabilidade:** FF-02 exige garantia de não sobreposição no banco e carga inicial da planilha; esforço revisado de 5 para 8.
- **Detalhes e Out of Scope:** `03-modelagem.md`, `04-feature-frames.md`

## 5. Interface

- **Telas:** T-01 — Disponibilidade; T-02 — Confirmar reserva; T-03 — Reserva confirmada; T-04 — Minhas reservas.
- **Lacunas do Design System:** biblioteca do sistema de membros não fornecida; componentes provisórios.
- **Teste de usabilidade:** não executado.
- **Detalhes:** `05-prototipacao.md`

## 6. Handoff

- **Issues:** FF-01, FF-02, FF-03.
- **Instrumentação:** `reserva_criada`, `reserva_conflito_bloqueado`, `disponibilidade_consultada`, `reserva_cancelada`; conflitos e não comparecimento por registro manual. Linha de base do KR3 a coletar.
- **Pendências técnicas:** contratos de API, restrição de não sobreposição no banco e carga inicial da planilha, a validar com o time.
- **Detalhes:** `06-handoff.md`

## 7–8. Pós-entrega

- **Achados priorizados:** A2 — rage click em "Confirmar reserva" (defeito em relação à especificação); A1 — dead click em células ocupadas (tratado no ajuste AJ-01).
- **Experimentos:** EXP-01 — destaque do próximo horário livre; aguarda as correções I1 e I2, nova linha de base e cálculo de amostra.

## Dúvidas abertas

| # | Dúvida | Quem pode responder |
| :--- | :--- | :--- |
| D1 | Regra de cancelamento | Helena |
| D2 | Administrador de empresa pode reservar por funcionários? | Helena |
| D3 | Quem é o encarregado de dados? | Helena, com o jurídico |
| D4 | Exigências contratuais ou regulatórias sobre dados dos membros | Jurídico |
| D5 | Integração com agenda externa neste ciclo? | Helena e Bianca |
| D6 | A medição manual de não comparecimento (KR3) foi iniciada? | Rui |

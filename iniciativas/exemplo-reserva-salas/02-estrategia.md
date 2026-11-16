# Módulo 2 — Estratégia: Reserva de salas (exemplo fictício)

**Entrada:** `01-discovery.md` e `contexto.md`

## Alinhamento Estratégico (Golden Circle)

- **Por quê (Propósito):** O membro precisa confiar que a sala reservada estará disponível quando chegar (P1, E004, E005).
- **Como (Diferencial):** Uma única fonte de disponibilidade, consultada e alterada pelo próprio membro, com bloqueio de conflito no momento da reserva `[inferência]` — decorre de P1, P2 e S4.
- **O quê (Entrega):** Reserva de salas por autoatendimento dentro do sistema web de membros existente (E010).

## Declaração de Visão de Produto

> Para **membros da Nimbo Coworking**, cujo **problema é não saber se há sala livre e perder salas já reservadas**, a **Reserva de Salas** é um **módulo de autoatendimento do sistema de membros** que **mostra a disponibilidade das 14 salas e garante que cada horário tenha uma única reserva**.

## Matriz de Hipóteses

| # | Suposição de origem | Hipótese | Sinal mensurável | Risco se falsa | Custo de validação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H1 | S1 | Acreditamos que a recepção será desonerada se os membros obtiverem autonomia de reserva por meio do autoatendimento web. | Ao menos 70% das reservas pelo canal de autoatendimento | Alto | Médio |
| H2 | S4 | Acreditamos que os conflitos serão eliminados se o sistema impedir duas reservas no mesmo horário. | Zero conflitos registrados no mês | Alto | Baixo — análise dos 41 registros de outubro |
| H3 | S2 | Acreditamos que a ocupação efetiva das salas aumentará se o não comparecimento for registrado e a sala for liberada. | Taxa de não comparecimento medida e em queda | Médio | Médio |
| H4 | S5 | Acreditamos que a consulta de disponibilidade precisa priorizar o dia corrente, porque os membros reservam no mesmo dia. | Maioria das reservas com antecedência inferior a 24 horas | Baixo | Baixo — análise da planilha de outubro |

Situação: nenhuma hipótese foi validada. A Etapa 2B não foi executada (ver `contexto.md`).

## Matriz de OKRs

**Objetivo:** Tornar a reserva de salas confiável e autônoma para o membro.

| Key Result | Tipologia de Medição | Linha de Base | Meta | Janela |
| :--- | :--- | :--- | :--- | :--- |
| KR1 — Reduzir os conflitos de reserva registrados por mês | Evolutivo | 41 em outubro/2026 (E003) | 0 (E004) | 1º mês completo após o lançamento |
| KR2 — Proporção das reservas feitas por autoatendimento | Razão | 0%: todas passam pela recepção (E002) | 70% (E009) | 2º mês após o lançamento |
| KR3 — Estabelecer a medição da taxa de não comparecimento | Instrumentação | Inexistente (E008) | Medição ativa com 4 semanas de dados | Até o fim do 1º mês após o lançamento |

A linha de base do KR1 refere-se a um único mês; a variação entre meses é desconhecida. O KR3 é de Instrumentação porque não há registro que permita definir meta para o não comparecimento.

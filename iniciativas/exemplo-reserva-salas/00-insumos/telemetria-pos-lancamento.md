# Telemetria pós-lançamento — Reserva de salas (FICTÍCIA)

> Conteúdo inventado para fins de demonstração.

## Ferramenta de sessão (resumo no formato de `scripts/clarity_resumo.py`)

- **Período:** 09/02/2027 a 11/02/2027 (3 dias)
- **Sessões no período:** 1.840
- **Segmento:** todos os dispositivos; sem quebra por unidade

| Métrica | URL | Sessões com a métrica | % das sessões |
| :--- | :--- | :--- | :--- |
| DeadClickCount | /disponibilidade | 388 | 21,1 |
| RageClickCount | /reservar | 212 | 11,5 |
| QuickbackClick | /reserva/confirmada | 169 | 9,2 |

Observação do time, a partir de 12 gravações de sessão assistidas:

- Em 9 das 12 gravações com dead click, o clique ocorreu sobre um bloco de horário ocupado na grade.
- Em 7 das 12 gravações com rage click, o botão "Confirmar reserva" foi clicado várias vezes e não houve mudança visual por mais de 1 segundo.

## Eventos do Plano de Instrumentação

- **Período:** 26/01/2027 a 08/02/2027 (2 semanas)

| Medida | Valor |
| :--- | :--- |
| Sessões com `disponibilidade_consultada` | 3.100 |
| `reserva_criada` com canal = autoatendimento | 1.054 |
| `reserva_criada` com canal = recepção | 233 |
| `reserva_conflito_bloqueado` | 67 |
| Conflitos registrados pela recepção | 0 |
| `reserva_cancelada` | 142 |

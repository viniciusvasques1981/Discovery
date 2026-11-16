# D1 — telemetria-pos-lancamento.md

D1:L0001 | # Telemetria pós-lançamento — Reserva de salas (FICTÍCIA)
D1:L0002 | > Conteúdo inventado para fins de demonstração.
D1:L0003 | ## Ferramenta de sessão (resumo no formato de `scripts/clarity_resumo.py`)
D1:L0004 | - **Período:** 09/02/2027 a 11/02/2027 (3 dias)
D1:L0005 | - **Sessões no período:** 1.840
D1:L0006 | - **Segmento:** todos os dispositivos; sem quebra por unidade
D1:L0007 | | Métrica | URL | Sessões com a métrica | % das sessões |
D1:L0008 | | :--- | :--- | :--- | :--- |
D1:L0009 | | DeadClickCount | /disponibilidade | 388 | 21,1 |
D1:L0010 | | RageClickCount | /reservar | 212 | 11,5 |
D1:L0011 | | QuickbackClick | /reserva/confirmada | 169 | 9,2 |
D1:L0012 | Observação do time, a partir de 12 gravações de sessão assistidas:
D1:L0013 | - Em 9 das 12 gravações com dead click, o clique ocorreu sobre um bloco de horário ocupado na grade.
D1:L0014 | - Em 7 das 12 gravações com rage click, o botão "Confirmar reserva" foi clicado várias vezes e não houve mudança visual por mais de 1 segundo.
D1:L0015 | ## Eventos do Plano de Instrumentação
D1:L0016 | - **Período:** 26/01/2027 a 08/02/2027 (2 semanas)
D1:L0017 | | Medida | Valor |
D1:L0018 | | :--- | :--- |
D1:L0019 | | Sessões com `disponibilidade_consultada` | 3.100 |
D1:L0020 | | `reserva_criada` com canal = autoatendimento | 1.054 |
D1:L0021 | | `reserva_criada` com canal = recepção | 233 |
D1:L0022 | | `reserva_conflito_bloqueado` | 67 |
D1:L0023 | | Conflitos registrados pela recepção | 0 |
D1:L0024 | | `reserva_cancelada` | 142 |

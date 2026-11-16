# Módulo 7 — Diagnóstico Comportamental: Reserva de salas (exemplo fictício)

| | |
| :--- | :--- |
| **Ferramenta** | Ferramenta de sessão e eventos do Plano de Instrumentação (`00-insumos/telemetria-pos-lancamento.md`) |
| **Período analisado** | Sessão: 09/02/2027 a 11/02/2027. Eventos: 26/01/2027 a 08/02/2027 |
| **Volume de sessões** | 1.840 (sessão); 3.100 sessões com consulta de disponibilidade (eventos) |
| **Segmento** | Todos os dispositivos; sem quebra por unidade |
| **Limitações dos dados** | Janela de 3 dias na ferramenta de sessão; 12 gravações assistidas; os dois conjuntos cobrem períodos diferentes |

## Tabela de Diagnóstico Comportamental

| # | Métrica avaliada | Elemento / tela afetada | Volume | Causa raiz (hipótese) | Nível de evidência | Heurística violada |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A1 | Dead Click | Células de horário ocupado em `/disponibilidade` (T-01) | 388 sessões (21,1%) | A célula ocupada é percebida como clicável; o usuário espera alguma resposta | Gravação de sessão: 9 de 12 gravações | Visibilidade do Estado do Sistema; affordance |
| A2 | Rage Click | Botão "Confirmar reserva" em `/reservar` (T-02) | 212 sessões (11,5%) | Ausência de mudança visual por mais de 1 segundo após o clique | Gravação de sessão: 7 de 12 gravações | Visibilidade do Estado do Sistema |
| A3 | Quick Back | `/reserva/confirmada` (T-03) | 169 sessões (9,2%) | Não determinada. Possibilidade: o usuário volta para fazer outra reserva pelo botão do navegador | Telemetria agregada | Não atribuída sem evidência adicional |

O achado A2 indica que o requisito "feedback visual em menos de 200ms" e o estado Loading do botão, especificados em `05-prototipacao.md`, não estão sendo atendidos em produção.

## Matriz de Intervenção de UX

| # | Achado | Solução técnica proposta | Microcopy de ajuste | Impacto esperado | Prioridade | Encaminhamento |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| I1 | A2 | Aplicar o estado Loading e desabilitar o botão no primeiro clique, conforme a especificação | "Reservando…" no botão durante a requisição | Alto | 1 | Correção direta — defeito em relação à especificação |
| I2 | A1 | Reduzir a aparência de elemento interativo da célula ocupada (sem cursor de ponteiro, sem hover) e reforçar o rótulo | "Ocupado" visível na célula | Médio | 2 | Correção direta |
| I3 | A1 | Ao abrir a grade, destacar o próximo horário livre do dia | "Próximo horário livre: [hora]" | Médio | 3 | Experimento — efeito sobre a conversão é incerto |
| I4 | A3 | Assistir gravações de sessões com quick back antes de propor intervenção | — | Não estimado | 4 | Investigação |

## Leitura dos Key Results

| Key Result | Resultado no período de eventos | Observação |
| :--- | :--- | :--- |
| KR1 | 0 conflitos registrados pela recepção; 67 tentativas bloqueadas | Duas semanas; a janela do KR é um mês completo |
| KR2 | 1.054 de 1.287 reservas por autoatendimento (81,9%) | Meta de 70% superada no período; a janela do KR é o 2º mês |
| KR3 | Sem dados no insumo | Verificar se a medição manual foi iniciada |

Conversão de consulta em reserva por autoatendimento: 1.054 em 3.100 sessões com consulta (34,0%). Parte das consultas não tem intenção de reserva, de modo que esse valor não é uma taxa de falha.

## Revisão da Matriz CSD

| Item | Classificação anterior | Nova classificação | Evidência |
| :--- | :--- | :--- | :--- |
| S1 — ao menos 70% reservarão por autoatendimento | Suposição | Certeza provisória | 81,9% em duas semanas; confirmar ao fim do 2º mês |
| S4 — conflitos decorrem da edição simultânea da planilha | Suposição | Suposição com evidência favorável | 0 conflitos após o bloqueio no sistema; a causa original não foi analisada |
| S2 — cerca de 20% de não comparecimento | Suposição | Suposição | Sem dados |

# Módulo 8 — Plano de Experimento: Reserva de salas (exemplo fictício)

## Ficha Técnica do Experimento

| | |
| :--- | :--- |
| **Identificador** | EXP-01 |
| **Origem** | Achado A1 e intervenção I3 de `07-diagnostico-comportamental.md` |
| **Hipótese Comportamental** | Se destacarmos o próximo horário livre do dia na abertura da grade (Variante B), então a proporção de sessões com consulta que terminam em reserva aumentará, porque o usuário deixa de percorrer a grade para localizar uma célula livre. A variação esperada não é estimada: não há dado que a sustente. |
| **Mecanismo Psicológico** | Redução de carga cognitiva na busca visual; efeito de opção padrão |

## Detalhamento das Variantes

| | Variante A (Controle) | Variante B (Tratamento) |
| :--- | :--- | :--- |
| **Descrição** | Grade atual, com as correções I1 e I2 já aplicadas | Grade atual com faixa "Próximo horário livre: [hora]" acima da grade e a célula correspondente destacada |
| **Elemento alterado** | — | Faixa informativa e destaque de uma célula |
| **Variáveis mantidas constantes** | Ordem das salas, cores de estado, fluxo de confirmação | As mesmas |

As correções I1 e I2 devem estar em produção antes do início, para que o controle não inclua defeitos já diagnosticados.

## Painel de Métricas

| Tipo | Métrica | Linha de base | Direção esperada | Limite |
| :--- | :--- | :--- | :--- | :--- |
| Primária | Sessões com `disponibilidade_consultada` que resultam em `reserva_criada` por autoatendimento | 34,0% (1.054 de 3.100, em 26/01 a 08/02/2027), medida antes de I1 e I2 | Aumentar | — |
| Secundária | Tempo entre a consulta e a reserva | `[pendente de dados]` | Diminuir | — |
| Secundária | Sessões com dead click em `/disponibilidade` | 21,1% (antes de I2) | Diminuir | — |
| Guardiã | `reserva_cancelada` ÷ `reserva_criada` | 142 de 1.287 (11,0%) | Não degradar | Limite a definir pelo time antes do início |
| Guardiã | Conflitos registrados pela recepção | 0 | Não degradar | 0 |
| Guardiã | Concentração de reservas na primeira sala da grade | `[pendente de dados]` | Não degradar | A definir |

A linha de base da métrica primária deve ser medida novamente após I1 e I2; o valor de 34,0% é anterior às correções.

## Critérios de Amostragem

| | |
| :--- | :--- |
| **Público elegível** | Membros autenticados que abrem a grade de disponibilidade |
| **Gatilho de ativação** | Carregamento da tela T-01 |
| **Condições de exclusão** | Reservas feitas pela recepção (`canal = recepcao`) |
| **Divisão de tráfego** | 50% / 50%, por membro, para que a mesma pessoa veja sempre a mesma variante |
| **Efeito mínimo detectável** | `[pendente de dados]` — a definir pelo time |
| **Significância / poder** | 5% / 80% (convenção usual; confirmar com o time) |
| **Tamanho de amostra por variante** | `[pendente de dados]` — calcular na ferramenta de experimentação com a linha de base atualizada e o efeito mínimo definido |
| **Duração mínima** | 2 semanas completas, para cobrir os ciclos de dia da semana |
| **Critério de parada** | Qualquer conflito registrado ou métrica guardiã além do limite definido |

O volume observado (cerca de 3.100 sessões com consulta em duas semanas) pode ser insuficiente para detectar efeitos pequenos. Se o cálculo indicar duração inviável, o experimento deve ser substituído por teste de usabilidade com protótipo.

## Critério de Decisão

| Resultado | Decisão |
| :--- | :--- |
| Primária melhora com significância e guardiãs estáveis | Implementar a Variante B para todos |
| Primária sem diferença significativa | Descartar; manter a grade atual |
| Concentração de reservas em uma sala acima do limite | Iterar: rever o critério de escolha do "próximo horário livre" |
| Guardiã degrada além do limite | Interromper |

## Resultado (preencher após a execução)

| | |
| :--- | :--- |
| **Período executado** | |
| **Amostra obtida** | |
| **Resultado da métrica primária** | |
| **Métricas guardiãs** | |
| **Decisão** | |
| **Reclassificação na Matriz CSD** | |

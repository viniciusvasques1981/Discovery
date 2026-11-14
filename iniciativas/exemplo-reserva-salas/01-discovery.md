# Módulo 1 — Discovery: Reserva de salas (exemplo fictício)

**Insumos analisados:** `00-insumos/transcricao-imersao.md` — imersão de 03/11/2026, com Helena (sponsor), Rui (Recepção), Bianca (Tech Lead) e Caio (membro). As origens citam a linha da transcrição.

## Download do Problema

### Cenário atual

A Nimbo Coworking opera 3 unidades com 14 salas de reunião (L01). As reservas são pedidas pelo WhatsApp da recepção e anotadas em uma planilha compartilhada entre as unidades (L02). O controle dos créditos de horas de cada plano é manual e fica na mesma planilha (L13). O membro só sabe se há sala livre perguntando à recepção (L06).

### Premissas

- O membro reservaria sozinho se pudesse fazê-lo pelo celular (L09).
- A solução deve estar em produção até o fim do trimestre (L12).

### Limitações técnicas

- Sistema de membros existente: web, React, API em Node e Postgres, com login por e-mail e senha; não há app nativo (L10).
- Time de 3 desenvolvedores (L11).
- Gateway de pagamento fora do trimestre; cobrança automática de excedente não será feita (L14).
- Fechaduras das salas sem integração (L17).
- Integração com agenda externa pedida, sem decisão (L15, L16).

### Dados pessoais e conformidade

| Pergunta | Resposta | Origem |
| :--- | :--- | :--- |
| A iniciativa trata dados pessoais? Quais? | Sim: nome, e-mail e telefone dos membros, já existentes no cadastro | L18 |
| Há dados pessoais sensíveis ou de crianças e adolescentes? | Não mencionado — ver D4 | — |
| Quem são os titulares? | Membros do coworking | L18 |
| Há exigência regulatória, contratual ou de segurança citada? | Não mencionada — ver D4 | — |
| Quem responde por privacidade e segurança na organização? | Desconhecido; jurídico terceirizado — ver D3 | L19 |

## Matriz CSD

### Certezas

| # | Certeza | Evidência | Origem |
| :--- | :--- | :--- | :--- |
| C1 | Há 3 unidades e 14 salas de reunião | Declaração da Diretora de Operações sobre a estrutura | L01 |
| C2 | Em outubro houve 612 reservas e 41 conflitos registrados | Planilha de reservas, coluna de ocorrências | L03 |
| C3 | Todas as reservas passam pela recepção, via WhatsApp e planilha | Descrição do processo pelo coordenador que o executa | L02 |
| C4 | O sistema de membros é web (React, Node, Postgres) com login existente | Declaração da Tech Lead | L10 |
| C5 | Cobrança automática e integração com fechaduras estão fora do alcance técnico do trimestre | Declaração da Tech Lead | L14, L17 |
| C6 | O controle de créditos de horas é manual | Declaração da sponsor | L13 |

41 conflitos em 612 reservas correspondem a 6,7% `[inferência]` — cálculo sobre C2; refere-se a um único mês.

### Suposições

| # | Suposição (afirmação falseável) | Como validar | Origem |
| :--- | :--- | :--- | :--- |
| S1 | Ao menos 70% dos membros farão a reserva por autoatendimento quando ele existir | Medir o canal das reservas após o lançamento; antes, entrevista ou fake door | L09 |
| S2 | Cerca de 20% das reservas resultam em não comparecimento | Registrar comparecimento por 4 semanas | L08 |
| S3 | A recepção gasta cerca de 2 horas por dia, por unidade, com reservas | Medição de tempo por amostragem em uma semana | L07 |
| S4 | Os conflitos decorrem da edição simultânea da planilha pelas unidades | Analisar os 41 registros de outubro | L02, L03 `[inferência]` |
| S5 | Membros reservam predominantemente no mesmo dia | Analisar a antecedência das 612 reservas de outubro | L22 (relato de um membro) |

### Dúvidas

| # | Dúvida (pergunta objetiva) | Quem pode responder | Origem |
| :--- | :--- | :--- | :--- |
| D1 | Qual é a regra de cancelamento (antecedência mínima e devolução de créditos)? | Helena | L20 |
| D2 | O administrador de uma empresa membro pode reservar em nome dos funcionários? | Helena | L21 |
| D3 | Quem é o encarregado de dados da Nimbo? | Helena, com o jurídico terceirizado | L19 |
| D4 | Há exigência contratual ou regulatória sobre os dados dos membros além do cadastro atual? | Jurídico terceirizado | L19 |
| D5 | Haverá integração com agenda externa neste ciclo? | Helena e Bianca | L15, L16 |

## Dores Validadas do Negócio/Operação

| # | Dor | Quem sofre | Evidência | Impacto no negócio |
| :--- | :--- | :--- | :--- | :--- |
| P1 | Conflito de reserva: duas equipes com a mesma sala no mesmo horário | Membros | 41 conflitos em outubro (L03); membro perdeu a sala 2 vezes em um mês (L05) | Principal motivo de reclamação, segundo a sponsor (L04) |
| P2 | Disponibilidade invisível: o membro precisa perguntar para saber se há sala livre | Membros | Relato de membro, com demora na resposta (L06) | Não quantificado nos insumos |
| P3 | Recepção ocupada com o atendimento de reservas | Equipe de recepção | Relato do coordenador (L07); tempo não medido | Não quantificado — depende de S3 |

O não comparecimento (L08) não entra como dor validada: não há registro, apenas estimativa. Está em S2.

## Dúvidas prioritárias

1. D1 — a regra de cancelamento define o comportamento de uma funcionalidade provável do MVP.
2. D2 — altera o modelo de permissões.
3. D3 — sem responsável por privacidade, a seção de conformidade do handoff fica sem validador.

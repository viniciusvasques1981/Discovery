# Módulo 1 — Discovery: Reserva de salas (exemplo fictício)

**Entrada:** `evidencias.md` (22 evidências extraídas da transcrição da imersão de 03/11/2026). A coluna Origem cita identificadores de evidência.

## Download do Problema

### Cenário atual

A Nimbo Coworking opera 3 unidades com 14 salas de reunião (E001). As reservas são pedidas pelo WhatsApp da recepção e anotadas em uma planilha compartilhada entre as unidades (E002). O controle dos créditos de horas de cada plano é manual e fica na mesma planilha (E013). O membro só sabe se há sala livre perguntando à recepção (E006).

### Premissas

- O membro reservaria sozinho se pudesse fazê-lo pelo celular (E009).
- A solução deve estar em produção até o fim do trimestre (E012).

### Limitações técnicas

- Sistema de membros existente: web, React, API em Node e Postgres, com login por e-mail e senha; não há app nativo (E010).
- Time de 3 desenvolvedores (E011).
- Gateway de pagamento fora do trimestre; cobrança automática de excedente não será feita (E014).
- Fechaduras das salas sem integração (E017).
- Integração com agenda externa pedida, sem decisão (E015, E016).

### Dados pessoais e conformidade

| Pergunta | Resposta | Origem |
| :--- | :--- | :--- |
| A iniciativa trata dados pessoais? Quais? | Sim: nome, e-mail e telefone dos membros, já existentes no cadastro | E018 |
| Há dados pessoais sensíveis ou de crianças e adolescentes? | Não mencionado — ver D4 | — |
| Quem são os titulares? | Membros do coworking | E018 |
| Há exigência regulatória, contratual ou de segurança citada? | Não mencionada — ver D4 | — |
| Quem responde por privacidade e segurança na organização? | Desconhecido; jurídico terceirizado — ver D3 | E019 |

## Matriz CSD

### Certezas

| # | Certeza | Evidência | Origem |
| :--- | :--- | :--- | :--- |
| C1 | Há 3 unidades e 14 salas de reunião | Declaração da Diretora de Operações sobre a estrutura | E001 |
| C2 | Em outubro houve 612 reservas e 41 conflitos registrados | Planilha de reservas, coluna de ocorrências | E003 |
| C3 | Todas as reservas passam pela recepção, via WhatsApp e planilha | Descrição do processo pelo coordenador que o executa | E002 |
| C4 | O sistema de membros é web (React, Node, Postgres) com login existente | Declaração da Tech Lead | E010 |
| C5 | Cobrança automática e integração com fechaduras estão fora do alcance técnico do trimestre | Declaração da Tech Lead | E014, E017 |
| C6 | O controle de créditos de horas é manual | Declaração da sponsor | E013 |

41 conflitos em 612 reservas correspondem a 6,7% `[inferência]` — cálculo sobre C2; refere-se a um único mês.

### Suposições

| # | Suposição (afirmação falseável) | Como validar | Origem |
| :--- | :--- | :--- | :--- |
| S1 | Ao menos 70% dos membros farão a reserva por autoatendimento quando ele existir | Medir o canal das reservas após o lançamento; antes, entrevista ou fake door | E009 |
| S2 | Cerca de 20% das reservas resultam em não comparecimento | Registrar comparecimento por 4 semanas | E008 |
| S3 | A recepção gasta cerca de 2 horas por dia, por unidade, com reservas | Medição de tempo por amostragem em uma semana | E007 |
| S4 | Os conflitos decorrem da edição simultânea da planilha pelas unidades | Analisar os 41 registros de outubro | E002, E003 `[inferência]` |
| S5 | Membros reservam predominantemente no mesmo dia | Analisar a antecedência das 612 reservas de outubro | E022 (relato de um membro) |

### Dúvidas

| # | Dúvida (pergunta objetiva) | Quem pode responder | Origem |
| :--- | :--- | :--- | :--- |
| D1 | Qual é a regra de cancelamento (antecedência mínima e devolução de créditos)? | Helena | E020 |
| D2 | O administrador de uma empresa membro pode reservar em nome dos funcionários? | Helena | E021 |
| D3 | Quem é o encarregado de dados da Nimbo? | Helena, com o jurídico terceirizado | E019 |
| D4 | Há exigência contratual ou regulatória sobre os dados dos membros além do cadastro atual? | Jurídico terceirizado | E019 |
| D5 | Haverá integração com agenda externa neste ciclo? | Helena e Bianca | E015, E016 |

## Dores Validadas do Negócio/Operação

| # | Dor | Quem sofre | Evidência | Impacto no negócio |
| :--- | :--- | :--- | :--- | :--- |
| P1 | Conflito de reserva: duas equipes com a mesma sala no mesmo horário | Membros | 41 conflitos em outubro (E003); membro perdeu a sala 2 vezes em um mês (E005) | Principal motivo de reclamação, segundo a sponsor (E004) |
| P2 | Disponibilidade invisível: o membro precisa perguntar para saber se há sala livre | Membros | Relato de membro, com demora na resposta (E006) | Não quantificado nos insumos |
| P3 | Recepção ocupada com o atendimento de reservas | Equipe de recepção | Relato do coordenador (E007); tempo não medido | Não quantificado — depende de S3 |

O não comparecimento (E008) não entra como dor validada: não há registro, apenas estimativa. Está em S2.

## Dúvidas prioritárias

1. D1 — a regra de cancelamento define o comportamento de uma funcionalidade provável do MVP.
2. D2 — altera o modelo de permissões.
3. D3 — sem responsável por privacidade, a seção de conformidade do handoff fica sem validador.

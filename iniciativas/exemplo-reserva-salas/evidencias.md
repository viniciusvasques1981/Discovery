# Base de Evidências: Reserva de salas (exemplo fictício)

> Fatos e declarações extraídos dos insumos, cada um com a linha de origem. É a única fonte que os módulos seguintes consultam: o material bruto em `00-insumos/` não é relido depois do Módulo 1.

**Insumos processados:** ver `00-insumos/numerados/INDICE.md` — D2, transcrição da imersão de 03/11/2026.

| ID | Evidência | Tipo | Fonte | Ref |
| :--- | :--- | :--- | :--- | :--- |
| E001 | A Nimbo tem 3 unidades e 14 salas de reunião no total. | Dado | Helena | D2:L0005 |
| E002 | Toda reserva chega pelo WhatsApp da recepção e é anotada em uma planilha compartilhada entre as três unidades. | Relato | Rui | D2:L0006 |
| E003 | A planilha de outubro registra 612 reservas e 41 conflitos (duas pessoas com a mesma sala no mesmo horário). | Dado | Rui, planilha de reservas | D2:L0007 |
| E004 | A sponsor quer zerar o conflito de reserva e afirma que é o que mais gera reclamação. | Declaração | Helena | D2:L0008 |
| E005 | No último mês, o membro perdeu duas vezes uma sala reservada, ocupada por outra equipe. | Relato | Caio | D2:L0009 |
| E006 | O membro só descobre se há sala livre perguntando no WhatsApp, e a resposta às vezes demora. | Relato | Caio | D2:L0010 |
| E007 | O coordenador estima que a recepção gasta cerca de duas horas por dia, por unidade, com mensagens de reserva; o tempo nunca foi medido. | Declaração | Rui | D2:L0011 |
| E008 | O coordenador estima que cerca de 20% das reservas resultam em não comparecimento; não há registro. | Declaração | Rui | D2:L0012 |
| E009 | A sponsor acredita que o membro reservará sozinho pelo celular e considera que 70% de reservas por autoatendimento liberam a recepção. | Declaração | Helena | D2:L0013 |
| E010 | O sistema de membros atual é web (React, API em Node, Postgres), tem login por e-mail e senha e não tem app nativo. | Restrição | Bianca | D2:L0014 |
| E011 | O time tem três desenvolvedores. | Restrição | Bianca | D2:L0015 |
| E012 | A sponsor precisa da solução em produção até o fim do trimestre. | Restrição | Helena | D2:L0016 |
| E013 | Os planos dão créditos mensais de horas de sala, controlados manualmente na planilha; a sponsor quer cobrar o excedente automaticamente. | Pedido | Helena | D2:L0017 |
| E014 | Gateway de pagamento não entra neste trimestre; cobrança automática fica fora. | Decisão | Bianca | D2:L0018 |
| E015 | O membro sugere integração com o Google Agenda. | Pedido | Caio | D2:L0019 |
| E016 | A integração com agenda foi pedida, mas não há decisão. | Declaração | Bianca | D2:L0020 |
| E017 | As fechaduras das salas não têm integração; não é possível liberar porta pelo sistema. | Restrição | Bianca | D2:L0021 |
| E018 | O cadastro de membros já guarda nome, e-mail e telefone. | Dado | Bianca | D2:L0022 |
| E019 | A sponsor não sabe quem é o encarregado de dados; o jurídico é terceirizado. | Declaração | Helena | D2:L0023 |
| E020 | Não há regra escrita de cancelamento; cada unidade faz de um jeito. | Relato | Rui | D2:L0024 |
| E021 | Empresas membro têm um administrador; não está definido se ele pode reservar em nome dos funcionários. | Declaração | Helena | D2:L0025 |
| E022 | O membro quase sempre reserva de última hora, no mesmo dia. | Relato | Caio | D2:L0026 |

Os dados de uso posteriores à entrega (D1, `telemetria-pos-lancamento.md`) são insumo direto dos Módulos 7 e 8 e não fazem parte desta base.

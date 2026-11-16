# Aprovações e Registro: Reserva de salas (exemplo fictício)

> Arquivo de registro. Recebe linhas novas; linhas existentes não são reescritas. Não é lido pelos agentes de módulo.

## Aprovações

| Módulo | Aprovador (papel) | Nome | Data | Verificação | Revisão independente | Pendências aceitas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Sponsor | Helena | 2026-11-03 | Sem erros | — | — |
| 2 — Estratégia | Sponsor | Helena | 2026-11-03 | Sem erros | Aprovado com ressalvas | Linha de base do KR1 de um único mês |
| 3 — Modelagem | Product Manager | Helena (acumula o papel) | 2026-11-04 | Sem erros | — | Protopersona baseada em um único membro |
| 4 — Feature Frame | Product Manager e Tech Lead | Helena e Bianca | 2026-11-04 | Sem erros | Aprovado | Esforço de FF-02 a confirmar com o esquema do banco |
| 5 — Prototipação | Product Designer | Helena (sem designer no time) | 2026-11-04 | Sem erros | — | Design System não fornecido |
| 6 — Handoff | Tech Lead | Bianca | 2026-11-04 | 1 erro, corrigido | Aprovado com ressalvas | Responsável por privacidade não identificado (D3) |
| 7 — Medição | Product Manager | Helena | 2027-02-12 | Sem erros | — | Janela de 3 dias na ferramenta de sessão |
| 8 — Experimentação | Product Manager | Pendente | — | Sem erros | Aprovado com ressalvas | — |

## Etapas opcionais

| Etapa | Executada | Decisão de quem | Motivo / risco aceito |
| :--- | :--- | :--- | :--- |
| 2B — Validação de Hipóteses | Não | Helena | Prazo do trimestre (E012). Risco aceito: H1 (adesão ao autoatendimento) só será verificada em produção, pelo KR2 |
| 3B — Árvore de Oportunidades | Não | Helena | As dores levam a uma solução direta; não havia soluções concorrentes na imersão |
| 5B — Teste de Usabilidade | Não | Helena | Prazo. Risco aceito: problemas de usabilidade detectados só no Módulo 7 — o que ocorreu (achados A1 e A2) |

## Alterações em artefatos já aprovados

| Data | Artefato | O que mudou | Motivo |
| :--- | :--- | :--- | :--- |
| 2026-11-04 | `06-handoff.md` | Incluída a medida manual do KR3 no Plano de Instrumentação | Erro apontado por `iniciativa.py verificar`: KR3 sem evento |
| 2027-02-12 | `01-discovery.md` (Matriz CSD) | S1 reclassificada como Certeza provisória; S4 com evidência favorável | Resultados de produção (Módulo 7) |
| 2027-02-15 | `ajustes/AJ-01-celula-ocupada.md` | Célula de horário ocupado perde a aparência interativa (trilha pocket) | Dead click em 21,1% das sessões (achado A1) |

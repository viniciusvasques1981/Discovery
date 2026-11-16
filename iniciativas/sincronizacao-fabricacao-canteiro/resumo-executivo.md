# Resumo Executivo — OptiObra Core

> **Simulação fictícia de Product Discovery.** Cenário, respostas, evidências, resultados, números e decisões deste documento foram simulados para demonstrar a esteira. Não representam entrevistas, workshop, validações, aprovações ou resultados de uma organização real.

## Síntese

O OptiObra Core foi concebido como uma solução para melhorar a coordenação entre planejamento de fabricação e execução de montagem no canteiro. O cenário simulado aponta fragmentação de informação, alterações de projeto acompanhadas manualmente, baixa visibilidade de componentes e dependência de planilhas e integrações incompletas.

A proposta de MVP concentra-se em três capacidades: (1) painel de sincronização fábrica–canteiro; (2) visualização dos impactos conhecidos de alterações de projeto; e (3) status de componentes, formas e ferramental por frente. A arquitetura adicional de App Operacional — incluindo autenticação, RBAC, operação offline, captura de fotos e notificações — permanece proposta sujeita à decisão de escopo e à validação técnica, de segurança e privacidade.

## Etapas realizadas na simulação

| Etapa | Trabalho realizado | Resultado / status |
| :--- | :--- | :--- |
| 0 — Entrada de insumos | Organizados como insumo fictício o roteiro de entrevista B2B e o workshop de alinhamento, incluindo cenário operacional e fontes de dados mencionadas. | Insumo de demonstração; não houve entrevista nem workshop reais. |
| 1 — Discovery | Estruturado cenário atual, premissas, limitações, Matriz CSD, dores e dúvidas prioritárias. | Dores simuladas: ruptura fábrica–canteiro; alterações sem visibilidade tempestiva; paradas por falta de componentes; custo/estoque de formas e gabaritos. |
| 2 — Estratégia | Elaborados propósito, visão, hipóteses e OKRs de exemplo. | Direção: previsibilidade, rastreabilidade e eficiência. Valores de baseline/meta registrados nos materiais são fictícios e devem ser substituídos por dados reais antes de qualquer decisão. |
| 2B — Validação de hipóteses | Registrado um exercício fictício sobre a hipótese de que visibilidade centralizada reduziria atraso e retrabalho. | Resultado ilustrativo, não é evidência de validação com participantes reais. |
| 3 — Modelagem | Descritas protopersonas de gestão de operações e coordenação de obra, mapa de empatia e jornada To-Be. | Jornada proposta: identificar alteração, entender impacto, comunicar à obra, ajustar sequência e acompanhar materiais. |
| 3B — Árvore de oportunidades | Comparadas oportunidades de painel integrado, impacto de alterações, rastreio de componentes e balanceamento de equipes. | Priorização simulada do painel, impacto de alterações e rastreio; balanceamento avançado fica para avaliação posterior. |
| 4 — Feature Frames | Delimitados FF-01 painel de sincronização, FF-02 impacto de alterações e FF-03 status de componentes/ferramental, com limites de escopo. | MVP recomendado; App offline-first, RBAC, fotos obrigatórias, previsão avançada e integrações profundas não estão aprovados como escopo. |
| 5 — Prototipação | Especificada arquitetura conceitual do Dashboard Gerencial, estados, ingestão/qualidade de dados, acessibilidade e fluxos propostos do App Operacional. | Design System e stack não fornecidos. App Operacional é proposta pendente; protótipo não foi implementado nem validado com usuários reais. |
| 5B — Teste de usabilidade | Documentado um cenário e achados fictícios para telas gerenciais. | Demonstração de método, sem teste com usuários reais ou resultados observacionais válidos. |
| 6 — Handoff | Preparado backlog para FF-01 a FF-03, critérios de aceite Gherkin, propostas de endpoints e entidades, regras, instrumentação e pendências. | Contratos são propostas `[a validar com o time técnico]`; script de montagem/verificação e revisão independente não foram executados nesta conversa. |
| 7 — Medição | Registrado diagnóstico comportamental conceitual e possibilidades de correção. | Não há telemetria de produto lançado; é diagnóstico hipotético, não análise de uso real. |
| 8 — Experimentação | Desenhados experimentos para resposta a alterações, paradas por indisponibilidade e balanceamento de equipes. | Planos para execução futura; nenhum experimento foi conduzido e nenhum resultado foi medido. |

## Direção recomendada do MVP

1. **Sincronização fábrica–canteiro:** apresentar status por frente com origem e horário da última atualização.
2. **Impacto de alterações:** tornar visíveis alterações registradas e seus impactos conhecidos em cronograma, materiais e frentes afetadas, sem automatizar replanejamento.
3. **Componentes e ferramental:** mostrar disponibilidade conforme qualidade e atualidade da fonte, distinguindo estado confirmado de informação indisponível ou em validação.
4. **Ingestão seletiva:** começar por fontes e campos priorizados, validando identificadores e qualidade antes de calcular indicadores.

## Riscos e decisões pendentes

- Confirmar se o MVP inclui apenas o Dashboard Gerencial ou também o App Operacional.
- Validar frequência, qualidade, responsáveis e identificadores das fontes SQL/ERP e planilhas.
- Aprovar regras de cálculo dos indicadores, metas e baselines com dados reais; não usar os números fictícios como compromisso.
- Se o App Operacional avançar, definir RBAC, multi-tenancy, funcionamento offline, conflitos e sincronização, segurança de dados locais e notificações.
- Definir finalidade, acesso, retenção e governança de fotos antes de qualquer captura obrigatória.
- Selecionar stack e Design System; revisar arquitetura, contratos e requisitos não funcionais com o Tech Lead.
- Executar verificação mecânica da iniciativa e revisão independente; registrar aprovações humanas antes de considerar o handoff aprovado.

## Status executivo

**Resultado:** documentação fictícia da esteira, do Discovery ao planejamento pós-entrega, com MVP conceitual e handoff inicial.  
**Prontidão para desenvolvimento:** condicionada às validações de escopo, dados, arquitetura e privacidade acima.  
**Aprovação:** nenhuma aprovação humana real está registrada; a tabela de aprovações permanece em branco.

## Artefatos da iniciativa

- `00-insumos/transcricao-imersao.md`
- `evidencias.md`
- `01-discovery.md`
- `02-estrategia.md`
- `02b-validacao-hipoteses.md`
- `03-modelagem.md`
- `03b-arvore-oportunidades.md`
- `04-feature-frames.md`
- `05-prototipacao.md`
- `05b-teste-usabilidade.md`
- `06-handoff.md`
- `07-diagnostico-comportamental.md`
- `08-experimentos.md`
- `contexto.md` e `aprovacoes.md`

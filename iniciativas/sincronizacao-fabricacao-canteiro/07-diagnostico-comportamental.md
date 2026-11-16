# Módulo 6 — Handoff: sincronizacao-fabricacao-canteiro

## Contexto do produto

A solução visa sincronizar dados operacionais entre fábrica e canteiro, com foco em visibilidade, rastreabilidade e priorização de sequenciamento. O problema principal é a baixa integração entre o planejamento da produção e a execução da obra, o que gera atrasos, retrabalho e ociosidade por falta de materiais e ferramental.

## Objetivo do MVP

1. Unificar a visão de cronograma e status de entrega entre fábrica e obra.
2. Exibir o impacto de alterações de projeto em tempo real.
3. Rastrear disponibilidade de componentes e ferramental para reduzir paradas.

## Requisitos do handoff

### BDD 01
- Dado que uma alteração de projeto foi registrada
- Quando o sistema processa o impacto
- Então o gestor visualiza o efeito em cronograma, materiais e equipe

### BDD 02
- Dado que um material está indisponível
- Quando a obra solicita a liberação
- Então o painel emite alerta e prioriza a frente afetada

### BDD 03
- Dado que uma frente de trabalho recebe nova sequência
- Quando o gestor confirma a alteração
- Então a obra recebe atualização centralizada e rastreável

## Instrumentação sugerida

- `alteracao_projeto_registrada`
- `impacto_cronograma_calculado`
- `material_indisponivel_alerta`
- `sequenciamento_confirmado`

## Observações técnicas

- Base de dados: ERP e planilhas como fonte inicial.
- Sistema de integração: ETL seletivo para ingestão de dados operacionais.
- Priorização: garantir consistência de ID de projeto, forma, gabarito e material.


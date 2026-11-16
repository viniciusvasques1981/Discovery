# Módulo 4 — Feature Frame: sincronizacao-fabricacao-canteiro

## Feature Frame 01 — Painel de Sincronização Fabrica x Canteiro

**Contexto:** planejamento e execução são geridos em sistemas diferentes e pouco integrados.  
**Problema:** a obra não recebe atualização em tempo real sobre a disponibilidade de formas, cronograma e impacto de alterações.  
**Solução:** painel unificado com visão de produção, cronograma de obra e status de liberação.  
**Limites:** não substituir todas as fontes de dados; MVP prioriza ingestão seletiva e leitura de status.  
**Evidências:** E001, E006, E009, E020

## Feature Frame 02 — Impacto de Alterações de Projeto

**Contexto:** alterações de projeto afetam a sequência de execução e exigem análise manual.  
**Problema:** mudanças não são identificadas com rapidez suficiente e as frentes de trabalho sofrem atraso.  
**Solução:** cálculo do impacto de alteração com destaque de prazos, materiais e equipes afetadas.  
**Limites:** não prevê alterações de escopo sem registro formal.  
**Evidências:** E002, E003, E010, E012

## Feature Frame 03 — Rastreador de Componentes e Ferramental

**Contexto:** materiais e gabaritos não têm rastreio integrado ao processo de obra.  
**Problema:** ausência de componente na hora certa gera parada de equipes e ociosidade.  
**Solução:** acompanhamento do status de componentes, ferramental e entrega por frente.  
**Limites:** depende de padrão de codificação e qualidade das bases de dados.  
**Evidências:** E004, E005, E017, E018

## MVP recomendado

- FF-01: painel central de sincronização
- FF-02: impacto de alterações de projeto
- FF-03: rastreador de materiais e ferramental

## Fora do MVP

- otimização global de portfólio
- predição avançada de demanda
- automação completa de logística
- integração profunda de todos os ERPs e ferramentas de campo


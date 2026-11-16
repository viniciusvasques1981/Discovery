# Módulo 4 — Feature Frames: sincronizacao-fabricacao-canteiro

> Simulação fictícia. As decisões e evidências abaixo são ilustrativas e não representam validação com clientes reais.

## Feature Frame 01 — Painel de Sincronização Fábrica x Canteiro

**Contexto:** planejamento e execução são geridos em sistemas distintos e pouco integrados.  
**Problema:** equipes não têm uma visão compartilhada e atualizada do cronograma, da liberação de elementos e do status operacional.  
**Solução:** painel gerencial com leitura consolidada da sincronização entre fábrica e canteiro e acesso ao status por frente.  
**Limites:** não substitui todas as fontes de dados; MVP prioriza ingestão seletiva e visualização de informações disponíveis.  
**Evidências:** E001, E006, E009, E020

## Feature Frame 02 — Impacto de Alterações de Projeto

**Contexto:** alterações de projeto podem afetar a sequência de execução e demandam coordenação manual.  
**Problema:** mudanças podem não chegar a tempo às equipes de campo.  
**Solução:** destacar alterações registradas e seus impactos conhecidos em cronograma, materiais e frentes afetadas.  
**Limites:** não prevê alterações não registradas nem automatiza decisões de replanejamento.  
**Evidências:** E002, E003, E010, E012

## Feature Frame 03 — Status de Componentes e Ferramental

**Contexto:** materiais, formas e gabaritos não têm rastreio integrado ao processo de obra.  
**Problema:** indisponibilidade no momento de uso pode interromper a execução.  
**Solução:** apresentar o status disponível de componentes, formas e ferramental por frente, condicionado à existência e qualidade dos dados de origem.  
**Limites:** depende de identificadores consistentes e de atualização das fontes; não inclui otimização automática de estoque.  
**Evidências:** E004, E005, E017, E018

## MVP recomendado

- FF-01: painel de sincronização fábrica × canteiro.
- FF-02: acompanhamento de alterações de projeto e impactos registrados.
- FF-03: visualização do status de componentes e ferramental.

## Fora do MVP / decisão necessária

- Previsão avançada de demanda e otimização global de portfólio.
- Automação completa de logística ou replanejamento.
- Integração profunda com todos os ERPs e ferramentas de campo.
- App mobile offline-first, autenticação RBAC, captura fotográfica obrigatória e fila de sincronização: propostos na arquitetura de interface recebida, mas ainda sem Feature Frame/decisão de escopo.
- Gestão executiva de roadmap e roster de squad: confirmar se pertencem ao produto ou são conteúdo interno de governança.
- Indicadores com metas numéricas, como “80 → 15” e “turnover -20%”: valores de exemplo; não tratados como baseline ou meta validada.


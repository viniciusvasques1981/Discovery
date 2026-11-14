---
name: behavioral-experimentation-cro
description: "Transformar oportunidades identificadas na análise comportamental ou hipóteses de produto em planos formais de experimentos A/B/n com rigor analítico e variáveis guardiãs de segurança. Cobre o Módulo 8 (Experimentação) do ciclo pós-entrega da esteira. Use quando houver uma hipótese a validar em produção, uma oportunidade de otimização de conversão ou a necessidade de planejar um teste A/B."
---

# Experimentação Comportamental e CRO

Módulo 8 — ciclo pós-entrega da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Experimentação controlada (A/B/n), Economia Comportamental |
| **Entradas** | `07-diagnostico-comportamental.md` ou a Matriz de Hipóteses de `02-estrategia.md`; volume de tráfego e taxa atual da métrica primária |
| **Saída** | `08-experimentos.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `behavioral-analytics-ux-fixes` |
| **Retroalimenta** | `discovery-product-strategy` (revisão da Matriz CSD e dos OKRs) |

## Regras de execução

1. Um experimento testa uma hipótese. Mais de uma intervenção por variante impede atribuição causal.
2. Não estimar linha de base nem tráfego: solicitar os dados. Sem eles, entregar o plano com os campos de amostragem marcados como `[pendente de dados]`.
3. Definir o critério de decisão antes do início do experimento (o que leva a implementar, descartar ou iterar).
4. O cálculo de tamanho de amostra e duração depende de taxa de base, efeito mínimo detectável, nível de significância e poder estatístico. Declarar os parâmetros usados; quando o cálculo não puder ser executado, indicar que deve ser feito na ferramenta de experimentação.

## Algoritmo de Execução

### 1. Estruturação de Hipótese Comportamental

Aplicar a fórmula de conversão:

> Se **[implementarmos a intervenção X na Variante B]**, então **[a Métrica Primária Y terá uma variação esperada de Z]**, porque **[fundamento psicológico/comportamental acionado, ex: redução de carga cognitiva, ancoragem, clareza funcional]**.

### 2. Arquitetura de Variantes

- **Variante A (Controle):** Estado atual da interface e do fluxo operacional.
- **Variante B (Desafio):** Modificação controlada e isolada, sem alterar variáveis secundárias que criem ruído causal.

Em testes A/B/n, cada variante adicional isola uma única alteração em relação ao controle.

### 3. Definição de Métricas do Experimento

- **Métrica Primária:** Indicador central de conversão ou conclusão da tarefa.
- **Métricas Secundárias:** Indicadores de engajamento correlacionados (CTR interno, tempo de tela, profundidade de scroll).
- **Métricas Guardiãs (Guardrail Metrics):** Indicadores de estabilidade da experiência que não podem degradar (taxa de erro de validação, requisições de suporte, cancelamentos, latência da aplicação).

### 4. Parâmetros de Segmentação e Amostragem

Critérios de público-alvo, gatilhos de disparo do experimento e condições de elegibilidade para garantir integridade amostral.

- Efeito mínimo detectável, nível de significância e poder estatístico adotados.
- Duração mínima cobrindo ciclos completos de uso (ao menos uma semana inteira, para neutralizar o efeito de dia da semana).
- Critérios de parada: degradação de métrica guardiã acima do limite definido.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/08-experimentos.md`.

- **Ficha Técnica do Experimento:** Identificador, Hipótese Comportamental e Mecanismo Psicológico.
- **Detalhamento das Variantes:** Descritivo comparativo entre Variante A (Controle) e Variante B (Tratamento).
- **Painel de Métricas:** Métrica Primária, Secundárias e Guardrail Metrics.
- **Critérios de Amostragem:** Definição do público elegível e gatilhos de ativação.
- **Critério de Decisão:** condições para implementar, descartar ou iterar.

## Passagem de contexto

Ao concluir o plano, registrar o experimento em `iniciativas/<slug>/contexto.md`. Após a execução, registrar o resultado e reclassificar na Matriz CSD a Suposição correspondente (para Certeza, se confirmada; removida ou reformulada, se refutada).

---
name: artifact-evidence-review
description: "Revisar de forma independente os artefatos de um bloco da esteira, conferindo se cada afirmação é sustentada pela evidência que cita e se os artefatos são coerentes entre si. As conferências mecânicas ficam a cargo de um script; a revisão cobre fidelidade e classificação. Use ao fim dos módulos 2, 4, 6 e 8, antes da aprovação humana, ou quando houver dúvida sobre a fidelidade de um artefato ao material de origem."
---

# Revisão Independente de Artefatos

Skill transversal da Esteira de Produto AI-Enhanced, aplicada ao fim de cada bloco.

| | |
| :--- | :--- |
| **Entradas** | Os artefatos do bloco, a saída do script de verificação e as evidências citadas. Nunca o material bruto completo |
| **Saída** | Nova seção em `iniciativas/<slug>/revisoes.md` |

## Princípio

Quem produz um artefato tende a não perceber as próprias lacunas. A revisão é feita em contexto separado, sem acesso ao raciocínio de quem produziu. O objetivo é localizar conteúdo plausível sem sustentação.

O trabalho é dividido em duas partes. O script confere tudo o que é mecânico. O revisor confere o que exige leitura: se a evidência citada diz o que o artefato afirma.

## Blocos

| Bloco | Artefatos revisados | Comparados com |
| :--- | :--- | :--- |
| Após o Módulo 2 | `evidencias.md`, `01-discovery.md`, `02-estrategia.md` | Linhas de origem citadas pelas evidências |
| Após o Módulo 4 | `03-modelagem.md`, `04-feature-frames.md` | `evidencias.md`, `01-discovery.md`, `02-estrategia.md` |
| Após o Módulo 6 | `05-prototipacao.md`, `06-handoff.md` | `04-feature-frames.md`, `02-estrategia.md` |
| Após o Módulo 8 | `07-diagnostico-comportamental.md`, `08-experimentos.md` | Dados de uso fornecidos, `02-estrategia.md` |

Artefatos de etapas opcionais (2B, 3B, 5B) entram no bloco em que foram produzidos.

## Regras de execução

1. O revisor aponta; não corrige. A correção cabe ao agente do módulo.
2. Todo apontamento cita a evidência que sustenta ou contradiz o item, ou indica que nada foi encontrado.
3. Não ler `00-insumos/` por inteiro. As linhas de origem são obtidas pelo script, somente as citadas.
4. Não refazer o que o script confere: campos obrigatórios, cálculo do índice, cobertura de issues, cenários mínimos, blocos derivados e instrumentação.
5. Não avaliar qualidade de estratégia, de design ou de decisão de negócio. Decisões cabem ao aprovador humano.
6. Ausência de apontamentos não equivale a artefato correto. Declarar o que não pôde ser conferido.

## Algoritmo de Execução

### 1. Verificação mecânica

Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>`. Cada linha `ERRO` vira um apontamento Bloqueante ou Relevante, sem nova análise. Se houver erro, o parecer já é "Reprovado" e o restante da revisão pode aguardar a correção.

### 2. Fidelidade das evidências (somente no bloco do Módulo 2)

Executar `python3 scripts/iniciativa.py citar iniciativas/<slug> --evidencias`. A saída mostra cada evidência seguida das linhas de origem. Conferir, uma a uma:

- a evidência diz o mesmo que a linha, sem acréscimo nem interpretação;
- o tipo está correto (Dado exige número ou registro; opinião de participante é Declaração);
- a fonte corresponde a quem fala na linha.

Cobertura: a pedido do aprovador, executar `citar --nao-citadas` para ver as linhas que nenhuma evidência usa e apontar omissões relevantes. Essa leitura equivale ao restante do material bruto e não faz parte da revisão padrão.

### 3. Sustentação das afirmações

Para cada afirmação factual dos artefatos do bloco, abrir a evidência citada em `evidencias.md` e conferir:

| Verificação | Critério |
| :--- | :--- |
| Sustentação | A evidência citada diz o que o item afirma |
| Números | Volume, percentual, prazo e custo têm o mesmo valor da evidência |
| Marcação | Conclusão que vai além da evidência está marcada como `[inferência]` |
| Classificação | Certeza apoiada apenas em Declaração, Relato ou Pedido deve ser Suposição |

### 4. Coerência específica do bloco

| Bloco | Verificações |
| :--- | :--- |
| Módulo 2 | Dúvidas em forma de pergunta; nenhuma solução proposta no Módulo 1; hipóteses derivadas de Suposições existentes; nenhuma linha de base estimada |
| Módulo 4 | Dores da Protopersona correspondem a dores do Módulo 1; cada Feature Frame resolve a dor que cita; Out of Scope é verificável; Confiança coerente com a situação da hipótese |
| Módulo 6 | Nenhuma tela implementa item de Out of Scope; mensagens dos cenários iguais às do Guia de Microcopy; contratos não confirmados estão marcados; cenários cobrem as regras de negócio críticas |
| Módulo 8 | Achados com volume e nível de evidência; causa raiz tratada como hipótese; uma hipótese por experimento; nenhum parâmetro de amostragem estimado |

### 5. Classificação e parecer

| Severidade | Definição | Efeito |
| :--- | :--- | :--- |
| Bloqueante | Afirmação sem sustentação que apoia decisão posterior; erro apontado pelo script em rastreabilidade ou escopo | Impede a aprovação até correção ou aceite registrado |
| Relevante | Classificação incorreta, número divergente, contradição entre artefatos | Corrigir antes do bloco seguinte |
| Menor | Imprecisão de redação, marcação ausente em item secundário | Corrigir quando conveniente |

- **Aprovado:** nenhum apontamento Bloqueante ou Relevante.
- **Aprovado com ressalvas:** apenas apontamentos Relevantes ou Menores.
- **Reprovado:** ao menos um apontamento Bloqueante.

Sem execução de scripts: fazer as conferências mecânicas manualmente e registrar essa condição nos limites da revisão.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/revisoes.md`. Acrescentar uma seção ao arquivo `revisoes.md` da iniciativa, sem apagar as anteriores.

## Fechamento

Registrar o parecer na coluna "Revisão independente" de `aprovacoes.md`, na linha do módulo que fecha o bloco.

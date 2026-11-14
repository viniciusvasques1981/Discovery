---
name: artifact-evidence-review
description: "Revisar de forma independente um artefato da esteira, confrontando cada afirmação com os insumos e com os artefatos dos módulos anteriores. Aponta itens sem origem, contradições, classificações incorretas na Matriz CSD, quebras de rastreabilidade e alterações indevidas em Out of Scope. Use ao concluir um módulo, antes da aprovação humana, ou quando houver dúvida sobre a fidelidade de um artefato ao material de origem."
---

# Revisão Independente de Artefatos

Skill transversal da Esteira de Produto AI-Enhanced, aplicada nos portões de saída.

| | |
| :--- | :--- |
| **Entradas** | O artefato a revisar, `00-insumos/`, `contexto.md` e os artefatos dos módulos anteriores |
| **Saída** | Nova seção em `iniciativas/<slug>/revisoes.md` |

## Princípio

Quem produz um artefato tende a não perceber as próprias lacunas. A revisão é feita em contexto separado, sem acesso ao raciocínio de quem produziu: apenas o artefato e as fontes. O objetivo é localizar conteúdo plausível que não tem sustentação nos insumos.

## Regras de execução

1. O revisor aponta; não corrige. A correção cabe ao agente do módulo.
2. Todo apontamento cita a evidência: o trecho do insumo ou do artefato anterior que sustenta ou contradiz o item, ou a indicação de que nada foi encontrado.
3. Ausência de apontamentos não equivale a artefato correto. Declarar o que não pôde ser conferido.
4. Não avaliar qualidade de estratégia, de design ou de decisão de negócio. A revisão cobre fidelidade às fontes e consistência interna. Decisões cabem ao aprovador humano.
5. Sem acesso aos insumos, executar apenas as verificações de consistência entre artefatos e registrar a limitação.

## Algoritmo de Execução

### 1. Verificações comuns a todos os artefatos

| Verificação | Critério |
| :--- | :--- |
| Origem | Cada afirmação factual tem origem identificável nos insumos ou em artefato anterior |
| Marcação | Conteúdo sem origem está marcado como `[inferência]`, `[pendente de dados]` ou `[a validar ...]` |
| Números | Todo número (volume, percentual, prazo, custo) consta nos insumos com o mesmo valor |
| Campos | Todos os campos obrigatórios do modelo estão preenchidos |
| Consistência | Não há contradição com `contexto.md` nem com artefatos anteriores |

### 2. Verificações por módulo

| Artefato | Verificações específicas |
| :--- | :--- |
| `01-discovery.md` | Certezas têm evidência documental ou dado; declarações de stakeholder sem dado estão em Suposições; Dúvidas estão em forma de pergunta; dores têm evidência; nenhuma solução foi proposta |
| `02-estrategia.md` | Visão de Produto no formato padrão; hipóteses derivam de Suposições existentes; KRs têm linha de base presente nos insumos ou são de Instrumentação; nenhuma linha de base foi estimada |
| `02b-validacao-hipoteses.md` | Critérios definidos antes do resultado; resultados informados pelo usuário, não simulados; reclassificações coerentes com o veredito |
| `03-modelagem.md` | Dores da Protopersona correspondem a dores do Módulo 1; atributos sem origem estão marcados; a jornada tem os quatro campos em todos os estágios |
| `03b-arvore-oportunidades.md` | Oportunidades vinculadas a dor e estágio; ao menos duas soluções por oportunidade priorizada |
| `04-feature-frames.md` | Todo Feature Frame tem estágio, Key Result e Out of Scope; hipótese não validada resulta em Confiança Baixa; checagem de viabilidade preenchida; índice calculado corretamente; nenhum item inviável no MVP |
| `05-prototipacao.md` | Toda tela vinculada a Feature Frame do MVP; nenhuma tela implementa item de Out of Scope; quatro estados por tela; mensagens de erro com os três elementos |
| `05b-teste-usabilidade.md` | Critérios de aprovação anteriores às sessões; resultados não simulados; percentuais não apresentados como representativos |
| `06-handoff.md` | Uma issue por Feature Frame do MVP; Out of Scope idêntico, caractere a caractere, ao do Módulo 4; cenários de caminho feliz, exceção e borda; Por quê e Key Result em cada issue; todo Key Result com evento; contratos não confirmados marcados |
| `07-diagnostico-comportamental.md` | Período e volume informados; cada achado com volume e nível de evidência; causa raiz tratada como hipótese |
| `08-experimentos.md` | Uma hipótese por experimento; métricas guardiãs e critério de decisão definidos; nenhum parâmetro de amostragem estimado sem dados |

### 3. Classificação dos apontamentos

| Severidade | Definição | Efeito |
| :--- | :--- | :--- |
| Bloqueante | Afirmação sem origem que sustenta decisão posterior; Out of Scope alterado; rastreabilidade quebrada | Impede a aprovação até correção ou aceite registrado |
| Relevante | Classificação incorreta, campo obrigatório ausente, contradição entre artefatos | Corrigir antes do módulo seguinte |
| Menor | Imprecisão de redação, marcação ausente em item secundário | Corrigir quando conveniente |

### 4. Parecer

- **Aprovado:** nenhum apontamento Bloqueante ou Relevante.
- **Aprovado com ressalvas:** apenas apontamentos Relevantes ou Menores.
- **Reprovado:** ao menos um apontamento Bloqueante.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/revisoes.md`. Acrescentar uma seção ao arquivo `revisoes.md` da iniciativa, sem apagar as anteriores.

- **Parecer.**
- **Apontamentos:** tipo, local, descrição, evidência e severidade.
- **Itens conferidos sem apontamento.**
- **Limites desta revisão.**

## Passagem de contexto

Registrar o parecer na coluna "Revisão independente" da tabela de Aprovações de `contexto.md`. Apontamento aceito pelo aprovador sem correção é registrado em "Pendências aceitas".

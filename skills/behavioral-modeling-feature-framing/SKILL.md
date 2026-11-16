---
name: behavioral-modeling-feature-framing
description: "Converter os direcionadores estratégicos em modelos comportamentais de uso e delimitar o escopo funcional por meio da metodologia Feature Framing, prevenindo a expansão descontrolada de escopo (scope creep). Cobre os Módulos 3 (Modelagem) e 4 (Feature Frame) da esteira: Protopersona, Mapa de Empatia, Jornada To-Be, Árvore de Oportunidades (opcional), Catálogo de Feature Frames, checagem de viabilidade técnica, priorização por valor e recorte de MVP. Use quando houver estratégia definida e for preciso modelar o usuário ou delimitar escopo de funcionalidades."
---

# Modelagem Comportamental e Feature Framing

Módulos 3 e 4 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | User Centered Design (UCD), Feature Frame, Lean Inception |
| **Entradas** | `contexto.md`, `01-discovery.md` e `02-estrategia.md`; `02b-validacao-hipoteses.md`, se existir. Não ler `00-insumos/` |
| **Saídas** | `03-modelagem.md` e `04-feature-frames.md` em `iniciativas/<slug>/`; `03b-arvore-oportunidades.md`, se a Etapa 3B for executada |
| **Skill anterior** | `discovery-product-strategy` |
| **Próxima skill** | `systemic-ui-interaction-design` |

## Regras de execução

1. Ler `contexto.md` antes de iniciar. Sem dores validadas e Visão de Produto, interromper e solicitar a execução dos Módulos 1 e 2.
2. Toda dor da Protopersona deve corresponder a uma dor validada no Módulo 1. Atributos não sustentados por evidência (E001…) recebem a marca `[inferência]`.
3. Cada Feature Frame deve referenciar o estágio da Jornada To-Be que atende e o Key Result que influencia. Funcionalidade sem esse vínculo não entra no catálogo.
4. O campo Out of Scope é obrigatório, não pode ficar vazio e é escrito uma única vez, no bloco do Feature Frame. Não repetir em tabela consolidada nem em `contexto.md`: o handoff recebe esses limites por script.
5. Feature Frame derivado de hipótese não validada recebe a marca `[não validada]` e Confiança Baixa.
6. O recorte de MVP só é fechado depois da checagem de viabilidade técnica.

## Algoritmo de Execução

### Módulo 3 — O Olhar do Usuário (Modelagem)

#### 1. Modelagem Centrada no Usuário (UCD)

- **Protopersona:** Perfil operacional, responsabilidades no ecossistema, 3 dores centrais no fluxo atual e necessidades imediatas. Incluir motivações e medos (o que a pessoa teme perder ou errar ao adotar a solução).
- **Mapa de Empatia:** O que pensa e sente, vê, ouve, fala e faz; dores e ganhos. Preencher apenas com o que os insumos sustentam.
- **Jornada To-Be:** Mapeamento sequencial contendo: Estágio da Jornada → Ação do Usuário → Fricção Eliminada → Gatilho de Sucesso.

Protopersona é hipótese de perfil, não persona validada por pesquisa. Registrar essa condição na entrega.

### Etapa 3B (opcional) — Árvore de Oportunidades

Indicada quando há mais de uma solução plausível por dor ou quando os stakeholders chegam com soluções prontas. Acrescenta tempo ao ciclo; se não for executada, registrar a decisão em `aprovacoes.md` e derivar as funcionalidades diretamente da Jornada To-Be.

1. **Resultado:** partir de um Key Result do Módulo 2.
2. **Oportunidades:** listar dores e necessidades do usuário que, resolvidas, movem o Key Result. Vincular cada uma a uma dor do Módulo 1 e a um estágio da jornada; classificar por frequência e severidade.
3. **Soluções candidatas:** gerar ao menos duas por oportunidade priorizada.
4. **Testes de suposição:** identificar a suposição mais arriscada de cada solução e o teste mais barato que a refutaria.
5. **Seleção:** indicar as soluções que seguem para Feature Frame, com justificativa.

Modelo: `assets/03b-arvore-oportunidades.md`.

### Módulo 4 — Definição (Feature Frame)

#### 2. Engenharia de Escopo via Feature Framing

Para cada funcionalidade proposta, estruturar a matriz de delimitação:

- **Contexto:** Momento exato e gatilho em que a funcionalidade entra em ação.
- **Problema:** A dor específica resolvida naquele ponto da jornada.
- **Solução:** O comportamento funcional e visual executado pelo sistema.
- **Out of Scope (Limites Rígidos):** O que a funcionalidade explicitamente não faz sob nenhuma hipótese neste ciclo.

#### 3. Pontuação de Valor, Confiança e Esforço

- **Valor (1–5):** contribuição direta ao Key Result relacionado e severidade da dor atendida. 5 = sem a funcionalidade o Key Result não se move; 1 = contribuição marginal.
- **Confiança:** Alta quando a dor é Certeza ou a hipótese foi validada na Etapa 2B; Média quando há evidência parcial; Baixa quando deriva de Suposição não validada.
- **Esforço (Fibonacci):** 1, 2, 3, 5, 8 ou 13. A estimativa é relativa e proposta pelo papel de produto; o valor definitivo é o revisado na checagem de viabilidade. Itens estimados em 13 devem ser decompostos.

#### 4. Checagem de Viabilidade Técnica

Antes do recorte de MVP, submeter o catálogo ao Tech Lead (pessoa do time ou agente `handoff-tech-lead`), que executa a skill `technical-feasibility-check` e preenche a seção correspondente de `04-feature-frames.md`. Feature Frame com parecer "Inviável neste ciclo" sai do MVP.

#### 5. Priorização e Recorte de MVP

- **Índice de prioridade:** Valor × Confiança ÷ Esforço revisado, com Confiança Alta = 1,0; Média = 0,7; Baixa = 0,4. Os pesos são convenção deste repositório e podem ser ajustados pelo time.
- **MVP (Sim/Não):** Classificar com base no menor conjunto funcional viável para entrega de valor. Critério: sem a funcionalidade, a Jornada To-Be não se completa de ponta a ponta para a Protopersona principal.
- O índice ordena; não decide sozinho. Uma funcionalidade de índice baixo permanece no MVP quando a jornada não se completa sem ela.

## Padrão de Entrega (Markdown)

Usar os modelos `assets/03-modelagem.md` e `assets/04-feature-frames.md`.

**`03-modelagem.md`**

- **Modelagem Comportamental:** Perfil da Protopersona, Mapa de Empatia e Matriz da Jornada To-Be.

**`04-feature-frames.md`**

- **Catálogo de Feature Frames:** Bloco individual para cada funcionalidade com Contexto, Problema, Solução, Out of Scope e Classificação de MVP.
- **Checagem de viabilidade técnica:** esforço revisado, dependências, risco e parecer por Feature Frame.
- **Matriz de priorização:** Funcionalidade, estágio da jornada, Key Result relacionado, valor, confiança, esforço, índice e MVP.
- **Recorte de MVP:** lista final do que entra e do que fica para ciclos seguintes.

Os títulos dos blocos seguem o padrão `### FF-01 — nome`, e as linhas da tabela usam os rótulos do modelo: os scripts de montagem e de verificação leem esse formato.

## Fechamento

1. Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>` e corrigir os erros apontados.
2. Atualizar apenas a seção "3–4. Usuário e escopo" de `contexto.md`, em linhas curtas: protopersona, estágios da jornada, Feature Frames do MVP e o que ficou fora. Não copiar Out of Scope.

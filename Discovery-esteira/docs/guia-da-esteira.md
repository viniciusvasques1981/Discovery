# O Guia da Esteira de Produto AI-Enhanced

## Por que isso é importante?

Muitas vezes, uma imersão gera apenas documentos que ficam esquecidos. Com essa esteira, cada conversa vira um dado que alimenta a fase seguinte, garantindo que o que foi discutido com o *sponsor* no Módulo 1 esteja refletido no código gerado pelo Copilot no Módulo 6.

## A Inteligência Integrada: Por que acelerar com IA?

Trabalhar com modelos preparados para a IA significa que cada palavra escrita em uma imersão tem um destino técnico. O grande benefício é a continuidade do fluxo: a informação não morre em um post-it esquecido; ela evolui até virar código.

### Os principais benefícios

- **Consistência Inabalável:** A IA garante que o "Porquê" definido lá no início esteja presente em cada critério de aceitação escrito no final.
- **Velocidade de Handoff:** O que levava dias para documentar — como escrever dezenas de BDDs e critérios de aceitação — agora acontece em segundos, com base no contexto real da reunião.
- **Redução de Ruído:** Ao usar prompts estruturados, eliminamos interpretações erradas. O desenvolvedor recebe exatamente o que foi validado com o sponsor.
- **Foco no Estratégico:** Com a IA cuidando da "escrita braçal", você e seu time ganham tempo para o que importa: pensar na estratégia, no negócio e na experiência do usuário.

### Regra de Ouro

Sempre que for pular de um módulo para o outro, você pode dizer: "Aqui está o resumo do módulo anterior para você usar como contexto". Isso mantém o fio da meada e garante que o Porquê lá do início chegue intacto ao código no final.

## Descrição resumida dos módulos

### Módulo 1: O Mergulho (Discovery)

- **Objetivo:** Limpar o ruído e nivelar o conhecimento de todos.
- **Framework:** Design Thinking (Fase de Empatia).
- **Resultado:** Matriz CSD (Certezas, Suposições e Dúvidas) e lista de dores validadas.

### Módulo 2: O Propósito (Estratégia)

- **Objetivo:** Definir o "Norte" e o valor real para o negócio.
- **Framework:** Golden Circle e Lean UX.
- **Resultado:** Visão do Produto consolidada e Matriz de Hipóteses.

### Módulo 3: O Olhar do Usuário (Modelagem)

- **Objetivo:** Humanizar os dados e desenhar a jornada ideal.
- **Framework:** User Centered Design (UCD).
- **Resultado:** Mapa visual da Jornada To-Be com pontos de fricção resolvidos.

### Módulo 4: Definição (Feature Frame)

- **Objetivo:** Delimitar o escopo técnico e funcional, evitando o scope creep.
- **Framework:** Feature Frame e Lean Inception.
- **Resultado:** Matriz de Feature Frames priorizada e recorte de MVP.

### Módulo 5: Do Mapa à Tela (Prototipação)

- **Objetivo:** Tangibilizar as ideias antes do desenvolvimento pesado.
- **Framework:** Agile Prototyping.
- **Resultado:** Wireframes funcionais e diretrizes de UI para o Copilot.

### Módulo 6: A Entrega (Handoff Técnico)

- **Objetivo:** Traduzir a estratégia para a linguagem do desenvolvedor e da IA.
- **Framework:** Agile Handoff.
- **Resultado:** Issues no GitHub prontas e contexto de prompt para o Copilot gerar código.

## Detalhamento dos módulos

### Módulo 1: O Mergulho (Discovery)

Este é o momento de "arrumar a casa". O objetivo é fazer um Download completo de tudo o que sabemos sobre o problema.

- **Framework:** Design Thinking (Fase de Empatia).
- **Na prática:** Usamos a Matriz CSD para separar o que é certeza do que é apenas "achismo".

**Prompt Sugerido:** "Atue como um Especialista em Produto. Analise a transcrição/documento anexo desta imersão e realize o 'Download do Problema'. Identifique o cenário atual, liste as dores reais e organize a Matriz CSD. Liste as premissas e limitações técnicas citadas."

### Módulo 2: O Propósito (Estratégia)

Definimos o "Norte". Não adianta construir algo incrível se não soubermos para que serve.

- **Framework:** Golden Circle e Lean UX.
- **Na prática:** Criamos a Visão do Produto e propomos OKRs.

**Prompt Sugerido:** "Com base no resumo do Módulo 1, aplique o framework do Círculo Dourado para definir a missão (Por quê), diferencial (Como) e entrega (O quê). Preencha o template de Visão: 'Para [cliente], cujo [problema], o [produto] é um [categoria] que [benefício]'. Proponha 3 OKRs."

### Módulo 3: O Olhar do Usuário (Modelagem)

Vamos olhar para quem vai usar a ferramenta no dia a dia.

- **Framework:** User Centered Design (UCD).
- **Na prática:** Criamos Protopersonas e a Jornada To-Be.

**Prompt Sugerido:** "Atue como um UX Designer. Modele a experiência criando uma Protopersona (problemas, motivos, medos), Mapa de Empatia e Jornada To-Be destacando a eliminação das dores atuais."

### Módulo 4: Mãos à Obra (Feature Frame)

Momento de delimitar o escopo técnico e funcional através do enquadramento rigoroso de funcionalidades.

- **Framework:** Feature Frame & Lean Inception.
- **Pilar do Enquadramento:** Contexto, Problema, Solução e Limites (Out of Scope).

**Prompt Sugerido:** "Atue como um Product Leader. Transforme a jornada do Módulo 3 em uma estrutura de **Feature Frame** detalhando Contexto, Problema, Solução e Limites (Out of Scope). Realize o 'Recorte do MVP' e atribua esforço em Fibonacci."

### Módulo 5: Prototipação Inteligente (Do Mapa à Tela)

Ponte entre o enquadramento estratégico e a tangibilização visual.

- **Framework:** Agile Prototyping.
- **Input Necessário:** Feature Frames do Módulo 4 e Design System da empresa.

**Prompt Sugerido:** "Atue como um UI/UX Designer. Com base nos Feature Frames e limites de escopo, descreva o fluxo de telas necessário. Liste componentes obrigatórios e gere um guia para o Copilot criar o código React usando nosso Design System."

### Módulo 6: O Handoff (Entrega Técnica)

O momento de "passar o bastão" falando a língua do robô (Copilot) e do desenvolvedor.

- **Framework:** Agile Handoff.
- **Na prática:** Usamos BDD (Dado que... Quando... Então...) e Planos de Arquitetura.

**Prompt Sugerido:** "Atue como um Tech Lead. Prepare o handoff técnico: transforme os Feature Frames em BDDs; descreva APIs e infraestrutura; crie o parágrafo de contexto para o Copilot respeitar as regras complexas e os limites de escopo."

## Resumo: Frameworks e Entregáveis

| Módulo | Framework | Entrega Principal   |
| :---- | :---- | :---- |
| 1. Discovery | Design Thinking | Matriz CSD e Dores validadas |
| 2. Estratégia | Golden Circle | Missão e OKRs de negócio |
| 3. Modelagem | UCD | Persona e Jornada To-Be |
| **4. Definição** | **Feature Frame** | **Escopo delimitado e Recorte de MVP** |
| 5. Protótipo | Agile Prototyping | Fluxos de tela e Guia UI |
| 6. Handoff | Agile Handoff | Issues GitHub e BDDs |

## Cronograma: Imersão "Mãos na Massa" (2 Dias)

| Dia | Período | Módulo / Atividade   |
| :---- | :---- | :---- |
| Dia 1 | Manhã | Módulo 1 - O Mergulho (Discovery) |
| Dia 1 | Tarde | Módulo 2 - O Propósito (Estratégia) |
| Dia 2 | Manhã | Módulo 3 (Usuário) e Módulo 5 (Prototipação) |
| Dia 2 | Tarde | **Módulo 4 (Feature Frame)** e Módulo 6 (Handoff Técnico) |

---

## Extensão: ciclo pós-entrega

Este repositório acrescenta dois módulos ao guia original, baseados nas skills de analytics e experimentação:

| Módulo | Framework | Entrega Principal |
| :---- | :---- | :---- |
| 7. Medição | Heurísticas de usabilidade | Diagnóstico comportamental e matriz de intervenção de UX |
| 8. Experimentação | Experimentação controlada (A/B/n) | Plano de experimento com métricas guardiãs |

Detalhes em [mapa-da-esteira.md](mapa-da-esteira.md).

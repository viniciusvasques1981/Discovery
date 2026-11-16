---
name: cross-product-alignment
description: "Manter alinhados os produtos que nasceram da mesma imersão e seguem em repositórios separados. Publica a interface do produto, lê a interface dos produtos vizinhos e trata dependências quebradas, sobreposições, divergências de vocabulário e suposições do tronco reclassificadas por outro produto. Use depois dos Módulos 4 e 6 de um produto derivado, antes de planejar uma integração ou quando for preciso saber como o outro produto evoluiu."
---

# Alinhamento entre Produtos

Skill transversal da Esteira de Produto AI-Enhanced, para imersões que originam mais de um produto.

| | |
| :--- | :--- |
| **Entradas** | `interface.md` deste produto e dos vizinhos (em `vizinhos/`), `partilha.md` e a saída do script. Nunca os artefatos completos do outro produto |
| **Saídas** | `interface.md` atualizado; decisões registradas em `contexto.md` e `aprovacoes.md` |

## Como os produtos se conectam

Cada produto publica um resumo gerado por script, `interface.md`: Feature Frames com situação, limites de Out of Scope, eventos instrumentados, contratos de API, entidades de dados e itens do tronco reclassificados. Um produto lê apenas esse resumo do outro. O cruzamento é feito por script; o modelo só é usado para decidir o que fazer com o que o script aponta.

A conexão é eventual: cada produto vê o vizinho no estado da última leitura.

## Regras de execução

1. Não abrir os artefatos do outro produto. A interface publicada é a fonte.
2. Não alterar artefatos herdados do tronco (`evidencias.md`, `01-discovery.md`, `02-estrategia.md`, `partilha.md` e, na separação pelo Módulo 4, `03-modelagem.md`). Mudança nesses arquivos é feita no repositório da imersão.
3. Dependência só existe se estiver declarada nos dois lados: "Depende de" em um Feature Frame e "Fornece para" no Feature Frame correspondente do outro produto.
4. Não resolver sozinho um conflito entre produtos. Apresentar ao usuário as opções e quem decide.

## Algoritmo de Execução

### 1. Publicar e cruzar

```bash
python3 scripts/iniciativa.py vizinhos iniciativas/<slug>
```

O comando atualiza o `interface.md` deste produto, lê a interface de cada vizinho listado em `vizinhos.json`, mostra o que mudou desde a última leitura e cruza os dois lados. Se a interface de um vizinho não estiver acessível, usa a última cópia e avisa.

### 2. Tratar o que o script aponta

| Saída | Significado | Ação |
| :--- | :--- | :--- |
| `ERRO` dependência inexistente ou removida | Este produto depende de algo que o outro não tem mais | Rever o Feature Frame dependente com o Product Manager; pode exigir mudança de escopo |
| `AVISO` dependência fora do MVP do vizinho | O que este produto precisa não será entregue no mesmo ciclo | Negociar a prioridade com o outro produto ou retirar a dependência do MVP |
| `AVISO` sobreposição | Os dois produtos têm funcionalidade no MVP para a mesma dor | Conferir em `partilha.md` se a dor é compartilhada; se não for, definir o dono |
| `AVISO` vocabulário | Evento ou entidade parecida com nomes diferentes | Adotar um nome único antes do handoff; depois dele, o custo de integração sobe |
| `AVISO` item do tronco reclassificado | O outro produto confirmou ou refutou uma suposição da imersão | Verificar quais Feature Frames deste produto se apoiam nesse item e rever a Confiança |
| `AVISO` versões diferentes do tronco | Os produtos foram derivados de estados diferentes da imersão | Derivar de novo ou registrar a diferença como aceita |
| `MUDOU` | A interface do vizinho mudou | Ler as linhas alteradas e verificar se afetam dependências ou pontos de integração |

### 3. Registrar

- Decisão tomada: uma linha em "Integrações com outros produtos", na seção "3–4. Usuário e escopo" de `contexto.md`.
- Risco aceito sem correção: uma linha em `aprovacoes.md`.
- Suposição do tronco confirmada ou refutada por este produto (Módulos 7 e 8): registrar no repositório da imersão, na Matriz CSD do tronco, e publicar a interface de novo, para que o vizinho receba o alerta.

## Quando executar

| Momento | Motivo |
| :--- | :--- |
| Fim do Módulo 4 | As dependências entre produtos acabam de ser declaradas |
| Fim do Módulo 6 | Eventos, contratos e entidades passam a constar na interface |
| Antes de planejar uma integração | Ver o estado atual do outro produto |
| Depois de um ciclo de Medição ou Experimentação | Propagar reclassificações de suposições do tronco |

Sem execução de scripts: preencher `interface.md` manualmente com as mesmas seções e comparar com a do vizinho item a item.

# Guia: protótipos em ferramentas de design

Para protótipos e telas feitos no Figma, no Paper e no Penpot. Tipo no cabeçalho: **Leitura de protótipo**.

## O que esta leitura é

Um protótipo trazido para a imersão mostra uma solução que alguém já desenhou. Por mais acabado que pareça, não foi validado pela esteira: entra no Módulo 1 como evidência do tipo Protótipo e sustenta Suposição ou Pedido. Pode servir de referência no Módulo 5; não substitui os Feature Frames nem a especificação de interface.

A diferença para um wireframe em foto é que o arquivo de design tem estrutura legível: nomes de telas e de camadas, textos, componentes, estilos e ligações de navegação. Essa estrutura é lida como dado, sem depender de interpretação visual.

## Como obter o conteúdo

| Ferramenta | Com conector no ambiente | Sem conector |
| :--- | :--- | :--- |
| **Figma** | Ler pelo conector, a partir do link do arquivo ou do quadro informado pelo usuário | Pedir a exportação das telas (PNG ou PDF) e, se houver, a lista de textos; tratar as imagens pelo guia de wireframes |
| **Paper** | Ler pelo conector. O servidor do Paper é local e só responde com o aplicativo de desktop aberto e o arquivo carregado; se não responder, pedir ao usuário que abra o arquivo | Pedir a exportação das telas em imagem ou do código gerado (HTML ou JSX) |
| **Penpot** | Ler pelo conector, com o arquivo aberto na ferramenta | Pedir a exportação das telas (PNG, SVG ou PDF) |

Regras de acesso:

1. Só o link, sem conector e sem exportação: pedir a exportação. Não descrever o protótipo a partir do link nem do nome do arquivo.
2. O conector é usado apenas para leitura. Não alterar o arquivo de design durante a entrada de insumos.
3. Ler somente as páginas e os quadros indicados pelo usuário. Arquivo de design costuma ter rascunhos e versões antigas; se o escopo não foi indicado, perguntar quais telas valem.
4. Guardar em `00-insumos/originais/` o que identifica a fonte: a exportação, ou um arquivo de texto com o link, a página, os quadros lidos e a data da leitura. O protótipo continua sendo editado depois.

## Formato

Um bloco por tela (quadro de nível superior), na ordem do fluxo quando houver, ou na ordem da página:

```text
## Tela: "Reservar / Disponibilidade"   (nome do quadro, como está no arquivo)

Dimensão: 390 × 844 (móvel)
Textos, na ordem de leitura:
- "Salas disponíveis"
- "Unidade Centro"
- "Hoje, 16 nov"
- "Reservar"
Componentes usados: "Button/Primary", "Select", "Calendar/Day cell" (nomes da biblioteca)
Estados presentes no arquivo: "Calendar/Day cell" com variantes "livre" e "ocupado"
Ligações de protótipo: clique em "Reservar" → tela "Reservar / Confirmar"
Comentários no arquivo: "falta estado de erro" (autor: Bianca)
[inferência] Finalidade provável: consulta de disponibilidade antes da reserva.
```

Ao final do arquivo, duas seções, quando a fonte permitir:

```text
## Fluxos
- "Reserva": Disponibilidade → Confirmar → Confirmada

## Estilos e variáveis encontrados
- Cores: "primary/500" #FF8A1F; "neutral/900" #161616
- Tipografia: "Heading/L" Outfit 32/40
```

## Regras

1. **Nomes e textos literais, entre aspas.** Nome de quadro, de camada, de componente e de variável é transcrito como está, mesmo quando é genérico ("Frame 12"). Não renomear.
2. **Estrutura lida x aparência interpretada.** O que vem da estrutura do arquivo (texto, componente, variante, ligação, variável) é fato sobre o protótipo. O que depende de olhar a imagem (hierarquia visual, finalidade, qualidade do layout) é `[inferência]`.
3. **Só o que existe no arquivo.** Estado, tela ou fluxo não desenhado não entra. Variante existente na biblioteca e não usada na tela é registrada como "disponível na biblioteca", não como parte da tela.
4. **Ligações de protótipo** são registradas como "gatilho em elemento → tela de destino". Tela sem ligação de entrada ou de saída é registrada como tal.
5. **Comentários e anotações** do arquivo são transcritos com autor e, se houver, situação (aberto ou resolvido). Costumam registrar dúvidas e decisões.
6. **Conteúdo de exemplo** (nomes, valores, datas fictícias nas telas) é marcado como exemplo. Não vira dado nem regra de negócio.
7. **Dados pessoais reais** visíveis no protótipo não são transcritos: `[dado pessoal omitido]`.
8. **Arquivo grande.** Ler uma tela por vez e gravar antes de seguir. Não carregar o arquivo inteiro nem exportar todas as telas como imagem de uma vez.
9. **Código gerado pela ferramenta** (no Paper, HTML ou JSX das telas) é uma representação do protótipo. Extrair dele textos e estrutura; não copiar o código para o insumo.

## Estilos, componentes e o Design System

Cores, tipografia, espaçamentos e componentes encontrados no arquivo descrevem o protótipo, não necessariamente o Design System oficial da empresa. Registrar o que foi encontrado e a origem (biblioteca vinculada ou estilo local). A decisão de usar esses valores como Design System é tomada no Módulo 5, com confirmação do usuário.

## Limites a registrar

Páginas e quadros lidos e não lidos, método usado (conector ou exportação), data da leitura, o que a fonte não forneceu (ligações, variáveis, comentários) e a quantidade de inferências feitas.

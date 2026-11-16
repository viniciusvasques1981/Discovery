# Guia: boards do Miro

Para boards de dinâmicas da imersão no Miro, FigJam ou ferramenta semelhante. Tipo no cabeçalho: **Extração de board**.

## Como obter o conteúdo

| Situação | O que fazer |
| :--- | :--- |
| Há conector com a ferramenta no ambiente | Ler o board pelo conector, a partir do link informado pelo usuário, e registrar "conector" em Método |
| O usuário exportou o board (CSV de post-its, PDF ou imagem) | Colocar a exportação em `00-insumos/originais/` e converter; CSV preserva o texto, imagem depende de leitura visual |
| Só há o link, sem conector | Pedir a exportação. Não descrever o board a partir do link |

Exportação em imagem de um board grande perde legibilidade: preferir a leitura pelo conector ou a exportação em CSV, e usar a imagem apenas para conferir os agrupamentos.

## Formato

Um bloco por quadro (frame) do board, na ordem de leitura:

```text
## Quadro: "Matriz CSD"

### Coluna: "Certezas"
- "3 unidades, 14 salas" (amarelo, autor: Helena)
- "Sistema atual é web" (amarelo, autor: Bianca)

### Coluna: "Suposições"
- "20% das reservas ninguém aparece" (rosa, autor: Rui; 3 votos)

Conectores: "Conflito de reserva" → "Planilha compartilhada" (seta com rótulo "causa?").
Itens soltos, fora de coluna: "integrar Google Agenda" (sem autor).
[inferência] O quadro registra a dinâmica de Certezas, Suposições e Dúvidas da imersão.
```

## Regras

1. **Um post-it por linha, texto literal entre aspas.** Não fundir post-its parecidos nem corrigir a redação.
2. **Estrutura declarada x estrutura inferida.** Título de quadro, de coluna e de seção escritos no board são estrutura declarada. Agrupamento percebido só pela proximidade é `[inferência]`: registrar "Grupo sem título [inferência]: itens próximos sobre cancelamento".
3. **Metadados quando disponíveis:** cor, autor, votos, etiquetas. A cor só tem significado se houver legenda no board; sem legenda, registrar a cor e não interpretar.
4. **Conectores** são registrados como "A → B", com o rótulo, se houver.
5. **Imagens e desenhos dentro do board** seguem o guia de wireframes, em bloco próprio dentro do quadro.
6. **Itens fora de qualquer quadro** são listados ao final, como "Itens soltos".
7. **Quadros vazios ou de instrução** (regras da dinâmica, cronograma) são citados em uma linha e não transcritos.

## O que um board representa

Post-it é o que alguém escreveu em uma dinâmica, muitas vezes em segundos. No Módulo 1 vira evidência do tipo Nota de dinâmica e sustenta Suposição. A posição de um post-it na coluna "Certezas" do board não o torna Certeza: a classificação é refeita no Módulo 1, com o critério da esteira.

## Limites a registrar

Quadros não lidos, post-its ilegíveis, metadados indisponíveis no método usado e a data em que o board foi lido, porque boards continuam sendo editados.

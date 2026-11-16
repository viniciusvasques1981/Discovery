# Guia: documentos

Para PDF, Word, apresentações e planilhas. Tipo no cabeçalho: **Documento convertido**.

## Procedimento

1. Extrair o texto com a ferramenta disponível no ambiente (leitura nativa de PDF, conversor de documentos ou script). Registrar a ferramenta em "Método".
2. Preservar a estrutura: títulos viram títulos Markdown; tabelas viram tabelas; listas continuam listas.
3. Marcar a origem de cada trecho com a página ou o slide, em linha própria: `[p. 3]`, `[slide 7]`. A marca permite conferir com o original.
4. Uma ideia por linha ou parágrafo curto. Parágrafos longos são divididos em frases, para que a citação aponte um trecho pequeno.
5. Figuras, gráficos e diagramas: descrever o que mostram, com a marca `[inferência]`, e transcrever literalmente títulos, legendas e números legíveis. Gráfico cujo valor não é legível não vira número.
6. Cabeçalhos, rodapés e numeração repetidos em toda página são removidos.

## Casos

| Situação | Tratamento |
| :--- | :--- |
| PDF digitalizado (imagem) | Só converter se houver reconhecimento de texto disponível; registrar "OCR" em Método e marcar como `[ilegível]` o que falhar |
| Apresentação com pouco texto | Converter slide a slide; anotações do apresentador entram identificadas como "Notas:" |
| Planilha | Converter cada aba relevante em tabela; planilha grande é resumida por aba, com o intervalo indicado, e os dados usados como evidência são transcritos sem arredondar |
| Documento com mais de um assunto | Manter um único arquivo; os títulos separam os assuntos |
| Documento confidencial ou com dados pessoais | Converter normalmente; `00-insumos/` não é versionado |

## Limites a registrar

Páginas não processadas, tabelas que perderam a estrutura, imagens não descritas e trechos em que o reconhecimento de texto pode ter trocado caracteres, sobretudo números.

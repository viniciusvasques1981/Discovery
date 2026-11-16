---
name: behavioral-analytics-ux-fixes
description: "Analisar dados de telemetria comportamental de ferramentas analíticas (como Microsoft Clarity) para diagnosticar fricções e quebras de interação em produção, prescrevendo correções cirúrgicas de UI e usabilidade. Cobre o Módulo 7 (Medição) do ciclo pós-entrega da esteira. Use quando houver dados de dead clicks, rage clicks, quick backs, scroll depth, heatmaps ou gravações de sessão para interpretar."
---

# Analytics Comportamental e Correções de UX

Módulo 7 — ciclo pós-entrega da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Heurísticas de usabilidade (Nielsen), Lei de Fitts, Teoria da Carga Cognitiva |
| **Entradas** | Exportações ou capturas de ferramentas analíticas (Microsoft Clarity, Hotjar, GA4), período e volume de sessões; `contexto.md` da iniciativa, quando existir |
| **Saída** | `07-diagnostico-comportamental.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `technical-handoff-prompt-engineering` |
| **Próxima skill** | `behavioral-experimentation-cro` |

## Regras de execução

1. Registrar período, volume de sessões e segmento analisado. Sem esses dados, declarar a limitação no diagnóstico.
2. Telemetria indica onde ocorre a fricção, não a causa. Toda causa raiz é hipótese até ser confirmada por gravação de sessão, teste de usabilidade ou experimento; indicar o nível de evidência de cada uma.
3. Não extrapolar a partir de amostras pequenas. Informar o volume que sustenta cada achado.
4. Correções de baixo risco e causa evidente seguem direto para implementação. Correções com causa incerta ou impacto em métrica de negócio seguem para `behavioral-experimentation-cro`.

## Coleta de dados do Microsoft Clarity

O script `scripts/clarity_resumo.py` converte a resposta da Data Export API do Clarity em tabelas Markdown, uma por métrica, para uso como insumo deste módulo.

```bash
# a partir de um arquivo JSON já exportado
python3 scripts/clarity_resumo.py --arquivo export.json > iniciativas/<slug>/00-insumos/clarity.md

# consultando a API (token em CLARITY_API_TOKEN)
python3 scripts/clarity_resumo.py --dias 3 --dimensao URL > iniciativas/<slug>/00-insumos/clarity.md
```

A API retorna dados agregados dos últimos 1 a 3 dias e tem limite diário de requisições por projeto. O período curto é uma limitação a declarar no diagnóstico; gravações de sessão e heatmaps continuam sendo consultados na interface do Clarity.

## Algoritmo de Execução

### 1. Diagnóstico de Métricas Comportamentais

- **Dead Clicks:** Elementos estáticos que sofrem cliques por falha de affordance visual (sombras inadequadas, layouts que simulam botões/links).
- **Rage Clicks:** Cliques repetidos em curto intervalo por lentidão, scripts travados ou ausência de feedback imediato de clique.
- **Quick Backs:** Navegação que retorna imediatamente ao ponto de origem devido a divergência entre a expectativa criada pela microcopy e o conteúdo real da página.
- **Scroll Depth & Heatmaps:** Dispersão da atenção, abandono prematuro ou pontos cegos de elementos críticos fora da área de foco.

### 2. Mapeamento Heurístico

Correlacionar cada anomalia a violações heurísticas (Visibilidade do Estado do Sistema, Correspondência com o Mundo Real, Controle e Liberdade do Usuário, Lei de Fitts, Carga Cognitiva).

### 3. Plano de Correção Estrutural

- Definir a intervenção direta (mudança de microcopy, inclusão de loaders/spinners, reordenação de hierarquia de informação ou ajuste de contraste/tamanho de alvo).
- Classificar o impacto esperado da intervenção (Alto, Médio, Baixo).
- Indicar o encaminhamento: correção direta ou experimento.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/07-diagnostico-comportamental.md`.

- **Tabela de Diagnóstico Comportamental:** Métrica avaliada, elemento/tela afetada, causa raiz e heurística violada.
- **Matriz de Intervenção de UX:** Solução técnica proposta, microcopy de ajuste e nível de prioridade.

## Fechamento

Atualizar apenas a seção "7–8. Pós-entrega" de `contexto.md` com os achados priorizados e as oportunidades encaminhadas para experimentação. Achados que contradizem Certezas ou confirmam/refutam Suposições da Matriz CSD são registrados como revisão do Módulo 1 em `aprovacoes.md`. Em produto derivado de imersão com vários produtos, a reclassificação é registrada também no tronco e propagada pela skill `cross-product-alignment`.

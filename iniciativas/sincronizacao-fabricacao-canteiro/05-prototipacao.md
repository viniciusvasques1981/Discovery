# Módulo 5 — Prototipação: sincronizacao-fabricacao-canteiro

> **Status:** especificação conceitual fictícia baseada na arquitetura de telas fornecida. Não representa validação com usuários, integração real ou decisão aprovada de escopo.

**Entrada:** `contexto.md`, `04-feature-frames.md`  
**Design System:** não fornecido — componentes e tokens são provisórios.

## Fluxo e arquitetura de informação

```text
Dashboard Gerencial
  ├─ Alinhamento estratégico (objetivo → alavanca → OKRs)
  ├─ Roadmap / status das frentes → detalhe do Feature Frame e escopo
  └─ Ingestão de dados → conexão SQL / importação de planilha

App Operacional (proposta sujeita à decisão de escopo)
  Login e seleção de obra → tarefas do dia → elemento / sequência
    → apontamento e foto → confirmação / fila offline
  Tarefas do dia → registro de ocorrência / impedimento
```

A arquitetura proposta contém duas superfícies e dois perfis de uso distintos. O Dashboard Gerencial se relaciona diretamente aos FF-01 a FF-03. O App Operacional detalhado abaixo amplia o escopo dos Feature Frames atuais; seus recursos específicos ficam pendentes de decisão antes de serem considerados parte do MVP.

## I. Dashboard Gerencial

### T-01 — Visão Gerencial e Sincronização

| | |
| :--- | :--- |
| **Feature Frame** | FF-01, FF-02, FF-03 |
| **Estágio da jornada** | J1 — acompanhar sincronização e identificar desvios |
| **Objetivo** | Oferecer leitura macro do estado conhecido entre fábrica e canteiro e mostrar a origem/frescor dos dados. |
| **Ação primária** | Abrir o detalhe de uma frente ou indicador com desvio. |
| **Ações secundárias** | Filtrar objetivo macro; consultar alavancas e KRs; abrir o detalhe do roadmap; acessar ingestão. |
| **Entrada / saída** | Entrada após autenticação e seleção do contexto organizacional; saída para detalhe de frente, roadmap ou ingestão. |

**Wireframe descritivo (ordem de leitura):**

1. Cabeçalho: OptiObra Core, domínio, contexto selecionado e estado da atualização. “On Track” só pode ser exibido se houver regra e dados definidos; caso contrário, mostrar “Status não calculado”.
2. Cascata estratégica: objetivo macro → alavancas → KRs. Valores como “80 → 15” e “turnover -20%” são placeholders fornecidos no exemplo, não metas aprovadas.
3. Visão central: roadmap em etapas e status por frente. Seleção de etapa abre drawer com Feature Frame, escopo In/Out e estado de aprovação.
4. Painel de governança/squad: papéis e nomes somente quando cadastrados e autorizados; sem dado, exibir estado vazio.
5. Ingestão: conexão SQL/ERP, última sincronização confirmada, resultado da importação e opção de carregar planilha; mostrar erro e fonte dos indicadores.

**Estados:**

| Estado | Comportamento |
| :--- | :--- |
| Carregando | Skeleton preserva a hierarquia; status de dados não é apresentado como atual até concluir a carga. |
| Vazio | “Ainda não há dados para este contexto. Conecte uma fonte ou carregue uma planilha.” |
| Erro | Informar fonte, horário, causa conhecida e ação possível; preservar a última atualização válida identificando-a como desatualizada. |
| Sucesso | Exibir data/hora da atualização e origem dos dados; distinguir dados atuais de importações manuais. |

### T-02 — Detalhe de Frente / Roadmap e Escopo

| | |
| :--- | :--- |
| **Feature Frame** | FF-01, FF-02 |
| **Estágio da jornada** | J1 — investigar desvio e alinhar ação |
| **Objetivo** | Consultar o estágio, os Feature Frames associados e o limite aprovado do escopo. |
| **Ação primária** | Voltar ao painel após consultar o detalhe. |
| **Ações secundárias** | Alternar entre In Scope e Out of Scope; consultar status e fonte do dado. |
| **Entrada / saída** | Drawer acionado a partir do roadmap; retorno à T-01. |

**Wireframe descritivo:** drawer lateral com título da frente, fase, status e data de atualização; resumo do Feature Frame; listas distintas de In Scope e Out of Scope; links ou referências aos detalhes. Não oferecer edição de escopo sem fluxo de autorização definido.

**Estados:** carregando, sem Feature Frames vinculados, falha ao carregar, detalhe disponível. Escopo não aprovado deve ser rotulado como “proposta”, não “aprovado”.

### T-03 — Ingestão e Qualidade das Fontes

| | |
| :--- | :--- |
| **Feature Frame** | FF-01, FF-03 |
| **Estágio da jornada** | J1/J3 — verificar disponibilidade e confiabilidade dos dados |
| **Objetivo** | Tornar visíveis as fontes disponíveis, estado da conexão/importação e atualidade dos dados. |
| **Ação primária** | Iniciar importação manual, se permitida, ou consultar o estado da conexão. |
| **Ações secundárias** | Ver histórico de sincronização; consultar campos aceitos e erros da importação. |
| **Entrada / saída** | Acesso a partir de T-01; após o processamento, retornar ao painel e indicar se os dados foram atualizados. |

**Wireframe descritivo:** cartão da conexão SQL/ERP sem expor credenciais; horário da última sincronização e resultado; área de upload XLSX com formatos e limite de arquivo a definir; prévia/validação antes de importar; lista de erros por linha; confirmação explícita antes de recálculo de indicadores.

**Estados:** sem fonte configurada; conexão ativa; sincronização em andamento; conexão indisponível; arquivo inválido; validação com erros; importação concluída; dados desatualizados. A frequência de atualização não é inferida: exibir o horário efetivamente fornecido pela fonte.

## II. App Operacional — proposta de interface, escopo pendente

> As telas abaixo reproduzem a proposta recebida. Autenticação, multi-tenancy local, uso offline, captura obrigatória de foto e notificações imediatas não estão cobertos de forma explícita pelos Feature Frames atuais. Devem ser validados e enquadrados antes do desenvolvimento.

### T-04 — Autenticação e Seleção de Obra

| | |
| :--- | :--- |
| **Feature Frame** | Pendente de enquadramento de escopo |
| **Estágio da jornada** | J2/J3 — iniciar o trabalho no contexto correto |
| **Objetivo** | Autenticar a pessoa e selecionar a unidade/obra autorizada. |
| **Ação primária** | Entrar e confirmar o contexto. |
| **Ações secundárias** | Trocar unidade; recuperar acesso, se suportado. |
| **Entrada / saída** | Abertura do app; segue para T-05. |

Não manter credenciais em texto claro. O comportamento de RBAC, seleção de tenant, expiração de sessão e dados locais precisa de decisão de segurança/arquitetura. Estado offline de login não é presumido.

### T-05 — Tarefas do Dia e Conectividade

| | |
| :--- | :--- |
| **Feature Frame** | FF-01/FF-03; enquadramento específico pendente |
| **Estágio da jornada** | J2 — consultar sequência e disponibilidade |
| **Objetivo** | Apresentar tarefas e lotes atribuídos ao contexto de obra selecionado. |
| **Ação primária** | Abrir uma tarefa/elemento. |
| **Ações secundárias** | Filtrar por frente; acessar impedimentos; consultar estado de sincronização. |
| **Entrada / saída** | Após T-04; segue para T-06 ou T-09. |

Mostrar claramente conectado, offline, sincronização pendente ou erro. Conteúdo local deve incluir horário da última atualização e não sugerir atualidade quando estiver desatualizado. Sequência diária depende de fonte e regra ainda não definidas.

### T-06 — Detalhe do Elemento e Sequenciamento

| | |
| :--- | :--- |
| **Feature Frame** | FF-03; enquadramento específico pendente |
| **Estágio da jornada** | J2/J3 — preparar a execução |
| **Objetivo** | Consultar dados disponíveis do elemento, forma/gabarito e sequência de montagem. |
| **Ação primária** | Iniciar ou registrar apontamento, se autorizado. |
| **Ações secundárias** | Consultar material relacionado; registrar impedimento. |
| **Entrada / saída** | A partir de T-05; segue para T-07 ou T-09. |

Exibir identificadores e status vindos da fonte; campos desconhecidos ficam explicitamente indisponíveis, sem valores presumidos.

### T-07 — Apontamento e Captura Fotográfica

| | |
| :--- | :--- |
| **Feature Frame** | Pendente de enquadramento de escopo e política de retenção |
| **Estágio da jornada** | J2 — registrar execução |
| **Objetivo** | Registrar conclusão e, se confirmado como necessário, anexar evidência fotográfica. |
| **Ação primária** | Salvar apontamento. |
| **Ações secundárias** | Tirar/selecionar foto; revisar registro antes do envio. |
| **Entrada / saída** | A partir de T-06; segue para T-08. |

A foto é dado potencialmente identificável. Antes de torná-la obrigatória, definir finalidade, acesso, retenção, consentimento/base aplicável e tratamento offline com responsáveis de privacidade/segurança. O protótipo não assume esses requisitos como aprovados.

### T-08 — Confirmação e Fila de Sincronização

| | |
| :--- | :--- |
| **Feature Frame** | Pendente de enquadramento de escopo |
| **Estágio da jornada** | J2 — confirmar registro |
| **Objetivo** | Confirmar salvamento local/remoto e informar o próximo estado da sincronização. |
| **Ação primária** | Voltar às tarefas. |
| **Ações secundárias** | Tentar sincronizar novamente; abrir detalhes do erro. |
| **Entrada / saída** | Após T-07; retorno a T-05. |

Diferenciar “salvo neste aparelho” de “sincronizado no servidor”. Em conflito, erro ou reenvio, preservar o registro e informar seu estado; regras de resolução, criptografia e retenção local dependem de validação técnica.

### T-09 — Registro de Ocorrência / Impedimento

| | |
| :--- | :--- |
| **Feature Frame** | FF-02/FF-03; notificações e fluxo específico pendentes |
| **Estágio da jornada** | J2/J3 — comunicar bloqueio de execução |
| **Objetivo** | Registrar falta de peça, atraso ou outro impedimento de campo. |
| **Ação primária** | Salvar e enviar/colocar em fila o impedimento. |
| **Ações secundárias** | Associar frente/elemento e incluir observação, conforme campos aprovados. |
| **Entrada / saída** | A partir de T-05 ou T-06; confirmação e retorno à tarefa. |

Informar se o alerta foi entregue, enfileirado offline ou falhou. “Notificação imediata” depende de conectividade, canal e política de notificação; não prometer entrega quando offline.

## Componentes e tokens provisórios

| Componente | Telas | Estados principais |
| :--- | :--- | :--- |
| Header e seletor de contexto | T-01, T-04, T-05 | default, carregando, erro |
| Card de indicador / badge de status | T-01, T-05, T-06 | atual, desatualizado, indisponível |
| Roadmap e drawer | T-01, T-02 | selecionado, proposta, aprovado |
| Card de fonte / upload e validação | T-01, T-03 | conexão, progresso, sucesso, falha |
| Lista de tarefas e detalhe | T-05, T-06 | pendente, em andamento, concluído, bloqueado |
| Botão de ação primária grande | T-06 a T-09 | default, focus, disabled, loading |
| Banner/fila offline | T-05, T-08, T-09 | conectado, offline, pendente, erro |

**Tokens provisórios:** usar escala de espaçamento 4/8px; cores semânticas para sucesso, aviso, erro e informação, sempre acompanhadas de rótulo/ícone; tipografia hierárquica de alta legibilidade. Valores finais dependem do Design System, não fornecido.

**Estados de interação:** default, hover (dashboard), active, focus visível, disabled e loading; feedback imediato em ações locais. Não usar apenas cor para comunicar estado.

## Acessibilidade e uso em campo

- Contraste mínimo de 4.5:1 para texto e 3:1 para componentes visuais.
- Alvos de toque de pelo menos 44×44 px no app; foco visível e ordem de teclado no dashboard.
- Rótulos acessíveis para controles e feedback anunciado por tecnologia assistiva.
- Texto/ícone junto a cores de conectividade e status; mensagens de erro com o que ocorreu, motivo conhecido e ação disponível.
- Considerar uso externo, luvas e conectividade limitada em teste futuro; não alegar usabilidade validada.

## Microcopy

| Tela | Elemento | Texto provisório |
| :--- | :--- | :--- |
| T-01 | Status sem regra/dado | “Status não calculado — verifique a atualização das fontes.” |
| T-03 | Empty state | “Nenhuma fonte configurada. Conecte uma fonte ou carregue um arquivo autorizado.” |
| T-03 | Erro | “Não foi possível importar o arquivo. Verifique o formato e os campos indicados e tente novamente.” |
| T-05 | Offline | “Sem conexão. Exibindo dados salvos em [horário]; alterações ficarão pendentes de sincronização.” |
| T-08 | Sucesso local | “Registro salvo neste aparelho. Aguardando sincronização.” |
| T-09 | CTA | “Registrar impedimento” |

## Lacunas e decisões antes do handoff

1. Confirmar se o escopo inclui Dashboard e App Operacional ou se o app é uma fase posterior.
2. Criar/atualizar Feature Frames para login/RBAC, multi-tenancy, offline-first, apontamento, fotos, impedimentos e sincronização, caso aprovados.
3. Definir regras de status, cálculo de KRs, baselines, metas e frescor dos dados; exemplos numéricos não são valores validados.
4. Definir fontes, esquema, permissões e validação/importação SQL/XLSX; a tela não implica conexão real.
5. Validar requisitos de segurança, privacidade e retenção de dados, especialmente fotos e armazenamento offline.
6. Obter Design System e definir stack/biblioteca; não especificados na entrada.
7. Avaliar com usuários de campo o fluxo sob conectividade ruim e em condições reais de uso antes de considerar o protótipo validado.

## Guia de UI para o Assistente de Código

```text
Stack de interface: não especificada; não assumir tecnologia.
Biblioteca do Design System: não fornecida; tokens são provisórios.
Componentes permitidos: header, cards, badges, timeline/roadmap, drawer, tabelas/listas, upload validado, formulários e feedback de sincronização descritos neste artefato.
Tokens obrigatórios: substituir os tokens provisórios pelo Design System aprovado; evitar valores visuais arbitrários.
Acessibilidade: contraste WCAG 2.1 AA, foco visível, navegação por teclado no dashboard, rótulos acessíveis, áreas de toque >=44×44 px e estados não comunicados só por cor.
Limites: não implementar como escopo aprovado os itens marcados como pendentes de decisão; não simular conexão SQL, sincronização ou notificação real sem integração definida.
```

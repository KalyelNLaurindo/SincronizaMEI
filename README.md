# SincronizaMEI — Sistema Integrado de Gestão (ERP)

> Gestão financeira, estoque e vendas com integridade de dados absoluta.

![Versão](https://img.shields.io/badge/versão-1.1.0-blue)
![Licença](https://img.shields.io/badge/licença-MIT-green)
![LGPD](https://img.shields.io/badge/LGPD-Compliant-blueviolet)
![Security](https://img.shields.io/badge/SAST-zero%20critical-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue?logo=githubactions)
![Cobertura](https://img.shields.io/badge/cobertura-≥90%25-brightgreen)
<br>
![Java](https://img.shields.io/badge/Java-21-orange?logo=openjdk)
![React](https://img.shields.io/badge/React-18-blue?logo=react)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?logo=tailwindcss)
![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?logo=pwa)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-7.2-red?logo=redis)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.13-orange?logo=rabbitmq)

**Fim do dinheiro no limbo. Reconciliacao financeira a prova de falhas — por design.**

![SincronizaMEI Dashboard Mockup](./assets/dashboard_mockup.png)

O **SincronizaMEI** e uma solucao completa de gestao para microempreendedores que exige o maximo de precisao financeira.
 Ele combina uma interface **PWA moderna (React + Tailwind)**, rápida e intuitiva, com um motor de reconciliação de nível bancário que trabalha incansavelmente nos bastidores para garantir que cada centavo e cada item de estoque estejam sempre onde deveriam estar.

> **Nota de Versionamento:** O projeto segue [Semantic Versioning 2.0](https://semver.org). Versões com sufixo `-RC` são release candidates sob validação de carga em staging.

---

## 📋 Tabela de Conteúdos

### I. 🚀 Produto & Experiência
1. [Visão Geral](#1-visão-geral)
2. [Requisitos do Sistema](#2-requisitos-do-sistema)
3. [Design (UI/UX) — Material 3 Vitrificado](#3-design-uiux---material-3-vitrificado)
4. [Plano de Testes — Defesa Profunda](#4-plano-de-testes--defesa-profunda-de-qualidade)

### II. 🏗️ Arquitetura & Engenharia
5. [Arquitetura de Missão Crítica](#5-arquitetura-de-missão-crítica)
6. [Segurança e Observabilidade](#6-segurança-e-observabilidade)
7. [API e Integrações](#7-api-e-integrações)
8. [Customizações e Extensibilidade](#8-customizações-e-extensibilidade)

### III. 🛠️ Desenvolvimento & Operação
9. [Quick Start](#9-quick-start)
10. [Estrutura do Código](#10-estrutura-do-código)
11. [Implantação (Deploy)](#11-implantação-deploy)
12. [Debug e Suporte Técnico](#12-debug-e-suporte-técnico)

### IV. 📈 Governança & Evolução
13. [Melhoria Contínua (20 Frentes)](#13-melhoria-contínua)
14. [Roadmap de Evolução](#14-roadmap-de-evolução)
15. [Guia de Contribuição](#15-guia-de-contribuição)
16. [Apêndices & Glossário](#16-apêndices)

---

## 1. 🎯 Visao Geral

### O Desafio: Falhas em Ambientes Distribuídos
A maioria dos ERPs do mercado opera sob a premissa do "Happy Path", assumindo que a rede e os serviços externos são infalíveis. No mundo real, timeouts ocorrem e webhooks falham silenciosamente. Isso gera o **Drift (Desvio Transacional)**: a divergência entre o saldo real e o saldo persistido. Para o microempreendedor, essa inconsistência não é apenas um erro técnico; é perda de capital e eficiência operacional.

### A Solução: Resiliência Sistêmica (Fault-Tolerance by Design)
O **SincronizaMEI** inverte o paradigma da passividade. Em vez de "esperar que a rede funcione", implementamos uma **Arquitetura de Reconciliação Proativa** baseada em eventos e workers resilientes.

| Modelo Tradicional (Passivo) | Modelo SincronizaMEI (Proativo) |
| :--- | :--- |
| Dependência de Webhooks externos | Varredura e convergência ativa de estados |
| Falha silenciosa em caso de infra instável | Recuperação automática via Workers proativos |
| Consistência baseada em "sorte" | Consistência Eventual Garantida (SLA < 15min) |

### Pilares de Engenharia & Arquitetura (Senior-Level)

- **Arquitetura MVC em Monólito & Bounded Contexts:** Desenvolvido guiado pela Programação Orientada a Objetos (POO), baseando-se no clássico MVC (Model-View-Controller) encapsulado em módulos de domínio (`Financeiro`, `Estoque` e `Vendas`). O uso rigoroso de princípios **Clean Code** e **Design Patterns** (ex: *Strategy*, *Factory*) garante um baixo acoplamento interno e facilidade extrema de evolução conceitual.
- **TDD (Test-Driven Development) como Lei:** Todo o roadmap técnico obedece o lifecycle RED-GREEN-REFACTOR. A automação das suítes de testes sempre antecede a implementação do controlador ou regra de negócio, sem abrir exceções.
- **Alta Performance com Java 21 (Virtual Threads):** Os motores de reconciliação utilizam *Project Loom* para gerenciar milhares de tarefas concorrentes de I/O com custo mínimo de memória, garantindo que o sistema escale horizontalmente de forma eficiente.
- **Persistência Bitemporal Estruturada:** Implementada via PostgreSQL `Range Types` e `Exclusion Constraints`, permitindo que o sistema reconstrua qualquer estado histórico com precisão de auditoria (Tempo de Fato vs. Tempo de Registro).
- **Idempotência a Nível de Infraestrutura:** Proteção contra duplicidade de transações e race conditions implementada via Redis `SET NX EX` no estágio inicial da requisição.
- **Experiência Dual-UX (PWA React + Tailwind):** Uma interface PWA moderna que se adapta dinamicamente ao contexto do usuário. Rapidez para o faturamento (MEI) e densidade analítica para a auditoria (Controller).
- **Observabilidade & API-First:** Sistema totalmente instrumentado (OpenTelemetry) e documentado (OpenAPI), focado em conectividade externa e diagnóstico rápido de integridade.

### Escopo e Garantias Técnicas

**Dentro do escopo — o sistema garante formalmente:**

| Garantia | Mecanismo de Enforcement | SLA (Service Level) |
|---|---|---|
| **Imutabilidade de Dados** | Triggers em nível de Banco de Dados bloqueiam `DELETE`/`UPDATE` físico | 100% (Zero Data Loss) |
| **Idempotência Resiliente** | Redis `SET NX EX` atômico + Interceptor de Infraestrutura | Janela de 24h (Configurável) |
| **Consistência Eventual** | Worker Proativo (Virtual Threads) + Fila de Dead Letter (DLQ) | Convergência em ≤ 15 min |
| **Rastreabilidade Distribuída**| Propagação de `X-Correlation-ID` (PWA → Backend → DB) | 100% das Transações |
| **Privacidade & Compliance** | Criptografia AES-256-GCM at-rest + Mascaramento `@Masked` | Auditoria Permanente (LGPD) |

**Fora do escopo — limites intencionais do sistema:**

- **Custódia de Valores:** O sistema não atua como gateway de pagamento ou banco; ele integra e reconcilia os dados provenientes dessas instituições.
- **Processamento de Câmbio Real-Time:** Suportado via snapshots diários (roadmap Q2 2026).
- **Substituição Contábil:** O ERP provê dados estruturados e auditáveis; o cálculo de impostos complexos e a emissão de NF-e são delegados via ACL (Anti-Corruption Layer).

> [!IMPORTANT]
> **Sobre limites de consistência:** O SincronizaMEI garante consistência *eventual* — não consistência *imediata* para o fluxo assíncrono. O fluxo síncrono (operações que retornam HTTP 201) é ACID por definição. Para operações assíncronas (HTTP 202), o contrato é: convergência garantida em ≤ 15 minutos. Qualquer design que exija consistência imediata em fluxo assíncrono deve ser escalado como decisão arquitetural antes da implementação.

---

## 2. 📋 Requisitos do Sistema

### 2.1 Requisitos Funcionais

#### RF-01 — Conciliação Transacional `Must` · ADR-02

**Descrição:** Sincronizar estados entre Pedido, Estoque e Financeiro usando transações ACID.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-01.1 | Uma ordem é criada com sucesso | O gateway confirma o pagamento via callback | O status muda de `PROCESSAMENTO_PENDENTE` para `CONCILIADO` em até 15 min |
| AC-01.2 | O gateway retorna valor diferente em até R$ 0,50 | O worker de reconciliação processa | Sistema aceita como `CONCILIADO` com nota de divergência |
| AC-01.3 | O gateway retorna diferença > R$ 0,50 | O worker processa | Status `DIVERGENTE_AUDITORIA` + alerta P2 disparado |

---

#### RF-02 — Motor de Idempotência `Must` · ADR-03

**Descrição:** Garantir que requisições repetidas não gerem duplicidade de lançamentos financeiros.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-02.1 | Ordem criada com `X-Idempotency-Key: uuid-A` | Mesma requisição enviada dentro de 24h | `HTTP 409` com response original cacheado — sem nova ordem |
| AC-02.2 | Duas requisições com mesma chave chegam em ms | Processamento concorrente ocorre | Apenas uma persiste via `SET NX` atômico no Redis |
| AC-02.3 | Chave expirada (> 24h) | Mesma operação enviada novamente | Nova ordem criada normalmente |

---

#### RF-03 — Gestão de Hooks `Must` · ADR-07

**Descrição:** Pontos de extensão para customizações sem alterar o binário core.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-03.1 | Plugin registra listener em `HookRegistry` | Ordem é faturada no Core | Handler executado assincronamente sem bloquear a API |
| AC-03.2 | Handler lança uma exceção | Handler é invocado | Exceção capturada + logada com `correlation_id`; Core continua |
| AC-03.3 | Plugin sem `fallback` é registrado | Sistema inicializa | `HookRegistry` rejeita o registro com erro descritivo no startup |

---

#### RF-04 — Auditoria Nativa `Must` · ADR-04

**Descrição:** Registro imutável de todas as alterações de estado ("quem", "quando", "de onde").

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-04.1 | Ordem está em `CONCILIADO` | Operador tenta `DELETE` em `financeiro.ordens` | Banco bloqueia via trigger com erro descritivo |
| AC-04.2 | Valor corrigido via reconciliação | `sp_reconciliar_ordem` é executada | Histórico contém versão anterior (`valid_to` preenchido) + nova versão, sem lacunas |
| AC-04.3 | Suporte investiga divergência | `SELECT * FROM financeiro.fn_check_integrity('uuid')` | Retorna todas as versões com `em_limbo` e `minutos_limbo` |

---

#### RF-05 — Bitemporalidade `Should` · ADR-04

**Descrição:** Consultar o estado do sistema em duas dimensões de tempo.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-05.1 | Ordem reconciliada em Janeiro e corrigida em Fevereiro | Auditoria fiscal consulta estado em Janeiro | `fn_estado_bitemporal(id, '2026-01-31')` retorna estado de Janeiro sem dados de Fevereiro |
| AC-05.2 | Transação registrada retroativamente | Sistema processa | `valid_from` (data real) ≠ `system_init` (data de registro) — ambas preservadas |

---

#### RF-06 — Suporte a Multi-moeda `Should` · Previsto Q2 2026

**Descrição:** Conversão dinâmica com base em câmbio diário, sem recálculo retroativo.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-06.1 | Ordem criada com `moeda: USD` | Sistema persiste | Valor em USD + equivalente BRL na data da transação em `valor_brl_na_data` |
| AC-06.2 | Taxa de câmbio muda no dia seguinte | Consulta histórica feita | Relatório exibe BRL original da data da transação, não a taxa atual |

> [!NOTE]
> O schema já prevê `moeda CHAR(3)` e `valor_brl_na_data` desde v1.0 para evitar migração destrutiva.

---

#### RF-07 — Notificações e Alertas Proativos `Should`

**Descrição:** Notificar ativamente usuários e operações sobre estados anômalos.

| # | Dado que... | Quando... | Então... |
|---|------------|-----------|----------|
| AC-07.1 | Transação em `PROCESSAMENTO_PENDENTE` | > 30 minutos sem callback | Alerta P2 para operações + mensagem humanizada na UI: *"Seu pagamento está sendo processado..."* |
| AC-07.2 | `DIVERGENTE_AUDITORIA` detectada | Worker de reconciliação finaliza | Registro em `auditoria.alertas` + notificação ao Controller responsável |
| AC-07.3 | DLQ ultrapassa 100 mensagens | Worker de health check executa | Alerta P1 via canal configurado (e-mail / Slack / webhook) |

---

### 2.2 Requisitos de Banco de Dados

| ID    | Requisito                  | Descrição                                                                                              |
|-------|----------------------------|--------------------------------------------------------------------------------------------------------|
| RP-01 | Procedures de Cálculo      | Reconciliação e impostos via Stored Procedures — atomicidade e redução de latência de rede             |
| RP-02 | Modelo Bitemporal          | Colunas `valid_from`, `valid_to`, `system_init_tstz`, `system_end_tstz` obrigatórias em tabelas core   |
| RP-03 | Cursor-based Pagination    | Queries de listagem com cursores (não `OFFSET`) para > 500k registros sem OOM na JVM                  |
| RP-04 | Versionamento de Schema    | DDL exclusivamente via Flyway — nenhuma migration alterada após merge em `main`                        |
| RP-05 | Diagnóstico de Integridade | `fn_check_integrity(idempotency_key)` disponível em produção para o time de suporte                    |

---

### 2.3 Requisitos Não Funcionais

#### Performance e Escalabilidade (ISO 25010)

| ID     | Requisito                                                          | Métrica                  |
|--------|--------------------------------------------------------------------|--------------------------|
| RNF-01 | Tempo de resposta para operações de escrita (POST/PUT)             | < 800ms em p95           |
| RNF-02 | Suporte a picos de 3× a carga média diária (fechamento fiscal)     | Sem degradação ou timeout|
| RNF-03 | Capacidade de catálogo                                             | 500k itens, 20k clientes |
| RNF-04 | Tempo máximo de reconciliação de ordem pendente                    | < 15 minutos             |

#### Segurança e Conformidade (LGPD)

| ID     | Requisito                                                                                  |
|--------|--------------------------------------------------------------------------------------------|
| RNF-05 | Dados PII (CPF, Conta Bancária) encriptados em repouso com AES-256-GCM                     |
| RNF-06 | Mascaramento dinâmico de PII em logs (`@Masked`) e ambientes de homologação                |
| RNF-07 | `DELETE` físico proibido em tabelas core via trigger de banco de dados                     |
| RNF-08 | Logs de auditoria imutáveis — acesso de escrita restrito ao usuário da aplicação           |

#### Disponibilidade e Recuperação

| ID     | Requisito                                                          | Meta      |
|--------|--------------------------------------------------------------------|-----------|
| RNF-09 | Disponibilidade do Core ERP                                        | ≥ 99,5%   |
| RNF-10 | Recovery Time Objective (RTO) em falha de infraestrutura           | < 30 min  |
| RNF-11 | Recovery Point Objective (RPO) — máximo de dados perdidos          | < 5 min   |

---

### 2.4 Restrições Inegociáveis do Sistema

> [!IMPORTANT]
> Qualquer decisão que viole estes princípios deve ser escalada para revisão arquitetural antes de avançar.

1. **Sem DELETE físico:** Soft-delete bitemporal obrigatório — triggers de banco garantem automaticamente.
2. **Sem lógica de negócio no Frontend:** React exibe e coleta. Cálculos e regras ficam no Java ou nas Stored Procedures.
3. **Sem acesso cross-módulo a repositórios:** Comunicação apenas via Eventos de Domínio (`ApplicationEventPublisher`).
4. **Sem H2 em testes de integração:** Testcontainers com PostgreSQL real obrigatório para qualquer teste com Procedures ou triggers.
5. **Sem credenciais no código:** `AES_SECRET_KEY` e URLs sensíveis sempre via HashiCorp Vault ou variáveis de ambiente CI/CD.

---

### 2.5 Ciclo de Vida da Transação

```mermaid
stateDiagram-v2
    direction LR

    [*] --> Criada : POST /ordens (idempotency key gerada)
    Criada --> Enfileirada : Aceita na API (HTTP 202)\nPublicada no RabbitMQ

    Enfileirada --> Processando : Worker consome da fila\nEnvia para Gateway Externo

    Processando --> ErroTecnico : Timeout / HTTP 5xx do Gateway
    Processando --> Rejeitada : Saldo insuficiente\nRegra de negócio violada
    Processando --> PendenteConciliacao : Callback HTTP 200 recebido\naguarda confirmação do Worker

    ErroTecnico --> Processando : Retry automático\n(backoff exp. — máx. 3x)
    ErroTecnico --> Limbo : Retries esgotados\n> 15 min sem resposta

    Limbo --> PendenteConciliacao : Worker de reconciliação\nencontra e processa (a cada 15 min)

    PendenteConciliacao --> Conciliada : Valores OK\n(diferença ≤ R$ 0,50)
    PendenteConciliacao --> DivergenciaAuditoria : Valores divergentes\n(diferença > R$ 0,50)

    Rejeitada --> [*] : Registro histórico mantido
    Conciliada --> [*] : Registro histórico mantido
    DivergenciaAuditoria --> Conciliada : Aprovação manual do Controller
    DivergenciaAuditoria --> [*] : Estorno solicitado
```

**Tabela de Status de Integração:**

| Status                   | Significado                                                 |
|--------------------------|-------------------------------------------------------------|
| `CRIADA`                 | Aceita pela API, publicada no RabbitMQ                      |
| `PROCESSAMENTO_PENDENTE` | Enviada ao gateway, aguardando callback                     |
| `CONCILIADO`             | Confirmada e verificada com tolerância de R$ 0,50           |
| `DIVERGENTE_AUDITORIA`   | Valor confirmado diferente do esperado (requer auditoria)   |
| `REJEITADA`              | Saldo insuficiente ou regra de negócio violada              |

---

### 2.6 Definition of Done

Um item de backlog só é **Pronto** quando todos os critérios abaixo são atendidos:

- [ ] SQL validado via `EXPLAIN ANALYZE` — sem Full Table Scans em tabelas core
- [ ] Swagger/OpenAPI atualizado e retrocompatível
- [ ] Testes de integração simulam falhas de rede (Chaos Engineering leve)
- [ ] Documentação "Como Dar Suporte" atualizada para o novo recurso
- [ ] Cobertura de testes unitários ≥ 85% e zero vulnerabilidades críticas (SAST)
- [ ] LGPD: nenhum campo PII novo sem `@Masked` ou encriptação AES-256

---
### 📈 Métricas de Sucesso (OKRs Técnicos)

| Métrica | Baseline | Meta (6m) | Monitoramento |
| :--- | :---: | :---: | :--- |
| 💰 **Reconciliação Manual** | ~4h/sem | **< 15 min** | Jira / Survey |
| 🌀 **Ordens em Limbo (>30m)** | ~8% | **< 0,1%** | Prometheus Gauge |
| 🛡️ **Idempotência (Duplicidade)** | N/A | **Zero** | Sentry / P1 Alerts |
| ⚡ **Lighthouse (PWA/Perf)** | ~70 | **≥ 95** | Lighthouse CI |
| 📱 **TTI (p95 3G)** | ~5s | **≤ 2.5s** | Web Vitals |
| 🧪 **Cobertura de Testes** | 0% | **≥ 90%** | JaCoCo / Jest |
| ⏱️ **Latência p95 (Escrita)** | N/A | **< 800ms** | OpenTelemetry |
| 🏗️ **RTO (Disaster Recovery)** | N/A | **< 30 min** | Runbook Drill |

---

## 4. 🧪 Plano de Testes — Defesa Profunda

### 4.6 Estratégia de Testes

| Tipo        | Ferramentas          | Escopo                                                          |
|-------------|----------------------|-----------------------------------------------------------------|
| Unitários   | JUnit 5 / Mockito    | Regras de negócio isoladas e lógica de hooks                    |
| Integração  | Testcontainers       | Stored Procedures no PostgreSQL real e filas no RabbitMQ        |
| E2E         | Cypress / Playwright | Fluxos bitemporais: da criação da ordem à auditoria histórica   |
| Performance | k6                   | Stress tests simulando picos de 3× a carga média               |
| Chaos Eng.  | Pumba / Toxiproxy    | Injeção de latência para validar retries e DLQs                 |

**Regras inegociáveis:**
- Testcontainers obrigatório para qualquer teste com Procedures ou triggers — H2 não reproduz comportamento real
- `@MockBean` apenas para serviços externos (Gateways). Lógica interna: mocks puros com Mockito

---

---

## 5. 🏗️ Arquitetura de Missão Crítica

## 1. Matriz de Rastreabilidade e Riscos

Esta matriz vincula os requisitos críticos de negócio às decisões técnicas, garantindo que nenhum "porquê" seja perdido ao longo da evolução do sistema.

| Requisito / Causa Raiz       | Risco (Ameaça)                                    | Impacto  | Decisão Arquitetural (ADR)                          |
|------------------------------|---------------------------------------------------|----------|-----------------------------------------------------|
| **Consistência Financeira**  | "Dinheiro no limbo" por falha de rede             | Crítico  | **ADR-02**: EDA com RabbitMQ + Reconciliador SQL    |
| **Idempotência**             | Cobranças duplicadas em retries de API            | Crítico  | **ADR-03**: Controle de Chaves via Redis            |
| **Auditoria / Compliance**   | Perda de histórico de alterações                  | Alto     | **ADR-04**: Persistência Bitemporal Nativa          |
| **LGPD / PII**               | Exposição de dados sensíveis em logs/DB           | Crítico  | **ADR-05**: AES-256-GCM + Mascaramento Dinâmico     |
| **Versionamento de Schema**  | Inconsistência de DDL entre ambientes             | Alto     | **ADR-06**: Flyway com Rollback Testado             |
| **Customização (ERP)**       | Regras de cliente quebram o Core                  | Médio    | **ADR-07**: Sistema de Hooks Isolados               |
| **Escalabilidade**           | Monólito acoplado dificulta extração futura       | Médio    | **ADR-01**: Arquitetura MVC em Monólito com Bounded Contexts |

---

## 2. Architecture Decision Records (ADRs)

### ADR-01 — Arquitetura MVC em Monólito com Padrões Ágeis (POO, TDD, Clean Code)

- **Status:** Aceito
- **Contexto:** Necessidade de alta performance sem a sobrecarga de gerenciar dezenas de microsserviços precocemente. É vital manter o nível do código legível, testado e estruturado a padrões clássicos de mercado (POO e MVC).
- **Decisão:** Backend em **Java 21 (Spring Boot 3)** organizado no padrão MVC. Models de domínio (`financeiro`, `estoque`), Views providas por DTOs REST, e Controllers dedicados baseados na **Programação Orientada a Objetos**. 
A engenharia é puramente **TDD First** (RED-GREEN-REFACTOR), e a inserção indiscriminada de lógica nos arquivos é proibida pelo selo do **Clean Code** (buscando usar padrões consolidados de GoF como Facades, Factory, e Strategy).
- **Consequências:**
  - ✅ Coverage altíssimo nativo pelo TDD e isolamento testável proporcionado pelos Padrões de Projeto.
  - ✅ Deploy único MVC com debugging simplificado.
  - ⚠️ Exige forte disciplina de POO — evitar os "God Objects" em controllers longos.
- **Critério de Revisão:** Reavaliar para microsserviços se o monolito exceder 100k LOC.

---

### ADR-02 — Arquitetura Orientada a Eventos (EDA) com RabbitMQ

- **Status:** Aceito
- **Contexto:** Integrações com gateways de pagamento REST são inerentemente instáveis (falhas de rede, timeouts, callbacks atrasados). O modelo síncrono cria acoplamento de tempo real com terceiros.
- **Decisão:** Uso de **RabbitMQ** para desacoplar a aceitação do pedido (`202 Accepted`) do seu processamento financeiro efetivo. Workers assíncronos com Dead Letter Queues (DLQ) para falhas definitivas.
- **Consequências:**
  - ✅ Resiliência total: se o gateway cair, a mensagem aguarda na fila com backoff exponencial.
  - ✅ Escalabilidade horizontal dos workers de reconciliação.
  - ⚠️ Consistência eventual: o estado do pedido pode não ser imediatamente visível no frontend — requer feedback via UI de "Processamento em Curso".

---

### ADR-03 — Idempotência via Redis com SET NX EX

- **Status:** Aceito
- **Contexto:** Clientes e gateways realizam retries automáticos em caso de timeout. Sem controle de idempotência, cada retry pode gerar uma nova cobrança ou entrada de estoque.
- **Decisão:** Implementar `IdempotencyInterceptor` no Spring que verifica a `X-Idempotency-Key` no Redis com `SET key response NX EX 86400` (atômico, expira em 24h). Se a chave já existir, o response cacheado é retornado sem reprocessamento.
- **Consequências:**
  - ✅ Prevenção de dupla cobrança garantida em nível de protocolo HTTP (Camada 7).
  - ✅ O Redis como cache de idempotência é separado logicamente do cache de leitura.
  - ⚠️ Requer que clientes gerem UUIDs v4 únicos por tentativa de operação.

---

### ADR-04 — Bitemporalidade SQL Nativa no PostgreSQL

- **Status:** Aceito
- **Contexto:** ERPs exigem saber como o dado estava em uma data retroativa (ex: fechamento de folha, auditoria fiscal). ALTER + DELETE destroem o histórico.
- **Decisão:** Implementação de quatro colunas de controle em todas as tabelas core:
  - `valid_from` / `valid_to` — Tempo de Validade (quando o evento ocorreu no negócio)
  - `system_init_tstz` / `system_end_tstz` — Tempo de Sistema (quando o ERP registrou)

  Operações de `DELETE` físico são proibidas via `TRIGGER BEFORE DELETE`. Alterações geram um novo registro com `valid_from = NOW()` e fecham o anterior com `valid_to = NOW()`.
- **Consequências:**
  - ✅ Trilha de auditoria imutável por design — permanentemente `audit-ready`.
  - ✅ Consultas históricas precisas via `fn_estado_bitemporal(id, as_of_date)`.
  - ⚠️ Aumenta o volume de dados. Exige política de archiving para tabelas com alto volume de mutações.

---

### ADR-05 — LGPD: AES-256-GCM + Mascaramento Dinâmico

- **Status:** Aceito
- **Contexto:** Dados de CPF, contas bancárias e e-mails são PII (Personal Identifiable Information) e estão sujeitos à LGPD. Logs e dumps de banco não podem conter essas informações em texto claro.
- **Decisão:**
  1. **Em repouso (at-rest):** Dados PII encriptados com **AES-256-GCM** antes de persistência (via `pgcrypto` no banco ou na camada Java, dependendo do campo).
  2. **Em logs:** Uso da anotação `@Masked` em campos de DTO para que o serializador de log substitua o valor por `***-[últimos 4 dígitos]`.
  3. **Em homologação:** Script de higienização de PII (`anonymize_dump.sql`) obrigatório antes de restaurar dumps de produção.
- **Consequências:**
  - ✅ Compliance LGPD com rastreabilidade — mantemos o **hash** do dado para cruzamento de logs sem expor a PII.
  - ⚠️ Queries de busca por CPF/e-mail devem usar o hash, não o valor original.

---

### ADR-06 — Flyway para Versionamento de Schema DDL

- **Status:** Aceito
- **Contexto:** Sem controle de schema, inconsistências entre ambientes (dev/staging/prod) causam bugs silenciosos difíceis de reproduzir.
- **Decisão:** **Flyway** como único mecanismo de alteração de DDL. Nenhuma migration pode ser alterada após o merge na branch `main`. Rollbacks são implementados como novas migrations `Vx__rollback_*.sql`.
- **Consequências:**
  - ✅ Paridade garantida entre ambientes via IaC + Flyway.
  - ✅ Pipeline de CI bloqueia deploy se houver migration pendente não aplicada.
  - ⚠️ Migrations de Stored Procedures têm convenção própria em `db/procedures/` e são re-executadas via `REPLACE`.

---

### ADR-07 — Extensibilidade via Hook System Isolado

- **Status:** Aceito
- **Contexto:** Clientes ERP exigem customizações de negócio. Permitir acesso ao Core cria risco de regressão e quebra de contratos internos.
- **Decisão:** Implementar um `HookRegistry` no Java. Eventos de domínio (`OrdemFaturadaEvent`, `EstoqueMovimentadoEvent`) são publicados via `ApplicationEventPublisher`. Listeners customizados (em `plugins/`) ouvem esses eventos sem acesso ao repositório ou serviço do Core.
- **Consequências:**
  - ✅ Customizações isoladas — bugs em plugins não quebram o Core.
  - ✅ Deploy de customizações sem necessidade de recompilar o ERP principal.
  - ⚠️ Plugins não podem executar operações síncronas bloqueantes na thread principal. Fallback obrigatório.

---

## 3. Diagramas de Arquitetura (C4 Model)

### Nível 1 — Contexto do Sistema

```mermaid
C4Context
    title Diagrama de Contexto — SincronizaMEI

    Person(mei, "Usuário MEI", "Gestor de pequeno negócio. Usa o sistema para faturar e controlar fluxo de caixa.")
    Person(analyst, "Controller / Analista", "Audita dados históricos e reconcilia divergências.")

    System(erp, "SincronizaMEI Core ERP", "Plataforma de gestão financeira e operacional com reconciliação bitemporal.")

    System_Ext(gateway, "Gateway de Pagamento", "Processa transações PIX, cartão e boleto.")
    System_Ext(receita, "Receita Federal / SEFAZ", "Consulta e emissão de NF-e.")

    Rel(mei, erp, "Fatura, consulta saldo, gerencia estoque")
    Rel(analyst, erp, "Audita histórico e reconcilia divergências")
    Rel(erp, gateway, "Envia ordens de pagamento e recebe callbacks", "HTTPS/REST")
    Rel(erp, receita, "Emite NF-e e consulta CNPJ", "HTTPS/SOAP")
```

### Nível 2 — Contêineres e Fluxo de Dados

```mermaid
C4Container
    title Diagrama de Contêineres — SincronizaMEI

    Person(user, "Usuário", "MEI ou Controller")

    Container(spa, "SPA React", "React 18 / Vite", "Interface com modo Operacional (MEI) e Auditoria (Especialista).")

    Boundary(backend, "Core ERP — Java 17") {
        Container(api, "API REST", "Spring Web MVC", "Entrypoint com Idempotency Interceptor e rate limiting.")
        Container(hook_engine, "Hook Registry", "Spring Events", "Publica eventos de domínio para listeners de plugins.")
        Container(worker, "Reconciliation Worker", "Spring Batch + Quartz", "Job de varredura a cada 15 min via sp_reconciliar_ordem.")
        Container(acl, "Anti-Corruption Layer", "Spring RestTemplate / WebClient", "Adapters para gateways externos com Circuit Breaker e Retry.")
    }

    ContainerDb(postgres, "PostgreSQL 15", "Bitemporal", "Tabelas core com valid_from/to. Stored Procedures de reconciliação e cálculo fiscal.")
    ContainerDb(redis, "Redis 7", "KV Store", "Cache de idempotência (TTL 24h) e dados de sessão.")
    ContainerQueue(rabbit, "RabbitMQ 3.12", "Message Broker", "Filas de processamento assíncrono com DLQ e backoff exponencial.")
    System_Ext(gateway, "Gateway Externo", "PIX / Cartão")

    Rel(user, spa, "Usa", "HTTPS")
    Rel(spa, api, "Requisições JSON", "HTTPS + X-Idempotency-Key")
    Rel(api, redis, "Verifica + armazena chave de idempotência", "SET NX EX")
    Rel(api, rabbit, "Enfileira eventos de falha ou processamento assíncrono")
    Rel(api, hook_engine, "Publica eventos de domínio após persistência")
    Rel(hook_engine, postgres, "Persiste estado via Stored Procedures")
    Rel(worker, postgres, "Executa sp_reconciliar_ordem a cada 15 min")
    Rel(acl, gateway, "Envia ordens e recebe callbacks", "HTTPS/REST")
    Rel(rabbit, acl, "Consome eventos de reconciliação pendente")
```

---

## 4. Camada de Dados: SQL de Missão Crítica

As procedures abaixo são o coração da integridade do sistema. O Java orquestra; o banco garante atomicidade.

### 4.1 Schema Bitemporal Base

```sql
-- Padrão de colunas bitemporais em todas as tabelas core
-- valid_from / valid_to   → Tempo de Validade (quando o evento ocorreu no negócio)
-- system_init / system_end → Tempo de Sistema (quando o ERP processou)

CREATE TABLE financeiro.ordens (
    id               UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
    idempotency_key  UUID        NOT NULL,
    cliente_id       UUID        NOT NULL,
    valor_total      NUMERIC(15, 2) NOT NULL,
    moeda            CHAR(3)     NOT NULL DEFAULT 'BRL',
    status           TEXT        NOT NULL,
    -- Dimensões bitemporais
    valid_from       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    valid_to         TIMESTAMPTZ NOT NULL DEFAULT 'infinity',
    system_init      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    system_end       TIMESTAMPTZ NOT NULL DEFAULT 'infinity',
    -- Rastreabilidade
    correlation_id   UUID,
    criado_por       TEXT        NOT NULL,
    CONSTRAINT uq_ordem_ativa UNIQUE (idempotency_key, valid_to)
);

-- Índices otimizados para consultas bitemporais e de reconciliação
CREATE INDEX idx_ordens_status_pendente ON financeiro.ordens (status, valid_from)
    WHERE status = 'PROCESSAMENTO_PENDENTE' AND valid_to = 'infinity';

CREATE INDEX idx_ordens_idempotency ON financeiro.ordens (idempotency_key)
    WHERE valid_to = 'infinity';

-- Trigger: bloqueia DELETE físico
CREATE OR REPLACE FUNCTION financeiro.bloquear_delete_fisico()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    RAISE EXCEPTION 'DELETE físico proibido em tabelas core. Use valid_to = NOW() para soft-delete bitemporal.';
END;
$$;

CREATE TRIGGER trg_bloquear_delete
    BEFORE DELETE ON financeiro.ordens
    FOR EACH ROW EXECUTE FUNCTION financeiro.bloquear_delete_fisico();
```

### 4.2 `sp_reconciliar_ordem` — Reconciliação com Tratamento de Exceção Sênior

```sql
CREATE OR REPLACE PROCEDURE financeiro.sp_reconciliar_ordem(
    p_idempotency_key   UUID,
    p_valor_confirmado  NUMERIC(15, 2),
    p_correlation_id    UUID DEFAULT NULL
)
LANGUAGE plpgsql AS $$
DECLARE
    v_valor_original  NUMERIC(15, 2);
    v_status_final    TEXT;
    v_ordem_id        UUID;
BEGIN
    -- Inicia bloco protegido com tratamento de exceção granular
    BEGIN
        -- Lock pessimista com NOWAIT: evita deadlocks ao tentar reconciliar a mesma ordem em paralelo
        SELECT id, valor_total
        INTO   v_ordem_id, v_valor_original
        FROM   financeiro.ordens
        WHERE  idempotency_key = p_idempotency_key
          AND  valid_to = 'infinity'
          AND  status   = 'PROCESSAMENTO_PENDENTE'
        FOR UPDATE NOWAIT;

        -- Regra de negócio: tolerância de R$ 0,50 para taxas de gateway não previstas
        IF ABS(v_valor_original - p_valor_confirmado) <= 0.50 THEN
            v_status_final := 'CONCILIADO';
        ELSE
            v_status_final := 'DIVERGENTE_AUDITORIA';
        END IF;

        -- Manobra Bitemporal: "versiona" o registro atual sem deletá-lo
        UPDATE financeiro.ordens
        SET    valid_to = NOW(),
               system_end = NOW()
        WHERE  id = v_ordem_id;

        -- Insere nova versão com o status reconciliado
        INSERT INTO financeiro.ordens (
            idempotency_key, cliente_id, valor_total, moeda, status,
            valid_from, correlation_id, criado_por
        )
        SELECT
            idempotency_key, cliente_id, p_valor_confirmado, moeda, v_status_final,
            NOW(), COALESCE(p_correlation_id, correlation_id), 'worker_reconciliacao'
        FROM financeiro.ordens
        WHERE id = v_ordem_id;

    EXCEPTION
        -- Ordem já sendo reconciliada por outro worker: ignora silenciosamente
        WHEN lock_not_available THEN
            RAISE NOTICE 'Ordem % em processamento por outro worker. Ignorando.', p_idempotency_key;

        -- Ordem não encontrada no estado esperado: loga e propaga
        WHEN no_data_found THEN
            INSERT INTO auditoria.logs_erro (contexto, chave, erro, correlation_id, data)
            VALUES ('sp_reconciliar_ordem', p_idempotency_key::TEXT,
                    'Ordem não encontrada em estado PROCESSAMENTO_PENDENTE',
                    p_correlation_id, NOW());
            RAISE;

        -- Erro genérico: loga com contexto completo para O11y e propaga
        WHEN OTHERS THEN
            INSERT INTO auditoria.logs_erro (contexto, chave, erro, correlation_id, data)
            VALUES ('sp_reconciliar_ordem', p_idempotency_key::TEXT, SQLERRM, p_correlation_id, NOW());
            RAISE;
    END;
END;
$$;
```

### 4.3 `fn_check_integrity` — Diagnóstico de Integridade para Suporte Técnico

```sql
-- Retorna o estado completo de uma transação para diagnóstico sem acesso ao código-fonte
-- Uso: SELECT * FROM financeiro.fn_check_integrity('uuid-da-ordem');
CREATE OR REPLACE FUNCTION financeiro.fn_check_integrity(p_idempotency_key UUID)
RETURNS TABLE (
    versao          INT,
    status          TEXT,
    valor_total     NUMERIC(15, 2),
    valid_from      TIMESTAMPTZ,
    valid_to        TIMESTAMPTZ,
    system_init     TIMESTAMPTZ,
    correlation_id  UUID,
    em_limbo        BOOLEAN,
    minutos_limbo   NUMERIC
)
LANGUAGE sql STABLE AS $$
    SELECT
        ROW_NUMBER() OVER (ORDER BY valid_from)::INT AS versao,
        o.status,
        o.valor_total,
        o.valid_from,
        o.valid_to,
        o.system_init,
        o.correlation_id,
        -- Detecta "dinheiro no limbo": pendente há mais de 30 minutos
        (o.status = 'PROCESSAMENTO_PENDENTE'
            AND o.valid_to = 'infinity'
            AND o.valid_from < NOW() - INTERVAL '30 minutes') AS em_limbo,
        ROUND(EXTRACT(EPOCH FROM (NOW() - o.valid_from)) / 60, 1) AS minutos_limbo
    FROM financeiro.ordens o
    WHERE o.idempotency_key = p_idempotency_key
    ORDER BY o.valid_from ASC;
$$;
```

### 4.4 `fn_estado_bitemporal` — Consulta Point-in-Time para Auditoria

```sql
-- Retorna como o sistema enxergava uma ordem em um momento específico do passado
-- Uso: SELECT * FROM financeiro.fn_estado_bitemporal('uuid', '2026-01-15 10:00:00+00');
CREATE OR REPLACE FUNCTION financeiro.fn_estado_bitemporal(
    p_idempotency_key UUID,
    p_as_of           TIMESTAMPTZ
)
RETURNS SETOF financeiro.ordens
LANGUAGE sql STABLE AS $$
    SELECT *
    FROM   financeiro.ordens
    WHERE  idempotency_key = p_idempotency_key
      AND  valid_from     <= p_as_of
      AND  valid_to        > p_as_of
      AND  system_init    <= p_as_of
      AND  system_end      > p_as_of;
$$;
```

---

---

### Princípio Arquitetural Central

A arquitetura do SincronizaMEI resolve um problema fundamental de **confiança em sistemas distribuídos**: como garantir que um estado financeiro seja verdadeiro quando parte da infraestrutura pode falhar silenciosamente?

A resposta é uma combinação de três princípios que se reforçam mutuamente:

1. **Eventos como fonte de verdade** (EDA com RabbitMQ): Nenhuma transação é considerada "perdida" enquanto existir na fila. O estado do banco é uma *projeção* dos eventos, não a fonte primária.
2. **Tempo como dado de primeira classe** (Bitemporalidade): O banco não armazena apenas "o que é verdade agora", mas "o que era verdade em cada momento" — em duas dimensões temporais independentes.
3. **Idempotência por protocolo, não por esperança** (Redis SET NX): A unicidade de operações é garantida na camada de transporte, não por validação de negócio que pode ter race conditions.

---

## 9. 🚀 Quick Start

### 🚀 Modo Expresso (Docker All-in-One)
Para ver o ecossistema completo rodando em menos de 5 minutos (Frontend + Backend + Infra):

```bash
# Sobe todos os serviços, aplica migrations e inicia o HMR do Front
docker compose up -d --build
```
> **Nota:** Certifique-se de que as portas `8080`, `5173`, `5432`, `6379` e `5672` estão livres.

---

## 10. 📂 Estrutura do Código e Diretrizes

A organização segue o padrão de **Monólito Modular com Fronteiras de Domínio Explícitas**. O critério de organização não é técnico (não temos pasta `services/` global) — é de domínio de negócio. Cada pasta em `modules/` é um Bounded Context que poderia, em tese, ser extraído como microsserviço sem modificações na lógica interna.

```
SincronizaMEI/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml               # Build → Lint → Test → SAST → Coverage Gate
│   │   ├── cd-staging.yml       # Flyway Staging → k6 Smoke → Deploy Blue-Green
│   │   ├── cd-production.yml    # Aprovação manual → Traffic Switch → Healthcheck
│   │   └── security-scan.yml    # Trivy CVE + TruffleHog secrets scan (semanal)
│   └── CODEOWNERS               # Aprovação obrigatória por domínio (financeiro → @sênior-fintech)
│
├── db/
│   ├── migrations/              # Flyway DDL — sequencial, imutável após merge em main
│   │   ├── V001__schema_inicial.sql
│   │   ├── V002__indices_parciais_limbo.sql
│   │   ├── V003__exclusion_constraints_bitemporais.sql
│   │   └── ...
│   └── procedures/
│       ├── sp_reconciliar_ordem.sql      # Reconciliação atômica com transição de estado
│       ├── sp_aprovar_divergencia.sql    # Aprovação manual de DIVERGENTE_AUDITORIA
│       ├── sp_anonimizar_titular.sql     # LGPD — Direito ao Esquecimento
│       ├── fn_check_integrity.sql        # Diagnóstico de integridade por idempotency_key
│       └── fn_estado_bitemporal.sql      # Consulta de estado em duas dimensões temporais
│
├── backend/
│   ├── src/main/java/br/com/sincronizamei/
│   │   ├── api/
│   │   │   ├── controllers/             # REST Controllers — apenas I/O, sem lógica de negócio
│   │   │   ├── interceptors/
│   │   │   │   ├── IdempotencyInterceptor.java   # SET NX EX antes de qualquer handler
│   │   │   │   └── CorrelationIdInterceptor.java # Propaga X-Correlation-ID para MDC + DB
│   │   │   └── filters/
│   │   │       └── MaskedLoggingFilter.java      # Mascara @Masked antes de logar request body
│   │   │
│   │   ├── modules/                     # Bounded Contexts — isolados por package
│   │   │   ├── financeiro/
│   │   │   │   ├── domain/              # Entidades, Value Objects, Domain Events
│   │   │   │   ├── application/         # Use Cases (Application Services)
│   │   │   │   ├── infrastructure/      # Repositórios, Publishers de evento
│   │   │   │   └── FinanceiroModule.java # Configuração do módulo — único ponto de entrada
│   │   │   ├── estoque/                 # Mesma estrutura hexagonal
│   │   │   └── rh/                      # Mesma estrutura hexagonal
│   │   │
│   │   ├── reconciliacao/               # Domínio de Reconciliação — separado por criticidade
│   │   │   ├── worker/
│   │   │   │   └── ReconciliationWorker.java    # Job Quartz + Virtual Threads
│   │   │   └── procedures/
│   │   │       └── ReconciliacaoProcedureAdapter.java  # Adapter para sp_reconciliar_ordem
│   │   │
│   │   ├── plugins/
│   │   │   ├── HookRegistry.java        # Registry com validação de contrato e timeout
│   │   │   ├── HookExecutor.java        # Thread pool dedicada + DLQ de hooks
│   │   │   └── examples/               # Exemplos documentados de implementação de plugins
│   │   │
│   │   └── infra/
│   │       ├── persistence/             # DataSource, JPA config, Flyway bean
│   │       ├── messaging/               # RabbitMQ config, DLX policy, serialization
│   │       ├── security/                # AES-256-GCM, @Masked processor, Vault integration
│   │       └── observability/           # OpenTelemetry config, Prometheus metrics registry
│   │
│   └── src/test/
│       ├── unit/                        # JUnit 5 + Mockito — sem I/O externo
│       ├── integration/                 # Testcontainers — PostgreSQL + RabbitMQ reais
│       └── architecture/
│           └── ModuleBoundaryTest.java  # ArchUnit: financeiro não acessa repo de estoque
│
├── frontend/
│   ├── src/
│   │   ├── features/
│   │   │   ├── mei-operacional/         # Modo MEI: dashboard simplificado, faturamento
│   │   │   ├── auditoria/               # Modo Controller: timeline bitemporal, divergências
│   │   │   ├── resiliencia/             # Circuit Breaker dashboard, status de gateways
│   │   │   └── shared/                  # Componentes compartilhados entre modos
│   │   ├── hooks/
│   │   │   ├── useIdempotentMutation.ts # Abstrai X-Idempotency-Key + affordance visual
│   │   │   ├── useBitemporalQuery.ts    # Consultas com valid_as_of e system_as_of
│   │   │   └── useCircuitBreaker.ts     # Subscrição SSE para estado de saúde de gateways
│   │   └── store/
│   │       ├── reconciliacao.slice.ts   # Estado global de reconciliação (Zustand)
│   │       └── system-health.slice.ts   # Estado de saúde de integrações externas
│   └── src/test/
│       ├── unit/                        # Vitest + Testing Library
│       └── e2e/                         # Playwright (fluxos críticos)
│
└── README.md
```

### 7.1 Filosofia de Organização — Decisões que Não São Óbvias

**Por que `reconciliacao/` é um módulo separado de `financeiro/`?**
A reconciliação é o mecanismo de *healing* do sistema — ela lê e corrige dados de múltiplos módulos. Colocá-la dentro de `financeiro/` criaria dependência de `financeiro` para `estoque` e vice-versa. Como módulo próprio, ela pode orquestrar sem pertencer a nenhum Bounded Context específico.

**Por que `procedures/` está fora do `backend/`?**
Stored Procedures são cidadãs de primeira classe — não são implementação do backend, são parte do domínio de dados. Tê-las em `db/procedures/` permite versionamento independente, code review especializado por DBAs, e deploy via Flyway sem recompilar o Java.

**Por que `architecture/` no diretório de testes?**
ArchUnit testes que validam as fronteiras de módulo são tão importantes quanto testes unitários. Tê-los em `src/test/architecture/` garante que o CI os executa e que violações de bounded context falham o build — não apenas aparecem em code review.

---

### 4.1 Estrutura do Monólito Modular

**Raiz do pacote:** `br.com.sincronizamei`

```
br.com.sincronizamei
├── core/          # Infraestrutura compartilhada: exceções globais, interceptors, utils
├── financeiro/    # Faturamento, reconciliação, bitemporalidade
├── estoque/       # Movimentação e inventário
├── rh/            # Capital humano e folha
└── integration/   # Clientes REST externos (ACL — Anti-Corruption Layer)
```

**Regra de ouro:** Um módulo comunica com outro via `ApplicationEventPublisher` + `@TransactionalEventListener`, nunca injetando repositórios ou serviços internos de outro módulo.

```java
// ✅ CORRETO — publicar evento após commit
eventPublisher.publishEvent(new OrdemCriadaEvent(this, ordem.getId(), dto.getItens()));

// ✅ CORRETO — ouvir evento no módulo de estoque
@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
public void onOrdemCriada(OrdemCriadaEvent event) {
    estoqueService.reservarItens(event.getOrdemId(), event.getItens());
}

// ❌ PROIBIDO — cross-módulo direto
@Autowired
private EstoqueRepository estoqueRepository; // em FaturamentoService
```

---

### 4.2 Persistência Bitemporal

**Regra:** Mutações em entidades bitemporais **somente via Stored Procedure**.

```java
// ✅ CORRETO — via EntityManager.createNativeQuery()
em.createNativeQuery("CALL financeiro.sp_reconciliar_ordem(:key, :valor, :correlation)")
  .setParameter("key", idempotencyKey)
  .setParameter("valor", valorConfirmado)
  .setParameter("correlation", correlationId)
  .executeUpdate();

// ❌ PROIBIDO — sobrescreve valid_to acidentalmente
ordemRepository.save(ordem.setStatus("CONCILIADO"));
```

**Convenção Flyway:**
- DDL/DML: `src/main/resources/db/migration/V{timestamp}__{descricao}.sql`
- Procedures: `src/main/resources/db/procedures/` (re-executadas via `CREATE OR REPLACE`)

---

### 4.3 Idempotência e Resiliência

**`IdempotencyInterceptor` — Fluxo:**

```java
@Component
@Order(1)
public class IdempotencyInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest req, HttpServletResponse res, Object handler) throws Exception {
        String key = req.getHeader("X-Idempotency-Key");
        if (key == null) return true;

        String cached = redis.opsForValue().get("idempotency:" + key);
        if (cached != null) {
            res.setStatus(HttpStatus.OK.value());
            res.setContentType(MediaType.APPLICATION_JSON_VALUE);
            res.getWriter().write(cached);
            return false; // Interrompe a chain sem reprocessar
        }
        redis.opsForValue().setIfAbsent("idempotency:" + key, "PROCESSING", 24, TimeUnit.HOURS);
        return true;
    }
}
```

**Resiliência de Gateway com `@Retryable`:**

```java
@Retryable(
    retryFor   = { ResourceAccessException.class, HttpServerErrorException.class },
    maxAttempts = 4,
    backoff    = @Backoff(delay = 1000, multiplier = 2) // 1s, 2s, 4s, 8s
)
public GatewayResponseDTO enviarOrdem(OrdemRequestDTO dto) { /* ... */ }

@Recover
public GatewayResponseDTO onFalhaCritica(RuntimeException ex, OrdemRequestDTO dto) {
    rabbitTemplate.convertAndSend("gateway.dlq", dto); // Falha definitiva → DLQ
    throw new GatewayIndisponivelException("Gateway indisponível após 4 tentativas", ex);
}
```

---

### 4.4 Observabilidade e LGPD

**Mascaramento `@Masked`:**

```java
public class ClienteDTO {
    private String nome;

    @Masked // Serializado como "***-1234" em logs
    private String cpf;

    @Masked
    private String contaBancaria;
}
```

**Encriptação AES-256-GCM:**

```java
@Component
public class AesGcmEncryptor {
    public String encrypt(String plaintext) {
        byte[] iv = new byte[12]; // 96 bits para GCM
        new SecureRandom().nextBytes(iv);
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, new GCMParameterSpec(128, iv));
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(concat(iv, ciphertext));
    }
}
```

---

### 4.5 Frontend (React & UX)

| Tipo de Estado                      | Solução             | Justificativa                                           |
|-------------------------------------|---------------------|---------------------------------------------------------|
| Dados de domínio (ordens, clientes) | **React Query**     | Cache automático, revalidação em foco, retry de queries |
| Estado da UI (modo especialista)    | **Zustand**         | Simples, sem boilerplate, persiste em `sessionStorage`  |
| Formulários complexos               | **React Hook Form** | Performance, validação nativa, integração com Zod       |

**Regras obrigatórias:**
- `ErrorBoundary` em todos os painéis de dashboard
- Skeletons de loading em todos os componentes de leitura assíncrona (CLS = 0)
- Lógica de negócio proibida no Frontend — mover para Service Java ou Stored Procedure

---

---

### 4.7 Anti-Patterns — O Que Nunca Fazer

> [!CAUTION]
> Os padrões abaixo são **motivo de rejeição de PR** imediata.

| ❌ Anti-Pattern                                     | ✅ Alternativa Correta                                       | ADR Violado |
|----------------------------------------------------|-------------------------------------------------------------|-------------|
| `repository.save()` em entidades bitemporais       | `CALL sp_*` via `EntityManager.createNativeQuery()`         | ADR-04      |
| Injetar repositório de outro módulo                | `ApplicationEventPublisher` + listener no módulo alvo       | ADR-01      |
| H2 em testes de integração com Procedures          | `@Testcontainers` com `postgres:15-alpine`                  | ADR-06      |
| Logar CPF / e-mail em texto claro                  | `@Masked` + hash SHA-256 para correlação                    | ADR-05      |
| Credenciais hardcoded em `application.properties`  | Variáveis de ambiente injetadas via Vault/CI                | ADR-05      |
| `Thread.sleep()` em testes de concorrência         | `CountDownLatch` ou `CompletableFuture.allOf()`             | —           |
| Queries de listagem com `OFFSET` em tabelas grandes| Cursor-based: `WHERE id > :cursor LIMIT n`                  | RP-03       |
| Lógica de negócio no Frontend (React)              | Mover para Service Java ou Stored Procedure                 | ADR-01      |
| Event listeners síncronos bloqueantes              | `@Async` + `@TransactionalEventListener(AFTER_COMMIT)`      | ADR-07      |

---

---

## 📡 API e Integrações

A camada de API do SincronizaMEI é o **guardião da consistência** do ecossistema. Cada decisão de design nessa camada existe para garantir que nenhuma transação seja perdida, duplicada ou corrompida — mesmo diante de infraestrutura não-confiável.

### 8.1 Protocolo de Resiliência e Status Codes

| Status | Semântica | Quando usar |
|---|---|---|
| `HTTP 201 Created` | Recurso persistido de forma síncrona e confirmada | Operações que completam em < 800ms dentro da mesma transação JDBC |
| `HTTP 202 Accepted` | Operação aceita, enfileirada no RabbitMQ, resultado assíncrono | Faturamento, reconciliação — qualquer operação que depende de gateway externo |
| `HTTP 400 Bad Request` | Erro de validação de entrada — jamais chega à camada de serviço | Header obrigatório ausente, body malformado, constraint violada no DTO |
| `HTTP 409 Conflict` | Violação de idempotência — operação já processada dentro da janela TTL | `X-Idempotency-Key` já existe no Redis — body contém a resposta original |
| `HTTP 422 Unprocessable Entity` | Dados semanticamente inválidos — estrutura OK, negócio rejeita | Saldo insuficiente, taxa de câmbio ausente, status de cliente inativo |
| `HTTP 429 Too Many Requests` | Rate limiting ativo — cabeçalho `Retry-After` presente | Proteção do core ERP contra burst de um único cliente/integração |
| `HTTP 503 Service Unavailable` | Circuit Breaker aberto para o gateway requisitado | Headers `X-Circuit-State: OPEN` e `X-Retry-After: {seconds}` presentes |

> [!IMPORTANT]
> **Sobre HTTP 202:** Quando o sistema retorna `202 Accepted`, ele *garante* que processará a operação — não que já processou. O cliente deve usar o `Location` header retornado para polling de status, ou subscrever ao SSE endpoint `/api/v1/ordens/{id}/events` para notificação push quando o estado mudar.

### 8.2 Headers Obrigatórios e Observabilidade End-to-End

| Header | Tipo | Valor | Finalidade |
|---|---|---|---|
| `X-Idempotency-Key` | **Obrigatório** | UUID v4 gerado pelo cliente | Previne dupla cobrança. Ausência → `HTTP 400` antes de atingir qualquer serviço |
| `X-Correlation-ID` | Recomendado | UUID v4 de sessão do usuário | Vincula logs do React, Spring Boot, RabbitMQ consumer e PostgreSQL em um único trace no Kibana/Jaeger. Se ausente, gerado pelo servidor |
| `X-Signature` | Obrigatório para webhooks inbound | `HMAC-SHA256(body, secret)` | Valida autenticidade e integridade de callbacks de gateway. Replay > 5 min → `HTTP 401` |
| `Authorization` | Obrigatório | `Bearer {JWT}` | JWT com claims de perfil (`MEI` vs `CONTROLLER`) para autorização de endpoints de auditoria |
| `Idempotency-Key-Expiry` | Opcional | Segundos (default: 86400) | Override da janela de TTL para operações que precisam de proteção mais curta ou mais longa |

### 8.3 Exemplo Completo — Faturamento Idempotente

**Request:**
```http
POST /api/v1/faturamento/ordens HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9...
X-Idempotency-Key: 7f3e9b2c-4a1d-4e8f-b7c2-1a9d3e5f7b2c
X-Correlation-ID: session-abc123-req-001
Content-Type: application/json

{
  "clienteId": "cli_abc123",
  "moeda": "BRL",
  "itens": [
    { "produtoId": "prod_xyz", "quantidade": 2, "valorUnitario": 49.90 }
  ],
  "meioDePagamento": "PIX",
  "callbackUrl": "https://webhook.meu-sistema.com/pagamento"
}
```

**Response (primeira chamada):**
```http
HTTP/1.1 202 Accepted
Location: /api/v1/faturamento/ordens/ord_789xyz
X-Correlation-ID: session-abc123-req-001
Content-Type: application/json

{
  "ordemId": "ord_789xyz",
  "status": "PROCESSAMENTO_PENDENTE",
  "idempotencyKey": "7f3e9b2c-4a1d-4e8f-b7c2-1a9d3e5f7b2c",
  "estimatedConciliationAt": "2026-04-16T15:30:00Z",
  "_links": {
    "self": { "href": "/api/v1/faturamento/ordens/ord_789xyz" },
    "events": { "href": "/api/v1/faturamento/ordens/ord_789xyz/events" },
    "audit": { "href": "/api/v1/auditoria/ordens/ord_789xyz" }
  }
}
```

**Response (chamada duplicada com mesma X-Idempotency-Key):**
```http
HTTP/1.1 409 Conflict
X-Idempotency-Original-Request-At: 2026-04-16T15:15:00Z
Content-Type: application/json

{
  "ordemId": "ord_789xyz",
  "status": "PROCESSAMENTO_PENDENTE",
  "message": "Operação já registrada. Retornando resultado original.",
  "idempotencyKey": "7f3e9b2c-4a1d-4e8f-b7c2-1a9d3e5f7b2c"
}
```

### 8.4 Exemplo de Controller — Java (Spring Boot 3 / Java 21)

```java
// api/controllers/FaturamentoController.java
`

## 7. 🔌 API e Integracoes

O SincronizaMEI opera sob uma filosofia **API-First**, onde o contrato e definido antes da implementacao. Nossa API segue padrões bancarios de resiliencia e seguranca.

### 7.1 Protocolo de Cabecalhos e Rastreabilidade

| Header | Obrigatorio | Funcao | Lifecycle |
| :--- | :--- | :--- | :--- |
| `X-Idempotency-Key` | Sim (POST/PUT) | Previne duplicidade de transacoes | Redis (TTL 24h) |
| `X-Correlation-ID` | Sim (Opcional) | Rastreio distribuido Cross-Stack | MDC → RabbitMQ → Logs |
| `Accept-Version` | Sim | Versionamento de contrato (Media-Type) | v1 (Default) |

### 7.2 Estandardizacao de Erros (RFC 7807)

Todas as falhas da API seguem o padrao `application/problem+json`, garantindo que o erro seja autoexplicativo:

```json
{
  "type": "https://sincronizamei.io/problems/idempotency-conflict",
  "title": "Chave de Idempotencia em Uso",
  "status": 409,
  "detail": "Esta operacao ja foi processada com sucesso anteriormente.",
  "instance": "/api/v1/faturamento/ordens/7f3e9b2c",
  "correlationId": "abc-123-xyz"
}
```

### 7.3 Integracoes e Anti-Corruption Layer (ACL)

Isolamos o dominio de negocio de APIs externas (Gateways, SEFAZ, etc.) atraves de Adapters e Circuit Breakers:

```java
@Component
public class GatewayPagamentoAdapter implements GatewayPagamentoPort {
    @Retry(name = "gateway", fallbackMethod = "queueForReconciliation")
    @CircuitBreaker(name = "gateway")
    public GatewayResponseDTO enviar(OrdemGatewayDTO dto) {
        return webClient.post().uri("/v1/payments").bodyValue(dto).retrieve().bodyToMono(GatewayResponseDTO.class).block();
    }
}
```

### 7.4 Ciclo de Vida de Webhooks (Inbound)

1. **Validacao de Assinatura**: Uso de HMAC-SHA256 para garantir autenticidade.
2. **Persistence First**: O evento e salvo em banco antes de qualquer processamento.
3. **Idempotencia**: O ID do evento externo e usado como chave para evitar processamento duplo.

---

## 11. 🐳 Implantacao (Deploy)

O SincronizaMEI adota **Entrega Contínua com Zero Downtime** como requisito não-negociável. O núcleo financeiro nunca pode ficar indisponível durante atualizações.

### 9.1 Estratégia Blue-Green com Traffic Switch Controlado

```
Ambiente Blue (produção atual):     versão v1.1.0, tráfego 100%
Ambiente Green (nova versão):       versão v1.2.0, tráfego 0%

Pipeline de promoção:
  1. Deploy no Green (sem tráfego)
  2. Flyway aplica migrations em Green (retrocompatíveis com Blue)
  3. Readiness Probes no Green: DB ✓, Redis ✓, RabbitMQ ✓, Flyway ✓
  4. Smoke tests k6 no Green (5 min, sem tráfego real)
  5. Traffic Switch: 5% Blue → Green (canary, 10 min de observação)
  6. Se p95 < 800ms e error rate < 0.1%: 100% para Green
  7. Blue fica de standby por 30 min (rollback imediato se necessário)
```

**Regra de compatibilidade de migrations:**
As migrations Flyway devem ser **retrocompatíveis** — o Green (nova versão do Java) e o Blue (versão anterior) precisam funcionar com o mesmo schema durante a janela de transição. Isso significa:
- Adicionar colunas `NULLABLE` ou com `DEFAULT` (compatível com Blue).
- **Nunca** fazer `ALTER COLUMN ... SET NOT NULL` sem o padrão expand-contract.
- **Nunca** fazer `DROP COLUMN` em migrations de release — apenas em sprints subsequentes após validação.

### 9.2 Pipeline de CI/CD — Quality Gates Detalhados

```yaml
# .github/workflows/ci.yml (simplificado)
jobs:
  quality-gate:
    steps:
      - name: "1. Build & Compile"
        run: ./mvnw compile -DskipTests

      - name: "2. Unit Tests + Coverage Gate"
        run: ./mvnw test
        # Falha se cobertura < 90% (JaCoCo) ou < 95% em pacotes críticos

      - name: "3. Integration Tests (Testcontainers)"
        run: ./mvnw verify -Dspring.profiles.active=test
        # Sobe PostgreSQL 16 + RabbitMQ 3.13 reais via Docker

      - name: "4. Architecture Tests (ArchUnit)"
        run: ./mvnw test -pl backend -Dtest=ModuleBoundaryTest
        # Falha se módulo financeiro acessar repositório de estoque diretamente

      - name: "5. SAST + CVE Scan"
        run: |
          trivy fs --severity HIGH,CRITICAL --exit-code 1 .
          ./mvnw org.owasp:dependency-check-maven:check
        # Zero vulnerabilidades críticas ou altas permitidas

      - name: "6. Secret Scan"
        run: trufflehog git file://. --since-commit HEAD~1 --fail

      - name: "7. Flyway Validation"
        run: ./mvnw flyway:validate -Dflyway.url=$STAGING_DB_URL
        # Valida checksums contra staging — nenhuma migration alterada após merge

      - name: "8. Performance Smoke Test"
        run: k6 run scripts/k6/smoke-test.js --vus 50 --duration 60s
        # Falha se p95 > 800ms ou error rate > 0.5%

      - name: "9. Docker Build (multi-stage)"
        run: docker build -t sincronizamei:$GITHUB_SHA .
        # Imagem final < 200MB (apenas JRE, sem JDK)
```

### 9.3 Infraestrutura como Código (Terraform da AWS)

> [!NOTE]
> Para toda a modelagem de Cloud e IAC, a **Amazon Web Services (AWS)** foi definida como provedor base. Os módulos implementados utilizam a infraestrutura VPC, RDS, ElastiCache e Load Balancers do ecossistema da AWS padrão.

```hcl
# terraform/modules/ecs-service/main.tf (esquema)
resource "aws_ecs_service" "sincronizamei" {
  name            = "sincronizamei-${var.environment}"
  desired_count   = var.min_instances

  deployment_circuit_breaker {
    enable   = true
    rollback = true  # Rollback automático se novo deploy falha healthcheck
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.blue.arn  # Inicializa no Blue
  }
}

# Graceful Shutdown: 30s para o Spring Boot drenar filas do RabbitMQ
resource "aws_ecs_task_definition" "sincronizamei" {
  stop_timeout = 30
  # ...
}
```

### 9.4 Variáveis de Ambiente — Classificação por Sensibilidade

| Variável | Descrição | Fonte | Sensibilidade |
|---|---|---|---|
| `DATABASE_URL` | String de conexão JDBC PostgreSQL | Vault / IAM Role (RDS IAM Auth) | 🔴 Crítico |
| `RABBITMQ_URL` | Endpoint do broker AMQP | AWS Secrets Manager | 🔴 Crítico |
| `AES_SECRET_KEY` | Chave de encriptação PII (LGPD) | Vault KMS — rotacionada a cada 90 dias | 🔴 Crítico |
| `JWT_PUBLIC_KEY` | Chave pública RSA para validação de JWT | Vault — rotacionada a cada 30 dias | 🟠 Alto |
| `GATEWAY_HMAC_SECRET` | Segredo para validação de callbacks | AWS Secrets Manager por gateway | 🟠 Alto |
| `IDEMPOTENCY_TTL` | Janela de idempotência (default: 86400s) | Config Map / Environment | 🟡 Médio |
| `RECONCILIATION_INTERVAL_MINUTES` | Frequência do Worker (default: 15) | Config Map | 🟡 Médio |
| `CIRCUIT_BREAKER_FAILURE_THRESHOLD` | % de falhas para abrir o circuit (default: 50) | Config Map | 🟡 Médio |

> [!WARNING]
> **Nenhuma dessas variáveis deve aparecer em logs, stack traces ou responses de erro.** O `MaskedLoggingFilter` e o handler global de exceções filtram automaticamente variáveis de ambiente conhecidas. Para variáveis customizadas, adicione o prefixo `SENSITIVE_` para ativar o filtro automático.

---

## 6. 🔒 Seguranca e Observabilidade

### 10.1 Pilares de Segurança (Security by Design)

**Encriptação At-Rest — PII:**
```java
// Coluna CPF encriptada com AES-256-GCM + IV único por registro
// O hash SHA-256 permite correlação em logs sem expor o dado real
@Column(name = "cpf_encrypted")
@Convert(converter = AesGcmEncryptedConverter.class)
private String cpf;

@Column(name = "cpf_hash")   // SHA-256(cpf) — usado para correlação de logs
private String cpfHash;

@Masked(strategy = MaskingStrategy.CPF)  // Log: "***.***.123-**"
public String getCpf() { return cpf; }
```

**Prevenção de SQL Injection — Múltiplas Camadas:**
1. **Prepared Statements obrigatórios** via JPA/Hibernate — nenhuma string interpolada em queries.
2. **Stored Procedures** para lógica sensível — parâmetros são sempre tipados no PostgreSQL.
3. **ArchUnit test** que falha o build se qualquer método usa `createNativeQuery` com concatenação de string.

**Validação de Webhooks Inbound (HMAC-SHA256):**
```java
// Previne ataques de replay e callbacks forjados
@Component
public class WebhookSignatureValidator {
    public void validate(String payload, String signature, String timestamp) {
        // Rejeita se timestamp > 5 minutos (previne replay attacks)
        if (Instant.now().minusSeconds(300).isAfter(Instant.ofEpochSecond(Long.parseLong(timestamp)))) {
            throw new ReplayAttackException("Webhook timestamp expirado");
        }
        String expectedSignature = hmacSha256(gatewaySecret, timestamp + "." + payload);
        if (!MessageDigest.isEqual(expectedSignature.getBytes(), signature.getBytes())) {
            throw new InvalidSignatureException("Assinatura de webhook inválida");
        }
    }
}
```

### 10.2 Observabilidade e Rastreio Distribuído (O11y)

**O objetivo da observabilidade no SincronizaMEI não é debugging post-mortem — é detecção proativa de Drift antes que o usuário perceba.**

**Trace-ID End-to-End:**
```
Browser → React (X-Correlation-ID: abc123)
  → Spring Boot Controller (MDC: correlationId=abc123)
    → RabbitMQ message headers (correlationId: abc123)
      → Worker Consumer (MDC: correlationId=abc123)
        → PostgreSQL (SET app.correlation_id = 'abc123')
          → Kibana/Jaeger: trace completo por correlationId
```

**Métricas de Negócio (Prometheus):**
```java
// Métricas que importam para o produto — não apenas infra
@Component
public class ReconciliacaoMetrics {

    private final Gauge ordemLimboGauge;
    private final Counter divergenciaDetectada;
    private final Histogram tempoReconciliacao;

    // Alertas automáticos:
    // ordens_em_limbo_ratio > 0.001 → Slack alert para #ops
    // divergencia_detectada_total rate > 5/min → PagerDuty P2
    // reconciliacao_tempo_p95 > 900s → PagerDuty P1 (SLA em risco)
}
```

**Dashboard Grafana — Visão de Saúde Financeira:**
```
┌─────────────────────────────────────────────────────────────┐
│ SincronizaMEI — Financial Health Dashboard                  │
├─────────────────────┬───────────────────────────────────────┤
│ Ordens em Limbo     │ ████░░░░░░ 0.03% (meta: < 0.1%)      │
│ DLQ Depth           │ 0 mensagens                           │
│ Latência p95        │ 423ms (meta: < 800ms) ✓               │
│ Circuit Breakers    │ Gateway PIX: CLOSED ✓                 │
│                     │ Gateway Cartão: CLOSED ✓              │
│ Última Reconciliação│ há 3 min (próxima: 12 min)            │
│ Uptime              │ 99.97% (30 dias)                      │
└─────────────────────┴───────────────────────────────────────┘
```

### 10.3 Auditoria Imutável — Garantias Técnicas

O modelo bitemporal não é apenas uma feature — é uma **garantia arquitetural** que transforma auditoria de uma atividade reativa em uma propriedade passiva do sistema.

```sql
-- Consulta de auditoria: "O que o sistema sabia sobre a ordem X em 01/Jan/2026?"
-- Resposta baseada no conhecimento que o sistema tinha naquela data
SELECT *
FROM financeiro.ordens
WHERE id = 'ord-abc123'
  -- Tempo de Validade: quando o evento ocorreu
  AND valid_from <= '2026-01-01'::timestamptz
  AND valid_to > '2026-01-01'::timestamptz
  -- Tempo de Sistema: o que o ERP sabia naquela data
  AND system_init_tstz <= '2026-01-01'::timestamptz
  AND system_end_tstz > '2026-01-01'::timestamptz;

-- Trigger que previne DELETE físico (última linha de defesa):
CREATE OR REPLACE FUNCTION trg_prevent_delete_fn() RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION
        'DELETE físico proibido na tabela %. Use soft-delete bitemporal via sp_reconciliar_ordem. Registro: %',
        TG_TABLE_NAME, OLD.id;
END;
$$ LANGUAGE plpgsql;
```

---

### 6.2 Responsible Disclosure

> [!CAUTION]
> **Não abra Issue pública** para vulnerabilidades. Isso expõe usuários antes que a correção esteja disponível.

**Processo:**
1. E-mail para `security@sincronizamei.com.br` com assunto `[SECURITY] Descrição`
2. Inclua: descrição, impacto, passos de reprodução (PoC), versão afetada, sugestão de fix
3. Aguarde: confirmação em 48h · avaliação em 5 dias úteis · plano de correção em 10 dias úteis

**SLA de Resposta por CVSS:**

| Severidade                 | Prazo de Patch     |
|----------------------------|--------------------|
| Crítica (CVSS ≥ 9.0)       | 72 horas           |
| Alta (CVSS 7.0–8.9)        | 30 dias            |
| Média (CVSS 4.0–6.9)       | Próximo release    |

**Escopo do programa:**
- ✅ SQLi em endpoints ou Stored Procedures
- ✅ Bypass de idempotência (timing attack → dupla cobrança)
- ✅ Exposição de PII em logs, API ou erros
- ✅ Race conditions que comprometem integridade financeira
- ❌ DoS volumétrico · Engenharia social · CVEs públicos sem exploração ativa

---

---

## 8. ⚙️ Customizacoes e Extensibilidade

O SincronizaMEI é projetado para **evolução controlada** — parceiros e clientes podem estender o comportamento do sistema sem acesso ao código de domínio e sem risco de regressão no Core ERP.

### Arquitetura de Plugins — Contrato Formal

Todo plugin deve implementar a interface `Hook<T>`, que define não apenas o comportamento principal mas também a estratégia de recuperação de falhas e o identificador para rastreamento:

```typescript
// plugins/types.ts — Contrato obrigatório para todos os plugins
export interface Hook<T extends DomainEvent> {
  readonly name: string;              // Identificador único para logs e DLQ
  readonly version: string;           // Semver — para compatibilidade de contrato
  execute(event: T): Promise<void>;   // Lógica principal
  onError(error: HookError): Promise<void>;  // Obrigatório — sem esta, registro falha no startup
  onTimeout(): Promise<void>;         // Chamado se execute() exceder 5s
}

// Exemplo de implementação:
// plugins/integracao-contabilidade.plugin.ts
export const integracaoContabilidade: Hook<OrdemConciliadaEvent> = {
  name: 'integracao-contabilidade-v1',
  version: '1.2.0',

  async execute(evento: OrdemConciliadaEvent): Promise<void> {
    await contabilidadeApiClient.lancar({
      ordemId: evento.id,
      valor: evento.valorFinal,
      contaDebito: evento.contaContabil.debito,
      contaCredito: evento.contaContabil.credito,
      dataCompetencia: evento.validFrom,
      correlationId: evento.correlationId,   // Propaga rastreabilidade
    });
  },

  async onError(error: HookError): Promise<void> {
    // Estratégia de fallback: enfileira para reprocessamento manual
    await dlqService.enfileirar({ hookName: this.name, payload: error.originalEvent });
  },

  async onTimeout(): Promise<void> {
    await alertingService.warn(`Hook ${this.name} excedeu timeout de 5s`);
  },
};

// Registro no bootstrap do módulo
HookRegistry.on('ordem.conciliada', integracaoContabilidade);
```

### Camadas de Customização por Complexidade

| Camada | Mecanismo | Caso de Uso | Risco Colateral |
|---|---|---|---|
| **Hook de Domínio** | `HookRegistry` + interface `Hook<T>` | Notificar ERP legado, lançar em contabilidade, enviar NF-e | Zero — executado em thread pool isolada com timeout |
| **Stored Procedure Customizada** | Rotinas SQL em `db/procedures/custom/` chamadas via `HookRegistry` com adapter JDBC | Cálculo fiscal específico por regime tributário (Simples, Lucro Presumido) | Baixo — procedure separada, sem acesso a tabelas core diretamente |
| **Módulo de Integração Java** | Sub-projeto em `integration-service/` com Spring Boot | Integração completa com ERP legado via SOAP, EDI ou OAuth2 com estado próprio | Médio — módulo separado com deploy independente |

> [!NOTE]
> **Processo de onboarding de plugin:** Todo plugin novo deve passar por code review de segurança (verificação de acesso indevido a recursos externos, ausência de hardcoded credentials, implementação correta de `onError`) antes de ser registrado em staging. O `HookRegistry` emite log de auditoria no startup listando todos os hooks registrados com sua versão.

---

## 12. 🐛 Processo de Debug e Suporte Tecnico

### Fluxo de Triagem Completo

```
Incidente Reportado
  → Classificação de Severidade (SLA: 30 min)
    → P1: Eng. Plantão acionado imediatamente
    → P2/P3: Triagem pelo time em horário comercial
  → Reprodução em dev com Testcontainers (SLA: 2h para P1)
  → Root Cause Analysis com correlationId no Kibana
    → Trace completo: React → Spring → RabbitMQ → PostgreSQL
  → Fix com TDD (teste que reproduz o bug vem primeiro)
  → PR com referência ao incidente + postmortem para P1
  → Deploy com Quality Gates obrigatórios
  → Confirmação de resolução com cliente afetado
```

### Ferramentas de Diagnóstico por Camada

| Camada | Ferramenta | Comando / Query | O que procurar |
|---|---|---|---|
| **Logs correlacionados** | Kibana / Loki | `correlationId: "abc123"` | Trace completo do request, ponto de falha |
| **Performance de queries** | PostgreSQL `EXPLAIN ANALYZE` | Ver query abaixo | Sequential scans, missing indexes, lock waits |
| **Replay de mensagens** | RabbitMQ Management UI | Filas → DLQ → Get Messages | Mensagens envenenadas, reason de rejeição |
| **Estado em tempo passado** | `fn_check_integrity()` | Ver query abaixo | Histórico de estados, tempo em limbo |
| **Circuit Breaker** | Spring Actuator | `GET /actuator/circuitbreakers` | Estado por gateway, taxa de erro, próxima tentativa |
| **Idempotência** | Redis CLI | `GET idempotency:{key}` | TTL restante, resposta cacheada |
| **Health completo** | Spring Actuator | `GET /actuator/health` | Latência por componente, pending migrations |

### Queries de Diagnóstico Essenciais

```sql
-- 1. Transações em Limbo há mais de 30 minutos (diagnóstico de Drift)
SELECT
    o.id,
    o.status,
    o.idempotency_key,
    o.valid_from,
    EXTRACT(EPOCH FROM (NOW() - o.valid_from)) / 60 AS minutos_em_limbo,
    o.gateway_usado,
    o.valor_esperado,
    o.correlation_id
FROM financeiro.ordens o
WHERE o.status = 'PROCESSAMENTO_PENDENTE'
  AND o.valid_to = 'infinity'::timestamptz
  AND o.valid_from < NOW() - INTERVAL '30 minutes'
ORDER BY o.valid_from ASC;
-- Esperado: 0 linhas em sistema saudável

-- 2. Diagnóstico completo de uma ordem específica (todas as versões históricas)
SELECT * FROM fn_check_integrity('7f3e9b2c-4a1d-4e8f-b7c2-1a9d3e5f7b2c');
-- Retorna: todas as versões com timestamps, estados, divergências e responsável por cada alteração

-- 3. Identificar queries lentas (p95 > 1s nos últimos 10 minutos)
SELECT
    query,
    calls,
    mean_exec_time,
    stddev_exec_time,
    total_exec_time,
    rows
FROM pg_stat_statements
WHERE mean_exec_time > 1000
  AND calls > 10
ORDER BY mean_exec_time DESC
LIMIT 20;
-- Requer extensão pg_stat_statements habilitada (disponível no docker-compose.dev.yml)

-- 4. Verificar consistência do modelo bitemporal (detecta sobreposição de versões)
-- Deveria retornar 0 linhas. Qualquer linha indica bug na Stored Procedure.
SELECT a.id, a.valid_from, a.valid_to, b.valid_from, b.valid_to
FROM financeiro.ordens a
JOIN financeiro.ordens b ON a.id = b.id AND a.ctid <> b.ctid
WHERE tstzrange(a.valid_from, a.valid_to) && tstzrange(b.valid_from, b.valid_to)
  AND a.valid_to = 'infinity'::timestamptz
  AND b.valid_to = 'infinity'::timestamptz;
```

### SLAs de Suporte e Processo de Escalada

| Severidade | Critério de Classificação | SLA Resposta | SLA Resolução | Escalada Automática |
|---|---|---|---|---|
| **P1 — Crítico** | Divergência financeira > R$ 10,00 confirmada OU sistema completamente indisponível OU vazamento de PII | 1 hora (24/7) | 4 horas | PagerDuty → Eng. Plantão → CTO em 2h sem resolução |
| **P2 — Alto** | Reconciliação travada > 1h OU bug de dados sem impacto financeiro confirmado OU DLQ > threshold | 4 horas (horário comercial) | 1 dia útil | Slack #incidents → Tech Lead |
| **P3 — Médio** | Bug de usabilidade OU relatório com dado incorreto sem impacto financeiro | 1 dia útil | 3 dias úteis | Jira → Sprint seguinte |
| **P4 — Baixo** | Melhoria de UX OU inconsistência de documentação | 3 dias úteis | Próximo ciclo de planejamento | Backlog |

> **Postmortem obrigatório para P1:** Todo incidente P1 encerrado deve ter um documento de postmortem publicado em `docs/postmortems/` dentro de 48h, contendo: timeline do incidente, root cause analysis, ações de remediação implementadas e ações preventivas para evitar recorrência.

---

### 7.2 Runbook — Recuperação de Drift

> **Severidade:** P1 / P2 · **Tempo estimado:** 15–60 min
> **Gatilho:** Ordem em `PROCESSAMENTO_PENDENTE` há mais de 30 minutos.

**1. Diagnóstico:**

```sql
-- Ordens em limbo
SELECT * FROM financeiro.fn_check_integrity_bulk() WHERE em_limbo = TRUE ORDER BY minutos_limbo DESC;

-- Ordem específica
SELECT * FROM financeiro.fn_check_integrity('<idempotency_key>');
```

```bash
# Saúde do gateway via /health
curl -s https://api.sincronizamei.com.br/health | jq '.checks.gateway'

# DLQ: acessar RabbitMQ Management UI → Queues → financeiro.reconciliacao.dlq
```

**2. Análise de Causa Raiz:**

| Sintoma                                 | Causa Provável                    | Ação                         |
|-----------------------------------------|-----------------------------------|------------------------------|
| Circuit Breaker OPEN no gateway         | Instabilidade do parceiro externo | Aguardar recovery automático |
| Mensagens na DLQ sem retry ativo        | Worker parado                     | Verificar logs do worker     |
| Ordem sem registro em fila ou DLQ       | Bug de consumer específico        | Acionar dev on-call          |

**3. Recuperação:**

- **Cenário A — Gateway recuperado, worker próximo ciclo:** aguardar 15 min ou forçar via:
  ```bash
  curl -X POST https://api.sincronizamei.com.br/admin/jobs/reconciliacao/trigger \
    -H "Authorization: Bearer $ADMIN_TOKEN" -H "X-Idempotency-Key: $(uuidgen)"
  ```
- **Cenário B — Mensagens na DLQ:** ver seção 7.3
- **Cenário C — `DIVERGENTE_AUDITORIA`:** não alterar o banco manualmente; acionar Controller para aprovação via UI de Auditoria

**4. Validação:**

```sql
SELECT COUNT(*) FROM financeiro.ordens
WHERE status = 'PROCESSAMENTO_PENDENTE' AND valid_to = 'infinity'
  AND valid_from < NOW() - INTERVAL '30 minutes';
-- Resultado esperado: 0
```

---

### 7.3 Runbook — Replay de Dead Letter Queue

> **Severidade:** P2 · **Tempo estimado:** 20–45 min
> **Gatilho:** DLQ com > 100 mensagens ou ordens em limbo com falha de processamento confirmada.

> [!CAUTION]
> **Nunca faça replay em massa sem identificar a causa raiz.** Reprocessar dados corrompidos pode gerar duplicidade financeira.

**1. Inspecionar sem consumir:**

```bash
curl -s -u $RABBIT_USER:$RABBIT_PASS \
  -X POST "http://rabbit.sincronizamei.com.br:15672/api/queues/%2F/financeiro.reconciliacao.dlq/get" \
  -H "Content-Type: application/json" \
  -d '{"count": 5, "ackmode": "ack_requeue_true", "encoding": "auto"}' \
  | jq '.[].payload | fromjson'
```

**2. Classificar:**

| Tipo de Erro              | Ação                              |
|---------------------------|-----------------------------------|
| `GatewayTimeoutException` | Gateway indisponível → reprocessar|
| `DuplicateKeyException`   | Já processado → descartar         |
| `JsonParseException`      | Corrompido → descartar + escalar  |
| `lock_not_available`      | Concorrência resolvida → reprocessar |

**3. Replay Seletivo (recomendado):**

```bash
curl -X POST https://api.sincronizamei.com.br/admin/dlq/replay \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "X-Idempotency-Key: $(uuidgen)" \
  -d '{"queue":"financeiro.reconciliacao.dlq","filter":{"erroTipo":"GatewayTimeoutException"},
       "targetQueue":"financeiro.reconciliacao","maxMessages":50,"dryRun":true}'
# dryRun:true → simula. Confirmar e repetir com dryRun:false
```

**4. Descarte Seguro (dados corrompidos):**

```bash
# 1. Exportar backup antes de purgar
curl ... -d '{"count":10000,"ackmode":"ack_requeue_false","encoding":"auto"}' \
  > /tmp/dlq_backup_$(date +%Y%m%d_%H%M%S).json

# 2. Confirmar backup e documentar justificativa no log de incidentes
```

---

### 7.4 Runbook — Hotfix de Stored Procedure sem Downtime

> **Severidade:** P1 / P2 · **Tempo estimado:** 30–90 min
> **Aplicável para:** Stored Procedures e funções SQL. **Não aplicável** para alterações de schema DDL.

**1. Pré-Análise (obrigatória antes de qualquer mudança):**

```sql
-- Verificar versão atual da procedure
SELECT prosrc FROM pg_proc WHERE proname = 'sp_reconciliar_ordem'
  AND pronamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'financeiro');

-- Quantificar impacto em produção
SELECT COUNT(*) FROM financeiro.ordens WHERE status = 'CONCILIADO'
  AND valid_from > NOW() - INTERVAL '24 hours'
  AND ABS(valor_total - 0) > 0.50; -- ajustar conforme o bug
```

**2. Desenvolvimento:**

```bash
git checkout main && git pull
git checkout -b hotfix/SMEI-{ID}-{descricao}
```

- Editar `src/main/resources/db/procedures/sp_reconciliar_ordem.sql` com `CREATE OR REPLACE`
- Criar migration de registro: `V{timestamp}__hotfix_sp_{descricao}.sql`
- Escrever teste de regressão (JUnit + Testcontainers) que reproduz o bug e valida o fix

**3. Aplicar em Staging (sem restart do servidor Java):**

```bash
# CREATE OR REPLACE é atômico no PostgreSQL — seguro com Java rodando
PGPASSWORD=$STAGING_DB_PASS psql -h staging-db.sincronizamei.com.br -U sincronizamei_app \
  -d sincronizamei -f src/main/resources/db/procedures/sp_reconciliar_ordem.sql

# Validar
./mvnw test -pl backend -Dtest="ReconciliacaoIntegrationTest" -Dspring.profiles.active=staging
```

**4. Aplicar em Produção:**

```bash
# Preferir pipeline CI/CD. Se urgente, aplicar manualmente:
PGPASSWORD=$PROD_DB_PASS psql -h prod-db.sincronizamei.com.br -U sincronizamei_app \
  -d sincronizamei -f src/main/resources/db/procedures/sp_reconciliar_ordem.sql
# Não requer restart do Java — próximas chamadas já usam a versão corrigida
```

**5. Documentar pós-hotfix:**
- Fechar Issue com link para PR e este runbook
- Registrar em `docs/incidents/YYYY-MM-DD-hotfix-{descricao}.md`
- Atualizar `CHANGELOG.md` com entrada em `Corrigido`

---

---

## 13. 🔄 Melhoria Continua (20 Frentes)

O SincronizaMEI opera sob um modelo de **Qualidade como Propriedade Emergente** — não como fase de projeto. A qualidade não é adicionada no final; ela emerge de práticas consistentes aplicadas em cada ciclo de desenvolvimento.

### 13.1 As 20 Frentes de Melhoria Estratégica

1. **Chaos Engineering Automático:** Injeção periódica de falhas (Pumba + Toxiproxy) em ambiente de staging para validar autorrecuperação do RabbitMQ, tolerância a latência de banco e resiliência do Circuit Breaker — com resultados publicados automaticamente no canal `#chaos-results`.

2. **Detecção de Drift Preditiva:** Modelo ML simples (regressão logística) treinado sobre padrões históricos de limbo para prever transações com alta probabilidade de divergência *antes* do timeout de 15 min — permitindo intervenção proativa.

3. **Otimização Contínua de Índices:** Analisador automático de `pg_stat_statements` que detecta queries com degradação de performance e abre issues automáticas com sugestões de índice geradas via `pg_recommend_indexes`.

4. **Automação de Versionamento Semântico:** CI gera automaticamente a versão seguinte (major/minor/patch) baseado no padrão de Conventional Commits, cria CHANGELOG e tagueia o release sem intervenção manual.

5. **Feature Flags Dinâmicas (OpenFeature):** Rollout progressivo de novas regras fiscais, novos gateways e mudanças de UX sem redeploy, com toggle por CNPJ/tenant para validação A/B controlada.

6. **Política Centralizada de Anonimização:** Pipeline automático de criação de dumps de staging com `sp_anonimizar_titular` aplicado — staging pode usar volume de dados reais sem risco de exposição de PII.

7. **Auto-scaling Baseado em Profundidade de Fila:** HPA (Horizontal Pod Autoscaler) configura réplicas adicionais do Worker quando a fila `reconciliacao.main` excede N mensagens, com scale-down gradual após normalização.

8. **Vulnerability Scanning Diário (Supply Chain):** Trivy + Snyk varrem dependências Maven e NPM diariamente. Vulnerabilidades críticas abrem issues automáticas e bloqueiam o próximo deploy via GitHub Environments.

9. **Doc-as-Code (OpenAPI Sincronizado):** `mvnw springdoc:generate` gera o `openapi.json` a partir das anotações do código. O CI valida que o arquivo commitado está sincronizado — sem documentação desatualizada em `main`.

10. **UX Feedback Loop Quantitativo:** Coleta de eventos de UX (cliques, abandonos, tempo em tela) via analytics self-hosted (Plausible) para identificar pontos de fricção na interface MEI e priorizá-los no backlog.

11. **Benchmarking de Latência com Regressão Automática:** Comparação automática de p95/p99 entre a versão atual e a anterior. Regressão > 20% bloqueia o merge com relatório de comparação.

12. **Suíte de Carga Pré-Release Obrigatória:** k6 Cloud executa suíte de carga completa (stress + spike + soak) antes de qualquer release para produção. Merge bloqueado se p95 > 800ms ou error rate > 0.1%.

13. **Hotfix Workflow para Stored Procedures:** Deploy seguro de procedures críticas via Flyway em modo "repair" com window de manutenção de 30s e rollback automático se a nova procedure falhar no smoke test pós-deploy.

14. **FinOps Monitoring — Custo por Transação:** Dashboard Grafana que correlaciona custo de infraestrutura (AWS Cost Explorer API) com volume de transações processadas — permite identificar ineficiências antes que se tornem problemas de negócio.

15. **Well-Architected Reviews Trimestrais:** Avaliação formal do sistema contra o AWS/CNCF Well-Architected Framework nos 5 pilares: Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance e Otimização de Custos.

16. **Developer Experience (DevEx) Contínua:** `make dev-setup` completo em < 5 minutos como KPI de DevEx. Onboarding de novos devs cronometrado; runbook de setup atualizado se tempo exceder o alvo.

17. **Regressão Bitemporal Automatizada:** Suite de testes que re-executa consultas históricas conhecidas após cada deploy e verifica que os resultados permanecem idênticos — garantindo que correções não corrompem o histórico.

18. **Detecção de Anomalias de Tráfego API:** Análise de padrões de requisição via OpenTelemetry para identificar uso anômalo de chaves de API, tentativas de força bruta no idempotency endpoint e patterns de scraping.

19. **Code Review Gamificado com Métricas de Qualidade:** Dashboard de engenharia que rastreia: tempo médio de PR em aberto, taxa de revisões solicitadas por PR, cobertura de testes em PRs de feature. Visibilidade, não punição.

20. **Self-Healing Workers com Restart Inteligente:** Monitoramento de consumo de memória dos Workers de Reconciliação via JVM MBeans. Se heap excede 85% após GC ou se thread count anômalo for detectado, worker é reiniciado graciosamente — sem intervenção manual.

---

## 14. 🗺️ Roadmap de Evolucao

Nosso horizonte técnico foca na expansão da inteligência do sistema e na abertura controlada do ecossistema para parceiros.

| Período | Marco | Entregáveis Técnicos | Dependências |
|---|---|---|---|
| **Q2 2026** | Consolidação & Multitenancy | Isolamento por tenant via Row-Level Security no PostgreSQL; suporte nativo a múltiplas moedas (RF-06); App Store SDK público v1.0 | Flyway migration para RLS; tabelas de câmbio diárias |
| **Q3 2026** | Inteligência Operacional | *Reconciliador IA*: modelo de classificação que sugere correções para divergências > R$ 0,50 com ≥ 90% de acurácia; detecção preditiva de drift antes do timeout | Dataset histórico de reconciliações; MLflow para versionamento de modelo |
| **Q4 2026** | Abertura do Ecossistema | **App Store SincronizaMEI**: portal de publicação de plugins com sandbox de testes automáticos, code review de segurança e versionamento de contrato; webhooks outbound configuráveis por evento | HookRegistry v2 com namespacing por parceiro; rate limiting por plugin |
| **Q1 2027** | Observabilidade Avançada | Migração para OpenTelemetry completo (logs, traces, métricas correlacionados); Grafana Tempo para trace storage self-hosted | Infraestrutura de observabilidade no Terraform |
| **2027** | Mobilidade & Operação de Rua | Apps nativos (React Native) para iOS/Android focados no perfil MEI em campo: faturamento offline com sincronização posterior, leitor de NF-e por câmera | Backend offline-first com CRDTs para sincronização; suporte a PWA no frontend atual |

> **Sobre o Roadmap:** Datas e escopo são indicativos. Cada marco tem sua própria Issue de Planning no GitHub com critérios de aceitação detalhados. O critério de promoção de um marco para "Em Desenvolvimento" é: spike técnico concluído, estimativa de esforço validada e riscos arquiteturais mapeados em ADR correspondente.

---

## 15. 🤝 Guia de Contribuicao

Contribuições são bem-vindas — e esperadas ao nível de qualidade que a criticidade financeira do sistema exige. O bar não é alto por burocracia; é alto porque dinheiro de MEIs depende deste código.

**Protocolo obrigatório:**

1. **Issue First:** Toda mudança — seja feature, bug fix ou refactor — deve estar vinculada a uma Issue técnica ou de negócio aberta e discutida *antes* de qualquer código ser escrito. Isso evita trabalho em direções erradas.

2. **TDD é Lei:** Commits sem testes que falham antes da implementação serão rejeitados. O CI verifica que a cobertura não regrediu. Testes escritos após o código para "atingir a meta" são detectados pela ausência do commit "Red" no histórico.

3. **Lint & Análise Estática:** Checkstyle (Java) + PMD + SpotBugs no backend. ESLint + TypeScript strict no frontend. CI bloqueia qualquer violação. Configurações não são negociáveis — PRs que desabilitam regras são fechados.

4. **Conventional Commits:** Use o padrão Angular (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`). O `commitlint` valida no pre-commit hook. Mensagens como "fix bug" ou "update" são rejeitadas automaticamente.

5. **Code Review Rigoroso:** Mínimo de 2 aprovações de engenheiros seniores para merge na `main`. Revisores verificam: correção funcional, cobertura de testes, aderência às restrições inegociáveis, impacto de performance e atualização de documentação relevante.

6. **CODEOWNERS:** Alterações em `db/procedures/`, `infra/security/` e workflows de CI/CD requerem aprovação explícita dos owners designados — independentemente de outras aprovações.

Para contribuições de maior impacto (novos módulos, mudanças arquiteturais, integrações de gateway), abra uma RFC (Request for Comments) no formato de ADR antes de qualquer código, para alinhar o design com a visão técnica do projeto.

---

## 16. 📂 Apendices & Glossario

### A. Glossário Técnico Completo

| Termo | Definição Técnica |
|---|---|
| **Tempo de Validade (Valid Time)** | Quando o evento de fato ocorreu no mundo real — independentemente de quando o sistema soube. Ex: uma venda feita em 30/Jan pode ser registrada no ERP em 05/Fev; o Valid Time é 30/Jan. |
| **Tempo de Sistema (System Time)** | Quando o dado foi gravado no banco de dados — a perspectiva do sistema. No exemplo acima, System Time = 05/Fev. |
| **Drift (Desvio Transacional)** | Divergência crescente entre o saldo real do negócio e o saldo que o ERP acredita ser verdadeiro, causada por falhas de comunicação com sistemas externos. |
| **Limbo** | Estado de uma transação que está processada pelo ERP mas ainda não confirmada pelo gateway externo, e que excedeu o timeout de retries automáticos. |
| **Idempotência** | Propriedade de uma operação que garante o mesmo resultado independentemente de quantas vezes é executada com os mesmos parâmetros. No SincronizaMEI, implementada via Redis `SET NX EX`. |
| **ACL (Anti-Corruption Layer)** | Camada de tradução que isola o domínio de negócio dos contratos de sistemas externos, evitando que mudanças em APIs de terceiros impactem a lógica central. |
| **DLQ (Dead Letter Queue)** | Fila de mensagens que falharam no processamento após o número máximo de retries. Permite diagnóstico e reprocessamento manual sem perda de dados. |
| **Bounded Context** | Fronteira explícita de um domínio de negócio — dentro desta fronteira, termos e modelos têm um significado específico e consistente. Módulos `financeiro`, `estoque` e `rh` são Bounded Contexts independentes. |
| **Circuit Breaker** | Padrão de resiliência que "abre" (para chamadas) quando a taxa de erro de um sistema externo excede um threshold, evitando cascata de falhas. Retorna ao estado normal gradualmente. |
| **Expand-Contract** | Padrão de migração de schema em duas fases para mudanças destrutivas: primeiro adicionar o novo estado sem remover o antigo (expand), depois remover o antigo após validação (contract). |

### B. Tabela de Status de Integração — Máquina de Estados Completa

| Status | Código | Semântica | Transições Possíveis | Persistência |
|---|---|---|---|---|
| `CRIADA` | `CREATED` | Aceita pela API, aguardando enfileiramento | → `ENFILEIRADA` | Bitemporal |
| `ENFILEIRADA` | `QUEUED` | Publicada no RabbitMQ, aguardando Worker | → `PROCESSANDO` | Bitemporal |
| `PROCESSANDO` | `PROCESSING` | Worker enviou ao gateway, aguardando resposta | → `PENDENTE_CONCILIACAO`, `ERRO_TECNICO`, `REJEITADA` | Bitemporal |
| `ERRO_TECNICO` | `TECHNICAL_ERROR` | Gateway retornou 5xx, retentativa em andamento | → `PROCESSANDO` (retry), `LIMBO` (retries esgotados) | Bitemporal |
| `LIMBO` | `IN_LIMBO` | Retries esgotados, aguardando Worker de 15 min | → `PENDENTE_CONCILIACAO` (Worker recupera) | Bitemporal |
| `PENDENTE_CONCILIACAO` | `PENDING_RECONCILIATION` | Gateway confirmou, Worker validando valores | → `CONCILIADA`, `DIVERGENTE_AUDITORIA` | Bitemporal |
| `CONCILIADA` | `CONCILIATED` | Valores confirmados, reconciliação completa | → (estado terminal) | Bitemporal |
| `DIVERGENTE_AUDITORIA` | `DIVERGENT_AUDIT` | Diferença de valor detectada, aguarda revisão | → `CONCILIADA` (aprovação manual), `ESTORNADA` | Bitemporal |
| `REJEITADA` | `REJECTED` | Regra de negócio ou 4xx do gateway | → (estado terminal) | Bitemporal |
| `ESTORNADA` | `REVERSED` | Estorno solicitado e confirmado pelo gateway | → (estado terminal) | Bitemporal |

### C. Decisões de Rejeição — Por que não X?

| Alternativa Avaliada | Por que foi rejeitada | ADR relacionado |
|---|---|---|
| Kafka em vez de RabbitMQ | Complexidade operacional desproporcional para volumes de MEI; RabbitMQ tem DLX nativo e management UI mais simples | ADR-02 |
| Event Sourcing (Axon Framework) | Curva de aprendizado steep; complexidade de projeções; bitemporalidade SQL resolve o problema com SQL familiar | ADR-04 |
| MongoDB em vez de PostgreSQL | Ausência de suporte nativo a TSTZRANGE, exclusion constraints e transações ACID com Stored Procedures | ADR-04 |
| Microsserviços desde o início | Complexidade de distributed tracing, sagas e service mesh sem maturidade de domínio validada | ADR-01 |
| JWT stateless sem Redis | Impossibilidade de revogar sessões imediatamente em incidentes de segurança | ADR-05 |
| H2 para testes | Não suporta features PostgreSQL críticas — triggers, TSTZRANGE, `btree_gist` | (Restrição #4) |

---

## 8. Changelog

> Formato: [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) · [Semantic Versioning 2.0.0](https://semver.org/lang/pt-BR/)

### [Unreleased]

**Adicionado:**
- RF-06: Suporte a multi-moeda com preservação de taxa de câmbio histórica (Q2 2026)
- RF-07: Sistema de alertas proativos para transações em limbo (Q2 2026)

---

### [1.0.0] — 2026-04-16

**Backend (Java 17 / Spring Boot 3.2)**
- `IdempotencyInterceptor`: controle de duplicidade via `SET NX EX` com TTL de 24h
- `HookRegistry`: extensão via eventos de domínio para customizações isoladas
- Módulos `financeiro`, `estoque`, `rh` com Bounded Contexts isolados
- `GatewayPagamentoAdapter`: ACL com Circuit Breaker e Backoff (1s, 2s, 4s, 8s)
- Worker de reconciliação assíncrona a cada 15 min via Quartz + Spring Batch
- Dead Letter Queue com isolamento de mensagens com falha definitiva

**Camada de Dados (PostgreSQL 15)**
- Schema bitemporal: `valid_from`, `valid_to`, `system_init`, `system_end` em tabelas core
- `sp_reconciliar_ordem`: tolerância de R$ 0,50 e versionamento bitemporal automático
- `fn_check_integrity`: diagnóstico point-in-time sem acesso ao código-fonte
- `fn_estado_bitemporal`: consulta histórica em qualquer ponto do tempo
- Trigger `trg_bloquear_delete`: `DELETE` físico proibido em tabelas core
- Flyway configurado com migrations DDL separadas de Stored Procedures

**Observabilidade e Segurança**
- Logging estruturado JSON com `traceId`/`correlationId`
- `@Masked` para mascaramento dinâmico de PII em logs
- `AesGcmEncryptor`: AES-256-GCM — chave injetada via Vault
- Health checks granulares: PostgreSQL, Redis, RabbitMQ DLQ, Gateway PIX
- OpenTelemetry para métricas p95 e rastreio distribuído

**Frontend (React 18 / Vite)**
- Interface Dual-UX: Modo Operacional (MEI) e Modo Auditoria (Especialista)
- React Query, Zustand, `ErrorBoundary`, Skeletons de loading
- Indicador de Circuit Breaker em tempo real

**CI/CD e Infraestrutura**
- GitHub Actions: Build → SAST → Flyway Staging → k6 Smoke → Docker Push
- Imagem Docker multi-stage (< 200MB)
- Terraform com paridade dev/staging/prod
- Blue-Green Deployment com Readiness Probes

---

[Unreleased]: https://github.com/kalyel/sincronizamei/compare/v1.0.0...HEAD  
[1.0.0]: https://github.com/kalyel/sincronizamei/releases/tag/v1.0.0

---

*Construído com ❤️ e obsessão por integridade financeira por Kalyel Nunes Laurindo*

*"O código que lida com dinheiro de pessoas reais não tem direito a ser casual."*

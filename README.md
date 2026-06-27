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

```text
           [Client POST /ordens] (Idempotency Key Generated)
                    │
                    ▼
       ┌──────────────────────────┐
       │  PROCESSAMENTO_PENDENTE  │
       │ (Persisted State in DB)  │
       └────────────┬─────────────┘
                    │ (API returns HTTP 202 Accepted)
                    ▼
       ┌──────────────────────────┐
  ┌───>│        ENFILEIRADA       │ ◄─────────────────────────┐
  │    │  (RabbitMQ Ingestion)    │                           │
  │    └────────────┬─────────────┘                           │
  │                 │ (Worker consumes from queue)            │
  │                 ▼                                         │
  │    ┌──────────────────────────┐                           │
  │    │       PROCESSANDO        │                           │
  │    │ (API call to Payment GW) │                           │
  │    └────────────┬─────────────┘                           │
  │                 │                                         │
  │                 ├──(success callback)──┐                  │
  │                 │                      │                  │
  │ (tech timeout)  ▼ (HTTP 5xx)           │                  │ (automatic retry, max 3x)
  │    ┌──────────────────────────┐        │                  │
  │    │       ERRO_TECNICO       ├────────┼──────────────────┘
  │    │ (Awaiting retry cycle)   │        │
  │    └────────────┬─────────────┘        │
  │                 │ (retries exhausted)  │
  │                 ▼                      │
  │    ┌──────────────────────────┐        │
  │    │          LIMBO           │        │
  │    │ (Unsettled transaction)  │        │
  │    └────────────┬─────────────┘        │
  │                 │                      │
  │                 │ (reconciliation job  │
  │                 │  scans every 15m)    │
  │                 ▼                      │
  │    ┌──────────────────────────┐        │
  │    │      RECONCILIANDO       │        │
  │    │ (Pessimistic DB lock)    │        │
  │    └────────────┬─────────────┘        │
  │                 │                      │
  │        ┌────────┴────────┬─────────────┤
  │        │ (diff <= R$0.50)│ (diff > R$0.50) (success PIX callback)
  ▼        ▼                 ▼             ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  REJEITADA   │   │  CONCILIADO  │   │  DIVERGENTE  │
│  (Fund Error │   │ (AC-01.1/2)  │   │  AUDITORIA   │
│  / Rejected) │   └──────▲───────┘   └──────┬───────┘
└──────┬───────┘          │                  │
       │                  │ (approved)       │ (refunded)
       ▼                  └──────────────────┼───────────────┐
   [  EXIT  ] <──────────────────────────────┘               ▼
                                                         [  EXIT  ]
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

## 5. 🏗️ Arquitetura, ADRs e Diagramas

Todas as especificações técnicas detalhadas de arquitetura de software, incluindo a **Matriz de Rastreabilidade de Riscos**, os **7 Registros de Decisão de Arquitetura (ADRs)**, os diagramas de modelagem C4 (Contexto, Container e Componente), e as DDLs das Stored Procedures, foram consolidadas no documento de design técnico:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md)**

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

A estrutura detalhada das pastas do projeto, bem como as diretrizes de desenvolvimento (Clean Code, padrões GoF, persistência bitemporal e padrões de segurança de dados), estão documentadas na seção correspondente do documento de design:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L346)**

---

## 7. 🔌 API e Integrações

Todos os contratos de API REST (RFC 7807), esquemas de cabeçalho, tratamentos de resiliência e validações de assinaturas de webhook estão consolidados no:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L476)**

---

## 11. 🐳 Implantação (Deploy)

As estratégias de deploy Blue-Green, configurações de pipelines de CI/CD (Quality Gates) e especificações de Terraform AWS estão documentadas em:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L295)**

---

## 6. 🔒 Segurança e Observabilidade

As diretrizes de conformidade LGPD (AES-256-GCM), criptografia, chaves de Vault, coleta de métricas com Prometheus, visualização no Grafana e políticas de segurança estão descritas em:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L137)**

---

## 8. ⚙️ Customizações e Extensibilidade

A especificação formal do Hook Registry e da interface do Plugin de customizações de negócio está disponível em:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L476)**

---

## 12. 🐛 Processo de Debug e Suporte Técnico

Os fluxos de triagem de incidentes, SLAs de severidade e runbooks de emergência (Recuperação de Drift, replay de DLQ e hotfix de Stored Procedures) estão disponíveis na Seção 15 do SDD:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L463)**

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

## 16. 📂 Apêndices & Glossário

O glossário de termos ubíquos, tabelas de status de integração e matrizes de decisões de rejeição técnica (Por que não X?) estão consolidados no:

👉 **[Software Design Document - SincronizaMEI.md](./context/Software%20Design%20Document%20-%20SincronizaMEI.md#L500)**

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

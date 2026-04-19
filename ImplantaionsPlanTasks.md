# 🚀 SincronizaMEI — Plano de Implantação & Backlog SMART

> **Gerente de Projeto / Arquiteto Sênior:** Plano de entrega incremental para dev júnior  
> **Priorização:** Matriz de Materialidade (Impacto × Urgência)  
> **Formato:** Compatível com Notion (headers + tabelas) e Trello (cards independentes)  
> **Convenção de commits:** `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`

---

## 📊 Legenda de Prioridade

| Prioridade | Símbolo | Critério |
|---|---|---|
| Crítico (bloqueante) | 🔴 P0 | Sem isso, nada funciona |
| Alto | 🟠 P1 | Fundação técnica / compliance obrigatório |
| Médio | 🟡 P2 | Feature core do produto |
| Baixo | 🟢 P3 | Qualidade, UX, observabilidade |

---

## 🗂️ ÉPICOS — Visão Geral

| # | Épico | Prioridade | Tasks |
|---|---|---|---|
| E1 | Setup de Ambiente & Infraestrutura | 🔴 P0 | 6 tasks |
| E2 | Banco de Dados & Migrations | 🔴 P0 | 7 tasks |
| E3 | Backend — Core ERP (Java/Spring) | 🟠 P1 | 10 tasks |
| E4 | Segurança & Compliance LGPD | 🟠 P1 | 5 tasks |
| E5 | Mensageria & Workers Assíncronos | 🟡 P2 | 5 tasks |
| E6 | Frontend React PWA | 🟡 P2 | 7 tasks |
| E7 | Testes & Qualidade | 🟠 P1 | 6 tasks |
| E8 | CI/CD & Deploy Blue-Green | 🟡 P2 | 5 tasks |
| E9 | Observabilidade & Alertas | 🟢 P3 | 4 tasks |

**Total: 55 tasks**

---

---

# 🔴 E1 — SETUP DE AMBIENTE & INFRAESTRUTURA

---

## TASK-001 · Configurar repositório Git e estrutura de pastas

**Épico:** E1 — Setup  
**Prioridade:** 🔴 P0  
**Estimativa:** 2h  
**Pré-requisitos:** Nenhum

### O que fazer
Criar o repositório, configurar `.gitignore`, `commitlint`, Husky pre-commit hook e estrutura de diretórios do monorepo.

### Critérios de Aceite (Definition of Done)
- [x] Repositório criado no GitHub com branch `main` protegida (mínimo 1 aprovação para merge)
- [x] `.gitignore` cobre: `target/`, `node_modules/`, `.env*`, `*.jar`, `*.class`
- [x] `commitlint` instalado e configurado com regra Angular — commits como "fix bug" são **rejeitados** automaticamente no pre-commit
- [x] Husky hook rodando: `npx commitlint --edit` no `commit-msg`
- [x] Estrutura de pastas criada conforme abaixo

### Referência no README
Seção 10 — Estrutura do Código

---

## TASK-002 · Configurar Docker Compose para ambiente local

**Épico:** E1 — Setup  
**Prioridade:** 🔴 P0  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-001

### O que fazer
Criar `docker-compose.yml` com todos os serviços de infraestrutura necessários para rodar o projeto localmente.

### Critérios de Aceite
- [x] `docker-compose.yml` na raiz com os seguintes serviços:
  - `postgres:16` na porta `5432`, banco `sincronizamei_dev`, usuário `app_user`
  - `redis:7.2` na porta `6379`
  - `rabbitmq:3.13-management` nas portas `5672` (AMQP) e `15672` (UI)
- [x] Arquivo `.env.example` com todas as variáveis necessárias (sem valores reais)
- [x] `docker-compose up -d` sobe todos os serviços sem erro
- [x] Health check configurado para cada serviço
- [x] `README-DEV.md` com instrução: `cp .env.example .env && docker-compose up -d`

### ⚠️ Restrição Inegociável
**NUNCA** colocar senhas reais no `docker-compose.yml`. Usar `${POSTGRES_PASSWORD}` lendo do `.env`.

---

## TASK-003 · Inicializar projeto Spring Boot 3 (backend)

**Épico:** E1 — Setup  
**Prioridade:** 🔴 P0  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-001

### O que fazer
Criar o projeto Spring Boot 3 com Java 21 via Spring Initializr com todas as dependências base.

### Critérios de Aceite
- [x] `pom.xml` com Java 21, Spring Boot 3.x, dependências:
  - `spring-boot-starter-web`
  - `spring-boot-starter-data-jpa`
  - `spring-boot-starter-security`
  - `spring-boot-starter-validation`
  - `spring-boot-starter-actuator`
  - `spring-boot-starter-amqp` (RabbitMQ)
  - `spring-boot-starter-data-redis`
  - `flyway-core` + `flyway-database-postgresql`
  - `resilience4j-spring-boot3`
  - `micrometer-registry-otlp`
  - `testcontainers-postgresql` (scope test)
- [x] Propriedade `spring.threads.virtual.enabled=true` configurada (Project Loom)
- [x] `application.yml` base sem credenciais hardcoded — todas via `${ENV_VAR}`
- [x] `mvn compile` sem erros

---

## TASK-004 · Inicializar projeto React + Vite (frontend)

**Épico:** E1 — Setup  
**Prioridade:** 🔴 P0  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-001

### O que fazer
Criar o projeto React 18 com Vite, Tailwind CSS e dependências necessárias.

### Critérios de Aceite
- [x] Projeto criado com `npm create vite@latest frontend -- --template react-ts`
- [x] Tailwind CSS 3.4 configurado e funcional
- [x] Dependências instaladas: `react-query`, `zustand`, `react-hook-form`, `zod`, `axios`
- [x] PWA configurado via `vite-plugin-pwa` com `manifest.json` básico
- [x] `npm run dev` abre em `localhost:5173` sem erros no console
- [x] `npm run build` gera bundle sem erros

---

## TASK-005 · Configurar HashiCorp Vault (secrets management)

**Épico:** E1 — Setup  
**Prioridade:** 🔴 P0  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-002, TASK-003

### O que fazer
Configurar o Vault para injeção de segredos sensíveis (chave AES, senhas de banco, tokens de gateway).

### Critérios de Aceite
- [x] Vault adicionado ao `docker-compose.yml` na porta `8200` (modo dev para local)
- [x] `spring-cloud-starter-vault-config` adicionado ao `pom.xml`
- [x] `bootstrap.yml` configurado para ler de `secret/sincronizamei`
- [x] Segredos mapeados: `AES_SECRET_KEY`, `POSTGRES_PASSWORD`, `REDIS_PASSWORD`, `RABBITMQ_PASSWORD`
- [x] `AES_SECRET_KEY` tem pelo menos 32 bytes aleatórios
- [x] **Teste:** iniciar Spring Boot — nenhum segredo aparece no log de startup

### ⚠️ Restrição Inegociável (ADR-05)
Nenhuma credencial em `application.properties` ou código-fonte. PR rejeitado se encontrado.

---

## TASK-006 · Configurar Terraform para infraestrutura base (staging)

**Épico:** E1 — Setup  
**Prioridade:** 🟠 P1  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-002

### O que fazer
Criar módulos Terraform para provisionar a infraestrutura de staging com paridade ao ambiente de produção.

### Critérios de Aceite
- [ ] Módulos em `infra/terraform/` para: VPC, instâncias de DB, Redis, RabbitMQ, Load Balancer
- [ ] Variáveis separadas por ambiente: `dev.tfvars`, `staging.tfvars`, `prod.tfvars`
- [ ] `terraform plan` executa sem erros contra staging
- [ ] `terraform apply` provisiona infra em < 10 min
- [ ] Output do Terraform exporta: `db_endpoint`, `redis_endpoint`, `rabbitmq_endpoint`

---

---

# 🔴 E2 — BANCO DE DADOS & MIGRATIONS

---

## TASK-007 · Criar schema inicial com Flyway (tabelas core)

**Épico:** E2 — Banco  
**Prioridade:** 🔴 P0  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-003, TASK-002

### O que fazer
Criar as migrations Flyway para o schema bitemporal das tabelas core dos três bounded contexts.

### Critérios de Aceite
- [ ] Migration `V1__create_schema_financeiro.sql` criada em `db/migrations/`
- [ ] Migration `V2__create_schema_estoque.sql`
- [ ] Migration `V3__create_schema_rh.sql`
- [ ] **Todas** as tabelas core possuem as quatro colunas bitemporais:
  ```sql
  valid_from       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  valid_to         TIMESTAMPTZ,
  system_init_tstz TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  system_end_tstz  TIMESTAMPTZ
  ```
- [ ] Extensões ativadas: `btree_gist`, `pgcrypto`
- [ ] `mvn flyway:migrate` aplica todas as migrations sem erro no PostgreSQL 16 real (não H2)
- [ ] Nenhuma migration alterada após o primeiro commit em `main`

### ⚠️ Restrição Inegociável (ADR-04)
Proibido usar H2. Usar PostgreSQL 16 real via Testcontainers para validar.

---

## TASK-008 · Implementar trigger de bloqueio de DELETE físico

**Épico:** E2 — Banco  
**Prioridade:** 🔴 P0  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-007

### O que fazer
Criar o trigger `trg_bloquear_delete` em todas as tabelas core para implementar a imutabilidade de dados por design.

### Critérios de Aceite
- [ ] Migration `V4__create_trigger_block_delete.sql` criada
- [ ] Trigger aplicado nas tabelas: `financeiro.ordens`, `financeiro.lancamentos`, `estoque.movimentacoes`, `rh.registros`
- [ ] **Teste SQL:** `DELETE FROM financeiro.ordens WHERE id = 'qualquer-id'` retorna erro com mensagem descritiva: `"DELETE físico proibido. Use soft-delete bitemporal."`
- [ ] Trigger documentado com comentário SQL explicando o motivo arquitetural

### Referência no README
RF-04 (AC-04.1), RNF-07, ADR-04

---

## TASK-009 · Implementar Stored Procedure sp_reconciliar_ordem

**Épico:** E2 — Banco  
**Prioridade:** 🔴 P0  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-007, TASK-008

### O que fazer
Criar a procedure central de reconciliação que implementa a tolerância de R$0,50 e o versionamento bitemporal automático.

### Critérios de Aceite
- [ ] Arquivo `db/procedures/sp_reconciliar_ordem.sql` criado
- [ ] Migration `V5__create_sp_reconciliar_ordem.sql` aplica via Flyway com `CREATE OR REPLACE`
- [ ] Lógica implementada:
  - Diferença ≤ R$0,50 → status `CONCILIADO` com nota de divergência
  - Diferença > R$0,50 → status `DIVERGENTE_AUDITORIA`
  - Versão anterior recebe `valid_to = NOW()` antes de criar nova versão
- [ ] Teste de integração com PostgreSQL real validando os 3 critérios de aceite do RF-01
- [ ] Procedure chamável via `EntityManager.createNativeQuery("CALL sp_reconciliar_ordem(?, ?)")`

### Referência no README
RF-01 (AC-01.1, AC-01.2, AC-01.3)

---

## TASK-010 · Implementar função fn_check_integrity

**Épico:** E2 — Banco  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-009

### O que fazer
Criar função de diagnóstico point-in-time para suporte de produção.

### Critérios de Aceite
- [ ] `db/procedures/fn_check_integrity.sql` criado
- [ ] Função aceita `idempotency_key UUID` como parâmetro
- [ ] Retorna: todas as versões históricas da ordem, campo `em_limbo BOOLEAN`, `minutos_limbo INTEGER`
- [ ] Disponível para execução pelo time de suporte sem acesso ao código-fonte
- [ ] Testado com query: `SELECT * FROM financeiro.fn_check_integrity('uuid-de-teste')`

### Referência no README
RF-04 (AC-04.3), RP-05

---

## TASK-011 · Implementar função fn_estado_bitemporal

**Épico:** E2 — Banco  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-009

### O que fazer
Criar função de consulta histórica para auditoria fiscal — "como estava o sistema em tal data?".

### Critérios de Aceite
- [ ] `db/procedures/fn_estado_bitemporal.sql` criado
- [ ] Assinatura: `fn_estado_bitemporal(p_id UUID, p_as_of TIMESTAMPTZ)`
- [ ] Retorna o estado da ordem **exatamente como estava** na data informada
- [ ] `valid_from` (data real do evento) ≠ `system_init_tstz` (data de registro) — ambas preservadas
- [ ] Teste: criar ordem em Janeiro, modificar em Fevereiro, consultar com data de Janeiro → retorna estado de Janeiro

### Referência no README
RF-05 (AC-05.1, AC-05.2)

---

## TASK-012 · Configurar cursor-based pagination nas queries principais

**Épico:** E2 — Banco  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-007

### O que fazer
Garantir que nenhuma query de listagem use `OFFSET` — implementar paginação por cursor em todas as listagens.

### Critérios de Aceite
- [ ] Queries de listagem usam padrão: `WHERE id > :cursor ORDER BY id LIMIT :size`
- [ ] Parâmetros de response incluem: `nextCursor`, `hasMore`
- [ ] Testado com 10.000+ registros sem OOM ou timeout
- [ ] **Nenhum** uso de `OFFSET` ou `Page` do Spring Data JPA em tabelas com > 1k registros esperados

### Referência no README
RP-03

---

## TASK-013 · Implementar script de anonimização de PII para homologação

**Épico:** E2 — Banco  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-007

### O que fazer
Criar script SQL obrigatório para higienização de dados PII antes de restaurar dumps de produção em staging.

### Critérios de Aceite
- [ ] `db/scripts/anonymize_dump.sql` criado
- [ ] Script mascara: CPF, e-mail, conta bancária, telefone
- [ ] CPF substituído por formato `000.000.000-XX` onde XX = últimos 2 dígitos reais (mantém unicidade)
- [ ] Script executado antes de qualquer `pg_restore` em staging (documentado no CI)
- [ ] Testado: após execução, `grep -i "cpf_real"` não encontra nada no dump anonimizado

### Referência no README
ADR-05, RNF-06

---

---

# 🟠 E3 — BACKEND CORE ERP (JAVA/SPRING)

---

## TASK-014 · Implementar IdempotencyInterceptor (Redis SET NX EX)

**Épico:** E3 — Backend  
**Prioridade:** 🔴 P0  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-003, TASK-002

### O que fazer
Implementar o interceptor de idempotência que protege todos os endpoints POST/PUT de processamento duplicado.

### Critérios de Aceite
- [ ] Classe `IdempotencyInterceptor` implementa `HandlerInterceptor`
- [ ] Header `X-Idempotency-Key` ausente em POST/PUT → `HTTP 400` com mensagem descritiva
- [ ] Chave nova: processa normalmente, salva response no Redis com `SET key response NX EX 86400`
- [ ] Chave existente (dentro de 24h): retorna `HTTP 409` com response original cacheado
- [ ] Duas requisições simultâneas com mesma chave: apenas uma persiste (atomicidade garantida pelo `NX`)
- [ ] Testes de integração cobrindo os 3 ACs do RF-02

### Referência no README
RF-02 (AC-02.1, AC-02.2, AC-02.3), ADR-03

---

## TASK-015 · Implementar bounded context Financeiro (entidades e repositórios)

**Épico:** E3 — Backend  
**Prioridade:** 🔴 P0  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-007, TASK-014

### O que fazer
Criar as entidades JPA, repositórios e serviços do módulo financeiro respeitando o bounded context.

### Critérios de Aceite
- [ ] Entidades em `com.sincronizamei.financeiro.domain`: `Ordem`, `Lancamento`
- [ ] Repositórios usam `EntityManager.createNativeQuery()` para operações bitemporais — **nunca** `repository.save()` em entidades bitemporais
- [ ] Enum `OrdemStatus` com todos os estados da máquina de estados (Apêndice B do README)
- [ ] Nenhum import de classes do pacote `estoque` ou `rh` (violação detectada por ArchUnit)
- [ ] Comunicação com outros módulos apenas via `ApplicationEventPublisher`
- [ ] Teste unitário para cada transição de estado do enum

### Referência no README
Apêndice B — Máquina de Estados, ADR-01, Restrição #3

---

## TASK-016 · Implementar bounded context Estoque (entidades e repositórios)

**Épico:** E3 — Backend  
**Prioridade:** 🟠 P1  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-007

### O que fazer
Criar as entidades, repositórios e serviços do módulo de estoque.

### Critérios de Aceite
- [ ] Entidades em `com.sincronizamei.estoque.domain`: `Produto`, `MovimentacaoEstoque`
- [ ] Capacidade para catálogo de 500k itens (índices corretos nas migrations)
- [ ] Movimentação de estoque usa stored procedure para atomicidade
- [ ] Listener de `OrdemCriadaEvent` do módulo financeiro atualiza estoque sem acesso direto ao repositório financeiro
- [ ] Teste de integração: criar ordem → verificar baixa de estoque sem chamar nenhum método do módulo financeiro diretamente

### Referência no README
RNF-03, ADR-01

---

## TASK-017 · Implementar FaturamentoController (endpoint POST /api/v1/faturamento/ordens)

**Épico:** E3 — Backend  
**Prioridade:** 🔴 P0  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-015, TASK-014

### O que fazer
Implementar o endpoint de faturamento seguindo o protocolo de resiliência documentado no README.

### Critérios de Aceite
- [ ] `POST /api/v1/faturamento/ordens` implementado
- [ ] Response síncrono retorna `HTTP 202 Accepted` com `Location` header
- [ ] Body de resposta contém: `ordemId`, `status: "PROCESSAMENTO_PENDENTE"`, `estimatedConciliationAt`, `_links`
- [ ] Header `X-Correlation-ID` propagado — se ausente, gerado pelo servidor
- [ ] Validação de DTO com Bean Validation — campos inválidos retornam `HTTP 400`
- [ ] Teste de integração cobrindo o exemplo completo da Seção 8.3 do README

### Referência no README
Seção 8.3, RF-01, RNF-01 (p95 < 800ms)

---

## TASK-018 · Implementar GatewayPagamentoAdapter com Circuit Breaker e Retry

**Épico:** E3 — Backend  
**Prioridade:** 🟠 P1  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-017

### O que fazer
Implementar o Anti-Corruption Layer para comunicação com o gateway de pagamento externo.

### Critérios de Aceite
- [ ] `GatewayPagamentoAdapter` implementa interface `GatewayPagamentoPort`
- [ ] Retry configurado: 4 tentativas, backoff exponencial 1s → 2s → 4s → 8s
- [ ] Circuit Breaker configurado com Resilience4j: abre após 50% de falha em 10 chamadas
- [ ] Método `@Recover`: falha definitiva → publica na DLQ do RabbitMQ
- [ ] `HTTP 503` retornado com headers `X-Circuit-State: OPEN` e `X-Retry-After: {seconds}` quando CB aberto
- [ ] Teste: simular gateway retornando 5xx → verificar que após 4 tentativas vai para DLQ

### Referência no README
Seção 7.3, Seção 8.1 (HTTP 503)

---

## TASK-019 · Implementar HookRegistry (sistema de extensibilidade)

**Épico:** E3 — Backend  
**Prioridade:** 🟡 P2  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-015, TASK-016

### O que fazer
Implementar o sistema de hooks que permite customizações isoladas sem modificar o core.

### Critérios de Aceite
- [ ] `HookRegistry` centraliza registro de listeners de eventos de domínio
- [ ] Plugin sem `fallback` definido → `HookRegistry` rejeita com erro descritivo no startup
- [ ] Exceção em handler capturada + logada com `correlation_id` — **Core não interrompe**
- [ ] Eventos publicados: `OrdemFaturadaEvent`, `EstoqueMovimentadoEvent`
- [ ] Listeners em `plugins/` não têm acesso a repositórios ou serviços do Core
- [ ] Teste: handler que lança exceção → verificar que o fluxo principal continua normalmente

### Referência no README
RF-03 (AC-03.1, AC-03.2, AC-03.3), ADR-07

---

## TASK-020 · Implementar endpoint de webhook inbound (callbacks do gateway)

**Épico:** E3 — Backend  
**Prioridade:** 🟠 P1  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-018

### O que fazer
Implementar o endpoint de recebimento de callbacks do gateway de pagamento com validação de assinatura.

### Critérios de Aceite
- [ ] `POST /api/v1/webhooks/gateway` implementado
- [ ] Validação `HMAC-SHA256` do body com o segredo configurado — assinatura inválida → `HTTP 401`
- [ ] Replay de webhook > 5 minutos → `HTTP 401` (timestamp no header `X-Signature`)
- [ ] Evento **salvo em banco antes** de qualquer processamento (Persistence First)
- [ ] ID do evento externo usado como chave de idempotência para evitar processamento duplo
- [ ] Teste: enviar mesmo webhook duas vezes → apenas um processamento ocorre

### Referência no README
Seção 7.4, Seção 8.2 (X-Signature)

---

## TASK-021 · Implementar padronização de erros RFC 7807

**Épico:** E3 — Backend  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-017

### O que fazer
Implementar handler global de exceções que retorna erros no formato `application/problem+json`.

### Critérios de Aceite
- [ ] `@ControllerAdvice` global implementado
- [ ] Todos os erros retornam `Content-Type: application/problem+json`
- [ ] Campos obrigatórios: `type`, `title`, `status`, `detail`, `instance`, `correlationId`
- [ ] Mapeamentos: `ValidationException → 400`, `IdempotencyConflictException → 409`, `BusinessRuleException → 422`, `RateLimitException → 429`, `CircuitBreakerOpenException → 503`
- [ ] Teste: cada tipo de exceção retorna o status HTTP correto com body no formato RFC 7807

### Referência no README
Seção 7.2

---

## TASK-022 · Implementar rate limiting por cliente

**Épico:** E3 — Backend  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-003

### O que fazer
Implementar rate limiting por `clientId` para proteger o core ERP contra burst de um único cliente.

### Critérios de Aceite
- [ ] Rate limiting configurado via Resilience4j ou Bucket4j
- [ ] Exceder limite → `HTTP 429` com header `Retry-After: {seconds}`
- [ ] Limite configurável por ambiente via `application.yml`
- [ ] Rate limiting baseado no `clientId` do JWT (não no IP)
- [ ] Teste de carga: 200 req/s de um cliente → `HTTP 429` a partir do threshold configurado

### Referência no README
Seção 8.1 (HTTP 429)

---

## TASK-023 · Implementar SSE endpoint para polling de status de ordem

**Épico:** E3 — Backend  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-017

### O que fazer
Implementar Server-Sent Events para notificação push quando o status de uma ordem muda.

### Critérios de Aceite
- [ ] `GET /api/v1/ordens/{id}/events` implementado com SSE
- [ ] Evento emitido quando status muda (PROCESSANDO → CONCILIADO, etc.)
- [ ] Conexão encerra automaticamente em estados terminais (`CONCILIADO`, `REJEITADO`, `ESTORNADO`)
- [ ] Timeout de conexão de 15 minutos (SLA máximo de reconciliação)
- [ ] Teste: criar ordem, abrir SSE, simular callback do gateway → evento de status recebido no SSE

### Referência no README
Seção 8.1 (Nota sobre HTTP 202)

---

---

# 🟠 E4 — SEGURANÇA & COMPLIANCE LGPD

---

## TASK-024 · Implementar AesGcmEncryptor para dados PII

**Épico:** E4 — Segurança  
**Prioridade:** 🔴 P0  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-005

### O que fazer
Implementar o encriptador AES-256-GCM para dados sensíveis (CPF, conta bancária) antes da persistência.

### Critérios de Aceite
- [ ] Classe `AesGcmEncryptor` implementada conforme exemplo da Seção 4.4 do README
- [ ] IV de 96 bits (12 bytes) gerado aleatoriamente por operação
- [ ] Chave injetada via `${AES_SECRET_KEY}` do Vault — **nunca** hardcoded
- [ ] Conversor JPA `@Converter(autoApply = false)` aplicado nos campos PII
- [ ] Queries de busca por CPF usam hash SHA-256 (não o valor criptografado diretamente)
- [ ] Teste: persistir cliente com CPF real → verificar que o valor no banco está encriptado

### Referência no README
ADR-05, RNF-05

---

## TASK-025 · Implementar @Masked para logs (mascaramento dinâmico PII)

**Épico:** E4 — Segurança  
**Prioridade:** 🔴 P0  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-003

### O que fazer
Implementar a anotação `@Masked` que mascara dados PII automaticamente na serialização de logs.

### Critérios de Aceite
- [ ] Anotação `@Masked` criada em `com.sincronizamei.shared.logging`
- [ ] Serializer customizado do Jackson substitui valor por `***-[últimos 4 dígitos]`
- [ ] Aplicada em `ClienteDTO`: campos `cpf`, `contaBancaria`, `email`
- [ ] Logging configurado com Logback em formato JSON estruturado
- [ ] Teste: logar um `ClienteDTO` com CPF real → verificar que o log contém `***-XXXX`, não o CPF completo
- [ ] Executar grep nos logs de staging: `grep -E "\d{3}\.\d{3}\.\d{3}-\d{2}"` não encontra nada

### Referência no README
ADR-05, RNF-06, Seção 4.4

---

## TASK-026 · Implementar autenticação JWT com perfis MEI e CONTROLLER

**Épico:** E4 — Segurança  
**Prioridade:** 🔴 P0  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-003

### O que fazer
Implementar autenticação JWT com suporte a dois perfis de usuário com permissões distintas.

### Critérios de Aceite
- [ ] JWT assinado com RS256 (chave privada via Vault)
- [ ] Claims obrigatórias: `sub` (userId), `role` (MEI | CONTROLLER), `iat`, `exp`
- [ ] Sessão armazenada no Redis para revogação imediata (não JWT stateless puro)
- [ ] Endpoints de auditoria (`/api/v1/auditoria/**`) requerem role `CONTROLLER`
- [ ] Endpoint de faturamento (`/api/v1/faturamento/**`) aceita ambos os roles
- [ ] Teste: token de MEI tentando acessar endpoint de auditoria → `HTTP 403`

### Referência no README
ADR-05, Seção 8.2 (Authorization header)

---

## TASK-027 · Implementar propagação de X-Correlation-ID end-to-end

**Épico:** E4 — Segurança  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-017

### O que fazer
Garantir que o `X-Correlation-ID` seja propagado de ponta a ponta: PWA → Backend → RabbitMQ → PostgreSQL.

### Critérios de Aceite
- [ ] Filter Spring adiciona `X-Correlation-ID` ao `MDC` (Mapped Diagnostic Context) do SLF4J
- [ ] Se ausente na requisição, UUID é gerado pelo servidor e incluído na response
- [ ] `correlationId` propagado no header de mensagens RabbitMQ (MessageProperties)
- [ ] Todo log JSON contém campo `correlationId`
- [ ] Teste: fazer requisição sem o header → response contém header gerado → logs do processamento assíncrono contêm o mesmo ID

### Referência no README
Seção 8.2, Garantia de Rastreabilidade Distribuída (Seção 1)

---

## TASK-028 · Configurar validação de assinatura de webhooks (HMAC-SHA256)

**Épico:** E4 — Segurança  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-020

### O que fazer
Garantir que a validação de assinatura de webhooks seja robusta contra replay attacks.

### Critérios de Aceite
- [ ] Validação HMAC-SHA256: `HMAC(body, secret)` comparado com `X-Signature` header usando `MessageDigest.isEqual()` (constant-time para evitar timing attack)
- [ ] Timestamp extraído da assinatura — webhooks com timestamp > 5 minutos → `HTTP 401`
- [ ] Segredo do gateway injetado via Vault
- [ ] Teste: body modificado após assinatura → `HTTP 401`
- [ ] Teste: webhook com timestamp de 10 minutos atrás → `HTTP 401`

### Referência no README
Seção 8.2 (X-Signature), Seção 7.4

---

---

# 🟡 E5 — MENSAGERIA & WORKERS ASSÍNCRONOS

---

## TASK-029 · Configurar RabbitMQ: exchanges, filas e DLQ

**Épico:** E5 — Mensageria  
**Prioridade:** 🟠 P1  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-002, TASK-003

### O que fazer
Configurar toda a topologia RabbitMQ: exchanges, filas de processamento, filas de reconciliação e Dead Letter Queues.

### Critérios de Aceite
- [ ] Exchange `financeiro.exchange` (direct)
- [ ] Fila `financeiro.processamento` com DLX configurado para `financeiro.dlq`
- [ ] Fila `financeiro.reconciliacao` para o worker de 15 min
- [ ] DLQ `financeiro.dlq` — mensagens chegam aqui após esgotamento de retries
- [ ] Configuração via `@Bean RabbitMQ` no Spring — não manual na UI
- [ ] Teste: publicar mensagem na fila principal, simular falha 3x → mensagem aparece na DLQ

### Referência no README
ADR-02, RF-07 (AC-07.3)

---

## TASK-030 · Implementar Worker de Reconciliação (Quartz + Spring Batch)

**Épico:** E5 — Mensageria  
**Prioridade:** 🔴 P0  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-009, TASK-029

### O que fazer
Implementar o worker que executa a cada 15 minutos e reconcilia ordens em limbo chamando `sp_reconciliar_ordem`.

### Critérios de Aceite
- [ ] Job Quartz configurado com cron `*/15 * * * *` (a cada 15 min)
- [ ] Worker busca ordens com status `LIMBO` usando cursor-based pagination
- [ ] Para cada ordem: chama `sp_reconciliar_ordem` via `EntityManager`
- [ ] Virtual Threads ativadas para processamento concorrente (Project Loom)
- [ ] Falha em uma ordem não interrompe o processamento das demais
- [ ] Log estruturado ao final: `{processadas: N, conciliadas: M, divergentes: K, falhas: J}`
- [ ] Teste de integração: colocar 100 ordens em LIMBO → worker processa todas em < 15 min

### Referência no README
Garantia de Consistência Eventual (Seção 1), RF-01 (AC-01.1)

---

## TASK-031 · Implementar consumidor da DLQ com alerta P1

**Épico:** E5 — Mensageria  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-029

### O que fazer
Implementar o consumidor que monitora a DLQ e dispara alertas quando ultrapassa 100 mensagens.

### Critérios de Aceite
- [ ] Worker verifica tamanho da DLQ a cada 5 minutos via Management API do RabbitMQ
- [ ] DLQ > 100 mensagens → alerta P1 disparado via canal configurado (e-mail / Slack / webhook)
- [ ] Canal de alerta configurável via `application.yml` sem recompilar
- [ ] Mensagens da DLQ logadas com `correlationId` para diagnóstico manual
- [ ] Endpoint `GET /api/v1/admin/dlq/status` expõe contagem atual da DLQ (role CONTROLLER)

### Referência no README
RF-07 (AC-07.3)

---

## TASK-032 · Implementar alerta de transações em limbo (> 30 min)

**Épico:** E5 — Mensageria  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-030

### O que fazer
Implementar alerta proativo para ordens que ficam mais de 30 minutos em `PROCESSAMENTO_PENDENTE`.

### Critérios de Aceite
- [ ] Query periódica detecta ordens com status `PROCESSAMENTO_PENDENTE` há > 30 minutos
- [ ] Alerta P2 enviado para operações
- [ ] Mensagem humanizada na UI: *"Seu pagamento está sendo processado. Aguarde até 15 minutos."*
- [ ] Registro criado em `auditoria.alertas` com `correlationId`, `orderId`, `timestamp`
- [ ] Não disparar alerta duplicado para a mesma ordem (idempotência do alerta)

### Referência no README
RF-07 (AC-07.1, AC-07.2)

---

## TASK-033 · Implementar suporte a multi-moeda (RF-06)

**Épico:** E5 — Mensageria  
**Prioridade:** 🟢 P3  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-015

### O que fazer
Implementar conversão dinâmica de moeda com snapshot diário de câmbio, sem recálculo retroativo.

### Critérios de Aceite
- [ ] Campo `moeda CHAR(3)` e `valor_brl_na_data NUMERIC(15,4)` já existem no schema (confirmar na migration)
- [ ] Job diário busca taxa de câmbio de API externa e persiste snapshot em `financeiro.cotacoes`
- [ ] Ao criar ordem em USD: persiste valor USD + equivalente BRL na data da transação
- [ ] Consulta histórica retorna o BRL da data original — **não** recalcula com taxa atual
- [ ] Teste: criar ordem USD em Janeiro com câmbio X, consultar em Março → BRL = valor de Janeiro

### Referência no README
RF-06 (AC-06.1, AC-06.2), Changelog [Unreleased]

---

---

# 🟡 E6 — FRONTEND REACT PWA

---

## TASK-034 · Implementar estrutura base com React Query, Zustand e ErrorBoundary

**Épico:** E6 — Frontend  
**Prioridade:** 🟠 P1  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-004

### O que fazer
Configurar a estrutura base do frontend com gerenciamento de estado, cache de queries e tratamento de erros.

### Critérios de Aceite
- [ ] `QueryClient` configurado com retry: 3x, stale time: 30s
- [ ] `Zustand` store com slice: `{ modoEspecialista: boolean, correlationId: string }`
- [ ] `ErrorBoundary` envolvendo cada painel de dashboard — erro em um painel não derruba a página
- [ ] Todos os componentes de leitura assíncrona têm Skeleton de loading (CLS = 0)
- [ ] Lógica de negócio **proibida** no frontend — qualquer cálculo deve vir do backend
- [ ] Teste: simular erro em uma query → ErrorBoundary exibe mensagem de erro, resto da UI funciona

### Referência no README
Seção 4.5, Restrição #2

---

## TASK-035 · Implementar modo Dual-UX (MEI vs CONTROLLER)

**Épico:** E6 — Frontend  
**Prioridade:** 🟡 P2  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-034, TASK-026

### O que fazer
Implementar a interface dual que adapta o contexto da UI ao perfil do usuário autenticado.

### Critérios de Aceite
- [ ] Modo MEI: foco em faturamento rápido, ações simples, sem dados de auditoria
- [ ] Modo CONTROLLER: densidade analítica, acesso a histórico bitemporal, divergências
- [ ] Toggle de modo persiste em `sessionStorage` via Zustand
- [ ] Perfil do JWT determina as permissões disponíveis — UI não exibe funcionalidades proibidas
- [ ] Transição entre modos sem reload da página

### Referência no README
Seção 1 (Experiência Dual-UX), Seção 4.5

---

## TASK-036 · Implementar formulário de faturamento com idempotência no cliente

**Épico:** E6 — Frontend  
**Prioridade:** 🟡 P2  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-035, TASK-017

### O que fazer
Implementar o formulário de criação de ordem com geração automática de `X-Idempotency-Key`.

### Critérios de Aceite
- [ ] UUID v4 gerado no frontend no momento de abertura do formulário
- [ ] UUID enviado no header `X-Idempotency-Key` a cada tentativa
- [ ] Resubmit do formulário: mesmo UUID reenviado → `HTTP 409` tratado como sucesso (order já criada)
- [ ] Validação com Zod antes do envio (campos obrigatórios, formatos)
- [ ] Feedback visual: estado "Processando..." com spinner após submit
- [ ] Polling de status via SSE endpoint após `HTTP 202` recebido

### Referência no README
Seção 8.3, RF-02

---

## TASK-037 · Implementar indicador de Circuit Breaker em tempo real

**Épico:** E6 — Frontend  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-018, TASK-036

### O que fazer
Implementar o componente de status do Circuit Breaker que informa o usuário quando o gateway está indisponível.

### Critérios de Aceite
- [ ] Componente `CircuitBreakerStatus` visível no dashboard
- [ ] Estados: CLOSED (verde), OPEN (vermelho), HALF_OPEN (amarelo)
- [ ] Quando OPEN: exibe mensagem *"Gateway temporariamente indisponível. Tentando novamente em X segundos."*
- [ ] Status atualizado via polling leve a cada 30s no endpoint `GET /api/v1/health/circuit-breaker`
- [ ] Teste: abrir CB no backend → componente exibe estado vermelho em < 35 segundos

### Referência no README
Seção 4.5 (Indicador de Circuit Breaker)

---

## TASK-038 · Implementar painel de auditoria bitemporal (modo CONTROLLER)

**Épico:** E6 — Frontend  
**Prioridade:** 🟢 P3  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-035, TASK-011

### O que fazer
Implementar a interface de consulta histórica que permite ao CONTROLLER consultar estados passados do sistema.

### Critérios de Aceite
- [ ] Date picker para seleção da data de consulta histórica
- [ ] Chamada para `fn_estado_bitemporal(id, asOfDate)` via API
- [ ] Exibe linha do tempo visual das versões do registro com `valid_from` e `system_init_tstz`
- [ ] Diferencia visualmente "data do evento no negócio" vs "data que o sistema registrou"
- [ ] Disponível apenas para role CONTROLLER (frontend valida via JWT claims)

### Referência no README
RF-05, Apêndice A (Glossário: Tempo de Validade vs Tempo de Sistema)

---

## TASK-039 · Configurar PWA (Service Worker + Manifest)

**Épico:** E6 — Frontend  
**Prioridade:** 🟢 P3  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-004

### O que fazer
Configurar o Service Worker e manifest para funcionamento offline parcial e instalabilidade.

### Critérios de Aceite
- [ ] `manifest.json` com: `name`, `short_name`, `icons` (192px + 512px), `theme_color`, `display: standalone`
- [ ] Service Worker com estratégia `NetworkFirst` para API calls, `CacheFirst` para assets estáticos
- [ ] App instalável via browser (ícone de instalação exibido)
- [ ] Offline: exibe dados em cache com banner "Modo offline — dados podem estar desatualizados"
- [ ] Lighthouse PWA score ≥ 90

### Referência no README
Badges do README (PWA-Ready)

---

## TASK-040 · Implementar internacionalização e acessibilidade base

**Épico:** E6 — Frontend  
**Prioridade:** 🟢 P3  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-034

### O que fazer
Garantir que a interface esteja em português e siga as diretrizes básicas de acessibilidade.

### Critérios de Aceite
- [ ] Todos os textos em pt-BR
- [ ] `lang="pt-BR"` no HTML
- [ ] Inputs com `aria-label` ou `<label>` associado
- [ ] Contraste mínimo WCAG AA (4.5:1) verificado com axe DevTools
- [ ] Navegação por teclado funcional nos formulários principais
- [ ] Lighthouse Accessibility score ≥ 85

---

---

# 🟠 E7 — TESTES & QUALIDADE

---

## TASK-041 · Configurar Testcontainers para testes de integração

**Épico:** E7 — Testes  
**Prioridade:** 🔴 P0  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-003, TASK-007

### O que fazer
Configurar o ambiente de testes de integração com Testcontainers usando PostgreSQL 16 real.

### Critérios de Aceite
- [ ] `@Testcontainers` configurado na classe base de testes de integração
- [ ] Container `postgres:16-alpine` iniciado para todos os testes com Procedures/triggers
- [ ] Flyway aplica todas as migrations no container de teste antes da execução
- [ ] Container RabbitMQ disponível para testes de mensageria
- [ ] **Zero** uso de H2 em qualquer teste de integração (ArchUnit valida isso)
- [ ] Tempo de startup do container < 30 segundos

### Referência no README
Restrição #4, ADR-06

---

## TASK-042 · Implementar testes de módulo com ArchUnit

**Épico:** E7 — Testes  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-015, TASK-016

### O que fazer
Implementar os testes de arquitetura que garantem que os bounded contexts não se violam.

### Critérios de Aceite
- [ ] `ModuleBoundaryTest` implementado com ArchUnit
- [ ] Regra: nenhuma classe em `financeiro.*` pode importar classes de `estoque.*` ou `rh.*`
- [ ] Regra: comunicação cross-módulo só via `ApplicationEvent`
- [ ] Regra: nenhum import de H2 em classes de teste de integração
- [ ] Regra: campos `@Masked` em todos os DTOs com campos PII
- [ ] Teste roda como gate na pipeline de CI (step 4 do CI/CD)

### Referência no README
ADR-01, Seção 9.2 (Step 4 do CI/CD)

---

## TASK-043 · Implementar testes de integração — fluxo completo de faturamento

**Épico:** E7 — Testes  
**Prioridade:** 🟠 P1  
**Estimativa:** 5h  
**Pré-requisitos:** TASK-041, TASK-030, TASK-017

### O que fazer
Implementar os testes de integração end-to-end cobrindo o fluxo completo de uma ordem do início ao fim.

### Critérios de Aceite
- [ ] Teste: criar ordem → status `PROCESSAMENTO_PENDENTE`
- [ ] Teste: simular callback do gateway → worker processa → status `CONCILIADO`
- [ ] Teste: simular divergência > R$0,50 → status `DIVERGENTE_AUDITORIA` + registro em `auditoria.alertas`
- [ ] Teste: retry do mesmo request (idempotência) → `HTTP 409` + nenhuma ordem duplicada no banco
- [ ] Cobertura ≥ 90% nos pacotes do módulo financeiro
- [ ] Cobertura ≥ 95% nas classes `IdempotencyInterceptor`, `GatewayPagamentoAdapter`, `ReconciliacaoWorker`

### Referência no README
Seção 4 (Plano de Testes), RNF (Cobertura ≥ 90%)

---

## TASK-044 · Configurar JaCoCo e gates de cobertura no Maven

**Épico:** E7 — Testes  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-043

### O que fazer
Configurar JaCoCo para mensurar cobertura e bloquear o build se ficar abaixo do mínimo.

### Critérios de Aceite
- [ ] Plugin JaCoCo configurado no `pom.xml`
- [ ] Gate de cobertura: `mvn verify` falha se cobertura geral < 90%
- [ ] Gate de cobertura: falha se pacotes críticos (`financeiro.service`, `financeiro.worker`) < 95%
- [ ] Relatório HTML gerado em `target/site/jacoco/`
- [ ] CI/CD publica relatório como artefato do build

### Referência no README
Badge de cobertura ≥90%, Seção 9.2 (Step 2 do CI)

---

## TASK-045 · Configurar script k6 de smoke test (performance)

**Épico:** E7 — Testes  
**Prioridade:** 🟡 P2  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-017

### O que fazer
Criar o script k6 de smoke test para validar performance antes de cada deploy.

### Critérios de Aceite
- [ ] Script em `scripts/k6/smoke-test.js`
- [ ] Cenário: 50 VUs, 60 segundos, endpoint `POST /api/v1/faturamento/ordens`
- [ ] Gate: falha se `p95 > 800ms`
- [ ] Gate: falha se `error_rate > 0.5%`
- [ ] Script parametrizável para ambiente (staging/prod)
- [ ] Roda no step 8 do CI/CD sem infraestrutura adicional (k6 via Docker)

### Referência no README
RNF-01, Seção 9.2 (Step 8 do CI)

---

## TASK-046 · Configurar SAST, CVE scan e secret scan no CI

**Épico:** E7 — Testes  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-003

### O que fazer
Configurar as ferramentas de segurança estática na pipeline de CI para garantir zero vulnerabilidades críticas.

### Critérios de Aceite
- [ ] Trivy configurado: `trivy fs --severity HIGH,CRITICAL --exit-code 1 .`
- [ ] OWASP Dependency Check: `mvn org.owasp:dependency-check-maven:check`
- [ ] TruffleHog: `trufflehog git file://. --since-commit HEAD~1 --fail`
- [ ] Qualquer vulnerabilidade HIGH ou CRITICAL bloqueia o merge
- [ ] Qualquer credencial detectada no código bloqueia o merge
- [ ] Runs nos steps 5 e 6 do CI/CD workflow

### Referência no README
Badge SAST-zero-critical, Seção 9.2 (Steps 5 e 6)

---

---

# 🟡 E8 — CI/CD & DEPLOY BLUE-GREEN

---

## TASK-047 · Criar workflow GitHub Actions (pipeline completa)

**Épico:** E8 — CI/CD  
**Prioridade:** 🟠 P1  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-044, TASK-045, TASK-046

### O que fazer
Criar o workflow completo do GitHub Actions com todos os 9 quality gates documentados no README.

### Critérios de Aceite
- [ ] Arquivo `.github/workflows/ci.yml` criado
- [ ] Steps em ordem: Build → Unit Tests (gate ≥90%) → Integration Tests → ArchUnit → SAST/CVE → Secret Scan → Flyway Validate → k6 Smoke → Docker Build
- [ ] Falha em qualquer step bloqueia o merge
- [ ] Imagem Docker multi-stage: JDK para build, JRE para runtime, tamanho final < 200MB
- [ ] Imagem tagueada com `$GITHUB_SHA` e publicada no registry
- [ ] Secrets do CI injetados via GitHub Secrets — nenhum hardcoded no YAML

### Referência no README
Seção 9.2 (Pipeline completa)

---

## TASK-048 · Criar Dockerfile multi-stage

**Épico:** E8 — CI/CD  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-003

### O que fazer
Criar o Dockerfile multi-stage otimizado para produção.

### Critérios de Aceite
- [ ] Stage 1 (build): `eclipse-temurin:21-jdk` — compila o JAR
- [ ] Stage 2 (runtime): `eclipse-temurin:21-jre-alpine` — apenas o JRE
- [ ] Usuário não-root criado e usado no stage de runtime
- [ ] Imagem final < 200MB verificado com `docker image ls`
- [ ] Health check configurado no Dockerfile: `HEALTHCHECK CMD curl -f http://localhost:8080/actuator/health`
- [ ] `.dockerignore` configurado para excluir `target/`, `.git/`, `node_modules/`

### Referência no README
Seção 9.2 (Step 9 do CI)

---

## TASK-049 · Configurar Blue-Green Deployment com Readiness Probes

**Épico:** E8 — CI/CD  
**Prioridade:** 🟡 P2  
**Estimativa:** 6h  
**Pré-requisitos:** TASK-048, TASK-006

### O que fazer
Implementar a estratégia de deploy Blue-Green com switch controlado de tráfego.

### Critérios de Aceite
- [ ] Readiness probe: `/actuator/health/readiness` retorna 200 quando DB ✓ + Redis ✓ + RabbitMQ ✓ + Flyway ✓
- [ ] Liveness probe: `/actuator/health/liveness`
- [ ] Pipeline de promoção implementa os 7 passos documentados na Seção 9.1
- [ ] Canary: 5% do tráfego para Green por 10 minutos antes de switch completo
- [ ] Rollback automático se `p95 > 800ms` ou `error_rate > 0.1%` durante o canary
- [ ] Blue fica de standby por 30 minutos após switch

### Referência no README
Seção 9.1

---

## TASK-050 · Implementar migrations retrocompatíveis (expand-contract)

**Épico:** E8 — CI/CD  
**Prioridade:** 🟠 P1  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-007, TASK-049

### O que fazer
Documentar e implementar o processo de expand-contract para mudanças destrutivas de schema.

### Critérios de Aceite
- [ ] `MIGRATIONS-GUIDE.md` criado documentando o padrão expand-contract
- [ ] Checklist de PR para migrations: [ ] NULLABLE ou DEFAULT? [ ] Sem DROP COLUMN no release? [ ] Sem NOT NULL sem expand-contract?
- [ ] Migration de exemplo demonstrando rename de coluna via expand-contract
- [ ] CI/CD valida checksums Flyway contra staging antes do deploy

### Referência no README
Seção 9.1 (Regra de compatibilidade de migrations)

---

## TASK-051 · Configurar health checks granulares no Actuator

**Épico:** E8 — CI/CD  
**Prioridade:** 🟠 P1  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-003

### O que fazer
Configurar health checks individuais para cada dependência crítica.

### Critérios de Aceite
- [ ] `GET /actuator/health` retorna status aggregado com detalhes de cada componente
- [ ] Componentes monitorados: `db` (PostgreSQL), `redis`, `rabbit` (RabbitMQ DLQ), `gatewayPix` (custom)
- [ ] Health check do Gateway PIX: verifica se o último ping teve sucesso em < 5 min
- [ ] `GET /actuator/health/circuit-breaker` expõe estado atual dos CBs (para o frontend)
- [ ] Actuator exposto apenas nas portas internas — não acessível externamente sem autenticação

### Referência no README
Seção 6 (Health checks granulares)

---

---

# 🟢 E9 — OBSERVABILIDADE & ALERTAS

---

## TASK-052 · Configurar OpenTelemetry e logging estruturado JSON

**Épico:** E9 — Observabilidade  
**Prioridade:** 🟠 P1  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-027

### O que fazer
Configurar instrumentação completa com OpenTelemetry para métricas, traces e logs estruturados.

### Critérios de Aceite
- [ ] `micrometer-registry-otlp` configurado exportando para coletor OTLP
- [ ] Todo log em formato JSON estruturado: `{timestamp, level, message, traceId, correlationId, spanId}`
- [ ] Métricas expostas: `http.server.request.duration` (histograma), `orders.created.total`, `reconciliation.duration`
- [ ] p95 de latência mensurável via métrica `http.server.request.duration.p95`
- [ ] `traceId` e `spanId` do OpenTelemetry propagados automaticamente no MDC

### Referência no README
Seção 6 (Observabilidade), RNF-01

---

## TASK-053 · Configurar dashboard Grafana base

**Épico:** E9 — Observabilidade  
**Prioridade:** 🟢 P3  
**Estimativa:** 4h  
**Pré-requisitos:** TASK-052

### O que fazer
Criar dashboard Grafana com os painéis essenciais para monitoramento operacional.

### Critérios de Aceite
- [ ] Dashboard com painéis: Latência p95 (último 1h), Taxa de Erros (%), Ordens por Status, DLQ size, Circuit Breaker status
- [ ] Alertas configurados: p95 > 800ms, error_rate > 1%, DLQ > 100 mensagens
- [ ] Dashboard exportado como JSON em `infra/grafana/dashboards/`
- [ ] Provisionado automaticamente via Terraform/Docker Compose

---

## TASK-054 · Implementar endpoint de diagnóstico de integridade (API)

**Épico:** E9 — Observabilidade  
**Prioridade:** 🟡 P2  
**Estimativa:** 2h  
**Pré-requisitos:** TASK-010, TASK-026

### O que fazer
Expor a função `fn_check_integrity` via API REST para uso pelo time de suporte sem acesso direto ao banco.

### Critérios de Aceite
- [ ] `GET /api/v1/auditoria/ordens/{idempotencyKey}/integrity` implementado
- [ ] Requer role CONTROLLER
- [ ] Chama `fn_check_integrity(idempotencyKey)` e retorna resultado como JSON
- [ ] Campos: todas as versões históricas, `emLimbo`, `minutosLimbo`, máquina de estados percorrida
- [ ] Rate limiting específico: máximo 10 req/min para este endpoint

### Referência no README
RF-04 (AC-04.3)

---

## TASK-055 · Criar documentação OpenAPI e Postman Collection

**Épico:** E9 — Observabilidade  
**Prioridade:** 🟢 P3  
**Estimativa:** 3h  
**Pré-requisitos:** TASK-017, TASK-020, TASK-023

### O que fazer
Gerar documentação completa da API e disponibilizar collection do Postman com exemplos funcionais.

### Critérios de Aceite
- [ ] `springdoc-openapi-starter-webmvc-ui` adicionado ao `pom.xml`
- [ ] Swagger UI disponível em `/api/docs` em ambientes não-prod
- [ ] Todos os endpoints documentados com: descrição, parâmetros, responses (200/201/202/400/401/403/409/422/429/503)
- [ ] Exemplos de request/response nos endpoints principais (faturamento, webhook, auditoria)
- [ ] Postman Collection exportada em `docs/postman/SincronizaMEI.postman_collection.json`
- [ ] Collection inclui variáveis de ambiente para dev e staging

### Referência no README
Seção 7 (API-First)

---

---

## 📋 ORDEM DE EXECUÇÃO RECOMENDADA (Para o Dev Júnior)

> Envie as tasks nesta sequência. Cada task só começa quando a anterior estiver **Done** e revisada.

| Sprint | Tasks | Foco |
|---|---|---|
| Sprint 1 (Semana 1-2) | TASK-001 → 006 | Ambiente e infraestrutura base |
| Sprint 2 (Semana 3-4) | TASK-007 → 013 | Banco de dados e schema bitemporal |
| Sprint 3 (Semana 5-6) | TASK-014 → 019 + TASK-041 | Backend core + testes de integração |
| Sprint 4 (Semana 7) | TASK-020 → 023 + TASK-024 → 026 | Webhooks + Segurança LGPD |
| Sprint 5 (Semana 8) | TASK-027 → 033 | Mensageria e workers |
| Sprint 6 (Semana 9-10) | TASK-034 → 040 | Frontend React PWA |
| Sprint 7 (Semana 11) | TASK-042 → 051 | Testes, qualidade e CI/CD |
| Sprint 8 (Semana 12) | TASK-052 → 055 | Observabilidade e documentação |

---

## 🚫 CHECKLIST DE ANTI-PATTERNS (Para revisar em todo PR)

Antes de aprovar qualquer PR, verificar:

- [ ] `repository.save()` em entidades bitemporais? → **REJEITAR** (usar `CALL sp_*`)
- [ ] Import cross-módulo (ex: `financeiro` importando `estoque`)? → **REJEITAR**
- [ ] H2 em testes de integração? → **REJEITAR**
- [ ] CPF/e-mail sem `@Masked` em DTO de log? → **REJEITAR**
- [ ] Credencial hardcoded em qualquer arquivo? → **REJEITAR**
- [ ] `Thread.sleep()` em teste de concorrência? → **REJEITAR**
- [ ] Query com `OFFSET` em tabela grande? → **REJEITAR**
- [ ] Lógica de negócio no React? → **REJEITAR**
- [ ] Event listener síncrono bloqueante? → **REJEITAR**

---

*Plano gerado por: Gerente de Projeto / Arquiteto Sênior*  
*Projeto: SincronizaMEI v1.1.0 — Kalyel Nunes Laurindo*  
*Total: 55 tasks · 8 épicos · ~12 semanas de desenvolvimento*
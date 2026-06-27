# **📋 Agile Backlog & Task Management: SincronizaMEI**

**Role:** Agile Coach / Tech Lead / Project Manager

**Objective:** Maintain a prioritizable backlog of atomic, SMART tasks, tracking their progress across a basic Markdown Kanban board from planning to verification.

**Context:** SincronizaMEI — Modular monolithic ERP designed with Project Loom Virtual Threads, Bitemporal PostgreSQL persistence, and Redis-backed HTTP idempotency, implementing a dual-UX dashboard for MEI operational profiles and auditor/controller profiles.

## **🏛️ Backlog Metadata**

* **Project Owner:** Kalyel N. Laurindo / Project Owner  
* **Lead Tech Lead:** Kalyel N. Laurindo / Software Engineer  
* **Current Sprint / Iteration:** Sprint 1  
* **Target Delivery Date:** TBD (Incremental delivery every 2 weeks)  
* **Document Version:** v1.0

---

## **1. 📊 Prioritization & Task Sizing Framework**

*   **Field 1.0 - Prioritization & Estimation Framework:** RICE Score + Fibonacci Story Points. Technical dependencies take precedence in conflicts.

### **1.1. RICE Score Calculation Formula**

RICE = (Reach * Impact * Confidence) / Effort

* **Reach:** Scaled from 1 to 10 based on system layers affected.
* **Impact:** Contribution to product vision (3 = Massive, 2 = High, 1 = Medium, 0.5 = Low).
* **Confidence:** Certainty of estimates (1 = High/100%, 0.8 = Medium/80%, 0.5 = Low/50%).
* **Effort:** Story points (1, 2, 3, 5, 8, 13, 21).

---

## **2. 🗂️ Prioritized Product Backlog Ledger**

### **📦 Backlog Phase 1: Backing Infrastructure & Configuration Setup**

* **[[TSK-01](TSK-01.md)]: Initialize Git Repository**  
  * *Epic/Requirement Link:* INFRA-01  
  * *Estimation/Priority:* SP: 1 | RICE: (1 * 0.5 * 1.0) / 1 = 0.5  
  * *TDD Test File:* N/A  
  * *Status:* Done  

* **[[TSK-02](TSK-02.md)]: Configure .gitignore Rules**  
  * *Epic/Requirement Link:* INFRA-01  
  * *Estimation/Priority:* SP: 1 | RICE: (1 * 0.5 * 1.0) / 1 = 0.5  
  * *TDD Test File:* N/A  
  * *Status:* Done  

* **[[TSK-03](TSK-03.md)]: Deploy local claude.md context file**  
  * *Epic/Requirement Link:* INFRA-01  
  * *Estimation/Priority:* SP: 1 | RICE: (1 * 0.5 * 1.0) / 1 = 0.5  
  * *TDD Test File:* N/A  
  * *Status:* To Do  

* **[[TSK-04](TSK-04.md)]: Setup multi-module pom.xml configuration**  
  * *Epic/Requirement Link:* INFRA-02  
  * *Estimation/Priority:* SP: 2 | RICE: (4 * 1.0 * 1.0) / 2 = 2.0  
  * *TDD Test File:* N/A  
  * *Status:* To Do  

* **[[TSK-05](TSK-05.md)]: Enable Spring Boot Virtual Threads configuration**  
  * *Epic/Requirement Link:* RP-01  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 0.8) / 2 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.config.ThreadConfigTest`  
  * *Status:* To Do  

* **[[TSK-06](TSK-06.md)]: Setup Docker Compose with PostgreSQL 16 container**  
  * *Epic/Requirement Link:* INFRA-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-07](TSK-07.md)]: Setup Docker Compose with Redis 7.2 container**  
  * *Epic/Requirement Link:* INFRA-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-08](TSK-08.md)]: Setup Docker Compose with RabbitMQ 3.13 container**  
  * *Epic/Requirement Link:* INFRA-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-09](TSK-09.md)]: Initialize local .env configuration variables**  
  * *Epic/Requirement Link:* INFRA-04  
  * *Estimation/Priority:* SP: 1 | RICE: (5 * 1.0 * 1.0) / 1 = 5.0  
  * *Status:* To Do  

* **[[TSK-10](TSK-10.md)]: Configure HashiCorp Vault local integrations**  
  * *Epic/Requirement Link:* SEC-01  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 3.0 * 0.8) / 3 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.config.VaultConfigTest`  
  * *Status:* To Do  

* **[[TSK-11](TSK-11.md)]: Setup spring-boot-starter-actuator dependencies**  
  * *Epic/Requirement Link:* OBS-01  
  * *Estimation/Priority:* SP: 1 | RICE: (8 * 1.0 * 1.0) / 1 = 8.0  
  * *Status:* To Do  

* **[[TSK-12](TSK-12.md)]: Configure Logback JSON layout logger**  
  * *Epic/Requirement Link:* OBS-02  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 1.0 * 1.0) / 2 = 5.0  
  * *Status:* To Do  

* **[[TSK-13](TSK-13.md)]: Configure local Flyway database migrations base pom plugin**  
  * *Epic/Requirement Link:* DB-01  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-14](TSK-14.md)]: Setup ArchUnit boundary tests framework**  
  * *Epic/Requirement Link:* ARCH-ENABLER  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *TDD Test File:* `br.com.sincronizamei.architecture.ArchUnitTest`  
  * *Status:* To Do  

* **[[TSK-15](TSK-15.md)]: Create project base exception templates**  
  * *Epic/Requirement Link:* CORE-01  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 1.0 * 1.0) / 2 = 4.0  
  * *TDD Test File:* `br.com.sincronizamei.domain.exception.DomainExceptionTest`  
  * *Status:* To Do  

### **⚙️ Backlog Phase 2: Database & Persistence Schema**

* **[[TSK-16](TSK-16.md)]: Setup Flyway DB migration folders structure**  
  * *Epic/Requirement Link:* DB-01  
  * *Estimation/Priority:* SP: 1 | RICE: (8 * 2.0 * 1.0) / 1 = 16.0  
  * *Status:* To Do  

* **[[TSK-17](TSK-17.md)]: Write V1 Flyway migration for financeiro.ordens table**  
  * *Epic/Requirement Link:* DB-02  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.db.MigrationV1Test`  
  * *Status:* To Do  

* **[[TSK-18](TSK-18.md)]: Write V2 Flyway migration for estoque table**  
  * *Epic/Requirement Link:* DB-03  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 1.0) / 3 = 5.3  
  * *TDD Test File:* `br.com.sincronizamei.db.MigrationV2Test`  
  * *Status:* To Do  

* **[[TSK-19](TSK-19.md)]: Write V3 Flyway migration for rh table**  
  * *Epic/Requirement Link:* DB-04  
  * *Estimation/Priority:* SP: 3 | RICE: (5 * 1.0 * 1.0) / 3 = 1.6  
  * *TDD Test File:* `br.com.sincronizamei.db.MigrationV3Test`  
  * *Status:* To Do  

* **[[TSK-20](TSK-20.md)]: Create V4 Flyway migration for auditoria.logs_erro table**  
  * *Epic/Requirement Link:* DB-05  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.db.MigrationV4Test`  
  * *Status:* To Do  

* **[[TSK-21](TSK-21.md)]: Implement physical delete prevention trigger function**  
  * *Epic/Requirement Link:* DB-06  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.db.TriggerBlockDeleteTest`  
  * *Status:* To Do  

* **[[TSK-22](TSK-22.md)]: Implement financeiro.sp_reconciliar_ordem procedure**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `br.com.sincronizamei.db.SpReconciliarOrdemTest`  
  * *Status:* To Do  

* **[[TSK-23](TSK-23.md)]: Implement financeiro.fn_check_integrity function**  
  * *Epic/Requirement Link:* RF-07  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.db.FnCheckIntegrityTest`  
  * *Status:* To Do  

* **[[TSK-24](TSK-24.md)]: Implement financeiro.fn_estado_bitemporal function**  
  * *Epic/Requirement Link:* RF-04  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.db.FnEstadoBitemporalTest`  
  * *Status:* To Do  

* **[[TSK-25](TSK-25.md)]: Create partial index idx_ordens_status_pendente**  
  * *Epic/Requirement Link:* DB-PERF  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-26](TSK-26.md)]: Create partial index idx_ordens_idempotency**  
  * *Epic/Requirement Link:* DB-PERF  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-27](TSK-27.md)]: Configure testcontainers database boot configurations**  
  * *Epic/Requirement Link:* TEST-01  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.test.TestcontainersConfigTest`  
  * *Status:* To Do  

* **[[TSK-28](TSK-28.md)]: Write integration test validating trigger blockage**  
  * *Epic/Requirement Link:* TEST-02  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *TDD Test File:* `br.com.sincronizamei.db.TriggerBlockDeleteTest`  
  * *Status:* To Do  

* **[[TSK-29](TSK-29.md)]: Write integration test validating sp_reconciliar_ordem rollback**  
  * *Epic/Requirement Link:* TEST-02  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.db.SpReconciliarOrdemTest`  
  * *Status:* To Do  

* **[[TSK-30](TSK-30.md)]: Implement database clean migrations validation in pipeline**  
  * *Epic/Requirement Link:* CI-01  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

### **📦 Backlog Phase 3: Bounded Domain Context & Core Models**

* **[[TSK-31](TSK-31.md)]: Initialize financeiro domain package boundary**  
  * *Epic/Requirement Link:* ARCH-01  
  * *Estimation/Priority:* SP: 1 | RICE: (10 * 3.0 * 1.0) / 1 = 30.0  
  * *Status:* To Do  

* **[[TSK-32](TSK-32.md)]: Code Money value object in financeiro domain**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.domain.MoneyTest`  
  * *Status:* To Do  

* **[[TSK-33](TSK-33.md)]: Code Ordem domain root aggregate**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.domain.OrdemTest`  
  * *Status:* To Do  

* **[[TSK-34](TSK-34.md)]: Code Cpf value object with AES encryption capability**  
  * *Epic/Requirement Link:* RNF-05  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.domain.CpfTest`  
  * *Status:* To Do  

* **[[TSK-35](TSK-35.md)]: Initialize estoque domain package boundary**  
  * *Epic/Requirement Link:* ARCH-01  
  * *Estimation/Priority:* SP: 1 | RICE: (8 * 2.0 * 1.0) / 1 = 16.0  
  * *Status:* To Do  

* **[[TSK-36](TSK-36.md)]: Code EstoqueItem domain entity**  
  * *Epic/Requirement Link:* RF-08  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.estoque.domain.EstoqueItemTest`  
  * *Status:* To Do  

* **[[TSK-37](TSK-37.md)]: Initialize rh domain package boundary**  
  * *Epic/Requirement Link:* ARCH-01  
  * *Estimation/Priority:* SP: 1 | RICE: (5 * 1.0 * 1.0) / 1 = 5.0  
  * *Status:* To Do  

* **[[TSK-38](TSK-38.md)]: Code Colaborador domain entity**  
  * *Epic/Requirement Link:* RF-09  
  * *Estimation/Priority:* SP: 2 | RICE: (5 * 1.0 * 1.0) / 2 = 2.5  
  * *TDD Test File:* `br.com.sincronizamei.modules.rh.domain.ColaboradorTest`  
  * *Status:* To Do  

* **[[TSK-39](TSK-39.md)]: Define DomainEvent abstract records**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-40](TSK-40.md)]: Create OrdemCriadaEvent domain event**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 1 | RICE: (10 * 3.0 * 1.0) / 1 = 30.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.domain.OrdemCriadaEventTest`  
  * *Status:* To Do  

* **[[TSK-41](TSK-41.md)]: Create OrdemReconciliadaEvent domain event**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 1 | RICE: (10 * 3.0 * 1.0) / 1 = 30.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.domain.OrdemReconciliadaEventTest`  
  * *Status:* To Do  

* **[[TSK-42](TSK-42.md)]: Define interface port OrdemRepositoryPort**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-43](TSK-43.md)]: Define interface port EstoqueRepositoryPort**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-44](TSK-44.md)]: Define interface port ColaboradorRepositoryPort**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 2 | RICE: (5 * 1.0 * 1.0) / 2 = 2.5  
  * *Status:* To Do  

* **[[TSK-45](TSK-45.md)]: Code CreateOrdemUseCase boundaries and implementation**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.application.CreateOrdemUseCaseTest`  
  * *Status:* To Do  

* **[[TSK-46](TSK-46.md)]: Code ReconcileOrdemUseCase boundaries and implementation**  
  * *Epic/Requirement Link:* RF-07  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.application.ReconcileOrdemUseCaseTest`  
  * *Status:* To Do  

* **[[TSK-47](TSK-47.md)]: Code ReservaEstoqueUseCase boundaries and implementation**  
  * *Epic/Requirement Link:* RF-08  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.modules.estoque.application.ReservaEstoqueUseCaseTest`  
  * *Status:* To Do  

* **[[TSK-48](TSK-48.md)]: Code AdmitirColaboradorUseCase boundaries and implementation**  
  * *Epic/Requirement Link:* RF-09  
  * *Estimation/Priority:* SP: 3 | RICE: (5 * 1.0 * 0.8) / 3 = 1.3  
  * *TDD Test File:* `br.com.sincronizamei.modules.rh.application.AdmitirColaboradorUseCaseTest`  
  * *Status:* To Do  

* **[[TSK-49](TSK-49.md)]: Setup ArchUnit tests enforcing pure domain models**  
  * *Epic/Requirement Link:* ARCH-ENABLER  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *TDD Test File:* `br.com.sincronizamei.architecture.DomainPurityTest`  
  * *Status:* To Do  

* **[[TSK-50](TSK-50.md)]: Create domain validations framework for inputs**  
  * *Epic/Requirement Link:* CORE-01  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 2.0 * 1.0) / 2 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.domain.ValidationEngineTest`  
  * *Status:* To Do  

### **⚙️ Backlog Phase 4: Interface Adapters & Persistence Adapters**

* **[[TSK-51](TSK-51.md)]: Setup PgOrdemRepositoryAdapter with bitemporal maps**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.infra.PgOrdemRepositoryAdapterTest`  
  * *Status:* To Do  

* **[[TSK-52](TSK-52.md)]: Setup PgEstoqueRepositoryAdapter mapping**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 1.0) / 3 = 5.3  
  * *TDD Test File:* `br.com.sincronizamei.modules.estoque.infra.PgEstoqueRepositoryAdapterTest`  
  * *Status:* To Do  

* **[[TSK-53](TSK-53.md)]: Setup PgColaboradorRepositoryAdapter mapping**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 3 | RICE: (5 * 1.0 * 1.0) / 3 = 1.6  
  * *TDD Test File:* `br.com.sincronizamei.modules.rh.infra.PgColaboradorRepositoryAdapterTest`  
  * *Status:* To Do  

* **[[TSK-54](TSK-54.md)]: Implement AesGcmEncryptedConverter for JPA entities**  
  * *Epic/Requirement Link:* RNF-05  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.security.AesGcmConverterTest`  
  * *Status:* To Do  

* **[[TSK-55](TSK-55.md)]: Create custom @Masked annotation**  
  * *Epic/Requirement Link:* RNF-06  
  * *Estimation/Priority:* SP: 1 | RICE: (10 * 3.0 * 1.0) / 1 = 30.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.logging.MaskedAnnotationTest`  
  * *Status:* To Do  

* **[[TSK-56](TSK-56.md)]: Build MaskedLoggingFilter utilizing Logback**  
  * *Epic/Requirement Link:* RNF-06  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.logging.MaskedLoggingFilterTest`  
  * *Status:* To Do  

* **[[TSK-57](TSK-57.md)]: Create CorrelationIdInterceptor filter**  
  * *Epic/Requirement Link:* OBS-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *TDD Test File:* `br.com.sincronizamei.api.interceptors.CorrelationIdInterceptorTest`  
  * *Status:* To Do  

* **[[TSK-58](TSK-58.md)]: Code Redis-backed IdempotencyInterceptor filter**  
  * *Epic/Requirement Link:* RNF-03  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `br.com.sincronizamei.api.interceptors.IdempotencyInterceptorTest`  
  * *Status:* To Do  

* **[[TSK-59](TSK-59.md)]: Implement FaturamentoController POST endpoint**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.FaturamentoControllerTest`  
  * *Status:* To Do  

* **[[TSK-60](TSK-60.md)]: Implement FaturamentoController GET status endpoint**  
  * *Epic/Requirement Link:* RF-04  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.FaturamentoControllerTest`  
  * *Status:* To Do  

* **[[TSK-61](TSK-61.md)]: Code HookRegistry component**  
  * *Epic/Requirement Link:* RF-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.HookRegistryTest`  
  * *Status:* To Do  

* **[[TSK-62](TSK-62.md)]: Code HookRegistry listener dispatch engine**  
  * *Epic/Requirement Link:* RF-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.events.HookListenerTest`  
  * *Status:* To Do  

* **[[TSK-63](TSK-63.md)]: Implement WebhookSignatureValidator checker**  
  * *Epic/Requirement Link:* SEC-02  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 3.0 * 0.8) / 3 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.infra.security.WebhookSignatureValidatorTest`  
  * *Status:* To Do  

* **[[TSK-64](TSK-64.md)]: Build Outbound API Gateway Pagamento ACL Adapter**  
  * *Epic/Requirement Link:* RF-01  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `br.com.sincronizamei.modules.financeiro.infra.GatewayPagamentoAclAdapterTest`  
  * *Status:* To Do  

* **[[TSK-65](TSK-65.md)]: Create Spring Event Publisher dispatch handler**  
  * *Epic/Requirement Link:* ARCH-HEX  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.events.EventPublisherTest`  
  * *Status:* To Do  

* **[[TSK-66](TSK-66.md)]: Setup transactional event listener for estoque reservation**  
  * *Epic/Requirement Link:* RF-08  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.modules.estoque.infra.EstoqueEventListenerTest`  
  * *Status:* To Do  

* **[[TSK-67](TSK-67.md)]: Configure RabbitMQ Connection Factory**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-68](TSK-68.md)]: Define RabbitMQ billing queue and exchange schema**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.messaging.RabbitSchemaTest`  
  * *Status:* To Do  

* **[[TSK-69](TSK-69.md)]: Implement RabbitMQ billing listener publisher**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.infra.messaging.BillingListenerTest`  
  * *Status:* To Do  

* **[[TSK-70](TSK-70.md)]: Setup RabbitMQ Dead Letter Exchange (DLX) retry configuration**  
  * *Epic/Requirement Link:* ARCH-EDA  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 3.0 * 0.8) / 3 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.infra.messaging.RabbitDlxRetryTest`  
  * *Status:* To Do  

### **📦 Backlog Phase 5: Diagnostics, Observability & Hardening**

* **[[TSK-71](TSK-71.md)]: Configure Quartz Scheduler properties**  
  * *Epic/Requirement Link:* OBS-04  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-72](TSK-72.md)]: Implement Quartz job for transaction reconciliation**  
  * *Epic/Requirement Link:* RF-07  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.reconciliacao.ReconciliationJobTest`  
  * *Status:* To Do  

* **[[TSK-73](TSK-73.md)]: Implement ReconciliationWorker running on Loom runner**  
  * *Epic/Requirement Link:* RP-01  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `br.com.sincronizamei.reconciliacao.ReconciliationWorkerTest`  
  * *Status:* To Do  

* **[[TSK-74](TSK-74.md)]: Setup Micrometer Prometheus metrics registry**  
  * *Epic/Requirement Link:* OBS-05  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *Status:* To Do  

* **[[TSK-75](TSK-75.md)]: Expose ordens_em_limbo_ratio custom Gauge**  
  * *Epic/Requirement Link:* OBS-05  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.infra.metrics.ReconciliacaoMetricsTest`  
  * *Status:* To Do  

* **[[TSK-76](TSK-76.md)]: Expose reconciliacao_tempo_p95 custom Histogram**  
  * *Epic/Requirement Link:* OBS-05  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 0.8) / 3 = 4.2  
  * *TDD Test File:* `br.com.sincronizamei.infra.metrics.ReconciliacaoMetricsTest`  
  * *Status:* To Do  

* **[[TSK-77](TSK-77.md)]: Integrate OpenTelemetry tracer instrumentation exporter**  
  * *Epic/Requirement Link:* OBS-06  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *Status:* To Do  

* **[[TSK-78](TSK-78.md)]: Implement Admin endpoints for manual job triggers**  
  * *Epic/Requirement Link:* RF-07  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 1.0) / 3 = 5.3  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.AdminJobControllerTest`  
  * *Status:* To Do  

* **[[TSK-79](TSK-79.md)]: Implement DLQ replay utility REST Endpoint**  
  * *Epic/Requirement Link:* RF-07  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 1.0) / 3 = 5.3  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.AdminDlqControllerTest`  
  * *Status:* To Do  

* **[[TSK-80](TSK-80.md)]: Add Spring Security configuration for REST APIs**  
  * *Epic/Requirement Link:* SEC-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.config.SecurityConfigTest`  
  * *Status:* To Do  

* **[[TSK-81](TSK-81.md)]: Setup JWT token validation filters**  
  * *Epic/Requirement Link:* SEC-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.api.filters.JwtValidationFilterTest`  
  * *Status:* To Do  

* **[[TSK-82](TSK-82.md)]: Configure Spring Boot Actuator security permissions**  
  * *Epic/Requirement Link:* SEC-03  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 1.0 * 1.0) / 2 = 4.0  
  * *Status:* To Do  

* **[[TSK-83](TSK-83.md)]: Implement global exception handler controller advice**  
  * *Epic/Requirement Link:* CORE-01  
  * *Estimation/Priority:* SP: 2 | RICE: (8 * 2.0 * 1.0) / 2 = 8.0  
  * *TDD Test File:* `br.com.sincronizamei.api.controllers.GlobalExceptionHandlerTest`  
  * *Status:* To Do  

* **[[TSK-84](TSK-84.md)]: Build resilience4j circuit breakers on gateway ACL**  
  * *Epic/Requirement Link:* RNF-04  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 3.0 * 0.8) / 3 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.infra.resilience.GatewayCircuitBreakerTest`  
  * *Status:* To Do  

* **[[TSK-85](TSK-85.md)]: Build resilience4j rate limiters on webhook endpoints**  
  * *Epic/Requirement Link:* RNF-04  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 3.0 * 0.8) / 3 = 6.4  
  * *TDD Test File:* `br.com.sincronizamei.infra.resilience.WebhookRateLimiterTest`  
  * *Status:* To Do  

### **⚙️ Backlog Phase 6: Frontend Dual-UX (MEI & Controller), Stores & Setup**

* **[[TSK-86](TSK-86.md)]: Setup react-router-dom base routing schema**  
  * *Epic/Requirement Link:* UI-01  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-87](TSK-87.md)]: Import Outfit and JetBrains Mono fonts config**  
  * *Epic/Requirement Link:* UI-01  
  * *Estimation/Priority:* SP: 1 | RICE: (10 * 1.0 * 1.0) / 1 = 10.0  
  * *Status:* To Do  

* **[[TSK-88](TSK-88.md)]: Define Design System tokens in tailwind.config.js**  
  * *Epic/Requirement Link:* UI-01  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 2.0 * 1.0) / 2 = 10.0  
  * *Status:* To Do  

* **[[TSK-89](TSK-89.md)]: Build BaseLayout component (Glassmorphic background)**  
  * *Epic/Requirement Link:* UI-02  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 2.0 * 0.8) / 2 = 8.0  
  * *TDD Test File:* `frontend/src/components/BaseLayout.test.tsx`  
  * *Status:* To Do  

* **[[TSK-90](TSK-90.md)]: Create Zustand state store for User Sessions**  
  * *Epic/Requirement Link:* UI-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 2.0 * 1.0) / 2 = 10.0  
  * *TDD Test File:* `frontend/src/store/userStore.test.ts`  
  * *Status:* To Do  

* **[[TSK-91](TSK-91.md)]: Create Zustand state store for Financial Orders**  
  * *Epic/Requirement Link:* UI-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *TDD Test File:* `frontend/src/store/orderStore.test.ts`  
  * *Status:* To Do  

* **[[TSK-92](TSK-92.md)]: Implement useIdempotentMutation hook**  
  * *Epic/Requirement Link:* RNF-03  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `frontend/src/hooks/useIdempotentMutation.test.ts`  
  * *Status:* To Do  

* **[[TSK-93](TSK-93.md)]: Build Login screen with authentication handlers**  
  * *Epic/Requirement Link:* UI-04  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 0.8) / 3 = 8.0  
  * *TDD Test File:* `frontend/src/features/auth/Login.test.tsx`  
  * *Status:* To Do  

* **[[TSK-94](TSK-94.md)]: Build MEI Invoicing Dashboard view**  
  * *Epic/Requirement Link:* UI-04  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `frontend/src/features/mei/InvoicingDashboard.test.tsx`  
  * *Status:* To Do  

* **[[TSK-95](TSK-95.md)]: Build Auditor/Controller Reconciliation Dashboard view**  
  * *Epic/Requirement Link:* UI-04  
  * *Estimation/Priority:* SP: 5 | RICE: (10 * 3.0 * 0.8) / 5 = 4.8  
  * *TDD Test File:* `frontend/src/features/auditor/ReconciliationDashboard.test.tsx`  
  * *Status:* To Do  

* **[[TSK-96](TSK-96.md)]: Build Audit Logs data-table with JetBrains Mono font**  
  * *Epic/Requirement Link:* UI-02  
  * *Estimation/Priority:* SP: 3 | RICE: (8 * 2.0 * 1.0) / 3 = 5.3  
  * *TDD Test File:* `frontend/src/features/auditor/AuditLogsTable.test.tsx`  
  * *Status:* To Do  

* **[[TSK-97](TSK-97.md)]: Add Vite PWA configuration and service worker registers**  
  * *Epic/Requirement Link:* RNF-01  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 2.0 * 0.8) / 3 = 5.3  
  * *Status:* To Do  

* **[[TSK-98](TSK-98.md)]: Setup Vitest testing environment runner**  
  * *Epic/Requirement Link:* TEST-03  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

* **[[TSK-99](TSK-99.md)]: Setup GitHub Actions CI/CD workflows configuration**  
  * *Epic/Requirement Link:* CI-02  
  * *Estimation/Priority:* SP: 3 | RICE: (10 * 3.0 * 1.0) / 3 = 10.0  
  * *Status:* To Do  

* **[[TSK-100](TSK-100.md)]: Setup proprietary LICENSE & verify full production builds**  
  * *Epic/Requirement Link:* INFRA-05  
  * *Estimation/Priority:* SP: 2 | RICE: (10 * 3.0 * 1.0) / 2 = 15.0  
  * *Status:* To Do  

---

## **3. 📋 Basic Markdown Kanban Board**

### **🔴 To Do (Ready for Development)**

* [ ] **[[TSK-03](TSK-03.md)]:** Deploy local claude.md context file
* [ ] **[[TSK-04](TSK-04.md)]:** Setup multi-module pom.xml configuration
* [ ] **[[TSK-05](TSK-05.md)]:** Enable Spring Boot Virtual Threads configuration
* [ ] **[[TSK-06](TSK-06.md)]:** Setup Docker Compose with PostgreSQL 16 container
* [ ] **[[TSK-07](TSK-07.md)]:** Setup Docker Compose with Redis 7.2 container
* [ ] **[[TSK-08](TSK-08.md)]:** Setup Docker Compose with RabbitMQ 3.13 container
* [ ] **[[TSK-09](TSK-09.md)]:** Initialize local .env configuration variables
* [ ] **[[TSK-10](TSK-10.md)]:** Configure HashiCorp Vault local integrations
* [ ] **[[TSK-11](TSK-11.md)]:** Setup spring-boot-starter-actuator dependencies
* [ ] **[[TSK-12](TSK-12.md)]:** Configure Logback JSON layout logger
* [ ] **[[TSK-13](TSK-13.md)]:** Configure local Flyway database migrations base pom plugin
* [ ] **[[TSK-14](TSK-14.md)]:** Setup ArchUnit boundary tests framework
* [ ] **[[TSK-15](TSK-15.md)]:** Create project base exception templates
* [ ] **[[TSK-16](TSK-16.md)]:** Setup Flyway DB migration folders structure
* [ ] **[[TSK-17](TSK-17.md)]:** Write V1 Flyway migration for financeiro.ordens table
* [ ] **[[TSK-18](TSK-18.md)]:** Write V2 Flyway migration for estoque table
* [ ] **[[TSK-19](TSK-19.md)]:** Write V3 Flyway migration for rh table
* [ ] **[[TSK-20](TSK-20.md)]:** Create V4 Flyway migration for auditoria.logs_erro table
* [ ] **[[TSK-21](TSK-21.md)]:** Implement physical delete prevention trigger function
* [ ] **[[TSK-22](TSK-22.md)]:** Implement financeiro.sp_reconciliar_ordem procedure
* [ ] **[[TSK-23](TSK-23.md)]:** Implement financeiro.fn_check_integrity function
* [ ] **[[TSK-24](TSK-24.md)]:** Implement financeiro.fn_estado_bitemporal function
* [ ] **[[TSK-25](TSK-25.md)]:** Create partial index idx_ordens_status_pendente
* [ ] **[[TSK-26](TSK-26.md)]:** Create partial index idx_ordens_idempotency
* [ ] **[[TSK-27](TSK-27.md)]:** Configure testcontainers database boot configurations
* [ ] **[[TSK-28](TSK-28.md)]:** Write integration test validating trigger blockage
* [ ] **[[TSK-29](TSK-29.md)]:** Write integration test validating sp_reconciliar_ordem rollback
* [ ] **[[TSK-30](TSK-30.md)]:** Implement database clean migrations validation in pipeline
* [ ] **[[TSK-31](TSK-31.md)]:** Initialize financeiro domain package boundary
* [ ] **[[TSK-32](TSK-32.md)]:** Code Money value object in financeiro domain
* [ ] **[[TSK-33](TSK-33.md)]:** Code Ordem domain root aggregate
* [ ] **[[TSK-34](TSK-34.md)]:** Code Cpf value object with AES encryption capability
* [ ] **[[TSK-35](TSK-35.md)]:** Initialize estoque domain package boundary
* [ ] **[[TSK-36](TSK-36.md)]:** Code EstoqueItem domain entity
* [ ] **[[TSK-37](TSK-37.md)]:** Initialize rh domain package boundary
* [ ] **[[TSK-38](TSK-38.md)]:** Code Colaborador domain entity
* [ ] **[[TSK-39](TSK-39.md)]:** Define DomainEvent abstract records
* [ ] **[[TSK-40](TSK-40.md)]:** Create OrdemCriadaEvent domain event
* [ ] **[[TSK-41](TSK-41.md)]:** Create OrdemReconciliadaEvent domain event
* [ ] **[[TSK-42](TSK-42.md)]:** Define interface port OrdemRepositoryPort
* [ ] **[[TSK-43](TSK-43.md)]:** Define interface port EstoqueRepositoryPort
* [ ] **[[TSK-44](TSK-44.md)]:** Define interface port ColaboradorRepositoryPort
* [ ] **[[TSK-45](TSK-45.md)]:** Code CreateOrdemUseCase boundaries and implementation
* [ ] **[[TSK-46](TSK-46.md)]:** Code ReconcileOrdemUseCase boundaries and implementation
* [ ] **[[TSK-47](TSK-47.md)]:** Code ReservaEstoqueUseCase boundaries and implementation
* [ ] **[[TSK-48](TSK-48.md)]:** Code AdmitirColaboradorUseCase boundaries and implementation
* [ ] **[[TSK-49](TSK-49.md)]:** Setup ArchUnit tests enforcing pure domain models
* [ ] **[[TSK-50](TSK-50.md)]:** Create domain validations framework for inputs
* [ ] **[[TSK-51](TSK-51.md)]:** Setup PgOrdemRepositoryAdapter with bitemporal maps
* [ ] **[[TSK-52](TSK-52.md)]:** Setup PgEstoqueRepositoryAdapter mapping
* [ ] **[[TSK-53](TSK-53.md)]:** Setup PgColaboradorRepositoryAdapter mapping
* [ ] **[[TSK-54](TSK-54.md)]:** Implement AesGcmEncryptedConverter for JPA entities
* [ ] **[[TSK-55](TSK-55.md)]:** Create custom @Masked annotation
* [ ] **[[TSK-56](TSK-56.md)]:** Build MaskedLoggingFilter utilizing Logback
* [ ] **[[TSK-57](TSK-57.md)]:** Create CorrelationIdInterceptor filter
* [ ] **[[TSK-58](TSK-58.md)]:** Code Redis-backed IdempotencyInterceptor filter
* [ ] **[[TSK-59](TSK-59.md)]:** Implement FaturamentoController POST endpoint
* [ ] **[[TSK-60](TSK-60.md)]:** Implement FaturamentoController GET status endpoint
* [ ] **[[TSK-61](TSK-61.md)]:** Code HookRegistry component
* [ ] **[[TSK-62](TSK-62.md)]:** Code HookRegistry listener dispatch engine
* [ ] **[[TSK-63](TSK-63.md)]:** Implement WebhookSignatureValidator checker
* [ ] **[[TSK-64](TSK-64.md)]:** Build Outbound API Gateway Pagamento ACL Adapter
* [ ] **[[TSK-65](TSK-65.md)]:** Create Spring Event Publisher dispatch handler
* [ ] **[[TSK-66](TSK-66.md)]:** Setup transactional event listener for estoque reservation
* [ ] **[[TSK-67](TSK-67.md)]:** Configure RabbitMQ Connection Factory
* [ ] **[[TSK-68](TSK-68.md)]:** Define RabbitMQ billing queue and exchange schema
* [ ] **[[TSK-69](TSK-69.md)]:** Implement RabbitMQ billing listener publisher
* [ ] **[[TSK-70](TSK-70.md)]:** Setup RabbitMQ Dead Letter Exchange (DLX) retry configuration
* [ ] **[[TSK-71](TSK-71.md)]:** Configure Quartz Scheduler properties
* [ ] **[[TSK-72](TSK-72.md)]:** Implement Quartz job for transaction reconciliation
* [ ] **[[TSK-73](TSK-73.md)]:** Implement ReconciliationWorker running on Loom runner
* [ ] **[[TSK-74](TSK-74.md)]:** Setup Micrometer Prometheus metrics registry
* [ ] **[[TSK-75](TSK-75.md)]:** Expose ordens_em_limbo_ratio custom Gauge
* [ ] **[[TSK-76](TSK-76.md)]:** Expose reconciliacao_tempo_p95 custom Histogram
* [ ] **[[TSK-77](TSK-77.md)]:** Integrate OpenTelemetry tracer instrumentation exporter
* [ ] **[[TSK-78](TSK-78.md)]:** Implement Admin endpoints for manual job triggers
* [ ] **[[TSK-79](TSK-79.md)]:** Implement DLQ replay utility REST Endpoint
* [ ] **[[TSK-80](TSK-80.md)]:** Add Spring Security configuration for REST APIs
* [ ] **[[TSK-81](TSK-81.md)]:** Setup JWT token validation filters
* [ ] **[[TSK-82](TSK-82.md)]:** Configure Spring Boot Actuator security permissions
* [ ] **[[TSK-83](TSK-83.md)]:** Implement global exception handler controller advice
* [ ] **[[TSK-84](TSK-84.md)]:** Build resilience4j circuit breakers on gateway ACL
* [ ] **[[TSK-85](TSK-85.md)]:** Build resilience4j rate limiters on webhook endpoints
* [ ] **[[TSK-86](TSK-86.md)]:** Setup react-router-dom base routing schema
* [ ] **[[TSK-87](TSK-87.md)]:** Import Outfit and JetBrains Mono fonts config
* [ ] **[[TSK-88](TSK-88.md)]:** Define Design System tokens in tailwind.config.js
* [ ] **[[TSK-89](TSK-89.md)]:** Build BaseLayout component (Glassmorphic background)
* [ ] **[[TSK-90](TSK-90.md)]:** Create Zustand state store for User Sessions
* [ ] **[[TSK-91](TSK-91.md)]:** Create Zustand state store for Financial Orders
* [ ] **[[TSK-92](TSK-92.md)]:** Implement useIdempotentMutation hook
* [ ] **[[TSK-93](TSK-93.md)]:** Build Login screen with authentication handlers
* [ ] **[[TSK-94](TSK-94.md)]:** Build MEI Invoicing Dashboard view
* [ ] **[[TSK-95](TSK-95.md)]:** Build Auditor/Controller Reconciliation Dashboard view
* [ ] **[[TSK-96](TSK-96.md)]:** Build Audit Logs data-table with JetBrains Mono font
* [ ] **[[TSK-97](TSK-97.md)]:** Add Vite PWA configuration and service worker registers
* [ ] **[[TSK-98](TSK-98.md)]:** Setup Vitest testing environment runner
* [ ] **[[TSK-99](TSK-99.md)]:** Setup GitHub Actions CI/CD workflows configuration
* [ ] **[[TSK-100](TSK-100.md)]:** Setup proprietary LICENSE & verify full production builds

### **🟡 In Progress (Actively Being Built)**

* *None*

### **🔵 In Review (QA & Test Verification)**

* *None*

### **🟢 Done (Merged & Verified in Main Trunk)**

* [x] **[TSK-01]:** Initialize Git Repository
* [x] **[TSK-02]:** Configure .gitignore Rules

---

## **📝 Individual Task Template (Save as TSK-[Number].md)**

When creating a new task, create a separate file named `TSK-[Number].md` inside the `backlog` directory using the following structure:

```markdown
# TSK-[Number]: [Task Title]

* **Owner / Assignee:** [Name]  
* **Estimated Effort:** [Story Points]  
* **Story / Epic Reference:** [Epic/RF ID]  
* **Development Methodology:** TDD (Red-Green-Refactor)

## 📖 Description & Objectives

[Description of the technical implementation. Details on files to create/modify. Propose the TDD flow: explicitly list the test files that must be created/run to fail before writing any production code.]

## ✅ Definition of Ready (DoR)

* [ ] [TDD Setup: Test file/suite path is determined and ready for Red phase]
* [ ] [Prerequisite 1: e.g., API contract, schema, or mock design defined]
* [ ] [Prerequisite 2: e.g., Pre-requisite dependencies/tasks completed]

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Testing/Quality - TDD]:** Follow Red-Green-Refactor. Test suite written first and runs with failures (Red). Minimal implementation code written to pass (Green). Refactored code maintains green tests. All unit/integration tests pass.
* [ ] **[Functional]:** [Describe the specific expected behavior/feature validation]
* [ ] **[UX & UI - If Applicable]:** [Describe required styles, responsiveness, or animations]
* [ ] **[Technical/Security]:** [Specify error handling, performance constraints, or code quality checks]
```

---

*Document Author: Kalyel N. Laurindo / Project Owner*

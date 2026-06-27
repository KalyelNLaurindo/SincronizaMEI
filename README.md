# 📋 **SincronizaMEI — Eliminating State Drift & Financial Inconsistency**

### **High-Performance Event-Driven ERP & Reconciliation Engine for Micro-Entrepreneurs**

[![Stack Version](https://img.shields.io/badge/Java-21-orange?style=for-the-badge&logo=openjdk)](https://openjdk.org)
[![Stack Version](https://img.shields.io/badge/React-18-blue?style=for-the-badge&logo=react)](https://react.dev)
[![Architecture](https://img.shields.io/badge/Architecture-Bounded_Contexts-8A2BE2?style=for-the-badge)](https://link-to-architecture)
[![Dependencies](https://img.shields.io/badge/Dependencies-Isolated_Containers-success?style=for-the-badge)](https://link-to-dependencies)
[![Testing Paradigm](https://img.shields.io/badge/Testing-TDD_Red_Green_Refactor-green?style=for-the-badge)](https://link-to-testing)
[![Compliance](https://img.shields.io/badge/LGPD-Compliant-blueviolet?style=for-the-badge)](https://link-to-compliance)

---

## **🏛️ Repository Metadata & Context**

| Property               | Description                                                                              |
| :--------------------- | :--------------------------------------------------------------------------------------- |
| **Role**               | Core Repository Architecture / Project Lead                                              |
| **Target Segment**     | Micro-entrepreneurs (MEIs) & Small-to-Medium Businesses (SMBs)                           |
| **Architecture Style** | Modular Monolith / Bounded Contexts (Finance, Inventory, Sales)                          |
| **Execution Engine**   | Spring Boot 3.2 (Java 21 Virtual Threads) + PostgreSQL Bitemporal Database & Redis Cache  |
| **Date of Creation**   | April 16, 2026                                                                           |
| **Current Version**    | v1.1.0                                                                                   |

---

## **🚀 1. The Product Vision & Core Problem**

### **1.1. The Macro Pain Space**

Most traditional platforms operate under a "Happy Path" premise, trusting that external webhooks, client systems, and network handshakes are structurally flawless.

In real-world decentralized environments, connectivity drops, network timeouts, and silent payload dropouts introduce **Systemic State Drift** (critical discrepancies between active physical states, third-party payment ledger checkpoints, and the central local database). This blind spot results in direct capital loss, asset leaks, and severe operational anxiety for micro-entrepreneurs.

### **1.2. The Core Solution Paradigm Shift**

**SincronizaMEI** flips the passive paradigm. Instead of trusting network calls to succeed, it employs a **Proactive Reconciliation Architecture** driven by background events, pessimistic database locks, and resilient workers. If a transaction fails or a webhook payload is dropped, the system actively detects the discrepancy and heals itself.

---

#### **📌 REFERENCE: Eventual Consistency Recovery Model**

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ 1. PASSIVE HAPPY-PATH MODEL (Traditional)                                  │
│                                                                           │
│ [External API] ──► [Callback/Request] ──► [Successful?] ──► (No/Timeout)  │
│                                                 │                         │
│                                                 └─► [Permanent Limbo State]
└───────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────┐
│ 2. PROACTIVE RESILIENCE MODEL (SincronizaMEI)                             │
│                                                                           │
│ [External API] ──► [Callback/Request] ──► [Successful?] ──► (No/Timeout)  │
│                                                 │                         │
│                                                 ▼                         │
│                                       [Mark State: Out-of-Sync]           │
│                                                 │                         │
│                                                 ▼                         │
│                                       [Proactive Recovery Worker]         │
│                                                 │                         │
│                                                 ▼                         │
│                                       [Stored Procedures Auto-Heal]       │
│                                                 │                         │
│                                                 ▼                         │
│                                       [Consistent State Reached]          │
└───────────────────────────────────────────────────────────────────────────┘
```

To guarantee business integrity, SincronizaMEI implements the following operational SLA constraint: **Automatic reconciliation and eventual state consistency are guaranteed to converge in under 15 minutes.**

---

## **🎮 2. API & Interface Usage Reference**

The backend exposes a highly idempotent, event-driven REST API. Use the following core execution contracts and headers:

| Request / Action | Method & Syntax | Description | Example Payload / Header |
| :--- | :--- | :--- | :--- |
| **Create Order** | `POST /api/orders` | Places an order, enqueues to RabbitMQ, and triggers background processing. | Header: `X-Idempotency-Key: <UUID>`<br>Body: `{"amount": 150.00, "items": [...]}` |
| **Check Order Status** | `GET /api/orders/{id}` | Retrieves the current state of a transaction and sync indicators. | Response: `{"id": "...", "status": "CONCILIADO", "drift": false}` |
| **Verify Integrity** | `GET /api/audit/integrity` | Runs a system-wide integrity check to query out-of-sync records. | Response: `{"in_limbo": 0, "divergencies": []}` |
| **Trigger Reconciliation** | `POST /api/reconcile` | Forces manual execution of the reconciliation background job. | Header: `Authorization: Bearer <token>` |

> [!NOTE]
> **Data & Validation Rules:**
>
> - **Idempotency Protection:** Requests to `POST /api/orders` require the `X-Idempotency-Key` header. Duplicate keys within a 24-hour window return the cached response (`HTTP 409 Conflict` if processing, or the original response).
> - **Bitemporal Auditing:** The database preserves historic state changes. Operations are logged with two time dimensions: transaction time (`valid_from`/`valid_to`) and system registration time (`system_init`/`system_end`).
> - **Financial Divergence Margin:** Financial variances $\le \text{R\$} 0.50$ are automatically matched and settled with audit footnotes. Variances $> \text{R\$} 0.50$ are marked as `DIVERGENTE_AUDITORIA` and trigger high-priority alerts.

---

## **🛠️ 3. Technical Stack Overview**

The engineering blueprint balances enterprise-grade backend reliability, high-throughput asynchronous event transport, and a responsive, localized user experience.

| Architectural Layer | Component / Technology | Technical Rationale |
| :--- | :--- | :--- |
| **Frontend Client** | React 18, Vite, Tailwind CSS 3.4, PWA | Modern, fast-rendering interface adapted for mobile usage, featuring offline-ready service workers. |
| **Backend Engine** | Spring Boot 3.2, Java 21 | Virtual Threads (Project Loom) for lightweight concurrent I/O task scheduling during reconciliation. |
| **Asynchronous Transport** | RabbitMQ 3.13 | High-throughput messaging pipeline separating ingestion HTTP endpoints from long-running workers. |
| **Cache & Key Store** | Redis 7.2 | Distributed locks and key storage with automatic TTL for API idempotency gates. |
| **Database & Ledger** | PostgreSQL 16 (Bitemporal schema) | Relational integrity, temporal queries, exclusion constraints, and complex reconciliation procedures stored as SQL functions. |
| **Security & Secrets** | HashiCorp Vault 8200 | Centralized secret retrieval for environment database passwords, API gateway tokens, and cryptographic keys. |

---

## **🏗️ 4. Core Architectural Premises**

Specify the architectural rules, coding standards, and validation strategies.

*   **Premise 4.1 - Design & Modularity Strategy:** MVC encapsulation with clean domain-driven bounded contexts. Cross-module database repository lookups are prohibited; communication is restricted to domain events.
*   **Premise 4.2 - Testing Strategy & Coverage Rule:** Test-Driven Development (TDD) cycle (Red-Green-Refactor) is strictly enforced. Integration tests use Testcontainers with real PostgreSQL and RabbitMQ instances. The use of in-memory H2 databases for testing is banned.
*   **Premise 4.3 - Data Deletion & Auditing Policy:** Hard deletes are blocked. Database triggers intercept and reject physical `DELETE` or `UPDATE` queries on ledger records. Soft-deletes and bitemporal record versioning are mandatory.
*   **Premise 4.4 - API Idempotency & Concurrency Strategy:** Atomic redis lock checking (`SET NX EX`) at the middleware layer prevents double submissions and race conditions.

---

## **📂 5. Codebase Structure & Directory Standards**

```text
sincronizamei/
├── backend/                  # Spring Boot backend application
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/         # Java source code (api, reconciliacao, modules, plugins)
│   │   │   └── resources/    # Application properties and database schemas
│   │   └── test/             # Unit and integration tests (Testcontainers)
│   └── pom.xml               # Maven configuration
├── frontend/                 # React (Vite) frontend application
│   ├── src/                  # React source files (components, styles, App.tsx)
│   ├── public/               # Static assets
│   └── package.json          # NPM configuration
├── db/                       # Database schema and procedures
│   ├── migrations/           # Flyway DDL migration scripts
│   └── procedures/           # PostgreSQL stored procedures
├── infra/                    # Infrastructure as Code
│   └── terraform/            # Terraform configurations for staging/production
├── context/                  # Project specifications and architecture reference docs
│   ├── Implementation Flow - SincronizaMEI.md
│   └── Software Design Document - SincronizaMEI.md
├── scripts/                  # DevOps and helper scripts
│   └── vault-init-dev.sh     # Script to initialize Vault in development
├── docker-compose.yml        # Orchestration for local infrastructure (Postgres, Redis, RabbitMQ, Vault)
└── package.json              # Workspace/root configuration
```

---

## **💻 6. Local Engineering Development Setup**

### **6.1. Core System Prerequisites**

Before setting up the project, make sure you have the following environments installed:

- **Runtime Environments:** JDK 21+ (OpenJDK recommended), Node.js 18+
- **Package Managers:** Maven 3.9+, npm 9+
- **Containerization:** Docker & Docker Compose
- **Version Control System:** Git

### **6.2. Initial Bootstrap Sequence**

1. Clone this repository locally to your workspace:

   ```bash
   git clone https://github.com/koyos-studios/sincronizamei.git
   cd SincronizaMEI
   ```

2. **Step 6.2.1 - Infrastructure Setup:**
   Copy the template environment configuration and spin up the background services:

   ```bash
   # Linux/macOS or Git Bash/WSL
   cp .env.example .env

   # Windows PowerShell
   Copy-Item .env.example .env
   ```

   *Note: Populate any sensitive credentials in `.env` if required for your local profile. Ports and credentials defaults match the Docker Compose configuration.*

   Boot the background backing containers:
   ```bash
   docker-compose up -d
   ```

   Verify container orchestration health to ensure that PostgreSQL, Redis, RabbitMQ, and Vault are running:
   ```bash
   docker-compose ps
   ```

   **Useful Local Ports Reference:**
   - **PostgreSQL:** `5432`
   - **Redis:** `6379`
   - **RabbitMQ (AMQP):** `5672`
   - **RabbitMQ (Web UI):** `15672` (Credentials: `guest` / `guest`)
   - **HashiCorp Vault:** `8200` (Token defaults to `root` in dev mode)

3. **Step 6.2.2 - Application / Main Engine Setup:**
   Run the backend integration test suite to verify connectivity and download dependencies:
   ```bash
   mvn clean test
   ```

   Start the local backend server (runs on `http://localhost:8080`):
   ```bash
   mvn spring-boot:run
   ```

4. **Step 6.2.3 - Client Frontend / UI Setup:**
   Open a separate terminal window, install dependencies, and launch the React Vite development server (runs on `http://localhost:5173`):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### **6.3. Automated Verification Commands**

Ensure your modifications pass the repository quality gates before submitting a Pull Request:

- **Execute primary backend tests (Unit & Testcontainers)**:
  ```bash
  mvn clean test
  ```

- **Verify code style and static analysis**:
  ```bash
  # Checkstyle & SpotBugs verification
  mvn verify -DskipTests
  ```

---

🏁 **End of Document:** This repository README serves as the definitive engineering portal for the SincronizaMEI ecosystem. Changes to stack versions, core patterns, or installation requirements must follow official pull-request governance.

Made with ❤️ by **Kalyel N. Laurindo / Software Engineer**

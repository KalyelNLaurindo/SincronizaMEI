# **🤖 SincronizaMEI — Claude Code / AI Assistant Reference Guide**

This file provides system context, build/test commands, architecture guidelines, and coding standards to align the development flow of **SincronizaMEI** (A modular monolithic ERP designed to enforce core business rules through Project Loom Virtual Threads, Bitemporal PostgreSQL persistence, and Redis-backed HTTP idempotency).

---

## 🛠️ Common Commands

### Running the Application

- **Run Backend Development Server:**
  ```bash
  ./mvnw spring-boot:run -pl backend
  ```
- **Run Frontend Development Server:**
  ```bash
  npm run dev --prefix frontend
  ```

### Running Tests

- **Run all backend tests:**
  ```bash
  ./mvnw test -pl backend
  ```
- **Run all frontend tests:**
  ```bash
  npm test --prefix frontend
  ```
- **Run specific test target:**
  ```bash
  ./mvnw test -pl backend -Dtest=ClassNameTest
  ```

---

## 🏛️ Technology Stack & Constraints

- **Runtime Environment:** Java 21 LTS (Project Loom Virtual Threads enabled) & Node.js v20 LTS (Vite + React)
- **Production Dependencies:** Spring Boot 3.2.x, Spring Data JPA, Spring Security, Flyway, Redis (Data Redis), RabbitMQ (AMQP), React 18, Tailwind CSS
- **Persistence Strategy:** PostgreSQL 16 (Bitemporal schemas using valid_from/to and system_init/end) and Redis 7.2 (used for HTTP request idempotency locks)
- **Performance Targets:** Low latency request handling leveraging virtual threads, caching via Redis, and database pessimistic locks (`FOR UPDATE NOWAIT`) executing under 100ms.

---

## 🏗️ Architectural Guardrails

Detail the structural boundaries and rules to prevent architectural regression:

1.  **Architecture Paradigm:** Modular Monolith with Hexagonal Bounded Contexts (Ports & Adapters)
2.  **Layer Isolation:** The Domain Layer (`br.com.sincronizamei.modules.<context>.domain`) must remain 100% pure (zero external framework imports, zero Spring, zero Hibernate annotations).
3.  **Ports & Adapters (Dependency Inversion):** Interactivity with external systems (database, file system, external APIs) must happen strictly through interfaces (Ports) in the application/domain layer and concrete Adapters in the infrastructure layer.
4.  **Data Durability & Transaction Safety:** State mutations must execute using database transactions with rollback logic. Bitemporal tracking is enforced at the database level; physical deletes are blocked by `trg_bloquear_delete` triggers.
5.  **Specific Domain Invariants:** Webhooks must check HMAC-SHA256 signatures and timestamp validity. Idempotency must be locked via Redis `SET NX EX` (24h TTL) using `X-Idempotency-Key` headers. Sensitive PII columns (CPF, email, bank details) must be encrypted at rest using AES-256-GCM.
6.  **Engineering Principles:** Always design and write code following: DRY, KISS, SOLID principles, standard Design Patterns, and Clean Code conventions.

---

## 🧪 Testing Paradigm (TDD Mandatory)

- **Testing Approach:** Strict Test-First (TDD) (write and run failing tests before production code)
- **Testing Framework:** JUnit 5 / Spring Boot Test / Testcontainers (for PostgreSQL/RabbitMQ integration tests) and Vitest/Jest (for frontend testing)
- **Boundary Conditions:** Implement explicit tests checking boundary conditions (e.g., empty values, negative thresholds, overflow, unauthorized roles, validation failure states).
- **Self-Healing Limit:** If the test runner, linter, or type checker fails more than 3 consecutive times during autonomous debugging/correction, stop execution immediately and request human developer intervention.

---

## 📂 Codebase Directory Structure

```text
SincronizaMEI/
├── backend/                              # Backend Application Root
│   ├── pom.xml                           # Maven project configuration
│   └── src/
│       ├── main/
│       │   ├── java/br/com/sincronizamei/modules/
│       │   │   ├── financeiro/           # Bounded context for financial management
│       │   │   │   ├── domain/           # Pure entities and value objects
│       │   │   │   ├── application/      # Use cases and inbound/outbound ports
│       │   │   │   └── infra/            # Adapters (Repositories, Controllers, Clients)
│       │   │   ├── estoque/              # Bounded context for inventory
│       │   │   └── rh/                   # Bounded context for human resources
│       │   └── resources/
│       │       ├── application.yml
│       │       └── db/
│       │           ├── migrations/       # Flyway database migrations
│       │           └── procedures/       # PostgreSQL reconciliation procedures/functions
│       └── test/                         # Unit and integration test suites
│
├── frontend/                             # Frontend React PWA Root
│   ├── package.json                      # NPM packaging manifest
│   ├── vite.config.ts                    # Vite compilation config
│   └── src/                              # SPA UI source files
│
├── infra/                                # Terraform IaC configurations
├── docker-compose.yml                    # Local multi-container database & queues
└── README.md                             # Repository main entrypoint
```

---

## 🏷️ Code Governance & Naming Conventions

- **Language & Style:** Code structures must remain highly professional and technical (utilizing strict typing, SOLID, and architectural concepts). However, all inline code comments and docstrings must be written in simple, layman-friendly English, explaining the underlying business rules and domain logic (the "why") rather than the technical implementation details (the "how"). Meanwhile, **all implementation plans (`implementation_plan.md`), walkthroughs (`walkthrough.md`), and user-facing design explanations must be written in Portuguese (PT-BR)**, using clear, simple, and highly explanatory language.
- **Naming Styles & Suffixes:**

| Role / Pattern         | Suffix / Prefix Selection                  | Example Name          |
| :--------------------- | :----------------------------------------- | :-------------------- |
| **Domain Entity**      | Entity suffix (e.g., OrdemEntity)          | `OrdemEntity`         |
| **Value Object**       | ValueObject suffix (e.g., CPFValueObject)   | `CPFValueObject`      |
| **Application Action** | UseCase suffix (e.g., ReconcileOrdemUseCase)| `ReconcileOrdemUseCase`|
| **Interface Port**     | Port suffix (e.g., OrdemRepositoryPort)    | `OrdemRepositoryPort` |
| **Concrete Adapter**   | Adapter suffix (e.g., PgOrdemRepositoryAdapter) | `PgOrdemRepositoryAdapter` |

---

## 🌿 Git Workflow & Commit Conventions

- **Branching Strategy:**
  - All development must take place on feature branches (e.g., `feature/phase-X-short-description` or `feature/short-description`).
  - **CRITICAL REQUIREMENT:** A separate git feature branch must be used for each phase of the project implementation (e.g., `feature/phase-1-infrastructure`, `feature/phase-2-domain`) to keep delivery phases isolated and tidy.
  - Direct commits to the main integration branch are prohibited; merge code via Pull Requests.
- **Semantic Commit Messages:** Use Conventional Commits standard. Commit titles must describe precisely **what the changes actually do** rather than using generic descriptions or directly referencing task numbers (e.g., use `feat(scope): add complex number struct` instead of `feat(scope): implement task 3` or `feat(scope): task 3`):
  - `feat(scope):` Introduces a new feature or domain component.
  - `fix(scope):` Patches a software bug or corrects an active system failure.
  - `docs(scope):` Updates markdown documents, guidelines, changelogs, or walkthroughs.
  - `test(scope):` Adds or updates test files without changing production code.
  - `chore(scope):` Builds setups, configuration files, or project dependency actions.
- **🚫 STRICTLY FORBIDDEN — AI Co-Author Trailers:** NEVER add `Co-Authored-By:`, `Co-authored-by:`, or any AI attribution trailer to commit messages. This includes any reference to Claude, Anthropic, or any AI assistant. All commits must be authored solely by the human developer. Violating this rule causes unwanted GitHub contributor entries and misrepresents the project authorship.

---

## 📋 Planning & Execution Flow Checklist

For every backlog task, the AI agent and developer must strictly follow this lifecycle:

1.  **Check Task & Branch Alignment:**
    - **FIRST-TIME SETUP (if repository is new):** Before any other action, verify the following exist in the project root: (1) `.git/` directory — if not, run `git init`; (2) `.gitignore` — if not, create one tailored to the project's tech stack and ensure `claude.md` is added to it to prevent it from being tracked; (3) `claude.md` — if not, create it from the standard playbook template. Once all three exist, perform an initial commit: `chore(setup): initialize repository` (committing only `.gitignore` and basic project configuration files, ensuring `claude.md` is ignored and remains unstaged).
    - Inspect the backlog folder (`context/backlog/` or equivalent) and the master backlog `README.md` to identify the next pending task (`TSK-XX`).
    - Ensure you are working on the correct git feature branch (`feature/phase-X-short-description` or `feature/short-description`). Create or switch to the branch if needed.
2.  **Planning Phase (Before Code Modifications):**
    - Create `implementation_plan.md` in the current conversation directory **written in Portuguese (PT-BR)**.
    - **CRITICAL REQUIREMENT:** Explain the implementation steps in simple, layman-friendly language so that non-technical stakeholders can easily understand what changes and why.
    - Mark `request_feedback = true` in the plan metadata and **STOP** to wait for the user's explicit approval before writing code.
3.  **Execution Phase (TDD Protocol):**
    - Create/update `task.md` in the conversation directory.
    - **Language Constraint:** Write all code, unit/integration tests, docstrings, inline comments, and technical schemas strictly in professional **Technical English**.
    - Write test cases under `tests/` and run the suite to verify they fail (Red).
    - Implement minimal production code in `src/` to satisfy the tests (Green).
    - Refactor the code while keeping all tests passing (Refactor).
    - **COMMIT PER CYCLE (Mandatory):** Upon completing each full Red-Green-Refactor cycle, perform a semantic commit on the feature branch before starting the next cycle (e.g., `feat(scope): implement [feature]`). **Do not accumulate multiple cycles before committing.**
4.  **Completion & Pre-Commit Sync Phase (Strict Sequence):**
    - Before committing any changes, perform the following updates in this exact order:
      1.  Mark the task's individual file checkboxes (DoR/DoD) as completed (`[x]`) inside the task's markdown file (`context/backlog/TSK-XX.md`).
      2.  Update the task's status to `Done` in the backlog master tracker (`context/backlog/README.md`).
      3.  **If and only if this is the last task** of the phase or project sprint, update the main project root `README.md` and the folder-level `README.md` to reflect the newly delivered features/states.
      4.  Create `walkthrough.md` in the conversation directory summarizing the changes (written in Portuguese, PT-BR).
      5.  **If and only if this is the final task of the entire project:** add the `LICENSE` file to the repository root, configure the CI/CD workflow (e.g., `.github/workflows/ci.yml` with lint, test, and build jobs), and validate the build/packaging script before the final commit.
    - Only after all the files above are updated and verified, stage the files, commit using Conventional Commits naming standards, and push the branch to the remote repository.
    - **🚫 NEVER COMMIT claude.md, implementation_plan_*.md, or walkthrough_*.md files.** These are internal development, planning, and session artifacts for reference only. They must NEVER be staged or committed to the repository (ensure they are added to `.gitignore` to prevent tracking).
5.  **Prepare for Next Task:**
    - Clean up the workspace and proceed to check the next pending task in the queue.

---

*Document Author: Kalyel N. Laurindo / Software Engineer*

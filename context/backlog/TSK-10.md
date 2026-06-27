# TSK-10: Configure HashiCorp Vault local integrations

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 3 Story Points  
* **Story / Epic Reference:** SEC-01  
* **Development Methodology:** TDD (Red-Green-Refactor)

## 📖 Description & Objectives

Setup spring-cloud-starter-vault-config properties, and map environment secret variables to bootstrap integration. Configure bootstrap properties and write a TDD config check.

## ✅ Definition of Ready (DoR)

* [ ] Spring Boot dependencies are configured (`TSK-04` complete).
* [ ] Local environment keys are configured in `.env` (`TSK-09` complete).

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Testing/Quality - TDD]:** Write `VaultConfigTest.java` verifying connection behavior. Test fails initially (Red), and passes once bootstrap properties are set (Green).
* [ ] **[Technical/Security]:** Secrets (database passwords, Redis host keys) are read cleanly from Vault context without plain text leakage.

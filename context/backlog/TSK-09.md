# TSK-09: Initialize local .env configuration variables

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 1 Story Point  
* **Story / Epic Reference:** INFRA-04  
* **Development Methodology:** TDD (Red-Green-Refactor) - N/A for environment setups.

## 📖 Description & Objectives

Create `.env.example` templates and a local `.env` containing local database, Redis, RabbitMQ credentials and connections keys to isolate development environments.

## ✅ Definition of Ready (DoR)

* [ ] Docker containers setup complete (`TSK-08` complete).
* [ ] `.gitignore` contains rules blocking `.env` from tracking.

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Infrastructure]:** `.env.example` exists containing schema variables. `.env` file created locally.
* [ ] **[Technical/Security]:** Git confirms `.env` is ignored. Variables mapped correctly to local ports (`5432`, `6379`, `5672`).

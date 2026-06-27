# TSK-06: Setup Docker Compose with PostgreSQL 16 container

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 2 Story Points  
* **Story / Epic Reference:** INFRA-03  
* **Development Methodology:** TDD (Red-Green-Refactor) - N/A for Docker configuration.

## 📖 Description & Objectives

Create a local `docker-compose.yml` defining the PostgreSQL 16 database service to spin up a fully isolated, production-like environment for local development and test validation.

## ✅ Definition of Ready (DoR)

* [ ] Docker is installed and running locally.
* [ ] `.gitignore` contains database mount volumes pattern exclusion.

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Infrastructure]:** `docker-compose.yml` has a `db` service using `postgres:16-alpine`.
* [ ] **[Technical/Security]:** `docker-compose config` verifies compose schema validity. Containers boot cleanly, exposing port `5432` to the host.

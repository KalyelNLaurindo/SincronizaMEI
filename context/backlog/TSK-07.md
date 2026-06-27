# TSK-07: Setup Docker Compose with Redis 7.2 container

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 2 Story Points  
* **Story / Epic Reference:** INFRA-03  
* **Development Methodology:** TDD (Red-Green-Refactor) - N/A for Docker configuration.

## 📖 Description & Objectives

Add a Redis 7.2 caching and key-value store service configuration into `docker-compose.yml` to enable HTTP request idempotency locking tests.

## ✅ Definition of Ready (DoR)

* [ ] `docker-compose.yml` exists and has database configurations (`TSK-06` complete).

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Infrastructure]:** `docker-compose.yml` includes a `cache` service running `redis:7.2-alpine`.
* [ ] **[Technical/Security]:** Redis container starts cleanly, exposing port `6379` to the host, verified by `redis-cli ping` or equivalent check.

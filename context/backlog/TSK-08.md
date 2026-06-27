# TSK-08: Setup Docker Compose with RabbitMQ 3.13 container

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 2 Story Points  
* **Story / Epic Reference:** INFRA-03  
* **Development Methodology:** TDD (Red-Green-Refactor) - N/A for Docker configuration.

## 📖 Description & Objectives

Add a RabbitMQ 3.13 message broker service with management UI enabled to `docker-compose.yml` to support asynchronous billing event queueing.

## ✅ Definition of Ready (DoR)

* [ ] `docker-compose.yml` contains database and cache configurations (`TSK-07` complete).

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Infrastructure]:** `docker-compose.yml` defines a `broker` service using `rabbitmq:3.13-management-alpine`.
* [ ] **[Technical/Security]:** RabbitMQ launches cleanly, exposing port `5672` (AMQP) and `15672` (Management UI) to the host.

# TSK-05: Enable Spring Boot Virtual Threads configuration

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 2 Story Points  
* **Story / Epic Reference:** RP-01  
* **Development Methodology:** TDD (Red-Green-Refactor)

## 📖 Description & Objectives

Enable Java 21 Project Loom virtual threads in Spring Boot (`spring.threads.virtual.enabled=true`) to optimize concurrency. Write a test first verifying that executor instances are indeed virtual threads.

## ✅ Definition of Ready (DoR)

* [ ] Java 21 LTS is set up as the compiler runtime in `pom.xml` (`TSK-04` complete).
* [ ] Target application properties path `backend/src/main/resources/application.yml` is ready.

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Testing/Quality - TDD]:** Write `ThreadConfigTest.java` verifying that the application context tasks run on Virtual Threads. Test fails initially (Red), passes after enabling configuration (Green).
* [ ] **[Technical/Security]:** `spring.threads.virtual.enabled: true` exists in application configurations.

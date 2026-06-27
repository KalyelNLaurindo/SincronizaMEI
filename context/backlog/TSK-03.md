# TSK-03: Deploy local claude.md context file

* **Owner / Assignee:** Kalyel N. Laurindo / Project Owner  
* **Estimated Effort:** 1 Story Point  
* **Story / Epic Reference:** INFRA-01  
* **Development Methodology:** TDD (Red-Green-Refactor) - N/A for raw text context.

## 📖 Description & Objectives

Copy/Deploy the standard `claude.md` file into the root folder of the project to set up the rules and constraints governing the development of SincronizaMEI.

## ✅ Definition of Ready (DoR)

* [ ] Git repository is initialized and `.gitignore` file includes `claude.md` rules (`TSK-02` complete).
* [ ] Master `claude.md` template is available in the Koyos Playbook.

## 🏁 Definition of Done (DoD) & Acceptance Criteria

* [ ] **[Infrastructure]:** `claude.md` exists in the workspace root.
* [ ] **[Technical/Security]:** `claude.md` is ignored by Git, ensuring it remains unstaged and untracked (verified with `git status`).

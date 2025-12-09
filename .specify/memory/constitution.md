---
title: "Project Constitution for Physical AI & Humanoid Robotics"
version: "0.1.0"
date: "2025-12-09"
authors: ["TODO: Define project authors/maintainers"]
repo: "TODO: Add repository URL"
license: "MIT"
---

<!--
---
Sync Impact Report
---
- Version Change: None -> 0.1.0
- Added Sections: All (Initial document)
- Removed Sections: None
- Templates Requiring Updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(authors): Define project authors/maintainers
  - TODO(repo): Add repository URL
-->

# 1. Purpose & Scope

This constitution defines the governing principles, standards, and procedures for the **Physical AI & Humanoid Robotics** Docusaurus book project.

**Mission:** To create a comprehensive, high-quality, and accessible educational resource on Physical AI and Humanoid Robotics.

**Components & Integrations:**
- **Core Content:** Docusaurus-based book.
- **Development Stack:** Speckit+ for spec-driven development, Gemini CLI for agent-based workflow.
- **Backend:** Python (FastAPI), Neon Postgres (database), Qdrant (vector store).
- **Frontend/Services:** Context7 for documentation fetching, BetterAuth for user authentication and personalization.
- **Features:** RAG (Retrieval-Augmented Generation) chatbot for interactive queries, user-specific content personalization, and Urdu language translation.
- **Deployment:** GitHub Pages or Vercel.

# 2. Governance

- **Maintainers:** Responsible for final architectural decisions, merging PRs, and enforcing the constitution.
- **Contributors:** Any individual who submits a PR that is merged.
- **Reviewers:** Designated experts or maintainers responsible for upholding code quality and adherence to principles in PRs.
- **Security Contact:** `TODO: design-a-security-contact-process`.

# 3. Repository Rules

- **Branch Names:** All branches MUST follow the pattern `feature/[description]`, `fix/[description]`, `docs/[description]`, or similar conventions.
- **Commits:** Commits MUST adhere to the Conventional Commits specification.
- **Pull Requests (PRs):** All changes to `main` MUST go through a PR. PRs require at least one approving review from a designated reviewer.
- **Branch Protection:** The `main` branch IS protected. Direct pushes are disabled.

# 4. Mandatory Push Rule

After every logical unit of work, especially after creating a Prompt History Record (PHR) or completing a feature task, the full repository state MUST be committed and pushed to its feature branch. A PR should be opened for integration.

**Example Git Workflow:**
```bash
# 1. Add changes
git add .
# 2. Commit with a conventional message
git commit -m "feat(auth): implement user profile storage"
# 3. Push to the remote branch
git push origin feature/user-profiles
# 4. Create a Pull Request against `main`
```

# 5. CI/CD & Deployment

- **CI Checks:** All PRs MUST pass automated checks, including linting, testing, and vulnerability scans before being eligible for merge.
- **Deployment:** The `main` branch is automatically deployed to GitHub Pages or Vercel.
- **Secrets:** No secrets or API keys shall ever be hardcoded. They MUST be managed through environment variables or a secure secret management service.

# 6. Specs & Documentation (Speckit+ + Context7)

- **Location:** All feature specifications reside in the `specs/` directory.
- **Header:** Every spec file MUST begin with a header defining its purpose and scope.

**Spec Header Example:**
```markdown
---
description: A brief, one-sentence description of the feature.
scope: Details what is in and out of scope for this specification.
---
```

# 7. RAG Chatbot Rules

- **Modes:** The chatbot operates in two modes:
    1.  **Full-Book:** Can answer questions using the entire book's content as context.
    2.  **Selected-Text:** When a user highlights text, the chatbot MUST ONLY use the provided text selection as its context.
- **Provenance:** All answers MUST cite the source chapter(s) or section(s) used to generate the response.
- **Vectorization:** Content is vectorized and stored in Qdrant. PII is explicitly excluded from vectorization.
- **Logging:** All queries and responses are logged to Neon Postgres for monitoring and improvement, scrubbing any potential PII.

# 8. Authentication & Personalization (BetterAuth)

- **Signup:** On signup, users are asked for their **software background** and **hardware background**.
- **Profile Storage:** User profiles, including personalization settings, are stored in a Neon Postgres database.
- **Personalization:** Logged-in users can reorder, hide, or highlight chapters.
- **Translation:** Logged-in users can enable automatic translation of content to Urdu.

**Minimal Schema Rules:**
- `users` table: `user_id`, `auth_provider_id`, `profile_data (JSONB)`
- `profiles` table (within `profile_data`): `background_sw`, `background_hw`, `preferences (JSONB)`

# 9. Privacy & Security

- **Data Handling:** Only essential user data is collected. All data in transit and at rest is encrypted.
- **Retention:** User data is retained only as long as necessary. A clear data deletion process will be provided.
- **Incident Policy:** A security incident response plan MUST be documented and followed.

# 10. Testing & Observability

- **Unit Tests:** Core logic and utility functions MUST have unit tests.
- **Integration Tests:** Interactions between services (e.g., FastAPI and Neon) MUST be covered by integration tests.
- **E2E Tests:** Critical user flows (e.g., signup, personalization, chatbot query) MUST have E2E tests.
- **Accessibility (a11y):** Frontend components MUST adhere to WCAG 2.1 AA standards.
- **Monitoring:** Basic application performance monitoring (APM) and logging are required for all services.

# 11. Contribution & Code of Conduct

- **Issues:** All bugs, feature requests, and discussions should start with a GitHub Issue.
- **PR Etiquette:** PRs should be small, focused, and clearly describe the "why" behind the change.
- **Formatting:** Code MUST be automatically formatted using pre-commit hooks (e.g., Prettier, Black).
- **Conduct:** All contributors MUST adhere to the Contributor Covenant Code of Conduct.

# 12. Releases

- **Versioning:** The project follows Semantic Versioning (SemVer).
- **Changelog:** A `CHANGELOG.md` file is maintained automatically from Conventional Commits.
- **Tagging:** Every release is marked with a Git tag (e.g., `v1.2.3`).

# 13. License / Third-Party

- **Project License:** This project is licensed under the MIT License.
- **Dependencies:** All third-party dependencies MUST have a compatible license and be reviewed for security vulnerabilities.

# 14. Enforcement

- Violations of this constitution may result in a PR being rejected, a contribution being reverted, or, in serious cases, a temporary or permanent ban from the project.

# 15. Appendices

---

### PR Checklist Template

```markdown
- [ ] My code follows the style guidelines of this project.
- [ ] I have performed a self-review of my own code.
- [ ] I have commented my code, particularly in hard-to-understand areas.
- [ ] I have made corresponding changes to the documentation.
- [ ] My changes generate no new warnings.
- [ ] I have added tests that prove my fix is effective or that my feature works.
```

---

### BetterAuth Signup Payload Sample

```json
{
  "email": "user@example.com",
  "password": "hashed_password_string",
  "profile": {
    "background_sw": "Intermediate",
    "background_hw": "Beginner"
  }
}
```

---

### RAG Answer JSON Example

```json
{
  "answer": "A humanoid robot's stability is maintained through its Center of Mass (CoM) and Zero Moment Point (ZMP).",
  "provenance": [
    {
      "chapter": "Chapter 3: Bipedal Locomotion",
      "url": "/docs/chapter3/bipedal-locomotion"
    }
  ]
}
```

---

### Git Push Example

```bash
git add .
git commit -m "docs(constitution): establish v0.1.0"
git push origin docs/update-constitution
```

---

### Translation Path Example

- **Original:** `/docs/intro`
- **Urdu:** `/ur/docs/intro`

---

### CI Job Names Example

- `lint`
- `test-unit-backend`
- `test-e2e-frontend`
- `build`
- `deploy-vercel`

---

# Constitution Changelog

- **v0.1.0 (2025-12-09):** Initial establishment of the project constitution.
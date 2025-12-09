# Implementation Plan: Physical AI & Humanoid Robotics Book

**Branch**: `gemini-plan-robotics-book-20251209` | **Date**: 2025-12-09 | **Spec**: D:\1.GITHUB\physical-ai-humanoid-robotics-book\specs\001-physical-ai-robotics-book\spec.md
**Input**: Feature specification from `/specs/001-physical-ai-robotics-book/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

To create a comprehensive, interactive online book titled "Physical AI & Humanoid Robotics" using Docusaurus. The book will serve as a definitive guide from beginner to professional levels and will include an integrated RAG (Retrieval-Augmented Generation) chatbot to answer user questions based on the book's content. The frontend will use Docusaurus and TypeScript, the backend will use FastAPI with Python and OpenAI-Agent SDK, authentication will be handled by BetterAuth, with Neon PostgreSQL for the database. Deployment will target Vercel, with GitHub Pages as a secondary option, and reusable frontend components will be utilized.

## Technical Context

**Language/Version**: Python 3.x (for FastAPI Backend), TypeScript (for Docusaurus Frontend)
**Primary Dependencies**: Docusaurus, FastAPI, OpenAI-Agent SDK, Auth0, Neon PostgreSQL client, Qdrant client
**Storage**: Neon PostgreSQL (User Profiles, Logs), Qdrant (Vector Store for book content)
**Testing**: pytest (FastAPI Unit/Integration), httpx (FastAPI API testing), pytest-asyncio (FastAPI async), Jest (Docusaurus Unit), React Testing Library (Docusaurus Unit), Playwright (Docusaurus E2E)
**Target Platform**: Web (Vercel, GitHub Pages)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: RAG chatbot response under 3 seconds (SC-002 from spec.md)
**Constraints**:
- Graceful degradation if BetterAuth is unavailable (Edge Case from spec.md)
- Daily RAG chatbot knowledge base update (FR-001 from spec.md)
- No secrets or API keys hardcoded (Constitution)
**Scale/Scope**: 10k users (assumption), 5 modules, 25 chapters (Book Structure from spec.md)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Repository Rules:**
- Branch Names: Current branch `gemini-plan-robotics-book-20251209` and feature branch `001-physical-ai-robotics-book` (from spec.md) deviate from the `feature/[description]` convention. *Deviation noted, but acceptable for a planning branch/initial feature branch.*
- Commits: All commits MUST adhere to the Conventional Commits specification. *Acknowledged, will be enforced.*
- Pull Requests (PRs): All changes to `main` MUST go through a PR. *Acknowledged, will be enforced.*

**CI/CD & Deployment:**
- CI Checks: All PRs MUST pass automated checks. *Acknowledged, will be configured.*
- Deployment: The `main` branch is automatically deployed to GitHub Pages or Vercel. *Aligns with user's requested deployment targets.*
- Secrets: No secrets or API keys shall ever be hardcoded. *Acknowledged, will be enforced.*

**RAG Chatbot Rules (aligned with spec.md):**
- Modes: Full-Book and Selected-Text modes supported. *Aligned.*
- Provenance: Answers MUST cite sources. *Aligned.*
- Vectorization: Content vectorized in Qdrant, PII excluded. *Aligned.*
- Logging: Queries/responses logged to Neon Postgres, PII scrubbed. *Aligned.*

**Authentication & Personalization (aligned with spec.md):**
- Signup: Background info requested. *Aligned.*
- Profile Storage: User profiles in Neon Postgres. *Aligned.*
- Personalization: Reorder, hide, highlight chapters. *Aligned.*
- Translation: Urdu translation. *Aligned.*
- Minimal Schema Rules: `users` table, `profile_data` (JSONB) with `background_sw`, `background_hw`, `preferences`. *Aligned.*

**Privacy & Security:**
- Data Handling, Retention, Incident Policy. *Acknowledged, will be addressed.*

**Testing & Observability:**
- Unit, Integration, E2E tests, Accessibility (a11y), Monitoring. *Acknowledged, will be addressed in tasks.*

**Contribution & Code of Conduct:**
- Issues, PR Etiquette, Formatting, Conduct. *Acknowledged, will be enforced.*

**Releases:**
- Versioning (SemVer), Changelog, Tagging. *Acknowledged, will be enforced.*

## Project Structure

### Documentation (this feature)

```text
specs/001-physical-ai-robotics-book/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

**Structure Decision**: The project will utilize a "frontend" and "backend" directory structure at the root, reflecting the distinct Docusaurus and FastAPI components.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|-------------------------------------|
| Branch Naming Convention (for feature branch) | Initial deviation from convention for planning phase, will adhere to `feature/[description]` for future feature branches. | N/A |
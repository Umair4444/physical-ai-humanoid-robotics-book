---
title: "Implementation Plan: Physical AI & Humanoid Robotics"
version: 0.1.0
date: 2025-12-09
---

## 1. Project Goals

- **Mission:** To create a comprehensive, interactive online book on Physical AI and Humanoid Robotics, serving a wide audience from beginners to professionals.
- **Success Criteria:** The project is successful when the full Docusaurus book is deployed, the RAG chatbot provides accurate answers, and user authentication is operational.
- **Deliverables:** A deployed Vercel application containing the Docusaurus book and the integrated RAG chatbot.

## 2. Phase Breakdown

This project is broken down into 10 distinct phases, with a clear folder structure to separate concerns.

- **`frontend/`**: Contains the Docusaurus application, UI components, and all user-facing code.
- **`backend/`**: Contains the FastAPI application, database logic, and AI services.

### Phase 1: Core Repository & Environment Setup
- **Goal:** Initialize the repository, define folder structure, and set up CI/CD pipelines.
- **Folders:**
  - `frontend/`
  - `backend/`
  - `.github/workflows/`

### Phase 2: Docusaurus and Context7 Integration
- **Goal:** Set up the basic Docusaurus site and integrate Context7 for documentation fetching.
- **Folders:**
  - `frontend/docs/`
  - `frontend/docusaurus.config.js`

### Phase 3: Content Structure and Writing Plan
- **Goal:** Create the folder structure for all modules and chapters and establish a writing and asset-gathering plan.
- **Folders:**
  - `frontend/docs/<module-name>/`
  - `frontend/static/img/`

### Phase 4: Authentication Backend (BetterAuth)
- **Goal:** Implement the backend endpoints for user signup, sign-in, and profile management.
- **Folders:**
  - `backend/auth/`
  - `backend/models/` (for Pydantic models)

### Phase 5: Frontend Personalization & Translation
- **Goal:** Build the frontend components for authentication forms, profile management, and the Urdu translation toggle.
- **Folders:**
  - `frontend/src/components/auth/`
  - `frontend/src/theme/` (for Docusaurus component swizzling)

### Phase 6: RAG Backend (FastAPI + OpenAI)
- **Goal:** Develop the core RAG logic, including the FastAPI endpoint and OpenAI Agent SDK integration.
- **Folders:**
  - `backend/rag/`
  - `backend/rag/tools/`

### Phase 7: Database & Vector Store Pipelines
- **Goal:** Set up Neon Postgres schemas and create the data ingestion pipeline for Qdrant.
- **Folders:**
  - `backend/db/`
  - `backend/db/schemas.py`
  - `scripts/ingest_vectors.py`

### Phase 8: Chatbot UI Integration
- **Goal:** Develop and integrate the RAG chatbot React component into the Docusaurus frontend.
- **Folders:**
  - `frontend/src/components/chatbot/`

### Phase 9: Deployment to Vercel
- **Goal:** Configure the project for deployment on Vercel, including serverless functions for the backend.
- **Folders:**
  - `vercel.json`
  - `build.sh` (if needed for complex build steps)

### Phase 10: Testing, QA, and Release
- **Goal:** Perform end-to-end testing, quality assurance, and tag the official `v1.0.0` release.

## 3. Module Writing Timeline

For each of the 5 modules, the following process will be followed:
1.  **Chapter Goals Definition:** Outline key takeaways for each of the 5 chapters.
2.  **Writing Order:** Chapters will be written sequentially (1.1, 1.2, ...).
3.  **Image Schedule:** A list of required images and diagrams will be created before writing begins. Placeholders will be used initially.
4.  **Review Checkpoints:** Each chapter will be reviewed upon completion of its first draft.

## 4. Technical Implementation Plan

### BetterAuth Integration
- **Backend (`backend/auth`):**
  - **Endpoints:**
    - `POST /auth/signup`: Accepts email, password, and background. Creates a user record in Neon DB.
    - `POST /auth/signin`: Authenticates user, returns a JWT.
    - `GET /auth/profile`: Returns profile data for the authenticated user.
    - `PUT /auth/profile`: Updates user preferences (e.g., translation).
- **Frontend (`frontend/src/components/auth`):**
  - React components for Signup and Sign-in forms.
  - A React Context provider to manage authentication state across the application.

### RAG Chatbot
- **Backend (`backend/rag`):**
  - **Endpoint `POST /rag/chat`**:
    1. Receives `query` and `mode` (`full-book` or `selected-text`).
    2. If `selected-text`, use that as the context.
    3. If `full-book`, generate an embedding for the query.
    4. Search Qdrant for the top-k most relevant text chunks.
    5. Pass the query and retrieved chunks to the OpenAI Agent SDK.
    6. The Agent generates a response, citing sources.
    7. Log the interaction in Neon DB and return the response.
- **Vector Store Ingestion (`scripts/ingest_vectors.py`):**
  - A Python script that runs daily.
  - Scans the `frontend/docs/` directory for changes.
  - Reads Markdown files, chunks them into smaller sections.
  - Generates embeddings for each chunk using an OpenAI model.
  - Upserts the vectors and their metadata (chapter/section ID) into a Qdrant collection.

### Docusaurus Frontend
- **Personalization (`frontend/src/theme/`):**
  - Docusaurus component "swizzling" will be used to wrap core layout components.
  - A top-level wrapper will check the auth state and provide user preferences via context.
- **Translation (`frontend/src/theme/`):**
  - A language toggle component will call the `/auth/profile` endpoint to set the user's language preference.
  - Docusaurus's built-in i18n functionality will be used, with the Urdu content potentially being auto-translated and stored.

## 5. Data & Storage Plan

- **Neon Postgres (`backend/db/schemas.py`):**
  - **`users` table:**
    - `id`: UUID (Primary Key)
    - `email`: VARCHAR(255) (Unique)
    - `password_hash`: VARCHAR(255)
    - `background`: JSONB (e.g., `{"software": "pro", "hardware": "beginner"}`)
    - `preferences`: JSONB (e.g., `{"language": "ur"}`)
    - `created_at`: TIMESTAMP
  - **`chat_logs` table:**
    - `id`: UUID (Primary Key)
    - `user_id`: UUID (Foreign Key to `users.id`, nullable)
    - `query`: TEXT
    - `response`: TEXT
    - `timestamp`: TIMESTAMP
- **Qdrant Vector Store:**
  - **Collection:** `robotics_book_content`
  - **Vector:** High-dimensional float array from OpenAI.
  - **Payload:**
    - `content`: The original text chunk.
    - `chapter_id`: e.g., "module-1-chapter-2"
    - `doc_url`: `/docs/module-1/chapter-2`

## 6. GitHub Workflow Plan

- **Branching Strategy:**
  - `main`: Production branch. Automatically deployed to Vercel.
  - `develop`: Integration branch. All feature branches are merged here first.
  - `feature/*`: For new features (e.g., `feature/rag-backend`).
  - `fix/*`: For bug fixes.
- **Pull Request (PR) Flow:**
  - PRs are made from `feature/*` branches into `develop`.
  - PRs require at least one approval and must pass all CI checks.
  - After testing on `develop`, PRs are merged into `main` for release.
- **CI/CD (`.github/workflows/`):**
  - A workflow will trigger on pushes to `develop` and `main`.
  - Jobs:
    1.  `lint`: Run linters on both `frontend` and `backend`.
    2.  `test-backend`: Run Pytest on the `backend`.
    3.  `test-frontend`: Run Jest/Vitest on the `frontend`.
    4.  `build`: Build the Docusaurus site and prepare the FastAPI app.
    5.  `deploy`: On a push to `main`, deploy the combined build to Vercel.

## 7. Risk & Mitigation

- **Risk 1: Content Delay:** The writing and asset creation for 25 chapters is a significant effort.
  - **Mitigation:** Establish a strict content calendar with milestones. Use placeholders for images initially to unblock development.
- **Risk 2: RAG Accuracy:** The chatbot may provide irrelevant or inaccurate answers.
  - **Mitigation:** Implement rigorous testing and a feedback mechanism for users to flag bad answers. Continuously fine-tune the chunking strategy and retrieval parameters.
- **Risk 3: Integration Complexity:** Coordinating the frontend, backend, auth service, and databases can be complex.
  - **Mitigation:** Use phased development. Ensure API contracts are clearly defined and agreed upon early. Use containerization for local development to mirror the production environment.

## 8. Appendix / Checklists

### Pre-Deployment Checklist
- [ ] All CI checks are passing.
- [ ] Environment variables for Vercel are set.
- [ ] Database migrations (if any) are applied.
- [ ] Final E2E tests on a staging environment are complete.

### Chapter Creation Checklist
- [ ] Chapter written in Markdown.
- [ ] All images sourced and placed in `frontend/static/img/`.
- [ ] Frontmatter (title, etc.) is complete.
- [ ] Chapter is added to the `sidebars.js` file in Docusaurus.

### RAG Ingestion Checklist
- [ ] `ingest_vectors.py` script has been run.
- [ ] Vector count in Qdrant collection has increased.
- [ ] Perform a test query to ensure new content is retrievable.
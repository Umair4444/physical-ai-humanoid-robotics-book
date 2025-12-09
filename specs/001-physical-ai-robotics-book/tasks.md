---
description: "Task list for feature implementation"
---

# Tasks: Physical AI & Humanoid Robotics Book

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend**: `frontend/`
- **Backend**: `backend/`
- **Scripts**: `scripts/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [ ] T001 Initialize the monorepo structure with `frontend`, `backend`, and `scripts` directories.
- [ ] T002 Create top-level `.gitignore` configured for Node.js and Python projects.
- [ ] T003 [P] Initialize a Python project with `uv` in the `backend` directory and add FastAPI.
- [ ] T004 [P] Initialize a Node.js project in the `frontend` directory.
- [ ] T005 [P] Create the CI/CD workflow file in `.github/workflows/ci.yml` to lint and test both frontend and backend.
- [ ] T006 [P] Create the deployment workflow file in `.github/workflows/deploy.yml` for Vercel.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [ ] T007 Install Docusaurus in the `frontend` directory.
- [ ] T008 Configure the basic site settings in `frontend/docusaurus.config.js`.
- [ ] T009 Create the initial module folder structure in `frontend/docs/`.
- [ ] T010 [P] Set up the Neon Postgres database and add connection secrets.
- [ ] T011 [P] Set up the Qdrant vector store and add connection secrets.
- [ ] T012 Implement database connection logic in `backend/db/session.py`.

---

## Phase 3: User Story 1 - Read and Learn (Priority: P1) 🎯 MVP

**Goal**: As a reader, I want to navigate through the book's chapters, read the content, and view the images, so that I can learn about humanoid robotics.

**Independent Test**: Given I am on the book's homepage, when I click on "Module 1" and then "Chapter 1.1", the chapter content is displayed correctly with text and images.

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create placeholder Markdown files for all 25 chapters within the `frontend/docs/` subdirectories.
- [ ] T014 [P] [US1] Add placeholder images for Module 1, Chapter 1 to `frontend/static/img/`.
- [ ] T015 [US1] Populate the content for `frontend/docs/module-1/chapter-1-1.md` using the specified chapter template.
- [ ] T016 [US1] Configure the sidebar navigation for all modules and chapters in `frontend/sidebars.js`.

**Checkpoint**: At this point, User Story 1 should be fully functional. The book structure is navigable, and at least one chapter renders correctly.

---

## Phase 4: User Story 3 - Personalize My Experience (Priority: P3)

**Goal**: As a user, I want to sign up and sign in to personalize my experience, such as enabling Urdu translation.

**Independent Test**: Given I am a new user, when I use the "Sign Up" form, my user profile is created. Given I am a registered user, when I sign in, I see a "Profile" button.

### Implementation for User Story 3

- [ ] T017 [P] [US3] Define the `User` Pydantic model in `backend/models/user.py`.
- [ ] T018 [P] [US3] Define the `users` table schema in `backend/db/schemas.py`.
- [ ] T019 [US3] Implement the `/auth/signup` and `/auth/signin` endpoints in `backend/auth/routes.py`.
- [ ] T020 [US3] Implement the `/auth/profile` GET and PUT endpoints in `backend/auth/routes.py`.
- [ ] T021 [P] [US3] Create the `AuthContext` provider in `frontend/src/contexts/AuthContext.js`.
- [ ] T022 [US3] Create the Sign-up and Sign-in form components in `frontend/src/components/auth/`.
- [ ] T023 [US3] "Swizzle" the Docusaurus `Navbar` to add authentication buttons in `frontend/src/theme/Navbar.js`.
- [ ] T024 [US3] Implement the Urdu translation toggle component and integrate with user preferences.

**Checkpoint**: At this point, User Story 3 should be functional. Users can create accounts, log in, and see personalization options.

---

## Phase 5: User Story 2 - Ask the RAG Chatbot (Priority: P2)

**Goal**: As a reader, I want to ask the chatbot a question and get an answer derived from the book's content, so that I can quickly clarify concepts.

**Independent Test**: Given the chatbot UI is open, when I ask "What is SLAM?", I receive a concise answer with a source link to the relevant chapter.

### Implementation for User Story 2

- [ ] T025 [P] [US2] Install OpenAI and Qdrant client libraries in `backend/`.
- [ ] T026 [P] [US2] Define the `chat_logs` table schema in `backend/db/schemas.py`.
- [ ] T027 [US2] Create the vector ingestion script in `scripts/ingest_vectors.py` to process and store chapter content in Qdrant.
- [ ] T028 [US2] Implement the core RAG service in `backend/rag/service.py` to query Qdrant and generate answers with the OpenAI SDK.
- [ ] T029 [US2] Implement the `/rag/chat` endpoint in `backend/rag/routes.py`.
- [ ] T030 [P] [US2] Design and create the Chatbot UI component in `frontend/src/components/chatbot/Chatbot.js`.
- [ ] T031 [US2] Implement the client-side logic to call the `/rag/chat` endpoint from the chatbot UI.
- [ ] T032 [US2] Integrate the Chatbot component into the Docusaurus layout as a floating action button.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T033 [P] Create `vercel.json` file and configure for monorepo deployment.
- [ ] T034 [P] Create `.env.example` files for both `frontend` and `backend` to document required variables.
- [ ] T035 Write end-to-end tests covering the main user flows (reading, signing in, asking a question).
- [ ] T036 Perform final QA, code cleanup, and documentation review.
- [ ] T037 Tag the `v1.0.0` release and merge to `main`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion. BLOCKS all user stories.
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion.
- **Polish (Phase 6)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational. No dependencies on other stories.
- **User Story 3 (P3)**: Can start after Foundational. No dependencies on other stories.
- **User Story 2 (P2)**: Depends on US1 for content to be available. The ingestion script needs the chapter files.

### Parallel Opportunities

- Once Phase 2 is complete, work on US1 and US3 can happen in parallel.
- The backend and frontend work within a single user story can often be parallelized (e.g., T017-T020 can be done while T021-T024 are in progress).

---

## Parallel Example: User Story 3

```bash
# Backend team can work on the auth API
Task: "Implement the /auth/signup and /auth/signin endpoints in backend/auth/routes.py"

# Frontend team can simultaneously work on the UI components
Task: "Create the Sign-up and Sign-in form components in frontend/src/components/auth/"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently. The book is readable.
5. Deploy/demo if ready.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!).
3.  Add User Story 3 → Test independently → Deploy/Demo.
4.  Add User Story 2 → Test independently → Deploy/Demo.
5.  Each story adds value without breaking previous stories.

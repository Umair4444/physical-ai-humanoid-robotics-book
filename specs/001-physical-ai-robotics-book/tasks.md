---

description: "Task list for Physical AI & Humanoid Robotics Book feature implementation"
---

# Tasks: Physical AI & Humanoid Robotics Book

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks are not explicitly requested, therefore they are omitted.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Project Initialization)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directories: `backend/`, `frontend/`
- [x] T002 Initialize Docusaurus project in `frontend/`
- [x] T003 Initialize FastAPI project in `backend/`
- [x] T004 Setup Python virtual environment and install dependencies for backend (`uv`) in `backend/`
- [x] T005 Setup Node.js dependencies for frontend (`npm`) in `frontend/`
- [x] T006 Configure basic `backend/src/` and `frontend/src/` structures.
- [x] T007 Configure `.gitignore` for frontend and backend in repository root
- [x] T008 Create `pyproject.toml` for backend with project metadata and dependencies in `backend/`
- [x] T009 Create `requirements.txt` for backend in `backend/`
- [x] T010 Configure `package.json` scripts for frontend (e.g., `start`, `build`) in `frontend/package.json`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T011 Implement environment variable loading in `backend/src/config.py`
- [x] T012 Setup Alembic for database migrations in `backend/`
- [x] T013 Initialize Neon Postgres connection in `backend/src/database.py`
- [x] T014 Configure Qdrant client in `backend/src/vector_db.py`
- [x] T015 Implement base FastAPI application with CORS and basic error handling in `backend/src/main.py`
- [x] T016 Setup basic structured logging in `backend/src/utils/logger.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Read and Learn (Priority: P1) 🎯 MVP

**Goal**: As a reader, I want to navigate through the book's chapters, read the content, and view the images, so that I can learn about humanoid robotics.

**Independent Test**: Navigate to each chapter and verify content and images are displayed correctly.

### Implementation for User Story 1

- [x] T017 [P] [US1] Update Docusaurus config `docusaurus.config.ts` for book structure and sidebar in `frontend/docusaurus.config.ts`
- [x] T018 [US1] Create markdown files for Module 1, Chapters 1.1-1.5 in `frontend/docs/module-1/`
- [x] T019 [US1] Create markdown files for Module 2, Chapters 2.1-2.5 in `frontend/docs/module-2/`
- [x] T020 [US1] Create markdown files for Module 3, Chapters 3.1-3.5 in `frontend/docs/module-3/`
- [x] T021 [US1] Create markdown files for Module 4, Chapters 4.1-4.5 in `frontend/docs/module-4/`
- [x] T022 [US1] Create markdown files for Module 5, Chapters 5.1-5.5 in `frontend/docs/module-5/`
- [x] T023 [P] [US1] Add placeholder content and images as per `spec.md` template for all chapters in their respective markdown files.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ask the RAG Chatbot (Priority: P2)

**Goal**: As a reader, I want to ask the chatbot a question and get an answer derived from the book's content, so that I can quickly clarify concepts.

**Independent Test**: Ask the chatbot various in-domain questions and verify accurate answers with source links, and test "selected-text only" mode.

### Implementation for User Story 2

- [x] T024 [P] [US2] Implement `ChapterVector` model for Qdrant in `backend/src/models/chapter_vector.py`
- [x] T025 [US2] Implement `RAGLog` model in `backend/src/models/rag_log.py`
- [x] T026 [P] [US2] Create `rag_service.py` for OpenAI Agent SDK integration in `backend/src/services/rag_service.py`
- [x] T027 [P] [US2] Implement content vectorization logic in `backend/src/services/vectorization_service.py`
- [x] T028 [US2] Implement `POST /rag/query` endpoint in `backend/src/api/rag.py`
- [x] T029 [P] [US2] Develop basic Docusaurus Chatbot UI component in `frontend/src/components/Chatbot.tsx`
- [x] T030 [US2] Connect frontend Chatbot UI to backend `/rag/query` endpoint
- [x] T031 [US2] Implement "selected-text only" mode logic in frontend and backend
- [x] T032 [P] [US2] Implement daily update mechanism for RAG knowledge base (e.g., a background job/cron)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Personalize My Experience (Priority: P3)

**Goal**: As a user, I want to sign up and sign in to personalize my experience, such as enabling Urdu translation.

**Independent Test**: Register a new user, sign in, update profile, and verify translation toggle functionality.

### Implementation for User Story 3

- [x] T033 [P] [US3] Implement `UserProfile` model in `backend/src/models/user_profile.py`
- [x] T034 [P] [US3] Create `auth_service.py` for BetterAuth integration in `backend/src/services/auth_service.py`
- [x] T035 [P] [US3] Implement `POST /auth/signup` endpoint in `backend/src/api/auth.py`
- [x] T036 [P] [US3] Implement `POST /auth/signin` endpoint in `backend/src/api/auth.py`
- [x] T037 [P] [US3] Implement `GET /users/me` endpoint in `backend/src/api/users.py`
- [x] T038 [P] [US3] Implement `PUT /users/me` endpoint in `backend/src/api/users.py`
- [x] T039 [P] [US3] Develop Docusaurus SignUp/SignIn UI components in `frontend/src/components/Auth.tsx`
- [x] T040 [P] [US3] Create user profile page (`frontend/src/pages/profile.tsx`) with personalization options
- [x] T041 [P] [US3] Implement UI for Urdu translation toggle and apply translation via Docusaurus i18n

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T042 Implement retry mechanisms with exponential backoff and circuit breakers in `backend/src/utils/resilience.py`
- [x] T043 Refine logging and metrics integration across backend services
- [x] T044 Implement user-friendly error messages and fallback content in both frontend and backend
- [x] T045 Configure Vercel deployment for frontend and backend (includes `vercel.json` and build scripts)
- [x] T046 Document build commands and environment variables in `README.md`
- [x] T047 Setup pre-commit hooks for Conventional Commits

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models, services, or UI components for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Update Docusaurus config and create chapter markdown files:
Task: "T017 [P] [US1] Update Docusaurus config docusaurus.config.ts for book structure and sidebar in frontend/docusaurus.config.ts"
Task: "T018 [US1] Create markdown files for Module 1, Chapters 1.1-1.5 in frontend/docs/module-1/"
Task: "T019 [US1] Create markdown files for Module 2, Chapters 2.1-2.5 in frontend/docs/module-2/"
Task: "T020 [US1] Create markdown files for Module 3, Chapters 3.1-3.5 in frontend/docs/module-3/"
Task: "T021 [US1] Create markdown files for Module 4, Chapters 4.1-4.5 in frontend/docs/module-4/"
Task: "T022 [US1] Create markdown files for Module 5, Chapters 5.1-5.5 in frontend/docs/module-5/"
Task: "T023 [P] [US1] Add placeholder content and images as per spec.md template for all chapters in their respective markdown files."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

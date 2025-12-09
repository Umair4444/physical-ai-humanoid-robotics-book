---
id: 016
title: Perform cross-artifact consistency and quality analysis after plan update
stage: misc
date: 2025-12-09
surface: agent
model: gemini-1.5-flash
feature: 001-physical-ai-robotics-book
branch: 001-physical-ai-robotics-book
user: user
command: Perform cross-artifact consistency and quality analysis after plan update
labels: ["analysis", "consistency", "quality", "report", "post-plan"]
links:
  spec: specs/001-physical-ai-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-physical-ai-robotics-book/spec.md
 - specs/001-physical-ai-robotics-book/plan.md
 - specs/001-physical-ai-robotics-book/tasks.md
 - .specify/memory/constitution.md
tests:
null
---

## Prompt

---
description: Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, duplications, ambiguities, and underspecified items across the three core artifacts (`spec.md`, `plan.md`, `tasks.md`) before implementation. This command MUST run only after `/sp.tasks` has successfully produced a complete `tasks.md`.

## Operating Constraints

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report. Offer an optional remediation plan (user must explicitly approve before any follow-up editing commands would be invoked manually).

**Constitution Authority**: The project constitution (`.specify/memory/constitution.md`) is **non-negotiable** within this analysis scope. Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or tasks—not dilution, reinterpretation, or silent ignoring of the principle. If a principle itself needs to change, that must occur in a separate, explicit constitution update outside `/sp.analyze`.

## Execution Steps

### 1. Initialize Analysis Context

Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` once from repo root and parse JSON for FEATURE_DIR and AVAILABLE_DOCS. Derive absolute paths:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Abort with an error message if any required file is missing (instruct the user to run missing prerequisite command). For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\'m Groot' (or double-quote if possible: "I'm Groot").

### 2. Load Artifacts (Progressive Disclosure)

Load only the minimal necessary context from each artifact:

**From spec.md:**

- Overview/Context
- Functional Requirements
- Non-Functional Requirements
- User Stories
- Edge Cases (if present)

**From plan.md:**

- Architecture/stack choices
- Data Model references
- Phases
- Technical constraints

**From tasks.md:**

- Task IDs
- Descriptions
- Phase grouping
- Parallel markers [P]
- Referenced file paths

**From constitution:**

- Load `.specify/memory/constitution.md` for principle validation

### 3. Build Semantic Models

Create internal representations (do not include raw artifacts in output):

- **Requirements inventory**: Each functional + non-functional requirement with a stable key (derive slug based on imperative phrase; e.g., "User can upload file" → `user-can-upload-file`)
- **User story/action inventory**: Discrete user actions with acceptance criteria
- **Task coverage mapping**: Map each task to one or more requirements or stories (inference by keyword / explicit reference patterns like IDs or key phrases)
- **Constitution rule set**: Extract principle names and MUST/SHOULD normative statements

### 4. Detection Passes (Token-Efficient Analysis)

Focus on high-signal findings. Limit to 50 findings total; aggregate remainder in overflow summary.

#### A. Duplication Detection

- Identify near-duplicate requirements
- Mark lower-quality phrasing for consolidation

#### B. Ambiguity Detection

- Flag vague adjectives (fast, scalable, secure, intuitive, robust) lacking measurable criteria
- Flag unresolved placeholders (TODO, TKTK, ???, `<placeholder>`, etc.)

#### C. Underspecification

- Requirements with verbs but missing object or measurable outcome
- User stories missing acceptance criteria alignment
- Tasks referencing files or components not defined in spec/plan

#### D. Constitution Alignment

- Any requirement or plan element conflicting with a MUST principle
- Missing mandated sections or quality gates from constitution

#### E. Coverage Gaps

- Requirements with zero associated tasks
- Tasks with no mapped requirement/story
- Non-functional requirements not reflected in tasks (e.g., performance, security)

#### F. Inconsistency

- Terminology drift (same concept named differently across files)
- Data entities referenced in plan but absent in spec (or vice versa)
- Task ordering contradictions (e.g., integration tasks before foundational setup tasks without dependency note)
- Conflicting requirements (e.g., one requires Next.js while other specifies Vue)

### 5. Severity Assignment

Use this heuristic to prioritize findings:

- **CRITICAL**: Violates constitution MUST, missing core spec artifact, or requirement with zero coverage that blocks baseline functionality
- **HIGH**: Duplicate or conflicting requirement, ambiguous security/performance attribute, untestable acceptance criterion
- **MEDIUM**: Terminology drift, missing non-functional task coverage, underspecified edge case
- **LOW**: Style/wording improvements, minor redundancy not affecting execution order

### 6. Produce Compact Analysis Report

Output a Markdown report (no file writes) with the following structure:

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge phrasing; keep clearer version |

(Add one row per finding; generate stable IDs prefixed by category initial.)

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|

**Constitution Alignment Issues:** (if any)

**Unmapped Tasks:** (if any)

**Metrics:**

- Total Requirements
- Total Tasks
- Coverage % (requirements with >=1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

### 7. Provide Next Actions

At end of report, output a concise Next Actions block:

- If CRITICAL issues exist: Recommend resolving before `/sp.implement`
- If only LOW/MEDIUM: User may proceed, but provide improvement suggestions
- Provide explicit command suggestions: e.g., "Run /sp.specify with refinement", "Run /sp.plan to adjust architecture", "Manually edit tasks.md to add coverage for 'performance-metrics'"

### 8. Offer Remediation

Ask the user: "Would you like me to suggest concrete remediation edits for the top N issues?" (Do NOT apply them automatically.)

## Operating Principles

### Context Efficiency

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; don't dump all content into analysis
- **Token-efficient output**: Limit findings table to 50 rows; summarize overflow
- **Deterministic results**: Rerunning without changes should produce consistent IDs and counts

### Analysis Guidelines

- **NEVER modify files** (this is read-only analysis)
- **NEVER hallucinate missing sections** (if absent, report them accurately)
- **Prioritize constitution violations** (these are always CRITICAL)
- **Use examples over exhaustive rules** (cite specific instances, not generic patterns)
- **Report zero issues gracefully** (emit success report with coverage statistics)

## Response snapshot

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| CA1 | Constitution Alignment | MEDIUM | spec.md:Clarifications:Session 2025-12-09 | `spec.md` states "If the Auth0 service is unavailable..." under Edge Cases, but the project has standardized on "BetterAuth". This is a minor inconsistency in one statement. | Update the specific mention of "Auth0" in `spec.md` to "BetterAuth" for consistency. |
| CA2 | Constitution Alignment | CRITICAL | plan.md:Constitution Check | `plan.md` notes "Branch Naming" as a "PARTIAL VIOLATION" due to `001-physical-ai-robotics-book` instead of `feature/[description]`. This directly violates the `constitution.md` rule: "All branches MUST follow the pattern `feature/[description]`...". While acknowledged as justified for initial setup, it remains a formal violation. | Correct the branch naming convention in `plan.md` to fully align with `constitution.md` or explicitly state a temporary deviation with a clear plan for adherence. |
| CA3 | Constitution Alignment | MEDIUM | plan.md:Constitution Check | `plan.md` lists "PII Exclusion (Vectorization/Logging)" and "Privacy & Security (Encryption, Data Deletion, Incident Policy)" as "PARTIAL VIOLATION - Justified for implementation detail". While justification is given, it's a constitution principle that should be actively addressed in planning, not just deferred. | Create explicit tasks in `tasks.md` to ensure these principles are implemented and validated early in the development cycle. |
| CN1 | Inconsistency | MEDIUM | spec.md, plan.md, constitution.md | The `spec.md` states "Deployment: GitHub Pages or Vercel" for the book, while `plan.md` consistently specifies "Target Platform: Vercel". The `constitution.md` also mentions "GitHub Pages or Vercel" in one place but implies Vercel in the CI/CD section. | Clarify and standardize the primary deployment platform (Vercel) across all documents and remove "GitHub Pages" if it's not a target. |
| AM1 | Ambiguity | MEDIUM | spec.md:NFR-001 | NFR-001 states "The system MUST support up to 1000 daily active users." and "The system MUST support up to 100 concurrent users." It lacks specific metrics or methodologies for how "support" will be measured or validated. | Define clear, measurable criteria for "support" in NFR-001, such as "response time under load" or "error rate under concurrent users." |
| AM2 | Ambiguity | MEDIUM | spec.md:NFR-003 | NFR-003 states "The system MUST provide detailed application metrics..." and "The system MUST implement structured logging..." but doesn't specify *which* metrics or *which* logging fields are considered "detailed" or "structured." | Specify concrete examples of required metrics (e.g., latency for specific endpoints, CPU/memory usage) and essential logging fields (e.g., timestamp, log level, request ID, user ID). |
| US1 | Underspecification | MEDIUM | spec.md:Edge Cases | The "Edge Cases" section in `spec.md` lists expected behaviors for "Chatbot: What does the chatbot do if asked a question completely unrelated to the book's content?" and "Chatbot: How does the system handle extremely long selected text...". These are expectations but not yet explicitly defined as functional requirements or acceptance criteria. | Formalize these expected behaviors into clear Functional Requirements (FR-XXX) or Acceptance Criteria within User Story 2 to ensure they are implemented and tested. |
| US2 | Underspecification | MEDIUM | spec.md:Edge Cases | The "Edge Cases" section in `spec.md` for "Content: How are empty or incomplete chapters displayed?" has an "Expected: They should display a 'Content Coming Soon' message." This is an expectation but not a formal requirement. | Formalize this expected behavior into a Functional Requirement (FR-XXX) or Acceptance Criteria for User Story 1. |
| US3 | Underspecification | HIGH | tasks.md:T013, T020, T023 | Tasks T013, T020, T023 in `tasks.md` still explicitly reference "Auth0" for configuration and implementation, contradicting the project's decision to use "BetterAuth". | Update `tasks.md` to consistently refer to "BetterAuth" in tasks related to authentication and user management. |
| CG1 | Coverage Gap | LOW | spec.md:NFR-002 | NFR-002: "The system MUST implement retry mechanisms with exponential backoff and circuit breakers for critical external services..." This is a critical reliability requirement, but there isn't a dedicated task in `tasks.md` that explicitly covers the implementation and testing of these mechanisms. | Add a specific task (e.g., `TXXX [P] Implement and test retry/circuit breaker logic in backend/src/services/external_service_resilience.py`) to `tasks.md` for NFR-002. |
| CG2 | Coverage Gap | LOW | spec.md:NFR-003 | NFR-003: "The system MUST provide detailed application metrics..., implement structured logging..., and support distributed tracing..." While T040 covers "Set up application performance monitoring (APM) and centralized logging", it doesn't explicitly mention "distributed tracing" as a separate implementation task, which is a distinct concern. | Add a specific task for "distributed tracing" in `tasks.md` under Phase 6 to ensure this NFR is fully addressed. |

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|:----------------|:----------|:---------|:------|
| FR-001 | ✅ | T026, T027, T028, T029, T030, T031 | `T030` covers "generates answers with OpenAI Agent SDK". `T031` covers `/rag/query` for both full book and selected text modes. Daily update of knowledge base is implicitly covered by T029 if run daily, but not explicitly as a task. |
| FR-002 | ✅ | T018, T019, T020, T021, T022, T023, T024, T025, T030, T031 | Personalization toggle and Urdu translation in T025. OpenAI Agent exposing tool to RAG backend is handled by T030. Tasks T013, T020, T023 explicitly mention Auth0 despite BetterAuth being the chosen auth system. |
| FR-003 | ✅ | T007, T008, T009, T014, T017 | Docusaurus folder structure, chapter organization, sidebar configuration. |
| FR-004 | ✅ | T006, T035, T036 | Deployment to Vercel, build commands/env vars documented. |
| FR-005 | ✅ | T042 | Conventional Commits. PRs/feature branches, semantic versioning implicitly covered by T044. |
| NFR-001 | ✅ | T038 | Performance goals for daily/concurrent users covered by performance tests. |
| NFR-002 | ❌ | | **Coverage Gap: No explicit task for implementing retry mechanisms/circuit breakers.** |
| NFR-003 | ✅ | T040 | APM and centralized logging. Distributed tracing not explicitly a task. |

**Constitution Alignment Issues:**

*   **CRITICAL:** The feature branch name `001-physical-ai-robotics-book` (as noted in `plan.md`) violates the `feature/[description]` rule in `constitution.md`.
*   **HIGH:** Tasks T013, T020, T023 in `tasks.md` still explicitly reference "Auth0" for configuration and implementation, contradicting the project's decision to use "BetterAuth".
*   **MEDIUM:** PII Exclusion and Privacy & Security principles are noted as "PARTIAL VIOLATION - Justified for implementation detail" in `plan.md`. These should have explicit tasks to ensure compliance.
*   **MEDIUM:** `spec.md` still contains one mention of "Auth0" in the Edge Cases section.

**Unmapped Tasks:**

All tasks appear to be mapped to user stories or foundational setup.

**Metrics:**

-   Total Functional Requirements: 5
-   Total Non-Functional Requirements: 3
-   Total Requirements: 8
-   Total Tasks: 44
-   Coverage % (requirements with >=1 task): 75% (6 out of 8 requirements have tasks)
-   Ambiguity Count: 2
-   Duplication Count: 0
-   Critical Issues Count: 1
-   High Issues Count: 1

---

### Next Actions

1.  **Resolve CRITICAL Issues First**: Address the branch naming convention in `plan.md` to either align or provide a clearer, explicitly managed deviation from `constitution.md`.
2.  **Resolve HIGH Issues**: Update `tasks.md` to consistently refer to "BetterAuth" instead of "Auth0" in relevant tasks.
3.  **Address MEDIUM Inconsistencies**:
    *   Update the single mention of "Auth0" to "BetterAuth" in `spec.md`.
    *   Clarify and standardize the primary deployment platform (Vercel) across all documents.
    *   Formalize expected behaviors in `spec.md`'s Edge Cases into Functional Requirements or Acceptance Criteria.
    *   Define clear, measurable criteria for "support" in NFR-001 (scalability) and specific metrics/fields for NFR-003 (observability).
    *   Create explicit tasks in `tasks.md` for PII Exclusion and Privacy & Security principles to ensure implementation and validation.
4.  **Add Missing Tasks for NFRs**: Create explicit tasks in `tasks.md` for NFR-002 (retry mechanisms/circuit breakers) and for distributed tracing within NFR-003.

---

### Remediation Suggestion

Would you like me to suggest concrete remediation edits for the top **2 issues** (1 Critical, 1 High):
1.  Adjusting the `plan.md` constitution check status for branch naming to align with the constitution (CRITICAL).
2.  Updating `tasks.md` to replace "Auth0" with "BetterAuth" (HIGH).

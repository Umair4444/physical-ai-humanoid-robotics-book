---
id: 015
title: Generate Implementation Plan for Robotics Book
stage: plan
date: 2025-12-09
surface: agent
model: gemini-1.5-flash
feature: 001-physical-ai-robotics-book
branch: 001-physical-ai-robotics-book
user: user
command: Execute implementation planning workflow
labels: ["plan", "implementation", "design", "contracts", "quickstart"]
links:
  spec: specs/001-physical-ai-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-physical-ai-robotics-book/plan.md
 - specs/001-physical-ai-robotics-book/research.md
 - specs/001-physical-ai-robotics-book/data-model.md
 - specs/001-physical-ai-robotics-book/contracts/auth.yaml
 - specs/001-physical-ai-robotics-book/contracts/rag.yaml
 - specs/001-physical-ai-robotics-book/quickstart.md
tests:
null
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType gemini`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

## Response snapshot

The implementation planning workflow has been successfully executed, generating design artifacts and updating the agent context.

-   **Branch**: `001-physical-ai-robotics-book`
-   **IMPL_PLAN path**: `specs/001-physical-ai-robotics-book/plan.md`
-   **Generated artifacts**:
    *   `specs/001-physical-ai-robotics-book/research.md`
    *   `specs/001-physical-ai-robotics-book/data-model.md`
    *   `specs/001-physical-ai-robotics-book/contracts/auth.yaml`
    *   `specs/001-physical-ai-robotics-book/contracts/rag.yaml`
    *   `specs/001-physical-ai-robotics-book/quickstart.md`

## Outcome

- ✅ Impact: Generated a comprehensive implementation plan, including research, data model, API contracts, and a quickstart guide.
- 🧪 Tests: No new tests were generated for this planning task.
- 📁 Files: 5 new design artifacts were created and one was updated (`plan.md`).
- 🔁 Next prompts: Review the generated artifacts, proceed to `/sp.tasks` to generate detailed implementation tasks.
- 🧠 Reflection: The workflow successfully generated all required design artifacts, providing a solid foundation for the implementation phase. The previous clarification regarding authentication (BetterAuth) was successfully integrated.

## Evaluation notes (flywheel)

- Failure modes observed: The `plan.md` file initially being a template highlighted a potential gap in the `/sp.plan` command's initial population, requiring manual reconstruction during this execution.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Review the `/sp.plan` command script to ensure it robustly populates `plan.md` on initial execution.

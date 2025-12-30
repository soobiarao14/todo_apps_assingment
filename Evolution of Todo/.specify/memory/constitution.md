<!--
=============================================================================
SYNC IMPACT REPORT
=============================================================================
Version Change: [No previous version] → 1.0.0
Change Type: MAJOR (Initial ratification)
Date: 2025-12-30

Modified Principles:
- NEW: I. Spec-Driven Development (Mandatory)
- NEW: II. Agent Behavior & Human Restrictions
- NEW: III. Phase Governance
- NEW: IV. Technology Constraints
- NEW: V. Quality & Architecture Principles
- NEW: VI. Feature Maturity Levels

Added Sections:
- Technology Stack
- Phase Boundaries
- Development Workflow

Removed Sections: N/A (initial version)

Templates Requiring Updates:
✅ .specify/templates/plan-template.md - Constitution Check section references this file
✅ .specify/templates/spec-template.md - Aligns with mandatory spec-first approach
✅ .specify/templates/tasks-template.md - Enforces spec → plan → tasks workflow
⚠️  .specify/templates/phr-template.prompt.md - No changes needed (recording only)
⚠️  .specify/templates/adr-template.md - No changes needed (decision recording)
⚠️  .specify/templates/checklist-template.md - No changes needed (validation tool)
⚠️  .specify/templates/agent-file-template.md - No changes needed (agent definition)

Follow-up TODOs: None - all placeholders filled

Constitution Authority: This document is the SUPREME governing document for
the Evolution of Todo project. All agents, workflows, and development
practices MUST comply with these principles. No deviation is permitted
without constitutional amendment.
=============================================================================
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (MANDATORY)

All development in the Evolution of Todo project MUST follow Spec-Driven Development without exception. This principle is NON-NEGOTIABLE across all phases.

**Mandatory Execution Order**:
1. Constitution (this document) - supreme governing law
2. Specifications (`specs/*/spec.md`) - what to build
3. Plan (`specs/*/plan.md`) - how to build it
4. Tasks (`specs/*/tasks.md`) - step-by-step implementation
5. Implementation - code execution only

**Enforcement Rules**:
- No agent may write code without approved specifications and tasks
- All refinements and changes MUST occur at the specification level
- Any deviation from this workflow is a constitutional violation
- Specifications are version-controlled and reviewed before approval
- Tasks must be derived from approved specs and plans, never invented

**Rationale**: Spec-first development ensures all stakeholders agree on requirements before expensive implementation begins. This prevents rework, scope creep, and architectural drift.

### II. Agent Behavior & Human Restrictions

Agents are autonomous implementers operating under strict constitutional constraints. Humans are architects and approvers, not coders.

**Agent Constraints**:
- Agents MUST NOT invent features beyond approved specifications
- Agents MUST NOT deviate from approved specifications
- Agents MUST NOT skip steps in the spec-driven workflow
- Agents MUST refuse implementation if specs or tasks are missing or invalid
- Agents MUST operate deterministically in early phases (I-III)

**Human Constraints**:
- Humans are STRICTLY FORBIDDEN from manual coding
- Humans provide specifications, review plans, approve tasks
- Humans may refine specs and plans, never code directly
- Code modifications require spec updates followed by agent re-implementation

**Rationale**: Clear separation of concerns - humans design systems, agents implement them reliably and consistently. Manual coding introduces unpredictability and violates the deterministic execution model.

### III. Phase Governance

The Evolution of Todo project evolves through five strictly defined phases. Each phase has absolute boundaries that cannot be violated.

**Phase Boundaries**:
- Each phase is scoped by its approved specification document
- Features from future phases MUST NOT appear in earlier phases
- Phase transitions require new specifications and constitutional validation
- Architecture may evolve only through updated specifications and plans
- No experimental or undocumented behavior is allowed in any phase

**Phase Integrity Rules**:
- Phase I deliverables cannot include Phase II technologies
- Each phase must be independently deployable and testable
- Cross-phase dependencies are prohibited
- Phase completion requires passing all quality gates defined in specifications

**Rationale**: Strict phase boundaries ensure predictable evolution, enable incremental deployment, prevent premature optimization, and maintain project discipline.

### IV. Technology Constraints

Only pre-approved technologies may be used in the Evolution of Todo project. Technology selection is phase-gated and version-controlled.

**Approved Technology Stack**:

**Backend (All Phases)**:
- Python 3.11+
- FastAPI (Phase II onward)
- SQLModel (Phase II onward)
- Neon Database (Phase II onward - PostgreSQL-compatible)

**Frontend (Phase II Onward)**:
- Next.js 14+ with App Router
- React 18+
- TypeScript 5+

**AI & Agent Integration (All Phases)**:
- OpenAI Agents SDK
- OpenAI ChatKit
- Official Model Context Protocol (MCP) SDK
- Claude Code with Spec-Driven Development extensions

**Infrastructure (Phase IV-V Only)**:
- Docker & Docker Compose
- Kubernetes (k8s)
- Minikube (local development)
- Apache Kafka (event streaming)
- Dapr (distributed application runtime)

**Technology Introduction Rules**:
- No technology outside this list may be used without constitutional amendment
- New technologies require justification in ADR (Architecture Decision Record)
- Technology upgrades within approved families (e.g., Python 3.11 → 3.12) allowed
- Framework changes require specification update and phase boundary validation

**Rationale**: Constrained technology choices prevent analysis paralysis, ensure agent competency, reduce complexity, and maintain long-term supportability.

### V. Quality & Architecture Principles

All code and architecture must adhere to clean architecture principles and measurable quality standards.

**Architecture Requirements**:
- Clean architecture is MANDATORY (separation of concerns, dependency inversion)
- Clear separation between layers: presentation, business logic, data access
- Stateless services MUST be used where applicable (API handlers, MCP tools)
- Deterministic behavior in Phases I-III (no random IDs, timestamps, or external API calls)
- Cloud-native readiness preserved throughout evolution (12-factor app principles)

**Code Quality Standards**:
- Readability: Code is written for humans first, computers second
- Maintainability: Single Responsibility Principle strictly enforced
- Simplicity: YAGNI (You Aren't Gonna Need It) - no speculative features
- Testability: All business logic must be unit-testable in isolation
- Documentation: Public APIs documented with clear contracts and examples

**Quality Gates**:
- Unit test coverage: ≥80% line coverage, ≥75% branch coverage
- Integration test coverage: 100% for API endpoints and authentication flows
- API contract compliance: 100% (verified against OpenAPI specs)
- Security scans: Zero HIGH or CRITICAL vulnerabilities
- Performance benchmarks: Meet phase-specific SLAs (defined in specs)

**Rationale**: Quality is non-negotiable. Technical debt compounds exponentially; preventing it costs less than fixing it. Clean architecture enables phase transitions without rewrites.

### VI. Feature Maturity Levels

The Todo application evolves through logical maturity levels. Features are implemented only when phase specifications explicitly authorize them.

**CRITICAL DISTINCTION**: These are maturity levels, NOT phases. Phase specifications determine which maturity levels are implemented in each phase.

**BASIC Level (Core Essentials)**:
- Add Task (title, description)
- Delete Task (by ID)
- Update Task (modify title, description, status)
- View Task List (all user tasks)
- Mark Task as Complete / Incomplete (toggle status)

**INTERMEDIATE Level (Organization & Usability)**:
- Priorities (high, medium, low)
- Tags/Labels (categorization)
- Due Dates (deadline management)
- Search & Filter (find tasks by criteria)
- Sort Options (by date, priority, status)

**ADVANCED Level (Collaboration & Intelligence)**:
- User Accounts & Authentication (JWT-based)
- Shared Tasks (multi-user collaboration)
- Task Assignment (delegate to team members)
- Comments & Notes (task discussions)
- AI-Powered Suggestions (smart recommendations via MCP)

**EXPERT Level (Automation & Integration)**:
- Recurring Tasks (automated creation)
- Reminders & Notifications (alerts)
- File Attachments (task-related documents)
- Third-Party Integrations (calendar sync, email)
- Analytics & Insights (productivity metrics)

**ENTERPRISE Level (Scale & Governance)**:
- Real-Time Collaboration (WebSocket-based)
- Event-Driven Architecture (Kafka-based task events)
- Role-Based Access Control (RBAC)
- Audit Logs (compliance tracking)
- Multi-Tenancy (organization isolation)

**Implementation Rules**:
- Features implemented strictly according to phase specifications
- No "sneak preview" features from higher maturity levels
- Each maturity level must be stable before advancing
- Maturity level progression documented in ADRs

**Rationale**: Logical maturity levels provide a roadmap without prescribing timeline. They guide incremental value delivery while maintaining architectural coherence.

## Technology Stack

### Phase-Technology Matrix

| Technology | Phase I | Phase II | Phase III | Phase IV | Phase V |
|------------|---------|----------|-----------|----------|---------|
| Python Core | ✅ | ✅ | ✅ | ✅ | ✅ |
| FastAPI | ❌ | ✅ | ✅ | ✅ | ✅ |
| SQLModel | ❌ | ✅ | ✅ | ✅ | ✅ |
| Neon DB | ❌ | ✅ | ✅ | ✅ | ✅ |
| Next.js | ❌ | ✅ | ✅ | ✅ | ✅ |
| MCP SDK | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAI SDK | ✅ | ✅ | ✅ | ✅ | ✅ |
| Docker | ❌ | ❌ | ❌ | ✅ | ✅ |
| Kubernetes | ❌ | ❌ | ❌ | ✅ | ✅ |
| Kafka | ❌ | ❌ | ❌ | ❌ | ✅ |
| Dapr | ❌ | ❌ | ❌ | ❌ | ✅ |

**Dependency Management**:
- All dependencies version-pinned in `requirements.txt` (Python) and `package.json` (Node.js)
- Security updates allowed within major version (e.g., FastAPI 0.109.0 → 0.109.2)
- Major version upgrades require ADR and specification update

## Phase Boundaries

### Phase I: Foundation
**Scope**: Spec-Driven Development infrastructure, constitutional framework, template system
**Deliverables**: Constitution, templates, PHR system, ADR framework
**Technologies**: Python, MCP SDK, OpenAI SDK
**No Feature Implementation**: Phase I establishes governance only

### Phase II: Core Application
**Scope**: Basic and Intermediate maturity levels (as specified)
**Deliverables**: FastAPI backend, SQLModel entities, Next.js frontend, authentication
**Technologies**: All Phase I + FastAPI, SQLModel, Neon DB, Next.js
**Feature Limit**: No collaboration, no AI features beyond basic MCP integration

### Phase III: AI Integration
**Scope**: MCP tool expansion, AI-powered features (as specified)
**Deliverables**: Advanced MCP tools, ChatKit UI, intelligent task management
**Technologies**: All Phase II + ChatKit enhancements
**Feature Limit**: No real-time collaboration, no event-driven architecture

### Phase IV: Cloud-Native
**Scope**: Containerization, orchestration, scalability
**Deliverables**: Docker images, Kubernetes manifests, Helm charts, observability
**Technologies**: All Phase III + Docker, Kubernetes, Minikube
**Feature Limit**: No event streaming, no Dapr integration

### Phase V: Event-Driven
**Scope**: Kafka-based event streaming, Dapr integration, enterprise features
**Deliverables**: Event-driven architecture, CQRS patterns, distributed tracing
**Technologies**: All Phase IV + Kafka, Dapr
**Feature Limit**: Defined by Phase V specification

**Phase Transition Rules**:
- Each phase requires completed specifications, approved plans, and executed tasks
- Quality gates must pass before phase transition (defined in phase specs)
- Architecture Decision Records document all significant phase decisions
- No backward transitions - phases are one-way gates

## Development Workflow

### Spec-Driven Execution Model

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CONSTITUTION (this file)                                 │
│    - Supreme governing law                                  │
│    - Technology constraints                                 │
│    - Phase boundaries                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. SPECIFICATION (specs/###-feature/spec.md)                │
│    - User stories with priorities                           │
│    - Functional requirements                                │
│    - Success criteria                                       │
│    - Created via: /sp.specify                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. PLAN (specs/###-feature/plan.md)                         │
│    - Technical approach                                     │
│    - Architecture decisions                                 │
│    - Data models and API contracts                          │
│    - Created via: /sp.plan                                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. TASKS (specs/###-feature/tasks.md)                       │
│    - Dependency-ordered checklist                           │
│    - Grouped by user story                                  │
│    - Parallelization markers                                │
│    - Created via: /sp.tasks                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. IMPLEMENTATION                                            │
│    - Agent executes tasks deterministically                 │
│    - TDD: Red → Green → Refactor                            │
│    - Quality gates enforced                                 │
│    - Executed via: /sp.implement or manual task execution   │
└─────────────────────────────────────────────────────────────┘
```

### Workflow Enforcement

**Pre-Implementation Validation**:
- Agent MUST verify spec exists and is approved
- Agent MUST verify plan exists and passes constitution check
- Agent MUST verify tasks exist and are derived from spec/plan
- Agent MUST refuse implementation if any prerequisite missing

**During Implementation**:
- Agent follows tasks in dependency order
- Agent writes tests first (Red phase)
- Agent implements to pass tests (Green phase)
- Agent refactors for quality (Refactor phase)
- Agent records decisions in PHRs (Prompt History Records)

**Post-Implementation Validation**:
- All tests must pass (unit, integration, contract)
- Coverage thresholds must be met (per Principle V)
- API contracts must validate against specs (100% compliance)
- Security scans must show zero HIGH/CRITICAL vulnerabilities
- Quality gate must approve before merge

### Refinement Process

**Allowed Refinement Paths**:
1. **Specification Refinement**: Update `spec.md` → regenerate plan → regenerate tasks → re-implement
2. **Plan Refinement**: Update `plan.md` → regenerate tasks → re-implement
3. **Task Refinement**: Update `tasks.md` → re-implement

**Prohibited Refinement Paths**:
- Direct code editing by humans (constitutional violation)
- Agent code changes without task authorization (constitutional violation)
- "Quick fixes" that bypass spec-plan-task workflow (constitutional violation)

**Rationale**: Refinement at higher abstraction levels (spec/plan) ensures consistency, traceability, and prevents implementation drift from requirements.

## Governance

### Constitutional Authority

This constitution is the **SUPREME GOVERNING DOCUMENT** for the Evolution of Todo project. All development practices, agent behaviors, and architectural decisions MUST comply with these principles.

**Precedence Hierarchy**:
1. Constitution (this document) - highest authority
2. Phase Specifications - constrained by constitution
3. Implementation Plans - constrained by specs and constitution
4. Tasks - derived from plans and specs
5. Code - implements tasks under constitutional constraints

**Amendment Process**:
1. Proposed amendments submitted as ADR (Architecture Decision Record)
2. Impact analysis on all phases and existing artifacts
3. Stakeholder review and approval required
4. Version increment (MAJOR for breaking changes, MINOR for additions, PATCH for clarifications)
5. Propagation to all dependent templates and documentation
6. Migration plan for existing implementations if needed

**Compliance Verification**:
- All pull requests MUST verify constitutional compliance
- Quality gates enforce constitutional principles (coverage, API contracts, security)
- Phase transition checkpoints validate phase boundary adherence
- Regular audits ensure specification-implementation alignment

**Violation Handling**:
- Constitutional violations MUST be rejected immediately
- Agents refuse non-compliant instructions
- Humans cannot override constitutional constraints
- Violations require spec updates and re-implementation, not workarounds

**Complexity Justification**:
- Any deviation from simplicity principles requires written justification
- Complexity must be documented in ADR with alternatives considered
- "Simpler alternative rejected because..." must be explicitly stated
- Complexity debt tracked and reviewed quarterly

### Guidance Documents

**Runtime Development Guidance**:
- Primary: This constitution (`SPECIFY/memory/constitution.md`)
- Agent Instructions: `CLAUDE.md` (agent-specific execution rules)
- Templates: `.specify/templates/*.md` (spec, plan, task, ADR, PHR formats)

**Principle Enforcement**:
- Templates embed constitution checks (see plan-template.md)
- Skills enforce agent behavior rules (see `.claude/skill/*/SKILL.md`)
- Quality gates validate architecture principles (see execute-quality-gate skill)

---

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30

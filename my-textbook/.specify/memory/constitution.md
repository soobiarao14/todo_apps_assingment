<!--
Sync Impact Report:
- Version change: [UNVERSIONED] → 1.0.0
- Rationale: Initial constitution for AI/Spec-Driven Book Creation project
- Modified principles: N/A (new constitution)
- Added sections: All core principles (5), Technical Standards, Quality & Workflow, Governance
- Removed sections: None
- Templates requiring updates:
  ✅ plan-template.md - Constitution Check section aligns with new principles
  ✅ spec-template.md - User Scenarios structure supports content standards
  ✅ tasks-template.md - Task organization aligns with modular development principle
- Follow-up TODOs: None - all placeholders resolved
-->

# AI/Spec-Driven Book Creation Constitution

## Core Principles

### I. Spec-Driven Writing

All content must originate from specifications following the constitution → plan → sections → expansions workflow.

**Rules**:
- No content may be written without being anchored to a spec phase
- Every chapter must map to a plan section
- Every subsection must map to a research item
- Changes to content structure require spec amendments first

**Rationale**: Ensures systematic development, traceability, and prevents scope creep or unplanned content divergence.

### II. Research-Concurrent Development

Every section must be written alongside research, not before or after.

**Rules**:
- Research and writing occur in parallel for each section
- No section proceeds to writing without concurrent research validation
- Primary sources must be consulted during writing, not referenced from memory
- All technical claims verified against official documentation before inclusion

**Rationale**: Prevents hallucinations, ensures technical accuracy, and maintains source authority throughout the writing process.

### III. Technical Accuracy (NON-NEGOTIABLE)

All definitions, patterns, workflows, and technical content must be accurate and verifiable.

**Rules**:
- MUST use only official, primary sources:
  - Docusaurus official documentation
  - Spec-Kit Plus documentation
  - Claude Code documentation
  - GitHub Pages documentation
  - MCP Server (Connect 7) documentation
- MUST cite sources for all technical claims
- MUST verify all commands, configurations, and code examples execute successfully
- Zero tolerance for hallucinated content or unverified claims

**Rationale**: Book credibility depends on technical correctness. Errors erode trust and harm readers' learning outcomes.

### IV. Reproducibility

All steps, examples, and workflows must be fully replicable by readers.

**Rules**:
- Include complete commands with expected outputs
- Document folder structures with exact paths
- Provide installation steps for all dependencies
- Include configuration files and code samples in full
- Test all reproduction paths in clean environments

**Rationale**: Readers must be able to follow along successfully. Non-reproducible examples frustrate learners and reduce book value.

### V. Modular Documentation Quality

Content must be clear, modular, reusable, and accessible to the target audience.

**Rules**:
- Target audience: beginner-to-intermediate developers
- Writing style: clear, instructional, free of jargon unless defined
- Paragraph limit: 4 sentences maximum per paragraph
- Sentence structure: short, direct, active voice
- Sections must be self-contained and independently understandable
- Use Docusaurus MDX best practices (callouts, code blocks, admonitions)

**Rationale**: Clear, modular writing improves comprehension, retention, and book usability. Modular sections enable reuse and reference.

## Technical Standards

### Content Formatting

- **Format**: Docusaurus MDX (Markdown with JSX components)
- **Structure**: Hierarchical chapters with nested sections
- **Code blocks**: Syntax-highlighted with language tags
- **Callouts**: Use Docusaurus admonitions (:::note, :::tip, :::warning, :::danger)
- **Diagrams**: Minimum 5 architecture diagrams (Mermaid or embedded images)
- **Examples**: Minimum 20 complete, executable code examples

### Source Citation

- **Style**: Documentation-style referencing
- **Links**: Inline hyperlinks to official sources
- **References**: End-of-chapter reference sections
- **Attribution**: Clear attribution for all external content

### Build Requirements

- All MDX files must build without errors in Docusaurus
- GitHub Pages deployment must succeed without warnings
- Navigation structure must be complete and functional
- Search functionality must index all content
- All internal links must resolve correctly

## Quality & Workflow

### Development Workflow

1. **Constitution phase**: Define project principles and standards (this document)
2. **Plan phase**: Create detailed chapter outlines and architecture
3. **Research phase**: Gather primary sources for each section
4. **Section generation**: Write content with concurrent research validation
5. **Review phase**: Verify technical accuracy, reproducibility, build success
6. **Build phase**: Generate Docusaurus site and deploy to GitHub Pages

### Quality Gates

**Pre-writing checklist**:
- [ ] Spec phase completed for content area
- [ ] Research sources identified and verified
- [ ] Target audience understanding documented
- [ ] Section objectives defined

**Post-writing checklist**:
- [ ] All technical claims verified against primary sources
- [ ] All commands tested and outputs documented
- [ ] All code examples execute successfully
- [ ] Paragraph and sentence length limits respected
- [ ] MDX syntax validated
- [ ] Sources cited properly

**Pre-deployment checklist**:
- [ ] Docusaurus build succeeds with no errors
- [ ] All internal links resolve
- [ ] Navigation complete
- [ ] Minimum content requirements met (10+ chapters, 5+ diagrams, 20+ examples)
- [ ] GitHub Pages deployment tested

### Complexity Justification

If any principle violation is necessary, it must be documented:

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [Principle name] | [Specific justification] | [Why alternative insufficient] |

## Governance

### Amendment Process

1. Constitution changes must be proposed with:
   - Clear rationale for change
   - Impact analysis on existing content
   - Migration plan if applicable
2. All amendments require version increment
3. Constitution version must be updated in this file
4. Dependent templates must be reviewed and updated
5. All team members must acknowledge changes

### Versioning Policy

- **MAJOR**: Backward-incompatible principle removals or redefinitions
- **MINOR**: New principles added or materially expanded guidance
- **PATCH**: Clarifications, wording fixes, non-semantic refinements

### Compliance

- All content development must verify compliance with constitution principles
- Constitution supersedes all other practices or guidelines
- Use `.specify/memory/constitution.md` (this file) as authoritative source during development
- Complexity violations require explicit justification in project documentation

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06

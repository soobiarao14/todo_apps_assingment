# Data Model: Physical AI & Humanoid Robotics Technical Book

**Feature**: 002-physical-ai-robotics-book
**Date Created**: 2025-12-06
**Purpose**: Define the structure and relationships of book content entities

---

## Content Hierarchy

```
Book
├── Module (4 total)
│   ├── Chapter (5 per module = 20 total)
│   │   ├── Section (3-5 per chapter)
│   │   │   ├── Content Block (text, code, diagrams)
│   │   │   ├── Code Example (inline or repository link)
│   │   │   └── Validation Checkpoint
│   │   ├── References Section
│   │   └── Exercises/Challenges
│   ├── Learning Outcomes
│   ├── Hardware Requirements
│   └── Module Validation Test
├── Code Examples Repository
│   └── Module Folder (organized by chapter)
└── Supplementary Materials
    ├── Architecture Diagrams
    ├── ADR Documents
    └── 16-Week Timeline
```

---

## Entity Definitions

### 1. Module

**Attributes**:
- `id`: string (e.g., "module-1", "module-2")
- `title`: string
- `priority`: P1, P2, P3, P4
- `user_story_id`: string (US1-US4)
- `week_range`: string (e.g., "Weeks 1-2")
- `learning_outcomes`: LearningOutcome[]
- `chapters`: Chapter[]
- `hardware_requirements`: HardwareRequirement[]
- `independent_test`: string (acceptance criteria)

**Relationships**:
- Contains 5 chapters
- Has multiple learning outcomes
- References hardware requirements
- Maps to user story in spec.md

**Example**:
```typescript
{
  id: "module-1",
  title: "Spec-Driven Workflow & Foundations",
  priority: "P1",
  user_story_id: "US1",
  week_range: "Weeks 1-2",
  learning_outcomes: [...],
  chapters: [...],
  hardware_requirements: [{...}],
  independent_test: "Reader can create Docusaurus project and write first spec"
}
```

---

### 2. Chapter

**Attributes**:
- `id`: string (e.g., "01-intro-spec-driven")
- `title`: string
- `module_id`: string
- `order`: number (1-5)
- `file_path`: string (MDX file path)
- `sections`: Section[]
- `code_examples`: CodeExample[]
- `diagrams`: Diagram[]
- `references`: Reference[]
- `validation_checkpoints`: ValidationCheckpoint[]
- `reading_time_minutes`: number

**Relationships**:
- Belongs to one module
- Contains 3-5 sections
- Links to code examples in repository
- References diagrams in static/diagrams/
- Cites primary sources

**Example**:
```typescript
{
  id: "01-intro-spec-driven",
  title: "Introduction to Spec-Driven Development",
  module_id: "module-1",
  order: 1,
  file_path: "docs/module-1-foundations/01-intro-spec-driven.md",
  sections: [...],
  code_examples: [...],
  diagrams: [{...}],
  references: [{...}],
  validation_checkpoints: [{...}],
  reading_time_minutes: 15
}
```

---

### 3. Section

**Attributes**:
- `id`: string
- `title`: string
- `chapter_id`: string
- `order`: number
- `content_blocks`: ContentBlock[]
- `paragraph_count`: number
- `flesch_kincaid_grade`: number (target: 10-12)

**Relationships**:
- Belongs to one chapter
- Contains multiple content blocks
- Must meet quality standards (4-sentence paragraph limit)

---

### 4. CodeExample

**Attributes**:
- `id`: string
- `title`: string
- `description`: string
- `language`: string ("python" | "bash" | "yaml" | "cpp")
- `repository_path`: string (in examples-repository)
- `inline_code`: string | null
- `chapter_references`: string[] (which chapters link to this)
- `setup_instructions`: string
- `expected_output`: string
- `tested_on`: string (e.g., "Ubuntu 22.04, ROS 2 Humble")

**Relationships**:
- Can be referenced by multiple chapters
- Stored in examples-repository/module-X/
- Licensed under MIT

**Example**:
```typescript
{
  id: "hello-ros2-publisher",
  title: "Hello World ROS 2 Publisher",
  description: "Basic rclpy publisher node demonstrating ROS 2 communication",
  language: "python",
  repository_path: "examples-repository/module-2/01-hello-ros2/publisher.py",
  inline_code: null,
  chapter_references: ["02-rclpy-packages"],
  setup_instructions: "Install ROS 2 Humble, source workspace",
  expected_output: "Publishing: 'Hello World: 0' every 1 second",
  tested_on: "Ubuntu 22.04, ROS 2 Humble"
}
```

---

### 5. Diagram

**Attributes**:
- `id`: string
- `title`: string
- `type`: "architecture" | "workflow" | "data-flow" | "component" | "timeline"
- `file_path`: string (SVG in static/diagrams/)
- `source_file`: string | null (Mermaid, Blender, USD source)
- `alt_text`: string (accessibility)
- `chapter_references`: string[]

**Relationships**:
- Referenced by one or more chapters
- Stored in physical-ai-robotics-book/static/diagrams/

**Example**:
```typescript
{
  id: "ros2-node-graph",
  title: "ROS 2 Node Communication Graph",
  type: "architecture",
  file_path: "static/diagrams/ros2-node-graph.svg",
  source_file: "static/diagrams/sources/ros2-node-graph.mermaid",
  alt_text: "Diagram showing ROS 2 nodes communicating via DDS topics",
  chapter_references: ["01-ros2-architecture", "02-rclpy-packages"]
}
```

---

### 6. LearningOutcome

**Attributes**:
- `id`: string
- `module_id`: string
- `description`: string
- `validation_method`: string
- `acceptance_criteria`: string
- `completion_indicator`: string

**Example**:
```typescript
{
  id: "LO-M1-01",
  module_id: "module-1",
  description: "Explain the five core principles of spec-driven writing",
  validation_method: "Can articulate each principle with examples",
  acceptance_criteria: "Reader creates spec.md following constitution",
  completion_indicator: "Successfully writes first spec document"
}
```

---

### 7. HardwareRequirement

**Attributes**:
- `module_id`: string
- `component`: string
- `minimum_spec`: string
- `recommended_spec`: string
- `purpose`: string
- `cloud_alternative`: string | null

**Example**:
```typescript
{
  module_id: "module-3",
  component: "GPU",
  minimum_spec: "RTX 3060 (12GB VRAM)",
  recommended_spec: "RTX 4070 Ti (16GB VRAM)",
  purpose: "Isaac Sim rendering and synthetic data generation",
  cloud_alternative: "NVIDIA Omniverse Cloud"
}
```

---

### 8. ValidationCheckpoint

**Attributes**:
- `id`: string
- `chapter_id`: string
- `type`: "concept_check" | "hands_on" | "troubleshooting"
- `title`: string
- `setup`: string
- `steps`: string[]
- `expected_results`: string
- `troubleshooting_guide`: string

**Example**:
```typescript
{
  id: "VC-M2-01",
  chapter_id: "02-rclpy-packages",
  type: "hands_on",
  title: "Verify ROS 2 Publisher Node",
  setup: "Create publisher.py from code example",
  steps: [
    "Source ROS 2 workspace: source /opt/ros/humble/setup.bash",
    "Run publisher: python3 publisher.py",
    "In new terminal, check topics: ros2 topic list"
  ],
  expected_results: "Topic /hello_world appears, messages publishing at 1Hz",
  troubleshooting_guide: "If topic missing, check ROS_DOMAIN_ID matches"
}
```

---

### 9. Reference

**Attributes**:
- `id`: string
- `type`: "peer_reviewed" | "official_docs" | "technical_blog" | "book"
- `title`: string
- `authors`: string[]
- `year`: number
- `url`: string
- `citation_apa`: string
- `chapters_cited_in`: string[]

**Example**:
```typescript
{
  id: "REF-ROS2-DESIGN",
  type: "official_docs",
  title: "ROS 2 Design Documentation",
  authors: ["Open Robotics"],
  year: 2023,
  url: "https://design.ros2.org/",
  citation_apa: "Open Robotics. (2023). ROS 2 Design. https://design.ros2.org/",
  chapters_cited_in: ["01-ros2-architecture", "04-launch-params"]
}
```

---

## Module-to-Chapter Mapping

### Module 1: Spec-Driven Workflow & Foundations (Weeks 1-2)
1. Introduction to Spec-Driven Development
2. Spec-Kit Plus Architecture
3. Claude Code Workflows
4. Docusaurus Basics & MDX
5. Technical Writing Standards

### Module 2: ROS 2 Fundamentals (Weeks 3-7)
1. ROS 2 Architecture & DDS
2. rclpy Packages & Nodes
3. URDF/SDF Robot Modeling
4. Launch Files & Parameters
5. Gazebo Integration

### Module 3: Digital Twins & NVIDIA Isaac (Weeks 8-12)
1. Isaac Sim Environment Setup
2. USD Workflow & Scene Creation
3. Synthetic Data Generation
4. Visual SLAM (VSLAM) Implementation
5. Jetson Orin Deployment

### Module 4: Vision-Language-Action Pipeline (Weeks 13-15)
1. Whisper ASR Setup & Configuration
2. LLM Integration for Task Planning
3. ROS Action Servers
4. End-to-End VLA Pipeline
5. Capstone Project Integration

---

## Quality Metrics Per Entity

### Chapter Quality Standards:
- Paragraphs: Max 4 sentences
- Flesch-Kincaid grade: 10-12
- Citations: 40%+ peer-reviewed or official docs
- Plagiarism: 0% (excluding proper citations)
- Code examples: All executable on Ubuntu 22.04
- Diagrams: Minimum 1 per chapter

### Module Completion Criteria:
- All 5 chapters published
- All code examples tested and working
- All diagrams created and referenced
- All validation checkpoints verified
- Learning outcomes documented
- Independent test passable by reader

---

## Storage & Versioning

- **Book Content**: Git repository (Docusaurus project)
- **Code Examples**: Separate Git repository (MIT license)
- **Diagrams**: SVG in static/diagrams/ with source files
- **Version Control**: Annual updates for compatibility
- **Deployment**: GitHub Pages (static site)

---

## Notes

This data model ensures:
1. Content is modular and independently testable
2. Clear separation between content (CC BY 4.0) and code (MIT)
3. Reproducibility through validated code examples
4. Quality enforcement at entity level
5. Traceability from spec → plan → tasks → content

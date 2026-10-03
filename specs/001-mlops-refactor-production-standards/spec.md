# Feature Specification: MLOps Refactor to Production Standards

**Feature Branch**: `001-mlops-refactor-production-standards`  
**Created**: 2026-10-03  
**Status**: Draft  
**Input**: User description: "Рефакторинг существующего проекта под production-стандарты пары MLOps. Логику модели не менять. ..."

## Execution Flow (main)
1. Parse user description from Input
2. Extract key concepts from description
3. For each unclear aspect, mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
5. Generate Functional Requirements
6. Identify Key Entities (if data involved)
7. Run Review Checklist
8. Return: SUCCESS (spec ready for planning)

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a ML practitioner working with the maternal risk classification project, I need the project restructured to follow production-grade MLOps practices so that I can reliably train, test, and use the model in a maintainable way without changing the underlying model logic.

### Acceptance Scenarios
1. **Given** existing notebooks contain EDA, model comparison, and final pipeline with a specific SVM configuration, **When** the code is refactored, **Then** the same model logic is preserved (no change to core model behavior).
2. **Given** the refactored codebase, **When** training via the CLI, **Then** training completes using configuration from config and produces expected artifacts consistent with historical behavior.
3. **Given** the refactored codebase, **When** running predictions via CLI, **Then** predictions return exactly 3 classes.
4. **Given** the refactored codebase, **When** tests are run, **Then** tests validate data cleaning behavior and that predict returns 3 classes.
5. **Given** the refactored codebase, **When** quality checks run via pre-commit, **Then** black (88), isort, and flake8 pass.
6. **Given** project artifacts, **When** onboarding new users, **Then** they can set up environment with Poetry, install hooks, train, and run tests following README.

### Edge Cases
- Data cleaning must handle typical input format from existing data files without breaking existing behavior.
- CLI tools must be runnable with standard arguments and return clear outputs for valid inputs.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The project MUST preserve existing model logic and final SVM configuration exactly as in README and notebooks; no changes to SVM parameters or behavior.
- **FR-002**: The system MUST extract existing logic into `src/maternal_risk` modules: config, data, features, train, predict, evaluate.
- **FR-003**: The system MUST provide CLI scripts: `scripts/train.py` and `scripts/predict.py`.
- **FR-004**: The system MUST use the same `random_state` value as used in the notebook.
- **FR-005**: The project MUST use Poetry for dependency management with committed `poetry.lock` and `pyproject.toml`. `.venv` must remain ignored.
- **FR-006**: The project MUST include `.env.example` with appropriate placeholders.
- **FR-007**: The project MUST configure pre-commit with black (line length 88), isort, and flake8.
- **FR-008**: The project MUST include pytest tests that validate data cleaning and that predict returns exactly 3 classes.
- **FR-009**: The project MUST include `MODEL_CARD.md` following Google Model Cards format with appropriate content based on project scope.
- **FR-010**: The project MUST include lifecycle documentation: `docs/model_lifecycle.bpmn` (BPMN 2.0) and `docs/MODEL_LIFECYCLE.md` with Mermaid diagram; steps must reference actual files in this repository.
- **FR-011**: The README MUST document: `poetry install`, `pre-commit install`, training, and running tests.
- **FR-012**: The refactoring MUST NOT remove or delete notebooks; existing notebooks must be preserved.

### Non-Functional Requirements
- **NFR-001**: Changes MUST be structured and documented to support maintainability and reproducibility.
- **NFR-002**: Quality gates (pre-commit checks) MUST pass on all committed code.

### Key Entities
- **Data**: Input datasets in `data/` as currently structured, processed by data module.
- **Model artifacts**: Trained model and related outputs produced by train/evaluate modules.
- **Configuration**: Settings (including random_state) managed via config module.
- **Prediction outputs**: Classification results with exactly 3 classes.

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Success criteria are technology-agnostic (no implementation details)
- [x] All acceptance scenarios are defined
- [x] Edge cases are identified
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Execution Status
*Updated by main() during processing*

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [x] Review checklist passed

---

## Assumptions
- The existing notebooks define the canonical model logic, configuration, and random_state; these will be extracted faithfully.
- Data files in `data/` remain in place and their formats are preserved.
- Google Model Cards format is used as specified (no need to guess alternative format).
- Lifecycle diagrams must reference actual repository file paths for each step.
- Training/inference CLIs will wrap the extracted logic without modifying model behavior.

## Out of Scope
- Changing the SVM model or its parameters
- Adding a new dataset
- Retraining to improve metrics
- Docker
- GitLab CI

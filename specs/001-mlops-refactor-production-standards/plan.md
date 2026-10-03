# Implementation Plan: MLOps Refactor to Production Standards

**Branch**: `001-mlops-refactor-production-standards` | **Date**: 2026-10-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-mlops-refactor-production-standards/spec.md`

## Execution Flow (/plan command scope)
1. Load feature spec from Input path
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
3. Fill Constitution Check section based on constitution document
4. Evaluate Constitution Check section below
5. Execute Phase 0 → research.md
6. Execute Phase 1 → data-model.md, contracts/, quickstart.md
7. Re-evaluate Constitution Check section
8. Plan Phase 2 → Describe task generation approach (only)
9. STOP - Ready for /tasks command

## Summary
Refactor the existing maternal risk classification project to production-grade MLOps structure without changing model logic. Extract code into `src/maternal_risk` modules (config, data, features, train, predict, evaluate), add CLI scripts, Poetry setup with lock file, pre-commit (black 88/isort/flake8), pytest tests, MODEL_CARD.md (Google format), lifecycle docs (BPMN + Mermaid), and update README.

## Technical Context
**Language/Version**: Python 3.10+  
**Primary Dependencies**: Dependencies from existing notebooks (preserve existing libraries; no new ML libraries)  
**Testing**: pytest  
**Linting/Formatting**: black (88), flake8, isort, pre-commit  
**Storage**: Local filesystem (data/, artifacts)  
**Project Type**: Single project (ML library/package with CLI)  
**Target Platform**: Local development  
**Constraints**: Preserve all existing model logic/SVM params/random_state as in README/notebooks; no Docker, GitLab CI, dataset change, retraining for metrics. Keep notebooks intact.  
**Scale/Scope**: Educational ML project, small dataset

## Constitution Check
*GATE: Must pass before Phase 0*

**I. Educational Scope**: Refactoring preserves logic/metrics as required. ✓  
**II. Locked Model Spec**: No changes to SVM (C=100, gamma=0.03, class_weight=balanced). ✓  
**III. Poetry & Git**: Will add Poetry with pyproject.toml and poetry.lock; .venv in .gitignore. ✓  
**IV. Code Quality**: black (88), isort, flake8, pre-commit configured; code in src/, notebooks preserved. ✓  
**V. Transparency & Safety**: MODEL_CARD.md (Google) with non-clinical disclaimer. ✓  
**Additional Constraints**: No Docker/FastAPI/CI added. ✓  
**Lifecycle Docs**: BPMN 2.0 and Mermaid with file references. ✓

**Initial Constitution Check**: PASS

## Project Structure

### Documentation (this feature)
```
specs/001-mlops-refactor-production-standards/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
src/
└── maternal_risk/
    ├── __init__.py
    ├── config.py
    ├── data.py
    ├── features.py
    ├── train.py
    ├── predict.py
    └── evaluate.py

scripts/
├── train.py
└── predict.py

tests/
├── __init__.py
├── test_data.py
└── test_predict.py

docs/
├── model_lifecycle.bpmn
└── MODEL_LIFECYCLE.md

MODEL_CARD.md
.env.example
pyproject.toml
poetry.lock
.pre-commit-config.yaml
```

**Structure Decision**: Single project with `src/maternal_risk` package and CLI scripts in `scripts/`. Tests in `tests/`. Docs in `docs/`. Aligns with constitution (code in src/, notebooks preserved).

## Phase 0: Outline & Research
No NEEDS CLARIFICATION in spec. Research focuses on best practices for extracting logic while preserving behavior, Google Model Cards format, BPMN/Mermaid documentation patterns.

### Research Tasks
1. **Extracting existing notebook logic**: Review notebooks to identify exact SVM params, random_state, preprocessing, feature engineering, train/test split approach. Document mapping to modules.
2. **Poetry setup**: Configure pyproject.toml with dependencies matching notebooks (no new ML libs). Ensure Python 3.10+ constraint.
3. **Pre-commit config**: Set black 88, isort (compatible with black), flake8.
4. **Google Model Cards**: Template/sections per Google Model Cards specification.
5. **BPMN + Mermaid lifecycle**: Create BPMN 2.0 file and corresponding Mermaid with steps linked to repo files (data/, notebooks, src/, scripts/, tests/).

**Output**: [research.md](./research.md)

## Phase 1: Design & Contracts

### Data Model
Entities identified: Dataset, Features, Model, Predictions, Configuration. See [data-model.md](./data-model.md).

### Contracts
No external API endpoints (CLI tools). Define CLI contracts (arguments, inputs/outputs) in contracts/ directory.

- `contracts/train.md`: CLI contract for `scripts/train.py`
- `contracts/predict.md`: CLI contract for `scripts/predict.py`

### Quickstart
Validation scenarios for setup, training, prediction, tests, pre-commit. See [quickstart.md](./quickstart.md).

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load plan.md, research.md, data-model.md, contracts/, quickstart.md
- Generate tasks by phases: Setup (Poetry, .gitignore, .env.example), Structure (src modules, scripts), Config (pre-commit), Tests, Docs (Model Card, lifecycle), README update
- Each task: specific, testable, references files
- Order: dependencies first (structure before tests that import)

**Task Categories**:
1. Project setup (pyproject.toml, poetry.lock, .gitignore, .env.example)
2. Source modules extraction
3. CLI scripts
4. Pre-commit configuration
5. Tests
6. Documentation (MODEL_CARD.md, docs/*.bpmn, docs/*.md)
7. README updates

**Estimated Output**: ~20-30 numbered tasks, grouped by category

## Complexity Tracking
*No constitutional violations requiring justification*

## Progress Tracking
**Phase Status**:
- [x] Phase 0: Research complete (/plan)
- [x] Phase 1: Design complete (/plan)
- [x] Phase 2: Task planning complete (/plan - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [x] Complexity deviations documented

---
*Based on Constitution v1.0.0 - See `/specify/memory/constitution.md`*

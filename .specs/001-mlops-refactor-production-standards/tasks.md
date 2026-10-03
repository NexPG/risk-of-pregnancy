# Tasks: MLOps Refactor to Production Standards

**Input**: Design documents from `/specs/001-mlops-refactor-production-standards/`
- plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Prerequisites**: plan.md, spec.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/`, `tests/` at repository root
- Paths shown below assume single project as per plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan: src/maternal_risk/ package with __init__.py, config.py, data.py, features.py, train.py, predict.py, evaluate.py
- [ ] T002 [P] Create scripts/ directory with train.py and predict.py
- [ ] T003 [P] Create tests/ directory with __init__.py, test_data.py, test_predict.py
- [ ] T004 [P] Create docs/ directory
- [ ] T005 [P] Initialize Poetry project: create pyproject.toml with Python 3.10+, dependencies matching notebooks (no new ML libs), and dev deps (pytest, black, flake8, isort, pre-commit)
- [ ] T006 Generate poetry.lock file
- [ ] T007 [P] Update .gitignore to include .venv and common entries
- [ ] T008 [P] Create .env.example

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before user story implementation

- [ ] T009 [P] Configure pre-commit: create .pre-commit-config.yaml with black (line length 88), isort (profile black), flake8
- [ ] T010 [P] Create __init__.py files for src/maternal_risk and tests
- [ ] T011 [P] Extract canonical values from notebooks/README (SVM params C=100, gamma=0.03, class_weight=balanced and random_state) and document mapping

**Checkpoint**: Foundation ready

---

## Phase 3: User Story 1 - MLOps Refactor to Production Standards (Priority: P1) — MVP

**Goal**: Refactor existing logic into modular structure with CLIs, tests, docs, and quality tooling while preserving model logic

**Independent Test**: Can train and predict via CLIs, all tests pass, pre-commit passes, all required files present

### Implementation for User Story 1

- [ ] T012 [P] [US1] Implement src/maternal_risk/config.py with configuration management (paths, model params locked to C=100,gamma=0.03,class_weight='balanced', random_state from notebook)
- [ ] T013 [P] [US1] Implement src/maternal_risk/data.py for data loading/cleaning (preserve existing behavior)
- [ ] T014 [P] [US1] Implement src/maternal_risk/features.py for feature engineering/preprocessing (match notebook)
- [ ] T015 [P] [US1] Implement src/maternal_risk/train.py for training logic (preserve exact SVM params and random_state)
- [ ] T016 [P] [US1] Implement src/maternal_risk/predict.py for prediction (must return exactly 3 classes)
- [ ] T017 [P] [US1] Implement src/maternal_risk/evaluate.py for evaluation logic
- [ ] T018 [US1] Implement scripts/train.py CLI (wraps src.maternal_risk.train; accepts args as per train contract)
- [ ] T019 [US1] Implement scripts/predict.py CLI (wraps src.maternal_risk.predict; accepts args as per predict contract; returns exactly 3 classes)
- [ ] T020 [P] [US1] Write tests/test_data.py: test data cleaning behavior
- [ ] T021 [P] [US1] Write tests/test_predict.py: test that predict returns exactly 3 classes
- [ ] T022 [P] [US1] Create MODEL_CARD.md following Google Model Cards format with non-clinical disclaimer
- [ ] T023 [P] [US1] Create docs/model_lifecycle.bpmn (BPMN 2.0) with steps referencing repo files
- [ ] T024 [P] [US1] Create docs/MODEL_LIFECYCLE.md with Mermaid diagram referencing repo files
- [ ] T025 [US1] Update README.md with poetry install, pre-commit install, training, and running tests

**Checkpoint**: All user story requirements met; independently testable

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and validation

- [ ] T026 [P] Run pre-commit on all files and fix any issues
- [ ] T027 [P] Run all tests (pytest) and verify they pass
- [ ] T028 [P] Validate quickstart.md steps work end-to-end
- [ ] T029 Verify no notebooks deleted; notebooks preserved as-is
- [ ] T030 Verify no Docker, FastAPI, or CI added

---

## Dependencies & Execution Order

### Phase Dependencies
- Phase 1 (Setup): No dependencies - can start immediately
- Phase 2 (Foundational): Depends on Phase 1 - BLOCKS user story
- Phase 3 (US1): Depends on Phase 2 completion
- Phase 4 (Polish): Depends on Phase 3 completion

### Within Each Phase
- Setup tasks T005/T006 are related (Poetry init then lock); others [P]
- Foundational tasks independent where marked [P]
- US1: T012-T017 [P] (modules) can run in parallel; T018 depends on T015/T017; T019 depends on T016; T020-T024 [P]; T025 depends on others
- Polish: mostly independent parallel tasks

### Parallel Opportunities
- T002-T005,T007-T008 parallel in Setup
- T009-T011 parallel in Foundational
- T012-T017, T020-T024 parallel in US1
- T026-T028 parallel in Polish

## Implementation Strategy

### MVP First
1. Complete Phase 1 + Phase 2
2. Complete Phase 3 (US1)
3. Complete Phase 4 validation
4. STOP and verify all requirements met

### Independent Test Criteria (US1)
- `poetry run pytest` passes (includes data cleaning test and predict returns 3 classes)
- `pre-commit run --all-files` passes
- `poetry run python scripts/train.py` runs successfully
- `poetry run python scripts/predict.py --input <data>` returns predictions with exactly 3 classes
- All required files exist as specified; notebooks unchanged; no forbidden tech added

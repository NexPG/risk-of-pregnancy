# Quickstart: MLOps Refactor Validation

**Purpose**: Validate the refactored project meets all requirements.

## Prerequisites
- Python 3.10+
- Poetry installed
- Git

## Setup
```bash
poetry install
pre-commit install
```

## Validation Steps

### 1. Code Quality
```bash
pre-commit run --all-files
```
Expected: black (88), isort, flake8 all pass (FR-007, NFR-002).

### 2. Tests
```bash
poetry run pytest
```
Expected: Tests pass including data cleaning validation and predict returns 3 classes (FR-008).

### 3. Training (CLI)
```bash
poetry run python scripts/train.py
```
Expected: Trains successfully using extracted logic with correct random_state and locked params (FR-001, FR-003, FR-004).

### 4. Prediction (CLI)
```bash
poetry run python scripts/predict.py --input <data_file>
```
Expected: Returns predictions with exactly 3 classes (FR-003).

### 5. Verify Structure
- [ ] `src/maternal_risk/` has config, data, features, train, predict, evaluate modules (FR-002)
- [ ] `scripts/train.py` and `scripts/predict.py` exist (FR-003)
- [ ] `pyproject.toml`, `poetry.lock` present; `.venv` not committed (FR-005)
- [ ] `.env.example` present (FR-006)
- [ ] `.pre-commit-config.yaml` present with black 88, isort, flake8 (FR-007)
- [ ] `MODEL_CARD.md` exists (Google format, non-clinical disclaimer) (FR-009)
- [ ] `docs/model_lifecycle.bpmn` and `docs/MODEL_LIFECYCLE.md` exist with file references (FR-010)
- [ ] README updated with poetry install, pre-commit install, training, tests (FR-011)
- [ ] Notebooks preserved (FR-012)

## Success Criteria
- All validation steps pass
- Model logic unchanged (locked SVM params match README/notebooks)
- random_state matches notebook value
- No Docker, FastAPI, CI added
- Code in src/, quality checks pass

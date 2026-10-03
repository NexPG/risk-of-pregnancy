# Phase 0: Research

**Feature**: MLOps Refactor to Production Standards  
**Date**: 2026-10-03

## Overview
This document consolidates research findings to resolve all unknowns for the refactoring plan.

## Research Findings

### 1. Extracting Existing Notebook Logic
**Decision**: Extract logic faithfully by mapping notebook cells to modules while preserving exact SVM parameters and random_state.  
**Rationale**: Must not change model logic (FR-001, FR-004). Need to identify canonical values from README and notebooks.  
**Key points to capture**:
- Final SVM: C=100, gamma=0.03, class_weight='balanced' (per constitution)
- random_state: extract exact value from notebook
- Preprocessing steps, feature selection, train/test split as implemented
- Data loading paths relative to repo

**Alternatives considered**: Reimplementing cleanly vs line-by-line extraction - chose faithful extraction to guarantee no behavioral change.

### 2. Poetry Setup
**Decision**: Use Poetry with Python 3.10+. Configure dependencies to match those used in notebooks (no new ML libs). Commit poetry.lock.  
**Rationale**: Constitution III requires Poetry; FR-005 requires committed lock file.  
**Notes**: Include dev dependencies: pytest, black, flake8, isort, pre-commit. .venv must remain in .gitignore.

### 3. Pre-commit Configuration
**Decision**: Configure `.pre-commit-config.yaml` with black (line length 88), isort (profile black), flake8.  
**Rationale**: FR-007 and Constitution IV mandate these tools.  
**References**: Common black+isort+flake8 pre-commit setup.

### 4. Google Model Cards
**Decision**: Create `MODEL_CARD.md` following Google Model Cards format with sections: Model details, Intended use, Factors, Metrics, Evaluation data, Training data, Ethical considerations, Caveats & recommendations. Include explicit non-clinical disclaimer per Constitution V.  
**Rationale**: FR-009 requires Google Model Cards format; Constitution V requires disclaimer.

### 5. BPMN 2.0 and Mermaid Lifecycle
**Decision**: Create `docs/model_lifecycle.bpmn` (BPMN 2.0 XML) and `docs/MODEL_LIFECYCLE.md` with Mermaid flowchart. Map steps to actual repo files (data/, notebooks/*.ipynb, src/maternal_risk/*, scripts/*, tests/*, MODEL_CARD.md, README.md).  
**Rationale**: FR-010 requires both formats with file references.  
**Approach**: Lifecycle steps: Data ingestion (data/), EDA/analysis (notebooks), Feature prep (src/features), Training (src/train, scripts/train), Evaluation (src/evaluate), Prediction (src/predict, scripts/predict), Testing (tests/), Documentation (MODEL_CARD, lifecycle docs), Quality checks (pre-commit).

All NEEDS CLARIFICATION resolved - no open questions.

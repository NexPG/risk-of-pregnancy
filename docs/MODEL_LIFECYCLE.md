# Model Lifecycle

This document describes the model lifecycle with Mermaid diagram and references to actual repository files.

## Lifecycle Steps

1. **Data Ingestion** - Read raw data from `data/Maternal Health Risk Data Set.xlsx`
2. **EDA & Analysis** - Explore data in `notebooks/maternal_risk_final.ipynb` and `code/EDA.ipynb`, `code/trainer.ipynb`
3. **Data Cleaning** - Remove duplicates and filter (HeartRate >= 40) via `src/maternal_risk/data.py`
4. **Feature Preparation** - Prepare features/target in `src/maternal_risk/features.py`
5. **Training** - Train SVM (C=100, gamma=0.03, class_weight=balanced, random_state=42) in `src/maternal_risk/train.py`, exposed via `scripts/train.py`
6. **Evaluation** - Compute metrics in `src/maternal_risk/evaluate.py`
7. **Prediction** - Inference via `src/maternal_risk/predict.py` and `scripts/predict.py` (returns exactly 3 classes)
8. **Testing** - Validate with `tests/test_data.py` and `tests/test_predict.py`
9. **Documentation** - Maintain `MODEL_CARD.md` (Google format), this lifecycle doc, and BPMN in `docs/model_lifecycle.bpmn`
10. **Quality Assurance** - Run pre-commit hooks (black 88, isort, flake8)

## Mermaid Diagram

```mermaid
graph LR
    A[Data Ingestion<br/>data/Maternal Health Risk Data Set.xlsx] --> B[EDA/Analysis<br/>notebooks/maternal_risk_final.ipynb<br/>code/EDA.ipynb<br/>code/trainer.ipynb]
    B --> C[Data Cleaning<br/>src/maternal_risk/data.py]
    C --> D[Feature Prep<br/>src/maternal_risk/features.py]
    D --> E[Training<br/>src/maternal_risk/train.py<br/>scripts/train.py]
    E --> F[Evaluation<br/>src/maternal_risk/evaluate.py]
    E --> G[Prediction<br/>src/maternal_risk/predict.py<br/>scripts/predict.py]
    G --> H[Testing<br/>tests/test_data.py<br/>tests/test_predict.py]
    F --> H
    H --> I[Documentation<br/>MODEL_CARD.md<br/>docs/MODEL_LIFECYCLE.md<br/>docs/model_lifecycle.bpmn]
    I --> J[QA/Pre-commit<br/>black 88, isort, flake8]
```

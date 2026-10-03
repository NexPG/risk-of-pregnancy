# Data Model

**Feature**: MLOps Refactor to Production Standards  
**Date**: 2026-10-03

## Entities

### Configuration
Represents project configuration (paths, model params, random_state).  
**Fields**:
- `random_state`: int (from notebook, must match exactly)
- `model_params`: dict (SVM params: C=100, gamma=0.03, class_weight='balanced')
- `data_path`: str (path to dataset in data/)
- `artifacts_dir`: str (model output dir)
- `target_column`: str (risk class)

**Validation**: Values must match canonical values from notebooks/README.

### Dataset
Raw/processed dataset loaded from data/.  
**Fields**:
- `features`: DataFrame/array structure as in existing code
- `target`: labels (3 classes: low/mid/high)
- `path`: source file path

**Validation**: Shape/types consistent with existing behavior.

### Features
Feature representation after preprocessing.  
**Fields**:
- `X_train`, `X_test`: feature matrices
- `y_train`, `y_test`: labels
- `preprocessing_steps`: list of applied transforms (as implemented)

### Model
Trained model artifact.  
**Fields**:
- `model`: sklearn SVC/RBF model with locked params
- `metadata`: training info (random_state, paths, etc.)
- `version`: artifact identifier

**Constraints**: Params fixed - C=100, gamma=0.03, class_weight='balanced'.

### Predictions
Model predictions on new data.  
**Fields**:
- `predictions`: array of class labels (exactly 3 classes)
- `probabilities` (if available): class probabilities
- `input_shape`: shape of input data

**Validation**: Output contains exactly 3 classes (FR-008).

## Relationships
- Configuration -> Dataset loading parameters
- Dataset + Features -> Training inputs
- Features + Model -> Predictions
- Train produces Model; Predict consumes Model + input data

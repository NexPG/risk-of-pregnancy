# CLI Contract: train.py

**Command**: `scripts/train.py`  
**Purpose**: Train the maternal risk model using extracted logic (no behavior change).

## Arguments
- `--config` (optional): Path to config file
- `--data` (optional): Path to dataset in data/
- `--output` (optional): Directory for model artifacts
- `--random-state` (optional): Override random_state if needed (must default to notebook value)

## Inputs
- Dataset file from data/ (existing format)
- Configuration values (model params locked: C=100, gamma=0.03, class_weight=balanced)

## Outputs
- Trained model artifact saved to artifacts/output dir
- Training logs/summary (as per existing behavior)
- Exit code 0 on success

## Behavior
- Uses same preprocessing, features, split as in notebook
- Uses identical random_state
- Does not modify SVM parameters
- Preserves all existing logic

## Validation
- Runs without errors on existing data
- Produces artifacts consistent with historical pipeline

# CLI Contract: predict.py

**Command**: `scripts/predict.py`  
**Purpose**: Make predictions using trained model; must return exactly 3 classes.

## Arguments
- `--model` (optional): Path to trained model artifact
- `--input` (required): Path to input data file
- `--output` (optional): Path to save predictions
- `--config` (optional): Path to config

## Inputs
- Trained model with locked params
- Input data in format compatible with existing pipeline

## Outputs
- Predictions (exactly 3 classes per sample)
- Exit code 0 on success

## Behavior
- Applies same preprocessing as training
- Returns predictions with exactly 3 possible class values
- Preserves existing prediction logic

## Validation
- Predict returns exactly 3 classes (tested by pytest)
- Compatible with existing data formats

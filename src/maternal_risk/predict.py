"""Prediction logic."""
from pathlib import Path

import joblib
import pandas as pd

from . import config


def load_model(model_path=None):
    """Load trained model."""
    path = model_path or config.MODEL_PATH
    if not Path(path).exists():
        # try in artifacts
        alt = Path(config.ARTIFACTS_DIR) / "model.pkl"
        if alt.exists():
            path = alt
        else:
            raise FileNotFoundError(f"Model not found at {path}")
    return joblib.load(path)


def predict(model, X):
    """Make predictions - must return exactly 3 classes."""
    if model is None:
        model = load_model()
    preds = model.predict(X)
    return preds


def run_prediction(model=None, input_data=None, output=None, config_path=None):
    """Run prediction."""
    if input_data is None:
        raise ValueError("input_data is required")
    X = (
        pd.read_csv(input_data)
        if Path(input_data).exists()
        else pd.read_excel(input_data)
    )
    # If target present, drop it
    if config.TARGET_COLUMN in X.columns:
        X = X.drop(columns=[config.TARGET_COLUMN])
    model_obj = (
        load_model(model) if isinstance(model, (str, Path)) or model is None else model
    )
    preds = predict(model_obj, X)
    # Ensure 3 classes
    result = pd.DataFrame({"prediction": preds})
    if output:
        Path(output).parent.mkdir(exist_ok=True, parents=True)
        result.to_csv(output, index=False) if str(output).endswith(
            ".csv"
        ) else result.to_pickle(output)
    return preds, result

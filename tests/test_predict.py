"""Tests for prediction."""

from maternal_risk import config, predict


def test_predict_returns_three_classes():
    """Test that predict returns exactly 3 classes."""
    # Create a dummy model
    import pandas as pd
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC

    # Simple model
    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", SVC(kernel="linear", random_state=42)),
        ]
    )
    X_train = pd.DataFrame(
        {
            "Age": [20, 30, 40],
            "SystolicBP": [120, 130, 140],
            "DiastolicBP": [80, 85, 90],
            "BS": [5, 7, 12],
            "BodyTemp": [98, 98, 99],
            "HeartRate": [70, 80, 90],
        }
    )
    y_train = ["low risk", "mid risk", "high risk"]
    model.fit(X_train, y_train)
    X_test = pd.DataFrame(
        {
            "Age": [25],
            "SystolicBP": [125],
            "DiastolicBP": [82],
            "BS": [6],
            "BodyTemp": [98],
            "HeartRate": [75],
        }
    )
    preds = predict.predict(model, X_test)
    # Should have predictions with values in the 3 classes
    assert len(preds) == 1
    assert preds[0] in config.LABELS

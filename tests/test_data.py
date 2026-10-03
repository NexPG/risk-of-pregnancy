"""Tests for data cleaning."""
from maternal_risk import data


def test_data_cleaning_removes_duplicates_and_bad_heart_rate():
    """Test that data cleaning works correctly."""
    import pandas as pd

    # Create test data with duplicates and bad HR
    df = pd.DataFrame(
        {
            "Age": [25, 25, 30],
            "SystolicBP": [130, 130, 140],
            "DiastolicBP": [80, 80, 85],
            "BS": [15.0, 15.0, 7.0],
            "BodyTemp": [98.0, 98.0, 98.0],
            "HeartRate": [86, 86, 7],
            "RiskLevel": ["high risk", "high risk", "high risk"],
        }
    )
    cleaned = data.clean_data(df)
    # Should remove duplicate and remove bad HR
    assert len(cleaned) == 1

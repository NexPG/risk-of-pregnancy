"""Data loading and preprocessing."""
from pathlib import Path

import pandas as pd

from . import config


def load_data(data_path=None):
    """Load dataset from path."""
    path = data_path or config.DATA_PATH
    # Try common excel/csv files
    data_file = Path(path)
    if data_file.is_file():
        if data_file.suffix in [".csv"]:
            return pd.read_csv(data_file)
        elif data_file.suffix in [".xlsx", ".xls"]:
            return pd.read_excel(data_file)
    # Look for known files
    for fname in [
        "Maternal Health Risk Data Set.xlsx",
        "Maternal Health Risk Data Set.csv",
    ]:
        fpath = Path(path) / fname if Path(path).is_dir() else Path(fname)
        if fpath.exists():
            if fpath.suffix == ".csv":
                return pd.read_csv(fpath)
            return pd.read_excel(fpath)
    # Default: try train.csv if exists
    if Path(config.TRAIN_DATA_PATH).exists():
        return pd.read_csv(config.TRAIN_DATA_PATH)
    raise FileNotFoundError(f"No data file found in {path}")


def clean_data(df):
    """Clean data preserving original logic: drop duplicates, filter HeartRate >= 40."""
    if df is None:
        return df
    df_clean = df.drop_duplicates().copy()
    if "HeartRate" in df_clean.columns:
        df_clean = df_clean[df_clean["HeartRate"] >= 40].reset_index(drop=True)
    return df_clean


def load_train_test(train_path=None, test_path=None):
    """Load train and test data."""
    train_p = train_path or config.TRAIN_DATA_PATH
    test_p = test_path or config.TEST_DATA_PATH
    train_df = pd.read_csv(train_p) if Path(train_p).exists() else None
    test_df = pd.read_csv(test_p) if Path(test_p).exists() else None
    return train_df, test_df

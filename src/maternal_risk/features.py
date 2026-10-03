"""Feature engineering and preprocessing."""

from . import config


def prepare_features(df, target_col=None):
    """Prepare features and target."""
    if df is None:
        return None, None
    target_col = target_col or config.TARGET_COLUMN
    if target_col in df.columns:
        X = df.drop(columns=[target_col])
        y = df[target_col]
    else:
        X = df
        y = None
    return X, y


def get_feature_columns():
    """Return feature columns."""
    return config.FEATURE_COLUMNS

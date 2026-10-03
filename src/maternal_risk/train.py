"""Training logic - preserves original model and params."""
from pathlib import Path

import joblib
from sklearn.model_selection import StratifiedKFold, cross_val_predict, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from . import config, data, features


def build_model(random_state=None):
    """Build SVM model with fixed params as in notebook."""
    rs = random_state if random_state is not None else config.DEFAULT_RANDOM_STATE
    params = config.SVM_PARAMS.copy()
    params["random_state"] = rs
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", SVC(**params)),
        ]
    )


def run_training(config_path=None, data_path=None, output=None, random_state=None):
    """Run training with original logic preserved."""
    rs = random_state if random_state is not None else config.DEFAULT_RANDOM_STATE
    # Load and clean data
    df = data.load_data(data_path)
    clean_df = data.clean_data(df)

    # Split if train/test not present
    train_path = config.TRAIN_DATA_PATH
    test_path = config.TEST_DATA_PATH
    if Path(train_path).exists() and Path(test_path).exists():
        train_df, test_df = data.load_train_test(train_path, test_path)
    else:
        train_df, test_df = train_test_split(
            clean_df,
            test_size=0.2,
            stratify=clean_df[config.TARGET_COLUMN],
            random_state=rs,
        )
        Path(config.DATA_PATH).mkdir(exist_ok=True)
        train_df.to_csv(train_path, index=False)
        test_df.to_csv(test_path, index=False)

    X_train, y_train = features.prepare_features(train_df)

    # Build and train model
    model = build_model(rs)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=rs)
    cross_val_predict(model, X_train, y_train, cv=cv)
    model.fit(X_train, y_train)

    # Save model
    out_dir = Path(output) if output else Path(config.ARTIFACTS_DIR)
    out_dir.mkdir(exist_ok=True)
    model_path = out_dir / "model.pkl"
    joblib.dump(model, model_path)

    return model, model_path

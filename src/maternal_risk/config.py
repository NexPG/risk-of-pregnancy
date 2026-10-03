"""Configuration for maternal risk model."""

DEFAULT_RANDOM_STATE = 42
SVM_PARAMS = {
    "kernel": "rbf",
    "C": 100,
    "gamma": 0.03,
    "class_weight": "balanced",
    "random_state": DEFAULT_RANDOM_STATE,
}
TARGET_COLUMN = "RiskLevel"
LABELS = ["low risk", "mid risk", "high risk"]
FEATURE_COLUMNS = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
DATA_PATH = "data"
TRAIN_DATA_PATH = "data/train.csv"
TEST_DATA_PATH = "data/test.csv"
MODEL_PATH = "models/model.pkl"
ARTIFACTS_DIR = "models"

"""Evaluation metrics."""
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)

from . import config


def compute_metrics(y_true, y_pred, labels=None):
    """Compute evaluation metrics."""
    labels = labels or config.LABELS
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_macro": f1_score(y_true, y_pred, average="macro"),
        "recall": dict(
            zip(
                labels,
                recall_score(y_true, y_pred, labels=labels, average=None).round(3),
            )
        ),
        "precision": dict(
            zip(
                labels,
                precision_score(y_true, y_pred, labels=labels, average=None).round(3),
            )
        ),
    }


def classification_report_text(y_true, y_pred, labels=None):
    """Return classification report text."""
    labels = labels or config.LABELS
    return classification_report(y_true, y_pred, labels=labels, digits=3)

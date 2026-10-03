# Model Card: Maternal Risk Classification

## Model Details
- **Model Name**: Maternal Risk Classification (SVM RBF)
- **Version**: 1.0.0
- **Model Type**: Support Vector Machine with RBF kernel
- **Authors**: Educational ML Project
- **Date**: 2026-10-03
- **License**: Not specified (educational use)
- **Model Architecture**: Scikit-learn Pipeline (StandardScaler + SVC)

**Parameters (locked as per project specification):**
- Kernel: RBF
- C: 100
- gamma: 0.03
- class_weight: balanced
- random_state: 42

## Intended Use
- **Primary Intended Use**: Educational purposes only - demonstration of ML pipeline for maternal health risk classification.
- **Primary Intended Users**: Students, researchers learning MLOps practices.
- **Out-of-Scope Uses**: This model is NOT intended for clinical diagnosis, medical decision-making, or use in healthcare settings. It must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Factors
- **Relevant Factors**: Age, SystolicBP, DiastolicBP, BS (blood sugar), BodyTemp, HeartRate
- **Evaluation Factors**: Class imbalance (3 classes: low/mid/high risk)

## Metrics
- **Primary Metric**: f1_macro (average F1 across all 3 classes)
- **Additional Metrics**: accuracy, precision, recall per class

## Training Data
Training data as processed from the original dataset: duplicates removed, HeartRate >= 40 filtered. Train/test split with stratification (random_state=42). See notebooks for full details.

## Evaluation Data
Held-out test set (20% stratified split) evaluated with cross-validation on training set.

## Ethical Considerations
- This is an educational project. No clinical validation sufficient for medical use.
- Class imbalance handled via class_weight='balanced'.
- Data preprocessing preserves original logic from notebooks.

## Caveats & Recommendations
**IMPORTANT DISCLAIMER**: This is NOT a clinical tool. The predictions from this model should not be used for medical diagnosis or treatment decisions. Always consult qualified healthcare professionals for medical advice. Results are for educational demonstration only.

For full details, see: maternal_risk_final.ipynb, code/EDA.ipynb, code/trainer.ipynb

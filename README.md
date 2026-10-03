# Maternal Health Risk

Прогноз уровня риска при беременности: `low risk` / `mid risk` / `high risk`.

Метрика отбора — **f1_macro**. Дополнительно смотрим recall mid и high.

Учебный проект. Модель не клинический инструмент и не заменяет врача.
Карточка модели: [MODEL_CARD.md](MODEL_CARD.md).
Жизненный цикл: [docs/MODEL_LIFECYCLE.md](docs/MODEL_LIFECYCLE.md), схема BPMN: [docs/model_lifecycle.bpmn](docs/model_lifecycle.bpmn).

## Данные

Maternal Health Risk Data Set.

Признаки: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate.

| этап | строк |
| --- | --- |
| сырой файл | 1014 |
| полные дубли | 562 |
| после дедупа + фильтр HeartRate < 40 | 451 |
| train / test (80/20, stratify) | 360 / 91 |

Дубли убраны: иначе одна и та же строка попадает в train и test.

## Модели (OOF, train)

| модель | f1_macro | recall mid | recall high |
| --- | --- | --- | --- |
| Logistic Regression | 0.60 | 0.32 | 0.63 |
| SVM RBF | **0.69** | **0.40** | 0.83 |
| Decision Tree | 0.67 | 0.35 | 0.79 |
| Random Forest | 0.68 | 0.32 | 0.87 |
| XGBoost | 0.69 | 0.40 | 0.83 |
| MLP | 0.62 | 0.28 | 0.71 |
| стек SVM+RF+XGB | ~0.67 | 0.34 | 0.82 |

Финал — **SVM** (`kernel=rbf`, `C=100`, `gamma=0.03`, `class_weight=balanced`): то же качество, что у XGB, модель проще.

## Тест (SVM)

| метрика | точка | 95% CI |
| --- | --- | --- |
| accuracy | 0.65 | 0.55–0.75 |
| f1_macro | 0.58 | 0.48–0.68 |
| recall low | 0.81 | 0.69–0.92 |
| recall mid | 0.24 | 0.06–0.44 |
| recall high | 0.70 | 0.50–0.88 |

High отделяется, mid — нет. В тесте 21 mid, интервал широкий. На уникальных профилях потолок примерно 0.65–0.70 f1_macro; 0.90+ обычно получают на сырых 1014 с копиями.

## Что в репозитории

- `data/` — сырой xlsx, `train.csv`, `test.csv`
- `code/EDA.ipynb` — разведка, дубли, артефакт пульса 7, сплит
- `code/trainer.ipynb` — подбор гиперпараметров, сравнение моделей
- `maternal_risk_final.ipynb` — финальный пайплайн в ноутбуке
- `src/maternal_risk/` — тот же пайплайн пакетом: `config`, `data`, `features`, `train`, `predict`, `evaluate`
- `scripts/train.py`, `scripts/predict.py` — запуск из командной строки
- `tests/` — очистка данных и предсказание трёх классов
- `pyproject.toml`, `poetry.lock` — зависимости
- `.pre-commit-config.yaml` — black, isort, flake8
- [MODEL_CARD.md](MODEL_CARD.md) — карточка модели
- [docs/MODEL_LIFECYCLE.md](docs/MODEL_LIFECYCLE.md) — жизненный цикл в Mermaid
- [docs/model_lifecycle.bpmn](docs/model_lifecycle.bpmn) — тот же процесс в BPMN 2.0

Ноутбуки остаются исследовательскими. Источник истины для запуска — `src/`.

## Окружение

Нужны Python 3.10+ и Poetry. Окружение в git не хранится.

```powershell
poetry install
poetry run pre-commit install
poetry run pre-commit run --all-files
poetry run pytest
poetry run python scripts/train.py
poetry run python scripts/predict.py --input data/test.csv
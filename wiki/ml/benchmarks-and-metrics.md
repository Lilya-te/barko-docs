---
type: ml
tags: [metrics, benchmarks, k3, k5]
sources: [ml-ideas-notes, helpdog-notebook-notes]
updated: 2026-06-09
status: stable
---

# Benchmarks and Metrics

## K3 — бенчмарки

1. **Внутренний:** сравнение всех кандидатов на едином split.
2. **Cross-source:** train на одном источнике, test на другом (где возможно).
3. **Baseline-to-baseline:** сравнение с `DummyClassifier` как нижней границей.

## K3 — метрики

| Категория | Метрики |
|-----------|---------|
| Основная | `ROC-AUC` |
| Дополнительные | `PR-AUC`, `Recall` (high-risk), `F1`, `Balanced Accuracy` |
| Калибровка | `Brier score`, calibration curve |

**Целевой ориентир MVP:** `ROC-AUC >= 0.75` на отложенной выборке.

## K5 — LLM + RAG

### Retrieval

- `Recall@k`
- Доля ответов с корректными источниками

### Generation quality

- Экспертная оценка полезности (Likert 1–5)
- Доля безопасных ответов (без неэтичных рекомендаций)
- Latency (`p50` / `p95`)

### Product metrics

- Доля успешно закрытых вопросов
- CSAT по чату

## Шаблон таблицы результатов (K3)

| Модель | ROC-AUC | PR-AUC | Recall (high-risk) | F1 | Brier | Комментарий |
|--------|--------:|-------:|-------------------:|---:|------:|-------------|
| Dummy | | | | | | нижняя граница |
| LogisticRegression | | | | | | интерпретируемая база |
| DecisionTree | | | | | | нелинейный baseline |
| RandomForest | | | | | | кандидат в MVP |
| XGBoost/LightGBM | | | | | | расширенный baseline |

### C-BARQ baseline (K3)

Таблица ниже — **ещё не заполнена**. Baseline на C-BARQ датасетах не запускался.

### HelpDog EDA (продуктовые данные)

Из `analytics/helpdog.ipynb` — exploratory analysis, **не ML benchmark**:

| Метрика | Значение |
|---------|----------|
| Пристроены ≥1 раз | 46 / 90 |
| Возвраты в приют | 26 / 46 (~57%) |

См. [helpdog-adoption-eda](helpdog-adoption-eda.md). Кандидат таргета: [adoption-return](../concepts/adoption-return.md).

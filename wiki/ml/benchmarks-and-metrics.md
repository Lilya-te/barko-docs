---
type: ml
tags: [metrics, benchmarks, k3, k5, nir3, recommendations]
sources: [ml-ideas-notes, helpdog-notebook-notes, nir3-hypotheses, nir3-ml-evaluation-pipeline]
updated: 2026-11-15
status: stable
---

# Benchmarks and Metrics

## Рекомендации плана (НИР-3) — основной измеримый контур семестра

Постановка: [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md).

| Гипотеза | Метрика | Порог / эталон |
|----------|---------|----------------|
| H₁-baseline | macro-F1 top-5 vs эксперт G | ≥ 0,6; random ≈ 0,125 (N=40, \|P\|=\|G\|=5) |
| H₁-plan | macro-F1_ML vs macro-F1_rule | ML строго лучше rule на том же val |
| H₁-quality | \(P_{\text{accept}}\), доля «безопасна» | ≥ 95% / ≥ 99% |
| H₁-transfer / H₁-channel | TOST по доменным скорам | заранее заданный δ, α = 0,05 |
| H₁-human-eval | доля предпочтений K5-RAG | ≥ 70% и значимо > 50% |

Формула на анкету \(i\): \(TP_i = |P_i \cap G_i|\), \(\mathrm{F1}_i = TP_i/5\); macro-F1 — среднее по выборке оценки.

### Шаблон таблицы (рекомендации)

| Метод | macro-F1 (val) | vs random | vs rule | Комментарий |
|-------|---------------:|----------:|--------:|-------------|
| Random top-5 | 0,125 | — | — | нижняя граница |
| Rule-based (домен+T) | | | — | H₁-baseline |
| LogisticRegression | | | | кандидат H₁-plan |
| DecisionTree | | | | формулировка Б2 |
| RandomForest | | | | кандидат H₁-plan |

Таблица **не заполнена** фактическими прогонами.

## K3 risk — бенчмарки (исторический контур)

1. **Внутренний:** сравнение всех кандидатов на едином split.
2. **Cross-source:** train на одном источнике, test на другом (где возможно).
3. **Baseline-to-baseline:** сравнение с `DummyClassifier` как нижней границей.

## K3 risk — метрики

| Категория | Метрики |
|-----------|---------|
| Основная | `ROC-AUC` |
| Дополнительные | `PR-AUC`, `Recall` (high-risk), `F1`, `Balanced Accuracy` |
| Калибровка | `Brier score`, calibration curve |

**Целевой ориентир (risk):** `ROC-AUC >= 0.75` на отложенной выборке. Не является критерием H₁ НИР-3.

## K5 — LLM + RAG

### Retrieval

- `Recall@k`
- Доля ответов с корректными источниками

### Generation quality

- Экспертная оценка полезности (Likert 1–5)
- Слепой pairwise A/B vs no-RAG (H₁-human-eval): preference ≥ 70%
- Доля безопасных ответов (без неэтичных рекомендаций)
- Latency (`p50` / `p95`)

### Product metrics

- Доля успешно закрытых вопросов
- CSAT по чату

## Шаблон таблицы результатов (K3 risk)

| Модель | ROC-AUC | PR-AUC | Recall (high-risk) | F1 | Brier | Комментарий |
|--------|--------:|-------:|-------------------:|---:|------:|-------------|
| Dummy | | | | | | нижняя граница |
| LogisticRegression | | | | | | интерпретируемая база |
| DecisionTree | | | | | | нелинейный baseline |
| RandomForest | | | | | | кандидат в MVP |
| XGBoost/LightGBM | | | | | | расширенный baseline |

### C-BARQ baseline (K3 risk)

Таблица ниже — **ещё не заполнена**. Baseline риска на C-BARQ датасетах не запускался.

### HelpDog EDA (продуктовые данные)

Из `analytics/helpdog_forum/helpdog.ipynb` — exploratory analysis, **не ML benchmark**:

| Метрика | Значение |
|---------|----------|
| Пристроены ≥1 раз | 46 / 90 |
| Возвраты в приют | 26 / 46 (~57%) |

См. [helpdog-adoption-eda](helpdog-adoption-eda.md). Кандидат таргета: [adoption-return](../concepts/adoption-return.md).

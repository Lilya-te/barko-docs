---
type: ml
tags: [metrics, benchmarks, k3, k5, nir3, recommendations]
sources: [ml-ideas-notes, helpdog-notebook-notes, nir3-hypotheses, nir3-ml-evaluation-pipeline, nir3-literature-delta]
updated: 2026-11-16
status: stable
---

# Benchmarks and Metrics

## Рекомендации плана (НИР-3) — основной измеримый контур семестра

Постановка: [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md).

| Гипотеза | Метрика | Порог / эталон |
|----------|---------|----------------|
| H₁-baseline | macro-F1 top-5 vs эксперт G | ≥ 0,6; random ≈ 0,125 (N=40, card(P)=card(G)=5) |
| H₁-plan | macro-F1_ML vs macro-F1_rule | ML строго лучше rule на том же val |
| H₁-quality | $P_{\text{accept}}$, доля «безопасна» | ≥ 95% / ≥ 99% |
| H₁-transfer / H₁-channel | TOST по доменным скорам | заранее заданный δ, α = 0,05 |
| H₁-human-eval | доля предпочтений K5-RAG | ≥ 70% и значимо > 50% |

Формула на анкету $i$: $TP_i = \lvert P_i \cap G_i \rvert$, $\mathrm{F1}_i = TP_i/5$; macro-F1 — среднее по выборке оценки.

**Random baseline** (равномерный выбор $k$ из $N$ без возвращения, card(G)=k):

$$
\mathbb{E}[TP] = k \cdot \frac{k}{N},\qquad \mathbb{E}[F1] = \frac{k}{N}.
$$

При $N=40$, $k=5$: $\mathbb{E}[F1]=0.125$. Порог H₁ «≥ 3 из 5» ↔ $F1 \ge 0.6$. Primary metric — **example-F1** (среднее по анкетам); не путать со sklearn label-macro-F1. Hamming / subset accuracy не использовать как sole metric при sparse top-5. Источник вывода: Б1 → [nir3-literature-delta](../sources/nir3-literature-delta.md).

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

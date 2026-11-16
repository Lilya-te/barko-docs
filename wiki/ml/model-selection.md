---
type: ml
tags: [k3, models, baseline, nir3, recommendations]
sources: [ml-ideas-notes, nir3-literature-delta, nir3-hypotheses]
updated: 2026-11-16
status: stable
---

# Model Selection

Сравнение кандидатов моделей и обоснование выбора для Hvostun.

## Рекомендации плана (НИР-3, H₁-plan)

Контекст: multilabel / top-5 из каталога $N \approx 40$ по доменам C-BARQ(Mini). Сравнение на **том же val**, что rule-based; метрика — example-F1. Источник: Б1 → [nir3-literature-delta](../sources/nir3-literature-delta.md).

| Критерий | LogisticRegression | DecisionTree |
|----------|--------------------|--------------|
| За | Стабильна на малых n; коэффициенты читаемы; калибруемые scores → top-5; близка к порогам rule-based | Нелинейности и взаимодействия доменов; правила в листьях; соответствует формулировке H₁-plan (Б2) |
| Против | Нет взаимодействий без feature engineering; one-vs-rest × 40 лейблов шумит при малом n | Overfit; нестабильность; грубые вероятности без pruning |
| Роль | **Первая ML-линия** после rule-based | Проверка нелинейных правил (`max_depth` ограничен) |
| Дальше | Если оба ≤ rule → в продукт rule; если лучше → H₁-quality; при росте n — RandomForest | |

**Rule-based параметры:** полная матрица доменов×рекомендаций $14 \times 40 = 560$ порогов; реалистичный sparse mapping ~40–80 рёбер (см. [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md)).

## K3 risk — сравнительная таблица (исторический контур)

| Кандидат | Плюсы | Риски | Потенциал улучшения | Рекомендация |
|----------|-------|-------|---------------------|--------------|
| `DummyClassifier` | Контрольная нижняя граница | Бесполезен продуктово | Нет | Только sanity check |
| `LogisticRegression` | Интерпретируемая, стабильна на малых данных | Слабее на нелинейностях | Высокий (feature engineering, calibration) | Baseline |
| `DecisionTree` | Простая нелинейность, объяснимость | Переобучение | Средний | Baseline |
| `RandomForest` | Устойчивее, обычно лучше по качеству | Менее прозрачная | Высокий | **Основной кандидат MVP (risk)** |
| `XGBoost` / `LightGBM` | Часто best-in-class на tabular | Больше tuning, риск overfit на малых данных | Очень высокий | Расширенный baseline (если данных достаточно) |

## Вывод по K3 risk

- **Базовый набор:** `LogisticRegression`, `DecisionTree`, `RandomForest`
- **Расширенный:** `XGBoost` / `LightGBM` при достаточном объёме данных
- **MVP-кандидат (risk):** `RandomForest` + обязательная интерпретация через `LogisticRegression`

## K5 — вывод

- Готовая **LLM API + RAG** — постоянная стратегия.
- Фокус: retrieval, prompt-policy, red-flag rules, human-reviewed KB.
- Multi-model pipeline (ответ + гуманность + здоровье) — на рассмотрении.

## Своя модель vs существующая

| Компонент | MVP | Следующий этап |
|-----------|-----|----------------|
| Рекомендации (НИР-3) | Rule-based → LR/DT сравнение | RF при росте разметки; H₁-quality |
| K3 risk | Baseline tabular ML | Собственная модель после накопления данных |
| K5 | LLM API + RAG | Улучшение RAG, промптов, safety, KB |
| K6 | Отсутствует | Собственная модель ranking |

См. [k3-risk-prediction](../components/k3-risk-prediction.md), [k5-ai-chat](../components/k5-ai-chat.md), [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md).

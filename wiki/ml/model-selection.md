---
type: ml
tags: [k3, models, baseline]
sources: [ml-ideas-notes]
updated: 2026-06-09
status: stable
---

# Model Selection

Сравнение кандидатов моделей и обоснование выбора для Barko.

## K3 — сравнительная таблица

| Кандидат | Плюсы | Риски | Потенциал улучшения | Рекомендация |
|----------|-------|-------|---------------------|--------------|
| `DummyClassifier` | Контрольная нижняя граница | Бесполезен продуктово | Нет | Только sanity check |
| `LogisticRegression` | Интерпретируемая, стабильна на малых данных | Слабее на нелинейностях | Высокий (feature engineering, calibration) | Baseline |
| `DecisionTree` | Простая нелинейность, объяснимость | Переобучение | Средний | Baseline |
| `RandomForest` | Устойчивее, обычно лучше по качеству | Менее прозрачная | Высокий | **Основной кандидат MVP** |
| `XGBoost` / `LightGBM` | Часто best-in-class на tabular | Больше tuning, риск overfit на малых данных | Очень высокий | Расширенный baseline (если данных достаточно) |

## Вывод по K3

- **Базовый набор:** `LogisticRegression`, `DecisionTree`, `RandomForest`
- **Расширенный:** `XGBoost` / `LightGBM` при достаточном объёме данных
- **MVP-кандидат:** `RandomForest` + обязательная интерпретация через `LogisticRegression`

## K5 — вывод

- Готовая **LLM API + RAG** — постоянная стратегия.
- Фокус: retrieval, prompt-policy, red-flag rules, human-reviewed KB.
- Multi-model pipeline (ответ + гуманность + здоровье) — на рассмотрении.

## Своя модель vs существующая

| Компонент | MVP | Следующий этап |
|-----------|-----|----------------|
| K3 | Baseline tabular ML | Собственная модель после накопления данных |
| K5 | LLM API + RAG | Улучшение RAG, промптов, safety, KB |
| K6 | Отсутствует | Собственная модель ranking |

См. [k3-risk-prediction](../components/k3-risk-prediction.md), [k5-ai-chat](../components/k5-ai-chat.md).

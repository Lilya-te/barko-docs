---
type: source
tags: [ml, passport, source]
sources: []
raw_path: _ml_ideas.md
updated: 2026-06-09
status: ingested
---

# Source: Подбор модели для ML-решений (BARKO)

**Исходный файл:** [`_ml_ideas.md`](../../_ml_ideas.md)

## Ключевые выводы

1. **K3 (MVP):** прогноз адаптационных трудностей по профилю собаки и анкете — tabular ML, baseline `RandomForest`.
2. **K5 (MVP):** ИИ-чат — LLM API + RAG, без обучения собственной LLM; фокус на safety и KB.
3. **K6 (roadmap):** next-best-action / ranking — не в MVP.
4. Данные: фрагментарные C-BARQ subsets + harmonization; см. [data-ideas-notes](data-ideas-notes.md).
5. Цель K3: `ROC-AUC >= 0.75`.

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Обзор проекта | [overview](../overview.md) |
| K3 | [k3-risk-prediction](../components/k3-risk-prediction.md) |
| K5 | [k5-ai-chat](../components/k5-ai-chat.md) |
| K6 | [k6-plan-correction](../components/k6-plan-correction.md) |
| Выбор моделей | [model-selection](../ml/model-selection.md) |
| Метрики | [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) |
| План эксперимента | [experiment-plan](../ml/experiment-plan.md) |
| Harmonization | [data-harmonization](../concepts/data-harmonization.md) |

## Не перенесено / требует уточнения

- Конкретная формула таргета для K3
- Фактические результаты экспериментов (таблица метрик пустая)
- Детали multi-model pipeline для K5

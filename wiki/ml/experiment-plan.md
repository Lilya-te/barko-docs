---
type: ml
tags: [experiment, passport, pipeline]
sources: [ml-ideas-notes, helpdog-notebook-notes]
updated: 2026-06-09
status: draft
---

# Experiment Plan

План baseline-эксперимента и критерии готовности раздела «Подбор модели для ML-решений» (Паспорт).

## Прогресс экспериментов

| Этап | Статус | Артефакт |
|------|--------|----------|
| EDA HelpDog (возвраты) | Выполнен | [helpdog-adoption-eda](helpdog-adoption-eda.md) |
| Формула таргета K3 | Черновик | [adoption-return](../concepts/adoption-return.md) |
| C-BARQ harmonization | Не начат | [data-harmonization](../concepts/data-harmonization.md) |
| Baseline K3 (ROC-AUC) | Не начат | [benchmarks-and-metrics](benchmarks-and-metrics.md) |

## Что приложить эксперту

1. Описание датасета и формулы таргета
2. Таблица сравнения моделей (метрики на valid/test)
3. Выбор лучшей baseline-модели и аргументы
4. Краткий вывод:
   - что берём в MVP;
   - что улучшаем без обучения собственной LLM;
   - какие улучшения планируем в НИР

## Пайплайн (целевая архитектура)

```
ingest → clean → feature_map → train → evaluate → calibrate → export model → integrate
```

### Структура кода (опционально)

| Путь | Назначение |
|------|------------|
| `data/` | Сырые и нормализованные данные |
| `src/features/` | Сбор и трансформации признаков |
| `src/models/` | Обучение, валидация, inference |
| `reports/` | EDA и таблицы бенчмарков |
| `api/` | Обёртка `predict_risk(profile)` |

## Критерий готовности раздела

Раздел готов, если:

- [x] Описана постановка задачи и класс моделей
- [x] Есть сравнительная таблица кандидатов и критерии выбора
- [x] Определены бенчмарки и метрики
- [x] Зафиксировано решение по компонентам (своя / существующая)
- [x] Подготовлен шаблон отчёта
- [ ] Заполнены фактические метрики baseline-эксперимента (C-BARQ)
- [x] EDA продуктовых данных (HelpDog) — [helpdog-adoption-eda](helpdog-adoption-eda.md)
- [ ] Утверждена формула таргета (черновик: [adoption-return](../concepts/adoption-return.md))

См. [benchmarks-and-metrics](benchmarks-and-metrics.md), [model-selection](model-selection.md).

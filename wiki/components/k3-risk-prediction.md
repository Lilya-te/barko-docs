---
type: component
tags: [k3, ml, mvp, adaptation]
sources: [ml-ideas-notes, helpdog-notebook-notes, plos-one-2024-short-cbarq-validation, fomina-2024-problem-behavior-review, fomina-2025-ai-pilot-study, gritsenko-2023-owner-frustration]
updated: 2026-06-09
status: draft
---

# K3 — Прогноз адаптационных трудностей

Основная ML-задача MVP Barko.

## Постановка

По профилю собаки и ответам анкеты оценить:
- риск сложной адаптации;
- приоритетные зоны внимания.

## Класс моделей

**Classical ML** (tabular) — классификация риска.

См. [model-selection](../ml/model-selection.md) для сравнения кандидатов.

## Данные

### Признаки (features)

- Профиль собаки + ответы анкеты (C-BARQ и производные).
- C-BARQ источники: 5 собранных датасетов — [collected-datasets-catalog](../datasets/collected-datasets-catalog.md).

### Таргет (label) — кандидат

Из EDA HelpDog: **возврат в приют после пристройства** — см. [adoption-return](../concepts/adoption-return.md), [helpdog-adoption-eda](../ml/helpdog-adoption-eda.md).

| Источник label | Объём | Статус |
|----------------|------:|--------|
| HelpDog (`back_shelter_at`) | 46 пристроенных, 26 возвратов | Кандидат, `draft` |
| C-BARQ proxy (поведенческие риски) | TBD | Для train baseline |

### Ограничения

- Полного open C-BARQ нет → [data-harmonization](../concepts/data-harmonization.md).
- HelpDog: 90 собак, нет C-BARQ — только валидация гипотез о таргете.

## Baseline (текущее решение)

| Роль | Модель |
|------|--------|
| Основной кандидат MVP | `RandomForest` |
| Интерпретация для пользователя/эксперта | `LogisticRegression` |
| Sanity check | `DummyClassifier` |
| Расширенный baseline (при достаточных данных) | `XGBoost` / `LightGBM` |

## Критерии выбора модели

1. Качество (`ROC-AUC`, `PR-AUC`, `Recall` high-risk)
2. Интерпретируемость
3. Устойчивость на малых/фрагментированных данных
4. Скорость внедрения в MVP
5. Потенциал улучшения до собственной модели

## MVP vs следующий этап

| Этап | Решение |
|------|---------|
| MVP | Существующая baseline-модель (tabular ML) |
| Следующий этап | Собственная улучшенная модель после накопления продуктовых данных |

## Метрики и бенчмарки

См. [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md).

Целевой ориентир: **ROC-AUC >= 0.75** на отложенной выборке.

## Открытые вопросы

- [ ] Утвердить формулу таргета: `returned_to_shelter` vs альтернативы — см. [adoption-return](../concepts/adoption-return.md).
- [x] Приоритетные шкалы зафиксированы в [k3-feature-candidates](../concepts/k3-feature-candidates.md); требует EDA на C-BARQ.
- [ ] Выбор MVP-анкеты: C-BARQ(S) vs полная версия.
- [ ] Дедупликация Wolfram ↔ Figshare перед объединением train-set.
- [ ] Запустить baseline K3 (ROC-AUC) на C-BARQ — таблица в [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) пустая.
- [ ] Связать HelpDog-собак с C-BARQ-признаками.

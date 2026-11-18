---
type: ml
tags: [experiment, passport, pipeline, nir3]
sources: [ml-ideas-notes, helpdog-notebook-notes, nir3-hypotheses, nir3-ml-evaluation-pipeline]
updated: 2026-11-15
status: draft
---

# Experiment Plan

План экспериментов: исторический baseline риска (Паспорт) + методика проверки гипотез НИР-3.

Полный пайплайн НИР-3: [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md).

## Прогресс экспериментов

| Этап | Статус | Артефакт |
|------|--------|----------|
| EDA HelpDog (возвраты) | Выполнен | [helpdog-adoption-eda](helpdog-adoption-eda.md) |
| Формула таргета K3 (возврат/риск) | Черновик | [adoption-return](../concepts/adoption-return.md) |
| C-BARQ mini harmonization | Выполнен (unified) | [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md) |
| Baseline K3 (ROC-AUC / риск) | Не начат | [benchmarks-and-metrics](benchmarks-and-metrics.md) |
| Методика H₁ НИР-3 (рекомендации) | Описана | [nir3-hypothesis-evaluation-pipeline](nir3-hypothesis-evaluation-pipeline.md) |
| Rule-based mapping (H₁-baseline) | Не начат | каталог + научный консультант |
| Экспертная разметка G | В процессе (админка) | [research-data-app](../concepts/research-data-app.md) |
| NLP-канал / vector index пунктов | Не начат | [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md) |

## Два измеримых контура

| Контур | Таргет | Метрика | Источник постановки |
|--------|--------|---------|---------------------|
| **A. Risk (исторический K3)** | трудность адаптации / прокси возврата | ROC-AUC ≥ 0,75 | [ml-ideas-notes](../sources/ml-ideas-notes.md) |
| **B. Recommendations (НИР-3)** | top-5 пунктов каталога | macro-F1, accept/safe, TOST, RAG preference | [nir3-hypotheses](../sources/nir3-hypotheses.md) |

Контур **B** — основной для проверки личных гипотез семестра. Контур **A** не отменён, но не блокирует методику Б3.

## Открытый вопрос по split (Б3)

В Б3: train/val = Bohland+Serpell, test = РФ. Для H₁-baseline/plan нужны этикетки каталога G — их нет на foreign-сессиях. Варианты:

1. train/val на размеченном РФ-пилоте; референс только для H₁-transfer / признаков;
2. synthetic/перенесённые этикетки на референс (требует отдельного обоснования).

До решения в отчётах явно указывать, на какой выборке считался macro-F1.

## Что приложить эксперту / комиссии

1. Формулировки H₁ / H₀ и формулы метрик ([nir3-hypotheses](../sources/nir3-hypotheses.md))
2. Описание датасета, канала, версии анкеты, split
3. Таблица: random → rule-based → DT / LR OvR (macro-F1 на одном val; Δ ≥ 0.10)
4. Expert accept/safe (H₀: accept < 60% или safe < 97%); при наличии — TOST и RAG pairwise
5. Вывод: что идёт в продукт (rule vs max(Δ) ML), что отложено

## Пайплайн (целевая архитектура)

```
ingest → clean/harmonize → feature_map → baseline(rule) → train(DT|LR OvR) → evaluate(val) → expert gate (test)
text → embed → vector (пункты) → NLP scores → TOST vs self-report
wiki → vector RAG → pairwise human-eval
```

Исторический risk-пайплайн (если нужен отдельно):

```
ingest → clean → feature_map → train → evaluate → calibrate → export model → integrate
```

## Критерий готовности раздела

- [x] Описана постановка и класс моделей (risk + recommendations)
- [x] Есть сравнительная таблица кандидатов и критерии выбора
- [x] Определены бенчмарки и метрики (включая НИР-3)
- [x] Зафиксировано решение по компонентам (своя / существующая)
- [x] Подготовлен шаблон отчёта / методика Б3
- [x] EDA HelpDog — [helpdog-adoption-eda](helpdog-adoption-eda.md)
- [x] Unified mini C-BARQ — [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md)
- [ ] Фактические метрики rule-based / ML (macro-F1)
- [ ] Утверждён split с учётом наличия этикеток G
- [ ] Утверждена формула таргета риска (черновик: [adoption-return](../concepts/adoption-return.md))

См. [benchmarks-and-metrics](benchmarks-and-metrics.md), [model-selection](model-selection.md).

# Barko Wiki — Index

Каталог страниц knowledge base. Обновлён: 2026-07-28 (реорганизация путей к источникам).

## Overview

| Страница | Описание |
|----------|----------|
| [overview](overview.md) | Barko: продукт, ML-компоненты, текущий статус исследований |
| [socio-economic-impact](socio-economic-impact.md) | Прогнозируемые социально-экономические эффекты |

## Components (K3 / K5 / K6)

| Страница | Описание |
|----------|----------|
| [k3-risk-prediction](components/k3-risk-prediction.md) | Прогноз адаптационных трудностей — основная ML-задача MVP |
| [k5-ai-chat](components/k5-ai-chat.md) | ИИ-чат на LLM + RAG с экспертной базой |
| [k6-plan-correction](components/k6-plan-correction.md) | Автокоррекция плана (next-best-action) — roadmap |

## Concepts

| Страница | Описание |
|----------|----------|
| [c-barq](concepts/c-barq.md) | Опросник C-BARQ: что это, шкалы, ограничения доступа |
| [data-harmonization](concepts/data-harmonization.md) | Объединение фрагментарных C-BARQ подмножеств для baseline |
| [adoption-return](concepts/adoption-return.md) | Возврат в приют как кандидат на таргет K3 |
| [k3-feature-candidates](concepts/k3-feature-candidates.md) | Приоритетные C-BARQ признаки для K3 (синтез статей) |
| [problem-behavior-taxonomy](concepts/problem-behavior-taxonomy.md) | Таксономия проблемного поведения |
| [owner-dog-attachment](concepts/owner-dog-attachment.md) | Тип привязанности владелец–собака |
| [owner-frustration](concepts/owner-frustration.md) | Разочарованность владельца (~14%) |
| [research-data-app](concepts/research-data-app.md) | Внутреннее приложение сбора данных: монолит, compose, схема Postgres |

## Datasets

| Страница | Описание |
|----------|----------|
| [collected-datasets-catalog](datasets/collected-datasets-catalog.md) | Сводка собранных датасетов для K3 baseline |
| [cbarq-open-data-landscape](datasets/cbarq-open-data-landscape.md) | Карта открытых и полуоткрытых C-BARQ источников |
| [2017-wolfram](datasets/2017-wolfram.md) | Wolfram C-BARQ Survey — 12 060 строк, доменные шкалы |
| [figshare-cbarq-dat](datasets/figshare-cbarq-dat.md) | Figshare C-BARQ — 12 061 строк, доменные шкалы |
| [padova-cbarq-italian](datasets/padova-cbarq-italian.md) | Padova — 807 строк, item-level (итальянский) |
| [padova-cbarq-column-dictionary](datasets/padova-cbarq-column-dictionary.md) | Словарь колонок Padova: перевод IT→EN и `@nn`→`question_nnn` |
| [manydogs-md1](datasets/manydogs-md1.md) | ManyDogs 1 — 705 строк, частичный C-BARQ |
| [plos-one-2024-short-cbarq](datasets/plos-one-2024-short-cbarq.md) | PLOS ONE 2024 — ~435 собак, short/full C-BARQ |
| [helpdog-forum-adoptions](datasets/helpdog-forum-adoptions.md) | HelpDog — 90 собак, история пристройств и возвратов |

## ML

| Страница | Описание |
|----------|----------|
| [model-selection](ml/model-selection.md) | Сравнение кандидатов моделей и критерии выбора |
| [benchmarks-and-metrics](ml/benchmarks-and-metrics.md) | Бенчмарки и метрики для K3 и K5 |
| [mvp-verifiable-metrics](ml/mvp-verifiable-metrics.md) | Измеримые метрики MVP вместо возврата как основной рабочей гипотезы |
| [experiment-plan](ml/experiment-plan.md) | План baseline-эксперимента и критерии готовности для Паспорта |
| [helpdog-adoption-eda](ml/helpdog-adoption-eda.md) | EDA возвратов в приют (57% среди пристроенных) |
| [cbarq-clustering](ml/cbarq-clustering.md) | Exploratory KMeans/GMM-кластеризация Padova; ограничения интерпретации |

## Sources

| Страница | Исходный файл | Описание |
|----------|---------------|----------|
| [ml-ideas-notes](sources/ml-ideas-notes.md) | `_ml_ideas.md` | Подбор модели для ML-решений BARKO |
| [app-ideas-notes](sources/app-ideas-notes.md) | `_app_ideas/_database_architecture.md` | Схема БД и scope research-ops |
| [data-ideas-notes](sources/data-ideas-notes.md) | `analytics/research/datatsets/_data_ideas.md` | Исследование открытых C-BARQ датасетов |
| [foreign-datasets-list-notes](sources/foreign-datasets-list-notes.md) | `analytics/research/datatsets/foreign_datasets_list.md` | Каталог собранных датасетов |
| [helpdog-notebook-notes](sources/helpdog-notebook-notes.md) | `analytics/helpdog_forum/helpdog.ipynb` | EDA пристройств HelpDog |
| [cbarq-clustering-notebooks](sources/cbarq-clustering-notebooks.md) | `analytics/research/notebooks/11,12,21_*.ipynb` | KMeans/GMM кластеризация доменных шкал Padova |
| [plos-one-2024-short-cbarq-validation](sources/plos-one-2024-short-cbarq-validation.md) | `статьи/journal.pone.0299973.pdf` | Валидация C-BARQ(S), 435 собак |
| [fomina-2024-problem-behavior-review](sources/fomina-2024-problem-behavior-review.md) | `статьи/4+RPJ+21(4)+РУ+Фомина.pdf` | Обзор 132 статей |
| [fomina-2025-ai-pilot-study](sources/fomina-2025-ai-pilot-study.md) | `статьи/11+РПЖ+22(4)+Фомина.pdf` | CBARQ + AI, n=35 |
| [gritsenko-2023-owner-frustration](sources/gritsenko-2023-owner-frustration.md) | `статьи/Gritsenko.pdf` | Опрос 5820 владельцев |
| [gilchrist-2025-shelter-cbarq](sources/gilchrist-2025-shelter-cbarq.md) | `статьи/4 Gilchrist_et_al_ABC_12(1).pdf` | Shelter C-BARQ: 24 пункта, 5 факторов |

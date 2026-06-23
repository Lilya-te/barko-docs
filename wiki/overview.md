---
type: overview
tags: [barko, mvp, ml]
sources: [ml-ideas-notes, data-ideas-notes, helpdog-notebook-notes]
updated: 2026-06-09
status: draft
---

# Barko — Overview

**Barko** — продукт для поддержки адаптации собак. ML-слой даёт персонализированный прогноз трудностей, а не общие советы.

## ML-компоненты

| Компонент | Статус MVP | Подход | Страница |
|-----------|------------|--------|----------|
| **K3** — прогноз адаптационных трудностей | MVP | Classical ML (tabular) | [k3-risk-prediction](components/k3-risk-prediction.md) |
| **K5** — ИИ-чат | MVP | LLM API + RAG | [k5-ai-chat](components/k5-ai-chat.md) |
| **K6** — автокоррекция плана | Roadmap | Learning-to-rank / next-best-action | [k6-plan-correction](components/k6-plan-correction.md) |

## Зачем ML

- Статические правила плохо масштабируются на разные профили собак.
- УТП Barko: «прогноз именно для вашей собаки».
- K3 даёт вероятность риска; K5 даёт grounded-советы из экспертной базы.

## Социально-экономический эффект

Прогнозируемые эффекты разработки — см. [socio-economic-impact](socio-economic-impact.md):

- **Экономика:** снижение затрат на возвраты (~45 000 руб./случай; ~620 млн руб./год по системе приютов).
- **Социум:** меньше бездомных животных, просвещение о гуманной кинологии, доступ к пристройству для **32%** «готовых, но боящихся» потенциальных хозяев.

## Данные

Основной инструмент поведенческой оценки — [C-BARQ](concepts/c-barq.md). Полного открытого датасета нет; см. [ландшафт данных](datasets/cbarq-open-data-landscape.md) и [harmonization](concepts/data-harmonization.md).

## Текущие решения (из первого ingest)

- **K3 baseline:** `RandomForest` + интерпретация через `LogisticRegression`; цель `ROC-AUC >= 0.75`.
- **K5:** готовая LLM через API, фокус на RAG, safety rules, human-reviewed knowledge base.
- **K6:** не в MVP.

## Связанные артефакты в репозитории

- `_ml_ideas.md` — исходная заметка по ML (ingested → [ml-ideas-notes](sources/ml-ideas-notes.md))
- `datatsets/_data_ideas.md` — исходная заметка по датасетам (ingested → [data-ideas-notes](sources/data-ideas-notes.md))
- `datatsets/foreign_datasets_list.md` — каталог собранных датасетов (ingested → [collected-datasets-catalog](datasets/collected-datasets-catalog.md))
- `analytics/helpdog.ipynb` — EDA пристройств HelpDog (ingested → [helpdog-adoption-eda](ml/helpdog-adoption-eda.md); ~57% возвратов)
- `статьи/*.pdf` — 4 статьи ingested → [sources/](sources/plos-one-2024-short-cbarq-validation.md), [k3-feature-candidates](concepts/k3-feature-candidates.md)

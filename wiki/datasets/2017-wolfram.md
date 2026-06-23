---
type: dataset
tags: [c-barq, collected, k3, wolfram]
sources: [foreign-datasets-list-notes]
raw_file: 2017_wolfram.csv
updated: 2026-06-09
status: stable
cbarq_coverage: full
rows: 12060
format: csv
---

# 2017 Wolfram C-BARQ Survey

Крупный open-датасет с агрегированными доменными шкалами C-BARQ.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `2017_wolfram.csv` |
| Строк | 12 060 |
| Размер | ~1.60 MB |
| Формат | CSV (доменные шкалы) |
| C-BARQ | Полностью (агрегированные шкалы) |
| Источник | [Wolfram Data Repository — C-BARQ Survey](https://datarepository.wolframcloud.com/resources/C-BARQ-Survey) |

## Ключевые поля

Агрегированные доменные оценки C-BARQ, в т.ч.:
- `StrangerDirectedAggression`
- `Trainability`
- `SeparationRelatedBehavior`
- `EnergyLevel`
- и др.

## Релевантность для K3

- Подходит как основной источник для baseline: большой объём, готовые доменные шкалы.
- Не требует агрегации из сырых ответов — проще для [harmonization](../concepts/data-harmonization.md).
- Кандидаты на признаки риска адаптации: `SeparationRelatedBehavior`, страх, агрессия.

## Заметки для harmonization

- Формат полей: PascalCase (`StrangerDirectedAggression`).
- Сопоставить с [figshare-cbarq-dat](figshare-cbarq-dat.md) — почти идентичный объём (12 060 vs 12 061 строк); возможное пересечение или дубликат, требует проверки.
- Маппинг на общую schema: lowercase-алиасы как в Figshare (`strangeraggr` ↔ `StrangerDirectedAggression`).

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [cbarq-open-data-landscape](cbarq-open-data-landscape.md)

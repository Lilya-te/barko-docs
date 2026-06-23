---
type: dataset
tags: [c-barq, collected, k3, padova, raw-responses]
sources: [foreign-datasets-list-notes]
raw_file: Dataset_CBARQ.xlsx
updated: 2026-06-09
status: stable
cbarq_coverage: full
rows: 807
format: xlsx
---

# Padova C-BARQ (Italian Translation)

Датасет валидации итальянского перевода C-BARQ с **сырыми ответами** на уровне пунктов анкеты.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `Dataset_CBARQ.xlsx` |
| Строк | 807 |
| Размер | ~0.37 MB |
| Формат | Excel |
| C-BARQ | Полностью (item-level, итальянская версия) |
| Источник | [University of Padova CAB Research Data](https://researchdata.cab.unipd.it/808/) |
| Публикация | Validation of the Italian translation of C-BARQ |

## Ключевые поля

Пункты анкеты в формате `@1`, `@2`, … с формулировками вопросов на итальянском.

## Релевантность для K3

- Единственный собранный датасет с **сырыми item-level** ответами — полезен для feature engineering.
- Малый объём (807) — хорош для валидации, но не как единственный train-set.
- Позволяет проверить, какие конкретные вопросы C-BARQ наиболее предиктивны.

## Заметки для harmonization

- Требует агрегации item-level → доменные шкалы перед объединением с Wolfram/Figshare.
- Язык вопросов — итальянский; маппинг на стандартные C-BARQ item IDs.
- Cross-source benchmark: train на Wolfram (доменные шкалы), test на агрегированных Padova данных.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [data-harmonization](../concepts/data-harmonization.md)

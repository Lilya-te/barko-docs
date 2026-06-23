---
type: dataset
tags: [c-barq, collected, k3, plos-one, raw-responses]
sources: [foreign-datasets-list-notes, data-ideas-notes, plos-one-2024-short-cbarq-validation]
raw_file: pone.0299973.s001.csv
updated: 2026-06-09
status: stable
cbarq_coverage: full
rows: 435
format: csv
---

# PLOS ONE 2024 — Shortened C-BARQ Validation

Supplementary data к статье о валидации сокращённой версии C-BARQ. Один из немногих открытых датасетов с реальными ответами.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `pone.0299973.s001.csv` |
| Строк | ~435 (из [data-ideas-notes](../sources/data-ideas-notes.md)) |
| Формат | CSV (supplementary data) |
| C-BARQ | Полностью (полная + сокращённая версия) |
| Источник | [Validation of shortened C-BARQ (PLOS ONE, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008875/) |

## Содержание

- Реальные ответы C-BARQ (435 пар владелец–собака, DAP)
- Сопоставление **полной** (100 пунктов) и **сокращённой** C-BARQ(S) (42 пункта)
- Pearson r >0.60 для 12 из 14 доменов — см. [plos-one-2024-short-cbarq-validation](../sources/plos-one-2024-short-cbarq-validation.md)
- Релевантно для MVP-анкеты Barko на базе **C-BARQ(S)**

## Релевантность для K3

- Прямая связь с выбором версии анкеты для продукта.
- Малый объём — validation set, не основной train.
- Item-level данные — возможность оценить, какие вопросы short version сохраняют предиктивную силу.

## Валидация (PLOS ONE 2024)

- DOI: [10.1371/journal.pone.0299973](https://doi.org/10.1371/journal.pone.0299973)
- Supplementary: `pone.0299973.s001.csv`
- Ключевые домены для K3: separation-related (r=0.68), stranger-directed fear (0.81), aggression (0.77)

## Заметки для harmonization

- Связать short/full item mapping с доменными шкалами Wolfram/Figshare.
- [ ] Схема столбцов CSV — уточнить при EDA файла.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [c-barq](../concepts/c-barq.md)
- [data-ideas-notes](../sources/data-ideas-notes.md)

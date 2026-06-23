---
type: dataset
tags: [c-barq, collected, k3, manydogs, partial]
sources: [foreign-datasets-list-notes]
raw_file: md1_data/manydogs_etal_2024_data.csv
updated: 2026-06-09
status: stable
cbarq_coverage: partial
rows: 705
format: csv
---

# ManyDogs 1 (md1_data)

Датасет проекта ManyDogs 1: экспериментальные данные + **частичный блок C-BARQ**.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Репозиторий | [GitHub — ManyDogsProject/md1_data](https://github.com/ManyDogsProject/md1_data) |
| Основной файл | `manydogs_etal_2024_data.csv` |
| Строк | 705 |
| Размер файла | ~0.86 MB |
| Размер папки | ~3.73 MB |
| C-BARQ | Частично |
| DOI | [10.5334/jopd.109](https://doi.org/10.5334/jopd.109) |

## Структура данных

### C-BARQ блок

Переменные с префиксом `cbarq_`:
- `cbarq_train_*`
- `cbarq_aggression_*`
- `cbarq_fear_*`
- и др.

### Не-C-BARQ блок (эксперимент)

- `onecup_*`, `twocup_*`
- `ostensive_*`, `odor_*`
- и др.

## Релевантность для K3

- C-BARQ-переменные можно извлечь для обучения/валидации.
- Экспериментальные переменные — **не для K3 baseline**, но потенциально интересны для будущих исследований.
- Малый объём (705) — лучше как hold-out / cross-source test, чем как основной train.

## Заметки для harmonization

- Извлечь только `cbarq_*` столбцы; отбросить экспериментальные.
- Маппинг `cbarq_aggression_*` → стандартные домены C-BARQ.
- Git-репозиторий — стабильный источник, предпочтительнее временных S3-ссылок.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [data-harmonization](../concepts/data-harmonization.md)

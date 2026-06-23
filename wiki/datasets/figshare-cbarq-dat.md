---
type: dataset
tags: [c-barq, collected, k3, figshare]
sources: [foreign-datasets-list-notes]
raw_file: CBARQ.dat
updated: 2026-06-09
status: stable
cbarq_coverage: full
rows: 12061
format: dat
---

# Figshare C-BARQ Survey

Крупный open-датасет C-BARQ на Figshare с доменными шкалами.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `CBARQ.dat` |
| Строк | 12 061 |
| Размер | ~0.97 MB |
| Формат | `.dat` (табличный) |
| C-BARQ | Полностью (агрегированные шкалы) |
| Источник | [Figshare — C-BARQ survey on dog behavior and temperament](https://figshare.com/articles/dataset/C_BARQ_survey_on_dog_behavior_and_temperament/715896) |

## Ключевые поля

Доменные шкалы C-BARQ (lowercase):
- `strangeraggr`, `owneraggr`, `dogaggr`
- `trainability`, `excitability`
- и др.

## Релевантность для K3

- Крупный объём, готовые доменные шкалы — основной кандидат для train-set наряду с [2017-wolfram](2017-wolfram.md).
- Подходит для cross-source benchmark: train Figshare → test Wolfram (или наоборот).

## Заметки для harmonization

- Формат полей: lowercase (`strangeraggr`) vs PascalCase в Wolfram — нужен явный маппинг.
- 12 061 строк vs 12 060 в Wolfram — **подозрение на пересечение или общий происхождение**; проверить дедупликацию перед объединением.
- Загрузка через Figshare; S3-ссылки временные — для воспроизводимости фиксировать DOI/страницу ресурса.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [2017-wolfram](2017-wolfram.md)

---
type: dataset
tags: [c-barq, doodle, crossbreed, collected, k3, item-level]
sources: []
raw_file: analytics/research/datatsets/foreign/bryson_2026_doodle_crossbreed_behaviour_responses.xlsx
updated: 2026-08-12
status: draft
cbarq_coverage: full
rows: 9456
format: xlsx
---

# Bryson 2026 — поведение Doodle и других собак

Item-level C-BARQ dataset к статье Bryson et al. (2026) о поведении
дизайнерских помесей Doodle в сравнении с исходными породами и другими собаками.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `bryson_2026_doodle_crossbreed_behaviour_responses.xlsx` |
| Строк данных | ~9 456 |
| Формат | XLSX, item-level ответы C-BARQ |
| Публикация | Bryson et al. (2026), Doodle crossbreed behaviour |
| DOI статьи | [10.1371/journal.pone.0342847](https://doi.org/10.1371/journal.pone.0342847) |
| DOI данных | [10.6084/m9.figshare.31282123](https://doi.org/10.6084/m9.figshare.31282123) |

## Содержание

- Поведенческие пункты C-BARQ, включая обучаемость, агрессию, страх,
  поведение при разлуке и другие домены.
- Идентификатор записи `record_id` и признаки, необходимые для сравнения групп собак.
- Локального PDF статьи в репозитории пока нет; происхождение подтверждается DOI
  и метаданными workbook.

## Релевантность для Barko

- Крупный item-level источник для feature engineering и внешней проверки C-BARQ mapping.
- Выборка не ориентирована на собак из приютов, поэтому не подходит как прямой proxy
  постадопционной адаптации или возврата.
- Перед использованием нужно проверить лицензию, codebook, число уникальных собак,
  пропуски и возможные фильтры исходной статьи.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [cbarq-open-data-landscape](cbarq-open-data-landscape.md)
- [data-harmonization](../concepts/data-harmonization.md)

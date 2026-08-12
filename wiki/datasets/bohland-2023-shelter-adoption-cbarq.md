---
type: dataset
tags: [c-barq, shelter-dogs, adoption, longitudinal, collected, k3]
sources: [bohland-2023-shelter-dog-behavior-ru]
raw_file: analytics/research/datatsets/foreign/bohland_2023_shelter_behavior_after_adoption_supplement_s4.csv
updated: 2026-08-12
status: stable
cbarq_coverage: short
rows: 505
format: csv
---

# Bohland 2023 — поведение собак после пристройства

Supplementary S4 к статье Bohland et al. (2023): лонгитюдные ответы
C-BARQ и административные данные о собаках, пристроенных из пяти приютов Огайо.

## Метаданные

| Параметр | Значение |
|----------|----------|
| Файл | `bohland_2023_shelter_behavior_after_adoption_supplement_s4.csv` |
| Строк данных | 505 |
| Собаки | 99 |
| Волны | 7, 30, 90 и 180 дней после пристройства |
| C-BARQ | 42 пункта, 14 доменов |
| Публикация | [Bohland et al. (2023)](../sources/bohland-2023-shelter-dog-behavior-ru.md) |
| DOI | [10.1371/journal.pone.0289356](https://doi.org/10.1371/journal.pone.0289356) |

505 строк не означают 505 уникальных собак: export включает повторные волны,
consent и административные события для одних и тех же `Record ID`.

## Релевантность для Barko

- Наиболее близкий открытый источник к задаче мониторинга адаптации после пристройства.
- Позволяет моделировать динамику признаков, а не только однократный профиль собаки.
- Поддерживает точки наблюдения первой недели, 30, 90 и 180 дней.
- Для ML нужно сначала выделить строки с заполненным C-BARQ, привести волны к long schema
  и не допустить попадания одной собаки одновременно в train и test.

## Ограничения

- Только 99 собак и пять приютов в двух городах Огайо.
- Повторные измерения и служебные строки требуют явного ключа `dog × wave`.
- Наблюдательный дизайн не позволяет интерпретировать связи как причинные.

## Ссылки

- [collected-datasets-catalog](collected-datasets-catalog.md)
- [data-harmonization](../concepts/data-harmonization.md)
- [Саммари статьи](../sources/bohland-2023-shelter-dog-behavior-ru.md)

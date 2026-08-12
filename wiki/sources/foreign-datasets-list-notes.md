---
type: source
tags: [datasets, c-barq, source]
sources: []
raw_path: analytics/research/datatsets/foreign_datasets_list.md
updated: 2026-08-12
status: ingested
---

# Source: Foreign Datasets List

**Исходный файл:** [`analytics/research/datatsets/foreign_datasets_list.md`](../../analytics/research/datatsets/foreign_datasets_list.md)

## Ключевые выводы

1. Собрано **7 датасетов**: пять item/domain-level C-BARQ источников,
   один лонгитюдный post-adoption export и один частичный C-BARQ (ManyDogs).
2. Крупнейшие: Wolfram (12 060) и Figshare (12 061) — почти одинаковый объём, возможное пересечение.
3. Padova (807) и PLOS ONE (~435) — item-level ответы, нужна агрегация.
4. ManyDogs (705) — частичный C-BARQ + экспериментальные данные.
5. Bohland 2023 содержит повторные C-BARQ измерения после пристройства.
6. Bryson 2026 — крупный item-level dataset; локального PDF статьи пока нет.
7. Dog Aging Project — кандидат, ещё не собран.

## Интегрировано в вики

| Датасет | Страница |
|---------|----------|
| Сводный каталог | [collected-datasets-catalog](../datasets/collected-datasets-catalog.md) |
| ghirlanda_2013_cbarq_survey_domain_scales_wolfram.csv | [2017-wolfram](../datasets/2017-wolfram.md) |
| broseghini_2023_cbarq_italian_validation_responses.xlsx | [padova-cbarq-italian](../datasets/padova-cbarq-italian.md) |
| ghirlanda_2013_cbarq_survey_domain_scales_figshare.dat | [figshare-cbarq-dat](../datasets/figshare-cbarq-dat.md) |
| md1_data/ | [manydogs-md1](../datasets/manydogs-md1.md) |
| wilkins_2024_shortened_cbarq_validation_supplement_s1.csv | [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md) |
| bohland_2023_shelter_behavior_after_adoption_supplement_s4.csv | [bohland-2023-shelter-adoption-cbarq](../datasets/bohland-2023-shelter-adoption-cbarq.md) |
| bryson_2026_doodle_crossbreed_behaviour_responses.xlsx | [bryson-2026-doodle-crossbreed-behaviour](../datasets/bryson-2026-doodle-crossbreed-behaviour.md) |

## Обновлённые страницы

- [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md) — добавлен раздел собранных датасетов
- [data-harmonization](../concepts/data-harmonization.md) — таблица с wiki-ссылками
- [k3-risk-prediction](../components/k3-risk-prediction.md) — ссылка на каталог

## Не перенесено / требует уточнения

- [ ] Дедупликация Wolfram vs Figshare
- [ ] Полная схема столбцов `wilkins_2024_shortened_cbarq_validation_supplement_s1.csv`
- [ ] Проверка codebook и лицензии Bryson 2026
- [x] Расположение файлов зафиксировано: `analytics/research/datatsets/`

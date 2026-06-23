---
type: source
tags: [datasets, c-barq, source]
sources: []
raw_path: datatsets/foreign_datasets_list.md
updated: 2026-06-09
status: ingested
---

# Source: Foreign Datasets List

**Исходный файл:** [`datatsets/foreign_datasets_list.md`](../../datatsets/foreign_datasets_list.md)

## Ключевые выводы

1. Собрано **5 датасетов** (4 полных C-BARQ + 1 частичный).
2. Крупнейшие: Wolfram (12 060) и Figshare (12 061) — почти одинаковый объём, возможное пересечение.
3. Padova (807) и PLOS ONE (~435) — item-level ответы, нужна агрегация.
4. ManyDogs (705) — частичный C-BARQ + экспериментальные данные.
5. Dog Aging Project — кандидат, ещё не собран.

## Интегрировано в вики

| Датасет | Страница |
|---------|----------|
| Сводный каталог | [collected-datasets-catalog](../datasets/collected-datasets-catalog.md) |
| 2017_wolfram.csv | [2017-wolfram](../datasets/2017-wolfram.md) |
| Dataset_CBARQ.xlsx | [padova-cbarq-italian](../datasets/padova-cbarq-italian.md) |
| CBARQ.dat | [figshare-cbarq-dat](../datasets/figshare-cbarq-dat.md) |
| md1_data/ | [manydogs-md1](../datasets/manydogs-md1.md) |
| pone.0299973.s001.csv | [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md) |

## Обновлённые страницы

- [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md) — добавлен раздел собранных датасетов
- [data-harmonization](../concepts/data-harmonization.md) — таблица с wiki-ссылками
- [k3-risk-prediction](../components/k3-risk-prediction.md) — ссылка на каталог

## Не перенесено / требует уточнения

- [ ] Дедупликация Wolfram vs Figshare
- [ ] Полная схема столбцов `pone.0299973.s001.csv` (в источнике описание минимальное)
- [ ] Фактическое расположение файлов в репозитории (`datatsets/` vs `datasets/`)

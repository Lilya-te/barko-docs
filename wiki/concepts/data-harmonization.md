---
type: concept
tags: [c-barq, data, harmonization, k3]
sources: [ml-ideas-notes, data-ideas-notes, foreign-datasets-list-notes]
updated: 2026-06-09
status: draft
---

# Data Harmonization

Стратегия объединения фрагментарных C-BARQ подмножеств для baseline K3.

## Проблема

Полного открытого C-BARQ raw-датасета не существует. Доступные источники:
- разные форматы (CSV, XLSX, .dat);
- разные версии опросника (полная, сокращённая, итальянский перевод);
- разный уровень агрегации (сырые ответы vs доменные шкалы).

См. [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md).

## Подход для MVP

1. Собрать все доступные open subsets.
2. Определить общий feature schema (доменные шкалы C-BARQ).
3. Маппинг полей между датасетами.
4. Cross-source benchmark: train на одном источнике, test на другом.

## Источники для harmonization

### Собранные (готовы к работе)

| Датасет | Строк | Уровень | Wiki |
|---------|------:|---------|------|
| Wolfram | 12 060 | Доменные шкалы (PascalCase) | [2017-wolfram](../datasets/2017-wolfram.md) |
| Figshare | 12 061 | Доменные шкалы (lowercase) | [figshare-cbarq-dat](../datasets/figshare-cbarq-dat.md) |
| Padova | 807 | Item-level (IT) | [padova-cbarq-italian](../datasets/padova-cbarq-italian.md) |
| ManyDogs | 705 | Частичный cbarq_* | [manydogs-md1](../datasets/manydogs-md1.md) |
| PLOS ONE 2024 | ~435 | Item-level (short+full) | [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md) |

Сводка: [collected-datasets-catalog](../datasets/collected-datasets-catalog.md).

### Кандидаты (не собраны)

| Источник | Тип доступа | Wiki |
|----------|-------------|------|
| Dog Aging Project | Заявка / portal | [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md) |
| Morris Animal Foundation | Регистрация | [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md) |

## Маппинг полей (черновик)

| Домен C-BARQ | Wolfram | Figshare |
|--------------|---------|----------|
| Stranger-directed aggression | `StrangerDirectedAggression` | `strangeraggr` |
| Owner-directed aggression | — | `owneraggr` |
| Dog-directed aggression | — | `dogaggr` |
| Trainability | `Trainability` | `trainability` |
| Separation-related behavior | `SeparationRelatedBehavior` | — |
| Excitability | — | `excitability` |
| Energy level | `EnergyLevel` | — |

Полный маппинг — после EDA; Wolfram ↔ Figshare — приоритет #1.

## Открытые вопросы

- [ ] Дедупликация Wolfram ↔ Figshare (12 060 vs 12 061 строк).
- [ ] Агрегация Padova/PLOS item-level → доменные шкалы.
- [ ] Стратегия обработки пропусков и разных шкал.
- [ ] Формула таргета для K3 на harmonized данных.

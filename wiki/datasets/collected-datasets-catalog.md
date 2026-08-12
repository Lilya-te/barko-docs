---
type: dataset
tags: [c-barq, collected, catalog, k3]
sources: [foreign-datasets-list-notes]
updated: 2026-08-12
status: stable
---

# Collected Datasets Catalog

Сводка **собранных** датасетов для baseline K3. Источник: `analytics/research/datatsets/foreign_datasets_list.md`.

## Быстрый статус

| C-BARQ покрытие | Датасеты |
|-----------------|----------|
| **Полностью / item-level** | [2017-wolfram](2017-wolfram.md), [padova-cbarq-italian](padova-cbarq-italian.md), [figshare-cbarq-dat](figshare-cbarq-dat.md), [plos-one-2024-short-cbarq](plos-one-2024-short-cbarq.md), [bryson-2026-doodle-crossbreed-behaviour](bryson-2026-doodle-crossbreed-behaviour.md) |
| **Лонгитюдный C-BARQ(S)** | [bohland-2023-shelter-adoption-cbarq](bohland-2023-shelter-adoption-cbarq.md) |
| **Частично** | [manydogs-md1](manydogs-md1.md) |

**Суммарно строк (без дедупликации и без учёта повторных волн):** ~36 000;
это не число уникальных собак. Реальный объём после дедупа Wolfram/Figshare
и нормализации Bohland — TBD.

## Сравнительная таблица

| Датасет | Строк | Формат | C-BARQ | Уровень данных | Роль в baseline |
|---------|------:|--------|--------|----------------|-----------------|
| [2017-wolfram](2017-wolfram.md) | 12 060 | CSV | Полный | Доменные шкалы | Основной train |
| [figshare-cbarq-dat](figshare-cbarq-dat.md) | 12 061 | .dat | Полный | Доменные шкалы | Train / dedup check с Wolfram |
| [padova-cbarq-italian](padova-cbarq-italian.md) | 807 | XLSX | Полный | Item-level (IT) | Feature engineering, validation |
| [manydogs-md1](manydogs-md1.md) | 705 | CSV | Частичный | cbarq_* + эксперимент | Cross-source test |
| [plos-one-2024-short-cbarq](plos-one-2024-short-cbarq.md) | ~435 | CSV | Полный | Item-level (short+full) | Анкета MVP, validation |
| [bohland-2023-shelter-adoption-cbarq](bohland-2023-shelter-adoption-cbarq.md) | 505 | CSV | Short | Longitudinal export, 99 собак | Post-adoption dynamics |
| [bryson-2026-doodle-crossbreed-behaviour](bryson-2026-doodle-crossbreed-behaviour.md) | ~9 456 | XLSX | Полный | Item-level | Feature engineering, external validation |

## Кандидаты (ещё не собраны)

| Источник | Доступ | Страница |
|----------|--------|----------|
| [Dog Aging Project](https://dogagingproject.org/data-access) | Заявка | [cbarq-open-data-landscape](cbarq-open-data-landscape.md) |
| Morris Animal Foundation | Регистрация | [cbarq-open-data-landscape](cbarq-open-data-landscape.md) |
| UPenn C-BARQ | Сотрудничество | [c-barq](../concepts/c-barq.md) |

## Приоритеты для harmonization

1. **Проверить пересечение** Wolfram ↔ Figshare (12 060 vs 12 061).
2. **Определить общую schema** доменных шкал (PascalCase vs lowercase).
3. **Агрегировать** Padova и PLOS item-level → доменные шкалы.
4. **Извлечь** `cbarq_*` из ManyDogs, отбросить экспериментальные поля.
5. **Нормализовать** Bohland в `dog × wave`, сохраняя group split по собаке.
6. **Проверить** codebook и лицензию Bryson до включения в baseline.

См. [data-harmonization](../concepts/data-harmonization.md).

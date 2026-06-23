---
type: dataset
tags: [c-barq, datasets, open-data]
sources: [data-ideas-notes, foreign-datasets-list-notes]
updated: 2026-06-09
status: stable
---

# C-BARQ Open Data Landscape

Карта доступных C-BARQ данных для baseline K3.

## Главный вывод

**Полного открытого датасета C-BARQ (как Kaggle) не существует.** Доступ фрагментированный и контролируемый. Baseline строится на объединении подмножеств — см. [data-harmonization](../concepts/data-harmonization.md).

## Источники

### 1. UPenn C-BARQ Database (основная база)

| Параметр | Значение |
|----------|----------|
| Масштаб | ~50 000+ собак, 300+ пород |
| Доступ | Только через сотрудничество с исследователями |
| Open export | Нет |
| Ссылка | [vetapps.vet.upenn.edu/cbarq](https://vetapps.vet.upenn.edu/cbarq/about.cfm) |

### 2. Supplementary datasets в статьях

| Параметр | Значение |
|----------|----------|
| Пример | [Validation of shortened C-BARQ (PLOS ONE, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008875/) |
| Формат | CSV (supplementary data) |
| Объём | ~435 собак |
| Содержание | Сопоставление полной и короткой версии C-BARQ |
| Статус | Один из немногих реально открытых C-BARQ датасетов |

### 3. Dog Aging Project (DAP)

| Параметр | Значение |
|----------|----------|
| C-BARQ | Включён как часть опросов |
| Доступ | Заявка / open portal |
| Данные | Поведение, демография, здоровье (анонимизированы) |
| Статус | Лучший источник open-ish данных с C-BARQ |
| Ссылка | [dogagingproject.org/data-access](https://dogagingproject.org/data-access) |

### 4. Morris Animal Foundation Data Commons

| Параметр | Значение |
|----------|----------|
| Содержание | Сырые данные по годам, агрегаты, сравнение с C-BARQ |
| Доступ | Может требовать регистрацию |
| Статус | Частично открытая инфраструктура, не полный датасет |
| Ссылка | [Behavior Data Commons](https://datacommons.morrisanimalfoundation.org/behavior-data) |

## Паттерн в публикациях

В статьях с C-BARQ почти всегда:
- нет полного raw dataset;
- есть агрегаты или subset.

## Собранные датасеты (в репозитории)

См. полный каталог: [collected-datasets-catalog](collected-datasets-catalog.md).

| Датасет | Строк | C-BARQ | Страница |
|---------|------:|--------|----------|
| Wolfram C-BARQ Survey | 12 060 | Полный | [2017-wolfram](2017-wolfram.md) |
| Figshare C-BARQ | 12 061 | Полный | [figshare-cbarq-dat](figshare-cbarq-dat.md) |
| Padova (Italian) | 807 | Полный (item-level) | [padova-cbarq-italian](padova-cbarq-italian.md) |
| ManyDogs 1 | 705 | Частичный | [manydogs-md1](manydogs-md1.md) |
| PLOS ONE 2024 (short C-BARQ) | ~435 | Полный (item-level) | [plos-one-2024-short-cbarq](plos-one-2024-short-cbarq.md) |

## Следующий шаг

- Дедупликация Wolfram ↔ Figshare
- ~~Ingest PDF из `статьи/`~~ — сделано; см. [k3-feature-candidates](../concepts/k3-feature-candidates.md)
- Заявка на Dog Aging Project

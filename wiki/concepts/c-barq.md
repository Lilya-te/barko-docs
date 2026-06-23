---
type: concept
tags: [c-barq, behavior, questionnaire]
sources: [data-ideas-notes, ml-ideas-notes, plos-one-2024-short-cbarq-validation]
updated: 2026-06-09
status: stable
---

# C-BARQ

**Canine Behavioral Assessment & Research Questionnaire** — валидированный опросник поведения и темперамента собак.

## Основная база (UPenn)

- Сайт: [C-BARQ database overview](https://vetapps.vet.upenn.edu/cbarq/about.cfm)
- Масштаб: ~50 000+ собак, 300+ пород
- Тип: **research database, not open dataset**

### Ограничения доступа

- Нет публичной CSV-выгрузки
- Нет API
- Доступ через сотрудничество с исследователями (Serpell lab)
- Данные связаны с профилями владельцев → ограничения приватности

## Версии опросника

| Версия | Пунктов | Доменов | Примечание |
|--------|--------:|---------|------------|
| Long C-BARQ | 100 | 14 + misc | Стандарт Serpell/Hsu |
| **C-BARQ(S)** | 42 | 14 + misc | Short, <10 мин; валидирован PLOS ONE 2024 |

См. [plos-one-2024-short-cbarq-validation](../sources/plos-one-2024-short-cbarq-validation.md).

## 14 доменов (long / short)

Stranger-directed aggression/fear, owner-directed aggression, dog-directed aggression/fear, dog rivalry, **separation-related behavior**, attachment/attention-seeking, trainability, chasing, excitability, touch sensitivity, energy level.

## Релевантность для Barko

- MVP-анкета: кандидат **C-BARQ(S)** (42 пункта).
- Признаки K3: см. [k3-feature-candidates](k3-feature-candidates.md).
- Данные: [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md).

## Почему нет полного open dataset

1. **Приватность** — данные владельцев и условий содержания
2. **Лицензирование** — quasi-proprietary валидированный инструмент
3. **Научный контроль** — база используется в ongoing research

## Типичные модели доступа у исследователей

1. Прямой доступ через UPenn
2. Собственные локальные C-BARQ опросы
3. Вторичные открытые когорты (DAP, Morris Foundation, supplementary data в статьях)

См. также [data-harmonization](data-harmonization.md).

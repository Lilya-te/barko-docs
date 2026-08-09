---
type: concept
tags: [c-barq, behavior, questionnaire]
sources: [data-ideas-notes, ml-ideas-notes, duffy-2014-shelter-relinquishment-cbarq, plos-one-2024-short-cbarq-validation, gilchrist-2025-shelter-cbarq]
updated: 2026-08-09
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

| Версия | Пунктов | Доменов / факторов | Примечание |
|--------|--------:|--------------------|------------|
| Long C-BARQ | 100 | 14 + misc | Стандарт Serpell/Hsu |
| **C-BARQ(S)** | 42 | 14 + misc | Short для владельцев; shelter-intake Duffy 2014, short/full validation PLOS ONE 2024 |
| **Shelter C-BARQ** | 24 | **5 факторов** | Для staff в приюте; Gilchrist et al. 2025 |

См. [duffy-2014-shelter-relinquishment-cbarq](../sources/duffy-2014-shelter-relinquishment-cbarq.md), [plos-one-2024-short-cbarq-validation](../sources/plos-one-2024-short-cbarq-validation.md) и [gilchrist-2025-shelter-cbarq](../sources/gilchrist-2025-shelter-cbarq.md).

### C-BARQ(S) при передаче собаки в приют

Duffy et al. (2014) показали, что owner-report C-BARQ(S) согласуется с независимой staff assessment агрессии и различает исходы adoption/euthanasia. После множественной поправки наиболее устойчивым признаком была stranger-directed aggression. Согласованность с оценкой нового владельца через два месяца сохранилась только для stranger-directed aggression, inappropriate chewing и urination when left alone, поэтому intake-профиль нельзя считать неизменной характеристикой собаки.

### Shelter C-BARQ (5 факторов)

Fear, **Arousal** (конструкт без прямого аналога в long C-BARQ), Human Excitability, Dog Aggression, Human Aggression. Средняя α ≈ 0.78; N=445, 11 приютов.

## 14 доменов (long / short)

Stranger-directed aggression/fear, owner-directed aggression, dog-directed aggression/fear, dog rivalry, **separation-related behavior**, attachment/attention-seeking, trainability, chasing, excitability, touch sensitivity, energy level.

## Релевантность для Barko

- MVP-анкета **владельца:** кандидат **C-BARQ(S)** (42 пункта).
- MVP-анкета **приюта / research-ops:** кандидат **Shelter C-BARQ** (24 пункта).
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

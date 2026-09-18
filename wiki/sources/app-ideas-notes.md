---
type: source
tags: [app, research-ops, postgres, c-barq, schema]
sources: []
raw_path: _app_ideas/_database_architecture.md
updated: 2026-09-09
status: ingested
---

# Source: Архитектура БД research-ops приложения

**Исходный файл:** [`_app_ideas/_database_architecture.md`](../../_app_ideas/_database_architecture.md)

Связанные черновики UX (пока пустые): `_app_ideas/_volonteer_ux.md`, `_app_ideas/_expert_ux.md`, `_app_ideas/_admin_ux.md`.  
Продуктовый scope (роли, цель наполнения БД) ранее был в `_app_ideas/_main_ideas.md` (файл удалён; выводы сохранены ниже и на [research-data-app](../concepts/research-data-app.md)).

## Ключевые выводы из схемы

1. **PostgreSQL** — единый OLTP; сущности `shelters`, `shelter_memberships`, `dogs`, `placement_events`, `users`, `consents`, каталог анкет + `answer_events`.
2. Связь человек↔приют — через **`shelter_memberships`** (`employee` / `volunteer` / `director`), не через `owner_id` у shelter.
3. Жизненный цикл собаки — **`placement_events`** (`shelter_started` / `home_started` / `back_shelter` / `overexposure_started`) + денормализованный `dogs.status`; на карточке также `sex`, `neutered`, `assigned_volunteer_id`, `created_by_id`.
4. Анкеты: `questionnaires` (`slug`) → `questions` (`global_number`, `order_number`, `scale_id`) → `scales` (int / text / date); сессии `draft` / `finished` / `canceled`; ответы — append-only `answer_events` с `value_num` / `value_text` / `value_date`.
5. **`consents`** — type, version, accepted_at (152-ФЗ / согласие на ПД).

## Scope приложения (из прежнего `_main_ideas`)

1. Интерфейс ввода для **исследования**, не owner-facing продукт.
2. MVP-роли: **волонтёр** (собака + анкета частями/динамика) и **админ** (права, пользователи). **Эксперт** — позже.
3. Цель — наполнение БД до/параллельно с обучением моделей.

## Архитектурные уточнения

Зафиксированы на [research-data-app](../concepts/research-data-app.md):

- первоначальное решение Django заменено официальным Full Stack FastAPI Template; auth берём из шаблона;
- `is_superuser` используется для системного администратора, object-scope ролей — через `shelter_memberships` и FastAPI permission dependencies;
- в `answer_events` нужны `author_id` и запрет UPDATE/DELETE;
- в `questions` — `domain` (+ стабильный `item_id` / `global_number` как ключ C-BARQ);
- в сессиях — `wave` (0/7/14/30) для longitudinal;
- на `dogs` — `provenance` / `source`; `adopted_at` не заменяет `placement_events`;
- административные изменения должны попадать в audit events (через FastAdmin hooks либо отдельный механизм).

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Research-ops приложение + схема | [research-data-app](../concepts/research-data-app.md) |
| C-BARQ | [c-barq](../concepts/c-barq.md) |
| HelpDog placement-даты | [helpdog-forum-adoptions](../datasets/helpdog-forum-adoptions.md) |
| Harmonization | [data-harmonization](../concepts/data-harmonization.md) |
| Longitudinal метрики | [mvp-verifiable-metrics](../ml/mvp-verifiable-metrics.md) |

---
type: source
tags: [nir3, diary, sprint, research-ops, c-barq, pilot]
sources: []
raw_path: I — НИР 3/03 — Индивидуальные части/Hvostun_Tereshchenkova_Liliia/Индивидуальные артефакты за 3 семестр/_draft_dairy.md
updated: 2026-11-21
status: draft
---

# Source: Личный дневник НИР-3 (черновик)

**Исходный файл:** [`_draft_dairy.md`](<../../I — НИР 3/03 — Индивидуальные части/Hvostun_Tereshchenkova_Liliia/Индивидуальные артефакты за 3 семестр/_draft_dairy.md>)

Параллельный командный нарратив: [`Описание хода работ по проекту.md`](<../../I — НИР 3/03 — Индивидуальные части/Hvostun_Tereshchenkova_Liliia/Индивидуальные артефакты за 3 семестр/Описание хода работ по проекту.md>) — в wiki не дублируется целиком.

Ниже — только решения и факты, полезные продукту / методике / данным. Полный текст спринтов остаётся в raw.

## Ключевые решения (по спринтам)

| Период | Решение / результат | Куда в wiki |
|--------|---------------------|-------------|
| 01–14.08 | Кастдевы с волонтёрами; C-BARQ материалы респондентам; запрос данных UPenn/Serpell; архитектура LLM+RAG + RiskScore → план 7/30/90/180; черновик Яндекс.Форма + TG-бот с персональными ссылками | [k5-ai-chat](../components/k5-ai-chat.md), [k3-risk-prediction](../components/k3-risk-prediction.md), [research-data-app](../concepts/research-data-app.md) |
| 15–28.08 | Отказ от собственной анкеты → **C-BARQ** как инструмент с датасетами; анкета как настройка схемы, не жёсткая таблица; тема ВКРС и имя **Хвостун**; 152-ФЗ до массового сбора | [c-barq](../concepts/c-barq.md), [personal-data-152-fz](../concepts/personal-data-152-fz.md), [overview](../overview.md) |
| 29.08–11.09 | Домен `hvostun.com` / DNS / почта; UPenn одобрил передачу данных; уведомление оператора ПДн; 30 персональных ссылок (механика позже пересмотрена) | [personal-data-152-fz](../concepts/personal-data-152-fz.md) |
| 12–25.09 | Сбор через Яндекс.Формы в РФ без ожидания ответа РКН; отказ от персональных ссылок → контакты + ID + реестр; график 1 нед / 1 мес / 3 мес; старт экспертной админки; лицензионный черновик для RAG по книге | [research-data-app](../concepts/research-data-app.md), [consent-v1-pilot-form](../concepts/consent-v1-pilot-form.md), [k5-ai-chat](../components/k5-ai-chat.md) |
| 26.09–09.10 | Данные UPenn получены (>2 мес ожидания); скоринг Mini, **reverse q27–28**; экспертная админка + резервный хостинг; 152-ФЗ в анкете Полины; договорённость с «Домом хвостиков» (листовки + донаты за 1-е и 3-е заполнение) | [c-barq-short-42-scoring](../concepts/c-barq-short-42-scoring.md), [consent-v1-pilot-form](../concepts/consent-v1-pilot-form.md) |
| 10–23.10 | Полевой рекрутинг (Юна-Фест); экспертная разметка «ответы → рекомендации»; сайт на своей инфре (`hvostun.com`, `/research`, `/ppd`); пакет уведомления оператора ПДн; Active Learning | [research-data-app](../concepts/research-data-app.md), [nir3-hypotheses](nir3-hypotheses.md) |
| 24.10–06.11 | Выставка «Надо брать»; EDA Bohland/Powell; эксперты (по 5 анкет, ≥90% заполненности); таргет = рекомендации; демо МИСИС; типовые вопросы комиссии (метрики, пороги, контроль, цели vs результат) | [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md), [nir3-ml-evaluation-pipeline](nir3-ml-evaluation-pipeline.md), [app-effect-rct-power](../ml/app-effect-rct-power.md) |

## Лонгитюд пилота (из дневника)

Волны заполнения, которые уже коммуницируют владельцам: **1 неделя / 1 месяц / 3 месяца** (три заполнения). Это согласуется с точками C-BARQ post-adoption и с дизайном сравнения групп в [app-effect-rct-power](../ml/app-effect-rct-power.md) (7→30 день как ближайший измеримый горизонт).

## 152-ФЗ (факты из дневника)

- Согласие и политика до массового сбора; форма сначала только для ограниченного теста.
- Уведомление оператора: УЗ-4, угрозы 3 типа; Яндекс.Формы + PostgreSQL в РФ; TLS, бэкапы, журналы, отзыв/удаление; разделение ops и ML.
- Подробный чеклист: [personal-data-152-fz](../concepts/personal-data-152-fz.md).

## Не перенесено

- Пустые шаблонные блоки спринтов (цель / самооценка без текста).
- Полные цитаты чатов и поимённые кастдев-расшифровки — в raw и в «Описание хода работ».
- Операционные детали хостинга/DNS сверх факта «своя инфра + РФ-контур».

## Связанные страницы

- [nir3-hypotheses](nir3-hypotheses.md), [nir3-ml-evaluation-pipeline](nir3-ml-evaluation-pipeline.md), [nir3-literature-delta](nir3-literature-delta.md)
- [experiment-plan](../ml/experiment-plan.md)

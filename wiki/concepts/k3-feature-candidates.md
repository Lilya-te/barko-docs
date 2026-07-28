---
type: concept
tags: [k3, features, c-barq, synthesis]
sources: [plos-one-2024-short-cbarq-validation, fomina-2024-problem-behavior-review, fomina-2025-ai-pilot-study, gritsenko-2023-owner-frustration, gilchrist-2025-shelter-cbarq]
updated: 2026-07-24
status: draft
---

# K3 Feature Candidates

Синтез признаков для прогноза адаптационных трудностей из ingest статей `статьи/`.

## C-BARQ домены (приоритет)

На основании PLOS ONE 2024 (валидность short↔full) и пилота Фоминой 2025:

| Приоритет | Признак / домен | Обоснование |
|-----------|-----------------|-------------|
| **Высокий** | Stranger-directed fear | r=0.81 short↔full; коморбидность со страхом (обзор 2024) |
| **Высокий** | Stranger-directed aggression | r=0.77; фактор разочарованности (Гриценко) |
| **Высокий** | Separation-related behavior | r=0.68; separation anxiety в обзоре; «Разлука» в CBARQ |
| **Высокий** | Nonsocial fear | r=0.74; социальная боязнь |
| **Средний** | Dog-directed aggression | r=0.75 |
| **Средний** | Excitability / Возбудимость | r=0.57; различает группы в пилоте (p=0.01) |
| **Средний** | Attachment / attention-seeking | r=0.65; тип привязанности (обзор 2024) |
| **Средний** | Trainability | r=0.68; обратная шкала |
| **Средний** | Chasing, touch sensitivity, energy | r=0.69–0.79 |
| **Низкий** | Owner-directed aggression | r=0.52; много нулей в данных |

## Shelter C-BARQ факторы (Gilchrist 2025)

Для **приютного** сбора (staff/волонтёр), не как замена owner C-BARQ(S):

| Приоритет | Фактор | Обоснование |
|-----------|--------|-------------|
| **Высокий** | Fear | α=0.85; сильная связь с Human Aggression (r=0.71); IRT точен на высоких уровнях |
| **Высокий** | Human Aggression | α=0.74; safety / placement; крайние уровни → риск возврата (авторы) |
| **Высокий** | Dog Aggression | α=0.72; коррелирует с Human Aggression (0.57) и Arousal (0.55) |
| **Средний** | Human Excitability | α=0.87; аналог excitability в long/short |
| **Средний** | **Arousal** | новый для shelter; нет прямого аналога в 14 доменах; связан с cortisol/overstimulation |

См. [gilchrist-2025-shelter-cbarq](../sources/gilchrist-2025-shelter-cbarq.md).

## Не-C-BARQ факторы (контекст)

| Фактор | Источник | Роль |
|--------|----------|------|
| Тип привязанности владелец–собака | [fomina-2024](sources/fomina-2024-problem-behavior-review.md) | Контекст, возможно не в MVP |
| Ранняя социализация | fomina-2024 | Анкета Barko / будущие features |
| Нейротизм владельца | fomina-2024 | K5 / рекомендации, не K3 baseline |
| Возврат в приют | [adoption-return](adoption-return.md) | Таргет, не признак |

## MVP-анкета

- **Владелец:** **C-BARQ(S)** — 42 пункта, валидирован (PLOS ONE 2024); [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md).
- **Приют / research-ops:** **Shelter C-BARQ** — 24 пункта, 5 факторов (Gilchrist 2025).

## Следующий шаг

- EDA на Wolfram/Figshare: корреляция доменов с proxy-таргетом.
- Сопоставить русские шкалы CBARQ (Фомина) с 14 доменами C-BARQ.
- Решить, нужна ли Shelter C-BARQ в схеме анкет [research-data-app](research-data-app.md).

См. [k3-risk-prediction](../components/k3-risk-prediction.md).

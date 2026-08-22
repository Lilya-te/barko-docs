---
type: source
tags: [personality, demographics, questionnaire, online-survey, source, translation-available]
sources: []
raw_path: статьи/foreign/hungary/Kubinyi_2009_SURVEY_dog_owner_demographics_personality.pdf
updated: 2026-08-22
status: ingested
doi: 10.1016/j.beproc.2009.04.004
---

# Source: Демография владельца/собаки и personality traits (Kubinyi et al. 2009)

**Оригинал:** [`статьи/foreign/hungary/Kubinyi_2009_SURVEY_dog_owner_demographics_personality.pdf`](../../статьи/foreign/hungary/Kubinyi_2009_SURVEY_dog_owner_demographics_personality.pdf)

Kubinyi, E., Turcsán, B., & Miklósi, Á. (2009). Dog and owner demographic characteristics and dog personality trait associations. *Behavioural Processes, 81*(3), 392–401. https://doi.org/10.1016/j.beproc.2009.04.004

## Саммари

### Суть

Крупнейший на момент публикации **онлайн-опрос** (немецкоязычные владельцы): связь **4 personality traits** собаки с **14 demographic variables** (dog + owner). Методы: GLM + **regression trees (CHAID)** для нелинейных паттернов.

### Данные

| Параметр | Значение |
|----------|----------|
| Исходная выборка | **14 004** собак |
| После исключения <1 года | **10 519** |
| Породы | 267 (+ 3920 mixed-breed) |
| Рекрутинг | журнал *Dogs* + `dogs-magazin.de`; анкета доступна с конца Aug 2007 до начала Jan 2008 (28 Aug 2007 – 8 Jan 2008) |
| Personality instrument | 24 пункта (адаптация Human Personality Inventory / Big Five для собак) → **4 фактора** (17/24 пунктов; 58% дисперсии) |
| Test–retest | n=42, α 0.83–0.88 по факторам |

**Факторы:** calmness (5 items, α=0.85), trainability (5, 0.71), dog sociability (4, 0.75), boldness (3, 0.65).

Дополнительно: средний возраст собак в «взрослой» выборке \(4.2 \pm 3.1\) года; 56.1% — ♂; 43.1% — neutered (39% ♂ и 48% ♀).

### Ключевые результаты (regression trees)

| Trait | Главные предикторы | Extreme groups |
|-------|-------------------|----------------|
| **Calmness** | age, neutering, training, age at acquisition | Наименее calm: <2.5 лет, neutered, позднее приобретение; наиболее calm: >6.9 лет, раннее приобретение |
| **Trainability** | training experience, age, purpose | Наименее trainable: 0 training, >3 лет; наиболее: ≥3 типов professional training |
| **Dog sociability** | age, time with owner, sex | Наименее sociable: >4.8 лет, <3 h/day с owner; наиболее: <1.5 лет; ♀ > ♂ к conspecifics |
| **Boldness** | sex, age at acquisition, age | Наименее bold: ♀, bred by owner или acquired >1 year; наиболее bold: ♂, <12 weeks, <2 years |

Owner variables (gender, education, household size и др.) — **minor but detectable** effects в GLM; associations **не causal** (owner-report).

### Ограничения

- Self-selected подвыборка вовлечённых немецкоязычных владельцев (читатели DOGS/пользователи сайта); не обязательно representative для общей популяции владельцев.
- Данные — owner-report: ассоциации не тождественны причинности; возможны confounding и reverse causality (например, обучение может быть и причиной, и следствием поведения).
- Boldness — самая слабая по внутренней согласованности субшкала (α=0.65); авторам прямо указывают на желательность расширения набора пунктов.
- Исключены щенки <1 года (26.8% исходной базы) → ограничена интерпретация о раннем развитии/социализации; при этом возраст приобретения (до 12 недель) всё равно оказался значимым предиктором для всех четырёх traits.

### Релевантность для Barko

- **K3:** age, neutering, age at acquisition, training exposure — кандидаты **owner/dog covariates** при harmonization с C-BARQ; осторожность с causal claims (confounding, reverse causality для training).
- **K5:** evidence base для объяснений «почему молодая кастрированная собака кажется менее calm»; онлайн-questionnaires at scale — методологический преcedent для pilot/research ops (с учётом 152-ФЗ для РФ).

## Полный перевод

[Открыть полный русский перевод](../../статьи/foreign/translations/kubinyi_2009_survey_dog_owner_demographics_personality_ru.md).

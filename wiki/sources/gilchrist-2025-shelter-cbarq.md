---
type: source
tags: [c-barq, shelter, source, psychometric, factor-analysis, translation-available]
sources: []
raw_path: статьи/foreign/usa/Gilchrist_2025_CBARQ_cbarq_for_shelter_dogs.pdf
updated: 2026-07-29
status: ingested
doi: 10.26451/abc.12.01.04.2025
---

# Source: Shelter C-BARQ — пять факторов (Gilchrist et al. 2025)

**Исходный файл:** [`статьи/foreign/usa/Gilchrist_2025_CBARQ_cbarq_for_shelter_dogs.pdf`](../../статьи/foreign/usa/Gilchrist_2025_CBARQ_cbarq_for_shelter_dogs.pdf)

Gilchrist, R. J., Gardner, M. J., Manapat, P. D., Gunter, L. M., Feuerbacher, E. N., Edwards, M. C., & Wynne, C. D. L. (2025). Tailoring the C-BARQ to shelter dogs: Identification of five reliable factors. *Animal Behavior and Cognition, 12*(1), 69–107. https://doi.org/10.26451/abc.12.01.04.2025. CC BY 3.0.

## Саммари

### Данные
Обезличенные анкеты (445 строк ответов) не опубликованы открыто — только по запросу авторам. Контакт: rgilchri@asu.edu (Rachel J. Gilchrist).

### Суть

Первая психометрическая валидация **адаптированного C-BARQ для собак в приюте** (не у владельца дома и не на сдаче в приют). Из 100-item C-BARQ эксперты отобрали 37 пунктов, применимых и в приюте, и дома; EFA/CFA/IRT сократили до **Shelter C-BARQ: 24 пункта, 5 факторов**.

### Ключевые цифры

| Параметр | Значение |
|----------|----------|
| Выборка | **445** собак, **11** приютов (США) |
| Респонденты | staff / volunteers / researchers — кто лучше знает собаку |
| Split | EFA n=222, CFA validation n=223, final CFA N=445 |
| Итоговая шкала | **24 items → 5 factors** |
| Средняя надёжность (α) | **~0.78** (все факторы ≥ 0.70) |
| Fit (full sample) | RMSEA=0.04, CFI=0.97, TLI=0.97, SRMR=0.10 |
| Median factor loading | **0.84** (диапазон 0.45–0.95) |

### Пять факторов Shelter C-BARQ

| Фактор | Пунктов | α / ω | Содержание (кратко) |
|--------|--------:|-------|---------------------|
| **Fear** | 7 | 0.85 / 0.92 | страх к незнакомцам, шуму, объектам, собакам, входу в вольер |
| **Arousal** | 6 | 0.74 / 0.85 | отвлекаемость, вой при уходе, погоня, жевание, тяга поводка, побег |
| **Human Excitability** | 4 | 0.87 / 0.89 | возбудимость при возвращении людей, игре, прогулке, визитах |
| **Dog Aggression** | 4 | 0.72 / 0.78 | агрессия к незнакомым собакам (+ слабый item про отбор игрушек) |
| **Human Aggression** | 3 | 0.74 / 0.74 | агрессия к людям на поводке / в вольере / к знакомым |

### Корреляции факторов (значимые)

| Пара | r |
|------|--:|
| Fear ↔ Human Aggression | **0.71** |
| Arousal ↔ Human Excitability | **0.65** |
| Dog Aggression ↔ Human Aggression | 0.57 |
| Arousal ↔ Dog Aggression | 0.55 |
| Fear ↔ Dog Aggression | 0.31 |
| Excitability ↔ Human Aggression | ≈0 (н.з.) |

### Отличие от C-BARQ(S)

| | **C-BARQ(S)** (Duffy et al. 2014) | **Shelter C-BARQ** (эта статья) |
|--|-----------------------------------|----------------------------------|
| Контекст | владелец при сдаче / после адопции | собака **живёт в приюте** |
| Пунктов | 42 | **24** |
| Цель | intake / прогноз исходов | оценка поведения **в приюте** |
| Фактор Arousal | нет | **есть** — авторы считают уникальным для shelter |

Многие пункты C-BARQ(S) описывают домашние сценарии, недоступные наблюдателю в приюте.

### Метод (кратко)

1. Эксперты (LG, EF) оставили 37 пунктов, отвечаемых и в shelter, и дома.
2. Убрали 7 пунктов из‑за полихорических корреляций ≥0.90 и 5 — из‑за floor effects.
3. EFA + parallel analysis → 4–6 факторов; выбран 5-factor model.
4. CFA на validation + full sample; IRT (graded response model) по факторам.

### Практические правила авторов

- Не менять формулировки / не выборочно тасовать пункты без новой валидации.
- Можно использовать **отдельные** шкалы (1–5 факторов), но **не** суммировать в один «total score».
- Sub-score = сумма пунктов фактора; NA допустим, если поведение не наблюдалось.
- IRT: Fear и Human Aggression точнее на **высоких** уровнях черты; Arousal — ближе к средним.

### Ограничения

- Split-sample ~200 на половину (меньше рекомендованных 300 для стабильных оценок).
- Floor effects: многие ответы «never» / «no reaction» (собаки уже кандидаты на foster/adoption).
- Нет inter-rater reliability (один оценщик на собаку — как в реальном приюте).
- Нет criterion validity с внешними мерами / пост-адопционным поведением.
- Данные по запросу, не open CSV.

### Релевантность для Barko

- **Приютный контур** ([research-data-app](../concepts/research-data-app.md)): компактная 24-item анкета для staff/волонтёров вместо полной C-BARQ / C-BARQ(S).
- **K3:** Fear, Human/Dog Aggression, Excitability согласуются с [k3-feature-candidates](../concepts/k3-feature-candidates.md); **Arousal** — новый кандидат-конструкт для shelter-контекста.
- **Таргет / matchmaking:** авторы связывают крайние уровни черт с возвратами и mismatch ожиданий — см. [adoption-return](../concepts/adoption-return.md).
- **Не замена** домашней C-BARQ(S) для владельца после адопции: другая популяция респондентов и среда.

### Противоречия / уточнения к вики

- В [c-barq](../concepts/c-barq.md) до сих пор фигурировали только Long (100) и C-BARQ(S) (42). Добавлен третий валидированный вариант — **Shelter C-BARQ (24)**.
- C-BARQ(S) остаётся кандидатом для **owner**-анкеты; Shelter C-BARQ — для **приютного** сбора.

### Интегрировано в вики

- [c-barq](../concepts/c-barq.md)
- [k3-feature-candidates](../concepts/k3-feature-candidates.md)
- [adoption-return](../concepts/adoption-return.md)

## Полный перевод

[Открыть полный русский перевод](../../статьи/foreign/translations/gilchrist_2025_cbarq_for_shelter_dogs_ru.md). Перевод вынесен из wiki, чтобы curated-слой оставался компактным.

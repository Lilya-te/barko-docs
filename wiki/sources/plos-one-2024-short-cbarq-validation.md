---
type: source
tags: [c-barq, source, plos-one, short-cbarq]
sources: []
raw_path: статьи/journal.pone.0299973.pdf
updated: 2026-06-09
status: ingested
doi: 10.1371/journal.pone.0299973
---

# Source: Validation of shortened C-BARQ (PLOS ONE 2024)

**Исходный файл:** [`статьи/journal.pone.0299973.pdf`](../../статьи/journal.pone.0299973.pdf)

Wilkins V. et al. (2024). PLOS ONE 19(4): e0299973. Dog Aging Project cohort.

## Суть

Валидация **C-BARQ(S)** — сокращённой версии (42 пункта из 100) — через сравнение с полной C-BARQ у одних и тех же 435 пар владелец–собака (DAP, 2020).

## Ключевые цифры

| Параметр | Значение |
|----------|----------|
| Участники | 435 собак (средний возраст 7.3 года, 50% сук) |
| Response rate | 58.1% (435 из 749 приглашённых) |
| Kappa (item-level) | fair–moderate (0.23–0.58) |
| Pearson r (domain means) | **>0.60 для 12 из 14 доменов** + miscellaneous |

## Домены с сильной корреляцией (r)

| Домен | Pearson r |
|-------|----------:|
| Stranger-directed fear | 0.81 |
| Stranger-directed aggression | 0.77 |
| Nonsocial fear | 0.74 |
| Chasing | 0.79 |
| Dog-directed aggression | 0.75 |
| Energy level | 0.74 |
| Separation-related behavior | **0.68** |
| Trainability | 0.68 |
| Touch sensitivity | 0.69 |
| Attachment/attention-seeking | 0.65 |
| Excitability | 0.57 |
| Owner-directed aggression | 0.52 |

## Выводы для Barko

- **C-BARQ(S) валиден** как замена полной версии для скрининга — релевантно для MVP-анкеты Barko.
- **Separation-related behavior** — подтверждённый домен для short/full mapping; кандидат признака K3.
- Supplementary CSV (`pone.0299973.s001.csv`) — open dataset, см. [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md).
- Ограничение: выборка DAP (self-selected), лето 2020 (COVID lockdowns).

## Интегрировано в вики

- [c-barq](../concepts/c-barq.md)
- [plos-one-2024-short-cbarq](../datasets/plos-one-2024-short-cbarq.md)
- [k3-feature-candidates](../concepts/k3-feature-candidates.md)

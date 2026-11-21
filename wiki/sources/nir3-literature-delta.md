---
type: source
tags: [nir3, literature, c-barq, pilot, delta, metrics, nlp]
sources: []
raw_path: NIR_3/personal_files/Б1_теоретический_анализ_источников.md
updated: 2026-11-16
status: ingested
---

# Source: Теоретический анализ источников (НИР-3, Б1)

**Исходный файл:** [`NIR_3/personal_files/Б1_теоретический_анализ_источников.md`](../../NIR_3/personal_files/Б1_теоретический_анализ_источников.md)

Саммари статей — отдельные страницы в [wiki/sources/](../index.md). Здесь — выводы Б1 для продукта и методики.

## Ключевые выводы

### Литература (приоритет)

Порядок в Б1: опорные для Hvostun (Wilkins Mini → Bohland → Duffy/Serpell → Gilchrist → Powell ×2 → Gates/Vitulová/Hoth-Zimak) → РФ (Фомина, Гриценко) → доп. шкалы (LIEBI, DMA, MCPQ, Lincoln, lab).

### Инструменты

Альтернативы (Campbell, РКФ Т1/Т2, DPQ, MCPQ-R, VIDOPET, Lincoln DIAS/CFQ/PANAS/LCAS/LSSS, Dog-ADHD, CADES/CCDR/CCAS) в основном **без** валидированного RU и **без** сопоставимого open data под post-adoption. Выбор пилота — **C-BARQ** (Mini/Shelter/full): есть рабочий RU и датасеты.

### C-BARQ данные (числа из Б1 / unified)

| Контур | Строк (заполнений) | Собаки | Доступ |
|--------|-------------------:|-------:|--------|
| Ландшафт «открытых» C-BARQ (каталог, до дедупа) | ~36 000 | ≠ уник. собак | Wolfram≈Figshare + Bryson + Padova + … |
| UPenn база | — | ~50 000+ | по запросу / сотрудничеству |
| Bohland в unified | 337 | 104 | открытый supplement |
| Serpell/Powell вложения | 619 | 562 | получены по запросу |
| **Unified mini итого** | **956** | — | Bohland + Serpell |

*Примечание:* в сыром S4 Bohland wiki раньше указывала 505 строк / 99 собак (с служебными событиями); в unified после фильтра анкет — 337 / 104.

### Инновационная дельта

1. Первое лонгитюдное исследование адаптации на российских владельцах.
2. Статистическое сравнение с данными США → [H₁-transfer](nir3-hypotheses.md).

### Методика ML (разделы Б1 → вики)

| Тема Б1 | Суть | Куда интегрировано |
|---------|------|-------------------|
| Multilabel-метрики | primary = example-F1; random $E[F1]=k/N=0.125$; Hamming/subset accuracy не sole | [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) |
| Rule-based матрица | $14\times 40 = 560$ порогов; sparse ~40–80 | [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md) |
| LR vs DT | LR — первая линия; DT — нелинейность с контролем глубины | [model-selection](../ml/model-selection.md) |
| Текст → анкета | embeddings+cosine → NLI/LLM → slot-filling диалог; confirm обязателен | [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md) |

## Не перенесено

- Полная таблица 26 статей (уже в `wiki/sources/*`).
- Повреждённые/укороченные ячейки таблицы альтернативных инструментов в Б1 (часть колонок «открытые данные» съехала) — опираться на вывод про C-BARQ, не на каждую ячейку до правки Б1.
- `dairy.md`, ход работ — нарратив.

## Интегрировано

| Тема | Страница |
|------|----------|
| Overview (дельта) | [overview](../overview.md) |
| Гипотезы | [nir3-hypotheses](nir3-hypotheses.md) |
| Unified mini | [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md) |
| Open landscape | [cbarq-open-data-landscape](../datasets/cbarq-open-data-landscape.md), [collected-datasets-catalog](../datasets/collected-datasets-catalog.md) |

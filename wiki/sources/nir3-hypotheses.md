---
type: source
tags: [nir3, hypotheses, k3, k5, c-barq, recommendations]
sources: []
raw_path: NIR_3/personal_files/Б2_гипотезы.md
updated: 2026-11-15
status: ingested
---

# Source: Личные исследовательские гипотезы НИР-3

**Исходный файл:** [`NIR_3/personal_files/Б2_гипотезы.md`](../../NIR_3/personal_files/Б2_гипотезы.md)

Связанная методика проверки: [nir3-ml-evaluation-pipeline](nir3-ml-evaluation-pipeline.md), синтез [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md).

## Ключевые выводы

Шесть опровержимых гипотез с численными порогами. Таргет рекомендательного контура — top-5 из каталога (N ≈ 40), эталон G — экспертная разметка; волна 7–14 дней.

| ID | Суть | H₀ / порог |
|----|------|------------|
| **H₁-baseline** | Rule-based «домен + порог T → каталог» | macro-F1 < 0,6 (random F1 = 0,125 при \|P\|=\|G\|=5, N=40) |
| **H₁-plan** | ML (в Б2: дерево решений) vs rule-based на том же val | macro-F1_ML ≤ macro-F1_baseline |
| **H₁-quality** | Кинолог: принять / править / отклонить + «безопасна» | accept < 95% или safe < 99% |
| **H₁-transfer** | Домены C-BARQ(S) пилота РФ ≈ референс (Bohland / short) | TOST: хотя бы один домен \|\Δ\| ≥ δ |
| **H₁-channel** | NLP-заполнение пунктов из текста чата ≈ self-report | TOST по доменам, α = 0,05 |
| **H₁-human-eval** | Pairwise A/B: K5-RAG vs ответ без RAG | preference ≤ 50% или < 70% |

### Метрика рекомендаций (H₁-baseline / H₁-plan)

На анкету \(i\): \(TP_i = |P_i \cap G_i|\), \(\mathrm{F1}_i = TP_i/5\); **macro-F1** — среднее по val. При \|P\|=\|G\|=5 это доля верных из пяти.

### Метрика качества эксперта (H₁-quality)

\(P_{\text{accept}} = N_{\text{принять}} / N_{\text{всего рекомендаций}}\); «править» и «отклонить» не считаются accept.

### TOST (H₁-transfer, H₁-channel)

Эквивалентность не доказывается тестом на *различие* с p > 0,05; нужны оба односторонних TOST и заранее заданный δ.

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Пайплайн оценки | [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md) |
| План эксперимента | [experiment-plan](../ml/experiment-plan.md) |
| Метрики | [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) |
| NLP-канал | [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md) |

## Противоречия / уточнения

- В Б2 для H₁-plan указано **дерево решений**; в методике Б3 кандидаты — **LogisticRegression** и **RandomForest**. В вики зафиксированы оба: дерево как формулировка гипотезы, LR/RF как экспериментальные кандидаты.
- Исторический K3 в wiki — риск / ROC-AUC; НИР-3 смещает измеримый ML-таргет на **рекомендации каталога** (macro-F1). Risk-скоринг не отменён, но не является критерием этих шести H₁.

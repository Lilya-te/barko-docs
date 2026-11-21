---
type: source
tags: [nir3, hypotheses, k3, k5, c-barq, recommendations]
sources: []
raw_path: NIR_3/personal_files/Б2_гипотезы.md
updated: 2026-11-19
status: ingested
---

# Source: Личные исследовательские гипотезы НИР-3

**Исходный файл:** [`NIR_3/personal_files/Б2_гипотезы.md`](../../NIR_3/personal_files/Б2_гипотезы.md)

Связанная методика проверки: [nir3-ml-evaluation-pipeline](nir3-ml-evaluation-pipeline.md), синтез [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md).

**Синхронизация:** при изменении порогов/H₁ править Б2 **и** Б3 (+ wiki); правило `.cursor/rules/nir3-hypotheses-pipeline-sync.mdc`.

## Ключевые выводы

Семь опровержимых гипотез с численными порогами (H₁-plan разделён на DT и LR OvR). Таргет рекомендательного контура — top-5 из каталога (N = 40), эталон G — экспертная разметка; волна 7–14 дней.

| ID | Суть | H₀ / порог |
|----|------|------------|
| **H₁-baseline** | Rule-based «домен + порог T → каталог» | `macro-F1 < 0.6` (random F1 = 0.125 при k=5, N=40) |
| **H₁-plan-DT** | DecisionTree vs rule-based на том же val | `Δ_DT < 0.10` |
| **H₁-plan-LR** | LogisticRegression one-vs-rest vs rule-based | `Δ_LR < 0.10`; в quality — max(Δ) |
| **H₁-quality** | Кинолог: принять / править / отклонить + «безопасна» | accept < 60% или safe < 97% (цель ~60–70% / ~97–98%) |
| **H₁-transfer** | Домены C-BARQ(S) пилота РФ ≈ референс (Bohland / short) | TOST: хотя бы один домен \|Δ\| ≥ δ |
| **H₁-channel** | NLP-заполнение пунктов из текста чата ≈ self-report | TOST по доменам, α = 0.05 |
| **H₁-human-eval** | Pairwise A/B: K5-RAG vs ответ без RAG | preference ≤ 50% или < 70% |

### Метрика рекомендаций (H₁-baseline / H₁-plan-*)

На анкету i:

$$
TP_i = \lvert P_i \cap G_i \rvert,\quad \mathrm{F1}_i = \frac{TP_i}{5},\quad \text{macro-F1} = \mathrm{mean}_i(\mathrm{F1}_i)
$$

При card(P)=card(G)=5 это доля верных из пяти. δ = 0.10 ≈ +0.5 верной рекомендации из 5.

### Метрика качества эксперта (H₁-quality)

$$
P_{\mathrm{accept}} = \frac{N_{\mathrm{принять}}}{N_{\mathrm{всего\ рекомендаций}}}
$$

«править» и «отклонить» не считаются accept.

### TOST (H₁-transfer, H₁-channel)

Эквивалентность не доказывается тестом на *различие* с p > 0.05; нужны оба односторонних TOST и заранее заданный δ.

**H₁-channel (уточнено 2026-11-19):** парный TOST по **каждому** ключевому домену (intersection–union), эквивалентно $\mathrm{CI}_{90\%}(\Delta_d) \subset (-\delta, +\delta)$. δ фиксируется до сбора: приоритет — test-retest формы, иначе 0.3–0.5 · SD домена. Размер выборки $n \approx 8.6\,(\sigma_D/\delta)^2$ (≈35 пар при δ = 0.5σ_D). Вторично: ICC(2,1) ≥ 0.75, Bland–Altman, weighted κ по пунктам, coverage ≥ 80%. Подробно — Б3 §5.3, [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md).

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Пайплайн оценки | [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md) |
| План эксперимента | [experiment-plan](../ml/experiment-plan.md) |
| Метрики | [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) |
| NLP-канал | [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md) |

## Противоречия / уточнения

- Ранее: Б2 только дерево, Б3 — LR/RF. **Снято:** канон = H₁-plan-DT + H₁-plan-LR (OvR); RF — опция при росте n, не отдельная H₁.
- Исторический K3 в wiki — риск / ROC-AUC; НИР-3 смещает измеримый ML-таргет на **рекомендации каталога** (macro-F1). Risk-скоринг не отменён, но не является критерием этих H₁.

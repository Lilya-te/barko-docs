---
type: ml
tags: [nir3, pipeline, hypotheses, recommendations, nlp, rag, evaluation]
sources: [nir3-hypotheses, nir3-ml-evaluation-pipeline]
updated: 2026-11-19
status: draft
---

# Пайплайн проверки гипотез НИР-3

Методика оценки ML-контуров Hvostun по личным гипотезам семестра. Источники: [nir3-hypotheses](../sources/nir3-hypotheses.md), [nir3-ml-evaluation-pipeline](../sources/nir3-ml-evaluation-pipeline.md).

**Синхронизация:** канон — `I — НИР 3/03 — Индивидуальные части/Hvostun_Tereshchenkova_Liliia/Индивидуальные артефакты за 3 семестр/Б2_личные_исследовательские_гипотезы.md` + `Б3_…пайплайн…md`; при правках порогов/H₁ обновлять оба и эту страницу (правило `.cursor/rules/nir3-hypotheses-pipeline-sync.mdc`).

Связано: [experiment-plan](experiment-plan.md), [benchmarks-and-metrics](benchmarks-and-metrics.md), [model-selection](model-selection.md), [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md), [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md).

## Объект и split

| Элемент | Фиксация |
|---------|----------|
| Объект | анкета 7–14 дней (C-BARQ Mini / C-BARQ(S)) + профиль собаки |
| Таргет | top-5 из каталога (N = 40); эталон G — экспертная разметка |
| Каналы | Яндекс.Форма и/или NLP из чата (`channel`, confirm) |
| Референс | unified mini (Bohland + Serpell) / short C-BARQ post-adoption |
| Split (Б3) | train/val — референс; test — РФ-пилот |

**Открытый вопрос:** для macro-F1 нужны этикетки каталога; на foreign-сессиях их нет. Рабочий вариант до уточнения: размеченный РФ-пилот → train/val для H₁-baseline/plan-*; референс — H₁-transfer и feature-harmonization.

## Этапы

1. **Сбор:** лонгитюд РФ (неделя / месяц / 3 мес.) → экспертная разметка рекомендаций → ingest/harmonize mini-42; без смешивания ПДн пилота с training без обезличивания.
2. **H₁-baseline:** rule-based «домен + порог T → каталог»; `|P|=|G|=5`; macro-F1 ≥ 0.6 vs random E[F1]=0.125. Полная матрица порогов 14×40=560 (sparse ~40–80). Черновик mapping — автор + научный консультант.
3. **H₁-plan-DT:** DecisionTree, top-5; тот же val; `Δ_DT = macro-F1_DT − macro-F1_baseline ≥ 0.10`.
4. **H₁-plan-LR:** LogisticRegression **one-vs-rest** (N=40 бинарных), top-5 по вероятностям; тот же val; `Δ_LR ≥ 0.10`. В H₁-quality идёт кандидат с большим Δ (если оба < 0.10 — rule-based). См. [model-selection](model-selection.md).
5. **H₁-quality:** принять / править / отклонить + «безопасна»; целевой коридор accept ~60–70%, safe ~97–98%; H₀: accept < 60% или safe < 97% (ориентир test ≈ 20×5 = 100 оценок).
6. **H₁-channel:** embeddings+cosine → confirm → парный TOST доменов vs self-report того же владельца. См. [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md).
   - **Дизайн:** контрбалансировка порядка (форма/чат), слепота NLP к ответам формы, скоры raw и `user_confirmed` (sensitivity), подвыборка test-retest формы.
   - **Критерий:** по каждому ключевому домену $\mathrm{CI}_{90\%}(\bar{D}_d) \subset (-\delta, +\delta)$ (intersection–union, без поправки на множественность).
   - **δ (до сбора):** test-retest «форма vs форма» → иначе 0.3–0.5 · SD домена по референсу → иначе 0.3–0.5 балла шкалы 0–4 с обоснованием кинолога; проверка, что сдвиг на δ почти не меняет top-5 rule-based.
   - **n пар:** $n \approx 8.6\,(\sigma_D/\delta)^2$ — ≈35 / 54 / 96 при δ/σ_D = 0.5 / 0.4 / 0.3; при n ≈ 20 эквивалентность практически не доказуема.
   - **Вторично:** ICC(2,1) absolute ≥ 0.75, Bland–Altman (bias внутри ±δ), quadratic weighted κ по пунктам ≥ 0.6, coverage ≥ 80% пунктов домена.
   - **152-ФЗ:** отдельное согласие на переписку/голос, сырой текст в РФ-контуре, в аналитику — псевдонимизированные скоры + `channel`; encoder локальный / РФ-хостинг.
7. **H₁-transfer:** TOST доменов РФ vs Bohland/short, заранее заданный δ, α = 0.05.
8. **H₁-human-eval:** слепой pairwise K5-RAG vs no-RAG; preference ≥ 70% и значимо > 50%.

## Контур артефактов

```
ingest → clean/harmonize → feature_map → baseline(rule) → train(DT|LR OvR) → evaluate(val)
                                                              ↘ expert accept/safe (test)
text → embed → vector retrieval (пункты шкалы) → NLP scores → TOST vs self-report
wiki → vector RAG → answers → pairwise human-eval
```

Индекс **пунктов C-BARQ** и индекс **wiki для K5** не смешивать.

## Сводка метрик

| Этап | Гипотеза | Ключевая метрика | Эталон |
|------|----------|------------------|--------|
| Rule-based top-5 | H₁-baseline | macro-F1 ≥ 0.6 | random F1 = 0.125 |
| ML top-5 DT | H₁-plan-DT | Δ_DT ≥ 0.10 vs rule | rule-based; CI желателен |
| ML top-5 LR OvR | H₁-plan-LR | Δ_LR ≥ 0.10 vs rule | rule-based; max(Δ) → quality |
| Эксперт | H₁-quality | accept ≥ ~60–70%, safe ≥ ~97–98%; H₀: < 60% / < 97% | принять/править/отклонить |
| NLP↔форма | H₁-channel | парный TOST по каждому домену, δ из test-retest; ICC ≥ 0.75 вторично | self-report того же владельца |
| РФ↔референс | H₁-transfer | TOST, δ | Bohland / short C-BARQ |
| K5-RAG | H₁-human-eval | preference ≥ 70% | ответ без RAG |

**Порядок:** baseline + разметка → plan-DT и plan-LR (один val) → quality для победителя; channel параллельно; transfer после РФ-скоров; human-eval после curated wiki-индекса.

## Связь с прежним K3

Ранее в wiki K3 = tabular risk с целью ROC-AUC ≥ 0.75 ([k3-risk-prediction](../components/k3-risk-prediction.md)). НИР-3 делает **измеримым** контур «анкета → рекомендации плана» (макро-F1 + эксперт). Risk/возврат остаётся долгосрочной продуктовой метрикой, не критерием этих H₁.

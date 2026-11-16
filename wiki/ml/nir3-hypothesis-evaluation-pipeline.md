---
type: ml
tags: [nir3, pipeline, hypotheses, recommendations, nlp, rag, evaluation]
sources: [nir3-hypotheses, nir3-ml-evaluation-pipeline]
updated: 2026-11-16
status: draft
---

# Пайплайн проверки гипотез НИР-3

Методика оценки ML-контуров Hvostun по личным гипотезам семестра. Источники: [nir3-hypotheses](../sources/nir3-hypotheses.md), [nir3-ml-evaluation-pipeline](../sources/nir3-ml-evaluation-pipeline.md).

Связано: [experiment-plan](experiment-plan.md), [benchmarks-and-metrics](benchmarks-and-metrics.md), [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md), [cbarq-mini-sessions-unified](../datasets/cbarq-mini-sessions-unified.md).

## Объект и split

| Элемент | Фиксация |
|---------|----------|
| Объект | анкета 7–14 дней (C-BARQ Mini / C-BARQ(S)) + профиль собаки |
| Таргет | top-5 из каталога (N ≈ 40); эталон G — экспертная разметка |
| Каналы | Яндекс.Форма и/или NLP из чата (`channel`, confirm) |
| Референс | unified mini (Bohland + Serpell) / short C-BARQ post-adoption |
| Split (Б3) | train/val — референс; test — РФ-пилот |

**Открытый вопрос:** для macro-F1 нужны этикетки каталога; на foreign-сессиях их нет. Рабочий вариант до уточнения: размеченный РФ-пилот → train/val для H₁-baseline/plan; референс — H₁-transfer и feature-harmonization.

## Этапы

1. **Сбор:** лонгитюд РФ (неделя / месяц / 3 мес.) → экспертная разметка рекомендаций → ingest/harmonize mini-42; без смешивания ПДн пилота с training без обезличивания.
2. **H₁-baseline:** rule-based «домен + порог T → каталог»; $\lvert P\rvert=5$; macro-F1 ≥ 0,6 vs random $\mathbb{E}[F1]=k/N=0.125$. Полная матрица порогов $14\times 40=560$ (sparse ~40–80). Черновик mapping — автор + научный консультант.
3. **H₁-plan:** мультилейбл / top-5; кандидаты LogisticRegression и DecisionTree (Б2), плюс RandomForest при достаточном n; тот же val; macro-F1_ML > macro-F1_rule. См. [model-selection](model-selection.md).
4. **H₁-quality:** принять / править / отклонить + «безопасна»; accept ≥ 95%, safe ≥ 99%.
5. **H₁-channel:** embeddings+cosine (первый кандидат) → опц. NLI/LLM schema → slot-filling диалог по дырам; confirm → TOST доменов vs self-report. См. [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md).
6. **H₁-transfer:** TOST доменов РФ vs Bohland/short, заранее заданный δ, α = 0,05.
7. **H₁-human-eval:** слепой pairwise K5-RAG vs no-RAG; preference ≥ 70% и значимо > 50%.

## Контур артефактов

```
ingest → clean/harmonize → feature_map → baseline(rule) → train(ML) → evaluate(val)
                                                      ↘ expert accept/safe
text → embed → vector retrieval (пункты шкалы) → NLP scores → TOST vs self-report
wiki → vector RAG → answers → pairwise human-eval
```

Индекс **пунктов C-BARQ** и индекс **wiki для K5** не смешивать.

## Сводка метрик

| Этап | Гипотеза | Ключевая метрика | Эталон |
|------|----------|------------------|--------|
| Rule-based top-5 | H₁-baseline | macro-F1 ≥ 0,6 | random F1 = 0,125 |
| ML top-5 | H₁-plan | macro-F1_ML > rule | rule-based |
| Эксперт | H₁-quality | accept ≥ 95%, safe ≥ 99% | схема принять/править/отклонить |
| NLP↔форма | H₁-channel | TOST, δ | self-report того же владельца |
| РФ↔референс | H₁-transfer | TOST, δ | Bohland / short C-BARQ |
| K5-RAG | H₁-human-eval | preference ≥ 70% | ответ без RAG |

**Порядок:** baseline + разметка → plan → quality; channel параллельно; transfer после РФ-скоров; human-eval после curated wiki-индекса.

## Связь с прежним K3

Ранее в wiki K3 = tabular risk с целью ROC-AUC ≥ 0,75 ([k3-risk-prediction](../components/k3-risk-prediction.md)). НИР-3 делает **измеримым** контур «анкета → рекомендации плана» (макро-F1 + эксперт). Risk/возврат остаётся долгосрочной продуктовой метрикой, не критерием этих H₁.

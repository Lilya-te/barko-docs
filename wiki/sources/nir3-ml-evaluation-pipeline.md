---
type: source
tags: [nir3, pipeline, evaluation, ml, c-barq, nlp, rag]
sources: []
raw_path: NIR_3/personal_files/Б3_Разработать пошаговую методику проверки гипотезы и (для ML) пайплайн оценки.md
updated: 2026-11-18
status: ingested
---

# Source: Методика проверки гипотез и ML-пайплайн оценки (НИР-3)

**Исходный файл:** [`NIR_3/personal_files/Б3_….md`](../../NIR_3/personal_files/Б3_Разработать%20пошаговую%20методику%20проверки%20гипотезы%20и%20(для%20ML)%20пайплайн%20оценки.md)

Гипотезы: [nir3-hypotheses](nir3-hypotheses.md). Curated-синтез: [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md).

**Синхронизация:** Б3 должен совпадать с Б2 по ID/порогам; правило `.cursor/rules/nir3-hypotheses-pipeline-sync.mdc`.

## Ключевые выводы

1. **Объект:** анкета владельца, волна 7–14 дней (C-BARQ Mini / C-BARQ(S)) + профиль собаки; таргет — top-5 из каталога (N = 40), эталон G — эксперт.
2. **Split (как в Б3):** train/val на референсе (Bohland + Serpell unified); **test** — российские респонденты.
3. **Сбор:** пилот РФ (Яндекс.Формы, 3 волны) + экспертный контур разметки + harmonized mini-42; канал `channel`, версия анкеты, согласие в ops.
4. **Порядок экспериментов:** H₁-baseline → H₁-plan-DT и H₁-plan-LR (один val, δ = 0.10) → H₁-quality для победителя (accept H₀ < 60%, safe H₀ < 97%); параллельно H₁-channel; H₁-transfer после РФ-скоров; H₁-human-eval после wiki-RAG.
5. **NLP-канал:** embeddings формулировок пунктов/ответов → cosine retrieval из текста чата → confirm пользователем → доменные скоры → TOST vs self-report.
6. **K5:** слепой pairwise RAG vs no-RAG; preference ≥ 70% и > 50% при α = 0.05.

## Критерии готовности данных

- Item-level или доменные скоры доступны.
- Экспертный эталон G на выборке оценки.
- Согласие / версия формы для ops-контура с ПДн.
- Разделение: сырые ПДн пилота не смешивать с training без обезличивания ([personal-data-152-fz](../concepts/personal-data-152-fz.md)).

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Полный пайплайн | [nir3-hypothesis-evaluation-pipeline](../ml/nir3-hypothesis-evaluation-pipeline.md) |
| Experiment plan | [experiment-plan](../ml/experiment-plan.md) |
| Benchmarks | [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md) |
| Channel / vector | [k5-k3-answer-bridge](../concepts/k5-k3-answer-bridge.md) |

## Противоречия / риски методики

- **Этикетки рекомендаций на foreign train/val:** у Bohland/Serpell нет экспертного каталога Hvostun. Rule-based и macro-F1 на «val = референс» требуют либо переноса разметки, либо уточнения: train/val на размеченных РФ-анкетах, референс — только для H₁-transfer / признаков. Зафиксировано как открытый вопрос на [experiment-plan](../ml/experiment-plan.md).
- Индекс пунктов анкеты и индекс wiki для K5-RAG — **разные** векторные базы.

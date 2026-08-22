# Barko Wiki — Index

Каталог страниц knowledge base. Обновлён: 2026-08-20 (ingest 11 personality/testing articles + MCPQ/DMA/LIEBI).

## Overview

| Страница | Описание |
|----------|----------|
| [overview](overview.md) | Barko: продукт, ML-компоненты, текущий статус исследований |
| [socio-economic-impact](socio-economic-impact.md) | Прогнозируемые социально-экономические эффекты |

## Components (K3 / K5 / K6)

| Страница | Описание |
|----------|----------|
| [k3-risk-prediction](components/k3-risk-prediction.md) | Прогноз адаптационных трудностей — основная ML-задача MVP |
| [k5-ai-chat](components/k5-ai-chat.md) | ИИ-чат на LLM + RAG с экспертной базой |
| [k6-plan-correction](components/k6-plan-correction.md) | Автокоррекция плана (next-best-action) — roadmap |

## Concepts

| Страница | Описание |
|----------|----------|
| [c-barq](concepts/c-barq.md) | Опросник C-BARQ: что это, шкалы, ограничения доступа |
| [pilot-questionnaire](concepts/pilot-questionnaire.md) | Пилотная анкета владельца: общие вопросы + 42 пункта C-BARQ(S) + варианты ответа |
| [data-harmonization](concepts/data-harmonization.md) | Объединение фрагментарных C-BARQ подмножеств для baseline |
| [adoption-return](concepts/adoption-return.md) | Возврат в приют как кандидат на таргет K3 |
| [k3-feature-candidates](concepts/k3-feature-candidates.md) | Приоритетные C-BARQ признаки для K3 (синтез статей) |
| [problem-behavior-taxonomy](concepts/problem-behavior-taxonomy.md) | Таксономия проблемного поведения |
| [owner-dog-attachment](concepts/owner-dog-attachment.md) | Тип привязанности владелец–собака |
| [owner-frustration](concepts/owner-frustration.md) | Разочарованность владельца (~14%) |
| [research-data-app](concepts/research-data-app.md) | Внутреннее приложение сбора данных: монолит, compose, схема Postgres |
| [personal-data-152-fz](concepts/personal-data-152-fz.md) | Чеклист 152-ФЗ для контуров Barko с ПДн |

## Datasets

| Страница | Описание |
|----------|----------|
| [collected-datasets-catalog](datasets/collected-datasets-catalog.md) | Сводка собранных датасетов для K3 baseline |
| [cbarq-open-data-landscape](datasets/cbarq-open-data-landscape.md) | Карта открытых и полуоткрытых C-BARQ источников |
| [2017-wolfram](datasets/2017-wolfram.md) | Wolfram C-BARQ Survey — 12 060 строк, доменные шкалы |
| [figshare-cbarq-dat](datasets/figshare-cbarq-dat.md) | Figshare C-BARQ — 12 061 строк, доменные шкалы |
| [padova-cbarq-italian](datasets/padova-cbarq-italian.md) | Padova — 807 строк, item-level (итальянский) |
| [padova-cbarq-column-dictionary](datasets/padova-cbarq-column-dictionary.md) | Словарь колонок Padova: перевод IT→EN и `@nn`→`question_nnn` |
| [manydogs-md1](datasets/manydogs-md1.md) | ManyDogs 1 — 705 строк, частичный C-BARQ |
| [plos-one-2024-short-cbarq](datasets/plos-one-2024-short-cbarq.md) | PLOS ONE 2024 — ~435 собак, short/full C-BARQ |
| [bohland-2023-shelter-adoption-cbarq](datasets/bohland-2023-shelter-adoption-cbarq.md) | Bohland 2023 — 505 строк, 99 собак, четыре post-adoption волны |
| [bryson-2026-doodle-crossbreed-behaviour](datasets/bryson-2026-doodle-crossbreed-behaviour.md) | Bryson 2026 — ~9 456 item-level C-BARQ записей |
| [helpdog-forum-adoptions](datasets/helpdog-forum-adoptions.md) | HelpDog — 90 собак, история пристройств и возвратов |

## ML

| Страница | Описание |
|----------|----------|
| [model-selection](ml/model-selection.md) | Сравнение кандидатов моделей и критерии выбора |
| [benchmarks-and-metrics](ml/benchmarks-and-metrics.md) | Бенчмарки и метрики для K3 и K5 |
| [mvp-verifiable-metrics](ml/mvp-verifiable-metrics.md) | Измеримые метрики MVP вместо возврата как основной рабочей гипотезы |
| [experiment-plan](ml/experiment-plan.md) | План baseline-эксперимента и критерии готовности для Паспорта |
| [helpdog-adoption-eda](ml/helpdog-adoption-eda.md) | EDA возвратов в приют (57% среди пристроенных) |
| [cbarq-clustering](ml/cbarq-clustering.md) | Exploratory KMeans/GMM-кластеризация Padova; ограничения интерпретации |

## Sources

| Страница | Исходный файл | Описание |
|----------|---------------|----------|
| [fz-152-personal-data](sources/fz-152-personal-data.md) | `152 ФЗ.md` | Саммари 152-ФЗ: только нормы, полезные Barko (согласие, локализация, ops/ML) |
| [ml-ideas-notes](sources/ml-ideas-notes.md) | `_ml_ideas.md` | Подбор модели для ML-решений BARKO |
| [app-ideas-notes](sources/app-ideas-notes.md) | `_app_ideas/_database_architecture.md` | Схема БД и scope research-ops |
| [data-ideas-notes](sources/data-ideas-notes.md) | `analytics/research/datatsets/_data_ideas.md` | Исследование открытых C-BARQ датасетов |
| [foreign-datasets-list-notes](sources/foreign-datasets-list-notes.md) | `analytics/research/datatsets/foreign_datasets_list.md` | Каталог собранных датасетов |
| [helpdog-notebook-notes](sources/helpdog-notebook-notes.md) | `analytics/helpdog_forum/helpdog.ipynb` | EDA пристройств HelpDog |
| [cbarq-clustering-notebooks](sources/cbarq-clustering-notebooks.md) | `analytics/research/notebooks/11,12,21_*.ipynb` | KMeans/GMM кластеризация доменных шкал Padova |
| [duffy-2014-shelter-relinquishment-cbarq](sources/duffy-2014-shelter-relinquishment-cbarq.md) | `статьи/foreign/usa/Duffy_2014_CBARQ_behavioral_assessment_relinquished_dogs.pdf` | Саммари: C-BARQ(S) при передаче собаки в приют; [перевод](../статьи/foreign/translations/duffy_2014_behavioral_assessment_relinquished_dogs_ru.md) |
| [plos-one-2024-short-cbarq-validation](sources/plos-one-2024-short-cbarq-validation.md) | `статьи/foreign/unknown/Wilkins_2024_CBARQ_shortened_cbarq_validation.pdf` | Саммари: валидация C-BARQ(S), 435 собак; [перевод](../статьи/foreign/translations/wilkins_2024_shortened_cbarq_validation_ru.md) |
| [fomina-2024-problem-behavior-review](sources/fomina-2024-problem-behavior-review.md) | `статьи/russian/фомина_2024_проблемное_поведение_собак.pdf` | Обзор 132 статей |
| [fomina-2025-ai-pilot-study](sources/fomina-2025-ai-pilot-study.md) | `статьи/russian/фомина_2025_ии_анализ_поведения.pdf` | CBARQ + AI, n=35 |
| [gritsenko-2023-owner-frustration](sources/gritsenko-2023-owner-frustration.md) | `статьи/russian/гриценко_2023_разочарованность_домашней_собакой.pdf` | Опрос 5820 владельцев |
| [gilchrist-2025-shelter-cbarq](sources/gilchrist-2025-shelter-cbarq.md) | `статьи/foreign/usa/Gilchrist_2025_CBARQ_cbarq_for_shelter_dogs.pdf` | Саммари: Shelter C-BARQ, 24 пункта, 5 факторов; [перевод](../статьи/foreign/translations/gilchrist_2025_cbarq_for_shelter_dogs_ru.md) |
| [bohland-2023-shelter-dog-behavior-ru](sources/bohland-2023-shelter-dog-behavior-ru.md) | `статьи/foreign/unknown/Bohland_2023_CBARQ_shelter_behavior_after_adoption.pdf` | Саммари: динамика C-BARQ за 180 дней; [перевод](../статьи/foreign/translations/bohland_2023_shelter_behavior_after_adoption_ru.md) |
| [gates-2018-post-adoption-problem-behaviours](sources/gates-2018-post-adoption-problem-behaviours.md) | `статьи/foreign/unknown/Gates_2018_SURVEY_post_adoption_problem_behaviours.pdf` | Саммари: проблемное поведение и обеспокоенность владельцев после пристройства; [перевод](../статьи/foreign/translations/gates_2018_post_adoption_problem_behaviours_ru.md) |
| [vitulova-2018-adopted-shelter-dog-behaviour](sources/vitulova-2018-adopted-shelter-dog-behaviour.md) | `статьи/foreign/czech-republic/Vitulova_2018_SURVEY_adopted_shelter_dog_behaviour.pdf` | Саммари: страх, общительность и агрессия в первую неделю и через шесть месяцев; [перевод](../статьи/foreign/translations/vitulova_2018_adopted_shelter_dog_behaviour_ru.md) |
| [powell-2021-deception-or-knowledge](sources/powell-2021-deception-or-knowledge.md) | `статьи/foreign/usa/Powell_2021_SURVEY_deception_or_knowledge.pdf` | Саммари: восприятие поведения при передаче собаки; [перевод](../статьи/foreign/translations/powell_2021_deception_or_knowledge_ru.md) |
| [powell-2022-shelter-dog-returns-ru](sources/powell-2022-shelter-dog-returns-ru.md) | `статьи/foreign/usa/Powell_2022_CBARQ_returning_a_shelter_dog.pdf` | Саммари: ожидания владельца и возврат собаки; [перевод](../статьи/foreign/translations/powell_2022_returning_a_shelter_dog_ru.md) |
| [shabelansky-2016-excitable-dog-behavior-ru](sources/shabelansky-2016-excitable-dog-behavior-ru.md) | `статьи/foreign/usa/Shabelansky_2016_SURVEY_excitable_dog_behavior.pdf` | Саммари: возбудимое поведение собак; [перевод](../статьи/foreign/translations/shabelansky_2016_excitable_dog_behavior_ru.md) |
| [savalli-2019-dog-panas-brazil](sources/savalli-2019-dog-panas-brazil.md) | `статьи/foreign/brazil/Savalli_2019_PANAS_dog_panas_brazil.pdf` | Саммари: PANAS для собак, валидация в Бразилии, n=1744; [перевод](../статьи/foreign/translations/savalli_2019_dog_panas_brazil_ru.md) |
| [fadel-2016-dog-impulsivity-working-show](sources/fadel-2016-dog-impulsivity-working-show.md) | `статьи/foreign/uk/Fadel_2016_DIAS_dog_impulsivity_working_show_lines.pdf` | Саммари: DIAS, рабочие vs выставочные линии Collie/Labrador; [перевод](../статьи/foreign/translations/fadel_2016_dog_impulsivity_working_show_lines_ru.md) |
| [hoth-zimak-2026-rescued-dogs-abroad-germany](sources/hoth-zimak-2026-rescued-dogs-abroad-germany.md) | `статьи/foreign/germany/Hoth_Zimak_2026_BEHAVIOR-SCALES_rescued_dogs_abroad_germany.pdf` | Саммари: проспективная адаптация 158 импортированных собак, 6 мес.; [перевод](../статьи/foreign/translations/hoth_zimak_2026_rescued_dogs_abroad_germany_ru.md) |
| [haverbeke-2008-cortisol-working-dogs](sources/haverbeke-2008-cortisol-working-dogs.md) | `статьи/foreign/belgium/Haverbeke_2008_CORTISOL_working_dogs_environmental_challenges.pdf` | Саммари: cortisol + поведение MWD при environmental challenges; [перевод](../статьи/foreign/translations/haverbeke_2008_cortisol_working_dogs_environmental_challenges_ru.md) |
| [kubinyi-2009-dog-owner-demographics-personality](sources/kubinyi-2009-dog-owner-demographics-personality.md) | `статьи/foreign/hungary/Kubinyi_2009_SURVEY_dog_owner_demographics_personality.pdf` | Саммари: демография и 4 personality traits, n≈14k; [перевод](../статьи/foreign/translations/kubinyi_2009_survey_dog_owner_demographics_personality_ru.md) |
| [ley-2008-mcpq-personality-dimensions](sources/ley-2008-mcpq-personality-dimensions.md) | `статьи/foreign/australia/Ley_2008_MCPQ_personality_dimensions_companion_canines.pdf` | Саммари: разработка MCPQ, 5 факторов personality; [перевод](../статьи/foreign/translations/ley_2008_mcpq_personality_dimensions_companion_canines_ru.md) |
| [ley-2009-mcpq-refinement-validation](sources/ley-2009-mcpq-refinement-validation.md) | `статьи/foreign/australia/Ley_2009_MCPQ_refinement_validation.pdf` | Саммари: MCPQ-R refinement/validation, SEM; [перевод](../статьи/foreign/translations/ley_2009_mcpq_refinement_validation_ru.md) |
| [ley-2009-mcpqr-reliability](sources/ley-2009-mcpqr-reliability.md) | `статьи/foreign/australia/Ley_2009_MCPQR_interrater_test_retest.pdf` | Саммари: надёжность MCPQ-R, inter-rater и test–retest; [перевод](../статьи/foreign/translations/ley_2009_mcpqr_interrater_test_retest_ru.md) |
| [oheare-2009-liebi-algorithm](sources/oheare-2009-liebi-algorithm.md) | `статьи/foreign/canada/OHeare_2009_LIEBI_least_intrusive_behavior_intervention.pdf` | Саммари: LIEBI алгоритм и уровни инвазивности; [перевод](../статьи/foreign/translations/oheare_2009_liebi_least_intrusive_behavior_intervention_ru.md) |
| [range-2009-ostensive-cues-social-learning](sources/range-2009-ostensive-cues-social-learning.md) | `статьи/foreign/austria/Range_2009_EXPERIMENT_ostensive_cues_social_learning.pdf` | Саммари: ostensive cues мешают manipulative social learning; [перевод](../статьи/foreign/translations/range_2009_experiment_ostensive_cues_social_learning_ru.md) |
| [svartberg-2003-dma-consistency](sources/svartberg-2003-dma-consistency.md) | `статьи/foreign/sweden/Svartberg_2003_DMA_consistency_personality_traits.pdf` | Саммари: повторяемость DMA traits и Boldness; [перевод](../статьи/foreign/translations/svartberg_2003_dma_consistency_personality_traits_ru.md) |
| [svartberg-2005-dma-boldness-everyday](sources/svartberg-2005-dma-boldness-everyday.md) | `статьи/foreign/sweden/Svartberg_2005_DMA_boldness_everyday_life.pdf` | Саммари: construct validity DMA vs CBARQ, n=697; [перевод](../статьи/foreign/translations/svartberg_2005_dma_boldness_everyday_life_ru.md) |
| [diederich-2006-behavioural-testing-review](sources/diederich-2006-behavioural-testing-review.md) | `статьи/foreign/belgium/Diederich_2006_REVIEW_behavioural_testing_methodology.pdf` | Саммари: обзор методологии поведенческих тестов, gap стандартизации; [перевод](../статьи/foreign/translations/diederich_2006_review_behavioural_testing_methodology_ru.md) |
| [vas-2008-threatening-cues-consistency](sources/vas-2008-threatening-cues-consistency.md) | `статьи/foreign/hungary/Vas_2008_EXPERIMENT_threatening_cues_consistency.pdf` | Саммари: friendly/threatening stranger, test–retest и inter-experimenter consistency; [перевод](../статьи/foreign/translations/vas_2008_experiment_threatening_cues_consistency_ru.md) |

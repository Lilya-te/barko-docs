# Wiki Log

Хронологический журнал операций над вики Barko.

---

## [2026-06-09] ingest | статьи/ (4 PDF)

**Источники:**
- `статьи/journal.pone.0299973.pdf` — PLOS ONE, валидация C-BARQ(S)
- `статьи/4+RPJ+21(4)+РУ+Фомина.pdf` — обзор проблемного поведения (132 статьи)
- `статьи/11+РПЖ+22(4)+Фомина.pdf` — пилот CBARQ + AI (n=35)
- `статьи/Gritsenko.pdf` — разочарованность владельцев (n=5820)

**Созданные страницы:**
- `sources/plos-one-2024-short-cbarq-validation.md`
- `sources/fomina-2024-problem-behavior-review.md`
- `sources/fomina-2025-ai-pilot-study.md`
- `sources/gritsenko-2023-owner-frustration.md`
- `concepts/k3-feature-candidates.md`
- `concepts/problem-behavior-taxonomy.md`
- `concepts/owner-dog-attachment.md`
- `concepts/owner-frustration.md`

**Обновлены:**
- `concepts/c-barq.md`, `datasets/plos-one-2024-short-cbarq.md`
- `components/k3-risk-prediction.md`, `components/k5-ai-chat.md`
- `index.md`

**Ключевые выводы:**
- MVP-анкета: кандидат **C-BARQ(S)** (42 пункта, валидирован).
- K3 features: separation-related, fear, aggression — высокий приоритет.
- Таргеты: возврат в приют (HelpDog) + разочарованность владельца (14%).
- K5 KB: обзор Фоминой, привязанность, таксономия поведения.

**Открытые вопросы:**
- EDA `pone.0299973.s001.csv` (схема столбцов).
- Лицензии на RAG по русскоязычным статьям.

---

## [2026-06-09] ingest | analytics/helpdog.ipynb

**Источник:**
- `analytics/helpdog.ipynb` + `dogs.csv`, `adoptions.csv`

**Созданные страницы:**
- `datasets/helpdog-forum-adoptions.md`
- `ml/helpdog-adoption-eda.md`
- `concepts/adoption-return.md`
- `sources/helpdog-notebook-notes.md`

**Обновлены:**
- `components/k3-risk-prediction.md`
- `ml/benchmarks-and-metrics.md`
- `ml/experiment-plan.md`
- `overview.md`
- `index.md`

**Ключевые выводы:**
- EDA, не ML benchmark: модели не обучались, ROC-AUC не считался.
- 90 собак, 46 пристроены, 26 вернулись — **~57% возвратов**.
- Кандидат на таргет K3: `returned_to_shelter` после пристройства.
- HelpDog-данные без C-BARQ — слишком малы для самостоятельного baseline.

**Открытые вопросы:**
- Финальное утверждение формулы таргета K3.
- Связка HelpDog с C-BARQ features.
- Запуск baseline K3 на C-BARQ датасетах.

---

## [2026-06-09] ingest | foreign_datasets_list.md

**Источник:**
- `datatsets/foreign_datasets_list.md` — каталог собранных C-BARQ датасетов

**Созданные страницы:**
- `datasets/collected-datasets-catalog.md`
- `datasets/2017-wolfram.md`
- `datasets/figshare-cbarq-dat.md`
- `datasets/padova-cbarq-italian.md`
- `datasets/manydogs-md1.md`
- `datasets/plos-one-2024-short-cbarq.md`
- `sources/foreign-datasets-list-notes.md`

**Обновлены:**
- `datasets/cbarq-open-data-landscape.md`
- `concepts/data-harmonization.md`
- `components/k3-risk-prediction.md`
- `index.md`

**Ключевые выводы:**
- Собрано 5 датасетов: 4 полных C-BARQ + 1 частичный (ManyDogs).
- Wolfram (12 060) и Figshare (12 061) — подозрение на пересечение; нужна дедупликация.
- Padova и PLOS — item-level, требуют агрегации в доменные шкалы.
- Dog Aging Project — кандидат, ещё не собран.

**Открытые вопросы:**
- Дедупликация Wolfram ↔ Figshare.
- Полная схема столбцов `pone.0299973.s001.csv`.
- Фактическое расположение файлов датасетов в репозитории.

---

## [2026-06-09] ingest | _ml_ideas.md + _data_ideas.md

**Источники:**
- `_ml_ideas.md` — подбор модели для ML-решений (BARKO)
- `datatsets/_data_ideas.md` — ландшафт открытых C-BARQ датасетов

**Созданные страницы:**
- `overview.md`
- `components/k3-risk-prediction.md`
- `components/k5-ai-chat.md`
- `components/k6-plan-correction.md`
- `concepts/c-barq.md`
- `concepts/data-harmonization.md`
- `datasets/cbarq-open-data-landscape.md`
- `ml/model-selection.md`
- `ml/benchmarks-and-metrics.md`
- `ml/experiment-plan.md`
- `sources/ml-ideas-notes.md`
- `sources/data-ideas-notes.md`

**Ключевые выводы:**
- MVP K3: tabular ML, baseline-кандидат `RandomForest` + интерпретация через `LogisticRegression`.
- MVP K5: готовая LLM API + RAG, без обучения собственной LLM.
- K6: roadmap, не в MVP.
- Полного открытого C-BARQ датасета нет; baseline на объединении фрагментарных подмножеств с harmonization.
- Целевой ориентир K3: `ROC-AUC >= 0.75`.

**Открытые вопросы:**
- Формула таргета для K3 ещё не зафиксирована в вики.
- ~~Детальные страницы по каждому собранному датасету~~ — сделано в ingest `foreign_datasets_list.md`.
- ~~Результаты `analytics/helpdog.ipynb`~~ — ingested (EDA + кандидат таргета; ML benchmark ещё не запущен).

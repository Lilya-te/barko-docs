# Wiki Log

Хронологический журнал операций над вики Barko.

---

## [2026-07-28] ingest | Схема БД research-ops (`_database_architecture`)

**Источники:**
- `_app_ideas/_database_architecture.md` — таблицы shelters, memberships, dogs, placement_events, consents, questionnaires, answer_events.
- Архитектурный разбор схемы (Groups вместо custom roles; author_id; wave; provenance; domain).

**Обновлены:**
- `sources/app-ideas-notes.md` — raw_path → `_database_architecture.md` (`_main_ideas.md` удалён)
- `concepts/research-data-app.md` — каноническая ER-схема и поля таблиц
- `index.md`

**Ключевые выводы:**
- Placement — отдельная `placement_events`, не одно поле `adopted_at`.
- Доступ к приюту — `shelter_memberships`; app-роли — Django Groups.
- Анкеты: slug + global_number/domain + typed scales; answer_events append-only с value_num/text/date.
- MVP без эксперта и без отдельного audit_log; consents обязательны (152-ФЗ).

**Открытые вопросы:**
- Нужен ли `wave` на первой поставке или хватит повторных sessions без метки дня.
- Добавлять ли Shelter C-BARQ как отдельный questionnaire slug сразу.

---

## [2026-07-24] ingest | Shelter C-BARQ (Gilchrist et al. 2025)

**Источники:**
- `статьи/4 Gilchrist_et_al_ABC_12(1).pdf` — валидация адаптированного C-BARQ для собак в приюте.

**Созданные страницы:**
- `sources/gilchrist-2025-shelter-cbarq.md`

**Обновлены:**
- `concepts/c-barq.md` — добавлена версия Shelter C-BARQ (24 / 5 факторов)
- `concepts/k3-feature-candidates.md` — приоритеты Fear / Aggression / Arousal / Excitability
- `concepts/adoption-return.md` — связь крайних уровней черт с риском возврата
- `index.md`

**Ключевые выводы:**
- Shelter C-BARQ: 24 пункта, 5 факторов (Fear, Arousal, Human Excitability, Dog Aggression, Human Aggression); N=445, 11 приютов; α≈0.78.
- Не то же самое, что C-BARQ(S): другая популяция (staff в приюте vs владелец) и сценарии.
- Фактор **Arousal** без прямого аналога в long C-BARQ; авторы связывают с overstimulation / cortisol в приюте.
- Fear ↔ Human Aggression r=0.71 — сильная коморбидность.

**Открытые вопросы:**
- Нужна ли Shelter C-BARQ в схеме анкет research-data-app наряду с C-BARQ(S) для владельца.
- Данные по запросу у авторов — open dataset нет.

---

## [2026-07-24] ingest | Идеи внутреннего research-ops приложения

**Источники:**
- `_app_ideas/_main_ideas.md` — интерфейс ввода данных для исследования; роли волонтёр/эксперт/админ; PostgreSQL; открытый вопрос по хранилищу training-данных.

**Созданные страницы:**
- `sources/app-ideas-notes.md`
- `concepts/research-data-app.md`

**Обновлены:**
- `index.md`
- `overview.md`

**Ключевые выводы:**
- Цель контура — наполнение БД (не owner UX / K5).
- MVP = modular monolith: один репозиторий, один `docker compose` (`web` + `postgres` + опционально `jupyter`), пакет `ml/` без микросервисов.
- Стек: cookiecutter-django, allauth, Groups, Django Ninja, HTMX, Admin.
- Ops и training — логические слои в одном Postgres + файлы `data/`; ClickHouse/Mongo на MVP не нужны.
- Анкеты: `questionnaires` + append-only `answer_events` (частичное заполнение и динамика).

**Открытые вопросы:**
- Object-level доступ «свой приют» (Groups vs django-guardian) — уточнить при первой пилотной организации.
- Нужен ли сервис `jupyter` в compose с первого дня или достаточно локальных ноутбуков.

---

## [2026-07-18] ingest | ML-заметки и C-BARQ clustering

**Источники:**
- `_ml_ideas.md` — уточнена роль K3 как основного ML-артефакта и связь контекста K3 ↔ K5.
- `analytics/research/notebooks/11_kmeans_cluster.ipynb` — KMeans на 775 очищенных Padova-анкетах и 13 доменных шкалах.
- `analytics/research/notebooks/12_gmm_cluster.ipynb` — GMM на том же срезе.
- `analytics/research/notebooks/21_clusters_compare.ipynb` — план сравнения моделей, без рассчитанных результатов.

**Созданные страницы:**
- `sources/cbarq-clustering-notebooks.md`
- `ml/cbarq-clustering.md`

**Обновлены:**
- `sources/ml-ideas-notes.md`
- `components/k3-risk-prediction.md`
- `concepts/data-harmonization.md`
- `index.md`

**Ключевые выводы:**
- Padova успешно сведён в рабочий срез из 775 собак и 13 доменных шкал; это частично продвигает harmonization, но mapping и обработку пропусков ещё нужно зафиксировать воспроизводимо.
- KMeans выбирает 2 кластера по silhouette (`0.190`): это слабое разделение, пригодное только для exploratory-профилей.
- GMM выбирает 6 компонентов по BIC (`15 463.26`), однако silhouette `−0.02` не подтверждает устойчиво отделённые классы.
- Кластеры не являются K3-target и не заменяют supervised baseline.

**Открытые вопросы:**
- Рассчитать совпадение KMeans/GMM при `k=2` и `k=6` (`ARI`, `NMI`, contingency table).
- Проверить устойчивость кластеров и только затем их связь с внешним target K3.
- Спроектировать K3 ↔ K5 data flow с согласием пользователя и provenance признаков.

---

## [2026-07-08] ingest | Словарь колонок Padova C-BARQ (IT→EN)

**Созданная страница:**
- `datasets/padova-cbarq-column-dictionary.md`

**Ключевые выводы:**
- Составлен перевод названий 123 колонок датасета Padova (`analytics/research/Dataset_22022022.csv`) с итальянского на английский.
- Поля анкеты `@nn.text` переименованы в `question_nnn` (100 пунктов), свободный текст вынесен в `other_*`, демография — в `snake_case`.
- Зафиксированы дефекты источника: дубликат префикса `@74` (squirrels → `question_076`) и пропуск официального C-BARQ item 51 → смещение нумерации после `question_050`.
- Файлы в `analytics/` не изменялись; в вики добавлен готовый Python-сниппет для переименования колонок.

---

## [2026-07-03] query | Измеримые метрики MVP

**Созданная страница:**
- `ml/mvp-verifiable-metrics.md`

**Ключевые выводы:**
- Возврат собаки в приют лучше оставить как долгосрочную north-star / social impact metric, а не как основную рабочую гипотезу MVP.
- Для пилота измеримы более близкие outcome: тревожность владельца, time to panic, доля закрытых вопросов, динамика проблемного поведения, уверенность владельца и качество K5.
- Рабочая причинная цепочка: `Barko -> меньше тревожности и панических ситуаций -> больше уверенности и выполненных рекомендаций -> ниже риск эскалации до возврата`.

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

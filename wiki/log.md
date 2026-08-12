# Wiki Log

Хронологический журнал операций над вики Barko.

---

## [2026-07-28] ingest | Реорганизация путей к источникам

**Источники:**
- `analytics/research/datatsets/` — новое расположение заметок и collected C-BARQ datasets.
- `analytics/helpdog_forum/` — новое расположение ноутбука и CSV HelpDog.
- `analytics/research/raw/padova-cbarq/` — новое расположение подготовленных CSV Padova.

**Обновлены:**
- `sources/data-ideas-notes.md`, `sources/foreign-datasets-list-notes.md`, `sources/helpdog-notebook-notes.md` — `raw_path` и ссылки на исходники.
- `datasets/` — полные пути в `raw_file` / `raw_files`, каталог collected datasets и словарь Padova.
- `ml/helpdog-adoption-eda.md`, `ml/benchmarks-and-metrics.md`, `overview.md`, `index.md` — ссылки на реорганизованные артефакты.

**Ключевые выводы:**
- Канонический каталог collected C-BARQ raw: `analytics/research/datatsets/foreign/`.
- Исторические записи журнала сохраняют пути, актуальные на момент соответствующего ingest.

---

## [2026-07-28] ingest | Bohland et al. (2023): поведение собак после пристройства

**Источник:**
- `статьи/Shelter dog behavior after adoption_ Using the C-BARQ to track dog behavior changes through the first six months after adoption _ PLOS One.pdf` — проспективное исследование 99 собак из пяти приютов Огайо, DOI `10.1371/journal.pone.0289356`.

**Созданная страница:**
- `sources/bohland-2023-shelter-dog-behavior-ru.md` — содержательное саммари и полный русский перевод основной статьи, всех 11 таблиц, рисунка, метаданных, дополнительных материалов, вкладов авторов и 78 источников.

**Обновлены:**
- `index.md`

**Ключевые выводы:**
- C-BARQ измеряли на 7-й, 30-й, 90-й и 180-й день; все четыре волны прошли 62 из 99 владельцев.
- За 180 дней выросли агрессия к незнакомцам, возбудимость, чувствительность к прикосновениям, трудности обучения и преследование; снизились проблемы разлуки и привязанность/поиск внимания.
- Психотропные препараты в приюте предсказывали агрессию к незнакомцам и чувствительность к прикосновениям дома.
- На 180-й день 93,7% владельцев оценили поведение как отличное или хорошее, несмотря на выявленную динамику.
- Для Barko нужны повторные измерения: профиль первой недели нельзя считать устойчивым; результаты наблюдательные и собраны во время COVID-19.

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

---

## [2026-07-29] ingest | Реорганизация каталога статей

**Изменения:**
- 3 российские научные статьи перемещены в `статьи/russian/`.
- 5 зарубежных научных статей перемещены в `статьи/foreign/`.
- PDF переименованы по схеме `главный_автор_год_краткий_заголовок.pdf`.
- Актуальные `raw_path` и markdown-ссылки обновлены в `wiki/sources/` и `wiki/index.md`.
- Практическое руководство VCA оставлено в корне `статьи/`; служебный экспорт `search results.txt` не перемещался.

---

## [2026-07-29] ingest | Саммари и переводы зарубежных статей

**Проверенные источники:**
- `статьи/foreign/bohland_2023_shelter_behavior_after_adoption.pdf` — саммари и полный перевод уже присутствовали.
- `статьи/foreign/gilchrist_2025_cbarq_for_shelter_dogs.pdf` — к существующему саммари добавлен полный перевод.
- `статьи/foreign/wilkins_2024_shortened_cbarq_validation.pdf` — к существующему саммари добавлен полный перевод.
- `статьи/foreign/powell_2022_returning_a_shelter_dog.pdf` — созданы саммари и полный перевод.
- `статьи/foreign/shabelansky_2016_excitable_dog_behavior.pdf` — созданы саммари и полный перевод.

**Созданные страницы:**
- `sources/powell-2022-shelter-dog-returns-ru.md`
- `sources/shabelansky-2016-excitable-dog-behavior-ru.md`

**Обновлённые страницы:**
- `sources/gilchrist-2025-shelter-cbarq.md`
- `sources/plos-one-2024-short-cbarq-validation.md`
- `index.md`

**Ключевые выводы:**
- Ожидания усыновителя и раннее несоответствие ожиданий — отдельный блок признаков риска возврата для K3.
- Возбудимость следует описывать через наблюдаемые сценарии и поведение, отделяя её от агрессии.
- Для K5 особенно важна поддержка владельца в первые дни и недели адаптации.

---

## [2026-07-29] ingest | Вынос полных переводов из wiki

**Изменения:**
- Полные переводы пяти зарубежных статей вынесены в `статьи/foreign/translations/`.
- В `wiki/sources/` оставлены компактные саммари, ссылки на оригинальные PDF и полные переводы.
- Тег `full-translation` на source-страницах заменён на `translation-available`.
- `wiki/index.md` обновлён прямыми ссылками на переводы.

**Причина:**
- `wiki/` остаётся curated-слоем для query и K5 RAG без загрузки полного текста статей в основной контекст.
- Полные переводы сохраняются как производные материалы рядом с зарубежными PDF и доступны по явным ссылкам.

---

## [2026-07-29] ingest | Powell et al. 2021 — восприятие поведения при передаче собаки

**Источник:**
- `статьи/foreign/powell_2021_deception_or_knowledge.pdf`
- DOI: `10.3389/fvets.2021.734973`

**Создано:**
- `sources/powell-2021-deception-or-knowledge.md` — компактное саммари.
- `статьи/foreign/translations/powell_2021_deception_or_knowledge_ru.md` — полный русский перевод.

**Ключевые выводы:**
- 69,3% отдающих владельцев при прямом вопросе не признавали проблем поведения, хотя mini C-BARQ показывал менее благоприятный профиль большинства шкал.
- Конфиденциальность ответов не объясняла расхождение, что не поддерживает гипотезу намеренного обмана.
- Для K3 и K5 конкретные контекстные вопросы надёжнее общего вопроса о наличии «проблемного поведения».

---

## [2026-08-09] ingest | Duffy et al. 2014 — C-BARQ(S) при передаче собаки

**Источник:**
- `статьи/foreign/duffy_2014_behavioral_assessment_relinquished_dogs.pdf`
- DOI: `10.1016/j.prevetmed.2014.10.003`

**Создано:**
- `sources/duffy-2014-shelter-relinquishment-cbarq.md` — компактное саммари.
- `статьи/foreign/translations/duffy_2014_behavioral_assessment_relinquished_dogs_ru.md` — полный русский перевод.

**Обновлено:**
- `concepts/c-barq.md`
- `concepts/k3-feature-candidates.md`
- `index.md`

**Ключевые выводы:**
- 42-пунктовый C-BARQ(S) согласовывался со staff assessment агрессии и различал outcomes adoption/euthanasia.
- После множественной поправки наиболее устойчивым признаком была stranger-directed aggression.
- Большинство intake-оценок слабо переносилось на post-adoption контекст; профиль следует обновлять повторными измерениями.

---

## [2026-08-12] ingest | Переименование и каталогизация зарубежных датасетов

**Переименовано:**
- `2017_wolfram.csv` → `ghirlanda_2013_cbarq_survey_domain_scales_wolfram.csv`.
- `CBARQ.dat` → `ghirlanda_2013_cbarq_survey_domain_scales_figshare.dat`.
- `Dataset_CBARQ.xlsx` → `broseghini_2023_cbarq_italian_validation_responses.xlsx`.
- `journal.pone.0289356.s004.csv` → `bohland_2023_shelter_behavior_after_adoption_supplement_s4.csv`.
- `pone.0299973.s001.csv` → `wilkins_2024_shortened_cbarq_validation_supplement_s1.csv`.
- `260206 Shared open access - Doodle - Behaviour data_.xlsx` →
  `bryson_2026_doodle_crossbreed_behaviour_responses.xlsx`.
- Служебная заметка `Untitled` получила описательное имя и актуальную ссылку.

**Без переименования:**
- `md1_data/manydogs_etal_2024_data.csv` и codebook уже названы по публикации;
  upstream-имена сохранены для воспроизводимости вложенного репозитория.

**Создано:**
- `datasets/bohland-2023-shelter-adoption-cbarq.md`.
- `datasets/bryson-2026-doodle-crossbreed-behaviour.md`.

**Обновлено:**
- Пути в dataset/source pages, сводном каталоге, data harmonization и `index.md`.
- Notebook `03_shelter_dogs_cbarq_data.ipynb` переведён на новое имя Bohland S4.

**Ключевые уточнения:**
- Wolfram и Figshare — два представления одного Ghirlanda 2013 data deposit,
  а не самостоятельные статьи; суффиксы сохраняют происхождение выгрузки.
- Bohland S4 содержит 505 строк export, но только 99 собак и повторные волны.
- Bryson 2026 добавлен как крупный item-level источник; до ML-использования
  нужны проверка codebook и лицензии.

---

## [2026-08-12] ingest | Gates et al. 2018 — проблемное поведение после пристройства

**Источник:**
- `статьи/foreign/gates_2018_post_adoption_problem_behaviours.pdf`
- прежнее имя: `animals-08-00093.pdf`
- DOI: `10.3390/ani8060093`

**Создано:**
- `sources/gates-2018-post-adoption-problem-behaviours.md` — компактное саммари.
- `статьи/foreign/translations/gates_2018_post_adoption_problem_behaviours_ru.md`
  — полный русский перевод основного текста, пяти таблиц и списка литературы.

**Обновлено:**
- `concepts/adoption-return.md`
- `components/k3-risk-prediction.md`
- `components/k5-ai-chat.md`
- `index.md`

**Ключевые выводы:**
- У 70% из 57 собак отмечалось хотя бы одно проблемное поведение, но 87%
  владельцев были не обеспокоены или обеспокоены лишь немного.
- Агрессия была связана с более высокой обеспокоенностью владельцев (`p = 0,012`).
- Возврат в исходный приют — неполный label: альтернативное перепристройство и
  исходы среди неответивших могут не фиксироваться.
- Цифровая поддержка после пристройства соответствует рекомендациям авторов
  и может снижать ресурсную стоимость сопровождения.

---

## [2026-08-12] ingest | Vitulová et al. 2018 — поведение собак после пристройства

**Источник:**
- `статьи/foreign/vitulova_2018_adopted_shelter_dog_behaviour.pdf`
- прежнее имя: `Behaviour_of_dogs_adopted_from_an_animal_shelter.pdf`
- DOI: `10.2754/avb201887020155`

**Создано:**
- `sources/vitulova-2018-adopted-shelter-dog-behaviour.md` — компактное саммари.
- `статьи/foreign/translations/vitulova_2018_adopted_shelter_dog_behaviour_ru.md`
  — полный русский перевод с тремя таблицами, расшифровкой рисунка и литературой.

**Обновлено:**
- `concepts/k3-feature-candidates.md`
- `concepts/adoption-return.md`
- `components/k3-risk-prediction.md`
- `components/k5-ai-chat.md`
- `index.md`

**Ключевые выводы:**
- В первую неделю поведенческие проблемы отмечались у 71,9% из 192 собак.
- Через шесть месяцев пугливость снизилась с 61% до 20%, а общительность
  выросла с 56% до 93%; агрессивность значимо не изменилась.
- Документированная история жестокого обращения была связана с более частым
  проблемным поведением, но исследование наблюдательное и owner-reported.
- Для Barko нужны повторные измерения: ранний страх не следует считать устойчивым
  профилем, тогда как агрессия требует ранней safety-маршрутизации.

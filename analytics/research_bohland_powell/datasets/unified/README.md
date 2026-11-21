# cbarq_mini_sessions

Одна строка = одно заполнение анкеты. Сборка: `src/unify_cbarq.py` (`python src/unify_cbarq.py` из `analytics/research_bohland_powell`).

Файлы: `cbarq_mini_sessions.csv`, `qc_by_source.csv`.

## Поля

`session_id`, `dog_id`, `source`, `instrument` (`mini` | `full_mapped`), `is_mapped`, `wave`, `survey_date`, `adopted_date`, `days_at_home`, `age_months`, `sex`, `neutered`, `weight_kg`, `breed`, `q01`–`q42`, `n_answered`, `shelter`, `raw_dog_id`, `notes`.

`adopted_date` — дата пристройства (когда собака попала домой). `days_at_home` = `survey_date − adopted_date` в днях, только если обе даты есть и разница неотрицательная. В shelter/owners/online даты пристройства нет, поэтому оба поля пустые. В Bohland дата берётся из consent (`Date of adoption`), в PostAdoptionMini — из `AdoptionDate`.

Даты рождения и роста в схеме нет. Возраст только в месяцах. Вес переведён из фунтов (`× 0.45359237`), включая Bohland Sheet1 (единица в файле не подписана, принято lb).

Ответы хранятся как в анкете (0–4). Обратный скоринг пунктов 27–28 для субшкалы Training difficulty здесь не применяется.

## Источники

| source | instrument | Что взято |
|--------|------------|-----------|
| `serpell_shelter_2009` | mini | Shelter Study 2009, пункты `EXC1`…`MIS42` |
| `serpell_postadoption_mini` | mini | PostAdoptionMini, волны `S1`–`S3`. Нет внешнего id и демографии; `dog_id=postmini_NNN` |
| `serpell_owners_full` | full_mapped | Adopting Owners ~100 пунктов → 42 |
| `serpell_online_full` | full_mapped | `Adopting_owners_cbarq_online.csv`, header=строка `DogID`. Возраст из `AgeAtEvaluation` |
| `bohland_2023` | mini | S4 (волны) ⋈ Sheet1 (3) по Animal ID с consent. Волны: 10 дней→`d7`, 30 дней→`d30`, 3 мес→`d90`, 6 мес→`d180` |

Не включён `journal.pone.0289356.s003` (агрегаты по породам). Из трёх Bohland Sheet1 в джойн идёт только Sheet1 (3).

## full → 42

Таблица short↔full: `QUESTS/c-barq-short-full-mapping.md`.

Слияния (max из непустых): `q08` = full 23 и 24; `q23` = full 58 и 59. Строки с `is_mapped=true` нельзя смешивать с нативным mini без этой оговорки.

В online-файле full-пункты 5, 6 и 7 уже развёрнуты. `q29` соответствует full 7 и поэтому тоже уже reversed; `q27`/`q28` — это full 2 и 3, их файл не разворачивает.

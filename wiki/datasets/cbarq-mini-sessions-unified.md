---
type: dataset
tags: [c-barq, harmonization, mini, longitudinal, k3]
sources: [bohland-2023-shelter-dog-behavior-ru]
raw_file: analytics/research_bohland_powell/datasets/unified/cbarq_mini_sessions.csv
updated: 2026-10-28
status: draft
cbarq_coverage: short
rows: 956
format: csv
---

# Единый C-BARQ mini: анкеты и домены

Сведение Bohland 2023 и вложений Serpell (2009 / post-adoption) к одной схеме. Одна строка — одно заполнение. Сборка описана в ноутбуке `analytics/research_bohland_powell/notebooks/01_eda.ipynb` и в `datasets/unified/README.md`.

## Файлы

| Файл | Строк | Что это |
|------|------:|---------|
| `cbarq_mini_sessions.csv` | 956 | анкета: `q01`–`q42` плюс демография |
| `domain_unified.csv` | 956 | те же строки, 14 субшкал и `misc_*` |
| `domain_dedup.csv` | 953 | домены после снятия 3 лишних совпадений профиля шкал |

Каталог: `analytics/research_bohland_powell/datasets/unified/`.

## Схема анкеты

`session_id`, `dog_id`, `source`, `instrument` (`mini` | `full_mapped`), `is_mapped`, `wave`, `survey_date`, `adopted_date`, `days_at_home`, `age_months`, `sex`, `neutered`, `weight_kg`, `breed`, `q01`–`q42`, `n_answered`, `shelter`, `raw_dog_id`.

Возраст только в месяцах. Вес переведён из фунтов (`× 0.45359237`); для Bohland Sheet1 единица в файле не подписана, принято lb. Роста нет. `days_at_home` = `survey_date − adopted_date`, если обе даты есть и разница неотрицательная.

`q27` и `q28` в анкете хранятся как ответил респондент. Обратный балл применяется только при расчёте субшкалы Training difficulty.

## Источники внутри таблицы

| source | Строк | instrument | Замечание |
|--------|------:|------------|-----------|
| `serpell_shelter_2009` | 444 | mini | `EXC1`…`MIS42`; даты пристройства нет |
| `bohland_2023` | 337 | mini | S4 ⋈ Sheet1 (3). Событие «10 days» записано как волна `d7` |
| `serpell_postadoption_mini` | 123 | mini | волны `S1`–`S3`; нет внешнего id и демографии |
| `serpell_owners_full` | 31 | full_mapped | ~100 пунктов → 42 |
| `serpell_online_full` | 21 | full_mapped | `header` на строке `DogID`; возраст из `AgeAtEvaluation` |

Не включён Bohland S3 (агрегаты по породам). Из трёх Sheet1 в джойн берётся только Sheet1 (3).

Full → short: [`QUESTS/c-barq-short-full-mapping.md`](../../QUESTS/c-barq-short-full-mapping.md). Слияния через max: `q08` = full 23 и 24, `q23` = full 58 и 59. В online-файле full-пункты 5–7 уже развёрнуты, поэтому `q29` (full 7) приходит reversed; `q27`/`q28` — это full 2 и 3, их файл не разворачивает.

## Домены

Формулы — [c-barq-short-42-scoring](../concepts/c-barq-short-42-scoring.md). В этом пайплайне среднее считается по непустым пунктам. Если заполнено меньше половины пунктов субшкалы, значение пустое. Это расходится с формулировкой инструкции «делитель фиксированный»: там правило для пропусков не задано.

Самая дырявая шкала — `familiar_dog_aggression` (пункты 11–12 пустые, если другой собаки в доме нет).

## EDA (2026-10-28)

- Совпадения только по 14 шкалам: 6 строк в группах, все кандидаты на снятие (не разные волны одной собаки). Полных дублей без `session_id` нет. Снято 3 строки → `domain_dedup` = 953.
- IQR (`1.5·IQR`) помечает 245 строк хотя бы по одной шкале. Шкалы лежат в 0–4 и скошены, поэтому это хвост, не критерий удаления.
- Пары Spearman/Pearson с |r| ≥ 0.5: агрессия к незнакомцам и к собакам (~0.59), страх незнакомцев и несоциальный страх (~0.53).

## Противоречия со страницами вики

- [c-barq-short-42-scoring](../concepts/c-barq-short-42-scoring.md) оставляет пропуски без правила и пишет про фиксированный делитель. Здесь порог — половина пунктов.
- [bohland-2023-shelter-adoption-cbarq](bohland-2023-shelter-adoption-cbarq.md) описывает волны как 7 / 30 / 90 / 180 дней. В REDCap S4 первая волна называется «10 days after adoption» и в unified помечена `d7`.
- Сырой путь на странице Bohland (`analytics/research/datatsets/...`) — прежнее расположение файла. Рабочая копия S4 для этой сборки: `analytics/research_bohland_powell/datasets/journal.pone.0289356/journal.pone.0289356.s004.csv` (разделитель `;`).

## Ссылки

- [data-harmonization](../concepts/data-harmonization.md)
- [bohland-2023-shelter-adoption-cbarq](bohland-2023-shelter-adoption-cbarq.md)
- [c-barq-short-42-scoring](../concepts/c-barq-short-42-scoring.md)

---
description: 
alwaysApply: true
---

---
description: 
alwaysApply: true
---

---
description: 
alwaysApply: true
---

---
description: 
alwaysApply: true
---

# Hvostun LLM Wiki — Schema

Этот репозиторий — персональная knowledge base проекта **Hvostun** (адаптация собак, C-BARQ, ML-компоненты K3/K5/K6). Агент поддерживает слой `wiki/`; сырые источники не изменяет.

## Три слоя

Корень индивидуальных артефактов НИР-3 (алиас ниже — **`NIR3_ART`**):

`I — НИР 3/03 — Индивидуальные части/Hvostun_Tereshchenkova_Liliia/Индивидуальные артефакты за 3 семестр/`

| Слой | Путь | Правило |
|------|------|---------|
| Raw sources | `NIR3_ART/Б1_…/00_примеры_анкет/` (бывш. `QUESTS/`), `…/01_статьи/`, `…/02_данные/` (бывш. `статьи/`, `analytics/`), `152 ФЗ.md` | Только чтение. Не редактировать PDF, CSV, ноутбуки. |
| Wiki | `wiki/` | Агент создаёт и обновляет markdown-страницы. |
| Schema | `AGENTS.md` | Этот файл — конвенции и workflow. |

Канон Б1/Б2/Б3: `NIR3_ART/Б1_теоретический_анализ_источников/03_выводы.md`, `NIR3_ART/Б2_личные_исследовательские_гипотезы.md`, `NIR3_ART/Б3_методика_проверки_гипотезы_пайплайн_оценки.md`. Заметки `_ml_ideas.md` и `_app_ideas/` **удалены**; канон — `wiki/sources/ml-ideas-notes.md`, `wiki/sources/app-ideas-notes.md`.

## Язык и стиль

- Основной язык страниц: **русский**.
- Технические термины: английские (`ROC-AUC`, `C-BARQ`, `RandomForest`, `next-best-action`).
- Ссылки между страницами: относительные markdown (`[[k3-risk-prediction]]` или `[K3](components/k3-risk-prediction.md)`).
- Каждая страница начинается с YAML frontmatter.

## Типы страниц

| type | Папка | Назначение |
|------|-------|------------|
| `overview` | `wiki/` | Общая картина проекта |
| `component` | `wiki/components/` | K3, K5, K6 — продуктовые ML-компоненты |
| `concept` | `wiki/concepts/` | C-BARQ, адаптация, harmonization |
| `dataset` | `wiki/datasets/` | Ландшафт и описание датасетов |
| `source` | `wiki/sources/` | Саммари одного исходного документа |
| `ml` | `wiki/ml/` | Модели, метрики, эксперименты |
| `synthesis` | любая | Ответы на query, сохранённые в вики |

### Frontmatter (обязательный минимум)

```yaml
---
type: component
tags: [k3, ml, mvp]
sources: [ml-ideas-notes]
updated: 2026-06-09
status: draft | stable | superseded
---
```

## Специальные файлы

- `wiki/index.md` — каталог всех страниц; обновлять при каждом ingest.
- `wiki/log.md` — append-only журнал; формат заголовка: `## [YYYY-MM-DD] ingest | Название`.

## Операции

### Ingest

1. Прочитать источник (raw или заметку).
2. Создать/обновить `wiki/sources/<slug>.md` с ключевыми выводами.
3. Обновить связанные страницы: `concepts/`, `components/`, `datasets/`, `ml/`.
4. Зафиксировать противоречия с существующими страницами (если есть).
5. Обновить `wiki/index.md` и добавить запись в `wiki/log.md`.

### Query

1. Сначала прочитать `wiki/index.md`, затем релевантные страницы.
2. Ответить с цитатами и ссылками на wiki-страницы.
3. Ценные синтезы сохранять как новые страницы (`type: synthesis`).

### Lint

Проверить: противоречия, устаревшие утверждения, orphan-страницы без входящих ссылок, концепты без собственной страницы, пробелы в источниках. Результат — запись в `log.md`.

### Персональные данные (152-ФЗ)

Если задача затрагивает **персональные данные** (контакты владельцев/волонтёров, согласия, идентификаторы пользователей, сообщения в чате, схемы БД/форм/ботов с ПДн, export/ingest):

1. Прочитать [wiki/concepts/personal-data-152-fz.md](wiki/concepts/personal-data-152-fz.md) и при необходимости [wiki/sources/fz-152-personal-data.md](wiki/sources/fz-152-personal-data.md).
2. Проверить соответствие **основным требованиям** 152-ФЗ: цель и минимизация, согласие (версия/фиксация/отзыв) или обезличивание для research/ML, хранение/сбор ПДн граждан РФ на территории РФ, разделение ops и training, отсутствие публикации сырых ПДн.
3. В ответе или плане кратко зафиксировать риски и меры; не править сырой `152 ФЗ.md`.

Правило дублируется в `.cursor/rules/personal-data-152-fz.mdc` (`alwaysApply`).

### NIR-3: гипотезы ↔ пайплайн

Канон: `NIR3_ART/Б2_личные_исследовательские_гипотезы.md` (H₁) и `NIR3_ART/Б3_методика_проверки_гипотезы_пайплайн_оценки.md` (методика). При правке порогов, ID гипотез, моделей или метрик — **обновлять оба файла** и связанные `wiki/sources/nir3-*.md`, `wiki/ml/nir3-hypothesis-evaluation-pipeline.md` (+ benchmarks/model-selection при необходимости), запись в `wiki/log.md`. Правило: `.cursor/rules/nir3-hypotheses-pipeline-sync.mdc`.

## Границы домена

- **В scope:** Hvostun MVP, C-BARQ, датасеты, ML baseline, K5 RAG, гуманная кинология.
- **Вне scope (по умолчанию):** `ds_managment/` — учебные материалы; не смешивать с продуктовой вики без явного запроса.
- **Данные / ноутбуки:** `NIR3_ART/Б1_…/02_данные/` (research_bohland_powell, research_padova, helpdog_forum, diagrams); выводы переносить в `wiki/ml/`, `.ipynb` менять по запросу после плана

## Связь с продуктом

- **K3:** признаки, таргет, модели → `wiki/components/k3-risk-prediction.md`, `wiki/ml/`.
- **K5:** экспертная база для RAG строится из `wiki/` (curated), не напрямую из PDF.
- **K6:** roadmap; страница есть, но в MVP не реализуется.

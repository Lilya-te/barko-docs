# Hvostun K3 RiskScore — план работ

План реализации K3 (прогноз адаптационных трудностей) и research-ops приложения для сбора данных.

Связанные страницы: [K3](../../wiki/components/k3-risk-prediction.md), [research-data-app](../../wiki/concepts/research-data-app.md), [152-ФЗ](../../wiki/concepts/personal-data-152-fz.md).

## Принятое решение по стеку

Основа — официальный [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template):

- FastAPI, Pydantic, SQLModel/SQLAlchemy, Alembic;
- PostgreSQL;
- React + TypeScript + Vite;
- Tailwind CSS + shadcn/ui;
- готовые JWT-auth, регистрация/вход, восстановление пароля, профиль и роль superuser;
- Docker Compose, Traefik, Mailpit, Pytest, Playwright.

Дополнительно:

- Redis — сессии внутренней админки, кэш и позднее Celery;
- FastAdmin — кандидат для CRUD-админки предметных сущностей;
- Jupyter, NumPy, pandas, scikit-learn, pyarrow, matplotlib;
- PyTorch — только после tabular baseline, не в первоначальный образ.

### Что важно не перепутать

Официальный шаблон содержит пользовательский кабинет и управление пользователями, но **не универсальную CRUD-админку уровня Django Admin**. Для shelters/dogs/questionnaires нужен FastAdmin либо отдельные React CRUD-страницы.

`fastapi-users` не подключаем: auth уже есть в шаблоне, а сама библиотека находится в maintenance mode. CRUDAdmin пока помечен авторами как experimental; его можно оценить позднее, но не делать критической зависимостью MVP.

Переход на официальный шаблон означает, что прежние Django, Bootstrap и HTMX исключаются из основного решения. UI делаем на React + Tailwind/shadcn.

## Архитектура

**Modular monolith:** один репозиторий `~/MIPT/startup/hvostun`, один backend FastAPI, один frontend React и один `docker compose`.

```text
~/MIPT/startup/hvostun/
├── backend/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── core/
│   │   ├── domains/
│   │   │   ├── shelters/
│   │   │   ├── dogs/
│   │   │   ├── questionnaires/
│   │   │   └── consents/
│   │   ├── admin/
│   │   ├── ml/
│   │   │   ├── ingest/
│   │   │   ├── export/
│   │   │   ├── features/
│   │   │   └── models/
│   │   └── main.py
│   ├── alembic/
│   ├── notebooks/
│   ├── tests/
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── routes/
│   │   ├── components/
│   │   └── client/
│   └── package.json
├── data/
│   ├── raw/
│   └── processed/
├── compose.yml
├── compose.override.yml
├── .env
└── README.md
```

Новые функции добавляются как доменные модули backend/frontend, а не отдельные HTTP-микросервисы.

## Compose-сервисы

| Сервис | Назначение |
|---|---|
| `backend` | FastAPI и собранный frontend |
| `db` | PostgreSQL |
| `redis` | admin sessions/cache, позднее Celery broker |
| `proxy` | Traefik |
| `mailpit` | перехват email только локально |
| `adminer` | DB-инструмент только локально |
| `jupyter` | опциональный ML-профиль |
| `worker` | Celery, когда появятся фоновые задачи |

## Этапы

| № | Этап | Результат |
|---:|---|---|
| 0 | Bootstrap шаблона | Готовый full-stack с auth, PostgreSQL и Compose |
| 1 | Безопасность, роли, согласия | `admin`/`volunteer`, memberships, версия согласия |
| 2 | Схема предметной БД | shelters, dogs, placements, questionnaires |
| 3 | Внутренняя админка | CRUD и ограничения доступа |
| 4 | Анкета | draft/finish, append-only answer events |
| 5 | ML baseline | ingest/export/train/evaluate |
| 6 | K3 inference | `/api/v1/k3/score`, UI и versioned model |
| 7 | Проверка качества | тесты, метрики, аудит ПДн |
| 8+ | Roadmap K5→K3 | Extract из чата и сравнение каналов |

---

## Этап 0. Создание проекта

### 0.1. Требования

```bash
docker --version
docker compose version
git --version
```

Для разработки без Docker также понадобятся `uv` и `bun`, но первый запуск можно выполнить полностью через Compose.

### 0.2. Получить официальный шаблон

```bash
mkdir -p ~/MIPT/startup
cd ~/MIPT/startup

git clone --depth 1 \
  https://github.com/fastapi/full-stack-fastapi-template.git \
  hvostun

cd ~/MIPT/startup/hvostun

# Сохранить ссылку на шаблон для будущего сравнения обновлений.
git remote rename origin template
```

Если собственный remote уже создан:

```bash
git remote add origin <URL_РЕПОЗИТОРИЯ_HVOSTUN>
```

### 0.3. Настроить локальное окружение

В `.env` заменить как минимум:

```dotenv
PROJECT_NAME="Hvostun"
SECRET_KEY=<openssl-rand-hex-32>
FIRST_SUPERUSER=<локальный-email>
FIRST_SUPERUSER_PASSWORD=<уникальный-пароль>
POSTGRES_PASSWORD=<уникальный-пароль>
```

Сгенерировать секреты:

```bash
openssl rand -hex 32
openssl rand -base64 32
```

Production-секреты не хранить в git. Отслеживаемый шаблонный `.env` допустим только для локальных фиктивных значений.

### 0.4. Первый запуск

```bash
cd ~/MIPT/startup/hvostun

docker compose build
docker compose run --rm backend bash scripts/prestart.sh
docker compose up -d
docker compose ps
```

Проверить:

- приложение: <http://localhost:8000>;
- OpenAPI: <http://localhost:8000/docs>;
- Adminer: <http://localhost:8080> — только local;
- Mailpit: <http://localhost:8025> — только local.

Логи:

```bash
docker compose logs backend
docker compose logs db
```

Для режима автоматической пересборки:

```bash
docker compose watch
```

### 0.5. Локальный режим без backend-контейнера

```bash
cd ~/MIPT/startup/hvostun
docker compose up -d db mailpit

cd backend
uv sync
uv run bash scripts/prestart.sh
uv run fastapi dev
```

В другом терминале:

```bash
cd ~/MIPT/startup/hvostun
bun install
bun run dev
```

Frontend: <http://localhost:5173>, backend: <http://localhost:8000>.

### 0.6. Добавить ML-каталоги и зависимости

```bash
cd ~/MIPT/startup/hvostun

mkdir -p \
  backend/app/ml/{ingest,export,features,models} \
  backend/notebooks \
  data/{raw,processed}

touch \
  backend/app/ml/__init__.py \
  backend/app/ml/ingest/__init__.py \
  backend/app/ml/export/__init__.py \
  backend/app/ml/features/__init__.py \
  backend/app/ml/models/__init__.py

cd backend
uv add numpy pandas scikit-learn pyarrow matplotlib jupyterlab
```

PyTorch пока не добавлять: он существенно увеличивает образ, а K3 начинается с `DummyClassifier`, `LogisticRegression` и `RandomForest`.

### 0.7. Добавить Redis

В `compose.yml`/`compose.override.yml` добавить сервис:

```yaml
redis:
  image: redis:7-alpine
  restart: unless-stopped
  command: redis-server --appendonly yes
  volumes:
    - app-redis-data:/data
  healthcheck:
    test: ["CMD", "redis-cli", "ping"]
    interval: 10s
    timeout: 5s
    retries: 5
```

И named volume:

```yaml
volumes:
  app-db-data:
  app-redis-data:
```

Redis не публиковать наружу в production; доступ — только из внутренней compose-сети.

### 0.8. Jupyter как optional profile

```yaml
jupyter:
  profiles: ["ml"]
  build:
    context: .
    dockerfile: backend/Dockerfile
  command:
    - uv
    - run
    - jupyter
    - lab
    - --ip=0.0.0.0
    - --port=8888
    - --no-browser
    - --allow-root
  volumes:
    - ./backend:/app/backend
    - ./data:/app/data
  ports:
    - "127.0.0.1:8888:8888"
  environment:
    DATABASE_URL: postgresql://postgres:${POSTGRES_PASSWORD}@db:5432/app
  depends_on:
    db:
      condition: service_healthy
```

Запуск:

```bash
docker compose --profile ml up -d jupyter
```

Перед применением уточнить рабочую директорию и путь `uv` по фактическому `backend/Dockerfile` шаблона.

### 0.9. Проверки и первый commit

```bash
cd ~/MIPT/startup/hvostun

docker compose exec backend bash scripts/tests-start.sh

git add .
git commit -m "chore: bootstrap Hvostun from full-stack FastAPI template"
```

Критерий готовности этапа 0:

- [ ] работает login и superuser;
- [ ] backend, frontend и PostgreSQL поднимаются Compose;
- [ ] `/docs` открывается;
- [ ] тесты шаблона проходят;
- [ ] Redis отвечает healthcheck;
- [ ] ML-пакет импортируется;
- [ ] production secrets и данные не попадают в git.

---

## Этап 1. Auth, роли и согласия

- Использовать auth из шаблона, не добавлять второй auth framework.
- Для внутреннего research-ops отключить публичную регистрацию: пользователей создаёт/приглашает администратор.
- Сохранить `is_superuser` для системного администратора.
- Добавить прикладные роли и `shelter_memberships`; проверять доступ на уровне API-запросов.
- Реализовать `consents`: `type`, `version`, `accepted_at`, `withdrawn_at`.
- Запретить анкету без действующего согласия нужной версии.
- Добавить rate limiting на login/reset и аудит административных действий.

## Этап 2. Схема БД

- SQLModel-модели и Alembic-миграции:
  `shelters`, `shelter_memberships`, `dogs`, `placement_events`,
  `consents`, `questionnaires`, `questions`, `scales`,
  `questionnaire_sessions`, `answer_events`.
- Стабильный `global_number` для C-BARQ; `wave` и `channel`.
- `answer_events` — append-only; текущий ответ вычисляется как последний event.
- Seed C-BARQ(S) 42 отдельной идемпотентной командой.

Команды миграций:

```bash
cd ~/MIPT/startup/hvostun/backend
uv run alembic revision --autogenerate -m "add research ops schema"
uv run alembic upgrade head
```

## Этап 3. Внутренняя админка

Сначала сделать короткий integration spike FastAdmin + SQLModel:

1. подключить `fastadmin[fastapi,sqlalchemy]`;
2. использовать существующую таблицу User и только superuser-auth;
3. смонтировать под `/internal/admin`, не под публичный API;
4. зарегистрировать shelters/dogs/questionnaires;
5. проверить relationships, permissions, CSRF/session security и audit.

```bash
cd ~/MIPT/startup/hvostun/backend
uv add "fastadmin[fastapi,sqlalchemy]"
```

Если spike не проходит критерии безопасности/совместимости, не менять ORM: сделать минимальные React CRUD-страницы поверх API и сгенерированного клиента.

Adminer — инструмент разработчика, не продуктовая админка; в production не публиковать.

## Этап 4. Анкета

- React + shadcn UI: сохранение draft, продолжение, finish.
- Backend валидирует диапазоны шкал и права на собаку.
- Все исправления создают новые `answer_events`.
- Показывать прогресс и источник (`channel`), не вычислять K3 до минимально достаточного набора.

## Этап 5. ML baseline

- `app.ml.ingest`: открытые subsets с provenance.
- `app.ml.export`: обезличенный Parquet.
- Baselines: DummyClassifier → LogisticRegression → RandomForest.
- Метрики: ROC-AUC, PR-AUC, Recall high-risk, calibration.
- Артефакт модели содержит версию схемы features и метрики.

## Этап 6. Inference

- `POST /api/v1/k3/score`;
- Pydantic request/response;
- model registry на локальном/RF-хранилище;
- вывод вероятности и зон внимания, не юридически значимое авторешение;
- логировать версию модели, но не сырые ПДн.

## Этап 7. Проверка готовности

- Pytest: permissions, consent, migrations, answer event immutability, scoring.
- Playwright: login → собака → анкета в два захода → результат.
- Backup/restore PostgreSQL.
- Закрытые Redis, Adminer, Jupyter и internal admin в production.
- Документация запуска и rollback.

## Этап 8+ (roadmap). K5 → K3 и сравнение каналов

См. [k5-k3-answer-bridge](../../wiki/concepts/k5-k3-answer-bridge.md):

- извлечение пунктов из диалога K5 только как draft + подтверждение;
- `channel=k5_extract`, confidence и provenance;
- сравнение Яндекс.Формы и Амелько;
- отдельный сборщик допустим, но данные ingestятся в общую схему.

## 152-ФЗ

- ПДн, сообщения и согласия хранить на инфраструктуре в РФ.
- Не использовать FastAPI Cloud, зарубежный error tracking/email или внешний primary store для production ПДн без отдельной правовой оценки.
- Mailpit — только local; Adminer/Jupyter — только локальный доступ.
- Ops Postgres содержит ПДн; training export обезличен и не содержит email, телефона, текста чата.
- Цель, минимизация, версия согласия, отзыв, сроки хранения и уничтожение должны быть реализованы до пилота.
- Это технический чеклист, не юридическое заключение; формулировки согласия согласовать с юристом.

## База данных - PostgreSQL

### ER-схема (черновик)
```mermaid
erDiagram
  shelters {
    uuid id PK
    text name
    text description
    text address
    text contact_info
    timestamptz created_at
    timestamptz updated_at
  }

  users {
    uuid id PK
    text name
    text "group"
    text email
    text phone
    text contact
    timestamptz created_at
    timestamptz updated_at
  }

  dogs {
    uuid id PK
    text name
    text sex
    bool neutered
    text status
    text description
    uuid shelter_id FK
    uuid assigned_volunteer FK
    uuid owner_id FK
    date birthday
    date status_at
    text breed
    bool mixed
    uuid created_by_id FK
    timestamptz created_at
    timestamptz updated_at
  }

  dog_chips {
    uuid id PK
    uuid dog_id FK
    text system
    text code
    timestamptz created_at
  }

  placement_events {
    uuid id PK
    uuid dog_id FK
    text code
    timestamptz created_at
  }

  consents {
    uuid user_id FK
    text type
    timestamptz accepted_at
    text version
  }

  surveys {
    uuid id PK
    text name
    text slug
    text description
    timestamptz created_at
    timestamptz updated_at
  }

  survey_versions {
    uuid id PK
    uuid survey_id FK
    int version_num
    text description
    timestamptz created_at
  }

  scales {
    uuid id PK
    text type
    jsonb config
    timestamptz created_at
    timestamptz updated_at
  }

  questions {
    uuid id PK
    uuid global_id
    text text
    uuid scale_id FK
    timestamptz created_at
    timestamptz updated_at
  }

  surveys_questions {
    uuid survey_version_id PK, FK
    uuid question_id PK, FK
    int order_num
    uuid user_id FK
    timestamptz created_at
  }

  survey_sessions {
    uuid id PK
    uuid owner_id FK
    uuid dog_id FK
    uuid survey_version_id FK
    text status
    jsonb client_metadata
    timestamptz created_at
    timestamptz updated_at
  }

  answer_events {
    uuid id PK
    uuid surveys_session_id FK
    uuid survey_version_id FK
    uuid question_id FK
    jsonb value
    timestamptz created_at
  }

  shelters ||--o{ dogs : "hosts"
  users ||--o{ dogs : "created_by"
  users ||--o{ dogs : "assigned_volunteer"
  users ||--o{ dogs : "owner"
  dogs ||--o{ dog_chips : "has"
  dogs ||--o{ placement_events : "timeline"
  users ||--o{ consents : "accepts"
  surveys ||--o{ survey_versions : "versions"
  survey_versions ||--o{ surveys_questions : "contains"
  questions ||--o{ surveys_questions : "included"
  scales ||--o{ questions : "uses"
  users ||--o{ survey_sessions : "fills"
  dogs ||--o{ survey_sessions : "about"
  survey_versions ||--o{ survey_sessions : "instance_of"
  survey_sessions ||--o{ answer_events : "stores"
  survey_versions ||--o{ answer_events : "validates"
  questions ||--o{ answer_events : "answers"
```

> 152-ФЗ: `users`, `consents`, `questionnaire_sessions.client_metadata` и ответы могут содержать ПДн; для ops-контура важно хранить согласия (версия/дата), минимизировать поля и отделять обезличенный ML-export.

### shelters
id
name
description
address
contact_info
created_at
updated_at

### dogs
id
name
sex
neutered
status (shelter / home / back_shelter / overexposure / unknown)
description
shelter_id
assigned_volunteer
owner_id
birthday
status_at
breed
mixed
created_by_id
created_at
updated_at

### dog_chips
id
dog_id
system
code
created_at

### placement_events
id
dog_id
code (shelter_started / home_started / back_shelter / overexposure_started)
created_at

### users
id
name
group
email
phone
contact
created_at
updated_at

### consents 
user_id
type
accepted_at
version

### surveys
например cbarq_s_42, cbarq_long_100 (см. c-barq)
id
name
slug
description
created_at
updated_at

### survey_versions — immutable
id
survey_id
version_num
description
created_at

### questions
id
global_id
text
scale_id
created_at
updated_at

### surveys_questions — immutable composition
survey_version_id
question_id
order_num
user_id
created_at

### scales
шкалы - целое число от 0 до 100 или от 0 до 4 или 0-10. Текст. Дата
id
type
config (json: min_value, max_value, legend)
created_at
updated_at

### survey_sessions — по собаке и точной версии анкеты
id
owner_id
dog_id
survey_version_id
status (draft/finished/canceled)
client_metadata (данные о сессии с устройства)
created_at
updated_at

### answer_events — append-only; текущий ответ = последний event
id
surveys_session_id
survey_version_id
question_id
value (json: {"value": ...})
created_at

Все внешние ключи используют `ON DELETE RESTRICT`. ORM запрещает изменение и
удаление survey_versions, questions, scales, recommendations и answer_events.
Два составных FK answer_events гарантируют, что session и question относятся
к одному survey_version.




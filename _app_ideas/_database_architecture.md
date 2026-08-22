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
    date adopted_at
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

  questionnairies {
    uuid id PK
    text name
    text slug
    text description
    timestamptz created_at
    timestamptz updated_at
  }

  scales {
    uuid id PK
    text type
    int min_value
    int max_value
    timestamptz created_at
    timestamptz updated_at
  }

  questions {
    uuid id PK
    uuid questionnairie_id FK
    int global_number
    int order_number
    text text
    uuid scale_id FK
    timestamptz created_at
    timestamptz updated_at
  }

  questionnaire_sessions {
    uuid id PK
    uuid user_id FK
    uuid dog_id FK
    uuid questionnairie_id FK
    text status
    jsonb client_metadata
    timestamptz created_at
    timestamptz updated_at
  }

  answer_events {
    uuid id PK
    uuid session_id FK
    uuid question_id FK
    numeric value_num
    text value_text
    date value_date
    timestamptz created_at
  }

  shelters ||--o{ dogs : "hosts"
  users ||--o{ dogs : "created_by"
  users ||--o{ dogs : "assigned_volunteer"
  users ||--o{ dogs : "owner"
  dogs ||--o{ dog_chips : "has"
  dogs ||--o{ placement_events : "timeline"
  users ||--o{ consents : "accepts"
  questionnairies ||--o{ questions : "contains"
  scales ||--o{ questions : "uses"
  users ||--o{ questionnaire_sessions : "fills"
  dogs ||--o{ questionnaire_sessions : "about"
  questionnairies ||--o{ questionnaire_sessions : "instance_of"
  questionnaire_sessions ||--o{ answer_events : "stores"
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
status (shelter / home / overexposure / unknown)
description
shelter_id
assigned_volunteer
owner_id
birthday
adopted_at
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
code (shelter_started / home_started / overexposure_started / unknown)
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

### questionnairies
например cbarq_s_42, cbarq_long_100 (см. c-barq)
id
name
slug
description
created_at
updated_at

### questions
id
questionnairie_id
global_number
order_number
text
scale_id
created_at
updated_at

### scales
шкалы - целое число от 0 до 100 или от 0 до 4 или 0-10. Текст. Дата
id
type
min_value
max_value
created_at
updated_at

### questionnaire_sessions — по собаке и анкете: draft  submitted
id
user_id
dog_id
questionnairie_id
status (draft/finished/canceled)
client_metadata (данные о сессии с устройства)
created_at
updated_at

### answer_events — append-only; текущий ответ = последний event
id
session_id
question_id
value_num
value_text
value_date
created_at




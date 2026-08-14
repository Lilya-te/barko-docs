## База данных - PostgreSQL
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




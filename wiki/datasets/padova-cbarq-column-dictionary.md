---
type: dataset
tags: [c-barq, padova, data-dictionary, column-mapping, k3]
sources: [padova-cbarq-italian]
raw_file: analytics/research/Dataset_22022022.csv
updated: 2026-07-08
status: stable
---

# Padova C-BARQ — словарь колонок (IT → EN)

Перевод названий полей датасета Padova C-BARQ с итальянского на английский и
переименование пунктов анкеты. Правила:

- Демографические / служебные поля → читаемые английские имена (`snake_case`).
- Поля анкеты в формате `@nn.text` → `question_nnn` (с ведущими нулями).
- Свободный текст («Are there any other situations…», «Please describe…») → отдельные `other_*` поля.

Всего **123 колонки**: 16 демографических + 100 вопросов + 7 свободного текста.

Источник данных: `analytics/research/Dataset_22022022.csv` (и идентичный по колонкам
`analytics/research/Dataset_CBARQ/Dataset_22022022.csv`). Файлы raw не изменяются —
см. [padova-cbarq-italian](padova-cbarq-italian.md).

## Известные особенности источника

- **Дубликат `@74`.** В шапке дважды встречается префикс `@74`: `@74.Rincorreigatti…`
  (chases cats) и `@74.Rincorregliscoiattoli…` (chases squirrels). Второй — опечатка,
  по содержанию это пункт 76. Маппинг: cats → `question_074`, birds → `question_075`,
  squirrels → `question_076`.
- **Пропущен официальный пункт 51** C-BARQ («When stepped over by a member of the
  household»). Поэтому в датасете 100 пунктов вместо официального 101, и после
  `question_050` нумерация датасета смещена на −1 относительно официальной анкеты
  (`question_051` = официальный item 52 «feet toweled», и т.д.).
- Два свободнотекстовых поля называются в CSV одинаково (`Sesìdescrivilequisotto`);
  при чтении через pandas второе становится `Sesìdescrivilequisotto.1`. Поэтому ниже
  рекомендуется переименование по позиции (`df.columns = new_columns`), а не по имени.

## Демографические и служебные поля

| # | Оригинал (IT) | English | New name |
|---|----------------|---------|----------|
| 1 | QualèletàdelcaneAnni | Dog's age — years | `dog_age_years` |
| 2 | QualèletàdelcaneMesi | Dog's age — months | `dog_age_months` |
| 3 | Razza | Breed | `breed` |
| 4 | RazzaAltro | Breed — other | `breed_other` |
| 5 | Sesso | Dog's sex | `dog_sex` |
| 6 | Ilcaneèstatocastratosterilizzato | Neutered / spayed | `neutered_spayed` |
| 7 | CheetàavevailcanequandolhaiadottatoAnni | Age at adoption — years | `age_at_adoption_years` |
| 8 | CheetàavevailcanequandolhaiadottatoMesi | Age at adoption — months | `age_at_adoption_months` |
| 9 | Qualèiltuosesso | Owner's sex | `owner_sex` |
| 10 | Quantiannihai | Owner's age | `owner_age` |
| 11 | Qualèlatuaprofessione | Owner's profession | `owner_profession` |
| 12 | QualèlatuaprofessioneAltro | Owner's profession — other | `owner_profession_other` |
| 13 | Almomentohaialtricanioltreaquello… | Other dogs currently in household | `other_dogs_present` |
| 14 | Sesìquantialtricanicisono…delq | Other dogs count by age | `other_dogs_by_age` |
| 15 | Sesìquantialtricanicisono…_A | Other dogs count by age (A) | `other_dogs_by_age_a` |
| 16 | Sesìquantialtricanicisono…_B | Other dogs count by age (B) | `other_dogs_by_age_b` |

## Свободнотекстовые поля

| Оригинал (IT) | English | New name |
|----------------|---------|----------|
| Cisonoaltresituazioni…comportamentoag | Other aggression situations? (yes/no) | `other_aggression_present` |
| Sesìdescrivilebrevementequisotto | Other aggression — describe | `other_aggression_describe` |
| Cisonoaltresituazioni…paura o è ansioso | Other fear/anxiety situations? (yes/no) | `other_fear_present` |
| Sesìdescrivilequisotto | Other fear/anxiety — describe | `other_fear_describe` |
| Cisonoaltresituazioni…eccessivamenteec | Other over-excitement situations? (yes/no) | `other_excitability_present` |
| Sesìdescrivilequisotto (.1) | Other over-excitement — describe | `other_excitability_describe` |
| Perfavoredescriviicomportamentibizzarri… | Bizarre/repetitive behaviour — describe | `other_bizarre_behavior_describe` |

## Пункты анкеты (`question_nnn`)

Английские формулировки — по официальному C-BARQ (©2015 J. A. Serpell, UPenn).

### Section 1 — Training & obedience
| New name | C-BARQ item |
|----------|-------------|
| `question_001` | Off leash, returns immediately when called |
| `question_002` | Obeys the "sit" command immediately |
| `question_003` | Obeys the "stay" command immediately |
| `question_004` | Attends/listens closely to everything you say/do |
| `question_005` | Slow to respond to correction/punishment ("thick-skinned") |
| `question_006` | Slow to learn new tricks or tasks |
| `question_007` | Easily distracted by sights, sounds, smells |
| `question_008` | Will fetch sticks, balls, or objects |

### Section 2 — Aggression
| New name | C-BARQ item |
|----------|-------------|
| `question_009` | When verbally corrected/punished by household member |
| `question_010` | Approached by unfamiliar adult while on leash |
| `question_011` | Approached by unfamiliar child while on leash |
| `question_012` | Toward strangers approaching while dog is in car |
| `question_013` | When toys/bones/objects taken away by household member |
| `question_014` | When bathed or groomed by household member |
| `question_015` | Stranger approaches you/family at home |
| `question_016` | Strangers approach you/family away from home |
| `question_017` | Approached by household member while eating |
| `question_018` | Toward mailmen / delivery workers |
| `question_019` | When food taken away by household member |
| `question_020` | Strangers walk past home while dog is outside |
| `question_021` | Stranger tries to touch or pet the dog |
| `question_022` | Toward joggers/cyclists/skateboarders passing home |
| `question_023` | Approached by unfamiliar male dog while on leash |
| `question_024` | Approached by unfamiliar female dog while on leash |
| `question_025` | Stared at directly by household member |
| `question_026` | Toward unfamiliar dogs visiting home |
| `question_027` | Toward cats/squirrels/animals entering yard |
| `question_028` | Toward unfamiliar persons visiting home |
| `question_029` | When barked/growled/lunged at by unfamiliar dog |
| `question_030` | When stepped over by household member |
| `question_031` | When you retrieve food/objects stolen by dog |
| `question_032` | Toward another familiar household dog |
| `question_033` | Approached at resting place by familiar household dog |
| `question_034` | Approached while eating by familiar household dog |
| `question_035` | Approached while playing/chewing by familiar household dog |

### Section 3 — Fear & anxiety
| New name | C-BARQ item |
|----------|-------------|
| `question_036` | Approached by unfamiliar adult away from home |
| `question_037` | Approached by unfamiliar child away from home |
| `question_038` | Sudden or loud noises |
| `question_039` | Unfamiliar persons visit home |
| `question_040` | Stranger tries to touch or pet the dog |
| `question_041` | In heavy traffic |
| `question_042` | Strange/unfamiliar objects on sidewalk |
| `question_043` | Examined/treated by veterinarian |
| `question_044` | Thunderstorms, fireworks, similar events |
| `question_045` | Approached by unfamiliar dog of same/larger size |
| `question_046` | Approached by unfamiliar dog of smaller size |
| `question_047` | First exposure to unfamiliar situations |
| `question_048` | Wind or wind-blown objects |
| `question_049` | When nails clipped by household member |
| `question_050` | When groomed or bathed by household member |
| `question_051` | When feet toweled by household member *(official item 52)* |
| `question_052` | When unfamiliar dogs visit home *(official item 53)* |
| `question_053` | When barked/growled/lunged at by unfamiliar dog *(official item 54)* |

### Section 4 — Separation-related behaviour
| New name | C-BARQ item |
|----------|-------------|
| `question_054` | Shaking, shivering, trembling |
| `question_055` | Excessive salivation |
| `question_056` | Restlessness, agitation, pacing |
| `question_057` | Whining |
| `question_058` | Barking |
| `question_059` | Howling |
| `question_060` | Chewing/scratching doors, floor, windows, etc. |
| `question_061` | Loss of appetite |

### Section 5 — Excitability
| New name | C-BARQ item |
|----------|-------------|
| `question_062` | When family comes home after brief absence |
| `question_063` | When playing with household members |
| `question_064` | When doorbell rings |
| `question_065` | Just before being taken for a walk |
| `question_066` | Just before a car trip |
| `question_067` | When visitors arrive at home |

### Section 6 — Attachment & attention-seeking
| New name | C-BARQ item |
|----------|-------------|
| `question_068` | Strong attachment to one particular household member |
| `question_069` | Follows household members around the house |
| `question_070` | Sits close to / in contact with you when seated |
| `question_071` | Nudges, nuzzles, or paws for attention |
| `question_072` | Agitated when you show affection to another person |
| `question_073` | Agitated when you show affection to another animal |

### Section 7 — Miscellaneous
| New name | C-BARQ item |
|----------|-------------|
| `question_074` | Chases or would chase cats |
| `question_075` | Chases or would chase birds |
| `question_076` | Chases or would chase squirrels/small animals *(labeled `@74` in source — typo)* |
| `question_077` | Escapes or would escape from home/yard |
| `question_078` | Rolls in droppings or "smelly" substances |
| `question_079` | Eats own or other animals' droppings |
| `question_080` | Chews inappropriate objects |
| `question_081` | "Mounts" objects, furniture, or people |
| `question_082` | Begs persistently for food |
| `question_083` | Steals food |
| `question_084` | Nervous or frightened on stairs |
| `question_085` | Pulls excessively hard on the leash |
| `question_086` | Urinates against objects/furnishings indoors |
| `question_087` | Urinates when approached, petted, handled |
| `question_088` | Urinates when left alone |
| `question_089` | Defecates when left alone |
| `question_090` | Hyperactive, restless, hard to settle |
| `question_091` | Playful, puppyish, boisterous |
| `question_092` | Active, energetic, always on the go |
| `question_093` | Stares intently at nothing visible |
| `question_094` | Snaps at invisible flies |
| `question_095` | Chases own tail / hind end |
| `question_096` | Chases shadows, light spots, etc. |
| `question_097` | Barks persistently when alarmed or excited |
| `question_098` | Licks him/herself excessively |
| `question_099` | Licks people or objects excessively |
| `question_100` | Displays other bizarre/strange/repetitive behaviour |

## Применение в ноутбуке

Переименование по позиции (устойчиво к дубликатам имён в CSV):

```python
new_columns = [
    # --- demographics & service (16) ---
    "dog_age_years", "dog_age_months", "breed", "breed_other", "dog_sex",
    "neutered_spayed", "age_at_adoption_years", "age_at_adoption_months",
    "owner_sex", "owner_age", "owner_profession", "owner_profession_other",
    "other_dogs_present", "other_dogs_by_age", "other_dogs_by_age_a", "other_dogs_by_age_b",
    # --- aggression Q1–Q35 ---
    *[f"question_{i:03d}" for i in range(1, 36)],
    "other_aggression_present", "other_aggression_describe",
    # --- fear Q36–Q53 ---
    *[f"question_{i:03d}" for i in range(36, 54)],
    # --- separation Q54–Q61 ---
    *[f"question_{i:03d}" for i in range(54, 62)],
    "other_fear_present", "other_fear_describe",
    # --- excitability Q62–Q67 ---
    *[f"question_{i:03d}" for i in range(62, 68)],
    "other_excitability_present", "other_excitability_describe",
    # --- attachment + miscellaneous Q68–Q100 ---
    *[f"question_{i:03d}" for i in range(68, 101)],
    "other_bizarre_behavior_describe",
]

assert len(new_columns) == df_cbarq.shape[1], (len(new_columns), df_cbarq.shape[1])
df_cbarq.columns = new_columns
```

## Ссылки

- [padova-cbarq-italian](padova-cbarq-italian.md)
- [c-barq](../concepts/c-barq.md)
- [k3-feature-candidates](../concepts/k3-feature-candidates.md)

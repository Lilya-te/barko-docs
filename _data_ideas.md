<!-- Техрешение -->
# Найти открытые датасеты по опроснику C-BARQ

**Данные C-BARQ частично существуют в открытом доступе — но не сам основной полный датасет UPenn.**
Доступ к данным — **фрагментированный и контролируемый**.

---

# 🧠 1. Основная база C-BARQ (University of Pennsylvania)

* Официальный сайт: [C-BARQ database overview](https://vetapps.vet.upenn.edu/cbarq/about.cfm?utm_source=chatgpt.com)
* Содержит **~50 000+ собак, 300+ пород** ([vetapps.vet.upenn.edu][1])

### ❗ Важно:

* ❌ **Нет публичной выгрузки (CSV / open dataset)**
* ❌ Нет API или открытого репозитория
* ✔ Доступ возможен:

  * через **сотрудничество с исследователями**
  * через участие в проектах
* ✔ Данные хранятся с профилями пользователей → ограничения по приватности ([vetapps.vet.upenn.edu][2])

👉 Это типичный случай: **“research database, not open dataset”**

---

# 📊 2. Есть ли опубликованные датасеты на основе C-BARQ?

Да — но **вторичные и фрагментарные**.

## ✅ 2.1. Supplementary datasets в статьях

Пример:

* 📄 [Validation of shortened C‑BARQ (PLOS ONE, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008875/?utm_source=chatgpt.com)

Что важно:

* В статье есть:

  * CSV-файл (supplementary data)
  * реальные ответы C-BARQ
* Данные:

  * ~435 собак
  * сопоставление полной и короткой версии

👉 Это **один из немногих реально открытых C-BARQ датасетов**

---

## ✅ 2.2. Dog Aging Project (DAP)

* Портал: [Dog Aging Project open data access](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008875/?utm_source=chatgpt.com)

Особенности:

* включает C-BARQ как часть опросов
* данные:

  * анонимизированы
  * доступны через **заявку / open portal**
* можно получить:

  * поведение
  * демографию
  * здоровье

👉 Это сейчас **лучший источник open-ish данных с C-BARQ**

---

## ✅ 2.3. Morris Animal Foundation Data Commons

* [Behavior Data Commons (C‑BARQ-based)](https://datacommons.morrisanimalfoundation.org/behavior-data?utm_source=chatgpt.com)

Что доступно:

* сырые данные (по годам)
* агрегированные показатели
* сравнение с общей базой C-BARQ

👉 Это **частично открытая инфраструктура**, но:

* не полный оригинальный датасет
* доступ может требовать регистрацию

---

# 🔬 3. Что обычно делают исследователи

Почти все публикации с C-BARQ используют:

### ✔ 3 модели доступа:

1. **Прямой доступ через UPenn (Serpell lab)**
2. **Собственные выборки (локальные C-BARQ опросы)**
3. **Вторичные открытые когорты (DAP, foundation data)**

👉 Поэтому:

* в статьях почти всегда:

  * ❌ нет полного raw dataset
  * ✔ есть агрегаты или subset

---

# 📉 4. Почему нет полного open dataset?

Основные причины:

### 1. Приватность

* данные связаны с владельцами и условиями содержания ([vetapps.vet.upenn.edu][2])

### 2. Лицензирование инструмента

* C-BARQ — валидированный инструмент (quasi-proprietary)

### 3. Научный контроль

* база используется для ongoing research проектов

---

# 📌 Вывод (важно)

* ❌ **Полного открытого датасета C-BARQ (как, например, Kaggle) — не существует**
* ✔ Но есть:

  * **open subsets (PLOS supplements)**
  * **крупные когорты с доступом по заявке (Dog Aging Project)**
  * **частично открытые репозитории (Morris Foundation)**


[1]: https://vetapps.vet.upenn.edu/cbarq/about.cfm?utm_source=chatgpt.com "About the C-BARQ - C-BARQ: Canine Behavioral Assessment & Research Questionnaire"
[2]: https://vetapps.vet.upenn.edu/cbarq/privacy-policy.cfm?utm_source=chatgpt.com "Privacy Policy - C-BARQ: Canine Behavioral Assessment & Research Questionnaire"

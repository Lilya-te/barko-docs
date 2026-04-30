# Датасеты в `datasets`

## Быстрый статус по C-BARQ

- **Полностью C-BARQ:** `2017_wolfram.csv`, `Dataset_CBARQ.xlsx`, `CBARQ.dat`
- **Частично C-BARQ:** `md1_data/` (содержит блок C-BARQ + отдельные экспериментальные данные ManyDogs 1)

## 1) `2017_wolfram.csv`
- **Источник загрузки (Firefox):** `https://www.wolframcloud.com/objects/342da588-d5f2-461e-9255-77a3e69a5fee`
- **Страница ресурса:** [Wolfram Data Repository — C-BARQ Survey](https://datarepository.wolframcloud.com/resources/C-BARQ-Survey)
- **Краткое описание ресурса:** датасет C-BARQ (Canine Behavioral Assessment and Research Questionnaire) с поведенческими метриками собак (агрессия, страх, обучаемость, энергичность и др.); в репозитории Wolfram указан табличный формат и возможность выгрузки в CSV.
- **Проверка на C-BARQ:** да. Поля `StrangerDirectedAggression`, `Trainability`, `SeparationRelatedBehavior`, `EnergyLevel` и др. соответствуют шкалам C-BARQ (агрегированные доменные оценки по вопросам опросника).
- **Количество строк:** 12 060
- **Размер файла:** 1 679 847 байт (~1.60 MB)

## 2) `Dataset_CBARQ.xlsx`
- **Источник загрузки (Firefox):** `https://researchdata.cab.unipd.it/808/1/Dataset_CBARQ.xlsx`
- **Страница ресурса:** [Canine Behaviour and Research Questionnaire (C-BARQ): validation of the Italian translation](https://researchdata.cab.unipd.it/808/)
- **Краткое описание ресурса:** набор данных, опубликованный в архиве University of Padova CAB Research Data в рамках работы по валидации итальянского перевода C-BARQ.
- **Проверка на C-BARQ:** да. В заголовках присутствуют пункты вида `@1`, `@2`, ... с формулировками вопросов анкеты (итальянская версия C-BARQ).
- **Количество строк:** 807 строк в листе Excel
- **Размер файла:** 392 384 байт (~0.37 MB)

## 3) `CBARQ.dat`
- **Источник загрузки (Firefox):** временная подписанная ссылка S3 вида `https://s3-eu-west-1.amazonaws.com/pfigshare-u-files/.../CBARQ.dat?...`
- **Страница ресурса:** [Figshare — C-BARQ survey on dog behavior and temperament](https://figshare.com/articles/dataset/C_BARQ_survey_on_dog_behavior_and_temperament/715896)
- **Краткое описание ресурса:** данные опросника C-BARQ о поведении и темпераменте собак (в т.ч. показатели агрессии, страха, обучаемости и др.), опубликованные на Figshare.
- **Проверка на C-BARQ:** да. Столбцы `strangeraggr`, `owneraggr`, `dogaggr`, `trainability`, `excitability` и др. — это домены/шкалы C-BARQ, рассчитанные из вопросов анкеты.
- **Количество строк:** 12 061
- **Размер файла:** 1 017 292 байт (~0.97 MB)

## 4) `md1_data/` (репозиторий с датасетом ManyDogs 1)
- **Источник:** [GitHub — ManyDogsProject/md1_data](https://github.com/ManyDogsProject/md1_data) (из `origin` локального git-репозитория)
- **Краткое описание ресурса:** полные данные и воспроизводимые материалы проекта ManyDogs 1; основной файл содержит записи по 704 собакам, протестированным в задаче выбора объекта в нескольких экспериментальных условиях.
- **Связанная публикация/DOI:** [10.5334/jopd.109](https://doi.org/10.5334/jopd.109)
- **Проверка на C-BARQ:** частично. Файл содержит большой блок переменных C-BARQ (`cbarq_train_*`, `cbarq_aggression_*`, `cbarq_fear_*` и т.д.), но также включает не-C-BARQ данные эксперимента (`onecup_*`, `twocup_*`, `ostensive_*`, `odor_*` и др.).
- **Количество строк (основной файл `manydogs_etal_2024_data.csv`):** 705
- **Размер (основной файл `manydogs_etal_2024_data.csv`):** 898 185 байт (~0.86 MB)
- **Размер папки `md1_data/` целиком:** 3 910 781 байт (~3.73 MB)

## 5) file - pone.0299973.s001.csv [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008875/)


## Кандидаты на источники данных

- [Dog Aging Project — Data Access](https://dogagingproject.org/data-access)  
  Проект Dog Aging Project собирает долгосрочные данные о здоровье, образе жизни и поведении собак для исследований старения; раздел Data Access описывает правила и способы получения исследовательских данных проекта.

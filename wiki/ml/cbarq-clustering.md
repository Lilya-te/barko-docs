---
type: ml
tags: [c-barq, clustering, padova, kmeans, gmm, exploratory, k3]
sources: [cbarq-clustering-notebooks, padova-cbarq-italian]
updated: 2026-07-18
status: draft
---

# C-BARQ clustering — Padova

Exploratory-кластеризация 775 очищенных анкет Padova по 13 стандартизированным
доменным шкалам C-BARQ. Это подготовительный анализ данных, а не K3 baseline и не
оценка риска возврата.

## Результаты

| Модель | Подбор `k` | Выбранное `k` | Качество / критерий | Вывод |
|---|---|---:|---|---|
| `KMeans` | `k=2…8` по максимуму silhouette | 2 | `silhouette=0.190` | Грубое, слабо разделённое деление; кластеры 244 и 531 собак |
| `GaussianMixture` (`diag`) | `k=2…8` по минимуму BIC | 6 | BIC `15 463.26`, silhouette `−0.02` | BIC предпочитает более сложную смесь, но геометрическое разделение слабое |

В KMeans-кластере 0 выше средние значения по stranger-/dog-directed aggression,
разным видам fear, separation-related behavior и excitability, чем в кластере 1.
Это описательная разница профилей, не клиническая и не продуктовая классификация.

## Что можно использовать

- Проверить кластеры как сегменты для EDA и как кандидаты на вспомогательные
  признаки после строгой валидации.
- Использовать рабочий срез как свидетельство того, что Padova можно агрегировать
  из item-level ответов в доменные признаки — см. [data-harmonization](../concepts/data-harmonization.md).

## Чего пока нельзя утверждать

- Что существует шесть устойчивых поведенческих типов: отрицательный silhouette
  GMM этого не подтверждает.
- Что кластер равен «high-risk»: для этого нужен независимо определённый target и
  supervised validation.
- Что KMeans и GMM согласуются: ноутбук сравнения пока не содержит расчётов.

## Следующий шаг

1. В `21_clusters_compare.ipynb` обучить обе модели при `k=2` и `k=6`.
2. Сопоставить разметки contingency table и `Adjusted Rand Index` / `NMI`.
3. Оценить устойчивость к resampling и варианту preprocessing.
4. Только затем проверять связь кластеров с внешним K3-target.

## Ссылки

- [cbarq-clustering-notebooks](../sources/cbarq-clustering-notebooks.md)
- [padova-cbarq-italian](../datasets/padova-cbarq-italian.md)
- [k3-risk-prediction](../components/k3-risk-prediction.md)

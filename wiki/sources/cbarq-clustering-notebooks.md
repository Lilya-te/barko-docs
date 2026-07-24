---
type: source
tags: [c-barq, clustering, padova, kmeans, gmm, source]
sources: [padova-cbarq-italian]
raw_paths:
  - analytics/research/notebooks/11_kmeans_cluster.ipynb
  - analytics/research/notebooks/12_gmm_cluster.ipynb
  - analytics/research/notebooks/21_clusters_compare.ipynb
updated: 2026-07-18
status: ingested
---

# Source: кластеризация C-BARQ на Padova

**Исходные файлы:** исследовательские ноутбуки KMeans, GMM и запланированного
сравнения кластеров.

## Что выполнено

- На очищенном срезе Padova: **775 собак**, **13 доменных шкал** C-BARQ,
  масштабированных перед кластеризацией.
- `KMeans` перебирает `k = 2…8`; максимум `silhouette_score` — при `k=2`
  (`0.190`). Размеры кластеров: 244 и 531.
- `GaussianMixture` с `covariance_type="diag"` и `k = 2…8` выбирает `k=6` по
  минимальному BIC (`15 463.26`); silhouette для этого решения `−0.02`.
- Экспортированы рабочие таблицы с метками: `df_domains_kmeans.csv` и
  `df_domains_gmm.csv` (по 775 строк).

## Интерпретация и ограничения

- KMeans выделяет грубое разделение профилей: первый кластер имеет более высокие
  средние по агрессии, страху, separation-related behavior и excitability.
- `silhouette=0.190` — слабая, а не хорошо отделённая структура; GMM-решение с
  шестью компонентами по BIC при отрицательном silhouette тем более нельзя
  интерпретировать как устойчивые естественные типы собак.
- Кластеры — exploratory-профили и возможные вспомогательные признаки K3, но не
  label «сложной адаптации» и не результат supervised baseline.
- Ноутбук `21_clusters_compare.ipynb` пока содержит только план сравнить KMeans
  и GMM для 2 и 6 кластеров; пересечение/согласие разметок ещё не рассчитано.

## Интегрировано в вики

- [cbarq-clustering](../ml/cbarq-clustering.md) — результаты и следующий шаг.
- [data-harmonization](../concepts/data-harmonization.md) — статус агрегации
  item-level Padova в доменные шкалы.
- [k3-risk-prediction](../components/k3-risk-prediction.md) — граница между
  exploratory clustering и target K3.

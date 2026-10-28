# C-BARQ research pipeline (Padova)

Структура каталога. Ноутбуки пока ссылаются на старые пути в корне `research/` — обновить `PATHS` при рефакторинге ячеек.

## Порядок запуска (целевой)

| # | Ноутбук | Выход |
|---|---------|-------|
| 1 | `notebooks/01_cbarq_clean.ipynb` | `artifacts/csv/clean/`, `artifacts/json/domain_items.json` |
| 2 | `notebooks/02_domains_scale.ipynb` | `artifacts/csv/scaled/`, `artifacts/models/domain_scaler.joblib` |
| 3 | `notebooks/03_kmeans_cluster.ipynb` | `artifacts/csv/clusters/df_domains_kmeans.csv` |
| 4 | `notebooks/04_gmm_cluster.ipynb` | `artifacts/csv/clusters/df_domains_gmm.csv` |
| 5 | `notebooks/05_clusters_compare.ipynb` | `artifacts/json/cluster_comparison.json` |

Шаги 3 и 4 независимы (после шага 2). Шаг 5 требует 3 и 4.

## Дерево

```
research/
├── raw/padova-cbarq/          # исходники (read-only)
├── notebooks/                 # ноутбуки 01..05
└── artifacts/
    ├── csv/clean/             # очищенные таблицы
    ├── csv/scaled/            # z-score домены
    ├── csv/clusters/          # метки кластеров
    ├── json/                  # domain_items.json, artifact_paths.json, cluster_comparison.json
    └── models/                # domain_scaler.joblib
```

## Текущее состояние

- Есть: `01_cbarq_clean`, `03_kmeans_cluster`
- Планируются: `02_domains_scale`, `04_gmm_cluster`, `05_clusters_compare`
- Wiki: [padova-cbarq-column-dictionary.md](../../wiki/datasets/padova-cbarq-column-dictionary.md)

## Заметки

- `raw/padova-cbarq/Dataset_22022022_alt.csv` — копия из корня `research/` (отличается от основного файла в `Dataset_CBARQ/`).
- `artifacts/csv/clean/cbarq_clean.csv` и `df_cbarq_clean.csv` — оба сохранены (содержимое различается); каноническое имя по плану: `df_cbarq_clean.csv`.

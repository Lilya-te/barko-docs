---
type: source
tags: [helpdog, eda, source, adoption]
sources: []
raw_path: analytics/helpdog.ipynb
updated: 2026-06-09
status: ingested
---

# Source: HelpDog Adoption EDA

**Исходный файл:** [`analytics/helpdog.ipynb`](../../analytics/helpdog.ipynb)

**Связанные данные:** `analytics/dogs.csv`, `analytics/adoptions.csv`

## Что делает ноутбук

Exploratory analysis истории пристройств собак с форума [HelpDog](https://helpdog.ru). **ML-модели не обучаются**, метрики ROC-AUC не считаются.

## Ключевые выводы

1. **90 собак** на форуме (`dogs.csv`).
2. **46 собак** пристроены хотя бы раз (`home_started_at` не пуст).
3. После очистки истории пристроек: **26 собак** вернулись в приют ≥1 раз.
4. **~57%** пристроенных собак возвращались в приют (26/46).
5. Очистка данных: для собак с несколькими пристройствами удаляются промежуточные записи без возврата; сохраняется последнее пристройство или запись с возвратом.

## Интегрировано в вики

| Тема | Страница |
|------|----------|
| Датасет | [helpdog-forum-adoptions](../datasets/helpdog-forum-adoptions.md) |
| EDA-выводы | [helpdog-adoption-eda](../ml/helpdog-adoption-eda.md) |
| Кандидат на таргет K3 | [adoption-return](../concepts/adoption-return.md) |
| K3 | [k3-risk-prediction](../components/k3-risk-prediction.md) |

## Не перенесено / требует уточнения

- [ ] Связка собак HelpDog с признаками C-BARQ (пока нет общих features).
- [ ] Парсинг текста `поступление` / `пристройство` / `возврат` для дополнительных признаков.
- [ ] Обучение baseline-моделей K3 на этих данных.
- [ ] Использование `forum_data.csv` (в ноутбуке не задействован).

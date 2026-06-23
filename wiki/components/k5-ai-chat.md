---
type: component
tags: [k5, llm, rag, mvp, safety]
sources: [ml-ideas-notes, fomina-2024-problem-behavior-review, gritsenko-2023-owner-frustration]
updated: 2026-06-09
status: draft
---

# K5 — ИИ-чат

Дополнительная AI-задача MVP: чат с опорой на экспертную базу.

## Постановка

Не обучать LLM с нуля, а обеспечить:
- **grounded-ответы** (привязка к источникам);
- **безопасность** (гуманная кинология, red flags).

## Стратегия

**Готовая LLM через API + RAG** — постоянная стратегия, не временный костыль.

### Quality control

- Retrieval quality (`Recall@k`, корректные источники)
- Prompt-policy
- Red-flag rules
- Human-reviewed knowledge base

### Развитие (без обучения собственной LLM)

- Качество базы знаний
- Маршрутизация контекста
- Контроль безопасности
- Мониторинг метрик

## База знаний

- Источник: литература **гуманной кинологии** + ingested статьи из `статьи/`.
- Wiki-слой (`wiki/`) — curated база для RAG; сырые PDF — только для верификации.
- Лицензирование: потребуется покупка лицензий на книги; статьи — проверить права на RAG.

### Ingested источники (стартовая KB)

| Тема | Страница |
|------|----------|
| Обзор проблемного поведения, диада, избегание аверсивных методов | [fomina-2024](../sources/fomina-2024-problem-behavior-review.md) |
| Типы привязанности | [owner-dog-attachment](../concepts/owner-dog-attachment.md) |
| Разочарованность владельца, агрессия, возбудимость | [gritsenko-2023](../sources/gritsenko-2023-owner-frustration.md) |
| Проблемное vs нежелательное поведение | [problem-behavior-taxonomy](../concepts/problem-behavior-taxonomy.md) |

## Идея multi-model pipeline

Рассматривается разделение на несколько моделей/этапов:
1. Ответ на вопрос пользователя
2. Проверка на гуманность ответа
3. Детекция проблем со здоровьем

## MVP vs следующий этап

| Этап | Решение |
|------|---------|
| MVP | Существующая LLM API + RAG |
| Следующий этап | Улучшение RAG-пайплайна, промптов, safety-правил, экспертной базы |

## Метрики

См. [benchmarks-and-metrics](../ml/benchmarks-and-metrics.md#k5-llm--rag).

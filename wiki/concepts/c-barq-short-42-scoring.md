---
type: concept
tags: [c-barq, questionnaire, scoring]
sources: [c-barq, pilot-questionnaire]
updated: 2026-10-04
status: draft
---

# Скоринг Mini C-BARQ / C-BARQ(S), 42 пункта

Метод, по которому ответы 42 пунктов группируются в 14 субшкал и усредняются. Источник формул — инструкция Mini C-BARQ (Serpell): каждая субшкала — среднее небольшого набора пунктов со шкалой 0–4.

Номера в формулах совпадают с номерами пилотной анкеты и с английским C-BARQ(S) (`QUESTS/CBARQ_short-final_copy.pdf`). С 2026-10-04 пункты 8 и 9 в форме стоят в том же порядке, что в short-PDF. Состав пунктов: [pilot-questionnaire](pilot-questionnaire.md). Short↔full: [`QUESTS/c-barq-short-full-mapping.md`](../../QUESTS/c-barq-short-full-mapping.md).

## Кодирование ответа

Пункты — шкалы тяжести (агрессия, страх, возбудимость) или частоты. В анкете тяжесть уже пронумерована 0–4. Частота кодируется так:

| Ответ | Балл |
|-------|-----:|
| Never / Нет, никогда | 0 |
| Seldom / Редко | 1 |
| Sometimes / Иногда | 2 |
| Usually / Обычно | 3 |
| Always / Всегда | 4 |

Исключение — только пункты **27 и 28** (сразу выполняет «сидеть» и «жди»). Для них порядок обратный: Never = 4, Seldom = 3, Sometimes = 2, Usually = 1, Always = 0. Пункт 29 («легко отвлекается») не обращается.

Инструкция не говорит, что делать с «Не наблюдалось или неприменимо». В формулах делитель фиксированный.

## 14 субшкал

| Субшкала | Формула |
|----------|---------|
| Excitability | (1 + 2) / 2 |
| Stranger-directed aggression | (3 + 6 + 9) / 3 |
| Owner-directed aggression | (4 + 5 + 7) / 3 |
| Dog-directed aggression | (8 + 10) / 2 |
| Familiar dog aggression (dog rivalry) | (11 + 12) / 2 |
| Stranger-directed fear | (13 + 15) / 2 |
| Nonsocial fear | (14 + 16 + 18) / 3 |
| Dog-directed fear | (17 + 19) / 2 |
| Touch sensitivity | (20 + 21) / 2 |
| Separation-related behavior | (22 + 23 + 24) / 3 |
| Attachment and attention-seeking | (25 + 26) / 2 |
| Training difficulty | (27 + 28 + 29) / 3, пункты 27 и 28 с обратным баллом |
| Chasing | (30 + 31) / 2 |
| Energy level | (39 + 40) / 2 |

Пункт 8 — незнакомая собака на поводке (dog-directed aggression). Пункт 9 — незнакомцы мимо дома (stranger-directed aggression).

## Прочие 9 пунктов

Пункты, не вошедшие в субшкалы, по инструкции необязательны и при сохранении считаются **по отдельности**, 0–4, без усреднения: 32, 33, 34, 35, 36, 37, 38, 41, 42 (побег, порча вещей, тянет поводок, метки в доме, мочится одна, испражняется одна, гиперактивность, гоняется за хвостом, устойчивый лай). Пункты 39 и 40 в этот список не входят: они дают Energy level.

## Связанные страницы

- [c-barq](c-barq.md)
- [pilot-questionnaire](pilot-questionnaire.md)
- [k3-feature-candidates](k3-feature-candidates.md)

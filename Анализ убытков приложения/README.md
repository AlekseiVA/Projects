# Анализ убытков приложения

Проведен анализ данных от ProcrastinatePRO+.
Рассчитаны различные метрики, использован когортный анализ: LTV, CAC, Retention rate, DAU, WAU, MAU и т.д. Использованы уже написанные ранее функции расчёта метрик. Сделаны правильные выводы по полученным данным.

**Типы данных:** int, object, datetime

**Задачи проекта:**
Несмотря на огромные вложения в рекламу, последние несколько месяцев компания терпит убытки. Задача — разобраться в причинах и помочь компании выйти в плюс.  

**Результат исследования:**  

* По странам лидирует United States, на нее приходится большая часть пользователей по количеству и доля платящих тоже выше (6.90%), чем у остальных стран. Остальные страны показывают около 4%

* Устройства показывают похожую конверсию, а вот по количеству платящих пользователей Iphone на первом месте

* По рекламным источникам можно выделить 3 канала, у которых высокая конверсия в платящего пользовтеля: FaceBoom, AdNonSense и lambdaMediaAds

* По количеству: FaceBoom, TipTop и WahooNetBanner

Причины неэффективности привлечения пользователей  

* С 5 мая 2019 года мы видим, что больше всего трат идет на 2 рекламных канала: TipTop и FaceBoom, которые при этом не окупаются. TipTop на первом месте по тратам и на самом последнем месте ROI

* C регионами похожая картина, есть страна, в которой самый большой бюджет и при этом, которая единственная не окупается: United States

* Также есть 2 устройства, в которых реклама не окупается: Mac и Iphone


Рекомендации для отдела маркетинга

* Уменьшить бюджет в United States и в каналах: TipTop и FaceBoom, нужно, чтобы экономика сошлась, пока бюджет выше эффективности, которую дают нам пользователи по эти источникам и стране

* Также, стоит обратить внимание на lambdaMediaAds - у него хороший LTV, окупается реклама и большая доля платящих пользователей

* Из стран больше всего ROI у UK, при этом затраты на рекламу средние

* Устройства, на которые стоит обратить внимание: PC и Android

**Инструменты:**
- Python
- Pandas
- Matplotlib
- Seaborn

**Навыки:**  

- Когортный анализ
- Юнит-экономика
- Продуктовые метрики

**Сфера деятельности:**
- Стартапы
- Инвестиции

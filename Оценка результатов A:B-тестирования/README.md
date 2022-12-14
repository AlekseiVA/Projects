# Оценка результатов A/B-тестирования
Проведена оценка результатов A/B-теста, оценена корректность проведения теста: пересечение тестовой аудитории с конкурирующим тестом и совпадение с маркетинговыми событиями, другие проблемы временных границ теста  

**Типы данных:** object, datetime

**Задачи проекта:**
Провести оценку результатов A/B-теста. В распоряжении есть датасет с действиями пользователей, техническое задание и несколько вспомогательных датасетов.

**Результат исследования:**  
Оценка корректности проведения теста:

* Группа A больше почти на 1000 пользователей группы B
* 1602 пользователя учавствовали в конкурирующем A/B-тесте
* Нам в данных не хватает 5 дней, либо мы подглядываем, что не хорошо, либо нам дали не все данные
* В момент тестирования были запущены 2 маркетинговые активности  
*Поэтому доверять результатам исследования не стоит, так как далеко не все правила ТЗ были исполнены*   

Значимая статистическая разница в конверсии групп А и В присутствует только для события product_page  
Но как показывает конверсия, изменения только ухудшили результаты  
Поэтому оснований считать изменения, связанные с внедрением улучшенной рекомендательной системы, успешными нет  
Лучше остаться на прошлом варианте до изменения или провести A/B тестирование заново, но строго по ТЗ, так как были допущены ошибки  

**Инструменты:**
- Python
- Pandas
- Matplotlib
- SciPy
- Seaborn

**Навыки:**  

- A/B-тестирование
- Проверка статистических гипотез

**Сфера деятельности:**
- Интернет-сервисы

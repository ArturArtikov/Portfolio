# Project 2. Анализ вакансий из HeadHunter

## Оглавление
[1. Описание проекта](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Описание-проекта)

[2. Какой кейс решаем](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Результаты)

[6. Выводы](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Выводы)

### Описание проекта
Провести анализ вакансий, предоставленных с сайта HeadHunter. Узнать информацию о компаниях, количестве их рабочих сфер,
вакансиях и предлагаемой заработной плате.

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

### Какой кейс решаем
Используя данные из 4 таблиц (и одной дополнительной) получить информацию о работодателях. Разобраться в регионах вакансий, компаниях с наибольшим количеством вакансий,
а также сферах работы компаний и требований по ключевым навыкам к соискателям.

**Что практикуем**
1. Умение работать с библиотекой Pandas для получения данных
2. Умение работать с библиотекой psycopg2 для считывания данных из удаленного источника
3. Навык написания SQL-запросов, при помощи f-строк
4. Навык использования агрегирующих функций в SQL
5. Навыки соединения таблиц (join, left join)
6. Навыки объединения таблиц (union, union all)
7. Умение получать выводы из данных без построения графиков

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

### Краткая информация о данных
Таблица VACANCIES - данные о вакансиях. Основная таблица для анализа.

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_2.png)

Таблица AREAS - данные о регионах и их названиях. Связана с таблицей VACANCIES, через VACANCIES.area_id = AREAS.id
![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_3.png)

Таблица EMPLOYERS - данные о работодателях, их ID и регионе. Связана с таблицей VACANCIES, через VACANCIES.employer_id = EMPLOYERS.id
![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d2a26db623c75572c71923b57241e038/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_4.png)

Таблица EMPLOYERS_INDUSTRIES - образует связь между таблицами EMPLOYERS и INDUSTRIES. Связана с таблицей EMPLOYERS, через EMPLOYERS_INDUSTRIES.employer_id = EMPLOYERS.id 
и с таблицей INDUSTRIES, через EMPLOYERS_INDUSTRIES.industry_id = INDUSTRIES.id
![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/16ff3df0bb0ddecd922562f3c4bdd32c/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_6.png)

Таблица INDUSTRIES - данные о сферах деятельности работодателей. Связана с таблицей EMPLOYERS_INDUSTRIES, через INDUSTRIES.id = EMPLOYERS_INDUSTRIES.industry_id
![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2c76bca09937a1a05a9e66d51008e298/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_5.png)

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

### Этапы работы над проектом

1. Установление связи с внешним источником, при помощи библиотеки psycopg2
2. Предварительный анализ данных (анализ количества записей в каждой из таблиц и пр.)
3. Детальный анализ вакансий (анализ количества вакансий по регионам, а также информации в данных вакансиях и пр.)
4. Анализ работодателей (анализ того, какие вакансии публикуют работодатели, в каких регионах и какие у работодателей сферы деятельности и пр.)
5. Предметный анализ (получение вакансий, относящихся к Data Science, получение числа ключевых навыков для вакансий и пр.)
6. Дополнительный анализ (зависимость среднего значения заработной платы по городам, а также получение списка компаний по числу их сфер деятельности)
7. Общий вывод по анализу
8. Выкладка работы на GitHub

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

### Результаты
Получены списки выводов, которые могут помочь соискателям в поиске работы, а также работодателям в выкладке вакансий, на основе собранной информации.

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

### Выводы
На основании проделанной работы получена информация о работодателях и вакансиях, которая может быть в дальнейшем использована для учлучшения рекомендательной системы вакансий соискателям
и помощи работодателям в написании четкого описания вакансии.

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter/README.md#Оглавление)

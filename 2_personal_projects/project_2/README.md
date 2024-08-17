# Проект №2. Анализ вакансий из HeadHunter

## Какой кейс решаем
<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project2.jpg" height=150 align="left"> 

У нас на руках есть данные о вакансиях, городах, списке работодателей и их сферах деятельности. Необходимо объединить, очистить и преобразовать данные таким образом, чтобы понять на что обращают внимание работодатели и какими навыками должны обладать соискатели, чтобы претендовать на ту или иную вакансию.


## Краткая информация о данных
Таблица VACANCIES - данные о вакансиях. Основная таблица для анализа.

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_2.png)

Таблица AREAS - данные о регионах и их названиях

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_3.png)

Таблица EMPLOYERS - данные о работодателях, их ID и регионе

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d2a26db623c75572c71923b57241e038/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_4.png)

Таблица EMPLOYERS_INDUSTRIES - образует связь между таблицами EMPLOYERS и INDUSTRIES

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/16ff3df0bb0ddecd922562f3c4bdd32c/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_6.png)

Таблица INDUSTRIES - данные о сферах деятельности работодателей

![](https://lms-cdn.skillfactory.ru/assets/courseware/v1/2c76bca09937a1a05a9e66d51008e298/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_5.png)


## Этапы работы над проектом

1. Установление связи с внешним источником, при помощи библиотеки psycopg2
2. Предварительный анализ данных (анализ количества записей в каждой из таблиц и пр.)
3. Детальный анализ вакансий (анализ количества вакансий по регионам, а также информации в данных вакансиях и пр.)
4. Анализ работодателей (анализ того, какие вакансии публикуют работодатели, в каких регионах и какие у работодателей сферы деятельности и пр.)
5. Предметный анализ (получение вакансий, относящихся к Data Science, получение числа ключевых навыков для вакансий и пр.)
6. Дополнительный анализ (зависимость среднего значения заработной платы по городам, а также получение списка компаний по числу их сфер деятельности)
7. Общий вывод по анализу
8. Выкладка работы на GitHub


## Результаты
Получены списки выводов, которые могут помочь соискателям в поиске работы, а также работодателям в выкладке вакансий, на основе собранной информации.


## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-%23ffffff.svg?style=for-the-badge)
![Psycopg2](https://img.shields.io/badge/psycopg2-%23fcd703.svg?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-%23636970.svg?style=for-the-badge)

[Вернуться в главное меню](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

# Changellenge Cup Russia 2024

## Краткое описание

[//]: # "Фото с изображением хакатона"

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/3_case_championships_projects/case_projects3.png" height=200 align="left"> 

__Кейс:__ Международный дебют, кейс от компании LAB Industries

__Задача:__ Разработать стратегию запуска нового бренда LAB Industries в категориях средств для окрашивания, стайлинга, или ухода за волосами на рынке одной из стран Центральной Азии - Азербайджана, Аремнии, Грузии, Казахстана, Киргизии, Таджикистана, Узбекистана, Туркмнистана - со сроком реализации до 2026 года

__Организаторы:__ Changellenge & Lab Industries (ex. Henkel)

__Результат:__ Разработака и предложение подхода к созданию рекомендательной системы, способной оптимизировать наличие и расположение товаров на полках

__Сфера применения:__ Парфюмерно-косметическая продукция

<br/>

## Входные данные

*Все данные являются конфиденциальными, а кейс принадлежит компании-составителю, поэтому приложение ссылок на данные и описание кейса невозможно ввиду ограничения со стороны правообладателя в лице компании Changellenge*

* pos_general.csv - фактические данные о POS (точках продаж). Одна транзакция — одна строка (объект)
* prod_dim.csv - мастер-данные по продуктам (DIM), перечень исключительно продуктов P&G
* site_dim.csv - мастер-данные по магазинам (DIM), перечень всех магазинов, в которые отгружаются товары P&G и каким клиентам они принадлежат
* cust_dim.csv - мастер-данные по клиентам (DIM), перечень всех клиентов P&G, вместо наименований клиентов хранятся зашифрованные значения в виде хешей (hash)
* cust_dim_hash.csv - вспомогательная расшифровка хешей для клиентов
* shipments.csv - данные по отгрузкам по времени и магазинам

<br/>

## Этапы работы над проектом

1. Получение всех доступных данных
2. Создание рабочего пространства в Google Colab и Drive
3. Визуализация данных о точках продаж
4. Визуализация данных об отгрузках
5. Объединение данных с целью поиска сочетаний популярных продуктов
6. Нахождение среднего чека по сочетаниям продуктов
7. Агрегация данных с помощью SQL
8. Проведение ABC-XYZ анализа
9. Разработка концепции планограммы стелажа
10. Создание визуального представления планограммы стелажа
11. Описание унифицированной планограммы магазина
12. Предложение вариантов рекомендательной системы: расположение товаров по типу и фирме
13. Описание будущего применения библиотеки OpenCV для решения задачи
14. Создание презентации
15. Публикация презентации в качестве решения (защита не предусмотрена)

<br/>

## Сроки и результаты

__Сроки:__ 11.03.2024 - 17.03.2024 (1-ый этап), 02.04.2024 - онлайн финал

__Результат:__ [презентация](https://github.com/ArturArtikov/Portfolio/blob/main/4_case_championships_projects/case_2/Changellenge%20Cup%20IT.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%20%D0%9A%D0%B5%D0%B9%D1%81%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8%20Procter%20and%20Gamble.%20%D0%9F%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F.%20%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0%20New%20challenge.pdf) решения кейса со всем необходимым описанием

__Возможные улучшения:__ создание рекомендательной модели на основе Python-библиотек OpenCV, TensorFlow, PyTorch

__Итоговый результат:__ оценка выполненной работы в виде показателя HQA (High Quality Awards)

__Сертификат|Диплом:__ [Диплом High Quality Awards](https://github.com/ArturArtikov/Portfolio/blob/main/1_media/4_certificates/Changellenge%20Cup%20IT%20-%202024.%20%D0%94%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC%20HQA.%20%D0%90%D1%80%D1%82%D1%83%D1%80%20%D0%90%D1%80%D1%82%D0%B8%D0%BA%D0%BE%D0%B2.pdf)

<br/>

## Командный состав

Команда: __New challenge__

Список участников команды:

* [Косицына Евгения](https://t.me/QEvgesha) - Капитан команды | Data Analyst
* [Артиков Артур](https://t.me/ArturArtikov) - Data Scientist | Data Analyst
* [Шевченко Андрей](https://t.me/drynya_7) - Backend Python Developer
* Галенда Семен - Data Analyst | Designer
* Самсонова Александра - Slide maker | Designer

<br/>

## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)

[Главная страница портфолио](https://github.com/ArturArtikov/Portfolio/blob/main/README.md)

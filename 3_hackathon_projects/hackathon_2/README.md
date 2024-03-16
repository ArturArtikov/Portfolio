# IT Purple Hack

## Краткое описание

<img src="https://leader-id.storage.yandexcloud.net/upload/342045/2bfaf28f-de99-4e54-aff4-8e995325f5f7.jpg" height=200 align="left"> 

Кейс Альфа-банка. Решение бизнес-задач, связанных с CLTV. 

Задача: Построение модели, которая будет предсказывать продуктовый кластер клиента - Юридического лица на горизонте в 12 месяцев. 

Организаторы: ФПМИ МФТИ & Альфа-банк

Результат: Модель, которая будет выдавать вероятности перехода в каждый из 17 продуктовых кластеров.

Сфера применения: Онлайн-банкинг

<br/>

## Входные данные

* train_data.pqt - тренировочный датасет с данными клиентов, а также информацией о предсказанных конечных классах (не выложен по просьбе Альфа-банка)
* test_data.pqt - тестовый датасет, для которого необходимо получить вероятности попадания клиента в продуктовые кластеры (не выложен по просьбе Альфа-банка)
* [cluster_weights.xlsx](https://github.com/ArturArtikov/Portfolio/blob/main/3_hackathon_projects/hackathon_2/data/cluster_weights.xlsx) - коэффициенты значимости кластеров
* [feature_description.xlsx](https://github.com/ArturArtikov/Portfolio/blob/main/3_hackathon_projects/hackathon_2/data/feature_description.xlsx) - описание признаков датасетов

<br/>

## Этапы работы над проектом

1. Получение всех доступных данных
2. Создание рабочего пространства в Google Colab и Drive
3. Подгрузка данных и работа с ними
4. Статистический анализ данных
5. Визуальный анализ данных
6. Заполнение пропусков в категориальных признаках
7. Заполнение пропусков в числовых признаках
8. Генерация новых признаков
9. Избавление от ненужных признаков, путем построения тепловой карты корреляций
10. Создание модели на LightGBM
11. Написание функций для преоьразования данных
12. Обновление исходных данных, с учетом заполнения пропусков
13. Использование CatBoost для получения результата
14. Отбор признаков для повышения качества модели
15. Наполнение репозитория в GitHub
16. Создание презентации
17. Защита результатов проекта

<br/>

## Сроки и результаты

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/3_hackathon_projects/hackathon_2/files/photo_1.jpg" height=200 align="right"> 

Сроки: 09.03.2024 - 15.03.2024

Результат: файл [submission.csv]() с предсказаниями вероятностей попадания в различные кластеры клиентов банка

Возможные улучшения: дозаполнение данных, более тонкая настройка модели

Итог: 6-ое место по сумме решения, реализации и защиты

Дополнительно: [сертификат участника]()

<br/>

## Командный состав

Команда: __На Хайпе__ | __On Hype__

Список участников:

* [Александр Зеленцов](https://github.com/CHex0K) - Капитан команды | ML-Engineer
* [Никита Юрьев](https://github.com/Serfetto) - Backend Python Developer
* [Артур Артиков](https://github.com/ArturArtikov) - Data Scientist
* [Алексей Безднин](https://github.com/BezdninAlex) - Data Analyst
* [Александра Ишмаева](https://github.com/alexandraishmaeva) - Backend Python Developer

<br/>

## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-%231d2f3e.svg?style=for-the-badge)
![Shap](https://img.shields.io/badge/Shap-%238f37bb.svg?style=for-the-badge)
![CatBoost](https://img.shields.io/badge/CatBoost-%23ffcc00.svg?style=for-the-badge)

[Главная страница портфолио](https://github.com/ArturArtikov/Portfolio/blob/main/README.md)
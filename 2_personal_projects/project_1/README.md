# Проект №1. Анализ резюме из HeadHunter

## Какой кейс решаем
<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project1.png" height=150 align="left">

Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю. Наша задача - преобразовать, исследовать и провести базовую очистку данных, чтобы специалисты компании смогли разработать такую модель.


## Краткая информация о данных

dst-3.0_16_1_hh_database.csv - база данных, содержащая вакансии и отклики по ним

[ExchangeRates.csv](https://github.com/ArturArtikov/Educational_projects/blob/main/Project_1_Analysis_of_resumes_from_HeadHunter/data/ExchangeRates.csv) - база данных, содержащая отношение валют к рублю за необходимый для анализа срок

[hh_database_preprocessed.csv](https://github.com/ArturArtikov/Educational_projects/blob/main/Project_1_Analysis_of_resumes_from_HeadHunter/data/hh_database_preprocessed.csv) - база данных, исходных вакансий с переведенными в рубли заработными платами, а также с измененными значениями столбцов


## Этапы работы над проектом

1. Считывание данных, оценка внешнего вида и проверка корректности данных
2. Изменение данных в столбцах таблицы, создание новых столбцов с признаками
3. Перевод заработных плат соискателей в рубли
4. Поиск взаимосвязей и выбросов в данных, путем построения графиков
5. Очистка данных от выбросов, пробелов и неинформативных признаков


## Результаты
На основании проделанной работы получены очищенные данные, необходимые для предсказания заработных плат соискателей по требуемым признакам.


## Используемый стек и технологии

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

[Вернуться в главное меню](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

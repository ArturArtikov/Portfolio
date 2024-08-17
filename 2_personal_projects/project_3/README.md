# Проект №3. Анализ отзывов отелей с Booking

## Какой кейс решаем
<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project3.png" height=150 align="left"> 

Используя предоставленные таблицы с отзывами об отелях провести анализ отзывов, заполнить пропущенные значения, подготовить данные к обучению модели машинного обучения. Обучить модель, получить список оценок для 128000 отзывов и узнать, насколько они отличаются от реальных.


## Краткая информация о данных

* hotels_train.csv - набор данных для обучения модели

* hotels_test.csv - набор данных для оценки качества модели

* [submission.csv](https://github.com/ArturArtikov/Portfolio/blob/main/2_personal_projects/project_3/submission.csv) -  файл сабмишна в нужном формате (то как должен будет выглядеть результат после предсказания)


## Этапы работы над проектом

1. Подгрузка трех файлов, получение основной информации о них
2. Описание содержимого всех трех файлов
3. Написание плана для работы над проектом
4. Объединение файлов hotels_train.csv и hotels_test.csv
5. Восстановление пропущенных координат через библиотеку Geocoder
6. Исследование данных
7. Визуальный анализ данных
8. Построение графиков и написание выводов к ним
9. Разведывательный анализ данных
10. Получение первой метрики MAPE на необработанных данных
11. Генерация признаков
12. Перевод текстовых признаков в числовые
13. Кодирование признаков
14. Получение общей оценки отеля по отзыву через библиотеку Nltk
15. Очистка данных от текстовых признаков и получение второй метрики MAPE
16. Отбор признаков для построения модели
17. Построение тепловой карты корреляци и списка значимости каждого признака
18. Дополнительное удаление неинформативных признаков и признаков с мультиколлинеарностью
19. Получение финальной метрики MAPE
20. Получение файла-предсказания оценок
21. Публиция результатов на Kaggle
22. Публикация результатов на GitHub


## Результаты

[submission_final.csv](https://github.com/ArturArtikov/Educational_projects/blob/main/Project_3_EDA_and_Feature_Engineering/submission_final.csv) - файл с предсказанными оценками

[Решение на Kaggle](https://www.kaggle.com/arturartikov/artur-artikov-baseline) - решение, а также метрика MAPE, полученная после публикации результатов на Kaggle, равная 12.71075% отклонений от идеальных значений


## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![GeoPy](https://img.shields.io/badge/GeoPy-%23EEE8AA.svg?style=for-the-badge&logo=google-earth&logoColor=#4285F4)
![Category-Encoders](https://img.shields.io/badge/category--encoders-%2300BFFF.svg?style=for-the-badge)
![Nltk](https://img.shields.io/badge/nltk-%235F9EA0.svg?style=for-the-badge)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

[Вернуться в главное меню](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

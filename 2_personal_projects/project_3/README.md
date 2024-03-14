# Project 3. EDA + Feature Engineering

## Оглавление
[1. Описание проекта](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Описание-проекта)

[2. Какой кейс решаем](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Результаты)

[6. Выводы](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Выводы)

### Описание проекта

Построить модель для определения того, является ли отзыв об отеле накрученным или нет. Для определения составить модель, предсказывающую то, какую оценку должен поставить отелю проживающий в зависимости от различных факторов.

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

### Какой кейс решаем

Используя предоставленные таблицы с отзывами об отелях провести анализ отзывов, заполнить пропущенные значения, подготовить данные к обучению модели машинного обучения. Обучить модель, получить список оценок для 128000 отзывов и узнать, насколько они отличаются от реальных.

**Что практикуем**

1. Умение работать с библиотекой Pandas для получения данных
2. Умение объединять данные при помощи библиотеки Pandas с созданием нового признака
3. Умение восстанавливать пропущенные значения с помощью библиотеки Geocoder
4. Умение визуализировать данные с помощью библиотек Pandas и Seaborn (Matplotlib)
5. Умение работать с библиотекой Sklearn
6. Навык генерации признаков из текстового в числовой формат
7. Умение кодировать информацию с помощью библиотеки category_encoders
8. Умение получать оценку об отелей через текстовый отзыв с помощью библиотеки Nltk
9. Умение отбирать признаки для лучшего построения модели машинного обучения
10. Навык нахождения наиболее важных для построения модели признаков

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

### Краткая информация о данных

[hotels_train.csv](https://drive.google.com/file/d/1KPOEfEaNcgZusdGXIL9HfsNEsIuTWHvz/view?usp=sharing) - набор данных для обучения модели

[hotels_test.csv](https://drive.google.com/file/d/13f6NlHlwiK8RIsv06y9r74jJ0KegyxVv/view?usp=sharing) - набор данных для оценки качества модели

[submission.csv](https://drive.google.com/file/d/19yA07dCMnkWQezDLqqfP63ZJi4XaSgLn/view?usp=sharing) -  файл сабмишна в нужном формате (то как должен будет выглядеть результат после предсказания)

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

### Этапы работы над проектом

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

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

### Результаты

[submission_final.csv](https://github.com/ArturArtikov/Educational_projects/blob/main/Project_3_EDA_and_Feature_Engineering/submission_final.csv) - файл с предсказанными оценками

[Решение на Kaggle](https://www.kaggle.com/arturartikov/artur-artikov-baseline) - решение, а также метрика MAPE, полученная после публикации результатов на Kaggle, равная 12.71075% отклонений от идеальных значений

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

### Выводы

На основании проделанной работы построена модель, предсказывающая оценки для отелей, выставляемые пользователями. Полученная модель может быть использована в дальнейшем для поиска отелей, завышающих себе рейтинг, а также для выявления накрученных отзывов

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering/README.md#Оглавление)

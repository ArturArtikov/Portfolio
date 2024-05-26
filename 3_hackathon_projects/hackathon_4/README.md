# RedLab Hack

## Краткое описание 

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/2_hackathon_projects/hackathon4.png" height=200 align="left"> 

**Кейс:** Разработка модели для выявления аномалий во временном ряду

**Задача:** Создать минимальный прототип сервиса на Python, который получает временное окно на входе и по загруженному в БД слепку данных анализирует указанное временное окно

**Организаторы:** Компания RedLab & Акселератор Возможностей МГУ

**Результат:** Сервис, принимающий данные о временном ряду за определенный период и указывающий на выборсы в данных 

**Сфера применения:** интернет-бизнес


<br/>

## Входные данные

* metrics_collector.tsv - файл, содержащий информацию о системе (слепок данных телеметрии), за 1 месяц с шагом в 1 минуту, с указанием названий, числа запросов, времени запросов и других данных необходимых для анализа
* Пояснения к данным.docx - файл с описанием признаков в данных, а также с информацией о метриках и способах их рассчета через ClickHouse и SQL

<br/>

## Этапы работы над проектом

1. Получение всех доступных данных
2. Подгрузка данных, добавление названий колонок
3. Работа с признаками, удаление неинформативных данных
4. Рассчет метрики Web Response и получение файла web_response.csv
5. Рассчет метрики Throughput и получение файла throughput.csv
6. Рассчет метрики Apdex и получение файла apdex.csv
7. Рассчет метрики Error и получение файла error.csv
8. Обработка файлов метрик, получение временных меток
9. Создание программы для выбора окна в данных
10. Преобразование значений данных в файлах метрик
11. Стандартизация всех метрик, для упрощения визуализации
12. Построение 4 предсказаний для метрик на основе IsolationForest библиотеки scikit-learn
13. Построение 4 предсказаний для метрик на основе KNN-алгоритма библиотеки pyod
14. Объединение предсказаний для получения наиболее точного результата
15. Сохранение файлов метрик в формате "дата-значение-предсказание модели"
16. Создание кода для визуализации данных и выбросов с помощью streamlit
17. Создание дополнительно визуализации на основе библиотеки matplotlib
18. Оформление репозитория на Github
19. Создание презентации
20. Защита решения

<br/>

## Сроки и результаты

**Сроки:** 24.05-26.05.2024

**Результат:** Прототип модели, подсвечивающий выбросы в выбранном окне временного ряда

**Возможные улучшения:** автоматизация визуализаций с помощью Strealmit, подключение внешней выгрузки данных и работа с новыми данными, создание нейронной сети, способной предсказывать аномалии в будущем

<br/>

Сроки и результаты

Сроки: 24.05.2024 - 26.05.2024

Результат: прототип модели на Python, подсвечивающий выбросы в данных в некотором временном отрезке, заданном пользователем

Возможные улучшения: использование дополнительных методов предсказания

Итог: 13-ое место по сумме решения, реализации и защиты (из 26 команд)

Дополнительно: [сертификат участника](https://github.com/ArturArtikov/Portfolio/blob/main/1_media/4_certificates/RedLab%20Hack%20-%202024.%20%D0%A1%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%20%D1%83%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%90%D1%80%D1%82%D1%83%D1%80%20%D0%90%D1%80%D1%82%D0%B8%D0%BA%D0%BE%D0%B2.pdf)

</br>

## Командный состав

Команда: __*Golden Path*__

Список участников команды:

* [Артур Артиков](https://github.com/ArturArtikov): Капитан команды | Data Scientist
* [Александр Зеленцов](https://github.com/CHex0K): ML-Engineer
* [Сергей Логинов](https://github.com/Sergey-1221): Fullstack Python Developer

<br/>

## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-%23FFFFFF.svg?style=for-the-badge&logo=streamlit&logoColor=DC143C)
![Pyod](https://img.shields.io/badge/pyod-%23FFD700.svg?style=for-the-badge&logo=pyod&logoColor=white)


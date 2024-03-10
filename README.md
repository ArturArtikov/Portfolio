<h1>Data Science Проекты</h1>

<h2>Общее описание раздела</h2>

В данном разделе приводится общее описание каждого реализованного проекта, а также рассказывается о стеке используемых в каждом проекте технологий. Более подробную информацию о каждом проекте вы можете узнать в соответствующем файле README.md, внутри каждой из папок с проектами.

<nav class="toc">
    <h2>Персональные проекты</h2>
      <a href="#project1">Проект №1. Анализ резюме из HeadHunter</a><br>
      <a href="#project2">Проект №2. Анализ вакансий из HeadHunter</a><br>
      <a href="#project3">Проект №3. Анализ отзывов отелей с Booking</a><br>
    <h2>Проекты с хакатонов</h2>
      <a href="#hackaton1">Хакатон №1. ML TalentMatch</a><br>
    <h2>Проекты с кейс-чемпионатов</h2>
      <a href="#case1">Axenix Business Cup</a><br>
</nav>


<h2>Персональные проекты</h2>
<h3 id="project1">Проект №1. Анализ резюме из HeadHunter</h3>

<h4>Краткое описание проекта</h4>

<p><img src="https://github.com/ArturArtikov/Portfolio/blob/main/media/project1.png" width=250 align="left">
Нашим заказчиком выступает крупнейшая российская компания интернет-рекрутмента - 
<a href="https://hh.ru/">HeadHunter</a>. У нас в руках есть база резюме, выгруженных с сайта. Проблема заключается в том, что часть соискателей не указывает заработную плату, когда составляет резюме. Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю. Наша задача - преобразовать, исследовать и провести базовую очистку данных, чтобы специалисты компании смогли разработать такую модель. 
<br clear=left></p>

<h4>План для достижения цели проекта</h4>

1. Считать данные и провести их базовый анализ
2. Преобразовать столбцы в единый числовой формат
3. Перевести все заработные платы в рублевый эквивалент, основываясь на данных ЦБ
4. Исследовать зависимости в данных
5. Провести базовую очистку данных

<h4>Используемые технологии и инструменты</h4>

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

Ссылка на весь проект целиком - [здесь](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_1_Analysis_of_resumes_from_HeadHunter)




<h3 id="project2">Проект 2. Анализ вакансий из HeadHunter</h3>

<h4>Краткое описание проекта</h4>

<p><img src="https://github.com/ArturArtikov/Portfolio/blob/main/media/project2.jpg" width=250 align="left"> 
Представим, что мы устроились в кадровое агенство. Наша задача - создать модель машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist. У нас на руках есть данные о вакансиях, городах, списке работодателей и их сферах деятельности. Необходимо объединить, очистить и преобразовать данные таким образом, чтобы понять на что обращают внимание работодатели и какими навыками должны обладать соискатели, чтобы претендовать на ту или иную вакансию.
<br clear=left></p>

<h4>План для достижения цели проекта</h4>

1. Подключиться к базе данных компании через библиотеку psycopg2 и PostgreSQL
2. Провести предварительный анализ полученных данных
3. Детально проанализировать вакансии и понять в каких городах есть большее число вакансий и какие у вакансий заработные платы
4. Провести анализ работодателей и понять их потребности и проблемы
5. Предметно проанализировать какие вакансии из базы подходят для начинающего Data Scientist
6. Узнать о том, какие ключевые навыки выделяют работодатели в вакансиях
7. Получить список советов для соискателей и работодателей, по поиску работы/сотрудников на основании предоставленной информации

<h4>План для достижения цели проекта</h4>

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-%23ffffff.svg?style=for-the-badge)
![Psycopg2](https://img.shields.io/badge/psycopg2-%23fcd703.svg?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-%23636970.svg?style=for-the-badge)


Ссылка на весь проект целиком - [здесь](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_2_Analysis_of_vacancies_from_HeadHunter)

<h3 id="project3">Проект 3. Анализ отзывов отелей с Booking</h3>

<h4>Краткое описание проекта</h4>

<p><img src="https://github.com/ArturArtikov/Portfolio/blob/main/media/project3.png" width=250 align="left"> 
Во время выполнения проекта мы представляем себя в роли дата-сайентиста компании Booking. Одна из проблем компании - это отели, которые накручивают себе ретинг. Наша задача - создать модель машинного обучения, которая будет предсказывать рейтинг отеля. В том случае, если значение предсказания и реальной оценки будут сильно отличаться мы будем считать, что отель накрутил себе отзыв. В наших руках данные об отелях, а именно: адрес, дата рецензии, название отеля, страна рецензента, тексты позитивного и негативного отзыва, и.т.д. Всего 17 критериев.
<br clear=left></p>

<h4>План для достижения цели проекта</h4>

1. Считать данные, а также ознакомиться с тем, как должен выглядеть файл Submission
2. Объединить данные тестовой и тренировочной выборок, чтобы работать с одним массивом данных
3. Восстановить пустые значения широты и долготы отеля, используя библиотеку GeoPy
4. Проводим визуальный анализ полного массива данных
5. Проводим разведывательный анализ данных с помощью Sklearn
6. Переводим категориальные признаки в числовые
7. Из текста негативного и позитивного отзыва получаем негативный и позитивный окрас оценки с помощью NLP (библиотека NLTK)
8. Строим матрицу корреляций признаков и отбираем необходимые нам
9. Предсказываем оценки отелей и стремимся свести метрику MAPE к значению менее 13%.

<h4>Используемые технологии и инструменты</h4>

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


Ссылка на весь проект целиком - [здесь](https://github.com/ArturArtikov/Educational_projects/tree/main/Project_3_EDA_and_Feature_Engineering)


<h2> Проекты с хакатонов </h2>

<h3 id="hackaton1"> Хакатон №1. ML TalentMatch </h3>


<p><img src="https://github.com/ArturArtikov/Portfolio/blob/main/media/hackaton1.jpg" width=250 align="left"> 
Разработать и реализовать алгоритм, который будет разбивать информацию, содержащуюся в резюме кандидата по смысловым блокам: образование, опыт работы, навыки и т.д. На выходе должен быть структурированный JSON.Данные предоставляются в виде структурированных резюме кандидатов в произвольном виде (word, pdf…).
<br clear=left></p>


<h2> Проекты с кейс-чемпионатов </h2>
<h3 id="case1">Axenix Business Cup</h3>

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/media/case_projects1.jpg" height=150 align="left">




Дата последнего обновления раздела - 08.03.2024<br>
Макет, написание кода и оформление - Артур Артиков

![Portfolio Header](https://github.com/ArturArtikov/Portfolio/blob/main/1_media/portfolio_header.png)

## Общее описание раздела

В данном разделе приводится общее описание каждого реализованного проекта, а также рассказывается о стеке используемых в каждом проекте технологий. Более подробную информацию о каждом проекте вы можете узнать в соответствующем файле README.md, внутри каждой из папок с проектами.

## Персональные проекты
#### [Проект №1. Анализ резюме из HeadHunter](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проект-1-анализ-резюме-из-headhunter-1)
#### [Проект №2. Анализ вакансий из HeadHunter](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проект-2-анализ-вакансий-из-headhunter-1)
#### [Проект №3. Анализ отзывов отелей с Booking](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проект-3-анализ-отзывов-отелей-с-booking-1)

## Проекты с хакатонов
#### [Хакатон №1. ML TalentMatch](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#хакатон-1-ml-TalentMatch-1)
#### [Хакатон №2. IT Purple Hack](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#хакатон-2-it-purple-hack-1)


## Проекты с кейс-чемпионатов
#### [Кейс-чемпионат №1. Axenix Business Cup](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#кейс-чемпионат-1-axenix-business-cup-1)
#### [Кейс-чемпионат №2. Changellenge Cup IT 2024]()

<br/>
<br/>

## Персональные проекты

### Проект №1. Анализ резюме из HeadHunter

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project1.png" height=150 align="left">

Нашим заказчиком выступает крупнейшая российская компания интернет-рекрутмента - [HeadHunter](https://hh.ru/). У нас в руках есть база резюме, выгруженных с сайта. Проблема заключается в том, что часть соискателей не указывает заработную плату, когда составляет резюме. Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю. Наша задача - преобразовать, исследовать и провести базовую очистку данных, чтобы специалисты компании смогли разработать такую модель. 

#### План для достижения цели проекта 

1. Считать данные и провести их базовый анализ<br>
2. Преобразовать столбцы в единый числовой формат<br>
3. Перевести все заработные платы в рублевый эквивалент, основываясь на данных ЦБ<br>
4. Исследовать зависимости в данных<br>
5. Провести базовую очистку данных<br>

#### Используемые технологии и инструменты
        
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%231F6F70.svg?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

<br/>

### Проект №2. Анализ вакансий из HeadHunter

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project2.jpg" height=150 align="left"> 

Представим, что мы устроились в кадровое агенство. Наша задача - создать модель машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist. У нас на руках есть данные о вакансиях, городах, списке работодателей и их сферах деятельности. Необходимо объединить, очистить и преобразовать данные таким образом, чтобы понять на что обращают внимание работодатели и какими навыками должны обладать соискатели, чтобы претендовать на ту или иную вакансию.

#### План для достижения цели проекта 

1. Подключиться к базе данных компании через библиотеку psycopg2 и PostgreSQL
2. Провести предварительный анализ полученных данных
3. Детально проанализировать вакансии и понять в каких городах есть большее число вакансий и какие у вакансий заработные платы
4. Провести анализ работодателей и понять их потребности и проблемы
5. Предметно проанализировать какие вакансии из базы подходят для начинающего Data Scientist
6. Узнать о том, какие ключевые навыки выделяют работодатели в вакансиях
7. Получить список советов для соискателей и работодателей, по поиску работы/сотрудников на основании предоставленной информации

#### Используемые технологии и инструменты

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-%23ffffff.svg?style=for-the-badge)
![Psycopg2](https://img.shields.io/badge/psycopg2-%23fcd703.svg?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-%23636970.svg?style=for-the-badge)

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

<br/>

### Проект №3. Анализ отзывов отелей с Booking

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/1_personal_projects/project3.png" height=150 align="left"> 

Во время выполнения проекта мы представляем себя в роли дата-сайентиста компании Booking. Одна из проблем компании - это отели, которые накручивают себе ретинг. Наша задача - создать модель машинного обучения, которая будет предсказывать рейтинг отеля. В том случае, если значение предсказания и реальной оценки будут сильно отличаться мы будем считать, что отель накрутил себе отзыв. В наших руках данные об отелях, а именно: адрес, дата рецензии, название отеля, страна рецензента, тексты позитивного и негативного отзыва, и.т.д. Всего 17 критериев.

#### План для достижения цели проекта

1. Считать данные, а также ознакомиться с тем, как должен выглядеть файл Submission
2. Объединить данные тестовой и тренировочной выборок, чтобы работать с одним массивом данных
3. Восстановить пустые значения широты и долготы отеля, используя библиотеку GeoPy
4. Проводим визуальный анализ полного массива данных
5. Проводим разведывательный анализ данных с помощью Sklearn
6. Переводим категориальные признаки в числовые
7. Из текста негативного и позитивного отзыва получаем негативный и позитивный окрас оценки с помощью NLP (библиотека NLTK)
8. Строим матрицу корреляций признаков и отбираем необходимые нам
9. Предсказываем оценки отелей и стремимся свести метрику MAPE к значению менее 13%.

#### Используемые технологии и инструменты

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

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#персональные-проекты)

<br/>
<br/>
<br/>

## Проекты с хакатонов

### Хакатон №1. ML TalentMatch

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/2_hackathon_projects/hackaton1.jpg" height=150 align="left"> 

Разработать и реализовать алгоритм, который будет разбивать информацию, содержащуюся в резюме кандидата по смысловым блокам: образование, опыт работы, навыки и т.д. На выходе должен быть структурированный JSON.Данные предоставляются в виде структурированных резюме кандидатов в произвольном виде (word, pdf…).

#### План для достижения цели проекта

1.
2.
3.
4.
5.

#### Используемые технологии и инструменты

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-%23bf3a1d.svg?style=for-the-badge)
![DOCX](https://img.shields.io/badge/DOCX-%230084ff.svg?style=for-the-badge)

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проекты-с-хакатонов)

<br/>

### Хакатон №2. IT Purple Hack

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/2_hackathon_projects/hackaton2.jpg" height=150 align="left"> 

Text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text

#### План для достижения цели проекта

1.
2.
3.
4.
5.

#### Используемые технологии и инструменты

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проекты-с-хакатонов)

<br/>
<br/>

## Проекты с кейс-чемпионатов

### Кейс-чемпионат №1. Axenix Business Cup

#### Краткое описание проекта

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/3_case_championships_projects/case_projects1.jpg" height=150 align="left"> 

Text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text-text

#### План для достижения цели проекта

1.
2.
3.
4.
5.

#### Используемые технологии и инструменты

##### 1-й этап

![Microsoft Word](https://img.shields.io/badge/Microsoft_Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white)
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)


##### 2-й этап (полуфинал)

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Microsoft Word](https://img.shields.io/badge/Microsoft_Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white)
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Miro](https://img.shields.io/badge/Miro-050038?style=for-the-badge&logo=Miro&logoColor=white)

#### Дополнительно

Ссылка на весь проект целиком - [здесь]()

:arrow_up: [к оглавлению](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проекты-с-кейс-чемпионатов)





Дата последнего обновления раздела - 08.03.2024<br>
Макет, написание кода и оформление - Артур Артиков

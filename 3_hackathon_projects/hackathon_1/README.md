# ML TalentMatch

## Запуск проекта
```
sudo docker build --no-cache -t resume_parser .
sudo docker run -d --name resume_parser -p 80:80 resume_parser

```

<br/>

## Краткое описание

<img src="https://github.com/ArturArtikov/Portfolio/blob/main/1_media/2_hackathon_projects/hackathon1.jpg" height=200 align="left"> 

**Кейс:** Алгоритм для структурирования информации в резюме кандидатов

**Задача:**  Разработать и реализовать алгоритм, который будет разбивать информацию, содержащуюся в резюме кандидата по смысловым блокам

**Организаторы:** SENSE Group & Акселератор Возможностей МГУ

**Результат:** Модель, выделяющая данные об имени, возрасте, образовании, опыте работы соискателя по его резюме в формате DOC, DOCX или PDF

**Сфера применения:** найм сотрудников и HR услуги

<br/>

## Входные данные

**106 резюме соискателей** с разным форматированием в формате PDF

**100 резюме соискателей** с разным форматированием в формате DOCX и DOC

_Файлы резюме скрыты по требованию правообладателя_

<br/>

## Этапы работы над проектом

1. Получили данные резюме в файлах разных форматов
2. Создали парсер для сбора данных из резюме в PDF
3. Создали парсер для сбора данных из резюме в DOCX
4. Обработали DOC-файл с резюме
5. Объединили полученные данные в таблицу в CSV формате
6. Соединили парсеры в единый скрипт
7. Написали регулярные выражения для получения данных номеров телефонов, электронных почт и имен участников
8. Провели работу с блоками данных в резюме
9. Выделили опыт работы и образование в резюме соискателей
10. Создали скрипт для перевода собранных данных в формат JSON
11. Собрали данные в контейнер Docker
12. Объединили и связали между собой скрипты и добавили в Docker
13. Создали презентацию защиты
14. Защитили презентацию и решение

<br/>

## Сроки и результаты

Сроки: 28.02.2024 - 01.03.2024

Результат: скрипт, воспринимающий более 50% данных из резюме соискателей

Возможные улучшения: использование NLP-технологий, замена PyPDF2 на PDFMiner, более глубокая очистка данных

Итог: 8-е место по сумме решения, реализации и защиты

Дополнительно: [сертификат участника](https://github.com/ArturArtikov/Portfolio/blob/main/1_media/4_certificates/ML%20TalentMatch%20-%202024.%20%D0%A1%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%20%D1%83%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%90%D1%80%D1%82%D1%83%D1%80%20%D0%90%D1%80%D1%82%D0%B8%D0%BA%D0%BE%D0%B2.pdf)

<br/>

## Командный состав

Команда: __*Digital Fintech Warriors*__

Список участников команды:

* [Руслан Кондрашук](https://github.com/GoodchildTrevor): Капитан | Data Analysts | Project Manager
* [Артур Артиков](https://github.com/ArturArtikov): Участник | Data Analysts | Data Scientist
* [Григорий Мацнев](https://github.com/PE51K): Участник | Backend Developer | Data Scientist
* [Александр Струнский](https://github.com/AlexStr94): Участник | Backend Developer

<br/>

## Используемый стек и технологии

![Google Colaboratory](https://img.shields.io/badge/Google%20Colaboratory-ffffff.svg?style=for-the-badge&logo=google-colab&logoColor=orange)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-%23bf3a1d.svg?style=for-the-badge)
![DOCX](https://img.shields.io/badge/DOCX-%230084ff.svg?style=for-the-badge)
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)


[Главная страница портфолио](https://github.com/ArturArtikov/Portfolio/blob/main/README.md#проекты-с-хакатонов)
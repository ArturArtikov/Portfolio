FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt \
    && python -m spacy download en_core_web_sm \
    && python -m nltk.downloader words \
    && python -m nltk.downloader stopwords

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
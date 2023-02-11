FROM python:3.8

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /code/

ENV PYTHONNUNBUFFERED 1

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
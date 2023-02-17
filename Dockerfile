FROM python

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code/

ENV PYTHONNUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

RUN cd /code/wedev

CMD python manage.py runserver 0.0.0.0:8000
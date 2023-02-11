FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

WORKDIR /app

COPY wedev/Pipfile .
RUN pip install --upgrade pip && pip install -r requirements.txt
#RUN python -m pip install --upgrade pip
#RUN pip install pipenv && pipenv shell

COPY wedev .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
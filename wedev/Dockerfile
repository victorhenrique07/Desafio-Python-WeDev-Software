FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recomends \
        postgresql-client

WORKDIR /usr/src/app
COPY Pipfile .
RUN pip install pipenv && pipenv sync
COPY . .
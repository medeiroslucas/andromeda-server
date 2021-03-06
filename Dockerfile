FROM python:3.8.10

RUN apt-get update

WORKDIR /home

RUN pip install poetry==1.1.11

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry update
RUN poetry install
RUN poetry lock

COPY app/ app/
COPY server.py server.py
COPY settings.py settings.py
COPY utils.py utils.py
COPY astro.json astro.json

CMD waitress-serve --call --port=$PORT 'app:create_app'
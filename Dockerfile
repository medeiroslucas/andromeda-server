FROM python:3.7

RUN apt-get update

WORKDIR /home

RUN pip install poetry==1.1.10

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry update
RUN poetry install
RUN poetry lock

COPY app/ app/
COPY server.py server.py

CMD python server.py
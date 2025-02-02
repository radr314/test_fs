FROM python:3.10

RUN pip install poetry
RUN mkdir -p /home/src

COPY ./static /home/src/static
COPY ./templates /home/src/templates
COPY ./app.py /home/src/app.py
COPY ./poetry.lock /home/src/poetry.lock
COPY ./pyproject.toml /home/src/pyproject.toml

WORKDIR /home/src

RUN poetry install

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

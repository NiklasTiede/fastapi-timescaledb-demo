FROM python:3.11.4-alpine

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --clear

COPY . /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]

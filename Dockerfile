FROM python:3.11.2-alpine3.17
WORKDIR /app

RUN apk update
RUN pip install --no-cache-dir poetry==1.3.2

COPY poetry.lock pyproject.toml ./

RUN poetry env use python3 \
    && poetry install

COPY user_storage user_storage

ENTRYPOINT ["poetry", "run", "uvicorn", "user_storage.__main__:API", "--host", "0.0.0.0", "--port", "8000"]

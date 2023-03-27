FROM docker.io/python:alpine3.17

WORKDIR /app

COPY [ "./", "./" ]

RUN apk add --no-cache poetry \
    && poetry install

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]

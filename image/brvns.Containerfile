FROM python:alpine3.16

WORKDIR /app

COPY [ "./", "./" ]

RUN apk add --no-cache poetry \
    && poetry install

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]

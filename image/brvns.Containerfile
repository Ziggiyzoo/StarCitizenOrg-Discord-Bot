FROM python:alpine3.16
ARG TOKEN

RUN apk add --no-cache poetry

WORKDIR /app

COPY [ "./", "./" ]

RUN poetry install

ENV TOKEN=${TOKEN}

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]

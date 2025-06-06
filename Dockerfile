# Imagem leve com Python
FROM python:3.12-alpine

RUN apk update && apk add --no-cache \
    bash \
    curl \
    vim \
    git \
    coreutils \
    grep \
    sed \
    util-linux \
    procps \
    shadow \
    build-base \
    python3-dev \
    py3-pip

WORKDIR /app


COPY . /app


CMD ["tail", "-f", "/dev/null"]



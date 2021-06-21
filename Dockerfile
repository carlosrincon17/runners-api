FROM python:3.9-alpine

COPY . /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6 \
  CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk update && apk add libpq

RUN apk add --no-cache --virtual .build-deps \ 
  gcc \
  musl-dev \
  libffi-dev \
  openssl-dev \
  python3-dev \
  rust \
  postgresql-dev \
  postgresql-libs \
  libressl-dev

RUN python3.9 -m venv /env && . /env/bin/activate
RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"


WORKDIR /app
COPY pyproject.toml /app/


RUN poetry install --no-dev
RUN apk del .build-deps gcc musl-dev
EXPOSE 8000
CMD ["poetry", "run", "python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
FROM python:3.9.0-alpine
WORKDIR /usr/src/app
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

# Production Dockerfile for Daily AI Preparation Platform
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

RUN mkdir -p data backups logs

VOLUME ["/app/data", "/app/backups", "/app/logs"]

ENTRYPOINT ["python", "-m", "app.main"]

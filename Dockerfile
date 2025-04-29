FROM python:3.13-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir fastapi motor pydantic uvicorn

COPY log_conf.json .

COPY src src

RUN chown -R appuser:appgroup /app

USER appuser

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-config", "log_conf.json"]
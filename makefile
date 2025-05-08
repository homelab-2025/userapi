.PHONY: install run cup cdown tests clean
.DEFAULT_GOAL := run

HOST = '0.0.0.0'
PORT = '8000'


install:
	uv sync
	
run:
	uv run uvicorn src.main:app --reload --host ${HOST} --port ${PORT} --log-config log_conf.json

cup:
	docker compose up -d

cdown:
	docker compose down

tests:
	uv run pytest

clean:
	rm -rf .venv

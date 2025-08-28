SHELL := /bin/bash
PY := 3.10

.PHONY: create-venv remove-venv precommit fmt lint test

create-venv:
	@echo "START: Creating .venv with uv (Python $(PY))" && \
	uv venv --python $(PY) && \
	uv sync && \
	uv run pre-commit install

remove-venv:
	@echo "START: removing .venv and lock" && \
	rm -rf .venv uv.lock

precommit:
	uv run pre-commit run -a

fmt:
	uv run isort .
	uv run black .

lint:
	uv run flake8 .

test:
	uv run pytest

requirements_txt:
	uv export

lock:
	uv lock

SHELL := /bin/bash
PY := 3.10

.PHONY: create-venv remove-venv precommit fmt lint test

create-venv:
	@echo "START: Creating .venv with uv (Python $(PY))" && \
	uv venv jet-env --python $(PY) && \
	uv sync && \
	uv run pre-commit install

remove:
	@echo "START: removing .venv and lock" && \
	rm -rf .venv uv.lock dist/

precommit:
	uv run pre-commit run -a

fmt:
	uv run isort .
	uv run black .

lint:
	uv run flake8 .

test:
	uv run pytest

rqts_txt:
	uv export --no-hashes  > requirements.txt

lock:
	uv lock
dev-install:
	uv pip install -e .

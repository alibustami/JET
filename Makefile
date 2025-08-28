SHELL := /bin/bash

.ONE_SHELL:
create-venv:
	@echo "START: Creating jet-env virtual environment" && \
	conda create -n jet-env python=3.10 -y && \
	conda run -n jet-env python -m pip install --upgrade pip && \
	conda run -n jet-env python -m pip install --upgrade setuptools wheel && \
	conda run -n jet-env pip install -e . && \
	conda run -n jet-env pre-commit install

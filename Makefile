SHELL := /bin/bash
PY := 3.10
VENV_DIR ?= jet-env

export UV_PROJECT_ENVIRONMENT := $(CURDIR)/$(VENV_DIR)

.PHONY: create-venv remove-venv precommit fmt lint test

create-venv:
	@echo "START: Creating .venv with uv (Python $(PY))" ; \
	export UV_PROJECT_ENVIRONMENT="jet-env" ; \
	uv venv jet-env --python $(PY) --system-site-packages ; \
	uv sync ; \
	uv run pre-commit install ; \
	wget https://pypi.jetson-ai-lab.io/jp6/cu126/+f/62a/1beee9f2f1470/torch-2.8.0-cp310-cp310-linux_aarch64.whl\#sha256\=62a1beee9f2f147076a974d2942c90060c12771c94740830327cae705b2595fc ; \
	wget https://pypi.jetson-ai-lab.io/jp6/cu126/+f/907/c4c1933789645/torchvision-0.23.0-cp310-cp310-linux_aarch64.whl\#sha256\=907c4c1933789645ebb20dd9181d40f8647978e6bd30086ae7b01febb937d2d1 ; \
	wget https://pypi.jetson-ai-lab.io/jp6/cu126/+f/4eb/e6a8902dc7708/onnxruntime_gpu-1.23.0-cp310-cp310-linux_aarch64.whl#sha256=4ebe6a8902dc7708434b2e1541b3fe629ebf434e16ab5537d1d6a622b42c622b ; \
	uv pip uninstall numpy torch torchvision ; \
	uv pip install --upgrade "numpy<2" pip setuptools wheel ; \
	uv pip install torch-2.8.0-cp310-cp310-linux_aarch64.whl torchvision-0.23.0-cp310-cp310-linux_aarch64.whl onnxruntime_gpu-1.23.0-cp310-cp310-linux_aarch64.whl

install-dataset:
	@echo "START: installing dataset" ; \
	uv pip install lvis ; \
	cd data ; \
	if [ ! -f lvis_v1_val.json.zip ]; then \
		echo "downloading lvis_v1_val.json.zip..." ; \
		wget https://dl.fbaipublicfiles.com/LVIS/lvis_v1_val.json.zip ; \
	else \
		echo "lvis_v1_val.json.zip already exists." ; \
	fi ; \
	if [ ! -f lvis_v1_val.json ]; then \
		echo "extracting lvis_v1_val.json..." ; \
		unzip lvis_v1_val.json.zip -d . ; \
	else \
		echo "lvis_v1_val.json already exists." ; \
	fi ; \
	if [ ! -f val2017.zip ]; then \
		echo "downloading val2017.zip..." ; \
		cd data ; \
		wget http://images.cocodataset.org/zips/val2017.zip ; \
	else \
		echo "val2017.zip already exists." ; \
	fi ; \
	if [ ! -d val2017 ]; then \
		echo "extracting val2017..." ; \
		unzip -q val2017.zip -d . ; \
	else \
		echo "val2017 already exists." ; \
	fi ; \
	rm -rf val2017.zip lvis_v1_val.json.zip

remove:
	@echo "START: removing .venv and lock" && \
	rm -rf .venv uv.lock dist/ jet-env/

precommit:
	uv run pre-commit run -a

rqts_txt:
	uv export --no-hashes  > requirements.txt

lock:
	uv lock

dev-install:
	uv pip install -e .

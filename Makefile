

deps:
	python -m pip install -r ./requirements/prod.txt

deps-dev:
	python -m pip install -r ./requirements/dev.txt

test:
	python -m pytest -n auto

cover:
	python -m pytest --cov . -n auto

lint:
	python -m mypy --config-file mypy.ini
	python -m pylint --recursive=y $(CURDIR)

APP_PORT ?= 8000
start:
	python -m uvicorn main:app --host 0.0.0.0 --port "$(APP_PORT)"

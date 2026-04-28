.PHONY: bootstrap install install-dev run run-school watch scan seed test compile clean

bootstrap:
	bash scripts/bootstrap.sh

install:
	python -m pip install -e .

install-dev:
	python -m pip install -e .[dev]

run:
	python -m last_dices_terminal_school.main

run-school:
	bash scripts/run_school.sh

watch:
	python -m last_dices_terminal_school.watch_imports

scan:
	bash scripts/scan_imports.sh

seed:
	python -m last_dices_terminal_school.setup_seed

test:
	pytest -q

compile:
	python -m compileall src tests

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

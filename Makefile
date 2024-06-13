.PHONY: style format

.DEFAULT_GOAL := all

style:
	ruff format

quality:
	ruff check

pre-commit:
	pre-commit run --all-files

all: style quality

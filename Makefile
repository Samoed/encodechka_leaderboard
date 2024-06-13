.PHONY: style format

.DEFAULT_GOAL := all

style:
	ruff format
	pre-commit run --all-files


quality:
	ruff check

all: style quality

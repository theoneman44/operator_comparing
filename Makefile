ifneq (,$(wildcard env))
	$(info Found env file.)
	include env
	export
endif

style:
	flake8 .

types:
	mypy webapp

tests:
	pytest

check:
	make style types tests

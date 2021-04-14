.PHONY: test test_regen

test:
	pytest -s

test_regen:
	pytest -s --force-regen

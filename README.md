# pytest-alt-reg

A pytest plugin to create regression tests for Altair charts.

## References

- [pytest-regressions](https://github.com/ESSS/pytest-regressions) plugin.
- [pytest-datadir](https://github.com/gabrielcnr/pytest-datadir) plugin.
- [cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) template.

## Development

- `poetry install`.

## Notes

- `poetry add pytest@^3.5.0`.
- `pytest -s tests` (show the prints).
- [jsondiff](https://github.com/xlwings/jsondiff) package (by xlwings).
- pytest:
  - [Temporary directories and files](https://docs.pytest.org/en/stable/tmpdir.html) (`tmpdir` fixture).
  - [\_\_tracebackhide\_\_ does not work with chained exceptions](https://github.com/pytest-dev/pytest/issues/1904) (open) issue.
- [altair_recipes](https://github.com/piccolbo/altair_recipes):
  - `regtest.write(alt.Chart.from_dict(round_floats(plot.to_dict(), 13)).to_json())`.
- [Boltons](https://github.com/mahmoud/boltons) (utility package).
- Miguel Brito's [The Best Way to Compare Two Dictionaries in Python](https://miguendes.me/the-best-way-to-compare-two-dictionaries-in-python) blog post:
  - [DeepDiff](https://github.com/seperman/deepdiff) package (it returns a dictionary with values changed from one dictionary to another, for example).
  - [Dictdiffer](https://github.com/inveniosoftware/dictdiffer) package.

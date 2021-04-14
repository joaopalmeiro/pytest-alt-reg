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
- [altair_recipes](https://github.com/piccolbo/altair_recipes):
  - `regtest.write(alt.Chart.from_dict(round_floats(plot.to_dict(), 13)).to_json())`.
- [Boltons](https://github.com/mahmoud/boltons) (utility package).

import re

import pytest

from .utils import json_loader, make_location_message


def check_spec_files(obtained_filename, expected_filename):
    obtained_spec = json_loader(obtained_filename)
    expected_spec = json_loader(expected_filename)

    if obtained_spec != expected_spec:
        raise AssertionError()


def perform_regression_check(
    datadir, request, dump_fn, extension, force_regen=False,
):
    __tracebackhide__ = True

    basename = re.sub(r"[\W]", "_", request.node.name)
    filename = datadir / (basename + extension)

    force_regen = force_regen or request.config.getoption("force_regen")

    if not filename.is_file():
        filename.parent.mkdir(parents=True, exist_ok=True)

        dump_fn(filename)

        msg = make_location_message(
            "File not found in the data directory. Created:", filename
        )
        pytest.fail(msg)
    else:
        obtained_filename = filename.with_suffix(".obtained" + extension)

        dump_fn(obtained_filename)

        try:
            check_spec_files(obtained_filename, filename)
        except AssertionError:
            raise
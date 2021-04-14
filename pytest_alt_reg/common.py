import re

import pytest

from .constants import TO_BE_COMPARED_SUFFIX
from .utils import json_loader, make_location_message


def check_spec_files(obtained_filename, expected_filename):
    __tracebackhide__ = True

    obtained_spec = json_loader(obtained_filename)
    expected_spec = json_loader(expected_filename)

    if obtained_spec != expected_spec:
        raise AssertionError()


def perform_regression_check(
    datadir, request, dump_fn, extension,
):
    __tracebackhide__ = True

    basename = re.sub(r"[\W]", "_", request.node.name)
    filename = datadir / (basename + extension)

    force_regen = request.config.getoption("force_regen")
    # print(force_regen)

    if not filename.is_file():
        filename.parent.mkdir(parents=True, exist_ok=True)

        dump_fn(filename)

        msg = make_location_message(
            "Spec not found in the respective data directory. Baseline created at:",
            filename,
        )
        pytest.fail(msg)
    else:
        obtained_filename = filename.with_suffix(f"{TO_BE_COMPARED_SUFFIX}{extension}")

        dump_fn(obtained_filename)

        try:
            check_spec_files(obtained_filename, filename)
        except AssertionError:
            if force_regen:
                dump_fn(filename)

                msg = make_location_message(
                    "Specs differ and --force-regen is set. Baseline recreated at:",
                    filename,
                )
                pytest.fail(msg)
            else:
                raise

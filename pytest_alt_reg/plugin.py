import os
from pathlib import Path

import pytest

from .chart_regression import ChartRegressionFixture


def pytest_addoption(parser):
    group = parser.getgroup("alt-reg")
    group.addoption(
        "--force-regen",
        action="store_true",
        default=False,
        help="Regenerate all chart_regression fixture data files.",
    )


# Source: pytest-datadir (https://github.com/gabrielcnr/pytest-datadir) plugin.
@pytest.fixture
def datadir(request):
    return Path(os.path.splitext(request.module.__file__)[0])


@pytest.fixture
def chart_regression(datadir, request):
    return ChartRegressionFixture(datadir, request)

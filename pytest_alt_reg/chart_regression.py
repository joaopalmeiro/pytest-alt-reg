from functools import partial

from .common import perform_regression_check
from .constants import JSON_EXTENSION
from .utils import altair_dumper


class ChartRegressionFixture:
    def __init__(self, datadir, request):
        self.request = request
        self.datadir = datadir

    def check(self, chart):
        __tracebackhide__ = True

        perform_regression_check(
            datadir=self.datadir,
            request=self.request,
            dump_fn=partial(altair_dumper, chart=chart),
            extension=JSON_EXTENSION,
        )

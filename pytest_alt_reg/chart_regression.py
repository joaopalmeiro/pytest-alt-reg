import json

from .common import perform_regression_check


class ChartRegressionFixture:
    def __init__(self, datadir, request):
        self.request = request
        self.datadir = datadir
        self.force_regen = False

    def check(self, chart):
        __tracebackhide__ = True

        def dump(filename):
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(chart, f, ensure_ascii=False, indent=4)

        perform_regression_check(
            datadir=self.datadir,
            request=self.request,
            dump_fn=dump,
            extension=".json",
            force_regen=self.force_regen,
        )

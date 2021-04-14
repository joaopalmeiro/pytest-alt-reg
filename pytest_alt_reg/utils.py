import json

from .constants import JSON_INDENT


def make_location_message(banner, filename):
    msg = [banner, f"- {filename}"]
    return "\n".join(msg)


def json_loader(filename):
    with open(filename) as file:
        data = json.load(file)

    return data


# More info:
# - https://github.com/altair-viz/altair/blob/master/tools/schemapi/schemapi.py#L340
def altair_dumper(filename, chart):
    chart_spec = chart.to_json(indent=JSON_INDENT, sort_keys=False)

    with open(filename, "w", encoding="utf-8") as file:
        # json.dump(chart_spec, file, indent=JSON_INDENT, sort_keys=False)
        file.write(chart_spec)

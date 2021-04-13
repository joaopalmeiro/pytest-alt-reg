import json


def make_location_message(banner, filename):
    msg = [banner, f"- {filename}"]
    return "\n".join(msg)


def json_loader(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    return data

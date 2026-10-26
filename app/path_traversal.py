from flask import request


def read_file():
    """TRUE POSITIVE: user-controlled path opened with no sanitisation."""
    name = request.args.get("file")
    with open("/var/data/" + name) as fh:
        return fh.read()

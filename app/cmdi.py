import os

from flask import request


def ping():
    """TRUE POSITIVE: user-controlled host passed to a shell."""
    host = request.args.get("host")
    os.system("ping -c 1 " + host)

import requests
from flask import request


def fetch():
    """TRUE POSITIVE: server fetches a URL fully controlled by the user."""
    url = request.args.get("url")
    return requests.get(url, timeout=5).text

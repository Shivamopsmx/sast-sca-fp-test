import pickle

import yaml
from flask import request


def load_profile():
    """TRUE POSITIVE: untrusted data deserialized without safe loaders."""
    blob = request.get_data()
    data = yaml.load(blob, Loader=yaml.Loader)
    return pickle.loads(blob), data

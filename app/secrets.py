# TRUE POSITIVE: hardcoded credential checked into source.
DB_PASSWORD = "S3cr3t-Pass-123"


def connect_string():
    return "postgresql://admin:%s@db.internal:5432/app" % DB_PASSWORD

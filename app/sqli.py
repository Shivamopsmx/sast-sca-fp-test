import sqlite3

from flask import request


def get_user():
    """TRUE POSITIVE: user input is concatenated straight into the SQL string."""
    name = request.args.get("name")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '%s'" % name
    cur.execute(query)
    return cur.fetchall()

#!/usr/bin/python3
"""
select all in states where name matches arg
"""

import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        charset="utf8",
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM states
        WHERE BINARY name=%(state)s
        ORDER BY id ASC
        """,
        {"state": sys.argv[4]},
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

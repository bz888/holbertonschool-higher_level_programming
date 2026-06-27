#!/usr/bin/python3
"""
select all in states where name matches arg
"""

import MySQLdb
import sys

if __name__ == "__main__":

    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    cur = conn.cursor()

    cur.execute(
        (
            "SELECT id, name "
            "FROM states "
            "WHERE BINARY name = '{}' "
            "ORDER BY id ASC"
        ).format(state_name)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

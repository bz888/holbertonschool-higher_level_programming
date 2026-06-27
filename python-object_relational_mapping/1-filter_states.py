#!/usr/bin/python3
"""
list all states with name starting with N
"""

import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT id, name "
        "FROM states "
        "WHERE name "
        "LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

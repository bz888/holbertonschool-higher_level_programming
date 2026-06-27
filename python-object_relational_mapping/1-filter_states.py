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

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name "
        "FROM states "
        "WHERE name "
        "LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

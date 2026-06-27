#!/usr/bin/python3
"""
takes name as arg, list all cities of that state
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
        SELECT cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name=%(state)s
        ORDER BY cities.id
    """,
        {"state": sys.argv[4]},
    )

    rows = cur.fetchall()

    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    cur.close()
    conn.close()

#!/usr/bin/python3
"""Module that query USA Cities from a database table"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name \
        FROM cities \
        LEFT JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC", (state,))
    query_rows = cur.fetchall()

    first = True
    for row in query_rows:
        for city in row:
            if not first:
                print(", ", end='')
            print(city, end="")
            first = False
    print()

    cur.close()
    conn.close()

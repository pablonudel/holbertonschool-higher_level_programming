#!/usr/bin/python3
"""Module that query USA States from a database table"""
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
    cur.execute("SELECT * FROM states \
        WHERE name = %s ORDER BY id ASC", (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

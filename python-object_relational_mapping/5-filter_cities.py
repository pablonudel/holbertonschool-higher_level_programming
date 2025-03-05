#!/usr/bin/python3
"""Module that query USA Cities from a database table"""
import MySQLdb
import sys


def query_states(mysql_username, mysql_password, database, state):
    """Access to database table for listing the all cities with states"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=mysql_username,
                               passwd=mysql_password,
                               db=database,
                               charset="utf8")
        cur = conn.cursor()
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
    except MySQLdb.Error as e:
        print(f"MySQL error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    """Main execution method"""
    if len(sys.argv) != 5:
        print(f"Usage: {format(sys.argv[0])} \
<mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    query_states(mysql_username, mysql_password, database, state)

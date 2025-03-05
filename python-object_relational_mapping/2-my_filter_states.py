#!/usr/bin/python3
"""Module that query USA States from a database table"""
import MySQLdb
import sys


def query_states(mysql_username, mysql_password, database, state):
    """Access to database for listing the states
    filter by state name"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=mysql_username,
                               passwd=mysql_password,
                               db=database,
                               charset="utf8")
        cur = conn.cursor()

        cur.execute("SELECT * FROM states \
            WHERE name = '{}' ORDER BY id ASC".format(state))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
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
<mysql_username> <mysql_password> <database_name> <State>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    query_states(mysql_username, mysql_password, database, state)

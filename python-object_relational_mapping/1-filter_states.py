#!/usr/bin/python3
"""filter_states lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE
                   BINARY 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()

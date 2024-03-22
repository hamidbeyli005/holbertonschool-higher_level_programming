#!/usr/bin/python3
"""
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host='localhost', port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db_connection.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY id""".format(argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

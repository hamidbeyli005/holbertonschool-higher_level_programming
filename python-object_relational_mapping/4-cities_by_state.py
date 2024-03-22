#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        sys.exit('Use: 4-cities_by_state.py <mysql username> <mysql password>'
                 ' <database name>')
    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    query = """SELECT cities.id as id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY id"""
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connection.close()

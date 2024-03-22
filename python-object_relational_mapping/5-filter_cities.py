#!/usr/bin/python3

"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    
    if len(sys.argv) != 5:
        sys.exit('Use: 5-filter_cities.py <mysql username> <mysql password>'
                 ' <database name> <state name searched>')
    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    query = """SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id"""
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db_connection.close()
#!/usr/bin/python3
"""
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    
    if len(sys.argv) != 5:
        sys.exit('Use: 1-filter_states.py <mysql username> <mysql password>'
                 ' <database name> <state name searched>')
        
    db_connection = MySQLdb.connect(host='localhost', port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db_connection.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY %s
                ORDER BY id"""
    cursor.execute(query, (sys.argv[4],))


    rows = cursor.fetchall()
    for row in rows:
        print(row)
#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


from sys import argv, exit
import MySQLdb

if __name__ == "__main__":
    for i in range(1, len(argv)):
        for c in argv[i]:
            if c in "; ":
                exit()
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id=states.id ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()

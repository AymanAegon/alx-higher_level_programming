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
    a = "SELECT cities.id, cities.name, states.name FROM cities, states"
    b = " WHERE cities.state_id=states.id ORDER BY cities.id ASC"
    cursor.execute(a + b)
    rows = cursor.fetchall()
    x = False
    for row in rows:
        if row[2] == argv[4]:
            if x:
                print(", {}".format(row[1]), end="")
            else:
                print(row[1], end="")
                x = True
    print()
    cursor.close()
    db.close()

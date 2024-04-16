#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    # and connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    #Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()

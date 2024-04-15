#!/usr/bin/python3
""" Scripts lists all states from the database hbtn_0e_0_usa  and
takes in 3 arguments: mysql username, mysql password and database name
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

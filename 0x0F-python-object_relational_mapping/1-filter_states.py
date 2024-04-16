#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    # Connect MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.connect()

    #Execute the SQL query to retrieve all states sorted by id
    c.execute("SELECT * FROM 'states' ORDER BY 'id'")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access the database and get the states from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], state_name=argv[4])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s LIKE BINARY ORDER \
                BY id ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

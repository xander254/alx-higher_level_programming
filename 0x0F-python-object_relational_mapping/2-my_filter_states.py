#!/usr/bin/python3
""" Display all states using state id """
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    word = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, ('%' + word + '%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

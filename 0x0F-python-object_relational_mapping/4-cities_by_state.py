#!/usr/bin/python3
""" Display all states using state id """
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

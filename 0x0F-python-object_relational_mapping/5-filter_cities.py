#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)

    cur = db.cursor()

    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    cur.execute(query, (state_name,))

    cities = cur.fetchall()
    if cities:
        print(", ".join([city[0] for city in cities]))
    else:
        print()

    cur.close()
    db.close()

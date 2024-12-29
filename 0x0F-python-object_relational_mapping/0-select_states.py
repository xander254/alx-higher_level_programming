#!/usr/bin/python3
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     passwd=password,
                     db=dbname)
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

for row in cur.fetchall():
    print(row)

db.close()

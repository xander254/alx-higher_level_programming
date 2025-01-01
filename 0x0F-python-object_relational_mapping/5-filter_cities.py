#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cur = db.cursor()

        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC;
        """

        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        print(", ".join([row[0] for row in rows]))

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

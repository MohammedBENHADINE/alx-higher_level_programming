#!/usr/bin/python3
"""script that lists all states with a name
starting with N (upper N) from the database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name REGEXP '^N' \
                 ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cur.close()
    db.close()
